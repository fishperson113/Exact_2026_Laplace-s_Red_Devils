"""Tải merged FOL từ Hugging Face Hub và đánh giá exact-match trên train/dev/test."""
from __future__ import annotations

import os
import random
from pprint import pprint
from typing import Any

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from data.fol_dataset import build_fol_dataset_dict
from services.config_fol import FolSFTConfig

from .generation_fol_eval import (
    collect_fol_inference_at_indices,
    collect_fol_inference_samples,
    fol_exact_match_on_splits,
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
    """Tải merged weights từ Hub, build dataset, exact-match + vài mẫu generate."""
    model, tokenizer = load_fol_merged_from_hub(repo_id, cfg, hf_token=hf_token)
    dataset_dict, filter_stats = build_fol_dataset_dict(cfg, tokenizer)
    lim = cfg.eval_fol_max_samples
    metrics = fol_exact_match_on_splits(
        cfg,
        model,
        tokenizer,
        dataset_dict,
        splits=splits,
        max_samples=lim,
    )
    if inference_split not in dataset_dict:
        inference_split = "test"
    samples = collect_fol_inference_samples(
        cfg,
        model,
        tokenizer,
        dataset_dict[inference_split],
        cfg.experiment_inference_sample_n,
        max_samples_cap=lim,
    )
    random_test_samples: list[dict[str, Any]] = []
    if random_test_infer_n > 0 and "test" in dataset_dict:
        tds = dataset_dict["test"]
        rng = random.Random(random_test_seed)
        pool = list(range(len(tds)))
        k = min(random_test_infer_n, len(pool))
        idxs = rng.sample(pool, k=k) if k < len(pool) else pool
        random_test_samples = collect_fol_inference_at_indices(
            cfg, model, tokenizer, tds, idxs
        )
    return {
        "repo_id": repo_id,
        "metrics_by_split": metrics,
        "filter_stats": filter_stats,
        "samples": samples,
        "inference_split": inference_split,
        "random_test_samples": random_test_samples,
    }


def print_fol_hub_eval_summary(result: dict[str, Any], *, max_sample_print: int = 8) -> None:
    print("\n=== FOL — sau khi tải lại từ Hub (exact-match JSON premises_fol) ===")
    for sp in sorted(result["metrics_by_split"].keys()):
        m = result["metrics_by_split"][sp]
        r = m.get("exact_match_rate", 0.0)
        ok = m.get("exact_match_count", 0)
        tot = m.get("total", 0)
        print(f"  {sp}: accuracy = {r:.6f}  ({ok}/{tot})")
    fs = result.get("filter_stats")
    if fs:
        print("  filter_stats:", fs)
    rows = result.get("samples") or []
    n = min(max_sample_print, len(rows))
    print(f"\n=== Mẫu inference ({result.get('inference_split', 'test')}, tối đa {n} mẫu đầu) ===")
    pprint(rows[:n])
    rts = result.get("random_test_samples") or []
    if rts:
        print(f"\n=== Mẫu ngẫu nhiên trên test (sau fine-tune), {len(rts)} dòng ===")
        pprint(rts)
