"""Sample a balanced subset from golden data for faster iteration.

Usage:
  python -m app.physics_solution.data.sample_golden                          # default: 200 rows
  python -m app.physics_solution.data.sample_golden --n 100                  # custom size
  python -m app.physics_solution.data.sample_golden --results path/to/results.json  # stratify by correct/incorrect

Output: app/physics_solution/data/golden/sampled_test.csv
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
import re
from collections import defaultdict
from pathlib import Path

GOLDEN_PATH = Path("app/physics_solution/data/golden/deepseek-v4-pro_golden_data.csv")
OUTPUT_PATH = Path("app/physics_solution/data/golden/sampled_test.csv")
PREFIX_RE = re.compile(r"^([A-Z]+)")
SEED = 42


def _detect_answer_type(answer: str) -> str:
    """Heuristic answer type detection from gold answer string."""
    answer = answer.strip()
    if answer.lower() in ("yes", "no", "có", "không"):
        return "yes_no"
    if ";" in answer:
        return "multi_value"
    if re.search(r"10\^", answer):
        return "sci_notation"
    if re.search(r"[a-zA-ZÀ-ỹ]{3,}", answer):
        return "text_only"
    try:
        float(answer.replace(",", "."))
        return "pure_numeric"
    except ValueError:
        return "mixed"


def _get_domain(row_id: str) -> str:
    m = PREFIX_RE.match(row_id)
    return m.group(1) if m else "UNKNOWN"


def sample(
    n: int = 200,
    results_path: str | None = None,
    seed: int = SEED,
) -> list[dict]:
    """Sample n rows from golden data, stratified by domain.

    If results_path is given, also stratifies by correct/incorrect,
    keeping ~70% incorrect to focus evaluation on hard cases.
    """
    random.seed(seed)

    with open(GOLDEN_PATH, encoding="utf-8") as f:
        all_rows = list(csv.DictReader(f))

    # Add metadata
    for row in all_rows:
        row["_domain"] = _get_domain(row["id"])
        row["_answer_type"] = _detect_answer_type(row.get("answer", ""))

    # Load results if available
    correct_ids: set[str] = set()
    wrong_ids: set[str] = set()
    if results_path:
        with open(results_path, encoding="utf-8") as f:
            results = json.load(f)
        for r in results.get("rows", []):
            if r.get("is_correct"):
                correct_ids.add(str(r["id"]))
            else:
                wrong_ids.add(str(r["id"]))
        print(f"Loaded results: {len(correct_ids)} correct, {len(wrong_ids)} wrong")

    # Group by domain
    by_domain: dict[str, list[dict]] = defaultdict(list)
    for row in all_rows:
        by_domain[row["_domain"]].append(row)

    # Calculate per-domain sample sizes (proportional)
    total = len(all_rows)
    domain_n: dict[str, int] = {}
    for domain, rows in sorted(by_domain.items()):
        # Proportional allocation, min 5
        allocated = max(5, round(n * len(rows) / total))
        domain_n[domain] = min(allocated, len(rows))

    # Adjust to hit target n
    current_total = sum(domain_n.values())
    if current_total < n:
        # Add more from largest domains
        for domain in sorted(by_domain, key=lambda d: len(by_domain[d]), reverse=True):
            if current_total >= n:
                break
            can_add = len(by_domain[domain]) - domain_n[domain]
            add = min(can_add, n - current_total)
            domain_n[domain] += add
            current_total += add
    elif current_total > n:
        # Remove from smallest domains
        for domain in sorted(by_domain, key=lambda d: len(by_domain[d])):
            if current_total <= n:
                break
            can_remove = domain_n[domain] - 5
            remove = min(can_remove, current_total - n)
            domain_n[domain] -= remove
            current_total -= remove

    # Sample within each domain
    sampled: list[dict] = []
    for domain, rows in sorted(by_domain.items()):
        target = domain_n[domain]

        if results_path and (correct_ids or wrong_ids):
            # Stratify by correct/incorrect: keep 70% incorrect
            wrong = [r for r in rows if r["id"] in wrong_ids]
            correct = [r for r in rows if r["id"] in correct_ids]
            unknown = [r for r in rows if r["id"] not in wrong_ids and r["id"] not in correct_ids]

            n_wrong = min(len(wrong), math.ceil(target * 0.7))
            n_correct = min(len(correct), target - n_wrong)
            n_unknown = min(len(unknown), target - n_wrong - n_correct)

            random.shuffle(wrong)
            random.shuffle(correct)
            random.shuffle(unknown)

            selected = wrong[:n_wrong] + correct[:n_correct] + unknown[:n_unknown]

            # Fill remaining if short
            remaining = [r for r in rows if r not in selected]
            random.shuffle(remaining)
            if len(selected) < target:
                selected += remaining[: target - len(selected)]
        else:
            # No results: stratify by answer_type within domain
            by_type: dict[str, list[dict]] = defaultdict(list)
            for r in rows:
                by_type[r["_answer_type"]].append(r)

            selected = []
            # Ensure at least 1 from each answer type present
            for atype, type_rows in by_type.items():
                random.shuffle(type_rows)
                selected.append(type_rows[0])

            # Fill remaining proportionally
            remaining = [r for r in rows if r not in selected]
            random.shuffle(remaining)
            selected += remaining[: target - len(selected)]

        sampled.extend(selected[:target])

    random.shuffle(sampled)

    # Print summary
    print(f"\nSampled {len(sampled)} / {total} rows")
    print(f"\nDomain distribution:")
    domain_counts = defaultdict(int)
    type_counts = defaultdict(int)
    for row in sampled:
        domain_counts[row["_domain"]] += 1
        type_counts[row["_answer_type"]] += 1
    for domain in sorted(domain_counts):
        orig = len(by_domain[domain])
        print(f"  {domain:6s}: {domain_counts[domain]:3d} / {orig} ({domain_counts[domain]/orig*100:.0f}%)")

    print(f"\nAnswer type distribution:")
    for atype in sorted(type_counts):
        print(f"  {atype:15s}: {type_counts[atype]}")

    if results_path and (correct_ids or wrong_ids):
        n_wrong_sampled = sum(1 for r in sampled if r["id"] in wrong_ids)
        n_correct_sampled = sum(1 for r in sampled if r["id"] in correct_ids)
        print(f"\nCorrectness split: {n_wrong_sampled} wrong, {n_correct_sampled} correct")

    return sampled


def main():
    parser = argparse.ArgumentParser(description="Sample balanced golden test subset")
    parser.add_argument("--n", type=int, default=200, help="Target sample size")
    parser.add_argument(
        "--results",
        default=None,
        help="Path to results.json for correct/incorrect stratification",
    )
    parser.add_argument("--seed", type=int, default=SEED)
    parser.add_argument("--out", default=None, help="Output path (default: sampled_test.csv)")
    args = parser.parse_args()

    sampled = sample(n=args.n, results_path=args.results, seed=args.seed)

    out_path = Path(args.out) if args.out else OUTPUT_PATH
    out_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = ["id", "question", "cot", "answer", "unit"]
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(sampled)

    print(f"\nWrote {out_path} ({len(sampled)} rows)")


if __name__ == "__main__":
    main()
