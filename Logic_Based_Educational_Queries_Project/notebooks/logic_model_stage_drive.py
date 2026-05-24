"""Yêu cầu: đã `from services.config import LogicSFTConfig` và `cfg = LogicSFTConfig(...)`.
Chạy: `%run -i logic_model_stage_drive.py`
"""
from __future__ import annotations

from services.drive import download_and_extract_from_drive

_ = download_and_extract_from_drive(cfg)
print("Drive OK:", _)
