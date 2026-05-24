"""Yêu cầu: `cfg` là `FolSFTConfig`. Chạy: `%run -i fol_model_stage_train.py`"""
from __future__ import annotations

from models.fol_model.train import run_train_and_eval

_ = run_train_and_eval(cfg)
print("FOL train OK:", _ is not None)
