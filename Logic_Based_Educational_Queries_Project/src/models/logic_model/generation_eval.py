"""Đánh giá greedy (Answer:) trên split có `eval_prompt` / `gold_answer`."""
from __future__ import annotations

from typing import Any

import torch

from evaluation.metrics import answer_accuracy, extract_answer_from_completion
from services.config import LogicSFTConfig


@torch.no_grad()
def accuracy_on_dataset(
    cfg: LogicSFTConfig,
    model,
    tokenizer,
    ds,
    max_samples: int | None = None,
) -> float:
    """Đo accuracy (parse Answer:) trên split bất kỳ có eval_prompt + gold_answer."""
    model.eval()
    device = next(model.parameters()).device
    n = len(ds)
    idxs = list(range(n))
    if max_samples is not None:
        idxs = idxs[: min(max_samples, n)]
    preds: list[str] = []
    golds: list[str] = []
    bs = max(1, cfg.eval_gen_batch_size)
    for start in range(0, len(idxs), bs):
        batch_i = idxs[start : start + bs]
        prompts = [ds[i]["eval_prompt"] for i in batch_i]
        gold_raw = [ds[i]["gold_answer"] for i in batch_i]
        enc = tokenizer(
            prompts,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=cfg.max_seq_length,
        )
        enc = {k: v.to(device) for k, v in enc.items()}
        pad_id = tokenizer.pad_token_id or tokenizer.eos_token_id
        out = model.generate(
            **enc,
            max_new_tokens=cfg.gen_max_new_tokens,
            do_sample=False,
            pad_token_id=pad_id,
            eos_token_id=tokenizer.eos_token_id,
        )
        in_len = enc["input_ids"].shape[1]
        for row, g in zip(out, gold_raw):
            gen_ids = row[in_len:]
            text = tokenizer.decode(gen_ids, skip_special_tokens=True)
            preds.append(extract_answer_from_completion(text))
            golds.append(str(g))
    return answer_accuracy(preds, golds)


@torch.no_grad()
def collect_inference_samples(
    cfg: LogicSFTConfig,
    model,
    tokenizer,
    ds,
    n: int,
    *,
    max_samples_cap: int | None = None,
) -> list[dict[str, Any]]:
    """Một vài ví dụ inference (gold vs pred) để đính kèm log / Hub."""
    if n <= 0:
        return []
    model.eval()
    device = next(model.parameters()).device
    out: list[dict[str, Any]] = []
    limit = min(n, len(ds))
    if max_samples_cap is not None:
        limit = min(limit, max_samples_cap)
    for i in range(limit):
        prompt = ds[i]["eval_prompt"]
        gold = str(ds[i]["gold_answer"])
        enc = tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=cfg.max_seq_length,
        )
        enc = {k: v.to(device) for k, v in enc.items()}
        pad_id = tokenizer.pad_token_id or tokenizer.eos_token_id
        gen_out = model.generate(
            **enc,
            max_new_tokens=cfg.gen_max_new_tokens,
            do_sample=False,
            pad_token_id=pad_id,
            eos_token_id=tokenizer.eos_token_id,
        )
        gen_ids = gen_out[0, enc["input_ids"].shape[1] :]
        text = tokenizer.decode(gen_ids, skip_special_tokens=True)
        try:
            pred = extract_answer_from_completion(text)
        except ValueError as e:
            pred = f"<parse_error: {e}>"
        row: dict[str, Any] = {
            "split_index": i,
            "gold_answer": gold,
            "predicted_label": pred,
            "completion_raw": text[:2000],
        }
        for key in ("record_id", "q_idx"):
            if key in ds.column_names:
                row[key] = ds[i][key]
        out.append(row)
    return out
