"""D-pre: rebuild the validation set (fix two problems with the old val_56).

Why this is needed
------------------
The original ``val_56.jsonl`` was frozen before the execution-grounded QC, so it
went stale:

1. **17/56 val problems were dropped by QC** — they have NO trajectory in
   ``trajectories_sft.jsonl``, so they can't give an eval-loss signal.
2. **56/60 golden problems DO have trajectories** in the SFT set. If we don't
   hold the 60 golden out of training, the golden accuracy is contaminated
   (the model trained on the exact eval problems). CLAUDE.md mandates the val
   split *include* (i.e. hold out) the 60 golden.

This script produces a fresh, honest val set:

* keep the surviving val problems (have a trajectory, not in golden_60),
* replace each dropped one with a **same (domain, answer_type)** problem that
  has a trajectory and is NOT in golden_60 (deterministic pick by sorted id),
* never overlap golden_60.

Every val problem therefore has at least one trajectory (eval-loss works) and is
held out from train (``build_sft.py`` excludes ``val ∪ golden_60`` from train).

Run:
    PYTHONPATH=. python -m app.physics_solution.versions.v07_final_version.make_val
"""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
V06_INPUT = HERE.parent / "v06_finetune" / "input" / "self_gen_dataset.jsonl"
TRAJ = HERE / "input" / "trajectories_sft.jsonl"
VAL_OUT = HERE / "val_56.jsonl"
GOLDEN_CSV = (
    HERE.parent.parent / "data" / "golden" / "golden_60.csv"
)


def _read_jsonl(path: Path) -> list[dict]:
    with open(path) as fh:
        return [json.loads(line) for line in fh if line.strip()]


def _golden_ids() -> set[str]:
    with open(GOLDEN_CSV, newline="") as fh:
        return {row["id"] for row in csv.DictReader(fh)}


def rebuild_val(write: bool = True) -> list[dict]:
    canonical = {r["id"]: r for r in _read_jsonl(V06_INPUT)}
    traj_src = {t["source_id"] for t in _read_jsonl(TRAJ)}
    golden = _golden_ids()
    current_val = _read_jsonl(VAL_OUT)

    # 1) survivors: in the old val, still have a trajectory, not a golden problem.
    survivors, missing = [], []
    for v in current_val:
        if v["id"] in traj_src and v["id"] not in golden:
            survivors.append(v)
        else:
            missing.append(v)

    chosen_ids = {v["id"] for v in survivors}

    # 2) candidate pool per (domain, answer_type): canonical problems that have a
    #    trajectory and are not golden. Deterministic order by id.
    pool: dict[tuple[str, str], list[str]] = defaultdict(list)
    for pid in sorted(canonical):
        if pid not in traj_src or pid in golden:
            continue
        r = canonical[pid]
        pool[(r["domain"], r["answer_type"])].append(pid)

    # 3) replace each missing problem with same-key candidate not already chosen.
    replacements: list[dict] = []
    for v in missing:
        key = (v["domain"], v["answer_type"])
        pick = next((pid for pid in pool.get(key, []) if pid not in chosen_ids), None)
        if pick is None:
            raise RuntimeError(
                f"No same-key replacement for {v['id']} key={key}. "
                f"Pool size={len(pool.get(key, []))}."
            )
        chosen_ids.add(pick)
        replacements.append(canonical[pick])

    new_val = survivors + replacements
    assert len(new_val) == len(current_val), (len(new_val), len(current_val))
    assert not ({v["id"] for v in new_val} & golden), "val leaks into golden_60"
    assert {v["id"] for v in new_val} <= traj_src, "a val problem has no trajectory"

    if write:
        with open(VAL_OUT, "w") as fh:
            for r in new_val:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    print(f"[make_val] survivors kept : {len(survivors)}")
    print(f"[make_val] dropped+replaced: {len(replacements)}")
    for v, r in zip(missing, replacements):
        print(f"    {v['id']:>12} ({v['domain']},{v['answer_type']}) -> {r['id']}")
    print(f"[make_val] wrote {len(new_val)} problems -> {VAL_OUT}")
    return new_val


if __name__ == "__main__":
    rebuild_val(write=True)
