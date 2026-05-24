"""Huấn luyện LoRA SFT: premises NL → premises FOL (JSON)."""
from __future__ import annotations

import inspect
import json

import torch
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from trl import SFTConfig, SFTTrainer

from data.fol_dataset import build_fol_dataset_dict
from services.config_fol import FolSFTConfig

from .experiment_log import (
    build_fol_experiment_log_document,
    write_experiment_log_json,
)
from .generation_fol_eval import collect_fol_inference_samples, fol_exact_match_rate


def load_tokenizer(cfg: FolSFTConfig):
    tok = AutoTokenizer.from_pretrained(
        cfg.model_name, trust_remote_code=cfg.trust_remote_code
    )
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    return tok


def _gpu_train_profile(cfg: FolSFTConfig) -> str:
    profile = cfg.gpu_profile
    if profile == "auto" and torch.cuda.is_available():
        profile = "kaggle_p100" if torch.cuda.get_device_capability(0)[0] < 7 else "default"
    return profile


def build_model(cfg: FolSFTConfig):
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
        model = prepare_model_for_kbit_training(model)
        train_bf16, train_fp16 = False, True
    else:
        dtype = torch.bfloat16 if cfg.bf16 else torch.float16
        model = AutoModelForCausalLM.from_pretrained(
            cfg.model_name,
            torch_dtype=dtype,
            trust_remote_code=cfg.trust_remote_code,
            device_map={"": 0},
        )
        train_bf16, train_fp16 = cfg.bf16, not cfg.bf16

    model.config.use_cache = False
    peft_config = LoraConfig(
        r=cfg.lora_r,
        lora_alpha=cfg.lora_alpha,
        lora_dropout=cfg.lora_dropout,
        target_modules=list(cfg.lora_target_modules),
        bias="none",
        task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, peft_config)
    model.print_trainable_parameters()
    if cfg.gradient_checkpointing:
        model.enable_input_require_grads()
        model.gradient_checkpointing_enable(
            gradient_checkpointing_kwargs={"use_reentrant": False}
        )
    return model, train_bf16, train_fp16


def _epoch_metrics_from_history(trainer: SFTTrainer) -> list[dict]:
    rows: list[dict] = []
    for h in trainer.state.log_history:
        if "eval_loss" not in h:
            continue
        rows.append(
            {
                "epoch": h.get("epoch"),
                "step": h.get("step"),
                "eval_loss": h.get("eval_loss"),
            }
        )
    return rows


def _persist_fol_experiment_log(
    cfg: FolSFTConfig,
    trainer: SFTTrainer,
    train_result,
    train_metrics_final: dict | None,
    fol_eval: dict | None,
    filter_stats: dict | None,
    fol_inference_samples: list | None,
) -> None:
    if cfg.out_dir is None:
        return
    tr_metrics = getattr(train_result, "metrics", None) or {}
    doc = build_fol_experiment_log_document(
        cfg,
        epoch_metrics=_epoch_metrics_from_history(trainer),
        trainer_log_history=[dict(x) for x in trainer.state.log_history],
        train_metrics_final=train_metrics_final,
        train_result_global_step=getattr(train_result, "global_step", None),
        train_result_epochs=(
            float(trainer.state.epoch)
            if getattr(trainer.state, "epoch", None) is not None
            else tr_metrics.get("epoch")
        ),
        fol_eval=fol_eval,
        filter_stats=filter_stats,
        fol_inference_samples=fol_inference_samples,
    )


def run_fol_eval_all_splits(
    cfg: FolSFTConfig,
    trainer: SFTTrainer,
    dataset_dict,
) -> dict[str, Any]:
    tok = getattr(trainer, "processing_class", None) or getattr(
        trainer, "tokenizer", None
    )
    lim = cfg.eval_fol_max_samples
    out: dict[str, Any] = {}
    for split in ("dev", "test"):
        ds = dataset_dict[split]
        metrics = fol_exact_match_rate(cfg, trainer.model, tok, ds, max_samples=lim)
        out[split] = metrics
    if cfg.out_dir:
        with open(cfg.out_dir / "fol_eval_metrics.json", "w", encoding="utf-8") as f:
            json.dump(out, f, indent=2)
    return out


def run_training(cfg: FolSFTConfig):
    if not cfg.run_train:
        return None

    tokenizer = load_tokenizer(cfg)
    dataset_dict, filter_stats = build_fol_dataset_dict(cfg, tokenizer)
    model, train_bf16, train_fp16 = build_model(cfg)

    assert cfg.out_dir is not None and cfg.checkpoint_dir is not None

    sft_config = SFTConfig(
        output_dir=str(cfg.out_dir),
        num_train_epochs=cfg.num_train_epochs,
        per_device_train_batch_size=cfg.per_device_train_batch_size,
        per_device_eval_batch_size=cfg.per_device_eval_batch_size,
        gradient_accumulation_steps=cfg.gradient_accumulation_steps,
        learning_rate=cfg.learning_rate,
        warmup_ratio=cfg.warmup_ratio,
        lr_scheduler_type="cosine",
        weight_decay=cfg.weight_decay,
        logging_steps=cfg.logging_steps,
        logging_strategy="steps",
        logging_first_step=True,
        disable_tqdm=False,
        eval_strategy="epoch",
        save_strategy="epoch",
        save_total_limit=2,
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        greater_is_better=False,
        bf16=train_bf16,
        fp16=train_fp16,
        gradient_checkpointing=False,
        seed=cfg.train_seed,
        report_to="none",
        max_length=cfg.max_seq_length,
        dataset_text_field="text",
        packing=False,
        remove_unused_columns=False,
    )

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
    train_result = trainer.train()
    cfg.checkpoint_dir.mkdir(parents=True, exist_ok=True)
    trainer.save_model(str(cfg.checkpoint_dir))
    tokenizer.save_pretrained(str(cfg.checkpoint_dir))

    metrics = trainer.evaluate()
    with open(cfg.out_dir / "train_metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    fol_eval = run_fol_eval_all_splits(cfg, trainer, dataset_dict)
    tok = getattr(trainer, "processing_class", None) or getattr(
        trainer, "tokenizer", None
    )
    fol_samples = collect_fol_inference_samples(
        cfg,
        trainer.model,
        tok,
        dataset_dict["test"],
        cfg.experiment_inference_sample_n,
        max_samples_cap=cfg.eval_fol_max_samples,
    )

    _persist_fol_experiment_log(
        cfg,
        trainer,
        train_result,
        train_metrics_final=metrics,
        fol_eval=fol_eval,
        filter_stats=filter_stats,
        fol_inference_samples=fol_samples,
    )
    return train_result, trainer, tokenizer, dataset_dict


def run_train_and_eval(cfg: FolSFTConfig | None = None):
    cfg = cfg or FolSFTConfig.from_env()
    return run_training(cfg)


if __name__ == "__main__":
    out = run_train_and_eval()
    print("Done:", out is not None)
