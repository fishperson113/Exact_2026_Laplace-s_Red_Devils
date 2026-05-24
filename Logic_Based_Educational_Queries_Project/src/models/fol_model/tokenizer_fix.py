"""Chuẩn hoá special tokens cho Qwen / TRL khi metadata bị placeholder (vd ``<EOS_TOKEN>``)."""
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


def sync_eos_token_string_with_id(tokenizer: Any) -> None:
    """Gán ``tokenizer.eos_token`` (và ``eos_token_id`` nếu thiếu) khớp vocab — tránh placeholder không tồn tại."""
    cur = getattr(tokenizer, "eos_token", None)
    eid = getattr(tokenizer, "eos_token_id", None)

    if eid is None and cur and cur not in BAD_PLACEHOLDER_TOKENS:
        try:
            tid = int(tokenizer.convert_tokens_to_ids(cur))
            unk = int(tokenizer.unk_token_id) if tokenizer.unk_token_id is not None else -1
            if tid >= 0 and tid != unk:
                tokenizer.eos_token_id = tid
                eid = tid
        except (TypeError, ValueError, KeyError, AttributeError):
            pass

    if eid is not None:
        if cur not in BAD_PLACEHOLDER_TOKENS and cur is not None:
            try:
                if int(tokenizer.convert_tokens_to_ids(cur)) == int(eid):
                    return
            except (TypeError, ValueError, KeyError, AttributeError):
                pass
        tok = tokenizer.convert_ids_to_tokens(int(eid))
        if isinstance(tok, list):
            tok = tok[0] if tok else None
        if tok:
            tokenizer.eos_token = tok
        return

    vocab = tokenizer.get_vocab()
    # Qwen2 / Qwen2.5 Instruct dùng <|im_end|>; thêm các biến thể hay gặp.
    for candidate in (
        "<|im_end|>",
        "<|endoftext|>",
        "</s>",
        "<|end|>",
    ):
        if candidate in vocab:
            tokenizer.eos_token = candidate
            if getattr(tokenizer, "eos_token_id", None) is None:
                tokenizer.eos_token_id = int(tokenizer.convert_tokens_to_ids(candidate))
            return


def _token_str_resolves_in_vocab(tokenizer: Any, tok_str: str | None) -> bool:
    """True nếu chuỗi là token thật trong vocab (không None, không trùng unk)."""
    if tok_str is None:
        return True
    try:
        tid = tokenizer.convert_tokens_to_ids(tok_str)
    except Exception:
        return False
    if tid is None:
        return False
    unk = getattr(tokenizer, "unk_token_id", None)
    if unk is not None and int(tid) == int(unk):
        return False
    return True


def scrub_sft_config_eos_pad_args(sft_args: Any, tokenizer: Any) -> None:
    """Gỡ ``eos_token`` / ``pad_token`` placeholder trên ``SFTConfig``; đồng bộ tokenizer trước ``SFTTrainer``."""
    sync_eos_token_string_with_id(tokenizer)
    pt = getattr(tokenizer, "pad_token", None)
    if pt in BAD_PLACEHOLDER_TOKENS or pt is None or not _token_str_resolves_in_vocab(tokenizer, pt):
        tokenizer.pad_token = tokenizer.eos_token

    for attr in ("eos_token", "pad_token"):
        val = getattr(sft_args, attr, None)
        if val in BAD_PLACEHOLDER_TOKENS or not _token_str_resolves_in_vocab(tokenizer, val):
            setattr(sft_args, attr, None)
            continue
        if val is None:
            continue
        try:
            tid = tokenizer.convert_tokens_to_ids(val)
        except Exception:
            setattr(sft_args, attr, None)
            continue
        unk = getattr(tokenizer, "unk_token_id", None)
        if unk is not None and tid == unk:
            setattr(sft_args, attr, None)
