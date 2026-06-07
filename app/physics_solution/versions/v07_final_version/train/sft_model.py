"""Load Qwen3.5-4B via Unsloth + attach LoRA. Encodes the tf5/torch2.10 gotchas
that the (proven) FOL training run hit on the same base model.

Gotchas baked in:
- import `unsloth` BEFORE `trl` (Unsloth patches TRL/transformers). train.py does
  this; here we import unsloth lazily inside the function for the same reason.
- disable transformers' flex-attention auto-detect — on tf5 + torch2.x it picks
  FlexFlashAttention and raises "too many values to unpack". Force SDPA.
- Qwen3.5 may load as a multimodal processor wrapping the real tokenizer; unwrap
  before touching vocab/special tokens. pad_token := eos_token if missing.
"""

from __future__ import annotations

import importlib
from typing import Any

import torch

# placeholder special-token strings sometimes left in tokenizer_config
_BAD_TOKENS = frozenset({"<EOS_TOKEN>", "<PAD_TOKEN>", "<BOS_TOKEN>", "<UNK_TOKEN>"})


def _inner_tokenizer(obj: Any) -> Any:
    """Real tokenizer inside a (possibly multimodal) processor wrapper."""
    tok = getattr(obj, "tokenizer", None)
    if tok is not None and hasattr(tok, "convert_ids_to_tokens"):
        return tok
    return obj


def _disable_flex_attention() -> None:
    for name in ("transformers.modeling_utils", "transformers.utils", "transformers"):
        try:
            mod = importlib.import_module(name)
            if hasattr(mod, "is_torch_flex_attn_available"):
                mod.is_torch_flex_attn_available = lambda: False  # type: ignore[assignment]
        except Exception:
            pass


def _fix_tokenizer(tokenizer: Any) -> None:
    tok = _inner_tokenizer(tokenizer)
    if tok.eos_token in _BAD_TOKENS or tok.eos_token is None:
        # Qwen instruct uses <|im_end|>; fall back to <|endoftext|>.
        vocab = tok.get_vocab()
        for cand in ("<|im_end|>", "<|endoftext|>"):
            if cand in vocab:
                tok.eos_token = cand
                break
    if tok.pad_token is None or tok.pad_token in _BAD_TOKENS:
        # pad := <|endoftext|> if present (distinct from eos stop token), else eos.
        vocab = tok.get_vocab()
        tok.pad_token = "<|endoftext|>" if "<|endoftext|>" in vocab else tok.eos_token
    tok.padding_side = "right"  # training; eval flips to left


def load_model_and_tokenizer(cfg: dict) -> tuple[Any, Any, bool]:
    """Return (model_with_lora, tokenizer, bf16). Import order matters — see module docstring."""
    _disable_flex_attention()
    from unsloth import FastLanguageModel  # noqa: WPS433  (after flex-disable)

    m = cfg["model"]
    load_kw: dict[str, Any] = dict(
        model_name=m["name"],
        max_seq_length=int(m["max_seq_length"]),
        trust_remote_code=bool(m.get("trust_remote_code", True)),
        attn_implementation=m.get("attn_implementation", "sdpa"),
    )
    if m.get("load_in_4bit", True):
        load_kw.update(load_in_4bit=True, load_in_8bit=False, load_in_16bit=False)
    else:
        load_kw.update(load_in_16bit=True, load_in_4bit=False, load_in_8bit=False)

    try:
        model, tokenizer = FastLanguageModel.from_pretrained(**load_kw)
    except TypeError:
        # older/newer Unsloth signatures: drop attn_implementation and retry.
        load_kw.pop("attn_implementation", None)
        model, tokenizer = FastLanguageModel.from_pretrained(**load_kw)

    if hasattr(model, "config"):
        model.config._attn_implementation = "sdpa"
    _fix_tokenizer(tokenizer)

    lo = cfg["lora"]
    model = FastLanguageModel.get_peft_model(
        model,
        r=int(lo["r"]),
        lora_alpha=int(lo["alpha"]),
        lora_dropout=float(lo.get("dropout", 0.0)),
        target_modules=list(lo["target_modules"]),
        bias=lo.get("bias", "none"),
        use_gradient_checkpointing="unsloth" if cfg["training"].get("gradient_checkpointing", True) else False,
        random_state=int(cfg["training"].get("seed", 42)),
        max_seq_length=int(m["max_seq_length"]),
    )
    model.print_trainable_parameters()

    # match Trainer mixed precision to the real weight dtype after Unsloth.
    bf16 = next(model.parameters()).dtype != torch.float16 and bool(cfg["training"].get("bf16", True))
    return model, tokenizer, bf16
