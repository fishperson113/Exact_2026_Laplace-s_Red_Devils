"""Async vLLM client for Route-1 self-gen (Phase 2).

Talks to the local vLLM OpenAI-compatible endpoint (Vast AI template, internal
port 18000). Mirrors `app/model/llm_client.py` but adds what self-gen needs:

  - `n`-sampling: multiple completions per request -> cheap on-policy augmentation,
  - env-driven base_url / model so the same code runs on any Vast box,
  - a per-request timeout (self-gen issues thousands of calls; never hang forever).

`enable_thinking=False` (Qwen3.5): we want code, not <think> walls -- the same
discipline that won v05 (short prompts, no LaTeX reasoning bloat).

This module runs ON THE GPU BOX (Vast AI), where the model is served. The DeepSeek
teacher uses the separate `ds_client.py`; the execution gate (`pot_common.verify`)
needs no GPU and runs anywhere.
"""

from __future__ import annotations

import os

_DEFAULT_BASE_URL = "http://localhost:18000/v1"
_DEFAULT_MODEL = "Qwen/Qwen3.5-4B"

# Qwen3.5 thinking mode OFF -- code, not reasoning walls (see config.py note).
_THINKING_OFF = {"chat_template_kwargs": {"enable_thinking": False}}


def default_base_url() -> str:
    """vLLM endpoint; override with VLLM_BASE_URL (template serves :18000)."""
    return os.environ.get("VLLM_BASE_URL", _DEFAULT_BASE_URL)


def default_model() -> str:
    """Served model id; override with VLLM_MODEL (template may rename it)."""
    return os.environ.get("VLLM_MODEL", _DEFAULT_MODEL)


def make_client(base_url: str | None = None, api_key: str = "dummy"):
    """Build an AsyncOpenAI client pointed at the vLLM endpoint (key is ignored by vLLM).

    Calls are traced at a higher, readable level by `pot_common.trace_sample` (per
    question/temperature/sample), not by wrapping the raw OpenAI client.
    """
    from openai import AsyncOpenAI  # lazy: keeps the offline core import-light

    return AsyncOpenAI(base_url=base_url or default_base_url(), api_key=api_key)


async def sample(
    client,
    messages: list[dict],
    *,
    model: str | None = None,
    temperature: float = 0.2,
    n: int = 1,
    max_tokens: int = 2000,
    timeout: float = 120.0,
) -> list[str]:
    """One chat request returning `n` sampled completions (text only).

    Raises on API/transport error -- callers decide whether to treat a failed
    request as "no samples this temp" (self-gen does) and move on.
    """
    resp = await client.chat.completions.create(
        model=model or default_model(),
        messages=messages,
        temperature=temperature,
        n=n,
        max_tokens=max_tokens,
        timeout=timeout,
        extra_body=_THINKING_OFF,
    )
    return [c.message.content or "" for c in resp.choices]


async def is_alive(client) -> bool:
    """True if the endpoint answers a models.list() -- a cheap pre-flight check."""
    try:
        await client.models.list()
        return True
    except Exception:
        return False
