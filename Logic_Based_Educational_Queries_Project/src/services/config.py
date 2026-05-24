from __future__ import annotations

import os
from dataclasses import dataclass, field, fields
from pathlib import Path
from typing import Any

from services.hf_repo_naming import build_hf_repo_id


def load_dotenv_for_logic() -> Path | None:
    """Một chỗ gọi `python-dotenv`: không ghi đè biến môi trường đã có sẵn."""
    try:
        from dotenv import load_dotenv
    except ImportError:
        return None
    candidates: list[Path] = []
    if extra := os.environ.get("LOGIC_ENV_FILE", "").strip():
        candidates.append(Path(extra).expanduser().resolve())
    pkg_root = Path(__file__).resolve().parent  # .../src/services
    project_root = pkg_root.parent.parent  # .../src/services -> thư mục gốc dự án
    candidates.extend(
        [
            Path.cwd() / ".env",
            pkg_root.parent / ".env",
            project_root / ".env",
        ]
    )
    for p in candidates:
        if p.is_file():
            load_dotenv(p, override=False)
            return p.resolve()
    return None


def _env_bool(key: str, default: bool = False) -> bool:
    v = os.environ.get(key)
    if v is None:
        return default
    return v.strip().lower() in ("1", "true", "yes", "y", "on")


def _env_int(key: str, default: int | None = None) -> int | None:
    v = os.environ.get(key)
    if v is None or v.strip() == "":
        return default
    return int(v.strip())


def _env_opt_str(key: str) -> str | None:
    v = os.environ.get(key)
    if v is None:
        return None
    s = v.strip()
    return s if s else None


def _path_from_env(key: str, default: Path) -> Path:
    raw = _env_opt_str(key)
    if raw:
        return Path(raw).expanduser().resolve()
    return default


@dataclass
class LogicSFTConfig:
    """Cấu hình tập trung — nạp từ `.env` qua `from_env()` hoặc chỉnh thủ công."""

    # Model (LLM được fine-tune)
    model_name: str = "Qwen/Qwen3.5-4B"
    max_seq_length: int = 2048
    trust_remote_code: bool = True
    gen_max_new_tokens: int = 160

    # LoRA
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

    # Data
    data_source: str = "local"  # "local" | "drive"
    data_filename: str = "Logic_Based_Educational_Queries.json"
    gdrive_file_id: str = "1-8Wu-2FikPQIX7_rRiY3wfe7c229To2Z"
    gdrive_zip_name: str = "EXACT2026_dataset_2026-05-15.zip"
    gdrive_url: str = (
        "https://drive.google.com/file/d/1-8Wu-2FikPQIX7_rRiY3wfe7c229To2Z/view?usp=drive_link"
    )
    data_root: Path = field(default_factory=lambda: Path.cwd() / "exact_data")
    split_ratios: tuple[float, float, float] = (0.8, 0.1, 0.1)
    split_seed: int = 42
    include_fol_in_user: bool = True

    # Training
    gpu_profile: str = "auto"  # "auto" | "kaggle_p100" | "default"
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

    eval_gen_batch_size: int = 2
    eval_accuracy_max_samples: int | None = None
    # Log / Hub: mỗi epoch đo thêm test (tốn GPU); inference mẫu ghi vào experiment_log.json
    log_test_each_epoch: bool = True
    experiment_inference_sample_n: int = 5

    # Hub — tên repo: {hf_org}/logic-{version}-{method}-{model_slug}
    hf_org: str = "Laplaces-Red-Devils"
    logic_repo_version: str = "v01"
    logic_repo_method: str = "fewshot"
    logic_repo_model_slug: str | None = None  # None = tự sinh từ model_name
    hf_repo_id: str | None = None  # Ghi đè toàn bộ nếu cần (vd. test repo khác)
    hf_private: bool = False
    hf_commit_message: str = "logic SFT — best checkpoint theo eval_accuracy"
    push_to_hub: bool = False

    app_dir: Path | None = None
    notebook_root: Path | None = None
    data_path: Path | None = None
    sft_processed_dir: Path | None = None  # thư mục logic_sft; None = auto / LOGIC_SFT_PROCESSED_DIR
    out_dir: Path | None = None
    processed_dir: Path | None = None
    checkpoint_dir: Path | None = None

    def resolved_hf_repo(self) -> str:
        if self.hf_repo_id:
            return self.hf_repo_id
        return build_hf_repo_id(
            org=self.hf_org,
            version=self.logic_repo_version,
            method=self.logic_repo_method,
            model_id=self.model_name,
            model_slug_override=self.logic_repo_model_slug,
        )

    @classmethod
    def from_env(cls, load_dotenv_file: bool = True, **overrides: Any) -> LogicSFTConfig:
        """
        Đọc `.env` (nếu có `python-dotenv`) rồi map biến môi trường → config.
        `overrides` ghi đè cuối cùng (tiện cho notebook).
        """
        if load_dotenv_file:
            load_dotenv_for_logic()

        kwargs: dict[str, Any] = {}

        if v := _env_opt_str("LOGIC_MODEL_NAME"):
            kwargs["model_name"] = v
        if v := _env_opt_str("LOGIC_DATA_SOURCE"):
            kwargs["data_source"] = v.strip().lower()
        if v := _env_opt_str("LOGIC_DATA_FILENAME"):
            kwargs["data_filename"] = v
        kwargs["data_root"] = _path_from_env("LOGIC_DATA_ROOT", Path.cwd() / "exact_data")

        if v := _env_int("LOGIC_MAX_SEQ_LENGTH"):
            kwargs["max_seq_length"] = v
        if v := _env_int("LOGIC_GEN_MAX_NEW_TOKENS"):
            kwargs["gen_max_new_tokens"] = v

        if v := _env_int("LOGIC_LORA_R"):
            kwargs["lora_r"] = v
        if v := _env_int("LOGIC_LORA_ALPHA"):
            kwargs["lora_alpha"] = v

        if v := _env_opt_str("LOGIC_GPU_PROFILE"):
            kwargs["gpu_profile"] = v.strip().lower()

        if v := _env_int("LOGIC_NUM_TRAIN_EPOCHS"):
            kwargs["num_train_epochs"] = v
        if v := _env_int("LOGIC_TRAIN_SEED"):
            kwargs["train_seed"] = v

        es = _env_opt_str("LOGIC_EVAL_ACCURACY_MAX_SAMPLES")
        if es is not None and es.lower() in ("none", "", "all"):
            kwargs["eval_accuracy_max_samples"] = None
        elif v := _env_int("LOGIC_EVAL_ACCURACY_MAX_SAMPLES"):
            kwargs["eval_accuracy_max_samples"] = v

        kwargs["log_test_each_epoch"] = _env_bool("LOGIC_LOG_TEST_EACH_EPOCH", default=True)
        if (es := _env_opt_str("LOGIC_EXPERIMENT_INFERENCE_SAMPLES")) is not None:
            low = es.lower()
            if low in ("0", "none", "off", ""):
                kwargs["experiment_inference_sample_n"] = 0
            else:
                kwargs["experiment_inference_sample_n"] = int(es.strip())

        kwargs["run_train"] = _env_bool("LOGIC_RUN_TRAIN", default=True)
        kwargs["push_to_hub"] = _env_bool("LOGIC_PUSH_TO_HUB", default=False)
        kwargs["hf_private"] = _env_bool("LOGIC_HF_PRIVATE", default=False)

        if v := _env_opt_str("LOGIC_HF_ORG"):
            kwargs["hf_org"] = v
        if v := _env_opt_str("LOGIC_REPO_VERSION"):
            kwargs["logic_repo_version"] = v
        if v := _env_opt_str("LOGIC_REPO_METHOD"):
            kwargs["logic_repo_method"] = v
        if v := _env_opt_str("LOGIC_REPO_MODEL_SLUG"):
            kwargs["logic_repo_model_slug"] = v
        if v := _env_opt_str("LOGIC_HF_REPO_ID"):
            kwargs["hf_repo_id"] = v
        if v := _env_opt_str("LOGIC_HF_COMMIT_MESSAGE"):
            kwargs["hf_commit_message"] = v
        if v := _env_opt_str("LOGIC_SFT_PROCESSED_DIR"):
            kwargs["sft_processed_dir"] = Path(v).expanduser().resolve()

        # Chỉ truyền field hợp lệ của dataclass
        valid = {f.name for f in fields(cls)}
        filtered = {k: v for k, v in kwargs.items() if k in valid}
        merged = {**filtered, **overrides}
        return cls(**merged)
