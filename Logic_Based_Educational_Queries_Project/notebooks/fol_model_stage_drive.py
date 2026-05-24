"""Tải dữ liệu thô từ Drive (dùng `LOGIC_*` trong `.env`).
Chạy: `%run -i fol_model_stage_drive.py`
"""
from __future__ import annotations

from services.config import LogicSFTConfig
from services.drive import download_and_extract_from_drive

_logic_cfg = LogicSFTConfig.from_env()
_ = download_and_extract_from_drive(_logic_cfg)
print("Drive OK:", _)
