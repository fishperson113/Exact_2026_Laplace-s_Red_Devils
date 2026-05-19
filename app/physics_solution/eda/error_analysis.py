"""Error analysis for inference results.

Categorises every wrong row into a *fail mode* so we can target fixes:

| Fail mode | Meaning |
|---|---|
| `format_no_final` | Completion never produced `FINAL ANSWER:` line. |
| `format_bad_number` | `FINAL ANSWER` present but extractor couldn't parse a float. |
| `off_by_power10` | Predicted number is gold × 10^k for some k ≠ 0 (forgot SI prefix). |
| `wrong_sign` | Predicted sign opposite gold. |
| `unit_mismatch` | Numeric correct (or close) but unit string disagrees with gold. |
| `magnitude_wrong` | Predicted within an order of magnitude but not close enough (1-1000× off). |
| `numeric_far` | Predicted is qualitatively wrong (≥ 1000× off). |
| `suspect_gold` | Predicted matches a *common alternative interpretation* of the problem — possible gold-label issue. |

Each row gets a single primary `fail_mode`. `format_*` modes take priority over numeric ones.

Usage:
    from app.physics_solution.eda.error_analysis import analyse
    report = analyse('app/physics_solution/results/v02_fewshot.csv')
    report.write('docs/eda/v02_error_report.md')
"""

from __future__ import annotations

import math
import re
from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd


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
    # Common unicode unifications.
    s = s.replace("μ", "u").replace("µ", "u")  # μ, µ -> u
    s = s.replace("Ω", "ohm").replace("ω", "ohm")
    s = s.replace("—", "-").replace("–", "-")
    s = re.sub(r"\s+", "", s)
    return s


def classify_row(row: pd.Series) -> str:
    """Return one fail-mode tag for a wrong row."""
    completion = str(row.get("completion", ""))
    if not FINAL_RE.search(completion):
        return "format_no_final"

    pred = row.get("pred_numeric")
    if pred is None or (isinstance(pred, float) and math.isnan(pred)):
        return "format_bad_number"

    gold = _to_float(row.get("gold_answer"))
    if gold is None:
        # Non-numeric gold — we shouldn't be here because the test set is
        # pure-numeric, but be defensive.
        return "format_bad_number"

    pred_f = float(pred)
    if gold != 0 and pred_f != 0 and (pred_f * gold < 0):
        return "wrong_sign"

    if gold == 0:
        return "magnitude_wrong" if abs(pred_f) > 1e-4 else "unit_mismatch"

    ratio = abs(pred_f / gold)
    log_ratio = math.log10(ratio) if ratio > 0 else float("inf")

    # Off-by-power-of-10 (forgot unit prefix conversion).
    near_int = abs(log_ratio - round(log_ratio))
    if abs(round(log_ratio)) >= 1 and near_int < 0.05:
        return "off_by_power10"

    # If pred numerically close (within 2%) the only thing wrong is the unit.
    if math.isclose(pred_f, gold, rel_tol=2e-2, abs_tol=1e-4):
        pu = _normalise_unit(row.get("pred_unit"))
        gu = _normalise_unit(row.get("gold_unit"))
        if pu != gu and pu and gu:
            return "unit_mismatch"
        # Close but not within our default tolerance — call it unit_ish.
        return "unit_mismatch"

    if 0.1 <= ratio <= 10:
        return "magnitude_wrong"
    return "numeric_far"


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
            "## Fail-mode breakdown",
            "",
            "| Fail mode | Count | % of wrong |",
            "|---|---:|---:|",
        ]
        wrong = max(self.wrong, 1)
        for mode, cnt in sorted(self.failmode_counts.items(), key=lambda kv: -kv[1]):
            lines.append(f"| `{mode}` | {cnt} | {cnt / wrong:.1%} |")

        if self.domain_breakdown is not None:
            lines += [
                "",
                "## Per-domain accuracy",
                "",
                self.domain_breakdown.to_markdown(index=False),
            ]

        if self.domain_x_failmode is not None and not self.domain_x_failmode.empty:
            lines += [
                "",
                "## Fail mode × domain",
                "",
                self.domain_x_failmode.to_markdown(),
            ]

        if self.examples_per_mode:
            lines += ["", "## Sample wrong rows per mode", ""]
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
    df["fail_mode"] = df.apply(
        lambda r: "correct" if r.get("is_correct") else classify_row(r),
        axis=1,
    )

    wrong_df = df[df["fail_mode"] != "correct"].copy()
    failmode_counts = wrong_df["fail_mode"].value_counts().to_dict()

    # Per-domain accuracy table
    counts = df.groupby("domain").size().rename("n")
    correct = df.groupby("domain")["is_correct"].sum().rename("correct")
    acc = (correct / counts).rename("accuracy")
    domain_breakdown = (
        pd.concat([counts, correct, acc], axis=1)
        .reset_index()
        .sort_values("n", ascending=False)
    )
    domain_breakdown["accuracy"] = domain_breakdown["accuracy"].round(3)

    # Fail mode × domain matrix
    if not wrong_df.empty:
        domain_x_failmode = (
            wrong_df.groupby(["fail_mode", "domain"]).size().unstack(fill_value=0)
        )
    else:
        domain_x_failmode = pd.DataFrame()

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
