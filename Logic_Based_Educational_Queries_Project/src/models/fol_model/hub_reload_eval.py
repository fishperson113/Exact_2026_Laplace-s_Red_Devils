"""Tải merged FOL từ Hugging Face Hub — mặc định chỉ greedy + exact-match trên N mẫu test ngẫu nhiên."""
from __future__ import annotations

import gc
import os
import random
from pprint import pprint
from typing import Any

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

from data.fol_dataset import build_fol_dataset_dict
from services.config_fol import FolSFTConfig, fol_should_load_in_8bit

from .generation_fol_eval import (
    collect_fol_inference_at_indices,
    collect_fol_inference_samples,
)


def _resolve_hf_token(hf_token: str | None) -> str | None:
    t = (hf_token or "").strip()
    if t:
        return t
    for k in ("HF_TOKEN", "HUGGINGFACE_HUB_TOKEN"):
        v = os.environ.get(k, "").strip()
        if v:
            return v
    return None


def _infer_dtype() -> torch.dtype:
    if not torch.cuda.is_available():
        return torch.float32
    major, _minor = torch.cuda.get_device_capability(0)
    return torch.bfloat16 if major >= 8 else torch.float16


def load_fol_merged_from_hub(
    repo_id: str,
    cfg: FolSFTConfig,
    *,
    hf_token: str | None = None,
) -> tuple[Any, Any]:
    token = _resolve_hf_token(hf_token)
    kwargs: dict[str, Any] = {"trust_remote_code": cfg.trust_remote_code}
    if token:
        kwargs["token"] = token
    if fol_should_load_in_8bit(cfg):
        bnb_config = BitsAndBytesConfig(load_in_8bit=True)
        model = AutoModelForCausalLM.from_pretrained(
            repo_id,
            quantization_config=bnb_config,
            device_map="auto",
            **kwargs,
        )
    else:
        dtype = _infer_dtype()
        model = AutoModelForCausalLM.from_pretrained(
            repo_id,
            torch_dtype=dtype,
            device_map="auto",
            **kwargs,
        )
    tokenizer = AutoTokenizer.from_pretrained(repo_id, **kwargs)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "left"
    return model, tokenizer


def evaluate_fol_hub_model(
    cfg: FolSFTConfig,
    repo_id: str,
    *,
    hf_token: str | None = None,
    splits: tuple[str, ...] = ("train", "dev", "test"),
    inference_split: str = "test",
    random_test_infer_n: int = 0,
    random_test_seed: int = 42,
) -> dict[str, Any]:
    """Tải merged từ Hub rồi đánh giá.

    - ``random_test_infer_n > 0`` (mặc định sau train): **chỉ** greedy trên **N mẫu test ngẫu nhiên**,
      ``metrics_by_split["test"]`` là exact-match **trên đúng N mẫu đó** (không quét train/dev).
    - ``random_test_infer_n == 0``: quét greedy exact-match trên ``splits`` như cũ (``cfg.eval_fol_max_samples``).
    """
    model, tokenizer = load_fol_merged_from_hub(repo_id, cfg, hf_token=hf_token)
    dataset_dict, filter_stats = build_fol_dataset_dict(cfg, tokenizer)
    if inference_split not in dataset_dict:
        inference_split = "test"

    random_test_samples: list[dict[str, Any]] = []
    metrics: dict[str, Any]
    samples: list[dict[str, Any]]
    eval_mode: str

    if random_test_infer_n > 0 and "test" in dataset_dict:
        eval_mode = "random_test_only"
        tds = dataset_dict["test"]
        rng = random.Random(random_test_seed)
        pool = list(range(len(tds)))
        k = min(random_test_infer_n, len(pool))
        idxs = rng.sample(pool, k=k) if k < len(pool) else pool
        random_test_samples = collect_fol_inference_at_indices(
            cfg, model, tokenizer, tds, idxs
        )
        metrics = {"test": {"total": len(random_test_samples)}}
        samples = []
        print(
            f"[FOL hub reload] Greedy tren {len(random_test_samples)} mau **test** ngau nhien "
            f"(seed={random_test_seed}).",
            flush=True,
        )
    elif random_test_infer_n > 0:
        eval_mode = "random_test_only"
        metrics = {}
        samples = []
    else:
        eval_mode = "all_splits"
        lim = cfg.eval_fol_max_samples
        metrics = {}
        samples = collect_fol_inference_samples(
            cfg,
            model,
            tokenizer,
            dataset_dict[inference_split],
            cfg.experiment_inference_sample_n,
            max_samples_cap=lim,
        )

    out: dict[str, Any] = {
        "repo_id": repo_id,
        "eval_mode": eval_mode,
        "metrics_by_split": metrics,
        "filter_stats": filter_stats,
        "samples": samples,
        "inference_split": inference_split,
        "random_test_samples": random_test_samples,
    }
    try:
        del model
        del tokenizer
    except Exception:
        pass
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    return out


def print_fol_hub_eval_summary(
    result: dict[str, Any],
    *,
    max_ordered_sample_print: int | None = 8,
    random_sample_print_limit: int | None = None,
) -> None:
    """In log terminal: nếu ``random_sample_print_limit`` là None → in hết mẫu ngẫu nhiên."""
    print("\n=== FOL — Hub reload ===")
    for sp in sorted(result["metrics_by_split"].keys()):
        m = result["metrics_by_split"][sp]
        tot = m.get("total", 0)
        print(f"  {sp}: {tot} samples")
    fs = result.get("filter_stats")
    if fs:
        print("  filter_stats:", fs)
    rows = result.get("samples") or []
    if rows:
        n_ord = (
            len(rows)
            if max_ordered_sample_print is None
            else min(max_ordered_sample_print, len(rows))
        )
        print(
            f"\n=== Mẫu inference ({result.get('inference_split', 'test')}, {n_ord}/{len(rows)} mẫu) ==="
        )
        pprint(rows[:n_ord])
    rts = result.get("random_test_samples") or []
    if rts:
        lim = len(rts) if random_sample_print_limit is None else min(random_sample_print_limit, len(rts))
        if random_sample_print_limit is None or lim >= len(rts):
            print(f"\n=== Mẫu ngẫu nhiên trên test (Hub) — đủ {len(rts)} dòng (terminal + JSON) ===")
        else:
            print(
                f"\n=== Mẫu ngẫu nhiên trên test (Hub) — xem trước {lim}/{len(rts)} dòng trên terminal (JSON đủ toàn bộ) ==="
            )
        pprint(rts[:lim])
