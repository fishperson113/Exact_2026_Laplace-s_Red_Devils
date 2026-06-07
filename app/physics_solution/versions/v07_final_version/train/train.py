"""E: SFT orchestrator — Unsloth QLoRA on the v07 code-gen trajectories.

    PYTHONPATH=. <venv>/bin/python -m \
      app.physics_solution.versions.v07_final_version.train.train \
      --config app/physics_solution/versions/v07_final_version/train/configs/sft.yaml

Flow: load (Unsloth+LoRA) -> render data -> SFTTrainer (loss on assistant only)
-> save adapter+tokenizer -> merge -> push adapter & merged + model card.
"""

from __future__ import annotations

# Unsloth MUST be imported before trl/transformers (it patches them).
import unsloth  # noqa: F401  isort:skip

import argparse
import inspect
import json
from pathlib import Path

import yaml
from transformers import EarlyStoppingCallback
from trl import SFTConfig, SFTTrainer

from .sft_data import load_datasets
from .sft_model import load_model_and_tokenizer


def _build_sft_config(cfg: dict, bf16: bool) -> SFTConfig:
    t = cfg["training"]
    kw = dict(
        output_dir=cfg["paths"]["out_dir"],
        num_train_epochs=float(t["num_train_epochs"]),
        per_device_train_batch_size=int(t["per_device_train_batch_size"]),
        per_device_eval_batch_size=int(t.get("per_device_eval_batch_size", t["per_device_train_batch_size"])),
        gradient_accumulation_steps=int(t["gradient_accumulation_steps"]),
        learning_rate=float(t["learning_rate"]),
        lr_scheduler_type=t.get("lr_scheduler_type", "cosine"),
        warmup_ratio=float(t.get("warmup_ratio", 0.05)),
        weight_decay=float(t.get("weight_decay", 0.0)),
        logging_steps=int(t.get("logging_steps", 5)),
        bf16=bf16,
        fp16=not bf16,
        optim=t.get("optim", "adamw_8bit"),
        seed=int(t.get("seed", 42)),
        eval_strategy=t.get("eval_strategy", "epoch"),
        save_strategy=t.get("save_strategy", "epoch"),
        load_best_model_at_end=bool(t.get("load_best_model_at_end", True)),
        metric_for_best_model=t.get("metric_for_best_model", "eval_loss"),
        greater_is_better=bool(t.get("greater_is_better", False)),
        save_total_limit=int(t.get("save_total_limit", 2)),
        packing=bool(t.get("packing", False)),
        dataset_text_field="text",
        report_to="none",
    )
    sig = inspect.signature(SFTConfig.__init__).parameters
    msl = int(cfg["model"]["max_seq_length"])
    if "max_seq_length" in sig:
        kw["max_seq_length"] = msl
    elif "max_length" in sig:
        kw["max_length"] = msl
    return SFTConfig(**{k: v for k, v in kw.items() if k in sig})


def run(config_path: str, skip_hub: bool = False) -> dict:
    cfg = yaml.safe_load(Path(config_path).read_text())
    t = cfg["training"]

    model, tokenizer, bf16 = load_model_and_tokenizer(cfg)
    dd = load_datasets(cfg, tokenizer)

    sft_config = _build_sft_config(cfg, bf16)
    trainer = SFTTrainer(
        model=model,
        args=sft_config,
        train_dataset=dd["train"],
        eval_dataset=dd["val"],
        processing_class=tokenizer,
    )
    if int(t.get("early_stopping_patience", 0) or 0) > 0:
        trainer.add_callback(EarlyStoppingCallback(early_stopping_patience=int(t["early_stopping_patience"])))

    if t.get("train_on_responses_only", True):
        from unsloth.chat_templates import train_on_responses_only

        trainer = train_on_responses_only(
            trainer,
            instruction_part=t["instruction_marker"],
            response_part=t["response_marker"],
        )

    print("[train] starting trainer.train() ...", flush=True)
    train_result = trainer.train()
    print("[train] done.", flush=True)

    # --- save adapter + tokenizer (reloads exactly) ---
    adapter_dir = Path(cfg["paths"]["adapter_dir"])
    adapter_dir.mkdir(parents=True, exist_ok=True)
    trainer.save_model(str(adapter_dir))
    tokenizer.save_pretrained(str(adapter_dir))

    # --- metrics for the model card ---
    hist = trainer.state.log_history
    eval_losses = [h["eval_loss"] for h in hist if "eval_loss" in h]
    metrics = {
        "train_loss": train_result.metrics.get("train_loss"),
        "best_eval_loss": min(eval_losses) if eval_losses else None,
        "final_eval_loss": eval_losses[-1] if eval_losses else None,
        "epochs": cfg["training"]["num_train_epochs"],
        "n_train": len(dd["train"]),
        "n_val": len(dd["val"]),
    }
    metrics_path = Path(cfg["paths"]["out_dir"]) / "metrics.json"
    metrics_path.parent.mkdir(parents=True, exist_ok=True)
    metrics_path.write_text(json.dumps(metrics, indent=2))
    print("[train] metrics:", json.dumps(metrics, indent=2))

    if cfg["hub"].get("push_to_hub") and not skip_hub:
        from .merge_push import merge_and_push

        urls = merge_and_push(cfg, str(adapter_dir), metrics)
        print("[train] pushed:", urls)
    else:
        print("[train] skip_hub -> not pushing. Adapter at", adapter_dir)
    return metrics


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--skip-hub", action="store_true", help="train+save locally, no Hub push")
    args = ap.parse_args()
    run(args.config, skip_hub=args.skip_hub)
