"""Error analysis for inference results.

Categorises every wrong row into a *fail mode* so we can target fixes.
Supports all answer types via branching on AnswerType from the scorer.

Fail modes (pure_numeric / sci_notation path):
| Fail mode           | Meaning |
|---------------------|---------|
| format_no_final     | Completion never produced `FINAL ANSWER:` line. |
| format_bad_number   | `FINAL ANSWER` present but extractor couldn't parse a float. |
| off_by_power10      | Predicted number is gold × 10^k for some k ≠ 0. |
| wrong_sign          | Predicted sign opposite gold. |
| unit_mismatch       | Numeric correct (or close) but unit string disagrees. |
| magnitude_wrong     | Within an order of magnitude but not close enough. |
| numeric_far         | Qualitatively wrong (≥ 1000× off). |
| sci_scale_wrong     | Sci-notation mantissa close but exponent wrong. |
| formula_off         | Ratio outside 10× AND not a power-of-10 multiple. |
| wrong_subquestion   | Pred matches a number extracted from the question text. |
| suspect_gold        | Pred matches a question number — possible gold-label issue. |

Non-numeric fail modes:
| wrong_choice        | yes_no: answered the opposite. |
| partial_match       | multi_value: some values correct, not all. |
| count_wrong         | multi_value: wrong number of values. |
| lexically_wrong     | text_only: text doesn't match gold. |

Usage:
    python -m app.physics_solution.eda.scripts.v2.error_analysis results.csv --out report.md
"""

from __future__ import annotations

import math
import re
from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd

from app.physics_solution.shared.eval.scorer import (
    AnswerType,
    detect_answer_type,
    extract,
    numeric_close,
    _parse_sci_notation,
    _NUM_RE,
)


PREFIX_RE = re.compile(r"^([A-Z]+)")
FINAL_RE = re.compile(r"FINAL\s*ANSWER\s*:", re.IGNORECASE)


def _domain(qid: str) -> str:
    m = PREFIX_RE.match(str(qid))
    return m.group(1) if m else "UNK"


def _to_float(s) -> float | None:
    try:
        return float(str(s).strip())
    except (ValueError, TypeError):
        return None


def _normalise_unit(u: str | None) -> str:
    if u is None:
        return ""
    s = str(u).strip().lower()
    s = s.replace("μ", "u").replace("µ", "u")
    s = s.replace("Ω", "ohm").replace("ω", "ohm")
    s = s.replace("—", "-").replace("–", "-")
    s = re.sub(r"\s+", "", s)
    return s


def _numbers_in_text(text: str) -> set[float]:
    """Extract all numbers from a text string."""
    nums = set()
    for m in _NUM_RE.finditer(str(text)):
        try:
            nums.add(float(m.group(0)))
        except ValueError:
            pass
    return nums


def _check_suspect_gold(pred_f: float, question: str) -> str | None:
    """If pred matches a number in the question, return an explanation."""
    q_nums = _numbers_in_text(question)
    if not q_nums:
        return None
    for qn in q_nums:
        if qn != 0 and numeric_close(pred_f, qn, rel_tol=1e-2, abs_tol=1e-4):
            return f"pred {pred_f} matches question number {qn}"
    return None


# ---------------------------------------------------------------- classify by type


def _classify_numeric(row: pd.Series, pred_f: float, gold_f: float) -> str:
    """Shared classification for pure_numeric and sci_notation (numeric path)."""
    question = str(row.get("question", ""))

    suspect = _check_suspect_gold(pred_f, question)
    if suspect:
        return "wrong_subquestion"

    if gold_f != 0 and pred_f != 0 and (pred_f * gold_f < 0):
        return "wrong_sign"

    if gold_f == 0:
        return "magnitude_wrong" if abs(pred_f) > 1e-4 else "unit_mismatch"

    ratio = abs(pred_f / gold_f)
    log_ratio = math.log10(ratio) if ratio > 0 else float("inf")

    if not math.isinf(log_ratio):
        near_int = abs(log_ratio - round(log_ratio))
        if abs(round(log_ratio)) >= 1 and near_int < 0.05:
            return "off_by_power10"

    if math.isclose(pred_f, gold_f, rel_tol=2e-2, abs_tol=1e-4):
        pu = _normalise_unit(row.get("pred_unit"))
        gu = _normalise_unit(row.get("gold_unit"))
        if pu != gu and pu and gu:
            return "unit_mismatch"
        return "unit_mismatch"

    if 0.1 <= ratio <= 10:
        return "magnitude_wrong"

    return "numeric_far"


def _classify_pure_numeric(row: pd.Series) -> str:
    completion = str(row.get("completion", ""))
    if not FINAL_RE.search(completion):
        return "format_no_final"

    pred = row.get("pred_numeric")
    if pred is None or (isinstance(pred, float) and math.isnan(pred)):
        return "format_bad_number"

    gold = _to_float(row.get("gold_answer"))
    if gold is None:
        return "format_bad_number"

    return _classify_numeric(row, float(pred), gold)


def _classify_sci_notation(row: pd.Series) -> str:
    completion = str(row.get("completion", ""))
    if not FINAL_RE.search(completion):
        return "format_no_final"

    extracted = extract(completion)
    gold_f = _parse_sci_notation(str(row.get("gold_answer", "")))
    if gold_f is None:
        return "format_bad_number"

    pred_f = None
    if extracted.raw_answer:
        pred_f = _parse_sci_notation(extracted.raw_answer)
    if pred_f is None:
        pred_f = extracted.numeric
    if pred_f is None or (isinstance(pred_f, float) and math.isnan(pred_f)):
        return "format_bad_number"

    # sci_scale_wrong: mantissa close but exponent different
    gold_str = str(row.get("gold_answer", ""))
    gold_sci = _parse_sci_notation(gold_str)
    if gold_sci and gold_sci != 0 and pred_f != 0:
        gold_mag = math.floor(math.log10(abs(gold_sci)))
        pred_mag = math.floor(math.log10(abs(pred_f)))
        if gold_mag != pred_mag:
            gold_mantissa = gold_sci / (10 ** gold_mag)
            pred_mantissa = pred_f / (10 ** pred_mag)
            if math.isclose(abs(gold_mantissa), abs(pred_mantissa), rel_tol=0.1):
                return "sci_scale_wrong"

    base_mode = _classify_numeric(row, pred_f, gold_f)

    # formula_off: ratio outside 10× AND not a power-of-10 multiple
    if base_mode == "numeric_far" and gold_f != 0 and pred_f != 0:
        ratio = abs(pred_f / gold_f)
        log_ratio = math.log10(ratio)
        near_int = abs(log_ratio - round(log_ratio))
        if near_int >= 0.05:
            return "formula_off"

    return base_mode


def _classify_yes_no(row: pd.Series) -> str:
    completion = str(row.get("completion", ""))
    if not FINAL_RE.search(completion):
        return "format_no_final"
    return "wrong_choice"


def _classify_multi_value(row: pd.Series) -> str:
    completion = str(row.get("completion", ""))
    if not FINAL_RE.search(completion):
        return "format_no_final"

    extracted = extract(completion)
    gold_parts = [p.strip() for p in str(row.get("gold_answer", "")).split(";") if p.strip()]
    pred_raw = extracted.raw_answer or ""
    pred_parts = [p.strip() for p in re.split(r"[;,]", pred_raw) if p.strip()]

    if len(pred_parts) != len(gold_parts):
        return "count_wrong"

    gold_floats = [_to_float(p) for p in gold_parts]
    pred_floats = [_to_float(p) for p in pred_parts]
    if all(g is not None for g in gold_floats) and all(p is not None for p in pred_floats):
        matches = sum(
            1 for g, p in zip(sorted(gold_floats), sorted(pred_floats))
            if numeric_close(p, g)
        )
        if matches > 0:
            return "partial_match"

    return "count_wrong"


def _classify_text_only(row: pd.Series) -> str:
    completion = str(row.get("completion", ""))
    if not FINAL_RE.search(completion):
        return "format_no_final"
    return "lexically_wrong"


def _classify_mixed(row: pd.Series) -> str:
    completion = str(row.get("completion", ""))
    if not FINAL_RE.search(completion):
        return "format_no_final"

    extracted = extract(completion)
    gold_answer = str(row.get("gold_answer", ""))
    nums_in_gold = _NUM_RE.findall(gold_answer)
    gold_f = _to_float(nums_in_gold[0]) if nums_in_gold else None

    if gold_f is not None and extracted.numeric is not None:
        return _classify_numeric(row, extracted.numeric, gold_f)

    return "lexically_wrong"


_CLASSIFY_DISPATCH = {
    AnswerType.PURE_NUMERIC: _classify_pure_numeric,
    AnswerType.SCI_NOTATION: _classify_sci_notation,
    AnswerType.YES_NO:       _classify_yes_no,
    AnswerType.MULTI_VALUE:  _classify_multi_value,
    AnswerType.TEXT_ONLY:    _classify_text_only,
    AnswerType.MIXED:        _classify_mixed,
}


def classify_row(row: pd.Series) -> str:
    """Return one fail-mode tag for a wrong row, branching by answer type."""
    gold_answer = str(row.get("gold_answer", ""))
    answer_type = detect_answer_type(gold_answer)
    classifier = _CLASSIFY_DISPATCH.get(answer_type, _classify_pure_numeric)
    return classifier(row)


# ---------------------------------------------------------------- suspect gold


def find_suspect_gold(df: pd.DataFrame, top_n: int = 15) -> list[dict]:
    """Find rows where prediction matches a number in the question text."""
    suspects = []
    for _, row in df.iterrows():
        if row.get("is_correct"):
            continue
        pred = row.get("pred_numeric")
        if pred is None or (isinstance(pred, float) and math.isnan(pred)):
            continue
        question = str(row.get("question", ""))
        explain = _check_suspect_gold(float(pred), question)
        if explain:
            suspects.append({
                "id": row.get("id", ""),
                "gold_answer": row.get("gold_answer", ""),
                "pred_numeric": pred,
                "gold_unit": row.get("gold_unit", ""),
                "question": question[:200],
                "explain": explain,
            })
    suspects.sort(key=lambda x: str(x["id"]))
    return suspects[:top_n]


# ---------------------------------------------------------------------- public API


@dataclass
class AnalysisReport:
    version: str
    total: int
    correct: int
    wrong: int
    accuracy: float
    failmode_counts: dict[str, int] = field(default_factory=dict)
    domain_breakdown: pd.DataFrame | None = None
    domain_x_failmode: pd.DataFrame | None = None
    wrong_df: pd.DataFrame | None = None
    examples_per_mode: dict[str, list[dict]] = field(default_factory=dict)
    answer_type_breakdown: pd.DataFrame | None = None
    failmode_x_answer_type: pd.DataFrame | None = None
    domain_x_answer_type: pd.DataFrame | None = None
    suspect_gold_cases: list[dict] = field(default_factory=list)

    def write(self, out_path: str | Path) -> Path:
        out_path = Path(out_path)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(self.to_markdown(), encoding="utf-8")
        return out_path

    def to_markdown(self) -> str:
        lines = [
            f"# Error analysis — {self.version}",
            "",
            f"- **Total:** {self.total}",
            f"- **Correct:** {self.correct} ({self.accuracy:.3f})",
            f"- **Wrong:** {self.wrong}",
            "",
        ]

        # Section 1: Per-answer-type accuracy
        if self.answer_type_breakdown is not None:
            lines += [
                "## 1. Per-answer-type accuracy",
                "",
                self.answer_type_breakdown.to_markdown(index=False),
                "",
            ]

        # Section 2: Fail-mode breakdown
        lines += [
            "## 2. Fail-mode breakdown",
            "",
            "| Fail mode | Count | % of wrong |",
            "|---|---:|---:|",
        ]
        wrong = max(self.wrong, 1)
        for mode, cnt in sorted(self.failmode_counts.items(), key=lambda kv: -kv[1]):
            lines.append(f"| `{mode}` | {cnt} | {cnt / wrong:.1%} |")

        # Section 3: Fail mode × domain
        if self.domain_breakdown is not None:
            lines += [
                "",
                "## 3. Per-domain accuracy",
                "",
                self.domain_breakdown.to_markdown(index=False),
            ]

        if self.domain_x_failmode is not None and not self.domain_x_failmode.empty:
            lines += [
                "",
                "## 4. Fail mode × domain",
                "",
                self.domain_x_failmode.to_markdown(),
            ]

        # Section 5: Fail mode × answer_type (NEW)
        if self.failmode_x_answer_type is not None and not self.failmode_x_answer_type.empty:
            lines += [
                "",
                "## 5. Fail mode × answer type",
                "",
                self.failmode_x_answer_type.to_markdown(),
            ]

        # Section 6: Domain × answer_type (NEW)
        if self.domain_x_answer_type is not None and not self.domain_x_answer_type.empty:
            lines += [
                "",
                "## 6. Domain × answer type",
                "",
                self.domain_x_answer_type.to_markdown(),
            ]

        # Section 7: Suspect gold cases (NEW)
        if self.suspect_gold_cases:
            lines += [
                "",
                "## 7. Top suspect gold cases",
                "",
                "Rows where the model's prediction matches a number from the question text,",
                "suggesting the model may have copied a given value instead of computing the answer.",
                "",
            ]
            for i, case in enumerate(self.suspect_gold_cases, 1):
                lines += [
                    f"### {i}. `{case['id']}`",
                    f"- **Gold:** `{case['gold_answer']}` (unit: `{case['gold_unit']}`)",
                    f"- **Pred:** `{case['pred_numeric']}`",
                    f"- **Explain:** {case['explain']}",
                    f"- **Q:** {case.get('question', '')[:200]}",
                    "",
                ]

        # Sample wrong rows
        if self.examples_per_mode:
            lines += ["", "## 8. Sample wrong rows per mode", ""]
            for mode, examples in self.examples_per_mode.items():
                lines += [f"### `{mode}`", ""]
                for ex in examples:
                    lines += [
                        f"- **{ex['id']}** gold=`{ex['gold_answer']}` "
                        f"pred=`{ex['pred_numeric']}` unit_gold=`{ex['gold_unit']}` "
                        f"unit_pred=`{ex['pred_unit']}`"
                    ]
                    q = (ex.get("question") or "")[:200]
                    if q:
                        lines.append(f"  - Q: {q}")
                lines.append("")

        # Section 9: Conclusions
        lines += [
            "",
            "## 9. Conclusions",
            "",
            "### Route priority for Stage 2+",
            "",
        ]
        if self.answer_type_breakdown is not None:
            lines.append("Based on per-answer-type accuracy, prioritize routing for types with lowest accuracy.")
            lines.append("")
        lines += [
            "- **yes_no / text_only:** Likely 0% with current numeric pipeline — needs dedicated classifier.",
            "- **sci_notation:** May benefit from notation-aware extraction.",
            "- **multi_value:** Requires structured output parsing.",
            "- **pure_numeric:** Baseline established — focus on reducing magnitude_wrong and off_by_power10.",
            "",
        ]

        return "\n".join(lines)


def analyse(
    csv_path: str | Path,
    *,
    n_examples_per_mode: int = 3,
    version_label: str | None = None,
) -> AnalysisReport:
    """Read a results CSV (or JSON-rows file) and produce an AnalysisReport."""
    path = Path(csv_path)
    if path.suffix == ".json":
        import json

        data = json.loads(path.read_text(encoding="utf-8"))
        df = pd.DataFrame(data.get("rows", []))
    else:
        df = pd.read_csv(path)
    if df.empty:
        raise ValueError(f"No rows in {path}")

    df["domain"] = df["id"].map(_domain)
    df["answer_type"] = df["gold_answer"].map(
        lambda g: detect_answer_type(str(g)).value
    )

    from app.physics_solution.shared.eval.scorer import score as rescore, extract
    def _rescore(row):
        completion = str(row.get("completion", ""))
        gold_answer = str(row.get("gold_answer", ""))
        gold_unit = str(row.get("gold_unit", ""))
        result = rescore(completion, gold_answer, gold_unit)
        return result.is_correct
    df["is_correct"] = df.apply(_rescore, axis=1)

    def _reextract_numeric(row):
        ext = extract(str(row.get("completion", "")))
        return ext.numeric
    df["pred_numeric"] = df.apply(_reextract_numeric, axis=1)

    df["fail_mode"] = df.apply(
        lambda r: "correct" if r.get("is_correct") else classify_row(r),
        axis=1,
    )

    wrong_df = df[df["fail_mode"] != "correct"].copy()
    failmode_counts = wrong_df["fail_mode"].value_counts().to_dict()

    # Per-domain accuracy
    counts = df.groupby("domain").size().rename("n")
    correct_col = df.groupby("domain")["is_correct"].sum().rename("correct")
    acc = (correct_col / counts).rename("accuracy")
    domain_breakdown = (
        pd.concat([counts, correct_col, acc], axis=1)
        .reset_index()
        .sort_values("n", ascending=False)
    )
    domain_breakdown["accuracy"] = domain_breakdown["accuracy"].round(3)

    # Fail mode × domain
    if not wrong_df.empty:
        domain_x_failmode = (
            wrong_df.groupby(["fail_mode", "domain"]).size().unstack(fill_value=0)
        )
    else:
        domain_x_failmode = pd.DataFrame()

    # Per-answer-type accuracy (NEW)
    at_counts = df.groupby("answer_type").size().rename("n")
    at_correct = df.groupby("answer_type")["is_correct"].sum().rename("correct")
    at_acc = (at_correct / at_counts).rename("accuracy")
    answer_type_breakdown = (
        pd.concat([at_counts, at_correct, at_acc], axis=1)
        .reset_index()
        .sort_values("n", ascending=False)
    )
    answer_type_breakdown["accuracy"] = answer_type_breakdown["accuracy"].round(3)

    # Fail mode × answer_type (NEW)
    if not wrong_df.empty:
        failmode_x_answer_type = (
            wrong_df.groupby(["fail_mode", "answer_type"]).size().unstack(fill_value=0)
        )
    else:
        failmode_x_answer_type = pd.DataFrame()

    # Domain × answer_type (NEW)
    domain_x_answer_type = (
        df.groupby(["domain", "answer_type"]).size().unstack(fill_value=0)
    )

    # Suspect gold (NEW)
    suspect_gold_cases = find_suspect_gold(df, top_n=15)

    # Sample examples per fail mode
    examples_per_mode: dict[str, list[dict]] = {}
    for mode, group in wrong_df.groupby("fail_mode"):
        sample = group.head(n_examples_per_mode)
        examples_per_mode[mode] = sample[
            ["id", "gold_answer", "pred_numeric", "gold_unit", "pred_unit", "question"]
        ].to_dict("records")

    version = version_label or path.stem
    return AnalysisReport(
        version=version,
        total=len(df),
        correct=int(df["is_correct"].sum()),
        wrong=len(wrong_df),
        accuracy=float(df["is_correct"].mean()),
        failmode_counts=failmode_counts,
        domain_breakdown=domain_breakdown,
        domain_x_failmode=domain_x_failmode,
        wrong_df=wrong_df,
        examples_per_mode=examples_per_mode,
        answer_type_breakdown=answer_type_breakdown,
        failmode_x_answer_type=failmode_x_answer_type,
        domain_x_answer_type=domain_x_answer_type,
        suspect_gold_cases=suspect_gold_cases,
    )


# ---------------------------------------------------------------------- CLI


def main() -> None:
    import argparse

    p = argparse.ArgumentParser(description="Categorise wrong inference rows.")
    p.add_argument("results", help="Path to results CSV (or JSON).")
    p.add_argument("--out", default=None, help="Markdown report destination.")
    p.add_argument(
        "--examples-per-mode",
        type=int,
        default=3,
        help="How many sample rows to show per fail mode.",
    )
    args = p.parse_args()

    report = analyse(args.results, n_examples_per_mode=args.examples_per_mode)
    print(report.to_markdown())
    if args.out:
        report.write(args.out)
        print(f"\nWrote: {args.out}")


if __name__ == "__main__":
    main()
