"""Sinh kết quả trên prompt tùy ý (sau khi đã có checkpoint LoRA)."""
from __future__ import annotations

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

from evaluation.metrics import extract_answer_from_completion
from services.config import LogicSFTConfig

from .train import load_tokenizer as load_base_tokenizer


def _load_tokenizer(cfg: LogicSFTConfig) -> AutoTokenizer:
    ck = cfg.checkpoint_dir
    if ck is not None and (ck / "tokenizer_config.json").is_file():
        return AutoTokenizer.from_pretrained(
            str(ck), trust_remote_code=cfg.trust_remote_code
        )
    return load_base_tokenizer(cfg)


def load_model_for_inference(cfg: LogicSFTConfig):
    """Nạp base + adapter từ `cfg.checkpoint_dir` nếu có `adapter_config.json`."""
    tok = _load_tokenizer(cfg)
    dtype = torch.bfloat16 if cfg.bf16 else torch.float16
    base = AutoModelForCausalLM.from_pretrained(
        cfg.model_name,
        torch_dtype=dtype,
        device_map="auto",
        trust_remote_code=cfg.trust_remote_code,
    )
    ckpt = cfg.checkpoint_dir
    if ckpt is not None and (ckpt / "adapter_config.json").is_file():
        model = PeftModel.from_pretrained(base, str(ckpt))
    else:
        model = base
    model.eval()
    return model, tok


@torch.no_grad()
def generate_answer_text(cfg: LogicSFTConfig, prompt: str) -> str:
    """`prompt` = chuỗi đã áp chat template (hoặc chỉ phần user tùy mô hình). Trả về text sinh."""
    model, tok = load_model_for_inference(cfg)
    enc = tok(prompt, return_tensors="pt").to(model.device)
    pad_id = tok.pad_token_id or tok.eos_token_id
    out = model.generate(
        **enc,
        max_new_tokens=cfg.gen_max_new_tokens,
        do_sample=False,
        pad_token_id=pad_id,
        eos_token_id=tok.eos_token_id,
    )
    gen = out[0, enc["input_ids"].shape[1] :]
    return tok.decode(gen, skip_special_tokens=True)


def predict_label(cfg: LogicSFTConfig, prompt: str) -> str:
    """Parse một trong 7 nhãn từ completion (raise nếu không hợp lệ)."""
    text = generate_answer_text(cfg, prompt)
    return extract_answer_from_completion(text)
