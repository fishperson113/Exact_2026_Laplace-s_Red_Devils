"""Cấu hình SFT NL → premises-FOL — biến môi trường prefix `FOL_`."""
from __future__ import annotations

import os
from dataclasses import dataclass, field, fields
from pathlib import Path
from typing import Any

from services.config import (
    _env_bool,
    _env_int,
    _env_opt_str,
    _path_from_env,
    load_dotenv_for_logic,
)
from services.hf_repo_naming import build_fol_hf_repo_id


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
        if load_dotenv_file:
            load_dotenv_for_logic()

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

        kwargs["load_in_8bit"] = _env_bool("FOL_LOAD_IN_8BIT", default=False)
        if _env_bool("FOL_LOAD_IN_4BIT", default=False):
            kwargs["load_in_8bit"] = True

        if v := _env_int("FOL_NUM_TRAIN_EPOCHS"):
            kwargs["num_train_epochs"] = v
        if v := _env_int("FOL_TRAIN_SEED"):
            kwargs["train_seed"] = v

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

        kwargs["run_train"] = _env_bool("FOL_RUN_TRAIN", default=True)
        kwargs["push_to_hub"] = _env_bool("FOL_PUSH_TO_HUB", default=False)
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

        kwargs["use_unsloth"] = _env_bool("FOL_USE_UNSLOTH", default=False)
        kwargs["unsloth_train_on_responses_only"] = _env_bool(
            "FOL_UNSLOTH_RESPONSES_ONLY", default=True
        )
        kwargs["use_adamw_8bit"] = _env_bool("FOL_USE_ADAMW_8BIT", default=True)
        if (v := _env_opt_str("FOL_UNSLOTH_INSTRUCTION_MARKER")) is not None:
            kwargs["unsloth_instruction_marker"] = v
        if (v := _env_opt_str("FOL_UNSLOTH_RESPONSE_MARKER")) is not None:
            kwargs["unsloth_response_marker"] = v

        kwargs["unsloth_load_in_4bit"] = _env_bool("FOL_UNSLOTH_NF4", default=False)
        if v := _env_int("FOL_EVAL_ACCUMULATION_STEPS"):
            kwargs["eval_accumulation_steps"] = v

        valid = {f.name for f in fields(cls)}
        filtered = {k: v for k, v in kwargs.items() if k in valid}
        merged = {**filtered, **overrides}
        if merged.pop("load_in_4bit", None):
            merged["load_in_8bit"] = True
        merged = {k: v for k, v in merged.items() if k in valid}
        return cls(**merged)
