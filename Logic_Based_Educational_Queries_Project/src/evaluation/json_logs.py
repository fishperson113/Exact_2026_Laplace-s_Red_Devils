"""Đọc JSON metrics sau train (trước đây `visualization/evaluation.py`)."""
from __future__ import annotations

import json

from services.config import LogicSFTConfig


def read_train_metrics(cfg: LogicSFTConfig) -> dict | None:
    if cfg.out_dir is None:
        return None
    p = cfg.out_dir / "train_metrics.json"
    if not p.is_file():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def read_test_accuracy(cfg: LogicSFTConfig) -> dict | None:
    if cfg.out_dir is None:
        return None
    p = cfg.out_dir / "test_accuracy.json"
    if not p.is_file():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def print_eval_summary(cfg: LogicSFTConfig) -> None:
    """In nhanh metrics đã lưu (thay cho biểu đồ nếu chưa cài matplotlib đầy đủ)."""
    print("train_metrics:", read_train_metrics(cfg))
    print("test_accuracy:", read_test_accuracy(cfg))
