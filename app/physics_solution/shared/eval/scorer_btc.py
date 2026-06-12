"""BTC-faithful Type-2 scorer (Submission Guide §4.5): answer AND unit both correct.

This deliberately mirrors what the organizer does with our /predict output and their
ground truth, and differs from shared/eval/scorer.py in these ways:

  1. SI-prefix aware (BTC confirmed they handle this): 0.005655 T == 5.654 mT counts —
     the unit must share the BASE unit with gold, and the value is rescaled by the prefix
     ratio before comparing. A different base unit still FAILS.
  2. Unit must MATCH on base unit (both sides go through normalizer.normalize_unit:
     Ω/Ohm/Ohms -> ohm, µ -> u, nan/empty/-/... -> 'N/A'). Internal scorer ignores the unit
     entirely except for the rescue.
  3. Text answers: exact match after lowercase/whitespace normalization — no bidirectional
     substring containment.

Numeric comparison keeps a small relative tolerance (default 2e-2, same as the internal
scorer) because gold values are rounded ("0.7" vs a computed 0.702562); pass rel_tol to
study stricter regimes.

Input is the already-extracted (answer, unit) pair — i.e. what /predict actually returns —
not the raw completion.
"""

from __future__ import annotations

import math
import re
from dataclasses import dataclass

from app.physics_solution.shared.eval.normalizer import NO_UNIT, normalize_answer, normalize_unit
from app.physics_solution.shared.eval.scorer import _convert_factor, _parse_sci_notation


@dataclass
class BtcResult:
    correct: bool
    value_ok: bool
    unit_ok: bool
    notes: str = ""


def _num(s: str) -> float | None:
    """Parse one scalar (plain / e-notation / x10^ / 10^{n}) to float, else None."""
    return _parse_sci_notation(str(s).strip())


def _values_close(p: float, g: float, rel_tol: float) -> bool:
    if math.isnan(p) or math.isinf(p):
        return False
    return math.isclose(p, g, rel_tol=rel_tol, abs_tol=1e-9)


def _norm_text(s: str) -> str:
    return re.sub(r"\s+", " ", str(s).strip().lower()).strip(" .")


def _broadcast(unit: str, n: int) -> list[str]:
    parts = [u.strip() for u in unit.split(";")]
    if len(parts) == 1:
        return parts * n
    return (parts + [NO_UNIT] * n)[:n]


def _value_unit_match(p_num: float | None, p_unit: str, g_num: float, g_unit: str,
                      rel_tol: float) -> tuple[bool, bool]:
    """(value_ok, unit_ok) with SI-prefix awareness: same unit -> direct compare; same base
    unit but different prefix -> rescale pred onto gold's scale first (5.654 mT == 0.005655 T).
    Different base unit -> unit fails."""
    if p_num is None:
        return False, p_unit == g_unit
    if p_unit == g_unit:
        return _values_close(p_num, g_num, rel_tol), True
    factor = _convert_factor(p_unit, g_unit)
    if factor is not None:                       # same base unit, different SI prefix
        return _values_close(p_num * factor, g_num, rel_tol), True
    return _values_close(p_num, g_num, rel_tol), False


def score_btc(pred_answer: str, pred_unit: str, gold_answer: str, gold_unit: str,
              rel_tol: float = 2e-2) -> BtcResult:
    """Strict BTC-style verdict on a (value, unit) prediction pair."""
    p_ans = normalize_answer(pred_answer)
    g_ans = normalize_answer(gold_answer)
    p_unit = normalize_unit(pred_unit)
    g_unit = normalize_unit(gold_unit)

    # ---- multi-value ("a; b") -------------------------------------------------
    if ";" in g_ans or ";" in p_ans:
        g_parts = [x.strip() for x in g_ans.split(";") if x.strip()]
        p_parts = [x.strip() for x in p_ans.split(";") if x.strip()]
        if len(g_parts) != len(p_parts):
            return BtcResult(False, False, p_unit == g_unit, "multi-value count mismatch")
        g_nums = [_num(x) for x in g_parts]
        p_nums = [_num(x) for x in p_parts]
        n = len(g_parts)
        p_units, g_units = _broadcast(p_unit, n), _broadcast(g_unit, n)
        if any(v is None for v in g_nums):           # text-ish multi-value
            value_ok = [_norm_text(a) for a in p_parts] == [_norm_text(b) for b in g_parts]
            unit_ok = p_units == g_units
        else:
            # sort by magnitude (order-free), then per-part prefix-aware compare
            pp = sorted(zip(p_nums, p_units), key=lambda t: (t[0] is None, t[0]))
            gp = sorted(zip(g_nums, g_units))
            value_ok = unit_ok = True
            for (p, pu), (g, gu) in zip(pp, gp):
                v_ok, u_ok = _value_unit_match(p, pu, g, gu, rel_tol)
                value_ok &= v_ok
                unit_ok &= u_ok
        return BtcResult(value_ok and unit_ok, value_ok, unit_ok, "multi-value")

    # ---- single value ----------------------------------------------------------
    g_num = _num(g_ans)
    if g_num is not None:
        value_ok, unit_ok = _value_unit_match(_num(p_ans), p_unit, g_num, g_unit, rel_tol)
        return BtcResult(value_ok and unit_ok, value_ok, unit_ok, "numeric")

    # ---- yes/no + free text ----------------------------------------------------
    value_ok = _norm_text(p_ans) == _norm_text(g_ans) and bool(_norm_text(g_ans))
    unit_ok = p_unit == g_unit
    return BtcResult(value_ok and unit_ok, value_ok, unit_ok, "text")


if __name__ == "__main__":
    cases = [
        # (pred_ans, pred_unit, gold_ans, gold_unit, expect)
        ("5", "A", "5", "A", True),
        ("0.702562", "N", "0.7", "N", True),                 # rounding tolerance
        ("0.005655", "T", "5.654", "mT", True),              # prefix-aware (BTC handles)
        ("4e-9", "F", "4e-3", "uF", True),                   # prefix-aware (BTC handles)
        ("4e-9", "F", "4 * 10^{-9}", "F", True),             # sci-form gold, same scale
        ("40", "Ohm", "40", "Ω", True),                      # unit naming unified
        ("0", "nan", "0", "-", True),                        # nan -> '-'
        ("0", "", "0", "—", True),                           # empty vs em-dash
        ("yes", "yes_no", "Yes", "-", True),                 # junk unit -> '-'
        ("512000", "V/m", "640000", "V/m", False),
        ("0.6; 1.2", "cm", "0.6; 1.2", "cm", True),
        ("1.2; 0.6", "cm", "0.6; 1.2", "cm", True),          # order-free numeric
        ("doubled", "-", "Doubled", "-", True),
        ("inductive", "-", "the circuit exhibits an inductive characteristic", "-", False),
        ("5", "A", "5", "mA", False),                        # unit scale mismatch
    ]
    bad = 0
    for pa, pu, ga, gu, want in cases:
        r = score_btc(pa, pu, ga, gu)
        ok = r.correct == want
        bad += not ok
        print(f"  [{'PASS' if ok else 'FAIL'}] ({pa!r},{pu!r}) vs ({ga!r},{gu!r}) "
              f"-> {r.correct} (value={r.value_ok} unit={r.unit_ok}) want {want}")
    print(f"\n{'ALL PASS' if not bad else f'{bad} FAILURES'}")
