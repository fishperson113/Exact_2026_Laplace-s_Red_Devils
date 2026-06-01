"""Materialize the canonical 60-question golden eval set as a CSV.

The "60 golden" set v05_best is scored on exists ONLY embedded in
`versions/v05_best/output/results_golden_60.json` (all 60 ids are electrostatics
`LD*`). v06 needs it as a real CSV so run.py can eval against the exact same set
for an apples-to-apples comparison with v05_best (58.3%).

This pulls the 60 ids (in their original eval order) from the JSON, joins the
full rows (`id, question, cot, answer, unit`) from the golden CSV, and appends a
canonical `domain` column. Output: app/physics_solution/data/golden/golden_60.csv

Run (from repo root):
    python -m app.physics_solution.versions.v06_finetune.data_pipeline.extract_golden60
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

from app.physics_solution.config import GOLDEN_TEST_FILE, repo_root
from app.physics_solution.versions.v06_finetune.data_pipeline.taxonomy import (
    domain_from_id,
)

RESULTS_60_JSON = (
    "app/physics_solution/versions/v05_best/output/results_golden_60.json"
)
OUT_CSV = "app/physics_solution/data/golden/golden_60.csv"
FIELDS = ["id", "question", "cot", "answer", "unit", "domain"]


def load_golden_60_ids(json_path: Path) -> list[str]:
    """The 60 eval ids, in the order v05_best scored them."""
    data = json.loads(json_path.read_text(encoding="utf-8"))
    rows = data.get("rows", [])
    return [str(r["id"]) for r in rows]


def load_golden_rows_by_id(csv_path: Path) -> dict[str, dict]:
    with open(csv_path, "r", encoding="utf-8", newline="") as f:
        return {r["id"]: r for r in csv.DictReader(f)}


def main() -> None:
    root = repo_root()
    json_path = root / RESULTS_60_JSON
    csv_path = root / GOLDEN_TEST_FILE
    out_path = root / OUT_CSV

    ids = load_golden_60_ids(json_path)
    by_id = load_golden_rows_by_id(csv_path)

    out_rows: list[dict] = []
    missing: list[str] = []
    for qid in ids:
        src = by_id.get(qid)
        if src is None:
            missing.append(qid)
            continue
        out_rows.append(
            {
                "id": qid,
                "question": src.get("question", ""),
                "cot": src.get("cot", ""),
                "answer": src.get("answer", ""),
                "unit": src.get("unit", ""),
                "domain": domain_from_id(qid) or "",
            }
        )

    if missing:
        print(f"WARNING: {len(missing)} ids in the 60-set not found in golden CSV: {missing}")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(out_rows)

    domains = {}
    for r in out_rows:
        domains[r["domain"]] = domains.get(r["domain"], 0) + 1
    print(f"Wrote {len(out_rows)} rows -> {out_path}")
    print(f"Domain breakdown: {domains}")
    if len(out_rows) != 60:
        print(f"NOTE: expected 60 rows, got {len(out_rows)}.", file=sys.stderr)


if __name__ == "__main__":
    main()
