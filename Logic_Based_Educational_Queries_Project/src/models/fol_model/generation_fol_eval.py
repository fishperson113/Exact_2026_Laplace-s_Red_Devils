"""Đánh giá greedy: so khớp JSON premises_fol với nhãn assistant."""
from __future__ import annotations

import json
import re
from typing import Any

import torch

from services.config_fol import FolSFTConfig


def _normalize_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip())


def _parse_premises_fol_list(text: str) -> list[str] | None:
    t = text.strip()
    if not t:
        return None
    try:
        data = json.loads(t)
    except json.JSONDecodeError:
        start = t.find("{")
        end = t.rfind("}")
        if start == -1 or end <= start:
            return None
        try:
            data = json.loads(t[start : end + 1])
        except json.JSONDecodeError:
            return None
    if not isinstance(data, dict):
        return None
    lst = data.get("premises_fol")
    if not isinstance(lst, list):
        return None
    out: list[str] = []
    for x in lst:
        if not isinstance(x, str):
            return None
        out.append(_normalize_ws(x))
    return out


def _lists_exact_match(a: list[str], b: list[str]) -> bool:
    if len(a) != len(b):
        return False
    return all(x == y for x, y in zip(a, b, strict=True))


@torch.no_grad()
def fol_exact_match_rate(
    cfg: FolSFTConfig,
    model,
    tokenizer,
    ds,
    max_samples: int | None = None,
) -> dict[str, Any]:
    model.eval()
    device = next(model.parameters()).device
    n = len(ds)
    idxs = list(range(n))
    if max_samples is not None:
        idxs = idxs[: min(max_samples, n)]
    ok = 0
    total = len(idxs)
    bs = max(1, cfg.eval_gen_batch_size)
    for start in range(0, len(idxs), bs):
        batch_i = idxs[start : start + bs]
        prompts = [ds[i]["eval_prompt"] for i in batch_i]
        golds = [ds[i]["gold_assistant"] for i in batch_i]
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
        for row, gold_txt in zip(out, golds):
            gen_ids = row[in_len:]
            pred_txt = tokenizer.decode(gen_ids, skip_special_tokens=True)
            gold_list = _parse_premises_fol_list(gold_txt)
            pred_list = _parse_premises_fol_list(pred_txt)
            if gold_list is not None and pred_list is not None and _lists_exact_match(
                gold_list, pred_list
            ):
                ok += 1
    rate = float(ok) / float(total) if total else 0.0
    return {"exact_match_count": ok, "total": total, "exact_match_rate": rate}


@torch.no_grad()
def collect_fol_inference_samples(
    cfg: FolSFTConfig,
    model,
    tokenizer,
    ds,
    n: int,
    *,
    max_samples_cap: int | None = None,
) -> list[dict[str, Any]]:
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
        gold = ds[i]["gold_assistant"]
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
        pred_txt = tokenizer.decode(gen_ids, skip_special_tokens=True)
        row: dict[str, Any] = {
            "split_index": i,
            "gold_assistant": gold[:4000],
            "predicted_raw": pred_txt[:4000],
        }
        for key in ("record_id", "q_idx"):
            if key in ds.column_names:
                row[key] = ds[i][key]
        out.append(row)
    return out
