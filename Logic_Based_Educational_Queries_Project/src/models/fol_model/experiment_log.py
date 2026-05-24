"""experiment_log.json cho pipeline FOL SFT."""
from __future__ import annotations

import json
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from services.config_fol import FolSFTConfig


def _project_root_from_cfg(cfg: FolSFTConfig) -> Path | None:
    if cfg.app_dir is not None:
        return Path(cfg.app_dir).resolve()
    return None


def try_read_fol_model_yaml(cfg: FolSFTConfig) -> tuple[dict[str, Any] | None, str | None]:
    root = _project_root_from_cfg(cfg)
    if root is None:
        return None, None
    p = root / "configs" / "fol_model.yaml"
    if not p.is_file():
        return None, None
    raw = p.read_text(encoding="utf-8")
    try:
        import yaml as _yaml

        data = _yaml.safe_load(raw) or {}
    except ImportError:
        return None, raw
    except Exception:
        data = {}
    return data if isinstance(data, dict) else {}, raw


def hyperparameters_fol_shape(cfg: FolSFTConfig) -> dict[str, Any]:
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
        "paths": {
            "sft_processed_dir": str(cfg.sft_processed_dir) if cfg.sft_processed_dir else None,
            "processed_dir": str(cfg.processed_dir) if cfg.processed_dir else None,
            "out_dir": str(cfg.out_dir) if cfg.out_dir else None,
            "checkpoint_dir": str(cfg.checkpoint_dir) if cfg.checkpoint_dir else None,
        },
        "hub": {
            "hf_org": cfg.hf_org,
            "fol_repo_version": cfg.fol_repo_version,
            "fol_data_variant": cfg.fol_data_variant,
            "fol_repo_model_slug": cfg.fol_repo_model_slug,
            "hf_repo_id": cfg.hf_repo_id,
            "resolved_hf_repo": cfg.resolved_hf_repo(),
            "push_to_hub": cfg.push_to_hub,
            "hf_private": cfg.hf_private,
        },
        "eval": {
            "eval_gen_batch_size": cfg.eval_gen_batch_size,
            "eval_fol_max_samples": cfg.eval_fol_max_samples,
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
        if obj != obj:
            return None
        return obj
    return obj


def fol_config_flat_dict(cfg: FolSFTConfig) -> dict[str, Any]:
    return _json_safe(asdict(cfg))


def build_fol_experiment_log_document(
    cfg: FolSFTConfig,
    *,
    epoch_metrics: list[dict[str, Any]],
    trainer_log_history: list[dict[str, Any]],
    train_metrics_final: dict[str, Any] | None,
    train_result_global_step: int | None,
    train_result_epochs: float | None,
    fol_eval: dict[str, Any] | None,
    filter_stats: dict[str, int] | None,
    fol_inference_samples: list[dict[str, Any]] | None = None,
    fol_preflight_baseline: dict[str, Any] | None = None,
    fol_test_benchmark: dict[str, Any] | None = None,
) -> dict[str, Any]:
    yaml_dict, yaml_raw = try_read_fol_model_yaml(cfg)
    doc: dict[str, Any] = {
        "schema": "fol_sft_experiment_log_v1",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "hyperparameters_effective": hyperparameters_fol_shape(cfg),
        "configs_fol_model_yaml_parsed": yaml_dict,
        "configs_fol_model_yaml_raw": yaml_raw,
        "fol_sft_config_flat": fol_config_flat_dict(cfg),
        "fol_filter_rows_dropped_per_split": filter_stats or {},
        "epoch_metrics_train_dev": epoch_metrics,
        "trainer_log_history": trainer_log_history,
        "final_trainer_eval_metrics": train_metrics_final,
        "train_result": {
            "global_step": train_result_global_step,
            "epochs_trained": train_result_epochs,
        },
        "fol_eval_greedy": fol_eval or {},
        "fol_inference_samples": fol_inference_samples or [],
    }
    if fol_preflight_baseline is not None:
        doc["fol_preflight_baseline"] = _json_safe(fol_preflight_baseline)
    if fol_test_benchmark is not None:
        doc["fol_test_benchmark"] = _json_safe(fol_test_benchmark)
    if fol_eval:
        doc["fol_eval_dev_exact_match"] = fol_eval.get("dev", {}).get("exact_match_rate")
        doc["fol_eval_test_exact_match"] = fol_eval.get("test", {}).get("exact_match_rate")
    return doc


def write_experiment_log_json(path: Path, doc: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(doc, indent=2, ensure_ascii=False), encoding="utf-8")


def merge_fol_eval_into_experiment_log(path: Path, fol_eval: dict[str, Any]) -> None:
    if not path.is_file():
        return
    doc = json.loads(path.read_text(encoding="utf-8"))
    doc["fol_eval_greedy"] = fol_eval
    doc["fol_eval_dev_exact_match"] = fol_eval.get("dev", {}).get("exact_match_rate")
    doc["fol_eval_test_exact_match"] = fol_eval.get("test", {}).get("exact_match_rate")
    doc["updated_utc"] = datetime.now(timezone.utc).isoformat()
    write_experiment_log_json(path, doc)
