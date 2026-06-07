"""
pipeline/fol_model.py
---------------------
Stage 1: Load FOL model từ HF Hub, nhận NL premises → sinh FOL premises.
"""
from __future__ import annotations

import json
import re

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

from prompts import SYSTEM_PROMPT_FOL, USER_TEMPLATE_FOL, format_nl_block


class FOLModel:
    """Load merged FOL model từ HF Hub và dịch NL → FOL."""

    def __init__(self, hub_repo_id: str, load_in_8bit: bool = True):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"[FOL] Loading: {hub_repo_id}")

        load_kwargs: dict = {"trust_remote_code": True, "device_map": "auto"}
        if load_in_8bit and self.device == "cuda":
            load_kwargs["quantization_config"] = BitsAndBytesConfig(load_in_8bit=True)
        else:
            load_kwargs["torch_dtype"] = torch.bfloat16

        self.tokenizer = AutoTokenizer.from_pretrained(hub_repo_id, trust_remote_code=True)
        self.model     = AutoModelForCausalLM.from_pretrained(hub_repo_id, **load_kwargs)
        self.model.eval()
        print(f"[FOL] Loaded on {self.device}")

    def generate(self, premises_nl: list[str], max_new_tokens: int = 400) -> tuple[list[str], str]:
        """
        Input : premises_nl  — list NL premises
        Output: (fol_list, raw_output)
                fol_list   — list FOL strings đã parse
                raw_output — chuỗi raw từ model (để debug)
        """
        nl_block = format_nl_block(premises_nl)
        user_msg = USER_TEMPLATE_FOL.format(premises_nl=nl_block)

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT_FOL},
            {"role": "user",   "content": user_msg},
        ]
        # enable_thinking=False: model Qwen3.5 (thinking) được train với no-think →
        # BẮT BUỘC tắt khi inference, nếu không <think> ăn hết token budget và JSON bị cắt.
        try:
            text = self.tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True, enable_thinking=False
            )
        except TypeError:
            text = self.tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True
            )
        inputs = self.tokenizer(
            text, return_tensors="pt", truncation=True, max_length=3500
        ).to(self.model.device)

        with torch.no_grad():
            out = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=False,
                repetition_penalty=1.2,
            )
        raw = self.tokenizer.decode(
            out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True
        ).strip()

        return self._parse_fol(raw), raw

    # ── private ────────────────────────────────────────────────────────────────

    @staticmethod
    def _parse_fol(text: str) -> list[str]:
        """Parse JSON {"premises_fol": [...]} hoặc fallback line-by-line."""
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            try:
                parsed = json.loads(match.group())
                if "premises_fol" in parsed and isinstance(parsed["premises_fol"], list):
                    return [str(f).strip() for f in parsed["premises_fol"]]
            except json.JSONDecodeError:
                pass
        # Fallback: lấy các dòng có ký hiệu logic
        lines = []
        for line in text.split("\n"):
            line = line.strip().lstrip("0123456789.)-  ")
            if any(c in line for c in "∀∃→∧∨¬↔") or re.match(r"\w+\(", line):
                lines.append(line)
        return lines
