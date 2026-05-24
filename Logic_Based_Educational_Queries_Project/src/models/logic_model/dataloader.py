"""Nạp `DatasetDict` train/dev/test từ CSV đã xử lý."""
from __future__ import annotations

from data.dataset import build_dataset_dict
from services.config import LogicSFTConfig


def load_dataset_dict(cfg: LogicSFTConfig, tokenizer):
    return build_dataset_dict(cfg, tokenizer)
