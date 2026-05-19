"""Build a stratified sample of pure-numeric physics questions.

Usage:
    python -m app.physics_solution.data.prepare_sample \\
        --n 50 --seed 42 \\
        --csv "EXACT_Materials/Datasets/EXACT2026_dataset_2026-05-15/Physics_Problems_Text_Only/Physics_Problems_Text_Only.csv" \\
        --out app/physics_solution/data/sample_test.csv

A row is "pure numeric" iff `float(answer)` parses cleanly. This filters
out scientific notation (× 10^-3), text answers, Yes/No, multi-value, sqrt.

Stratification: proportional to the count of pure-numeric rows per domain
prefix (LD, CH, NL, TD, DDT, THCB, DT, CHLT). If a stratum has fewer
candidates than its quota we take all of them and redistribute the slack
to larger strata.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import numpy as np
import pandas as pd


PREFIX_RE = re.compile(r"^([A-Z]+)")


def domain_prefix(row_id: str) -> str:
    m = PREFIX_RE.match(str(row_id))
    return m.group(1) if m else "UNK"


def is_pure_numeric(ans: str) -> bool:
    if ans is None:
        return False
    s = str(ans).strip()
    if not s:
        return False
    # Reject obvious non-numeric markers cheaply before float() (faster + clearer).
    if any(ch in s for ch in [";", "×", "x10", "x 10", "sqrt", "\\sqrt", "π"]):
        return False
    if re.search(r"[a-zA-Z]", s):
        return False
    try:
        float(s)
        return True
    except ValueError:
        return False


def stratified_sample(df: pd.DataFrame, n: int, seed: int) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    df = df.copy()
    df["__prefix"] = df["id"].map(domain_prefix)

    counts = df["__prefix"].value_counts()
    total = counts.sum()
    # Initial proportional quota (round-down) then top-up with the largest
    # residuals.
    quotas = {}
    residuals = {}
    for prefix, c in counts.items():
        exact = n * c / total
        quotas[prefix] = int(np.floor(exact))
        residuals[prefix] = exact - quotas[prefix]
    deficit = n - sum(quotas.values())
    for prefix in sorted(residuals, key=residuals.get, reverse=True)[:deficit]:
        quotas[prefix] += 1

    picks = []
    leftover = 0
    # First pass: take min(quota, available).
    for prefix, quota in quotas.items():
        sub = df[df["__prefix"] == prefix]
        take = min(quota, len(sub))
        leftover += quota - take
        if take > 0:
            picks.append(sub.sample(n=take, random_state=int(rng.integers(0, 2**31 - 1))))

    # Redistribute leftover slack across remaining rows.
    if leftover:
        picked_ids = pd.concat(picks)["id"] if picks else pd.Series([], dtype=str)
        remaining = df[~df["id"].isin(picked_ids)]
        if len(remaining) >= leftover:
            picks.append(
                remaining.sample(n=leftover, random_state=int(rng.integers(0, 2**31 - 1)))
            )

    out = pd.concat(picks).drop(columns="__prefix").reset_index(drop=True)
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "--csv",
        default="EXACT_Materials/Datasets/EXACT2026_dataset_2026-05-15/Physics_Problems_Text_Only/Physics_Problems_Text_Only.csv",
    )
    parser.add_argument(
        "--n",
        type=int,
        default=973,
        help="Default 973 = all pure-numeric rows in the 2026-05-15 dataset. "
        "Set lower (e.g. 50) for fast smoke tests.",
    )
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--out",
        default="app/physics_solution/data/sample_test.csv",
    )
    args = parser.parse_args()

    src = pd.read_csv(args.csv)
    print(f"Loaded {len(src)} rows from {args.csv}")

    numeric = src[src["answer"].map(is_pure_numeric)].reset_index(drop=True)
    print(f"Pure-numeric rows: {len(numeric)}")

    sample = stratified_sample(numeric, n=args.n, seed=args.seed)
    print(f"Sampled {len(sample)} rows. Domain breakdown:")
    print(sample["id"].map(domain_prefix).value_counts().to_string())

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    sample.to_csv(out_path, index=False)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
