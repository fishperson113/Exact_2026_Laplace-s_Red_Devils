"""Curate few-shot examples keyed by (domain, answer_type).

Extends v02's logic:
- Covers ALL answer types present in each domain (not just pure_numeric).
- Each example gets an `answer_type` label via `detect_answer_type()`.
- Key = (prefix, answer_type) -> pick K examples whose CoT step count
  is near the median for that group.
- Excludes full_test.csv IDs to prevent leakage.

Output: `input/examples.json` with field `answer_type` on every example.

Usage:
    python -m app.physics_solution.versions.v03_routed_fewshot.select_fewshot \\
        --k 2 --seed 42
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import numpy as np
import pandas as pd

from app.physics_solution.shared.eval.scorer import AnswerType, detect_answer_type


PREFIX_RE = re.compile(r"^([A-Z]+)")
HERE = Path(__file__).resolve().parent


def domain_prefix(row_id: str) -> str:
    m = PREFIX_RE.match(str(row_id))
    return m.group(1) if m else "UNK"


def cot_step_count(cot: str) -> int:
    return len(re.findall(r"(?im)^\s*step\s*\d+", cot))


def format_assistant_response(cot: str, answer: str, unit: str) -> str:
    cot = cot.strip()
    unit = (unit or "").strip()
    return f"{cot}\n\nFINAL ANSWER: {answer}\nUNIT: {unit}"


def pick_for_group(sub: pd.DataFrame, k: int, rng: np.random.Generator) -> pd.DataFrame:
    if len(sub) == 0:
        return sub
    sub = sub.copy()
    sub["__steps"] = sub["cot"].fillna("").map(cot_step_count)
    if sub["__steps"].max() == 0:
        return sub.sample(n=min(k, len(sub)), random_state=int(rng.integers(0, 2**31 - 1)))

    median = sub["__steps"].median()
    sub["__dist"] = (sub["__steps"] - median).abs()
    pool = sub.nsmallest(min(3 * k, len(sub)), "__dist")
    return pool.sample(n=min(k, len(pool)), random_state=int(rng.integers(0, 2**31 - 1)))


def main() -> None:
    parser = argparse.ArgumentParser(description="Curate (domain, answer_type) few-shot examples for v03")
    parser.add_argument(
        "--csv",
        default="EXACT_Materials/Datasets/EXACT2026_dataset_2026-05-15/Physics_Problems_Text_Only/Physics_Problems_Text_Only.csv",
    )
    parser.add_argument(
        "--exclude",
        default="",
        help="Test CSV whose IDs must be excluded. Empty = no exclusion "
        "(run.py handles per-question exclusion at inference time).",
    )
    parser.add_argument("--k", type=int, default=2, help="Examples per (domain, answer_type) group.")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--out",
        default=str(HERE / "input" / "examples.json"),
    )
    args = parser.parse_args()

    src = pd.read_csv(args.csv)
    excl_ids = set()
    if args.exclude and Path(args.exclude).exists():
        excl_ids = set(pd.read_csv(args.exclude)["id"].astype(str))
    print(f"Excluding {len(excl_ids)} test IDs")

    src = src[~src["id"].astype(str).isin(excl_ids)].copy()
    src = src[src["answer"].notna() & src["cot"].notna()].copy()
    src["__prefix"] = src["id"].map(domain_prefix)
    src["__answer_type"] = src["answer"].astype(str).map(
        lambda a: detect_answer_type(a).value
    )
    print(
        f"Candidate pool: {len(src)} rows across "
        f"{src['__prefix'].nunique()} domains, "
        f"{src['__answer_type'].nunique()} answer types"
    )
    print("Groups:")
    print(src.groupby(["__prefix", "__answer_type"]).size().to_string())

    rng = np.random.default_rng(args.seed)
    picks: list[pd.DataFrame] = []
    for (prefix, atype), sub in src.groupby(["__prefix", "__answer_type"]):
        picked = pick_for_group(sub, args.k, rng)
        if len(picked) > 0:
            picks.append(picked)

    chosen = pd.concat(picks).sort_values(["__prefix", "__answer_type"]).reset_index(drop=True)
    out_rows = []
    for _, row in chosen.iterrows():
        out_rows.append(
            {
                "id": str(row["id"]),
                "prefix": row["__prefix"],
                "answer_type": row["__answer_type"],
                "question": str(row["question"]).strip(),
                "cot": str(row["cot"]).strip(),
                "answer": str(row["answer"]).strip(),
                "unit": str(row.get("unit", "")).strip(),
                "formatted_assistant": format_assistant_response(
                    str(row["cot"]),
                    str(row["answer"]),
                    str(row.get("unit", "")),
                ),
            }
        )

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out_rows, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nWrote {len(out_rows)} examples to {out_path}")
    breakdown = chosen.groupby(["__prefix", "__answer_type"]).size()
    print("Breakdown:")
    print(breakdown.to_string())


if __name__ == "__main__":
    main()
