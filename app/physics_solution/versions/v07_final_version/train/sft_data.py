"""Load output/{train,val}.jsonl (chat `messages`) -> HF DatasetDict with a
rendered `text` field, using the tokenizer's chat template so the Qwen special
tokens (<|im_start|>/<|im_end|>) are exactly right. train_on_responses_only then
masks everything before the assistant header at train time.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from datasets import Dataset, DatasetDict


def _read_jsonl(path: str | Path) -> list[dict]:
    with open(path) as fh:
        return [json.loads(line) for line in fh if line.strip()]


def load_datasets(cfg: dict, tokenizer: Any) -> DatasetDict:
    paths = cfg["paths"]

    def render(example: dict) -> dict:
        # add_generation_prompt=False -> include the assistant turn + closing
        # <|im_end|> so the model learns to stop.
        text = tokenizer.apply_chat_template(
            example["messages"], tokenize=False, add_generation_prompt=False
        )
        return {"text": text}

    out = {}
    for split, key in (("train", "train_jsonl"), ("val", "val_jsonl")):
        rows = _read_jsonl(paths[key])
        ds = Dataset.from_list(rows)
        ds = ds.map(render, desc=f"render {split}")
        out[split] = ds
    dd = DatasetDict(out)
    print(f"[sft_data] train={len(dd['train'])} val={len(dd['val'])}")
    print("[sft_data] sample rendered text head:\n" + dd["train"][0]["text"][:400])
    return dd
