"""Stage 1: Load trained FOL model tu HF Hub va sinh FOL tu NL.

- generate(premises_nl)            → list[str] premises FOL
- generate_question_fol(q, pl)     → str question FOL (1 formula cho Z3 entailment)
- generate_options_fol(opts, pl)   → dict[str,str] MCQ options FOL {"A":"FOL",...}

Duoc import boi: pipeline.py
Import tu:       data.prompts (SYSTEM_PROMPT_FOL_SFT, USER_TEMPLATE_FOL_SFT)
"""
from __future__ import annotations

import json
import re

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

from data.prompts import (
    SYSTEM_PROMPT_FOL_SFT,
    USER_TEMPLATE_FOL_SFT,
    format_nl_block_numbered,
)

from .config import FOLz3Config
from .prompts import (
    SYSTEM_PROMPT_OPTIONS2FOL,
    SYSTEM_PROMPT_Q2FOL,
    USER_TEMPLATE_OPTIONS2FOL,
    USER_TEMPLATE_Q2FOL,
)


class FOLInference:
    """Load FOL model (merged tu Hub) va generate premises_fol."""

    def __init__(self, cfg: FOLz3Config):
        self.cfg = cfg
        self.device = self._resolve_device(cfg.device)
        print(f"[FOL] Loading model: {cfg.fol_hub_repo_id}")

        load_kwargs = {
            "trust_remote_code": cfg.trust_remote_code,
            "device_map": self.device,
        }
        if cfg.load_in_8bit:
            load_kwargs["quantization_config"] = BitsAndBytesConfig(load_in_8bit=True)

        self.tokenizer = AutoTokenizer.from_pretrained(
            cfg.fol_hub_repo_id, trust_remote_code=cfg.trust_remote_code
        )
        self.model = AutoModelForCausalLM.from_pretrained(
            cfg.fol_hub_repo_id, **load_kwargs
        )
        self.model.eval()
        print(f"[FOL] Model loaded on {self.device}")

    @staticmethod
    def _resolve_device(device: str) -> str:
        if device == "auto":
            return "cuda" if torch.cuda.is_available() else "cpu"
        return device

    def generate(self, premises_nl: list[str]) -> list[str]:
        """NL premises -> FOL premises (list[str])."""
        nl_block = format_nl_block_numbered(premises_nl)
        user_msg = USER_TEMPLATE_FOL_SFT.format(premises_nl=nl_block)

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT_FOL_SFT},
            {"role": "user", "content": user_msg},
        ]
        text = self.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = self.tokenizer(text, return_tensors="pt").to(self.model.device)

        with torch.no_grad():
            out = self.model.generate(
                **inputs,
                max_new_tokens=self.cfg.fol_max_new_tokens,
                do_sample=False,
                temperature=1.0,
            )

        generated = self.tokenizer.decode(
            out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True
        ).strip()

        return self._parse_fol_output(generated)

    def generate_question_fol(
        self, question: str, premises_fol: list[str]
    ) -> str:
        """Dich question NL thanh 1 FOL formula de Z3 check entailment.

        premises_fol duoc truyen vao de model biet dung chung predicate names.
        Tra ve "" neu khong parse duoc.
        """
        fol_block = "\n".join(f"{i}. {p}" for i, p in enumerate(premises_fol, 1))
        user_msg = USER_TEMPLATE_Q2FOL.format(
            premises_fol_block=fol_block,
            question=question,
        )
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT_Q2FOL},
            {"role": "user", "content": user_msg},
        ]
        text = self.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = self.tokenizer(text, return_tensors="pt").to(self.model.device)

        with torch.no_grad():
            out = self.model.generate(
                **inputs,
                max_new_tokens=128,   # question FOL = 1 formula, thuong ~20-50 tokens
                do_sample=False,
                temperature=1.0,
            )

        generated = self.tokenizer.decode(
            out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True
        ).strip()

        return self._parse_single_fol(generated)

    def generate_options_fol(
        self, options: dict[str, str], premises_fol: list[str]
    ) -> dict[str, str]:
        """Dich tat ca MCQ options thanh FOL trong 1 call duy nhat.

        options: {"A": "option text", "B": "option text", ...}
        Returns: {"A": "FOL_A", "B": "FOL_B", ...}
        """
        fol_block = "\n".join(f"{i}. {p}" for i, p in enumerate(premises_fol, 1))
        options_block = "\n".join(
            f"{label}. {options[label]}" for label in sorted(options)
        )
        user_msg = USER_TEMPLATE_OPTIONS2FOL.format(
            premises_fol_block=fol_block,
            options_block=options_block,
        )
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT_OPTIONS2FOL},
            {"role": "user", "content": user_msg},
        ]
        text = self.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = self.tokenizer(text, return_tensors="pt").to(self.model.device)

        with torch.no_grad():
            out = self.model.generate(
                **inputs,
                max_new_tokens=256,   # 4 FOL formulas, thuong ~80-150 tokens
                do_sample=False,
                temperature=1.0,
            )

        generated = self.tokenizer.decode(
            out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True
        ).strip()

        return self._parse_options_fol(generated, list(options.keys()))

    @staticmethod
    def _parse_single_fol(text: str) -> str:
        """Parse 1 FOL formula tu model output. Tra ve "" neu fail."""
        # Thu JSON {"question_fol": "..."}
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            parsed = json.loads(match.group())
            if "question_fol" in parsed:
                return str(parsed["question_fol"]).strip()

        # Fallback: lay dong dau tien co FOL syntax
        for line in text.split("\n"):
            line = line.strip().lstrip("0123456789.)-  ")
            if any(c in line for c in "∀∃→∧∨¬↔") or re.match(r"\w+\(", line):
                return line
        return ""

    @staticmethod
    def _parse_options_fol(text: str, labels: list[str]) -> dict[str, str]:
        """Parse JSON {"A":"FOL","B":"FOL",...} tu model output.

        Fallback: tra ve dict rong cho cac label khong parse duoc.
        """
        result = {label: "" for label in labels}
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            parsed = json.loads(match.group())
            for label in labels:
                if label in parsed:
                    result[label] = str(parsed[label]).strip()
        return result

    @staticmethod
    def _parse_fol_output(text: str) -> list[str]:
        """Parse JSON output {"premises_fol": [...]} tu model."""
        # Tim JSON object trong output
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            parsed = json.loads(match.group())
            if "premises_fol" in parsed and isinstance(parsed["premises_fol"], list):
                return [str(f).strip() for f in parsed["premises_fol"]]

        # Fallback: tach tung dong co FOL syntax
        lines = []
        for line in text.split("\n"):
            line = line.strip().lstrip("0123456789.)-  ")
            if any(c in line for c in "∀∃→∧∨¬↔") or re.match(r"\w+\(", line):
                lines.append(line)
        return lines
