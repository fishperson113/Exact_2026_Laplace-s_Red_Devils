"""Chuẩn hoá special tokens cho Qwen / TRL khi metadata bị placeholder (vd ``<EOS_TOKEN>``).

Qwen3-VL (4B) load qua Unsloth/HF trả về ``Qwen3VLProcessor`` — một wrapper đa phương thức
bọc tokenizer thật ở ``processor.tokenizer``. Các method vocab (``convert_ids_to_tokens``,
``convert_tokens_to_ids``, ``get_vocab``) chỉ tồn tại trên tokenizer bên trong, không có trên
processor. Module này luôn unwrap về tokenizer thật trước khi thao tác, và đồng bộ ngược chuỗi
special token lên processor để code downstream đọc ``processor.eos_token`` / ``.pad_token`` nhất quán.
"""
from __future__ import annotations

from typing import Any

# Chuỗi placeholder hay gặp trong tokenizer_config lỗi — không phải token thật trong vocab.
BAD_PLACEHOLDER_TOKENS: frozenset[str] = frozenset(
    {
        "<EOS_TOKEN>",
        "<PAD_TOKEN>",
        "<BOS_TOKEN>",
        "<UNK_TOKEN>",
        "<MASK>",
    }
)


def inner_tokenizer(obj: Any) -> Any:
    """Tokenizer thật bên trong. Processor đa phương thức (Qwen3-VL) bọc nó ở ``.tokenizer``."""
    tok = getattr(obj, "tokenizer", None)
    if tok is not None and hasattr(tok, "convert_ids_to_tokens"):
        return tok
    return obj


def _set_special(processor: Any, tok: Any, attr: str, value: Any) -> None:
    """Gán special token lên tokenizer thật và mirror lên processor (nếu khác) để downstream đọc nhất quán."""
    setattr(tok, attr, value)
    if processor is not tok:
        try:
            setattr(processor, attr, value)
        except Exception:
            pass


def sync_eos_token_string_with_id(tokenizer: Any) -> None:
    """Gán ``eos_token`` (và ``eos_token_id`` nếu thiếu) khớp vocab — tránh placeholder không tồn tại."""
    tok = inner_tokenizer(tokenizer)
    cur = getattr(tok, "eos_token", None)
    eid = getattr(tok, "eos_token_id", None)

    if eid is None and cur and cur not in BAD_PLACEHOLDER_TOKENS:
        try:
            tid = int(tok.convert_tokens_to_ids(cur))
            unk = int(tok.unk_token_id) if tok.unk_token_id is not None else -1
            if tid >= 0 and tid != unk:
                _set_special(tokenizer, tok, "eos_token_id", tid)
                eid = tid
        except (TypeError, ValueError, KeyError, AttributeError):
            pass

    if eid is not None:
        if cur not in BAD_PLACEHOLDER_TOKENS and cur is not None:
            try:
                if int(tok.convert_tokens_to_ids(cur)) == int(eid):
                    return
            except (TypeError, ValueError, KeyError, AttributeError):
                pass
        tok_str = tok.convert_ids_to_tokens(int(eid))
        if isinstance(tok_str, list):
            tok_str = tok_str[0] if tok_str else None
        if tok_str:
            _set_special(tokenizer, tok, "eos_token", tok_str)
        return

    vocab = tok.get_vocab()
    # Qwen2 / Qwen2.5 / Qwen3 Instruct dùng <|im_end|>; thêm các biến thể hay gặp.
    for candidate in (
        "<|im_end|>",
        "<|endoftext|>",
        "</s>",
        "<|end|>",
    ):
        if candidate in vocab:
            _set_special(tokenizer, tok, "eos_token", candidate)
            if getattr(tok, "eos_token_id", None) is None:
                _set_special(tokenizer, tok, "eos_token_id", int(tok.convert_tokens_to_ids(candidate)))
            return


def _token_str_resolves_in_vocab(tokenizer: Any, tok_str: str | None) -> bool:
    """True nếu chuỗi là token thật trong vocab (không None, không trùng unk)."""
    if tok_str is None:
        return True
    tok = inner_tokenizer(tokenizer)
    try:
        tid = tok.convert_tokens_to_ids(tok_str)
    except Exception:
        return False
    if tid is None:
        return False
    unk = getattr(tok, "unk_token_id", None)
    if unk is not None and int(tid) == int(unk):
        return False
    return True


def scrub_sft_config_eos_pad_args(sft_args: Any, tokenizer: Any) -> None:
    """Gỡ ``eos_token`` / ``pad_token`` placeholder trên ``SFTConfig``; đồng bộ tokenizer trước ``SFTTrainer``."""
    sync_eos_token_string_with_id(tokenizer)
    tok = inner_tokenizer(tokenizer)
    pt = getattr(tok, "pad_token", None)
    if pt in BAD_PLACEHOLDER_TOKENS or pt is None or not _token_str_resolves_in_vocab(tokenizer, pt):
        _set_special(tokenizer, tok, "pad_token", tok.eos_token)

    for attr in ("eos_token", "pad_token"):
        val = getattr(sft_args, attr, None)
        if val in BAD_PLACEHOLDER_TOKENS or not _token_str_resolves_in_vocab(tokenizer, val):
            setattr(sft_args, attr, None)
            continue
        if val is None:
            continue
        try:
            tid = tok.convert_tokens_to_ids(val)
        except Exception:
            setattr(sft_args, attr, None)
            continue
        unk = getattr(tok, "unk_token_id", None)
        if unk is not None and tid == unk:
            setattr(sft_args, attr, None)
