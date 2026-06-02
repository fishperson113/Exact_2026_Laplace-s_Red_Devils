"""Compare original test data answers against golden data.

Usage (from repo root):
    python -m app.physics_solution.shared.eval.compare_golden --golden path/to/golden.csv
    python -m app.physics_solution.shared.eval.compare_golden --golden path/to/golden.csv --diff-csv diffs.csv
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

from app.physics_solution.config import GOLDEN_DIR, TEST_FILE, repo_root
from app.physics_solution.shared.eval.scorer import (
    AnswerType,
    _parse_sci_notation,
    _safe_float,
    detect_answer_type,
    numeric_close,
)

# ------------------------------------------------------------------ domain extraction

_DOMAIN_RE = re.compile(r"^([A-Z]+)")

DOMAIN_NAMES = {
    "LD": "Luc dien (Coulomb)",
    "DT": "Dien truong (E-field)",
    "CH": "Mach dien AC (RLC)",
    "NL": "Nang luong (Energy/LC)",
    "TD": "Tu dien (Capacitor)",
    "DDT": "Dien tu (EM induction)",
    "THCB": "Tong hop co ban",
    "CHLT": "Cau hoi ly thuyet",
}


def get_domain(qid: str) -> str:
    m = _DOMAIN_RE.match(qid)
    return m.group(1) if m else "UNKNOWN"


# ------------------------------------------------------------------ comparison

def answers_match(orig: str, golden: str) -> tuple[bool, str]:
    """Compare two answer strings, returning (match, note)."""
    orig = str(orig).strip()
    golden = str(golden).strip()

    if not orig or not golden:
        return False, "empty"

    atype_orig = detect_answer_type(orig)
    atype_gold = detect_answer_type(golden)

    if atype_orig == AnswerType.YES_NO or atype_gold == AnswerType.YES_NO:
        match = orig.lower() == golden.lower()
        return match, "yes_no"

    if atype_orig == AnswerType.MULTI_VALUE or atype_gold == AnswerType.MULTI_VALUE:
        orig_parts = sorted([p.strip() for p in orig.split(";") if p.strip()])
        gold_parts = sorted([p.strip() for p in golden.split(";") if p.strip()])

        orig_floats = [_safe_float(p) for p in orig_parts]
        gold_floats = [_safe_float(p) for p in gold_parts]

        if all(f is not None for f in orig_floats) and all(f is not None for f in gold_floats):
            if len(orig_floats) != len(gold_floats):
                return False, f"multi_value count {len(orig_floats)} vs {len(gold_floats)}"
            matches = sum(
                1 for o, g in zip(sorted(orig_floats), sorted(gold_floats))
                if numeric_close(o, g)
            )
            return matches == len(gold_floats), f"multi_value {matches}/{len(gold_floats)}"

        return orig_parts == gold_parts, "multi_value text"

    if atype_orig == AnswerType.SCI_NOTATION or atype_gold == AnswerType.SCI_NOTATION:
        o_f = _parse_sci_notation(orig)
        g_f = _parse_sci_notation(golden)
        if o_f is not None and g_f is not None:
            return numeric_close(o_f, g_f), "sci_notation"
        return False, "sci_notation parse fail"

    o_f = _safe_float(orig)
    g_f = _safe_float(golden)
    if o_f is not None and g_f is not None:
        return numeric_close(o_f, g_f), "numeric"

    return orig.lower() == golden.lower(), "text"


# ------------------------------------------------------------------ I/O

def load_csv(path: Path) -> dict[str, dict]:
    with open(path, "r", encoding="utf-8", newline="") as f:
        return {row["id"]: row for row in csv.DictReader(f)}


# ------------------------------------------------------------------ main

def main() -> None:
    parser = argparse.ArgumentParser(description="Compare original vs golden data")
    parser.add_argument("--golden", required=True, help="Path to golden data CSV (e.g. data/golden/gpt-5.4-mini_golden_data.csv)")
    parser.add_argument("--diff-csv", default=None, help="Path for CSV of differing rows")
    args = parser.parse_args()

    root = repo_root()
    golden_path = Path(args.golden)
    if not golden_path.is_absolute():
        golden_path = root / golden_path

    orig_data = load_csv(root / TEST_FILE)
    golden_data = load_csv(golden_path)

    common_ids = sorted(set(orig_data) & set(golden_data))
    print(f"Original: {len(orig_data)} rows | Golden: {len(golden_data)} rows | Common: {len(common_ids)}\n")

    match_count = 0
    diff_count = 0
    domain_stats: dict[str, dict[str, int]] = defaultdict(lambda: {"match": 0, "diff": 0, "total": 0})
    diffs: list[dict] = []

    for qid in common_ids:
        orig = orig_data[qid]
        gold = golden_data[qid]
        domain = get_domain(qid)
        domain_stats[domain]["total"] += 1

        ans_match, note = answers_match(orig.get("answer", ""), gold.get("answer", ""))

        if ans_match:
            match_count += 1
            domain_stats[domain]["match"] += 1
        else:
            diff_count += 1
            domain_stats[domain]["diff"] += 1
            diffs.append({
                "id": qid,
                "domain": domain,
                "orig_answer": orig.get("answer", ""),
                "golden_answer": gold.get("answer", ""),
                "orig_unit": orig.get("unit", ""),
                "golden_unit": gold.get("unit", ""),
                "compare_note": note,
            })

    total = match_count + diff_count
    pct = match_count / total * 100 if total else 0

    print("=" * 60)
    print(f"  TOTAL:   {total}")
    print(f"  MATCH:   {match_count} ({pct:.1f}%)")
    print(f"  DIFFER:  {diff_count} ({100 - pct:.1f}%)")
    print("=" * 60)

    print(f"\n{'Domain':<8} {'Name':<25} {'Total':>6} {'Match':>6} {'Diff':>6} {'Acc%':>7}")
    print("-" * 60)
    for domain in sorted(domain_stats):
        s = domain_stats[domain]
        acc = s["match"] / s["total"] * 100 if s["total"] else 0
        name = DOMAIN_NAMES.get(domain, "")
        print(f"{domain:<8} {name:<25} {s['total']:>6} {s['match']:>6} {s['diff']:>6} {acc:>6.1f}%")

    if args.diff_csv and diffs:
        diff_path = Path(args.diff_csv)
        diff_path.parent.mkdir(parents=True, exist_ok=True)
        with open(diff_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=list(diffs[0].keys()))
            writer.writeheader()
            writer.writerows(diffs)
        print(f"\nDiff details saved to {diff_path}")

    if not args.diff_csv and diffs:
        print(f"\nTip: add --diff-csv diffs.csv to export {len(diffs)} differing rows.")


if __name__ == "__main__":
    main()
