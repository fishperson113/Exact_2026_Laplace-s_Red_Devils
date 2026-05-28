"""Stage 1: Load trained FOL model tu HF Hub va sinh premises_fol tu NL.

Input:  list[str] premises NL
Output: list[str] premises FOL

Duoc import boi: pipeline.py
Import tu:       data.prompts (SYSTEM_PROMPT_FOL_SFT, USER_TEMPLATE_FOL_SFT)
"""
from __future__ import annotations

import json
import re

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from data.prompts import (
    SYSTEM_PROMPT_FOL_SFT,
    USER_TEMPLATE_FOL_SFT,
    format_nl_block_numbered,
)

from .config import FOLz3Config


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
            load_kwargs["load_in_8bit"] = True

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
