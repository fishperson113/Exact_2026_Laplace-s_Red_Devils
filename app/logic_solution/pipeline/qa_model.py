"""
pipeline/qa_model.py
--------------------
Stage 2: Load QA model (base + LoRA adapter) từ HF Hub.
Nhận NL + FOL + options + question → sinh:
  <reasoning steps Rule:/Fact:/Derive:/Conclusion:>
  {"premises_used": [...], "explanation": "...", "answer": "..."}   (answer ĐỨNG CUỐI)

ĐỒNG BỘ 1:1 với luồng train QA v3 (src/models/QA_model/prepare_data.py + train.py):
prompt có Options block, premises 0-indexed, MCQ trả VERBATIM option text.
"""
from __future__ import annotations

import torch
from peft import PeftConfig, PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

from prompts import (
    SYSTEM_PROMPT_QA,
    USER_TEMPLATE_QA,
    format_premises_nl,
    format_premises_fol,
    format_options,
)
from parsing import parse_qa_output


class QAModel:
    """Load QA LoRA adapter từ HF Hub và sinh reasoning steps + answer."""

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
        # QA v3 được train no-think → mặc định enable_thinking=False (greedy).
        # Qwen3 think mode KHÔNG được greedy (lặp vô hạn) → nếu bật phải sampling.
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
        options:      list[str] | None = None,
        max_new_tokens: int = 1000,
    ) -> dict:
        """
        Input : premises_nl, premises_fol, question, options
        Output: {"answer", "explanation", "premises_used",
                 "reasoning": {"type": "fol", "steps": [...]}}

        reasoning.steps = NGUYÊN VĂN các dòng Rule:/Fact:/Derive:/Conclusion: model
        sinh ra (không cắt câu lại). reasoning.type LUÔN là "fol" (schema BTC).
        """
        user_content = USER_TEMPLATE_QA.format(
            premises_nl_block  = format_premises_nl(premises_nl),
            premises_fol_block = format_premises_fol(premises_fol),
            options_block      = format_options(options or []),
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

        # Sampling theo chế độ: think → sampling (Qwen3), no-think → greedy (khớp eval train).
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

        # Tách <think>…</think> (nếu có) trước khi parse — tránh ngoặc trong think vỡ parser.
        _think, answer_text = self._split_thinking(raw)
        parsed = parse_qa_output(answer_text)

        return {
            "answer":        parsed["answer"],
            "explanation":   parsed["explanation"],
            "premises_used": parsed["premises_used"],
            # type LUÔN "fol" theo schema BTC; steps nguyên bản từ model.
            "reasoning":     {"type": "fol", "steps": parsed["reasoning_steps"]},
        }

    # ── private ────────────────────────────────────────────────────────────────

    @staticmethod
    def _split_thinking(raw: str) -> tuple[str, str]:
        """Tách (think_text, answer_text) từ output thô.

        - Có '</think>'         → think = trước nó, answer = sau nó.
        - Bắt đầu '<think>' mà KHÔNG đóng (think bị cắt vì hết token) → toàn bộ
          là think, answer rỗng (parser sẽ fallback — đúng ý: think tràn budget).
        - Không có think         → answer = toàn bộ.
        """
        if "</think>" in raw:
            think, _, after = raw.partition("</think>")
            return think.replace("<think>", "").strip(), after.strip()
        if raw.lstrip().startswith("<think>"):
            return raw.replace("<think>", "").strip(), ""
        return "", raw.strip()
