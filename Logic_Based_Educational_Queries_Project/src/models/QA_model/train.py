"""Train QA Stage 2: LoRA SFT on COT reasoning (NL + FOL → answer + explanation).

Single-file training script. Loads config from YAML, prepares data, trains with SFT.

Usage:
    python -m models.QA_model.train --config configs/qa_model.yaml
    python -m models.QA_model.train --config configs/qa_model.yaml --debug-samples 10
"""
from __future__ import annotations

import argparse
import gc
import json
import os
import shutil
from pathlib import Path

import torch
import yaml
from datasets import DatasetDict, load_from_disk
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    EarlyStoppingCallback,
)
from trl import SFTConfig, SFTTrainer

from .prepare_data import build_qa_dataset_dict


# ─── Config ──────────────────────────────────────────────────────────────────

def load_config(config_path: str) -> dict:
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def resolve_project_root() -> Path:
    return Path(__file__).resolve().parents[3]


# ─── Dataset ─────────────────────────────────────────────────────────────────

def get_or_build_dataset(cfg: dict, project_root: Path) -> DatasetDict:
    """Load cached dataset or build from raw data."""
    data_dir = project_root / "data"
    cache_dir = data_dir / "processed" / "qa_sft"

    if cache_dir.exists() and (cache_dir / "dataset_dict.json").exists():
        print(f"[Data] Loading cached dataset from {cache_dir}")
        return load_from_disk(str(cache_dir))

    print("[Data] Building dataset from raw data...")
    ds_dict = build_qa_dataset_dict(data_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    ds_dict.save_to_disk(str(cache_dir))
    print(f"[Data] Cached to {cache_dir}")
    return ds_dict


# ─── Model Loading ───────────────────────────────────────────────────────────

def load_model_and_tokenizer(cfg: dict):
    """Load base model with quantization + LoRA."""
    model_cfg = cfg["model"]
    lora_cfg = cfg["lora"]
    train_cfg = cfg["training"]

    model_name = model_cfg["name"]
    print(f"[Model] Loading: {model_name}")

    # Quantization
    quant_config = None
    if train_cfg.get("load_in_8bit", False):
        quant_config = BitsAndBytesConfig(load_in_8bit=True)
    elif train_cfg.get("load_in_4bit", False):
        quant_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
        )

    tokenizer = AutoTokenizer.from_pretrained(
        model_name, trust_remote_code=model_cfg.get("trust_remote_code", True)
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    load_kwargs = {
        "trust_remote_code": model_cfg.get("trust_remote_code", True),
        "device_map": "auto",
    }
    if quant_config:
        load_kwargs["quantization_config"] = quant_config
    if train_cfg.get("bf16", True):
        load_kwargs["torch_dtype"] = torch.bfloat16

    model = AutoModelForCausalLM.from_pretrained(model_name, **load_kwargs)

    # Prepare for kbit training if quantized
    if quant_config:
        model = prepare_model_for_kbit_training(
            model, use_gradient_checkpointing=train_cfg.get("gradient_checkpointing", True)
        )

    # LoRA
    lora = LoraConfig(
        r=lora_cfg.get("r", 16),
        lora_alpha=lora_cfg.get("alpha", 32),
        lora_dropout=lora_cfg.get("dropout", 0.05),
        bias="none",
        task_type="CAUSAL_LM",
        target_modules=lora_cfg.get("target_modules", ["q_proj", "k_proj", "v_proj", "o_proj"]),
    )
    model = get_peft_model(model, lora)
    model.print_trainable_parameters()

    return model, tokenizer


# ─── Training ────────────────────────────────────────────────────────────────

def train(cfg: dict, debug_max_samples: int | None = None):
    """Full training pipeline."""
    project_root = resolve_project_root()
    train_cfg = cfg["training"]
    model_cfg = cfg["model"]

    # 1. Dataset
    ds_dict = get_or_build_dataset(cfg, project_root)

    if debug_max_samples:
        for split in ds_dict:
            n = min(debug_max_samples, len(ds_dict[split]))
            ds_dict[split] = ds_dict[split].select(range(n))
        print(f"[Debug] Limited to {debug_max_samples} samples per split")

    print(f"[Data] Train: {len(ds_dict['train'])}, Dev: {len(ds_dict['dev'])}, Test: {len(ds_dict['test'])}")

    # 2. Model
    model, tokenizer = load_model_and_tokenizer(cfg)

    # 3. Output dir
    hub_cfg = cfg.get("hub", {})
    version = hub_cfg.get("repo_version", "v01")
    output_dir = project_root / "outputs" / f"qa-sft-{version}"
    output_dir.mkdir(parents=True, exist_ok=True)

    # 4. SFT Config
    sft_config = SFTConfig(
        output_dir=str(output_dir),
        num_train_epochs=train_cfg.get("num_train_epochs", 10),
        per_device_train_batch_size=train_cfg.get("per_device_train_batch_size", 1),
        per_device_eval_batch_size=train_cfg.get("per_device_eval_batch_size", 4),
        gradient_accumulation_steps=train_cfg.get("gradient_accumulation_steps", 8),
        learning_rate=float(train_cfg.get("learning_rate", 2e-5)),
        warmup_ratio=train_cfg.get("warmup_ratio", 0.05),
        weight_decay=train_cfg.get("weight_decay", 0.01),
        logging_steps=train_cfg.get("logging_steps", 10),
        eval_strategy="epoch",
        save_strategy="epoch",
        save_total_limit=train_cfg.get("save_total_limit", 2),
        load_best_model_at_end=train_cfg.get("load_best_model_at_end", True),
        metric_for_best_model=train_cfg.get("metric_for_best_model", "eval_loss"),
        greater_is_better=train_cfg.get("greater_is_better", False),
        bf16=train_cfg.get("bf16", True),
        gradient_checkpointing=train_cfg.get("gradient_checkpointing", True),
        max_seq_length=model_cfg.get("max_seq_length", 4096),
        seed=train_cfg.get("train_seed", 42),
        report_to="none",
    )

    # 5. Callbacks
    callbacks = []
    patience = train_cfg.get("early_stopping_patience", 5)
    if patience > 0:
        callbacks.append(EarlyStoppingCallback(early_stopping_patience=patience))

    # 6. Trainer
    trainer = SFTTrainer(
        model=model,
        args=sft_config,
        train_dataset=ds_dict["train"],
        eval_dataset=ds_dict["dev"],
        processing_class=tokenizer,
        callbacks=callbacks,
    )

    # 7. Train
    print("\n" + "=" * 60)
    print("  Starting QA COT SFT Training")
    print("=" * 60)
    trainer.train()

    # 8. Save final LoRA adapter
    final_dir = output_dir / "final_lora"
    trainer.save_model(str(final_dir))
    tokenizer.save_pretrained(str(final_dir))
    print(f"\n[Save] LoRA adapter saved to: {final_dir}")

    # 9. Push to Hub (optional)
    if hub_cfg.get("push_to_hub", False):
        org = hub_cfg.get("org", "")
        repo_name = f"qa-{version}-cot-{model_cfg['name'].split('/')[-1]}"
        hub_repo_id = f"{org}/{repo_name}" if org else repo_name
        print(f"[Hub] Pushing to: {hub_repo_id}")
        trainer.push_to_hub(repo_id=hub_repo_id, private=hub_cfg.get("hf_private", True))

    # 10. Cleanup
    del model, trainer
    gc.collect()
    torch.cuda.empty_cache() if torch.cuda.is_available() else None

    print("\n[Done] Training complete.")
    return str(final_dir)


# ─── Merge LoRA → Full Model ─────────────────────────────────────────────────

def merge_and_push(cfg: dict, lora_dir: str | None = None):
    """Merge LoRA adapter into base model and optionally push to Hub."""
    from peft import PeftModel

    project_root = resolve_project_root()
    model_cfg = cfg["model"]
    hub_cfg = cfg.get("hub", {})
    version = hub_cfg.get("repo_version", "v01")

    if lora_dir is None:
        lora_dir = str(project_root / "outputs" / f"qa-sft-{version}" / "final_lora")

    print(f"[Merge] Loading base: {model_cfg['name']}")
    base_model = AutoModelForCausalLM.from_pretrained(
        model_cfg["name"],
        trust_remote_code=model_cfg.get("trust_remote_code", True),
        torch_dtype=torch.bfloat16,
        device_map="cpu",
    )
    tokenizer = AutoTokenizer.from_pretrained(
        model_cfg["name"], trust_remote_code=model_cfg.get("trust_remote_code", True)
    )

    print(f"[Merge] Loading LoRA from: {lora_dir}")
    model = PeftModel.from_pretrained(base_model, lora_dir)
    model = model.merge_and_unload()

    merged_dir = str(project_root / "outputs" / f"qa-sft-{version}" / "merged")
    model.save_pretrained(merged_dir)
    tokenizer.save_pretrained(merged_dir)
    print(f"[Merge] Merged model saved to: {merged_dir}")

    if hub_cfg.get("push_to_hub", False):
        org = hub_cfg.get("org", "")
        repo_name = f"qa-{version}-cot-{model_cfg['name'].split('/')[-1]}"
        hub_repo_id = f"{org}/{repo_name}" if org else repo_name
        print(f"[Hub] Pushing merged model to: {hub_repo_id}")
        model.push_to_hub(hub_repo_id, private=hub_cfg.get("hf_private", True))
        tokenizer.push_to_hub(hub_repo_id, private=hub_cfg.get("hf_private", True))

    print("[Done] Merge complete.")
    return merged_dir


# ─── CLI ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Train QA COT model (Stage 2)")
    parser.add_argument("--config", type=str, default="configs/qa_model.yaml")
    parser.add_argument("--debug-samples", type=int, default=None, help="Limit samples for quick test")
    parser.add_argument("--merge", action="store_true", help="Merge LoRA into base model after training")
    parser.add_argument("--merge-only", action="store_true", help="Only merge (skip training)")
    parser.add_argument("--lora-dir", type=str, default=None, help="Path to LoRA adapter for merge")
    args = parser.parse_args()

    cfg = load_config(args.config)

    if args.merge_only:
        merge_and_push(cfg, args.lora_dir)
    else:
        lora_dir = train(cfg, debug_max_samples=args.debug_samples)
        if args.merge:
            merge_and_push(cfg, lora_dir)


if __name__ == "__main__":
    main()
