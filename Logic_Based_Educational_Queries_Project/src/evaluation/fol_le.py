"""Logical Equivalence (LE): kiểm tra 2 FOL formula có tương đương logic không.

Dùng Z3 (SMT solver): gold ↔ pred là tautology ⟺ ¬(gold ↔ pred) là unsatisfiable.
Fallback: LE = 0 nếu parse fail hoặc Z3 timeout.
"""
from __future__ import annotations

import logging
from typing import Any

_LOG = logging.getLogger(__name__)

_Z3_TIMEOUT_MS = 5000  # 5 giây mỗi cặp formula


def _z3_available() -> bool:
    try:
        import z3  # noqa: F401
        return True
    except ImportError:
        return False


def le_single_z3(gold_z3: Any, pred_z3: Any, timeout_ms: int = _Z3_TIMEOUT_MS) -> float:
    """LE cho 1 cặp Z3 expression.

    Returns
    -------
    1.0 nếu tương đương logic, 0.0 nếu không (hoặc timeout).
    """
    import z3

    s = z3.Solver()
    s.set("timeout", timeout_ms)
    # ¬(gold ↔ pred): nếu unsat → tương đương
    s.add(z3.Not(gold_z3 == pred_z3))
    result = s.check()
    if result == z3.unsat:
        return 1.0
    return 0.0


def le_single_from_strings(
    gold_fol: str,
    pred_fol: str,
    cache: dict[str, Any] | None = None,
    timeout_ms: int = _Z3_TIMEOUT_MS,
) -> float:
    """LE cho 1 cặp FOL string. Trả 0.0 nếu parse fail."""
    if cache is None:
        cache = {}
    try:
        from .fol_z3_translator import fol_string_to_z3

        g = fol_string_to_z3(gold_fol, cache)
        p = fol_string_to_z3(pred_fol, cache)
        return le_single_z3(g, p, timeout_ms=timeout_ms)
    except Exception as e:
        _LOG.debug("LE parse/solve fail: %s | gold=%r pred=%r", e, gold_fol, pred_fol)
        return 0.0


def le_record(
    gold_list: list[str],
    pred_list: list[str],
    timeout_ms: int = _Z3_TIMEOUT_MS,
) -> float:
    """LE trung bình trên từng cặp premise (per-premise LE).

    Premise thiếu/thừa → LE = 0 cho dòng đó.
    """
    n = len(gold_list)
    if n == 0:
        return 0.0
    cache: dict[str, Any] = {}
    scores: list[float] = []
    for i in range(n):
        if i >= len(pred_list):
            scores.append(0.0)
            continue
        scores.append(
            le_single_from_strings(gold_list[i], pred_list[i], cache, timeout_ms)
        )
    return sum(scores) / n


def le_record_no_z3(gold_list: list[str], pred_list: list[str]) -> float:
    """Fallback LE khi không có Z3: so khớp string (normalized whitespace).

    Kém chính xác hơn Z3 nhưng chạy được mọi nơi.
    """
    import re

    def _norm(s: str) -> str:
        return re.sub(r"\s+", " ", s.strip())

    n = len(gold_list)
    if n == 0:
        return 0.0
    match = 0
    for i in range(n):
        if i < len(pred_list) and _norm(gold_list[i]) == _norm(pred_list[i]):
            match += 1
    return match / n
