"""Unsloth + chỉ tính loss trên phần assistant + AdamW 8-bit — giảm VRAM (T4) cho FOL SFT."""
from __future__ import annotations

import inspect
import logging
from typing import TYPE_CHECKING, Any

import torch

if TYPE_CHECKING:
    from services.config_fol import FolSFTConfig

_LOG = logging.getLogger(__name__)

# Lần thử ``import unsloth`` gần nhất thất bại (để thông báo RuntimeError rõ ràng hơn).
_last_unsloth_import_error: str | None = None


def unsloth_import_error_detail() -> str | None:
    """Thông điệp lỗi từ lần import ``unsloth`` thất bại gần nhất, hoặc None nếu chưa thử / đã OK."""
    return _last_unsloth_import_error


def is_unsloth_available() -> bool:
    global _last_unsloth_import_error
    try:
        import unsloth  # noqa: F401

        _last_unsloth_import_error = None
        return True
    except Exception as e:
        _last_unsloth_import_error = f"{type(e).__name__}: {e}"
        _LOG.warning("import unsloth thất bại: %s", _last_unsloth_import_error)
        return False


def load_unsloth_model_and_tokenizer(cfg: "FolSFTConfig") -> tuple[Any, Any, bool, bool]:
    """Nạp Qwen qua ``FastLanguageModel`` + LoRA Unsloth; trả về ``(model, tokenizer, bf16, fp16)`` cho ``SFTConfig``."""
    if not is_unsloth_available():
        detail = unsloth_import_error_detail() or "không rõ"
        raise ImportError(
            "Không import được gói `unsloth`. Chi tiết: "
            + detail
            + " — xem https://github.com/unslothai/unsloth (torch/CUDA đúng bản; Jupyter: cài bằng `%pip install` "
            "hoặc `python -m pip` trùng `sys.executable`)."
        )
    # Tắt flex_attention detection trong transformers — tránh ValueError "too many values to unpack"
    # khi transformers 5.x + PyTorch 2.x auto-chọn FlexFlashAttention thay vì SDPA.
    for _mod_name in ("transformers.modeling_utils", "transformers.utils", "transformers"):
        try:
            import importlib
            _mod = importlib.import_module(_mod_name)
            if hasattr(_mod, "is_torch_flex_attn_available"):
                setattr(_mod, "is_torch_flex_attn_available", lambda: False)
        except Exception:
            pass

    from unsloth import FastLanguageModel  # type: ignore[import-untyped]

    from services.config_fol import fol_should_load_in_8bit

    from .tokenizer_fix import sync_eos_token_string_with_id

    print(
        "[FOL train][Unsloth] Nạp model + tokenizer (gradient checkpointing kiểu unsloth nếu bật).",
        flush=True,
    )

    load_kw: dict[str, Any] = dict(
        model_name=cfg.model_name,
        max_seq_length=cfg.max_seq_length,
        trust_remote_code=cfg.trust_remote_code,
        attn_implementation="sdpa",
    )
    if cfg.unsloth_load_in_4bit:
        load_kw["load_in_4bit"] = True
        load_kw["load_in_8bit"] = False
        # NF4 và FP16 full weights loại trừ nhau — muốn 16-bit: tắt cfg.unsloth_load_in_4bit / FOL_UNSLOTH_NF4.
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
        err_msg = str(e).lower()
        if "attn_implementation" in err_msg or "unexpected keyword" in err_msg:
            _LOG.warning("Unsloth không nhận attn_implementation — thử lại không có nó.")
            load_kw.pop("attn_implementation", None)
            try:
                model, tokenizer = FastLanguageModel.from_pretrained(**load_kw)
            except TypeError as e2:
                if "load_in_8bit" in str(e2) or "unexpected keyword" in str(e2).lower():
                    _LOG.warning("Unsloth không nhận load_in_8bit — thử lại với load_in_16bit.")
                    load_kw.pop("load_in_8bit", None)
                    load_kw["load_in_16bit"] = True
                    load_kw["load_in_4bit"] = False
                    model, tokenizer = FastLanguageModel.from_pretrained(**load_kw)
                else:
                    raise
        elif "load_in_8bit" in str(e) or "unexpected keyword" in err_msg:
            _LOG.warning("Unsloth không nhận load_in_8bit — thử lại với load_in_16bit.")
            load_kw.pop("load_in_8bit", None)
            load_kw["load_in_16bit"] = True
            load_kw["load_in_4bit"] = False
            model, tokenizer = FastLanguageModel.from_pretrained(**load_kw)
        else:
            raise

    if hasattr(model, "config"):
        model.config._attn_implementation = "sdpa"

    sync_eos_token_string_with_id(tokenizer)
    if tokenizer.pad_token is None or tokenizer.pad_token in (
        "<EOS_TOKEN>",
        "<PAD_TOKEN>",
    ):
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

    # Khớp SFTConfig với dtype thật của weights sau Unsloth (tránh: model bf16 + fp16=True → TypeError).
    p0 = next(model.parameters())
    if p0.dtype == torch.bfloat16:
        train_bf16, train_fp16 = True, False
    elif p0.dtype == torch.float16:
        train_bf16, train_fp16 = False, True
    else:
        train_bf16, train_fp16 = bool(cfg.bf16), not bool(cfg.bf16)
    print(
        f"[FOL train][Unsloth] Trainer mixed precision: bf16={train_bf16}, fp16={train_fp16} "
        f"(dtype tham số: {p0.dtype}).",
        flush=True,
    )
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
