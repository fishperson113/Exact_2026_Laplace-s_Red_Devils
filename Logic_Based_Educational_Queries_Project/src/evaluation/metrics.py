from __future__ import annotations

import re
from typing import Iterable

# Đúng 7 nhãn trong Logic_Based_Educational_Queries.json — không map, không đổi hoa thường.
ANSWERS_ALLOWED = frozenset({"A", "B", "C", "D", "Yes", "No", "Unknown"})

_ANSWER_LINE = re.compile(r"(?im)^\s*answer\s*:\s*(.+?)(?:\n|$)")


def require_answer_label(raw: str) -> str:
    """Chỉ chấp nhận đúng một trong 7 chuỗi trên (sau strip); sai → ValueError."""
    v = str(raw).strip().split("\n", 1)[0].strip()
    if v not in ANSWERS_ALLOWED:
        raise ValueError(
            f"Invalid answer label (must be one of {sorted(ANSWERS_ALLOWED)}): {raw!r}"
        )
    return v


def extract_answer_from_completion(text: str) -> str:
    """Lấy phần sau `Answer:` hoặc dòng đầu; phải là một trong 7 nhãn, không thì raise."""
    if not text or not str(text).strip():
        raise ValueError("Empty model output; cannot parse answer label.")
    m = _ANSWER_LINE.search(text)
    chunk = (m.group(1) if m else text.strip().splitlines()[0]).strip()
    return require_answer_label(chunk)


def answer_accuracy(preds: Iterable[str], golds: Iterable[str]) -> float:
    ps, gs = list(preds), list(golds)
    if len(ps) != len(gs) or not gs:
        return 0.0
    return sum(1 for p, g in zip(ps, gs) if p == g) / len(gs)
