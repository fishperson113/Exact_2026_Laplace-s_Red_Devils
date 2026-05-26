"""Một file JSON thống nhất: siêu tham số, log từng epoch (train/dev/test), log_history HF."""
from __future__ import annotations

import json
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from services.config import LogicSFTConfig

from .generation_eval import collect_inference_samples


def _project_root_from_cfg(cfg: LogicSFTConfig) -> Path | None:
    if cfg.app_dir is not None:
        return Path(cfg.app_dir).resolve()
    return None


def try_read_logic_model_yaml(cfg: LogicSFTConfig) -> tuple[dict[str, Any] | None, str | None]:
    """Đọc `configs/logic_model.yaml` nếu tìm thấy; trả về (dict, raw_text)."""
    root = _project_root_from_cfg(cfg)
    if root is None:
        return None, None
    p = root / "configs" / "logic_model.yaml"
    if not p.is_file():
        return None, None
    raw = p.read_text(encoding="utf-8")
    try:
        import yaml as _yaml

        data = _yaml.safe_load(raw) or {}
    except ImportError:
        return None, raw
    except _yaml.YAMLError:
        data = {}
    return data if isinstance(data, dict) else {}, raw


def hyperparameters_logic_model_shape(cfg: LogicSFTConfig) -> dict[str, Any]:
    """Cấu trúc gần giống `configs/logic_model.yaml` — lấy từ `LogicSFTConfig` thực tế chạy train."""
    return {
        "model": {
            "name": cfg.model_name,
            "trust_remote_code": cfg.trust_remote_code,
            "max_seq_length": cfg.max_seq_length,
            "gen_max_new_tokens": cfg.gen_max_new_tokens,
        },
        "lora": {
            "r": cfg.lora_r,
            "alpha": cfg.lora_alpha,
            "dropout": cfg.lora_dropout,
            "target_modules": list(cfg.lora_target_modules),
        },
        "training": {
            "num_train_epochs": cfg.num_train_epochs,
            "per_device_train_batch_size": cfg.per_device_train_batch_size,
            "per_device_eval_batch_size": cfg.per_device_eval_batch_size,
            "gradient_accumulation_steps": cfg.gradient_accumulation_steps,
            "learning_rate": cfg.learning_rate,
            "warmup_ratio": cfg.warmup_ratio,
            "weight_decay": cfg.weight_decay,
            "logging_steps": cfg.logging_steps,
            "bf16": cfg.bf16,
            "gradient_checkpointing": cfg.gradient_checkpointing,
            "train_seed": cfg.train_seed,
            "gpu_profile": cfg.gpu_profile,
        },
        "data": {
            "split_ratios": list(cfg.split_ratios),
            "split_seed": cfg.split_seed,
            "include_fol_in_user": cfg.include_fol_in_user,
        },
        "paths": {
            "sft_processed_dir": str(cfg.sft_processed_dir) if cfg.sft_processed_dir else None,
            "processed_dir": str(cfg.processed_dir) if cfg.processed_dir else None,
            "out_dir": str(cfg.out_dir) if cfg.out_dir else None,
            "checkpoint_dir": str(cfg.checkpoint_dir) if cfg.checkpoint_dir else None,
        },
        "hub": {
            "hf_org": cfg.hf_org,
            "logic_repo_version": cfg.logic_repo_version,
            "logic_repo_method": cfg.logic_repo_method,
            "logic_repo_model_slug": cfg.logic_repo_model_slug,
            "hf_repo_id": cfg.hf_repo_id,
            "resolved_hf_repo": cfg.resolved_hf_repo(),
            "push_to_hub": cfg.push_to_hub,
            "hf_private": cfg.hf_private,
        },
        "eval": {
            "eval_gen_batch_size": cfg.eval_gen_batch_size,
            "eval_accuracy_max_samples": cfg.eval_accuracy_max_samples,
            "log_test_each_epoch": cfg.log_test_each_epoch,
            "experiment_inference_sample_n": cfg.experiment_inference_sample_n,
        },
    }


def _json_safe(obj: Any) -> Any:
    if isinstance(obj, Path):
        return str(obj.resolve())
    if isinstance(obj, dict):
        return {k: _json_safe(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_json_safe(v) for v in obj]
    if isinstance(obj, float):
        if obj != obj:  # NaN
            return None
        return obj
    return obj


def logic_config_flat_dict(cfg: LogicSFTConfig) -> dict[str, Any]:
    return _json_safe(asdict(cfg))


def build_experiment_log_document(
    cfg: LogicSFTConfig,
    *,
    epoch_metrics: list[dict[str, Any]],
    trainer_log_history: list[dict[str, Any]],
    train_metrics_final: dict[str, Any] | None,
    train_result_global_step: int | None,
    train_result_epochs: float | None,
    test_eval: dict[str, Any] | None,
    inference_samples: list[dict[str, Any]] | None,
) -> dict[str, Any]:
    yaml_dict, yaml_raw = try_read_logic_model_yaml(cfg)
    return {
        "schema": "logic_sft_experiment_log_v2",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "hyperparameters_effective": hyperparameters_logic_model_shape(cfg),
        "configs_logic_model_yaml_parsed": yaml_dict,
        "configs_logic_model_yaml_raw": yaml_raw,
        "logic_sft_config_flat": logic_config_flat_dict(cfg),
        "epoch_metrics_train_dev_test": epoch_metrics,
        "trainer_log_history": trainer_log_history,
        "final_trainer_eval_metrics": train_metrics_final,
        "train_result": {
            "global_step": train_result_global_step,
            "epochs_trained": train_result_epochs,
        },
        "test_eval_after_train": test_eval,
        "inference_samples": inference_samples or [],
    }


def write_experiment_log_json(path: Path, doc: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(doc, indent=2, ensure_ascii=False), encoding="utf-8")


def merge_test_into_experiment_log(
    path: Path,
    test_eval: dict[str, Any],
    inference_samples: list[dict[str, Any]],
) -> None:
    """Ghi đè / bổ sung phần test + inference sau `run_test_eval`."""
    if not path.is_file():
        return
    doc = json.loads(path.read_text(encoding="utf-8"))
    doc["test_eval_after_train"] = test_eval
    doc["inference_samples"] = inference_samples
    doc["updated_utc"] = datetime.now(timezone.utc).isoformat()
    write_experiment_log_json(path, doc)


def build_inference_samples_after_train(
    cfg: LogicSFTConfig,
    trainer,
    dataset_dict,
) -> list[dict[str, Any]]:
    n = cfg.experiment_inference_sample_n
    if n <= 0 or cfg.out_dir is None:
        return []
    tok = getattr(trainer, "processing_class", None) or getattr(trainer, "tokenizer", None)
    return collect_inference_samples(
        cfg,
        trainer.model,
        tok,
        dataset_dict["test"],
        n,
        max_samples_cap=cfg.eval_accuracy_max_samples,
    )
