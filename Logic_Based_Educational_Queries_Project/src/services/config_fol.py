"""Cấu hình SFT NL → premises-FOL — đọc ``configs/fol_model.yaml`` (Git); ``.env`` chỉ cho token (HF/GIT). Tùy chọn ghi đè bằng biến ``FOL_*`` trên shell/CI."""
from __future__ import annotations

import os
from dataclasses import dataclass, field, fields
from pathlib import Path
from typing import Any

from services.config import (
    _env_bool,
    _env_int,
    _env_key_set,
    _env_opt_str,
    _path_from_env,
    load_dotenv_for_logic,
)
from services.hf_repo_naming import build_fol_hf_repo_id


def _fol_find_project_root_for_yaml() -> Path | None:
    """Thư mục gốc repo có ``configs/fol_model.yaml`` (ưu tiên ``LOGIC_PROJECT_ROOT``, rồi cwd, rồi vị trí package)."""
    if v := os.environ.get("LOGIC_PROJECT_ROOT", "").strip():
        p = Path(v).expanduser().resolve()
        if (p / "configs" / "fol_model.yaml").is_file():
            return p
    here = Path.cwd().resolve()
    for base in (here, *here.parents):
        if (base / "configs" / "fol_model.yaml").is_file():
            return base
    pkg_root = Path(__file__).resolve().parent.parent.parent  # .../src/services -> repo root
    if (pkg_root / "configs" / "fol_model.yaml").is_file():
        return pkg_root
    return None


def _fol_config_dict_from_yaml(project_root: Path) -> dict[str, Any]:
    """Đọc ``configs/fol_model.yaml`` → dict trùng tên field ``FolSFTConfig`` (không ghi đè .env)."""
    p = project_root / "configs" / "fol_model.yaml"
    if not p.is_file():
        return {}
    try:
        import yaml as _yaml
    except ImportError:
        return {}
    try:
        data = _yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    except _yaml.YAMLError:
        return {}
    if not isinstance(data, dict):
        return {}
    out: dict[str, Any] = {}

    if m := data.get("model"):
        if isinstance(m, dict):
            if "name" in m:
                out["model_name"] = str(m["name"])
            if "trust_remote_code" in m:
                out["trust_remote_code"] = bool(m["trust_remote_code"])
            if "max_seq_length" in m:
                out["max_seq_length"] = int(m["max_seq_length"])
            if "gen_max_new_tokens" in m:
                out["gen_max_new_tokens"] = int(m["gen_max_new_tokens"])

    if lo := data.get("lora"):
        if isinstance(lo, dict):
            if "r" in lo:
                out["lora_r"] = int(lo["r"])
            if "alpha" in lo:
                out["lora_alpha"] = int(lo["alpha"])
            if "dropout" in lo:
                out["lora_dropout"] = float(lo["dropout"])

    if t := data.get("training"):
        if isinstance(t, dict):
            int_keys = (
                "num_train_epochs",
                "per_device_train_batch_size",
                "per_device_eval_batch_size",
                "gradient_accumulation_steps",
                "logging_steps",
                "train_seed",
            )
            float_keys = ("learning_rate", "warmup_ratio", "weight_decay")
            bool_keys = (
                "bf16",
                "gradient_checkpointing",
                "load_in_8bit",
                "use_unsloth",
                "unsloth_train_on_responses_only",
                "use_adamw_8bit",
            )
            for k in int_keys:
                if k in t and t[k] is not None:
                    out[k] = int(t[k])
            for k in float_keys:
                if k in t and t[k] is not None:
                    out[k] = float(t[k])
            for k in bool_keys:
                if k in t and t[k] is not None:
                    out[k] = bool(t[k])
            if "gpu_profile" in t and t["gpu_profile"] is not None:
                out["gpu_profile"] = str(t["gpu_profile"]).strip().lower()
            if "early_stopping_patience" in t and t["early_stopping_patience"] is not None:
                out["early_stopping_patience"] = int(t["early_stopping_patience"])
            if "load_best_model_at_end" in t and t["load_best_model_at_end"] is not None:
                out["load_best_model_at_end"] = bool(t["load_best_model_at_end"])
            if "metric_for_best_model" in t and t["metric_for_best_model"] is not None:
                out["metric_for_best_model"] = str(t["metric_for_best_model"]).strip()
            if "greater_is_better" in t and t["greater_is_better"] is not None:
                out["greater_is_better"] = bool(t["greater_is_better"])
            if "best_model_exact_match_max_samples" in t:
                v = t["best_model_exact_match_max_samples"]
                if v is None or (
                    isinstance(v, str) and v.strip().lower() in ("null", "none", "", "all")
                ):
                    out["best_model_exact_match_max_samples"] = None
                else:
                    out["best_model_exact_match_max_samples"] = int(v)
            if "save_total_limit" in t and t["save_total_limit"] is not None:
                out["save_total_limit"] = int(t["save_total_limit"])
            if "delete_output_checkpoints_after_save" in t and t["delete_output_checkpoints_after_save"] is not None:
                out["delete_output_checkpoints_after_save"] = bool(
                    t["delete_output_checkpoints_after_save"]
                )
            if "debug_max_train_samples" in t:
                v = t["debug_max_train_samples"]
                if v is None or (isinstance(v, str) and v.strip().lower() in ("null", "none", "", "all")):
                    out["debug_max_train_samples"] = None
                else:
                    out["debug_max_train_samples"] = int(v)

    if paths := data.get("paths"):
        if isinstance(paths, dict) and (sub := paths.get("processed_subdir")):
            subp = Path(str(sub).strip())
            out["sft_processed_dir"] = (
                subp if subp.is_absolute() else (project_root / subp).resolve()
            )

    if hub := data.get("hub"):
        if isinstance(hub, dict):
            if "org" in hub and hub["org"] is not None:
                out["hf_org"] = str(hub["org"])
            if "repo_version" in hub and hub["repo_version"] is not None:
                out["fol_repo_version"] = str(hub["repo_version"])
            if "data_variant" in hub and hub["data_variant"] is not None:
                out["fol_data_variant"] = str(hub["data_variant"]).strip().lower()
            if "push_to_hub" in hub and hub["push_to_hub"] is not None:
                out["push_to_hub"] = bool(hub["push_to_hub"])
            if "hf_private" in hub and hub["hf_private"] is not None:
                out["hf_private"] = bool(hub["hf_private"])

    if ev := data.get("eval"):
        if isinstance(ev, dict):
            if "eval_gen_batch_size" in ev and ev["eval_gen_batch_size"] is not None:
                out["eval_gen_batch_size"] = int(ev["eval_gen_batch_size"])
            if "eval_fol_max_samples" in ev:
                out["eval_fol_max_samples"] = ev["eval_fol_max_samples"]
            if "experiment_inference_sample_n" in ev and ev["experiment_inference_sample_n"] is not None:
                out["experiment_inference_sample_n"] = int(ev["experiment_inference_sample_n"])
            if "inference_latency_benchmark_n" in ev and ev["inference_latency_benchmark_n"] is not None:
                out["inference_latency_benchmark_n"] = int(ev["inference_latency_benchmark_n"])
            if "inference_latency_warmup" in ev and ev["inference_latency_warmup"] is not None:
                out["inference_latency_warmup"] = int(ev["inference_latency_warmup"])
            if "inference_latency_benchmark_split" in ev and ev["inference_latency_benchmark_split"] is not None:
                out["inference_latency_benchmark_split"] = str(
                    ev["inference_latency_benchmark_split"]
                ).strip().lower()
            if "hub_reload_after_push" in ev and ev["hub_reload_after_push"] is not None:
                out["hub_reload_after_push"] = bool(ev["hub_reload_after_push"])
            if "hub_reload_random_test_n" in ev and ev["hub_reload_random_test_n"] is not None:
                out["hub_reload_random_test_n"] = int(ev["hub_reload_random_test_n"])
            if "hub_reload_random_seed" in ev and ev["hub_reload_random_seed"] is not None:
                out["hub_reload_random_seed"] = int(ev["hub_reload_random_seed"])

    return out


def fol_should_load_in_8bit(cfg: "FolSFTConfig") -> bool:
    """True → nạp base weights **INT8** (BitsAndBytes ``load_in_8bit``), tiết kiệm VRAM, chính xác hơn NF4.

    Bật khi: ``load_in_8bit``; hoặc ``gpu_profile`` ∈ {8bit, bnb_8bit, 4bit, bnb_4bit, kaggle_p100}
    (``4bit``/``FOL_LOAD_IN_4BIT`` giữ tên cũ nhưng thực tế dùng **8-bit**);
    hoặc ``gpu_profile=auto`` trên GPU compute capability < 7.
    """
    import torch

    if cfg.load_in_8bit:
        return True
    p = (cfg.gpu_profile or "auto").strip().lower()
    if p in ("8bit", "bnb_8bit", "4bit", "bnb_4bit", "kaggle_p100"):
        return True
    if p == "auto" and torch.cuda.is_available():
        major, _minor = torch.cuda.get_device_capability(0)
        if major < 7:
            return True
    return False


@dataclass
class FolSFTConfig:
    """Fine-tune sinh `premises_fol` từ `premises_nl` (đồng bộ độ dài)."""

    model_name: str = "Qwen/Qwen2.5-3B-Instruct"
    max_seq_length: int = 4096
    trust_remote_code: bool = True
    gen_max_new_tokens: int = 512

    lora_r: int = 10
    lora_alpha: int = 16
    lora_dropout: float = 0.05
    lora_target_modules: tuple[str, ...] = (
        "q_proj",
        "k_proj",
        "v_proj",
        "o_proj",
        "gate_proj",
        "up_proj",
        "down_proj",
    )

    # gpu_profile: auto | default | kaggle_p100 | 8bit | bnb_8bit | 4bit | bnb_4bit — xem fol_should_load_in_8bit
    gpu_profile: str = "auto"
    # True = luôn INT8 8-bit (mọi GPU); hoặc FOL_LOAD_IN_8BIT=1 (FOL_LOAD_IN_4BIT=1 vẫn bật 8-bit, tên legacy)
    load_in_8bit: bool = False

    num_train_epochs: int = 10
    per_device_train_batch_size: int = 1
    per_device_eval_batch_size: int = 1
    gradient_accumulation_steps: int = 8
    learning_rate: float = 2e-4
    warmup_ratio: float = 0.05
    weight_decay: float = 0.01
    logging_steps: int = 10
    bf16: bool = True
    gradient_checkpointing: bool = True
    train_seed: int = 3407
    run_train: bool = True
    debug_max_train_samples: int | None = None
    """Giới hạn số mẫu mỗi split (train/dev/test) để test nhanh luồng. None hoặc 0 = dùng hết."""
    # Trainer: checkpoint tốt nhất + early stop (theo metric trên dev mỗi epoch)
    early_stopping_patience: int = 0
    """0 = tắt. Ví dụ 3 → ``EarlyStoppingCallback(patience=3)`` (đếm theo lần **eval**, khớp ``eval_strategy``)."""
    load_best_model_at_end: bool = True
    metric_for_best_model: str = "eval_loss"
    greater_is_better: bool = False  # với exact_match trên dev → thường True
    best_model_exact_match_max_samples: int | None = None

    save_total_limit: int = 1
    """Số checkpoint tối đa trong ``out_dir`` lúc train (HF xoay + giữ best khi ``load_best_model_at_end``)."""
    delete_output_checkpoints_after_save: bool = True
    """Sau ``trainer.save_model`` → ``checkpoint_dir`` (vd. ``final_lora``), xóa ``checkpoint-*`` trong ``out_dir`` để tiết kiệm đĩa."""

    eval_gen_batch_size: int = 2
    eval_fol_max_samples: int | None = None
    experiment_inference_sample_n: int = 3
    # Sau FT: đo greedy 1 prompt/mẫu, trung bình trên N index ngẫu nhiên (0 = tắt).
    inference_latency_benchmark_n: int = 30
    inference_latency_warmup: int = 2
    inference_latency_benchmark_split: str = "test"
    """train | dev | test — split dùng cho benchmark latency."""
    inference_latency_benchmark_seed: int | None = None
    """None = dùng ``train_seed``."""
    # Sau khi merge+push Hub: tải lại merged từ Hub, exact-match + mẫu test ngẫu nhiên (CLI / tmux).
    hub_reload_after_push: bool = True
    """Tắt: ``hub_reload_after_push: false`` hoặc ``FOL_HUB_RELOAD_AFTER_PUSH=false``."""
    hub_reload_random_test_n: int = 20
    """Số mẫu **test** greedy ngẫu nhiên sau khi tải model từ Hub (0 = tắt). Env: ``FOL_HUB_RELOAD_RANDOM_N``."""
    hub_reload_random_seed: int = 42
    """Env: ``FOL_HUB_RELOAD_SEED``."""

    # --- Unsloth / VRAM (T4): FastLanguageModel + loss chỉ assistant + adamw_8bit ---
    use_unsloth: bool = False
    """Bật khi đã ``pip install unsloth``; xem ``models/fol_model/unsloth_sft.py``."""
    unsloth_train_on_responses_only: bool = True
    """Bọc ``SFTTrainer`` bằng ``unsloth.chat_templates.train_on_responses_only``."""
    unsloth_instruction_marker: str = "<|im_start|>user\n"
    unsloth_response_marker: str = "<|im_start|>assistant\n"
    use_adamw_8bit: bool = True
    """``SFTConfig.optim=adamw_8bit`` (bitsandbytes), áp dụng cả pipeline HF/PEFT không Unsloth."""
    unsloth_load_in_4bit: bool = False
    """Unsloth: NF4 4-bit (VRAM thấp hơn nhiều so với 16-bit / INT8 base). Bật khi T4 vẫn OOM."""

    eval_accumulation_steps: int = 4
    """Trainer: tích lũy eval theo nhiều micro-batch → giảm đỉnh VRAM lúc ``evaluate()``."""

    hf_org: str = "Laplaces-Red-Devils"
    fol_repo_version: str = "v01"
    fol_data_variant: str = "origin"  # origin | augmented
    fol_repo_model_slug: str | None = None
    hf_repo_id: str | None = None
    hf_private: bool = False
    hf_commit_message: str = "fol SFT — NL to premises-FOL"
    push_to_hub: bool = False

    app_dir: Path | None = None
    notebook_root: Path | None = None
    sft_processed_dir: Path | None = None
    out_dir: Path | None = None
    processed_dir: Path | None = None
    checkpoint_dir: Path | None = None

    def resolved_hf_repo(self) -> str:
        if self.hf_repo_id:
            return self.hf_repo_id
        return build_fol_hf_repo_id(
            org=self.hf_org,
            version=self.fol_repo_version,
            variant=self.fol_data_variant,
            model_id=self.model_name,
            model_slug_override=self.fol_repo_model_slug,
        )

    @classmethod
    def from_env(cls, load_dotenv_file: bool = True, **overrides: Any) -> FolSFTConfig:
        """Nạp ``configs/fol_model.yaml`` (nếu tìm thấy repo), rồi ghi đè bởi biến ``FOL_*`` / ``LOGIC_SFT_PROCESSED_DIR`` chỉ khi được set, cuối cùng ``**overrides``."""
        if load_dotenv_file:
            load_dotenv_for_logic()

        _root = _fol_find_project_root_for_yaml()
        yaml_defaults = _fol_config_dict_from_yaml(_root) if _root is not None else {}

        kwargs: dict[str, Any] = {}

        if v := _env_opt_str("FOL_MODEL_NAME"):
            kwargs["model_name"] = v
        if v := _env_int("FOL_MAX_SEQ_LENGTH"):
            kwargs["max_seq_length"] = v
        if v := _env_int("FOL_GEN_MAX_NEW_TOKENS"):
            kwargs["gen_max_new_tokens"] = v

        if v := _env_int("FOL_LORA_R"):
            kwargs["lora_r"] = v
        if v := _env_int("FOL_LORA_ALPHA"):
            kwargs["lora_alpha"] = v

        if v := _env_opt_str("FOL_GPU_PROFILE"):
            kwargs["gpu_profile"] = v.strip().lower()

        if _env_bool("FOL_LOAD_IN_4BIT", default=False):
            kwargs["load_in_8bit"] = True
        elif _env_key_set("FOL_LOAD_IN_8BIT"):
            kwargs["load_in_8bit"] = _env_bool("FOL_LOAD_IN_8BIT", default=False)

        if v := _env_int("FOL_NUM_TRAIN_EPOCHS"):
            kwargs["num_train_epochs"] = v
        if v := _env_int("FOL_TRAIN_SEED"):
            kwargs["train_seed"] = v
        if v := _env_int("FOL_EARLY_STOPPING_PATIENCE"):
            kwargs["early_stopping_patience"] = v
        if v := _env_int("FOL_SAVE_TOTAL_LIMIT"):
            kwargs["save_total_limit"] = v
        if (v := _env_opt_str("FOL_METRIC_FOR_BEST_MODEL")) is not None:
            kwargs["metric_for_best_model"] = v.strip()
        if _env_key_set("FOL_GREATER_IS_BETTER"):
            kwargs["greater_is_better"] = _env_bool("FOL_GREATER_IS_BETTER", default=True)
        if (es := _env_opt_str("FOL_BEST_MODEL_EM_MAX_SAMPLES")) is not None:
            low = es.lower()
            if low in ("", "none", "null", "all"):
                kwargs["best_model_exact_match_max_samples"] = None
            else:
                kwargs["best_model_exact_match_max_samples"] = int(es.strip())

        if _env_key_set("FOL_PRUNE_TRAINER_CHECKPOINTS"):
            kwargs["delete_output_checkpoints_after_save"] = _env_bool(
                "FOL_PRUNE_TRAINER_CHECKPOINTS", default=True
            )

        es = _env_opt_str("FOL_EVAL_FOL_MAX_SAMPLES")
        if es is not None and es.lower() in ("none", "", "all"):
            kwargs["eval_fol_max_samples"] = None
        elif v := _env_int("FOL_EVAL_FOL_MAX_SAMPLES"):
            kwargs["eval_fol_max_samples"] = v

        if (es := _env_opt_str("FOL_EXPERIMENT_INFERENCE_SAMPLES")) is not None:
            low = es.lower()
            if low in ("0", "none", "off", ""):
                kwargs["experiment_inference_sample_n"] = 0
            else:
                kwargs["experiment_inference_sample_n"] = int(es.strip())

        if (es := _env_opt_str("FOL_INFER_BENCH_N")) is not None:
            low = es.lower()
            if low in ("0", "none", "off", ""):
                kwargs["inference_latency_benchmark_n"] = 0
            else:
                kwargs["inference_latency_benchmark_n"] = int(es.strip())
        if v := _env_int("FOL_INFER_BENCH_WARMUP"):
            kwargs["inference_latency_warmup"] = v
        if (v := _env_opt_str("FOL_INFER_BENCH_SPLIT")) is not None:
            kwargs["inference_latency_benchmark_split"] = v.strip().lower()
        if (es := _env_opt_str("FOL_INFER_BENCH_SEED")) is not None:
            low = es.lower()
            if low in ("", "none", "train", "same"):
                kwargs["inference_latency_benchmark_seed"] = None
            else:
                kwargs["inference_latency_benchmark_seed"] = int(es.strip())

        if (es := _env_opt_str("FOL_DEBUG_MAX_TRAIN_SAMPLES")) is not None:
            low = es.lower()
            if low in ("", "none", "null", "all", "0"):
                kwargs["debug_max_train_samples"] = None
            else:
                kwargs["debug_max_train_samples"] = int(es.strip())

        if _env_key_set("FOL_RUN_TRAIN"):
            kwargs["run_train"] = _env_bool("FOL_RUN_TRAIN", default=True)
        if _env_key_set("FOL_PUSH_TO_HUB"):
            kwargs["push_to_hub"] = _env_bool("FOL_PUSH_TO_HUB", default=False)
        if _env_key_set("FOL_HF_PRIVATE"):
            kwargs["hf_private"] = _env_bool("FOL_HF_PRIVATE", default=False)

        if v := _env_opt_str("FOL_HF_ORG"):
            kwargs["hf_org"] = v
        if v := _env_opt_str("FOL_REPO_VERSION"):
            kwargs["fol_repo_version"] = v
        if v := _env_opt_str("FOL_DATA_VARIANT"):
            kwargs["fol_data_variant"] = v.strip().lower()
        if v := _env_opt_str("FOL_REPO_MODEL_SLUG"):
            kwargs["fol_repo_model_slug"] = v
        if v := _env_opt_str("FOL_HF_REPO_ID"):
            kwargs["hf_repo_id"] = v
        if v := _env_opt_str("FOL_HF_COMMIT_MESSAGE"):
            kwargs["hf_commit_message"] = v

        if v := _env_opt_str("FOL_SFT_PROCESSED_DIR"):
            kwargs["sft_processed_dir"] = Path(v).expanduser().resolve()
        elif v := _env_opt_str("LOGIC_SFT_PROCESSED_DIR"):
            kwargs["sft_processed_dir"] = Path(v).expanduser().resolve()

        if v := _env_int("FOL_EVAL_GEN_BATCH_SIZE"):
            kwargs["eval_gen_batch_size"] = v

        if _env_key_set("FOL_USE_UNSLOTH"):
            kwargs["use_unsloth"] = _env_bool("FOL_USE_UNSLOTH", default=False)
        if _env_key_set("FOL_UNSLOTH_RESPONSES_ONLY"):
            kwargs["unsloth_train_on_responses_only"] = _env_bool(
                "FOL_UNSLOTH_RESPONSES_ONLY", default=True
            )
        if _env_key_set("FOL_USE_ADAMW_8BIT"):
            kwargs["use_adamw_8bit"] = _env_bool("FOL_USE_ADAMW_8BIT", default=True)
        if (v := _env_opt_str("FOL_UNSLOTH_INSTRUCTION_MARKER")) is not None:
            kwargs["unsloth_instruction_marker"] = v
        if (v := _env_opt_str("FOL_UNSLOTH_RESPONSE_MARKER")) is not None:
            kwargs["unsloth_response_marker"] = v

        if _env_key_set("FOL_UNSLOTH_NF4"):
            kwargs["unsloth_load_in_4bit"] = _env_bool("FOL_UNSLOTH_NF4", default=False)
        if v := _env_int("FOL_EVAL_ACCUMULATION_STEPS"):
            kwargs["eval_accumulation_steps"] = v

        if _env_key_set("FOL_HUB_RELOAD_AFTER_PUSH"):
            kwargs["hub_reload_after_push"] = _env_bool("FOL_HUB_RELOAD_AFTER_PUSH", default=True)
        if v := _env_int("FOL_HUB_RELOAD_RANDOM_N"):
            kwargs["hub_reload_random_test_n"] = v
        if v := _env_int("FOL_HUB_RELOAD_SEED"):
            kwargs["hub_reload_random_seed"] = v

        valid = {f.name for f in fields(cls)}
        filtered = {k: v for k, v in kwargs.items() if k in valid}
        merged = {**yaml_defaults, **filtered, **overrides}
        if merged.pop("load_in_4bit", None):
            merged["load_in_8bit"] = True
        merged = {k: v for k, v in merged.items() if k in valid}
        return cls(**merged)
