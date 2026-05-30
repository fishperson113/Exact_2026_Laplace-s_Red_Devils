"""Đánh giá greedy: so khớp JSON premises_fol với nhãn assistant + RM (LE + FOL BLEU)."""
from __future__ import annotations

import json
import logging
import random
import re
import statistics
import time
from typing import Any, Mapping

_LOG = logging.getLogger(__name__)

# Tắt flex_attention — tránh ValueError trong model.generate()
for _mod_name in ("transformers.modeling_utils", "transformers.utils", "transformers"):
    try:
        import importlib as _importlib
        _mod = _importlib.import_module(_mod_name)
        if hasattr(_mod, "is_torch_flex_attn_available"):
            setattr(_mod, "is_torch_flex_attn_available", lambda: False)
    except Exception:
        pass

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
    *,
    split_label: str | None = None,
) -> dict[str, Any]:
    model.eval()
    device = next(model.parameters()).device
    # model.generate() cần left-padding; SFTTrainer có thể đã đổi sang right.
    orig_padding_side = tokenizer.padding_side
    tokenizer.padding_side = "left"
    n = len(ds)
    idxs = list(range(n))
    if max_samples is not None:
        idxs = idxs[: min(max_samples, n)]
    ok = 0
    total = len(idxs)
    bs = max(1, cfg.eval_gen_batch_size)
    tag = split_label or "eval"
    print(f"[FOL greedy eval] {tag}: {total} mẫu, batch_size={bs}", flush=True)
    log_every_batches = 10 if total >= 40 else 0
    batch_num = 0
    for start in range(0, len(idxs), bs):
        batch_num += 1
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
            repetition_penalty=1.2,
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
        if log_every_batches and batch_num % log_every_batches == 0:
            done = min(start + bs, total)
            print(f"[FOL greedy eval] {tag}: tiến độ {done}/{total}", flush=True)
    rate = float(ok) / float(total) if total else 0.0
    print(f"[FOL greedy eval] {tag}: xong — đúng {ok}/{total}", flush=True)
    tokenizer.padding_side = orig_padding_side
    return {"exact_match_count": ok, "total": total, "exact_match_rate": rate}


def fol_exact_match_on_splits(
    cfg: FolSFTConfig,
    model,
    tokenizer,
    dataset_dict: Mapping[str, Any],
    *,
    splits: tuple[str, ...] = ("train", "dev", "test"),
    max_samples: int | None = None,
) -> dict[str, Any]:
    """Exact-match JSON `premises_fol` trên nhiều split (mặc định train/dev/test)."""
    out: dict[str, Any] = {}
    for sp in splits:
        if sp not in dataset_dict:
            continue
        out[sp] = fol_exact_match_rate(
            cfg,
            model,
            tokenizer,
            dataset_dict[sp],
            max_samples=max_samples,
            split_label=sp,
        )
    return out


def fol_summarize_exact_match_rows(
    rows: list[dict[str, Any]],
    *,
    attach_per_row: bool = True,
) -> dict[str, Any]:
    """Đếm exact-match ``premises_fol`` trên các hàng có ``gold_assistant`` / ``predicted_raw``."""
    ok = 0
    total = 0
    for row in rows:
        g = str(row.get("gold_assistant", ""))
        p = str(row.get("predicted_raw", ""))
        gl = _parse_premises_fol_list(g)
        pl = _parse_premises_fol_list(p)
        match = gl is not None and pl is not None and _lists_exact_match(gl, pl)
        if attach_per_row:
            row["premises_fol_exact_match"] = match
        total += 1
        if match:
            ok += 1
    rate = float(ok) / float(total) if total else 0.0
    return {"exact_match_count": ok, "total": total, "exact_match_rate": rate}


@torch.no_grad()
def fol_rm_score(
    cfg: FolSFTConfig,
    model,
    tokenizer,
    ds,
    max_samples: int | None = None,
    *,
    split_label: str | None = None,
) -> dict[str, Any]:
    """Tính RM = le_weight * LE + bleu_weight * FOL BLEU trên split.

    Greedy generate → parse gold/pred → tính LE (Z3 nếu có) + FOL BLEU → RM.
    """
    from evaluation.fol_bleu import fol_bleu_record
    from evaluation.fol_le import _z3_available, le_record, le_record_no_z3

    le_weight = getattr(cfg, "rm_le_weight", 0.7)
    bleu_weight = getattr(cfg, "rm_bleu_weight", 0.3)
    use_z3 = _z3_available()
    if not use_z3:
        _LOG.warning(
            "z3-solver chưa cài — LE fallback sang string match. pip install z3-solver"
        )

    model.eval()
    device = next(model.parameters()).device
    orig_padding_side = tokenizer.padding_side
    tokenizer.padding_side = "left"

    n = len(ds)
    idxs = list(range(n))
    if max_samples is not None:
        idxs = idxs[: min(max_samples, n)]
    total = len(idxs)
    bs = max(1, cfg.eval_gen_batch_size)
    tag = split_label or "eval"
    print(f"[FOL RM eval] {tag}: {total} mẫu, batch_size={bs}", flush=True)

    rm_scores: list[float] = []
    le_scores: list[float] = []
    bleu_scores: list[float] = []

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
            repetition_penalty=1.2,
        )
        in_len = enc["input_ids"].shape[1]
        for row, gold_txt in zip(out, golds):
            gen_ids = row[in_len:]
            pred_txt = tokenizer.decode(gen_ids, skip_special_tokens=True)
            gold_list = _parse_premises_fol_list(gold_txt)
            pred_list = _parse_premises_fol_list(pred_txt)

            if gold_list is None:
                gold_list = []
            if pred_list is None:
                pred_list = []

            # FOL BLEU
            bleu = fol_bleu_record(gold_list, pred_list)
            bleu_scores.append(bleu)

            # LE
            if use_z3:
                le = le_record(gold_list, pred_list)
            else:
                le = le_record_no_z3(gold_list, pred_list)
            le_scores.append(le)

            # RM
            rm = le_weight * le + bleu_weight * bleu
            rm_scores.append(rm)

    rm_avg = sum(rm_scores) / len(rm_scores) if rm_scores else 0.0
    le_avg = sum(le_scores) / len(le_scores) if le_scores else 0.0
    bleu_avg = sum(bleu_scores) / len(bleu_scores) if bleu_scores else 0.0

    print(
        f"[FOL RM eval] {tag}: RM={rm_avg:.4f} (LE={le_avg:.4f}, BLEU={bleu_avg:.4f})",
        flush=True,
    )
    tokenizer.padding_side = orig_padding_side
    return {
        "rm_score": rm_avg,
        "le_score": le_avg,
        "fol_bleu": bleu_avg,
        "total": total,
        "le_weight": le_weight,
        "bleu_weight": bleu_weight,
        "z3_available": use_z3,
    }


def fol_rm_on_splits(
    cfg: FolSFTConfig,
    model,
    tokenizer,
    dataset_dict: Mapping[str, Any],
    *,
    splits: tuple[str, ...] = ("train", "dev", "test"),
    max_samples: int | None = None,
) -> dict[str, Any]:
    """RM (LE + FOL BLEU) trên nhiều split."""
    out: dict[str, Any] = {}
    for sp in splits:
        if sp not in dataset_dict:
            continue
        out[sp] = fol_rm_score(
            cfg, model, tokenizer, dataset_dict[sp],
            max_samples=max_samples, split_label=sp,
        )
    return out


def _fol_one_greedy_generate(
    cfg: FolSFTConfig,
    model,
    tokenizer,
    device: torch.device,
    prompt: str,
) -> None:
    enc = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=cfg.max_seq_length,
    )
    enc = {k: v.to(device) for k, v in enc.items()}
    pad_id = tokenizer.pad_token_id or tokenizer.eos_token_id
    model.generate(
        **enc,
        max_new_tokens=cfg.gen_max_new_tokens,
        do_sample=False,
        pad_token_id=pad_id,
        eos_token_id=tokenizer.eos_token_id,
        repetition_penalty=1.2,
    )


@torch.no_grad()
def benchmark_fol_greedy_latency_per_sample(
    cfg: FolSFTConfig,
    model,
    tokenizer,
    ds,
    *,
    n: int = 30,
    seed: int = 42,
    warmup: int = 2,
    split_name: str = "test",
) -> dict[str, Any]:
    """Đo thời gian greedy **một prompt / một lần generate**; trả về trung bình trên ``n`` mẫu ngẫu nhiên."""
    model.eval()
    device = next(model.parameters()).device
    n_total = len(ds)
    if n_total == 0:
        return {"error": "empty_dataset", "split": split_name}
    k = min(max(0, n), n_total)
    rng = random.Random(seed)
    pool = list(range(n_total))
    idxs = rng.sample(pool, k=k) if k < len(pool) else pool[:k]

    w = max(0, min(int(warmup), n_total))
    w_idx = idxs[0] if idxs else 0
    for _ in range(w):
        if torch.cuda.is_available():
            torch.cuda.synchronize()
        _fol_one_greedy_generate(cfg, model, tokenizer, device, str(ds[w_idx]["eval_prompt"]))
    if torch.cuda.is_available():
        torch.cuda.synchronize()

    times: list[float] = []
    for i in idxs:
        prompt = str(ds[i]["eval_prompt"])
        if torch.cuda.is_available():
            torch.cuda.synchronize()
        t0 = time.perf_counter()
        _fol_one_greedy_generate(cfg, model, tokenizer, device, prompt)
        if torch.cuda.is_available():
            torch.cuda.synchronize()
        t1 = time.perf_counter()
        times.append(t1 - t0)

    mean_s = float(sum(times) / len(times)) if times else 0.0
    std_s = float(statistics.pstdev(times)) if len(times) > 1 else 0.0
    result: dict[str, Any] = {
        "split": split_name,
        "n_samples": len(times),
        "seed": seed,
        "warmup_runs": w,
        "mean_seconds_per_sample": mean_s,
        "std_seconds_per_sample": std_s,
        "min_seconds": float(min(times)) if times else None,
        "max_seconds": float(max(times)) if times else None,
        "gen_max_new_tokens": cfg.gen_max_new_tokens,
        "max_seq_length_cap": cfg.max_seq_length,
        "note": "Mỗi mẫu: một lần greedy generate từ eval_prompt; đồng bộ CUDA quanh đo để gần với thời gian GPU.",
    }
    print(
        f"[FOL latency] {split_name}: trung bình {mean_s:.3f}s/mẫu (n={len(times)}, σ={std_s:.3f}s)",
        flush=True,
    )
    return result


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
            repetition_penalty=1.2,
        )
        gen_ids = gen_out[0, enc["input_ids"].shape[1] :]
        pred_txt = tokenizer.decode(gen_ids, skip_special_tokens=True)
        row: dict[str, Any] = {
            "split_index": i,
            "gold_assistant": gold[:4000],
            "predicted_raw": pred_txt[:4000],
        }
        for key in ("record_id", "q_idx", "premises_nl", "premises_fol"):
            if key in ds.column_names:
                row[key] = ds[i][key]
        out.append(row)
    return out


@torch.no_grad()
def collect_fol_inference_at_indices(
    cfg: FolSFTConfig,
    model,
    tokenizer,
    ds,
    indices: list[int],
) -> list[dict[str, Any]]:
    """Greedy generate cho từng chỉ số trong `indices` (subset của split)."""
    if not indices:
        return []
    model.eval()
    device = next(model.parameters()).device
    out: list[dict[str, Any]] = []
    for i in indices:
        if i < 0 or i >= len(ds):
            continue
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
            repetition_penalty=1.2,
        )
        gen_ids = gen_out[0, enc["input_ids"].shape[1] :]
        pred_txt = tokenizer.decode(gen_ids, skip_special_tokens=True)
        row: dict[str, Any] = {
            "split_index": i,
            "gold_assistant": gold[:4000],
            "predicted_raw": pred_txt[:4000],
        }
        for key in ("record_id", "q_idx", "premises_nl", "premises_fol"):
            if key in ds.column_names:
                row[key] = ds[i][key]
        out.append(row)
    return out
