"""Build a stratified sample of physics questions.

Usage:
    # Default (backward compatible): pure-numeric only
    python -m app.physics_solution.cli.prepare_sample \\
        --n 973 --seed 42

    # Full dataset (all answer types)
    python -m app.physics_solution.cli.prepare_sample \\
        --n 1352 --seed 42 --answer-types all

    # Specific subset
    python -m app.physics_solution.cli.prepare_sample \\
        --n 200 --answer-types pure_numeric,sci_notation

Stratification: proportional to the count of eligible rows per domain
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

from app.physics_solution.shared.eval.scorer import AnswerType, detect_answer_type


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
    if any(ch in s for ch in [";", "×", "x10", "x 10", "sqrt", "\\sqrt", "π"]):
        return False
    if re.search(r"[a-zA-Z]", s):
        return False
    try:
        float(s)
        return True
    except ValueError:
        return False


def filter_by_answer_types(
    df: pd.DataFrame,
    answer_types: list[str] | None,
) -> pd.DataFrame:
    """Filter dataframe by answer types. None or ['pure_numeric'] uses the legacy filter."""
    if answer_types is None or answer_types == ["pure_numeric"]:
        return df[df["answer"].map(is_pure_numeric)].reset_index(drop=True)

    valid_types = {t.value for t in AnswerType}
    requested = set(answer_types)
    invalid = requested - valid_types - {"all"}
    if invalid:
        raise ValueError(f"Unknown answer types: {invalid}. Valid: {sorted(valid_types)} or 'all'")

    if "all" in requested:
        return df.reset_index(drop=True)

    df = df.copy()
    df["__answer_type"] = df["answer"].map(lambda a: detect_answer_type(str(a)).value)
    filtered = df[df["__answer_type"].isin(requested)].drop(columns="__answer_type")
    return filtered.reset_index(drop=True)


def stratified_sample(df: pd.DataFrame, n: int, seed: int) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    df = df.copy()
    df["__prefix"] = df["id"].map(domain_prefix)

    counts = df["__prefix"].value_counts()
    total = counts.sum()
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
    for prefix, quota in quotas.items():
        sub = df[df["__prefix"] == prefix]
        take = min(quota, len(sub))
        leftover += quota - take
        if take > 0:
            picks.append(sub.sample(n=take, random_state=int(rng.integers(0, 2**31 - 1))))

    if leftover:
        picked_ids = pd.concat(picks)["id"] if picks else pd.Series([], dtype=str)
        remaining = df[~df["id"].isin(picked_ids)]
        if len(remaining) >= leftover:
            picks.append(
                remaining.sample(n=leftover, random_state=int(rng.integers(0, 2**31 - 1)))
            )

    out = pd.concat(picks).drop(columns="__prefix").reset_index(drop=True)
    return out


def _parse_answer_types(raw: str | None) -> list[str] | None:
    if raw is None:
        return None
    return [t.strip() for t in raw.split(",") if t.strip()]


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
        default="app/physics_solution/data/test/sample_test.csv",
    )
    parser.add_argument(
        "--answer-types",
        default=None,
        help="Comma-separated answer types to include: "
        "pure_numeric,sci_notation,yes_no,multi_value,text_only,mixed "
        "or 'all' for full dataset. Default: pure_numeric only.",
    )
    args = parser.parse_args()

    src = pd.read_csv(args.csv)
    print(f"Loaded {len(src)} rows from {args.csv}")

    answer_types = _parse_answer_types(args.answer_types)
    eligible = filter_by_answer_types(src, answer_types)

    type_label = "all types" if answer_types and "all" in answer_types else (
        ", ".join(answer_types) if answer_types else "pure_numeric"
    )
    print(f"Eligible rows ({type_label}): {len(eligible)}")

    n = min(args.n, len(eligible))
    sample = stratified_sample(eligible, n=n, seed=args.seed)
    print(f"Sampled {len(sample)} rows. Domain breakdown:")
    print(sample["id"].map(domain_prefix).value_counts().to_string())

    if answer_types and "all" in answer_types:
        at_dist = sample["answer"].map(lambda a: detect_answer_type(str(a)).value)
        print(f"\nAnswer type breakdown:")
        print(at_dist.value_counts().to_string())

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    sample.to_csv(out_path, index=False)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
