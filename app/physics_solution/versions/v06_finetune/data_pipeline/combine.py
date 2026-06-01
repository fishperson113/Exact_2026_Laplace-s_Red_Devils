"""Merge the two normalized ProblemSpec sets into one combined JSONL.

Inputs (produced by btc_normalize.py + vietjack_normalize.py):
    input/btc_normalized.jsonl
    input/vietjack_normalized.jsonl
Output:
    input/problems_all.jsonl   (BTC + Vietjack, the Phase-2 trajectory-gen input)

Run (from repo root):
    python -m app.physics_solution.versions.v06_finetune.data_pipeline.combine
"""

from __future__ import annotations

from app.physics_solution.config import repo_root
from app.physics_solution.versions.v06_finetune.data_pipeline.schema import (
    read_jsonl,
    write_jsonl,
)

BTC = "app/physics_solution/versions/v06_finetune/input/btc_normalized.jsonl"
VIETJACK = "app/physics_solution/versions/v06_finetune/input/vietjack_normalized.jsonl"
OUT = "app/physics_solution/versions/v06_finetune/input/problems_all.jsonl"


def main() -> None:
    root = repo_root()
    merged: list[dict] = []
    counts: dict[str, int] = {}
    for path in (root / BTC, root / VIETJACK):
        if not path.exists():
            print(f"WARNING: missing {path} — skipping (run its normalizer first).")
            continue
        rows = list(read_jsonl(path))
        merged.extend(rows)
        counts[path.name] = len(rows)

    write_jsonl(root / OUT, merged)
    by_src: dict[str, int] = {}
    by_domain: dict[str, int] = {}
    for r in merged:
        by_src[r.get("dataset_source", "?")] = by_src.get(r.get("dataset_source", "?"), 0) + 1
        by_domain[r.get("domain", "?")] = by_domain.get(r.get("domain", "?"), 0) + 1
    print(f"Inputs: {counts}")
    print(f"Wrote {len(merged)} -> {OUT}")
    print(f"By source: {by_src}")
    print(f"By domain: {by_domain}")


if __name__ == "__main__":
    main()
