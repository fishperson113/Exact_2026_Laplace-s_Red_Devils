"""Unsloth + chỉ tính loss trên phần assistant + AdamW 8-bit — giảm VRAM (T4) cho FOL SFT."""
from __future__ import annotations

import inspect
import logging
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from services.config_fol import FolSFTConfig

_LOG = logging.getLogger(__name__)


def is_unsloth_available() -> bool:
    try:
        import unsloth  # noqa: F401

        return True
    except ImportError:
        return False


def load_unsloth_model_and_tokenizer(cfg: "FolSFTConfig") -> tuple[Any, Any, bool, bool]:
    """Nạp Qwen qua ``FastLanguageModel`` + LoRA Unsloth; trả về ``(model, tokenizer, bf16, fp16)`` cho ``SFTConfig``."""
    if not is_unsloth_available():
        raise ImportError(
            "Thiếu gói `unsloth`. Cài: pip install unsloth  "
            "(Kaggle: thường cần torch đúng phiên bản; xem https://github.com/unslothai/unsloth)."
        )
    from unsloth import FastLanguageModel  # type: ignore[import-untyped]

    from services.config_fol import fol_should_load_in_8bit

    print(
        "[FOL train][Unsloth] Nạp model + tokenizer (gradient checkpointing kiểu unsloth nếu bật).",
        flush=True,
    )

    load_kw: dict[str, Any] = dict(
        model_name=cfg.model_name,
        max_seq_length=cfg.max_seq_length,
        trust_remote_code=cfg.trust_remote_code,
    )
    if cfg.unsloth_load_in_4bit:
        load_kw["load_in_4bit"] = True
        load_kw["load_in_8bit"] = False
        load_kw["load_in_16bit"] = False
        print(
            "[FOL train][Unsloth] NF4 4-bit (VRAM thấp; cfg.unsloth_load_in_4bit / FOL_UNSLOTH_NF4).",
            flush=True,
        )
    elif fol_should_load_in_8bit(cfg):
        load_kw["load_in_8bit"] = True
        load_kw["load_in_4bit"] = False
        load_kw["load_in_16bit"] = False
    else:
        load_kw["load_in_16bit"] = True
        load_kw["load_in_4bit"] = False
        load_kw["load_in_8bit"] = False

    try:
        model, tokenizer = FastLanguageModel.from_pretrained(**load_kw)
    except TypeError as e:
        if "load_in_8bit" in str(e) or "unexpected keyword" in str(e).lower():
            _LOG.warning("Unsloth không nhận load_in_8bit — thử lại với load_in_16bit.")
            load_kw.pop("load_in_8bit", None)
            load_kw["load_in_16bit"] = True
            load_kw["load_in_4bit"] = False
            model, tokenizer = FastLanguageModel.from_pretrained(**load_kw)
        else:
            raise

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "left"

    gc_mode: str | bool = "unsloth" if cfg.gradient_checkpointing else False
    model = FastLanguageModel.get_peft_model(
        model,
        r=cfg.lora_r,
        lora_alpha=cfg.lora_alpha,
        lora_dropout=cfg.lora_dropout,
        target_modules=list(cfg.lora_target_modules),
        bias="none",
        use_gradient_checkpointing=gc_mode,
        random_state=cfg.train_seed,
        max_seq_length=cfg.max_seq_length,
    )
    model.print_trainable_parameters()

    # T4: fp16 train ổn định; bf16 trên sm75 không có tensor core bf16
    train_bf16, train_fp16 = False, True
    return model, tokenizer, train_bf16, train_fp16


def apply_train_on_responses_only(trainer: Any, cfg: "FolSFTConfig") -> Any:
    """Bọc ``SFTTrainer`` để chỉ tính loss trên completion (sau marker assistant Qwen)."""
    from unsloth.chat_templates import train_on_responses_only  # type: ignore[import-untyped]

    sig = inspect.signature(train_on_responses_only)
    kw: dict[str, Any] = {
        "instruction_part": cfg.unsloth_instruction_marker,
        "response_part": cfg.unsloth_response_marker,
    }
    if "force_match" in sig.parameters:
        kw["force_match"] = False
    return train_on_responses_only(trainer, **kw)
