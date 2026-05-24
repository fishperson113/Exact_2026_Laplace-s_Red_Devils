"""Định nghĩa kiến trúc train (base LLM + LoRA) — delegate `models.logic_model.train.build_model`."""
from __future__ import annotations

from services.config import LogicSFTConfig

from .train import build_model

__all__ = ["build_model", "LogicSFTConfig"]
