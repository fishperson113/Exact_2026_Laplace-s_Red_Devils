"""Yêu cầu: `cfg` (LogicSFTConfig). Chạy: `%run -i logic_model_stage_train.py`"""
from __future__ import annotations

from models.logic_model.train import run_test_eval, run_training

train_out = run_training(cfg)
if train_out is None:
    print("RUN_TRAIN=False — bỏ qua.")
else:
    _result, trainer, _tok, dataset_dict = train_out
    test_metrics = run_test_eval(cfg, trainer, dataset_dict)
    print("Test metrics:", test_metrics)
