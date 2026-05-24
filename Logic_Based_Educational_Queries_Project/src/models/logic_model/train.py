"""Huấn luyện LoRA SFT + đánh giá accuracy trên dev/test (logic_model)."""
from __future__ import annotations

import inspect
import json

import torch
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from trl import SFTConfig

from data.dataset import build_dataset_dict
from services.config import LogicSFTConfig

from .experiment_log import (
    build_experiment_log_document,
    build_inference_samples_after_train,
    merge_test_into_experiment_log,
    write_experiment_log_json,
)
from .generation_eval import accuracy_on_dataset
from .trainer_accuracy import AccuracySFTTrainer


def load_tokenizer(cfg: LogicSFTConfig):
    tok = AutoTokenizer.from_pretrained(
        cfg.model_name, trust_remote_code=cfg.trust_remote_code
    )
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    tok.padding_side = "left"
    return tok


def _gpu_train_profile(cfg: LogicSFTConfig) -> str:
    profile = cfg.gpu_profile
    if profile == "auto" and torch.cuda.is_available():
        profile = "kaggle_p100" if torch.cuda.get_device_capability(0)[0] < 7 else "default"
    return profile


def build_model(cfg: LogicSFTConfig):
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


def _persist_experiment_log(
    cfg: LogicSFTConfig,
    trainer: AccuracySFTTrainer,
    train_result,
    train_metrics_final: dict | None,
    test_eval: dict | None,
    inference_samples: list | None,
) -> None:
    if cfg.out_dir is None:
        return
    tr_metrics = getattr(train_result, "metrics", None) or {}
    doc = build_experiment_log_document(
        cfg,
        epoch_metrics=list(trainer.epoch_metric_rows),
        trainer_log_history=[dict(x) for x in trainer.state.log_history],
        train_metrics_final=train_metrics_final,
        train_result_global_step=getattr(train_result, "global_step", None),
        train_result_epochs=(
            float(trainer.state.epoch)
            if getattr(trainer.state, "epoch", None) is not None
            else tr_metrics.get("epoch")
        ),
        test_eval=test_eval,
        inference_samples=inference_samples,
    )
    write_experiment_log_json(cfg.out_dir / "experiment_log.json", doc)


def run_training(cfg: LogicSFTConfig):
    """SFT + chọn checkpoint theo eval_accuracy (không phải eval_loss)."""
    if not cfg.run_train:
        return None

    tokenizer = load_tokenizer(cfg)
    dataset_dict = build_dataset_dict(cfg, tokenizer)
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
        metric_for_best_model="eval_accuracy",
        greater_is_better=True,
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
        logic_cfg=cfg,
        logic_dataset_dict=dataset_dict,
    )
    if "processing_class" in inspect.signature(AccuracySFTTrainer.__init__).parameters:
        trainer_kwargs["processing_class"] = tokenizer
    else:
        trainer_kwargs["tokenizer"] = tokenizer
    trainer = AccuracySFTTrainer(**trainer_kwargs)
    train_result = trainer.train()
    cfg.checkpoint_dir.mkdir(parents=True, exist_ok=True)
    trainer.save_model(str(cfg.checkpoint_dir))
    tokenizer.save_pretrained(str(cfg.checkpoint_dir))

    metrics = trainer.evaluate()
    with open(cfg.out_dir / "train_metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    _persist_experiment_log(
        cfg,
        trainer,
        train_result,
        train_metrics_final=metrics,
        test_eval=None,
        inference_samples=None,
    )
    return train_result, trainer, tokenizer, dataset_dict


def _trainer_tokenizer(trainer: AccuracySFTTrainer):
    return getattr(trainer, "processing_class", None) or getattr(
        trainer, "tokenizer", None
    )


def run_test_eval(
    cfg: LogicSFTConfig, trainer: AccuracySFTTrainer, dataset_dict
) -> dict:
    tok = _trainer_tokenizer(trainer)
    test_acc = accuracy_on_dataset(
        cfg,
        trainer.model,
        tok,
        dataset_dict["test"],
        max_samples=cfg.eval_accuracy_max_samples,
    )
    out = {"test_accuracy": test_acc}
    if cfg.out_dir:
        with open(cfg.out_dir / "test_accuracy.json", "w", encoding="utf-8") as f:
            json.dump(out, f, indent=2)
        samples = build_inference_samples_after_train(cfg, trainer, dataset_dict)
        merge_test_into_experiment_log(cfg.out_dir / "experiment_log.json", out, samples)
    return out


def run_train_and_test(cfg: LogicSFTConfig | None = None):
    cfg = cfg or LogicSFTConfig.from_env()
    train_out = run_training(cfg)
    if train_out is None:
        return None
    _result, trainer, _tok, dataset_dict = train_out
    return run_test_eval(cfg, trainer, dataset_dict)


if __name__ == "__main__":
    out = run_train_and_test()
    print("Test metrics:", out)
