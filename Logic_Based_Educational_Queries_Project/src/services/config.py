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


def _env_key_set(key: str) -> bool:
    v = os.environ.get(key)
    return v is not None and str(v).strip() != ""


def _logic_find_project_root_for_yaml() -> Path | None:
    """Thư mục gốc repo có ``configs/logic_model.yaml`` (cwd rồi cha ông; rồi gói ``src/services`` → repo)."""
    if v := os.environ.get("LOGIC_PROJECT_ROOT", "").strip():
        p = Path(v).expanduser().resolve()
        if (p / "configs" / "logic_model.yaml").is_file():
            return p
    here = Path.cwd().resolve()
    for base in (here, *here.parents):
        if (base / "configs" / "logic_model.yaml").is_file():
            return base
    pkg_root = Path(__file__).resolve().parent.parent.parent  # .../src/services -> repo root
    if (pkg_root / "configs" / "logic_model.yaml").is_file():
        return pkg_root
    return None


def _logic_config_dict_from_yaml(project_root: Path) -> dict[str, Any]:
    """Đọc ``configs/logic_model.yaml`` → dict trùng tên field ``LogicSFTConfig``."""
    p = project_root / "configs" / "logic_model.yaml"
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
            if "name" in m and m["name"] is not None:
                out["model_name"] = str(m["name"])
            if "trust_remote_code" in m and m["trust_remote_code"] is not None:
                out["trust_remote_code"] = bool(m["trust_remote_code"])
            if "max_seq_length" in m and m["max_seq_length"] is not None:
                out["max_seq_length"] = int(m["max_seq_length"])
            if "gen_max_new_tokens" in m and m["gen_max_new_tokens"] is not None:
                out["gen_max_new_tokens"] = int(m["gen_max_new_tokens"])

    if lo := data.get("lora"):
        if isinstance(lo, dict):
            if "r" in lo and lo["r"] is not None:
                out["lora_r"] = int(lo["r"])
            if "alpha" in lo and lo["alpha"] is not None:
                out["lora_alpha"] = int(lo["alpha"])
            if "dropout" in lo and lo["dropout"] is not None:
                out["lora_dropout"] = float(lo["dropout"])

    if t := data.get("training"):
        if isinstance(t, dict):
            for k in (
                "num_train_epochs",
                "per_device_train_batch_size",
                "per_device_eval_batch_size",
                "gradient_accumulation_steps",
                "logging_steps",
                "train_seed",
            ):
                if k in t and t[k] is not None:
                    out[k] = int(t[k])
            for k in ("learning_rate", "warmup_ratio", "weight_decay"):
                if k in t and t[k] is not None:
                    out[k] = float(t[k])
            for k in ("bf16", "gradient_checkpointing"):
                if k in t and t[k] is not None:
                    out[k] = bool(t[k])
            if "gpu_profile" in t and t["gpu_profile"] is not None:
                out["gpu_profile"] = str(t["gpu_profile"]).strip().lower()

    if d := data.get("data"):
        if isinstance(d, dict):
            if "split_ratios" in d and d["split_ratios"] is not None and isinstance(
                d["split_ratios"], (list, tuple)
            ):
                out["split_ratios"] = tuple(float(x) for x in d["split_ratios"])
            if "split_seed" in d and d["split_seed"] is not None:
                out["split_seed"] = int(d["split_seed"])
            if "include_fol_in_user" in d and d["include_fol_in_user"] is not None:
                out["include_fol_in_user"] = bool(d["include_fol_in_user"])
            if "data_source" in d and d["data_source"] is not None:
                out["data_source"] = str(d["data_source"]).strip().lower()

    if paths := data.get("paths"):
        if isinstance(paths, dict):
            if sub := paths.get("processed_subdir"):
                subp = Path(str(sub).strip())
                out["sft_processed_dir"] = (
                    subp if subp.is_absolute() else (project_root / subp).resolve()
                )
            if raw := paths.get("raw_filename"):
                out["data_filename"] = str(raw).strip()

    if hub := data.get("hub"):
        if isinstance(hub, dict):
            if "org" in hub and hub["org"] is not None:
                out["hf_org"] = str(hub["org"])
            if "repo_version" in hub and hub["repo_version"] is not None:
                out["logic_repo_version"] = str(hub["repo_version"])
            if "repo_method" in hub and hub["repo_method"] is not None:
                out["logic_repo_method"] = str(hub["repo_method"]).strip().lower()
            if "push_to_hub" in hub and hub["push_to_hub"] is not None:
                out["push_to_hub"] = bool(hub["push_to_hub"])
            if "hf_private" in hub and hub["hf_private"] is not None:
                out["hf_private"] = bool(hub["hf_private"])

    if ev := data.get("eval"):
        if isinstance(ev, dict):
            if "log_test_each_epoch" in ev and ev["log_test_each_epoch"] is not None:
                out["log_test_each_epoch"] = bool(ev["log_test_each_epoch"])
            if (
                "experiment_inference_sample_n" in ev
                and ev["experiment_inference_sample_n"] is not None
            ):
                out["experiment_inference_sample_n"] = int(ev["experiment_inference_sample_n"])
            if "eval_gen_batch_size" in ev and ev["eval_gen_batch_size"] is not None:
                out["eval_gen_batch_size"] = int(ev["eval_gen_batch_size"])
            if "eval_accuracy_max_samples" in ev:
                evs = ev["eval_accuracy_max_samples"]
                if evs is None or (
                    isinstance(evs, str) and evs.strip().lower() in ("none", "all", "")
                ):
                    out["eval_accuracy_max_samples"] = None
                elif evs is not None:
                    out["eval_accuracy_max_samples"] = int(evs)

    return out


@dataclass
class LogicSFTConfig:
    """Cấu hình tập trung — đọc ``configs/logic_model.yaml`` (theo repo), tùy chọn ghi đè biến ``LOGIC_*`` trên shell/CI, rồi ``**overrides``."""

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
    sft_processed_dir: Path | None = None  # thư mục có train.csv (mặc định data/processed); None = auto
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
        Nạp ``configs/logic_model.yaml`` (nếu tìm thấy repo), rồi ghi đè bởi biến ``LOGIC_*`` chỉ khi biến đó được set,
        cuối cùng ``**overrides`` (tiện notebook). File ``.env`` chỉ cần token — xem ``.env.example``.
        """
        if load_dotenv_file:
            load_dotenv_for_logic()

        _root = _logic_find_project_root_for_yaml()
        yaml_defaults = _logic_config_dict_from_yaml(_root) if _root is not None else {}

        kwargs: dict[str, Any] = {}

        if v := _env_opt_str("LOGIC_MODEL_NAME"):
            kwargs["model_name"] = v
        if v := _env_opt_str("LOGIC_DATA_SOURCE"):
            kwargs["data_source"] = v.strip().lower()
        if v := _env_opt_str("LOGIC_DATA_FILENAME"):
            kwargs["data_filename"] = v
        if _env_key_set("LOGIC_DATA_ROOT"):
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

        if _env_key_set("LOGIC_LOG_TEST_EACH_EPOCH"):
            kwargs["log_test_each_epoch"] = _env_bool("LOGIC_LOG_TEST_EACH_EPOCH", default=True)
        if (es := _env_opt_str("LOGIC_EXPERIMENT_INFERENCE_SAMPLES")) is not None:
            low = es.lower()
            if low in ("0", "none", "off", ""):
                kwargs["experiment_inference_sample_n"] = 0
            else:
                kwargs["experiment_inference_sample_n"] = int(es.strip())

        if _env_key_set("LOGIC_RUN_TRAIN"):
            kwargs["run_train"] = _env_bool("LOGIC_RUN_TRAIN", default=True)
        if _env_key_set("LOGIC_PUSH_TO_HUB"):
            kwargs["push_to_hub"] = _env_bool("LOGIC_PUSH_TO_HUB", default=False)
        if _env_key_set("LOGIC_HF_PRIVATE"):
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
        merged = {**yaml_defaults, **filtered, **overrides}
        merged = {k: v for k, v in merged.items() if k in valid}
        return cls(**merged)
