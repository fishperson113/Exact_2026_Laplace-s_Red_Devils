"""D: build the SFT train/val splits in Qwen chat-message format.

Reads the execution-verified trajectory set and emits two JSONL files where each
row is one chat conversation (``messages`` = system / user / assistant):

    system    = GEN_SYSTEM (the data_pipeline generation prompt)
    user      = the PLAIN problem block (build_gen_messages) — NO hint, even for
                hinted-route rows, because at inference the model never sees a hint
    assistant = the trajectory's `assistant` field (5-10 line reasoning + ONE
                code block) — the SFT target

We store ``messages`` (not a pre-rendered string) so the training side applies
the tokenizer's chat template itself (correct ``<|im_start|>`` / ``<|im_end|>``
tokens) and masks the prompt (train-on-completion).

Split rule (honest eval):
    * source_id in golden_60        -> DROP   (golden is the held-out test;
                                               evaluated by running the model on
                                               golden_60.csv, must not be trained)
    * source_id in val_56           -> val.jsonl  (eval-loss + accuracy)
    * otherwise                     -> train.jsonl

Run:
    PYTHONPATH=. python -m app.physics_solution.versions.v07_final_version.build_sft
"""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

from app.physics_solution.versions.v06_finetune.data_pipeline.prompts import (
    build_gen_messages,
)

HERE = Path(__file__).resolve().parent
TRAJ = HERE / "input" / "trajectories_sft.jsonl"
VAL = HERE / "val_56.jsonl"
GOLDEN_CSV = HERE.parent.parent / "data" / "golden" / "golden_60.csv"
OUT_DIR = HERE / "output"

# fields carried alongside `messages` for eval / bookkeeping
_META = ("id", "source_id", "domain", "answer_type", "gold_answer", "gold_unit",
         "dataset_source")


def _read_jsonl(path: Path) -> list[dict]:
    with open(path) as fh:
        return [json.loads(line) for line in fh if line.strip()]


def _golden_ids() -> set[str]:
    with open(GOLDEN_CSV, newline="") as fh:
        return {row["id"] for row in csv.DictReader(fh)}


def _to_row(t: dict) -> dict:
    """One trajectory -> a chat-format SFT row."""
    msgs = build_gen_messages(t["question"], t["domain"], t["answer_type"])
    msgs = msgs + [{"role": "assistant", "content": t["assistant"]}]
    row = {k: t.get(k) for k in _META}
    row["messages"] = msgs
    return row


def build(write: bool = True) -> dict:
    traj = _read_jsonl(TRAJ)
    val_ids = {v["id"] for v in _read_jsonl(VAL)}
    golden = _golden_ids()

    train, val, dropped = [], [], 0
    for t in traj:
        sid = t["source_id"]
        if sid in golden:
            dropped += 1
            continue
        (val if sid in val_ids else train).append(_to_row(t))

    if write:
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        for name, rows in (("train.jsonl", train), ("val.jsonl", val)):
            with open(OUT_DIR / name, "w") as fh:
                for r in rows:
                    fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    stats = {
        "train_rows": len(train),
        "val_rows": len(val),
        "dropped_golden_traj": dropped,
        "train_problems": len({r["source_id"] for r in train}),
        "val_problems": len({r["source_id"] for r in val}),
        "train_domains": dict(Counter(r["domain"] for r in train)),
        "val_domains": dict(Counter(r["domain"] for r in val)),
    }
    # leak guards
    train_src = {r["source_id"] for r in train}
    assert not (train_src & val_ids), "train leaks val problems"
    assert not (train_src & golden), "train leaks golden problems"

    print(json.dumps(stats, indent=2, ensure_ascii=False))
    if write:
        print(f"[build_sft] wrote {OUT_DIR/'train.jsonl'} and {OUT_DIR/'val.jsonl'}")
    return stats


if __name__ == "__main__":
    build(write=True)
