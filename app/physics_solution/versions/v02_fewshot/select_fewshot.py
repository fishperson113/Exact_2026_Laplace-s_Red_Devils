"""Curate a small set of few-shot examples from golden data.

Strategy:
- Source from DeepSeek-rewritten golden data (high-quality CoT).
- Prefer pure-numeric answers for cleaner few-shot demonstrations.
- Exclude any ID that appears in the test set (no leakage).
- For each domain prefix, pick K examples whose CoT step count is near
  the domain median — avoids both 2-step trivia and 13-step monsters.

Output: `examples.json` next to this script, used at inference time by
`prompt.py`.

Usage:
    python -m app.physics_solution.versions.v02_fewshot.select_fewshot \\
        --k 2

    # Re-roll with a different seed / different K:
    python -m app.physics_solution.versions.v02_fewshot.select_fewshot \\
        --k 3 --seed 7
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import numpy as np
import pandas as pd


PREFIX_RE = re.compile(r"^([A-Z]+)")
HERE = Path(__file__).resolve().parent


def domain_prefix(row_id: str) -> str:
    m = PREFIX_RE.match(str(row_id))
    return m.group(1) if m else "UNK"


def is_pure_numeric(ans: str) -> bool:
    if ans is None:
        return False
    s = str(ans).strip()
    if not s or any(ch in s for ch in [";", "×", "x10", "x 10", "sqrt", "\\sqrt", "π"]):
        return False
    if re.search(r"[a-zA-Z]", s):
        return False
    try:
        float(s)
        return True
    except ValueError:
        return False


def cot_step_count(cot: str) -> int:
    return len(re.findall(r"(?im)^\s*step\s*\d+", cot))


def format_assistant_response(cot: str, answer: str, unit: str) -> str:
    """Reshape a dataset CoT into our strict response format."""
    cot = cot.strip()
    unit = (unit or "").strip()
    return f"{cot}\n\nFINAL ANSWER: {answer}\nUNIT: {unit}"


def pick_for_domain(sub: pd.DataFrame, k: int, rng: np.random.Generator) -> pd.DataFrame:
    sub = sub.copy()
    sub["__steps"] = sub["cot"].fillna("").map(cot_step_count)
    if sub["__steps"].max() == 0:
        return sub.sample(n=min(k, len(sub)), random_state=int(rng.integers(0, 2**31 - 1)))

    median = sub["__steps"].median()
    sub["__dist"] = (sub["__steps"] - median).abs()
    # Take the closest 3*k candidates then sample k from them to add a bit of
    # diversity without picking the same examples every time.
    pool = sub.nsmallest(min(3 * k, len(sub)), "__dist")
    return pool.sample(n=min(k, len(pool)), random_state=int(rng.integers(0, 2**31 - 1)))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "--csv",
        default="app/physics_solution/data/golden/deepseek-v4-pro_golden_data.csv",
    )
    parser.add_argument(
        "--exclude",
        default="app/physics_solution/data/test/sample_test.csv",
        help="Test CSV whose IDs must be excluded from the few-shot pool.",
    )
    parser.add_argument("--k", type=int, default=2, help="Examples per domain.")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--out",
        default=str(HERE / "input" / "examples.json"),
    )
    args = parser.parse_args()

    src = pd.read_csv(args.csv)
    excl_ids = set()
    if Path(args.exclude).exists():
        excl_ids = set(pd.read_csv(args.exclude)["id"].astype(str))
    print(f"Excluding {len(excl_ids)} test IDs")

    src = src[~src["id"].astype(str).isin(excl_ids)].copy()
    # Prefer pure-numeric examples for cleaner few-shot demonstrations.
    # Fall back to mixed if the pure-numeric pool is too small.
    pn = src[src["answer"].map(is_pure_numeric)]
    if len(pn) >= args.k * 7:  # ~K per domain × 7 domains
        src = pn.copy()
        pool_kind = "pure-numeric"
    else:
        src = src[src["answer"].notna() & src["cot"].notna()].copy()
        pool_kind = "mixed (pure-numeric pool too small)"
    src["__prefix"] = src["id"].map(domain_prefix)
    print(
        f"Candidate pool: {len(src)} rows ({pool_kind}) across "
        f"{src['__prefix'].nunique()} domains"
    )

    rng = np.random.default_rng(args.seed)
    picks: list[pd.DataFrame] = []
    for prefix, sub in src.groupby("__prefix"):
        picks.append(pick_for_domain(sub, args.k, rng))

    chosen = pd.concat(picks).sort_values("__prefix").reset_index(drop=True)
    out_rows = []
    for _, row in chosen.iterrows():
        out_rows.append(
            {
                "id": str(row["id"]),
                "prefix": row["__prefix"],
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
    print(f"Wrote {len(out_rows)} examples to {out_path}")
    print("Breakdown:", chosen["__prefix"].value_counts().to_dict())


if __name__ == "__main__":
    main()
