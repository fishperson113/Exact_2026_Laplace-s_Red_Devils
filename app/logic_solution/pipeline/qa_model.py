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

    def __init__(
        self,
        hub_repo_id: str,
        load_in_8bit: bool = True,
        enable_thinking: bool = False,
        temperature: float = 0.6,
        top_p: float = 0.95,
        top_k: int = 20,
    ):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        # Chế độ B — native thinking: stage 2 sinh <think>…</think> CoT trước JSON.
        # Qwen3 think mode KHÔNG được greedy (lặp vô hạn) → bắt buộc sampling.
        self.enable_thinking = enable_thinking
        self.temperature = temperature
        self.top_p = top_p
        self.top_k = top_k
        print(f"[QA] Loading adapter: {hub_repo_id}  (thinking={enable_thinking})")

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
    ) -> dict:
        """
        Input : premises_nl, premises_fol, question
        Output: {"answer", "explanation", "reasoning": {"type", "steps"}, "thinking"}

        Khi enable_thinking=True (Chế độ B): model sinh <think>…</think> CoT trước,
        nội dung think trở thành reasoning.steps (type="cot"). JSON answer được
        parse SAU khi đã strip think → tránh dấu ngoặc trong think làm vỡ parser.
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
        try:
            text = self.tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True,
                enable_thinking=self.enable_thinking,
            )
        except TypeError:
            text = self.tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True
            )
        inputs = self.tokenizer(
            text, return_tensors="pt", truncation=True, max_length=4096
        ).to(self.model.device)

        # Sampling theo chế độ: think → sampling (Qwen3), no-think → greedy.
        gen_kwargs: dict = {"max_new_tokens": max_new_tokens}
        if self.enable_thinking:
            gen_kwargs.update(
                do_sample=True,
                temperature=self.temperature,
                top_p=self.top_p,
                top_k=self.top_k,
            )
        else:
            gen_kwargs.update(do_sample=False)

        with torch.no_grad():
            out = self.model.generate(**inputs, **gen_kwargs)
        raw = self.tokenizer.decode(
            out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True
        ).strip()

        # Tách <think>…</think> trước khi parse JSON.
        think_text, answer_text = self._split_thinking(raw)
        parsed = self._parse_output(answer_text)

        # reasoning.steps: ưu tiên CoT trong <think>; fallback về explanation.
        steps = self._steps_from_text(think_text)
        reasoning_type = "cot" if steps else "fol"
        if not steps:
            steps = self._steps_from_text(parsed["explanation"])

        return {
            "answer":      parsed["answer"],
            "explanation": parsed["explanation"],
            "reasoning":   {"type": reasoning_type, "steps": steps},
        }

    # ── private ────────────────────────────────────────────────────────────────

    @staticmethod
    def _split_thinking(raw: str) -> tuple[str, str]:
        """Tách (think_text, answer_text) từ output thô.

        - Có '</think>'         → think = trước nó, answer = sau nó.
        - Bắt đầu '<think>' mà KHÔNG đóng (think bị cắt vì hết token) → toàn bộ
          là think, answer rỗng (parser sẽ fallback Unknown — đúng ý: think tràn budget).
        - Không có think         → answer = toàn bộ.
        """
        if "</think>" in raw:
            think, _, after = raw.partition("</think>")
            return think.replace("<think>", "").strip(), after.strip()
        if raw.lstrip().startswith("<think>"):
            return raw.replace("<think>", "").strip(), ""
        return "", raw.strip()

    @staticmethod
    def _steps_from_text(text: str, max_steps: int = 12) -> list[str]:
        """Tách văn bản reasoning thành list bước (theo dòng / câu)."""
        if not text:
            return []
        parts = re.split(r"\n+|(?<=[.。!?])\s+", text)
        steps = [p.strip(" \t-•*>").strip() for p in parts]
        steps = [s for s in steps if len(s) > 1]
        return steps[:max_steps]

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
