"""Stage 1 Pretrain: train FOL model tren MALLS dataset (28K samples, 3 epochs).

Output:
  1. LoRA adapter luu tai configs/fol_pretrain.yaml > paths.checkpoint_dir
  2. Merge LoRA + push len Hub (hub.repo_id trong fol_pretrain.yaml)
     → Stage 2 (train.py) set model.name = repo_id nay de fine-tune tiep

Cach chay:
  cd src && python -m models.fol_model.pretrain
  hoac: bash scripts/run_fol_pretrain.sh

Duoc import boi: notebook, scripts/run_fol_pretrain.sh
Import tu:       data.fol_dataset, services.config_fol, train.py (shared utils)
"""
from __future__ import annotations

# Tat flex_attention truoc moi import transformers
for _mod_name in ("transformers.modeling_utils", "transformers.utils", "transformers"):
    try:
        import importlib as _importlib
        _mod = _importlib.import_module(_mod_name)
        if hasattr(_mod, "is_torch_flex_attn_available"):
            setattr(_mod, "is_torch_flex_attn_available", lambda: False)
    except Exception:
        pass

import gc
import inspect
import os
from pathlib import Path

import torch
import yaml

try:
    from unsloth import FastLanguageModel as _UnslothFastLanguageModel  # noqa: F401
except ImportError:
    try:
        import unsloth  # noqa: F401
    except ImportError:
        pass

from trl import SFTConfig, SFTTrainer

from data.fol_dataset import build_malls_pretrain_dataset
from data.ingestion import project_root
from services.config_fol import FolSFTConfig

from .tokenizer_fix import scrub_sft_config_eos_pad_args, sync_eos_token_string_with_id
from .train import (
    _build_fol_sft_config,
    _fol_cuda_bootstrap,
    build_model,
    load_tokenizer,
)


def _load_pretrain_yaml() -> dict:
    """Doc configs/fol_pretrain.yaml."""
    root = project_root()
    yaml_path = root / "configs" / "fol_pretrain.yaml"
    if not yaml_path.is_file():
        raise FileNotFoundError(f"Khong tim thay {yaml_path}")
    with open(yaml_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def build_pretrain_config() -> tuple[FolSFTConfig, Path, Path, str]:
    """Tao FolSFTConfig tu fol_pretrain.yaml.

    Returns: (cfg, out_dir, checkpoint_dir, malls_json_path)
    """
    raw = _load_pretrain_yaml()
    root = project_root()

    # Map YAML -> FolSFTConfig kwargs
    m = raw.get("model", {})
    lo = raw.get("lora", {})
    t = raw.get("training", {})
    d = raw.get("data", {})
    p = raw.get("paths", {})

    kwargs = {
        "model_name": m.get("name", "Qwen/Qwen2.5-3B-Instruct"),
        "trust_remote_code": bool(m.get("trust_remote_code", True)),
        "max_seq_length": int(m.get("max_seq_length", 2048)),
        "gen_max_new_tokens": int(m.get("gen_max_new_tokens", 512)),
        "lora_r": int(lo.get("r", 8)),
        "lora_alpha": int(lo.get("alpha", 16)),
        "lora_dropout": float(lo.get("dropout", 0.05)),
        "num_train_epochs": int(t.get("num_train_epochs", 3)),
        "per_device_train_batch_size": int(t.get("per_device_train_batch_size", 1)),
        "per_device_eval_batch_size": int(t.get("per_device_eval_batch_size", 1)),
        "gradient_accumulation_steps": int(t.get("gradient_accumulation_steps", 8)),
        "learning_rate": float(t.get("learning_rate", 2e-4)),
        "warmup_ratio": float(t.get("warmup_ratio", 0.05)),
        "weight_decay": float(t.get("weight_decay", 0.01)),
        "logging_steps": int(t.get("logging_steps", 50)),
        "bf16": bool(t.get("bf16", True)),
        "gradient_checkpointing": bool(t.get("gradient_checkpointing", True)),
        "train_seed": int(t.get("train_seed", 3407)),
        "load_in_8bit": bool(t.get("load_in_8bit", True)),
        "use_unsloth": bool(t.get("use_unsloth", True)),
        "unsloth_train_on_responses_only": bool(t.get("unsloth_train_on_responses_only", True)),
        "use_adamw_8bit": bool(t.get("use_adamw_8bit", True)),
        "early_stopping_patience": int(t.get("early_stopping_patience", 0)),
        "load_best_model_at_end": bool(t.get("load_best_model_at_end", False)),
        "save_total_limit": int(t.get("save_total_limit", 1)),
        "push_to_hub": False,
        "run_train": True,
    }

    cfg = FolSFTConfig(**kwargs)

    out_dir = root / p.get("output_dir", "notebooks/output/pipeline_fol_pretrain")
    checkpoint_dir = root / p.get("checkpoint_dir", "notebooks/output/pipeline_fol_pretrain/pretrain_lora")
    malls_json = str(root / d.get("malls_json", "data/processed/malls_v01_normalized.json"))

    cfg.out_dir = out_dir
    cfg.checkpoint_dir = checkpoint_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    # max_train_samples: gioi han so mau train (None = dung het)
    max_train_samples = d.get("max_train_samples", None)
    if max_train_samples is not None:
        max_train_samples = int(max_train_samples)

    return cfg, out_dir, checkpoint_dir, malls_json, max_train_samples


def _merge_and_push_pretrain(
    base_model_name: str,
    checkpoint_dir: Path,
    out_dir: Path,
    repo_id: str,
    hf_token: str,
    private: bool = False,
    trust_remote_code: bool = True,
) -> str:
    """Merge LoRA adapter voi base model, push len HF Hub.

    Chay tren CPU (device_map="cpu") de giai phong GPU cho Stage 2.
    Returns: URL repo tren Hub.
    """
    from huggingface_hub import HfApi
    from peft import PeftModel
    from transformers import AutoModelForCausalLM, AutoTokenizer

    # Load base + LoRA, merge
    base = AutoModelForCausalLM.from_pretrained(
        base_model_name,
        torch_dtype="auto",
        trust_remote_code=trust_remote_code,
        device_map="cpu",
    )
    model = PeftModel.from_pretrained(base, str(checkpoint_dir))
    merged = model.merge_and_unload()

    # Save merged local
    merged_dir = out_dir / "merged_for_hub"
    merged_dir.mkdir(parents=True, exist_ok=True)
    merged.save_pretrained(merged_dir)

    tok = AutoTokenizer.from_pretrained(
        str(checkpoint_dir), trust_remote_code=trust_remote_code
    )
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    tok.padding_side = "left"
    tok.save_pretrained(merged_dir)

    # Push to Hub
    merged.push_to_hub(repo_id, token=hf_token, private=private)
    tok.push_to_hub(repo_id, token=hf_token, private=private)

    # Upload README
    api = HfApi(token=hf_token)
    readme_path = merged_dir / "README.md"
    readme_path.write_text(
        f"""---
license: apache-2.0
base_model: {base_model_name}
tags:
  - exact-2026
  - fol
  - pretrain
  - malls
---

# {repo_id.split("/")[-1]}

Stage 1 Pretrain: LoRA SFT tren MALLS dataset (28K mau, 3 epochs).

Base model: `{base_model_name}`

Day la model trung gian — dung lam base cho Stage 2 fine-tune tren target dataset.
""",
        encoding="utf-8",
    )
    api.upload_file(
        path_or_fileobj=str(readme_path),
        path_in_repo="README.md",
        repo_id=repo_id,
        repo_type="model",
    )

    # Cleanup merged khoi RAM
    del base, model, merged
    gc.collect()

    return f"https://huggingface.co/{repo_id}"


def run_pretrain():
    """Chay Stage 1 pretrain tren MALLS."""
    cfg, out_dir, checkpoint_dir, malls_json, max_train_samples = build_pretrain_config()

    _fol_cuda_bootstrap()
    print("[Pretrain] Stage 1: MALLS pretrain", flush=True)
    print(f"[Pretrain] Model: {cfg.model_name}", flush=True)
    print(f"[Pretrain] LoRA r={cfg.lora_r}, alpha={cfg.lora_alpha}", flush=True)
    print(f"[Pretrain] Epochs: {cfg.num_train_epochs}, LR: {cfg.learning_rate}", flush=True)
    print(f"[Pretrain] MALLS data: {malls_json}", flush=True)

    # Load tokenizer + dataset
    if cfg.use_unsloth:
        from .unsloth_sft import (
            apply_train_on_responses_only,
            load_unsloth_model_and_tokenizer,
        )
        model, tokenizer, train_bf16, train_fp16 = load_unsloth_model_and_tokenizer(cfg)
    else:
        tokenizer = load_tokenizer(cfg)
        model, train_bf16, train_fp16 = build_model(cfg)

    dataset_dict = build_malls_pretrain_dataset(malls_json, tokenizer)

    # Gioi han so mau train neu config chi dinh (random shuffle)
    if max_train_samples and len(dataset_dict["train"]) > max_train_samples:
        dataset_dict["train"] = dataset_dict["train"].shuffle(seed=cfg.train_seed).select(range(max_train_samples))
        print(f"[Pretrain] Limited train to {max_train_samples} samples (random)", flush=True)

    print(
        f"[Pretrain] Dataset: train={len(dataset_dict['train'])}, dev={len(dataset_dict['dev'])}",
        flush=True,
    )

    # SFT config
    sft_config = _build_fol_sft_config(cfg, train_bf16, train_fp16, tokenizer)
    scrub_sft_config_eos_pad_args(sft_config, tokenizer)
    sft_config.eos_token = None
    sft_config.pad_token = None
    # Pretrain: eval moi epoch de theo doi loss, khong early stopping
    sft_config.eval_strategy = "epoch"
    sft_config.save_strategy = "epoch"

    trainer_kwargs = dict(
        model=model,
        args=sft_config,
        train_dataset=dataset_dict["train"],
        eval_dataset=dataset_dict["dev"],
    )
    if "processing_class" in inspect.signature(SFTTrainer.__init__).parameters:
        trainer_kwargs["processing_class"] = tokenizer
    else:
        trainer_kwargs["tokenizer"] = tokenizer

    trainer = SFTTrainer(**trainer_kwargs)

    if cfg.use_unsloth and cfg.unsloth_train_on_responses_only:
        print("[Pretrain] Applying train_on_responses_only ...", flush=True)
        trainer = apply_train_on_responses_only(trainer, cfg)

    # Train
    print("[Pretrain] Starting trainer.train() ...", flush=True)
    train_result = trainer.train()
    print("[Pretrain] Training done.", flush=True)

    # Save LoRA adapter
    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    trainer.save_model(str(checkpoint_dir))
    tokenizer.save_pretrained(str(checkpoint_dir))
    print(f"[Pretrain] LoRA adapter saved: {checkpoint_dir}", flush=True)

    # Cleanup GPU truoc khi merge (merge chay CPU, can RAM)
    del trainer, model
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

    # Merge LoRA + push len Hub
    raw = _load_pretrain_yaml()
    hub_cfg = raw.get("hub", {})
    hub_repo_id = hub_cfg.get("repo_id", "")
    hub_push = hub_cfg.get("push_to_hub", False)
    hub_private = hub_cfg.get("private", False)

    if hub_push and hub_repo_id:
        hf_token = (
            os.environ.get("HF_TOKEN")
            or os.environ.get("HUGGINGFACE_HUB_TOKEN")
            or ""
        ).strip()
        if not hf_token:
            print("[Pretrain][Hub] push_to_hub=True nhung thieu HF_TOKEN — bo qua merge+push.", flush=True)
        else:
            print(f"[Pretrain][Hub] Merge LoRA + push len {hub_repo_id} ...", flush=True)
            hub_url = _merge_and_push_pretrain(
                base_model_name=cfg.model_name,
                checkpoint_dir=checkpoint_dir,
                out_dir=out_dir,
                repo_id=hub_repo_id,
                hf_token=hf_token,
                private=hub_private,
                trust_remote_code=cfg.trust_remote_code,
            )
            print(f"[Pretrain][Hub] Done: {hub_url}", flush=True)
            print(f"[Pretrain] Next: sua fol_model.yaml > model.name = {hub_repo_id}", flush=True)
            print(f"[Pretrain] Roi chay Stage 2: bash scripts/run_fol_train.sh", flush=True)
    else:
        print("[Pretrain] Hub push disabled. LoRA adapter tai:", checkpoint_dir, flush=True)

    print("[Pretrain] Stage 1 complete.", flush=True)
    return train_result, checkpoint_dir


if __name__ == "__main__":
    run_pretrain()
