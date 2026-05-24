"""Yêu cầu: `cfg` là `FolSFTConfig`. Token: `HF_Token` hoặc `HF_TOKEN`.
Chạy: `%run -i fol_model_stage_push.py`
"""
from __future__ import annotations

import os

from services.hub_push import push_merged_fol_lora

if not cfg.push_to_hub:
    print("push_to_hub=False — bỏ qua.")
else:
    token = (
        globals().get("HF_Token")
        or os.environ.get("HF_TOKEN")
        or os.environ.get("HUGGINGFACE_HUB_TOKEN")
        or ""
    )
    if not token:
        raise ValueError(
            "Thiếu token HF: đặt HF_TOKEN trong .env hoặc HF_Token trong notebook (Kaggle secrets)."
        )
    url = push_merged_fol_lora(cfg, token)
    print(url)
    print("Repo:", cfg.resolved_hf_repo())
