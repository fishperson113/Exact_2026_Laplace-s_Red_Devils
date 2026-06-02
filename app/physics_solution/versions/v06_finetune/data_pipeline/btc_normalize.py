"""BTC golden -> normalized ProblemSpec JSONL.

The BTC (organizer) set is already English with reliable `answer`/`unit` (only its
CoT is unreliable, and v06 regenerates that anyway). So this branch is light:

  load golden CSV -> assign canonical domain (from id) + answer_type (from gold)
                  -> reshape to ProblemSpec  [offline]
                  -> Step-0 filter (DeepSeek flash): drop figure/underspecified/theory
                  -> write input/btc_normalized.jsonl (kept)
                     + output/btc_dropped.jsonl (DROPPED rows + reason -- audit trail)

The original CoT is preserved in `meta.cot` (a hint for the Phase-2 teacher route).

Run (from repo root; needs DEEPSEEK_API_KEY):
    python -m app.physics_solution.versions.v06_finetune.data_pipeline.btc_normalize
    python -m ...btc_normalize --limit 20 --concurrency 8        # small batch
    python -m ...btc_normalize --no-filter                        # offline reshape only
"""

from __future__ import annotations

import argparse
import asyncio
import csv

from app.physics_solution.config import COMMERCIAL_MODEL_FLASH, GOLDEN_TEST_FILE, repo_root
from app.physics_solution.shared.eval.scorer import detect_answer_type
from app.physics_solution.shared.router import _ANSWER_TYPE_ALIASES
from app.physics_solution.versions.v06_finetune.data_pipeline import ds_client
from app.physics_solution.versions.v06_finetune.data_pipeline.filter import (
    build_filter_messages,
    parse_filter,
)
from app.physics_solution.versions.v06_finetune.data_pipeline.schema import (
    ProblemSpec,
    read_jsonl,
    write_jsonl,
)
from app.physics_solution.versions.v06_finetune.data_pipeline.taxonomy import domain_from_id

OUT_KEPT = "app/physics_solution/versions/v06_finetune/input/btc_normalized.jsonl"
OUT_DROPPED = "app/physics_solution/versions/v06_finetune/output/btc_dropped.jsonl"


def _load(path) -> list[dict]:
    """Load a JSONL file if it exists, else []."""
    return list(read_jsonl(path)) if path.exists() else []


def _answer_type_from_gold(gold_answer: str) -> str:
    """6-way scorer type -> 4-way ProblemSpec type (numeric/yes_no/multi_value/text)."""
    raw = detect_answer_type(gold_answer).value  # e.g. "pure_numeric", "sci_notation"
    return _ANSWER_TYPE_ALIASES.get(raw, raw)


def load_specs(csv_path, limit: int | None = None) -> list[ProblemSpec]:
    """Offline: load golden CSV into ProblemSpec list (no API)."""
    specs: list[ProblemSpec] = []
    with open(csv_path, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    if limit:
        rows = rows[:limit]
    for r in rows:
        qid = str(r["id"])
        specs.append(
            ProblemSpec(
                id=qid,
                question=str(r["question"]),
                domain=domain_from_id(qid) or "",
                answer_type=_answer_type_from_gold(str(r.get("answer", ""))),
                gold_answer=str(r.get("answer", "")),
                gold_unit=str(r.get("unit", "")),
                dataset_source="btc_golden",
                meta={"cot": str(r.get("cot", ""))},
            )
        )
    return specs


async def _run(args) -> None:
    root = repo_root()
    csv_path = root / GOLDEN_TEST_FILE
    specs = load_specs(csv_path, args.limit)

    no_domain = [s.id for s in specs if not s.domain]
    print(f"Loaded {len(specs)} BTC rows. Unmapped-domain: {len(no_domain)}")
    dist: dict[str, int] = {}
    for s in specs:
        dist[s.domain or "?"] = dist.get(s.domain or "?", 0) + 1
    print(f"Domain distribution: {dist}")

    spec_by_id = {s.id: s for s in specs}
    kept_path, dropped_path = root / OUT_KEPT, root / OUT_DROPPED

    if args.no_filter:
        write_jsonl(kept_path, specs)
        print(f"[no-filter] wrote {len(specs)} specs -> {OUT_KEPT}")
        return

    # --- resume: skip ids already kept/dropped from a previous run ---
    existing_kept = [] if args.fresh else _load(kept_path)
    existing_dropped = [] if args.fresh else _load(dropped_path)
    done_ids = {r["id"] for r in existing_kept} | {r["id"] for r in existing_dropped}
    todo = [s for s in specs if s.id not in done_ids]
    items = [{"id": s.id, "question": s.question} for s in todo]
    print(f"Already done: {len(done_ids)} | to process: {len(items)}")
    if not items:
        print("Nothing to do (all ids already processed; use --fresh to redo).")
        return

    def _parse(item: dict, text: str) -> dict:
        v = parse_filter(text)
        v["id"] = item["id"]
        return v

    # --- auto-save: rebuild + write the real kept/dropped files every 50 ---
    def _save(results: list[dict]) -> None:
        kept = [dict(r) for r in existing_kept]
        dropped = list(existing_dropped)
        for r in results:
            if "__error__" in r:  # API failed after retries -> keep conservatively
                s = spec_by_id[r["__item__"]["id"]]
                kept.append(s.to_dict())
            elif r.get("solvable", True):
                kept.append(spec_by_id[r["id"]].to_dict())
            else:
                s = spec_by_id[r["id"]]
                dropped.append({"id": s.id, "question": s.question, "reason": r.get("reason", "")})
        write_jsonl(kept_path, kept)
        write_jsonl(dropped_path, dropped)

    await ds_client.run_batch(
        items, lambda it: build_filter_messages(it["question"]), _parse,
        model=args.model, concurrency=args.concurrency, on_progress=_save, save_every=50,
    )
    n_kept = len(_load(kept_path))
    n_dropped = len(_load(dropped_path))
    print(f"\nKept {n_kept} -> {OUT_KEPT}")
    print(f"Dropped {n_dropped} (audit) -> {OUT_DROPPED}")


def main() -> None:
    p = argparse.ArgumentParser(description="Normalize BTC golden -> ProblemSpec JSONL")
    p.add_argument("--limit", type=int, default=None)
    p.add_argument("--concurrency", type=int, default=10)
    p.add_argument("--model", default=COMMERCIAL_MODEL_FLASH)
    p.add_argument("--no-filter", action="store_true", help="Offline reshape only (no API).")
    p.add_argument("--fresh", action="store_true",
                   help="Ignore existing output and redo from scratch (default: resume).")
    args = p.parse_args()
    asyncio.run(_run(args))


if __name__ == "__main__":
    main()
