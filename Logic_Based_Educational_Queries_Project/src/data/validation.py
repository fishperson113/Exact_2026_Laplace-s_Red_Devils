"""Kiểm tra dữ liệu trước khi train (số câu, file split, nhãn)."""
from __future__ import annotations

from pathlib import Path

from .ingestion import load_raw_records, project_root


def validate_raw_question_count(expected: int = 808) -> None:
    recs = load_raw_records()
    n = sum(len(r["questions"]) for r in recs)
    if n != expected:
        raise ValueError(f"Số câu sau flatten ({n}) khác kỳ vọng ({expected}).")


def validate_processed_splits() -> Path:
    d = project_root() / "data" / "processed" / "logic_sft"
    for name in ("train.csv", "dev.csv", "test.csv", "split_record_ids.json", "split_summary.json"):
        p = d / name
        if not p.is_file():
            raise FileNotFoundError(f"Thiếu file split: {p}")
    return d
