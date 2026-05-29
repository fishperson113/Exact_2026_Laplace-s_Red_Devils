"""Stage 3: Load base Qwen model va generate answer + explanation.

Input:  premises NL, premises FOL (tu Stage 1), Z3Result (tu Stage 2), question
Output: dict {answer, explanation}

Duoc import boi: pipeline.py
Import tu:       .prompts (SYSTEM_PROMPT_QA, USER_TEMPLATE_QA)
"""
from __future__ import annotations

import json
import re

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from .config import FOLz3Config
from .prompts import (
    SYSTEM_PROMPT_QA,
    SYSTEM_PROMPT_QA_BASELINE,
    USER_TEMPLATE_QA,
    USER_TEMPLATE_QA_BASELINE,
)
from .z3_solver import Z3Result


class QAInference:
    """Load base Qwen model va generate JSON {answer, explanation}."""

    def __init__(self, cfg: FOLz3Config):
        self.cfg = cfg
        self.device = self._resolve_device(cfg.device)
        print(f"[QA] Loading model: {cfg.qa_model_name}")

        load_kwargs = {
            "trust_remote_code": cfg.trust_remote_code,
            "device_map": self.device,
        }
        if cfg.load_in_8bit:
            load_kwargs["load_in_8bit"] = True

        self.tokenizer = AutoTokenizer.from_pretrained(
            cfg.qa_model_name, trust_remote_code=cfg.trust_remote_code
        )
        self.model = AutoModelForCausalLM.from_pretrained(
            cfg.qa_model_name, **load_kwargs
        )
        self.model.eval()
        print(f"[QA] Model loaded on {self.device}")

    @staticmethod
    def _resolve_device(device: str) -> str:
        if device == "auto":
            return "cuda" if torch.cuda.is_available() else "cpu"
        return device

    def generate(
        self,
        premises_nl: list[str],
        premises_fol: list[str],
        z3_result: Z3Result,
        question: str,
    ) -> dict:
        """Compose prompt tu FOL + Z3 output, generate JSON {answer, explanation}."""
        # Format premises blocks
        nl_block = "\n".join(f"{i}. {p}" for i, p in enumerate(premises_nl, 1))
        fol_block = "\n".join(f"{i}. {p}" for i, p in enumerate(premises_fol, 1))

        # Format Z3 model assignments
        if z3_result.conclusions:
            z3_conclusions = "; ".join(z3_result.conclusions)
        else:
            z3_conclusions = "(no ground terms)"

        user_msg = USER_TEMPLATE_QA.format(
            premises_nl_block=nl_block,
            premises_fol_block=fol_block,
            z3_status=z3_result.raw_status,
            z3_entailment=z3_result.entailment,
            z3_parsed_count=len(z3_result.premises_parsed),
            z3_total_count=len(z3_result.premises_parsed) + len(z3_result.premises_failed),
            z3_conclusions=z3_conclusions,
            question=question,
        )

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT_QA},
            {"role": "user", "content": user_msg},
        ]
        return self._call_model(messages)

    def generate_baseline(
        self,
        premises_nl: list[str],
        question: str,
    ) -> dict:
        """Baseline: chi NL premises, khong FOL/Z3 (dung khi use_fol=false)."""
        nl_block = "\n".join(f"{i}. {p}" for i, p in enumerate(premises_nl, 1))
        user_msg = USER_TEMPLATE_QA_BASELINE.format(
            premises_nl_block=nl_block,
            question=question,
        )
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT_QA_BASELINE},
            {"role": "user", "content": user_msg},
        ]
        return self._call_model(messages)

    def _call_model(self, messages: list[dict]) -> dict:
        """Shared: tokenize, generate, parse output."""
        text = self.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = self.tokenizer(text, return_tensors="pt").to(self.model.device)

        with torch.no_grad():
            out = self.model.generate(
                **inputs,
                max_new_tokens=self.cfg.qa_max_new_tokens,
                do_sample=False,
                temperature=1.0,
            )

        generated = self.tokenizer.decode(
            out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True
        ).strip()

        return self._parse_qa_output(generated)

    @staticmethod
    def _parse_qa_output(text: str) -> dict:
        """Parse JSON {"answer": "...", "explanation": "..."} tu model output."""
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            parsed = json.loads(match.group())
            if "answer" in parsed:
                return {
                    "answer": str(parsed["answer"]).strip(),
                    "explanation": str(parsed.get("explanation", "")).strip(),
                }

        # Fallback: tim answer label trong text
        for label in ("A", "B", "C", "D", "Yes", "No", "Unknown"):
            if label in text:
                return {"answer": label, "explanation": text}

        return {"answer": "Unknown", "explanation": text}
