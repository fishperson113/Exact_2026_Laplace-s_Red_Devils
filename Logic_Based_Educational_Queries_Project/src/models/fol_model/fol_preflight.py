"""Baseline FOL: base model (chưa LoRA), NLL trên completion, exact-match, inference ngẫu nhiên."""
from __future__ import annotations

import json
import random
from pathlib import Path
from typing import Any

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

from services.config_fol import FolSFTConfig

from .generation_fol_eval import (
    collect_fol_inference_at_indices,
    fol_exact_match_rate,
)


def _gpu_train_profile(cfg: FolSFTConfig) -> str:
    profile = cfg.gpu_profile
    if profile == "auto" and torch.cuda.is_available():
        profile = "kaggle_p100" if torch.cuda.get_device_capability(0)[0] < 7 else "default"
    return profile


def load_base_causal_lm_for_fol_eval(cfg: FolSFTConfig):
    """Base weights (không LoRA) để đo baseline trước SFT."""
    profile = _gpu_train_profile(cfg)
    if profile == "kaggle_p100":
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_use_double_quant=True,
        )
        model = AutoModelForCausalLM.from_pretrained(
            cfg.model_name,
            quantization_config=bnb_config,
            device_map={"": 0},
            trust_remote_code=cfg.trust_remote_code,
        )
    else:
        dtype = torch.bfloat16 if cfg.bf16 else torch.float16
        model = AutoModelForCausalLM.from_pretrained(
            cfg.model_name,
            torch_dtype=dtype,
            device_map={"": 0},
            trust_remote_code=cfg.trust_remote_code,
        )
    model.config.use_cache = True
    model.eval()
    return model


@torch.no_grad()
def mean_nll_completion_on_split(
    cfg: FolSFTConfig,
    model,
    tokenizer,
    ds,
    *,
    max_samples: int | None = None,
) -> dict[str, Any]:
    """Trung bình CE (mean trên token completion) theo từng mẫu rồi macro-average."""
    model.eval()
    device = next(model.parameters()).device
    n = len(ds)
    idxs = list(range(n))
    if max_samples is not None:
        idxs = idxs[: min(max_samples, n)]
    losses: list[float] = []
    for i in idxs:
        prompt = ds[i]["eval_prompt"]
        completion = ds[i]["gold_assistant"]
        full = tokenizer(
            prompt + completion,
            return_tensors="pt",
            truncation=True,
            max_length=cfg.max_seq_length,
        )
        prompt_tok = tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=cfg.max_seq_length,
        )
        input_ids = full["input_ids"].to(device)
        plen = int(prompt_tok["input_ids"].shape[1])
        if input_ids.shape[1] <= plen:
            continue
        labels = input_ids.clone()
        labels[:, :plen] = -100
        out = model(input_ids=input_ids, labels=labels)
        losses.append(float(out.loss.item()))
    mean_loss = sum(losses) / len(losses) if losses else 0.0
    return {
        "mean_nll_completion": mean_loss,
        "n_examples": len(losses),
        "split_size": n,
    }


def print_fol_prompt_previews(dataset_dict, tokenizer, n: int = 3) -> None:
    """In vài `eval_prompt` (đầy đủ template) từ tập train."""
    if n <= 0:
        return
    ds = dataset_dict["train"]
    k = min(n, len(ds))
    print(f"\n=== Xem trước {k} eval_prompt (train) ===\n")
    for i in range(k):
        print("--- mẫu", i, "---")
        print(ds[i]["eval_prompt"][:6000])
        print()


def run_random_base_inference(
    cfg: FolSFTConfig,
    model,
    tokenizer,
    ds,
    *,
    n: int,
    seed: int,
) -> list[dict[str, Any]]:
    rng = random.Random(seed)
    pool = list(range(len(ds)))
    k = min(n, len(pool))
    idxs = rng.sample(pool, k=k) if k < len(pool) else pool
    return collect_fol_inference_at_indices(cfg, model, tokenizer, ds, idxs)


def run_preflight_baseline_and_save(
    cfg: FolSFTConfig,
    tokenizer,
    dataset_dict,
    *,
    random_infer_n: int = 10,
    random_seed: int = 3407,
    preview_rows: int = 3,
) -> dict[str, Any]:
    """
    Base model: in preview prompt, inference ngẫu nhiên, full-test exact-match + mean NLL.
    Ghi `fol_preflight_baseline.json` vào cfg.out_dir.
    """
    assert cfg.out_dir is not None
    print_fol_prompt_previews(dataset_dict, tokenizer, n=preview_rows)
    model = load_base_causal_lm_for_fol_eval(cfg)
    try:
        rnd_rows = run_random_base_inference(
            cfg,
            model,
            tokenizer,
            dataset_dict["train"],
            n=random_infer_n,
            seed=random_seed,
        )
        print(f"\n=== Base model — {len(rnd_rows)} mẫu ngẫu nhiên (train), greedy ===\n")
        for j, row in enumerate(rnd_rows):
            print(f"--- [{j}] idx={row['split_index']} ---")
            print("gold:", row["gold_assistant"][:800])
            print("pred:", row["predicted_raw"][:800])
            print()

        test_ds = dataset_dict["test"]
        acc = fol_exact_match_rate(cfg, model, tokenizer, test_ds, max_samples=None)
        nll = mean_nll_completion_on_split(cfg, model, tokenizer, test_ds, max_samples=None)
        print("=== Base model — FULL test (trước fine-tune) ===")
        print("exact_match:", acc)
        print("nll:", nll)

        doc: dict[str, Any] = {
            "model_name": cfg.model_name,
            "phase": "preflight_base_model",
            "random_train_infer_n": random_infer_n,
            "random_train_infer_seed": random_seed,
            "random_train_samples": rnd_rows,
            "test_exact_match_full": acc,
            "test_mean_nll_completion_full": nll,
        }
        path = cfg.out_dir / "fol_preflight_baseline.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
        print("Đã lưu:", path.resolve())
        return doc
    finally:
        del model
        if torch.cuda.is_available():
            torch.cuda.empty_cache()


def load_preflight_baseline(out_dir: Path | None) -> dict[str, Any] | None:
    if out_dir is None:
        return None
    p = out_dir / "fol_preflight_baseline.json"
    if not p.is_file():
        return None
    return json.loads(p.read_text(encoding="utf-8"))
