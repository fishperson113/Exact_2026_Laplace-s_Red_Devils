"""Stage 1 Pretrain: train FOL model tren MALLS dataset (28K samples, 3 epochs).

Output: LoRA adapter luu tai configs/fol_pretrain.yaml > paths.checkpoint_dir
Sau do Stage 2 (train.py) load adapter nay lam diem khoi dau de fine-tune tren target.

Cach chay:
  cd src && python -m models.fol_model.pretrain
  hoac trong notebook:
    from models.fol_model.pretrain import run_pretrain
    run_pretrain()

Duoc import boi: notebook
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
        "trust_remote_code": m.get("trust_remote_code", True),
        "max_seq_length": m.get("max_seq_length", 2048),
        "gen_max_new_tokens": m.get("gen_max_new_tokens", 512),
        "lora_r": lo.get("r", 8),
        "lora_alpha": lo.get("alpha", 16),
        "lora_dropout": lo.get("dropout", 0.05),
        "num_train_epochs": t.get("num_train_epochs", 3),
        "per_device_train_batch_size": t.get("per_device_train_batch_size", 1),
        "per_device_eval_batch_size": t.get("per_device_eval_batch_size", 1),
        "gradient_accumulation_steps": t.get("gradient_accumulation_steps", 8),
        "learning_rate": t.get("learning_rate", 2e-4),
        "warmup_ratio": t.get("warmup_ratio", 0.05),
        "weight_decay": t.get("weight_decay", 0.01),
        "logging_steps": t.get("logging_steps", 50),
        "bf16": t.get("bf16", True),
        "gradient_checkpointing": t.get("gradient_checkpointing", True),
        "train_seed": t.get("train_seed", 3407),
        "load_in_8bit": t.get("load_in_8bit", True),
        "use_unsloth": t.get("use_unsloth", True),
        "unsloth_train_on_responses_only": t.get("unsloth_train_on_responses_only", True),
        "use_adamw_8bit": t.get("use_adamw_8bit", True),
        "early_stopping_patience": t.get("early_stopping_patience", 0),
        "load_best_model_at_end": t.get("load_best_model_at_end", False),
        "save_total_limit": t.get("save_total_limit", 1),
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

    return cfg, out_dir, checkpoint_dir, malls_json


def run_pretrain():
    """Chay Stage 1 pretrain tren MALLS."""
    cfg, out_dir, checkpoint_dir, malls_json = build_pretrain_config()

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

    # Cleanup
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

    print("[Pretrain] Stage 1 complete.", flush=True)
    print(f"[Pretrain] Next: Stage 2 fine-tune voi fol_model.yaml, set checkpoint = {checkpoint_dir}", flush=True)

    return train_result, checkpoint_dir


if __name__ == "__main__":
    run_pretrain()
