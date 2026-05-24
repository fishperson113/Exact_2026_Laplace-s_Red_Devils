"""Huấn luyện LoRA SFT: premises NL → premises FOL (JSON)."""
from __future__ import annotations

import inspect
import json
from typing import Any

import torch
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from trl import SFTConfig, SFTTrainer

from data.fol_dataset import build_fol_dataset_dict
from services.config_fol import FolSFTConfig, fol_should_load_in_8bit

from .experiment_log import (
    build_fol_experiment_log_document,
    write_experiment_log_json,
)
from .fol_preflight import load_preflight_baseline, mean_nll_completion_on_split
from .generation_fol_eval import (
    collect_fol_inference_samples,
    fol_exact_match_on_splits,
    fol_exact_match_rate,
)


def load_tokenizer(cfg: FolSFTConfig):
    tok = AutoTokenizer.from_pretrained(
        cfg.model_name, trust_remote_code=cfg.trust_remote_code
    )
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    # Decoder-only + batched generate: pad bên trái để token cuối cùng của prompt nằm sát phải.
    tok.padding_side = "left"
    return tok


def build_model(cfg: FolSFTConfig):
    if fol_should_load_in_8bit(cfg):
        print("[FOL train] Nạp base weights: INT8 8-bit (BitsAndBytes), tiết kiệm VRAM hơn full fp16/bf16.", flush=True)
        bnb_config = BitsAndBytesConfig(load_in_8bit=True)
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


def _build_fol_sft_config(cfg: FolSFTConfig, train_bf16: bool, train_fp16: bool) -> SFTConfig:
    optim = "adamw_8bit" if cfg.use_adamw_8bit else "adamw_torch"
    sft_kw: dict[str, Any] = dict(
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
        optim=optim,
        gradient_checkpointing=False,
        seed=cfg.train_seed,
        report_to="none",
        max_length=cfg.max_seq_length,
        dataset_text_field="text",
        packing=False,
        remove_unused_columns=False,
    )
    if "max_seq_length" in inspect.signature(SFTConfig.__init__).parameters:
        sft_kw["max_seq_length"] = cfg.max_seq_length
    return SFTConfig(**sft_kw)


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
    *,
    fol_preflight_baseline: dict | None = None,
    fol_test_benchmark: dict | None = None,
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
        fol_preflight_baseline=fol_preflight_baseline,
        fol_test_benchmark=fol_test_benchmark,
    )
    write_experiment_log_json(cfg.out_dir / "experiment_log.json", doc)


def run_fol_eval_all_splits(
    cfg: FolSFTConfig,
    trainer: SFTTrainer,
    dataset_dict,
) -> dict[str, Any]:
    tok = getattr(trainer, "processing_class", None) or getattr(
        trainer, "tokenizer", None
    )
    lim = cfg.eval_fol_max_samples
    out = fol_exact_match_on_splits(
        cfg,
        trainer.model,
        tok,
        dataset_dict,
        splits=("train", "dev", "test"),
        max_samples=lim,
    )
    for split, m in out.items():
        print(
            f"[FOL eval] {split}: accuracy={m['exact_match_rate']:.4f} "
            f"({m['exact_match_count']}/{m['total']})"
        )
    if cfg.out_dir:
        with open(cfg.out_dir / "fol_eval_metrics.json", "w", encoding="utf-8") as f:
            json.dump(out, f, indent=2)
    return out


def run_training(cfg: FolSFTConfig):
    if not cfg.run_train:
        return None

    print("[FOL train] Bắt đầu: tokenizer + dataset + model (bước này có thể vài phút, chưa có thanh epoch).", flush=True)

    if cfg.use_unsloth:
        from .unsloth_sft import (
            apply_train_on_responses_only,
            is_unsloth_available,
            load_unsloth_model_and_tokenizer,
        )

        if not is_unsloth_available():
            raise RuntimeError(
                "cfg.use_unsloth=True nhưng chưa cài `unsloth`. Chạy: pip install unsloth  "
                "hoặc đặt FOL_USE_UNSLOTH=false / FolSFTConfig.from_env(use_unsloth=False)."
            )
        model, tokenizer, train_bf16, train_fp16 = load_unsloth_model_and_tokenizer(cfg)
        print("[FOL train] Đã nạp tokenizer (Unsloth).", flush=True)
        dataset_dict, filter_stats = build_fol_dataset_dict(cfg, tokenizer)
    else:
        tokenizer = load_tokenizer(cfg)
        print("[FOL train] Đã nạp tokenizer.", flush=True)
        dataset_dict, filter_stats = build_fol_dataset_dict(cfg, tokenizer)
        model, train_bf16, train_fp16 = build_model(cfg)

    print(
        "[FOL train] Dataset:",
        {k: len(dataset_dict[k]) for k in dataset_dict},
        "| filter_stats:",
        filter_stats,
        flush=True,
    )
    if not cfg.use_unsloth:
        print("[FOL train] Đã nạp model + LoRA. Chuẩn bị SFTTrainer.train() (tqdm từng epoch/step sẽ hiện bên dưới).", flush=True)
    else:
        print(
            "[FOL train][Unsloth] Dataset xong. optim="
            + ("adamw_8bit" if cfg.use_adamw_8bit else "adamw_torch")
            + "; train_on_responses_only="
            + str(cfg.unsloth_train_on_responses_only)
            + ".",
            flush=True,
        )

    assert cfg.out_dir is not None and cfg.checkpoint_dir is not None

    sft_config = _build_fol_sft_config(cfg, train_bf16, train_fp16)

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
        print("[FOL train][Unsloth] Áp train_on_responses_only (loss chỉ trên assistant) …", flush=True)
        trainer = apply_train_on_responses_only(trainer, cfg)

    print("[FOL train] Bắt đầu trainer.train() …", flush=True)
    train_result = trainer.train()
    print("[FOL train] trainer.train() xong.", flush=True)
    cfg.checkpoint_dir.mkdir(parents=True, exist_ok=True)
    trainer.save_model(str(cfg.checkpoint_dir))
    tokenizer.save_pretrained(str(cfg.checkpoint_dir))

    print("[FOL train] trainer.evaluate() trên dev (loss) …", flush=True)
    metrics = trainer.evaluate()
    with open(cfg.out_dir / "train_metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    print("[FOL train] trainer.evaluate() trên test (loss) …", flush=True)
    test_trainer_metrics = trainer.evaluate(eval_dataset=dataset_dict["test"])

    print("[FOL train] Greedy exact-match JSON trên train/dev/test (lâu nếu full split + null max_samples) …", flush=True)
    fol_eval = run_fol_eval_all_splits(cfg, trainer, dataset_dict)
    tok = getattr(trainer, "processing_class", None) or getattr(
        trainer, "tokenizer", None
    )
    post_test_exact = fol_exact_match_rate(
        cfg,
        trainer.model,
        tok,
        dataset_dict["test"],
        max_samples=None,
        split_label="test_post_ft_exact",
    )
    print("[FOL train] mean NLL completion trên test (full) …", flush=True)
    post_test_nll = mean_nll_completion_on_split(
        cfg, trainer.model, tok, dataset_dict["test"], max_samples=None
    )
    print("[Sau FT] test full exact_match:", post_test_exact)
    print("[Sau FT] test full mean NLL (completion):", post_test_nll)
    print("[Sau FT] trainer.evaluate(test):", test_trainer_metrics)

    preflight = load_preflight_baseline(cfg.out_dir)
    bench: dict[str, Any] = {
        "before_finetune_summary": {
            "test_exact_match_full": (preflight or {}).get("test_exact_match_full"),
            "test_mean_nll_completion_full": (preflight or {}).get(
                "test_mean_nll_completion_full"
            ),
        },
        "after_finetune": {
            "test_exact_match_full": post_test_exact,
            "test_mean_nll_completion_full": post_test_nll,
            "trainer_evaluate_test_metrics": test_trainer_metrics,
            "fol_eval_greedy_splits_respecting_FOL_EVAL_FOL_MAX_SAMPLES": fol_eval,
        },
    }
    with open(cfg.out_dir / "fol_test_benchmark.json", "w", encoding="utf-8") as f:
        json.dump(bench, f, indent=2, ensure_ascii=False)

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
        fol_preflight_baseline=preflight,
        fol_test_benchmark=bench,
    )
    return train_result, trainer, tokenizer, dataset_dict


def run_train_and_eval(cfg: FolSFTConfig | None = None):
    cfg = cfg or FolSFTConfig.from_env()
    return run_training(cfg)


if __name__ == "__main__":
    out = run_train_and_eval()
    print("Done:", out is not None)
