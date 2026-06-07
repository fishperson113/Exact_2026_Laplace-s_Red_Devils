"""
pipeline/qa_model.py
--------------------
Stage 2: Load QA model (base + LoRA adapter) từ HF Hub,
nhận NL + FOL + question → sinh {"answer": "...", "explanation": "..."}.
"""
from __future__ import annotations

import json
import re

import torch
from peft import PeftConfig, PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

from prompts import SYSTEM_PROMPT_QA, USER_TEMPLATE_QA, format_nl_block, format_fol_block


class QAModel:
    """Load QA LoRA adapter từ HF Hub và sinh answer + explanation."""

    def __init__(self, hub_repo_id: str, load_in_8bit: bool = True):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"[QA] Loading adapter: {hub_repo_id}")

        load_kwargs: dict = {"trust_remote_code": True, "device_map": "auto"}
        if load_in_8bit and self.device == "cuda":
            load_kwargs["quantization_config"] = BitsAndBytesConfig(load_in_8bit=True)
        else:
            load_kwargs["torch_dtype"] = torch.bfloat16

        # Đọc base model từ adapter_config.json trên Hub
        peft_cfg       = PeftConfig.from_pretrained(hub_repo_id)
        base_model_id  = peft_cfg.base_model_name_or_path
        print(f"[QA] Base model: {base_model_id}")

        # Tokenizer + chat_template lấy TỪ repo adapter (final_lora) để dùng ĐÚNG
        # template lúc train; vocab giống base (LoRA không đổi tokenizer).
        self.tokenizer = AutoTokenizer.from_pretrained(hub_repo_id, trust_remote_code=True)
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        base  = AutoModelForCausalLM.from_pretrained(base_model_id, **load_kwargs)
        self.model = PeftModel.from_pretrained(base, hub_repo_id)
        self.model.eval()
        print(f"[QA] Loaded on {self.device}")

    def generate(
        self,
        premises_nl:  list[str],
        premises_fol: list[str],
        question:     str,
        max_new_tokens: int = 200,
    ) -> dict[str, str]:
        """
        Input : premises_nl, premises_fol, question
        Output: {"answer": "...", "explanation": "..."}
        """
        user_content = USER_TEMPLATE_QA.format(
            premises_nl_block  = format_nl_block(premises_nl),
            premises_fol_block = format_fol_block(premises_fol),
            question           = question,
        )
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT_QA},
            {"role": "user",   "content": user_content},
        ]
        # enable_thinking=False: khớp lúc train (no-think) → đầu ra là JSON thuần,
        # tránh <think> ăn token budget làm cắt JSON.
        try:
            text = self.tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True, enable_thinking=False
            )
        except TypeError:
            text = self.tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True
            )
        inputs = self.tokenizer(
            text, return_tensors="pt", truncation=True, max_length=4096
        ).to(self.model.device)

        with torch.no_grad():
            out = self.model.generate(
                **inputs, max_new_tokens=max_new_tokens, do_sample=False,
            )
        raw = self.tokenizer.decode(
            out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True
        ).strip()

        return self._parse_output(raw)

    # ── private ────────────────────────────────────────────────────────────────

    @staticmethod
    def _parse_output(text: str) -> dict[str, str]:
        """Parse JSON {"answer": ..., "explanation": ...} với fallback."""
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            try:
                parsed = json.loads(match.group())
                if "answer" in parsed:
                    return {
                        "answer":      str(parsed["answer"]).strip(),
                        "explanation": str(parsed.get("explanation", "")).strip(),
                    }
            except json.JSONDecodeError:
                pass
        # JSON cụt/lỗi: moi "answer": "..." (và explanation nếu có)
        m = re.search(r'"answer"\s*:\s*"([^"]+)"', text)
        if m:
            ans = m.group(1).strip()
            em = re.search(r'"explanation"\s*:\s*"(.*)', text, re.DOTALL)
            explanation = em.group(1).strip().rstrip('"}').strip() if em else ""
            return {"answer": ans, "explanation": explanation}
        # Last-resort: word-boundary + cue, KHÔNG đoán bừa chữ "A" trong văn xuôi
        m2 = re.search(
            r"(?:answer|final answer|đáp án|conclusion)\D{0,15}\b(Yes|No|Unknown|[ABCD])\b",
            text, re.I,
        )
        if m2:
            return {"answer": m2.group(1), "explanation": ""}
        for label in ("Unknown", "Yes", "No"):
            if re.search(rf"\b{label}\b", text):
                return {"answer": label, "explanation": ""}
        return {"answer": "Unknown", "explanation": ""}
