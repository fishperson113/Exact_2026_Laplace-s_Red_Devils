"""Answer extraction + numeric comparison + multi-type scoring.

Handles all answer types found in the EXACT 2026 physics dataset:
pure_numeric, sci_notation, yes_no, multi_value, text_only, mixed.
"""

from __future__ import annotations

import math
import re
from dataclasses import dataclass, field
from enum import Enum


# ------------------------------------------------------------------ regex

_FINAL_RE = re.compile(r"FINAL\s*ANSWER\s*:\s*([^\n]+)", re.IGNORECASE)
_UNIT_RE = re.compile(r"UNIT\s*:\s*([^\n]+)", re.IGNORECASE)
_NUM_RE = re.compile(
    r"[-+]?(?:\d+\.\d+|\d+)(?:[eE][-+]?\d+)?"
)

_SUPERSCRIPT_MAP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺", "0123456789-+")

_SCI_RE = re.compile(
    r"([-+]?\d+(?:\.\d+)?)\s*(?:[x×·*]|\\times)\s*10\s*"
    r"(?:\^?\s*\{?\s*([-+]?\d+)\s*\}?"  # caret: 10^-3 or 10^{-3}
    r"|([⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]+))",          # superscript: 10⁻³
    re.IGNORECASE,
)

_SCI_DOT_RE = re.compile(
    r"([-+]?\d+)\s*\.\s*10\s*\^?\s*\{?\s*([-+]?\d+)\s*\}?",
)

_BARE_POWER_RE = re.compile(
    r"^[-+]?\s*10\s*\^\s*\{?\s*([-+]?\d+)\s*\}?\s*$"
)

_E_NOTATION_RE = re.compile(
    r"([-+]?\d+(?:\.\d+)?)\s*[eE]\s*([-+]?\d+)"
)


# ------------------------------------------------------------------ answer type

class AnswerType(str, Enum):
    PURE_NUMERIC = "pure_numeric"
    SCI_NOTATION = "sci_notation"
    MULTI_VALUE  = "multi_value"
    YES_NO       = "yes_no"
    TEXT_ONLY    = "text_only"
    MIXED        = "mixed"


def detect_answer_type(gold_answer: str) -> AnswerType:
    """Classify a gold answer string into one of the 6 answer types."""
    s = str(gold_answer).strip()
    if not s:
        return AnswerType.TEXT_ONLY

    low = s.lower()
    if low in ("yes", "no"):
        return AnswerType.YES_NO

    if ";" in s:
        return AnswerType.MULTI_VALUE

    if _SCI_RE.search(s):
        return AnswerType.SCI_NOTATION

    if _SCI_DOT_RE.search(s):
        return AnswerType.SCI_NOTATION

    if _BARE_POWER_RE.match(s):
        return AnswerType.SCI_NOTATION

    if any(marker in s for marker in ["×", "x10", "x 10", "\\times"]):
        return AnswerType.SCI_NOTATION

    if re.search(r"[a-zA-Z\\]", s) and not _E_NOTATION_RE.fullmatch(s.strip()):
        try:
            float(s)
            return AnswerType.PURE_NUMERIC
        except ValueError:
            nums = _NUM_RE.findall(s)
            if nums:
                return AnswerType.MIXED
            return AnswerType.TEXT_ONLY

    try:
        float(s)
        return AnswerType.PURE_NUMERIC
    except ValueError:
        pass

    return AnswerType.TEXT_ONLY


@dataclass
class Extraction:
    raw_answer: str | None = None
    raw_unit: str | None = None
    numeric: float | None = None


def _strip_latex_answer(s: str) -> str:
    """Strip $...$ wrapper and normalise LaTeX \\times → * for parsing."""
    s = s.strip()
    if s.startswith("$") and s.endswith("$"):
        s = s[1:-1].strip()
    s = s.replace("\\times", "*")
    return s


def extract(completion: str) -> Extraction:
    """Pull FINAL ANSWER / UNIT from a model completion."""
    ans_match = _FINAL_RE.search(completion)
    unit_match = _UNIT_RE.search(completion)

    out = Extraction()
    if ans_match:
        out.raw_answer = _strip_latex_answer(ans_match.group(1).strip())
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


# ------------------------------------------------------------------ multi-type scoring


@dataclass
class ScoringResult:
    is_correct: bool
    pred_value: float | str | list | None
    pred_unit: str | None
    detected_answer_type: AnswerType
    partial_correct: bool = False
    notes: str = ""


def _parse_sci_notation(s: str) -> float | None:
    """Parse scientific notation strings like '5.07 × 10^-6', '5.07e-6', '5.07 x 10⁻⁶',
    '4 . 10^{-9}', '10^4'."""
    s = str(s).strip()
    m = _SCI_RE.search(s)
    if m:
        mantissa = float(m.group(1))
        if m.group(2) is not None:
            exponent = int(m.group(2))
        else:
            sup = m.group(3).translate(_SUPERSCRIPT_MAP)
            exponent = int(sup)
        return mantissa * (10 ** exponent)

    m = _SCI_DOT_RE.search(s)
    if m:
        mantissa = float(m.group(1))
        exponent = int(m.group(2))
        return mantissa * (10 ** exponent)

    m = _BARE_POWER_RE.match(s)
    if m:
        exponent = int(m.group(1))
        sign = -1 if s.lstrip().startswith("-") else 1
        return sign * (10 ** exponent)

    m = _E_NOTATION_RE.search(s)
    if m:
        return float(m.group(1)) * (10 ** int(m.group(2)))

    try:
        return float(s)
    except ValueError:
        return None


def _score_pure_numeric(pred_completion: str, gold_answer: str) -> ScoringResult:
    extracted = extract(pred_completion)
    gold_f = _safe_float(gold_answer)
    if gold_f is None:
        return ScoringResult(
            is_correct=False, pred_value=extracted.numeric,
            pred_unit=extracted.raw_unit, detected_answer_type=AnswerType.PURE_NUMERIC,
            notes="gold not parseable as float",
        )
    correct = numeric_close(extracted.numeric, gold_f)
    return ScoringResult(
        is_correct=correct, pred_value=extracted.numeric,
        pred_unit=extracted.raw_unit, detected_answer_type=AnswerType.PURE_NUMERIC,
    )


def _score_sci_notation(pred_completion: str, gold_answer: str) -> ScoringResult:
    extracted = extract(pred_completion)
    gold_f = _parse_sci_notation(gold_answer)
    if gold_f is None:
        return ScoringResult(
            is_correct=False, pred_value=extracted.numeric,
            pred_unit=extracted.raw_unit, detected_answer_type=AnswerType.SCI_NOTATION,
            notes="gold sci_notation unparseable",
        )
    pred_f = None
    if extracted.raw_answer:
        pred_f = _parse_sci_notation(extracted.raw_answer)
    if pred_f is None:
        pred_f = extracted.numeric
    correct = pred_f is not None and numeric_close(pred_f, gold_f)
    return ScoringResult(
        is_correct=correct, pred_value=pred_f,
        pred_unit=extracted.raw_unit, detected_answer_type=AnswerType.SCI_NOTATION,
    )


def _score_yes_no(pred_completion: str, gold_answer: str) -> ScoringResult:
    extracted = extract(pred_completion)
    gold_norm = gold_answer.strip().lower()
    if gold_norm not in ("yes", "no"):
        return ScoringResult(
            is_correct=False, pred_value=None,
            pred_unit=extracted.raw_unit, detected_answer_type=AnswerType.YES_NO,
            notes=f"gold '{gold_answer}' not yes/no",
        )
    pred_raw = (extracted.raw_answer or "").strip().lower()
    pred_norm = None
    for token in [pred_raw] + pred_raw.split():
        if token in ("yes", "y"):
            pred_norm = "yes"
            break
        if token in ("no", "n"):
            pred_norm = "no"
            break
    if pred_norm is None:
        final_match = _FINAL_RE.search(pred_completion)
        if final_match:
            line = final_match.group(1).strip().lower()
            if line in ("yes", "y"):
                pred_norm = "yes"
            elif line in ("no", "n"):
                pred_norm = "no"
    correct = pred_norm == gold_norm
    return ScoringResult(
        is_correct=correct, pred_value=pred_norm or pred_raw,
        pred_unit=extracted.raw_unit, detected_answer_type=AnswerType.YES_NO,
    )


def _score_multi_value(pred_completion: str, gold_answer: str) -> ScoringResult:
    extracted = extract(pred_completion)
    gold_parts = [p.strip() for p in gold_answer.split(";") if p.strip()]
    gold_floats = []
    for p in gold_parts:
        f = _safe_float(p)
        if f is not None:
            gold_floats.append(f)

    pred_raw = extracted.raw_answer or ""
    pred_parts = [p.strip() for p in re.split(r"[;,]", pred_raw) if p.strip()]
    pred_floats = []
    for p in pred_parts:
        f = _safe_float(p)
        if f is not None:
            pred_floats.append(f)

    if not gold_floats:
        gold_strs = sorted(p.lower() for p in gold_parts)
        pred_strs = sorted(p.lower() for p in pred_parts)
        correct = gold_strs == pred_strs
        return ScoringResult(
            is_correct=correct, pred_value=pred_parts,
            pred_unit=extracted.raw_unit, detected_answer_type=AnswerType.MULTI_VALUE,
            notes="text-based multi-value comparison",
        )

    gold_sorted = sorted(gold_floats)
    pred_sorted = sorted(pred_floats)
    matches = sum(
        1 for g, p in zip(gold_sorted, pred_sorted) if numeric_close(p, g)
    )
    all_correct = len(gold_sorted) == len(pred_sorted) and matches == len(gold_sorted)
    partial = matches > 0 and not all_correct
    return ScoringResult(
        is_correct=all_correct, pred_value=pred_floats,
        pred_unit=extracted.raw_unit, detected_answer_type=AnswerType.MULTI_VALUE,
        partial_correct=partial,
        notes=f"matched {matches}/{len(gold_sorted)} values",
    )


def _score_text_only(pred_completion: str, gold_answer: str) -> ScoringResult:
    extracted = extract(pred_completion)
    gold_norm = gold_answer.strip().lower()
    pred_raw = (extracted.raw_answer or "").strip().lower()
    correct = gold_norm != "" and gold_norm in pred_raw
    return ScoringResult(
        is_correct=correct, pred_value=extracted.raw_answer,
        pred_unit=extracted.raw_unit, detected_answer_type=AnswerType.TEXT_ONLY,
    )


def _score_mixed(pred_completion: str, gold_answer: str) -> ScoringResult:
    extracted = extract(pred_completion)
    nums_in_gold = _NUM_RE.findall(gold_answer)
    gold_f = _safe_float(nums_in_gold[0]) if nums_in_gold else None
    if gold_f is not None:
        correct = numeric_close(extracted.numeric, gold_f)
        return ScoringResult(
            is_correct=correct, pred_value=extracted.numeric,
            pred_unit=extracted.raw_unit, detected_answer_type=AnswerType.MIXED,
            notes="extracted first numeric from mixed gold",
        )
    gold_norm = gold_answer.strip().lower()
    pred_raw = (extracted.raw_answer or "").strip().lower()
    correct = gold_norm != "" and gold_norm in pred_raw
    return ScoringResult(
        is_correct=correct, pred_value=extracted.raw_answer,
        pred_unit=extracted.raw_unit, detected_answer_type=AnswerType.MIXED,
        notes="text fallback for mixed",
    )


def _safe_float(s) -> float | None:
    try:
        return float(str(s).strip())
    except (ValueError, TypeError):
        return None


_SCORE_DISPATCH: dict[AnswerType, callable] = {
    AnswerType.PURE_NUMERIC: _score_pure_numeric,
    AnswerType.SCI_NOTATION: _score_sci_notation,
    AnswerType.YES_NO:       _score_yes_no,
    AnswerType.MULTI_VALUE:  _score_multi_value,
    AnswerType.TEXT_ONLY:     _score_text_only,
    AnswerType.MIXED:        _score_mixed,
}


def score(pred_completion: str, gold_answer: str, gold_unit: str) -> ScoringResult:
    """Score a prediction against a gold answer, dispatching by answer type."""
    answer_type = detect_answer_type(gold_answer)
    result = _SCORE_DISPATCH[answer_type](pred_completion, gold_answer)
    if result.pred_unit is None:
        ext = extract(pred_completion)
        result.pred_unit = ext.raw_unit
    return result


# ------------------------------------------------------------------ inline tests

if __name__ == "__main__":
    def _test():
        ok = 0
        total = 0

        def check(label, result, expected_correct):
            nonlocal ok, total
            total += 1
            status = "PASS" if result.is_correct == expected_correct else "FAIL"
            if status == "PASS":
                ok += 1
            print(f"  [{status}] {label}: correct={result.is_correct} "
                  f"type={result.detected_answer_type.value} "
                  f"pred={result.pred_value} notes={result.notes}")

        print("=== Pure numeric ===")
        check("exact match",
              score("FINAL ANSWER: 5.07\nUNIT: N", "5.07", "N"), True)
        check("close match",
              score("FINAL ANSWER: 5.08\nUNIT: N", "5.07", "N"), True)
        check("wrong",
              score("FINAL ANSWER: 99.0\nUNIT: N", "5.07", "N"), False)

        print("\n=== Scientific notation ===")
        check("caret format",
              score("FINAL ANSWER: 5.07 × 10^-6\nUNIT: C", "5.07 × 10^-6", "C"), True)
        check("e-notation pred",
              score("FINAL ANSWER: 5.07e-6\nUNIT: C", "5.07 × 10^-6", "C"), True)
        check("superscript gold",
              score("FINAL ANSWER: 5.07e6\nUNIT: Hz", "5.07 × 10⁶", "Hz"), True)
        check("wrong exponent",
              score("FINAL ANSWER: 5.07e-3\nUNIT: C", "5.07 × 10^-6", "C"), False)
        check("asterisk format",
              score("FINAL ANSWER: 2.707e-3\nUNIT: C", "2.707*10^-3", "C"), True)
        check("dot format",
              score("FINAL ANSWER: 4e-9\nUNIT: F", "4 . 10^{-9}", "F"), True)
        check("bare power",
              score("FINAL ANSWER: 10000\nUNIT: -", "10^4", "-"), True)
        check("latex \\times pred",
              score("FINAL ANSWER: $5.07 \\times 10^{-6}$\nUNIT: C", "5.07 * 10^{-6}", "C"), True)
        check("latex \\times no dollar",
              score("FINAL ANSWER: 2.027 \\times 10^{6}\nUNIT: V/m", "2.027 * 10^{6}", "V/m"), True)

        print("\n=== Yes/No ===")
        check("yes exact",
              score("FINAL ANSWER: Yes\nUNIT: -", "Yes", "—"), True)
        check("yes lowercase",
              score("FINAL ANSWER: yes\nUNIT: -", "Yes", "—"), True)
        check("no correct",
              score("FINAL ANSWER: No\nUNIT: -", "No", "—"), True)
        check("wrong choice",
              score("FINAL ANSWER: Yes\nUNIT: -", "No", "—"), False)

        print("\n=== Multi-value ===")
        check("both correct",
              score("FINAL ANSWER: 0.6; 1.2\nUNIT: cm", "0.6; 1.2", "cm"), True)
        check("reordered",
              score("FINAL ANSWER: 1.2; 0.6\nUNIT: cm", "0.6; 1.2", "cm"), True)
        check("partial",
              score("FINAL ANSWER: 0.6; 9.9\nUNIT: cm", "0.6; 1.2", "cm"), False)

        print("\n=== Text-only ===")
        check("substring match",
              score("FINAL ANSWER: Doubled\nUNIT: -", "Doubled", "-"), True)
        check("case insensitive",
              score("FINAL ANSWER: doubled\nUNIT: -", "Doubled", "-"), True)
        check("wrong text",
              score("FINAL ANSWER: Tripled\nUNIT: -", "Doubled", "-"), False)

        print("\n=== Mixed ===")
        check("numeric part",
              score("FINAL ANSWER: 20.0\nUNIT: Ω", "Rtd = 20.0", "Ω"), True)
        check("wrong numeric",
              score("FINAL ANSWER: 99.0\nUNIT: Ω", "Rtd = 20.0", "Ω"), False)

        print(f"\n{'='*40}\n{ok}/{total} tests passed")

    _test()
