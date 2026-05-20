"""Answer extraction + numeric comparison.

Only handles pure-numeric ground truths for now (matching v01 test set).
Future versions will route Yes/No, multi-value, text answers separately.
"""

from __future__ import annotations

import math
import re
from dataclasses import dataclass, field


_FINAL_RE = re.compile(r"FINAL\s*ANSWER\s*:\s*([^\n]+)", re.IGNORECASE)
_UNIT_RE = re.compile(r"UNIT\s*:\s*([^\n]+)", re.IGNORECASE)
_NUM_RE = re.compile(
    r"[-+]?(?:\d+\.\d+|\d+)(?:[eE][-+]?\d+)?"
)


@dataclass
class Extraction:
    raw_answer: str | None = None
    raw_unit: str | None = None
    numeric: float | None = None


def extract(completion: str) -> Extraction:
    """Pull FINAL ANSWER / UNIT from a model completion."""
    ans_match = _FINAL_RE.search(completion)
    unit_match = _UNIT_RE.search(completion)

    out = Extraction()
    if ans_match:
        out.raw_answer = ans_match.group(1).strip()
        num_match = _NUM_RE.search(out.raw_answer)
        if num_match:
            try:
                out.numeric = float(num_match.group(0))
            except ValueError:
                out.numeric = None
    else:
        # Fallback: last number in the completion.
        nums = _NUM_RE.findall(completion)
        if nums:
            try:
                out.numeric = float(nums[-1])
                out.raw_answer = nums[-1]
            except ValueError:
                pass

    if unit_match:
        out.raw_unit = unit_match.group(1).strip()

    return out


def numeric_close(
    pred: float | None,
    gold: float,
    rel_tol: float = 1e-2,
    abs_tol: float = 1e-4,
) -> bool:
    if pred is None or math.isnan(pred) or math.isinf(pred):
        return False
    if math.isclose(pred, gold, rel_tol=rel_tol, abs_tol=abs_tol):
        return True
    # Common off-by-power-of-10 errors (forgot unit prefix); treat as miss but
    # easy to detect later — flag separately rather than counting as correct.
    return False


@dataclass
class RowResult:
    id: str
    question: str
    gold_answer: str
    gold_unit: str
    completion: str
    pred_numeric: float | None
    pred_unit: str | None
    is_correct: bool
    elapsed_s: float
    extra: dict = field(default_factory=dict)


def summarise(results: list[RowResult]) -> dict:
    n = len(results)
    correct = sum(1 for r in results if r.is_correct)
    return {
        "n": n,
        "correct": correct,
        "accuracy": correct / n if n else 0.0,
        "mean_latency_s": sum(r.elapsed_s for r in results) / n if n else 0.0,
    }
