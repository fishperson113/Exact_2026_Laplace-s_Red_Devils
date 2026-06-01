"""Reusable async DeepSeek helper for Phase-1 data prep.

Factors out the AsyncOpenAI + semaphore + incremental-save pattern (same shape
as shared/eval/gen_golden.py) so filter / translate / extract stages share it.

Phase-1 stages (filter, vietjack translate+extract) are simple -> use the cheap
`deepseek-v4-flash`. Only Phase-2 code-gen / teacher uses `deepseek-v4-pro`.
Model names are exact; do not "correct" them.

Config comes from app.physics_solution.config (provider, base_url, api key env).
"""

from __future__ import annotations

import asyncio
import os
from typing import Any, Callable, Sequence

from app.physics_solution.config import (
    COMMERCIAL_API_KEY_ENV,
    COMMERCIAL_BASE_URL,
    COMMERCIAL_MODEL_FLASH,
    COMMERCIAL_PROVIDER,
)

# `openai` is imported lazily inside make_client so the offline stages (md parsing,
# BTC reshape, keyword pre-filter) can run without the dependency installed.

# thinking off: these are deterministic formatting/classification tasks
_THINKING_OFF = {"thinking": {"type": "disabled"}}


def make_client(provider: str = COMMERCIAL_PROVIDER):
    """Build an AsyncOpenAI client for the given provider. Raises if key missing."""
    from openai import AsyncOpenAI  # lazy: offline stages don't need this dep

    key_var = COMMERCIAL_API_KEY_ENV.get(provider)
    if not key_var:
        raise ValueError(f"Unknown provider: {provider}")
    api_key = os.environ.get(key_var)
    if not api_key:
        raise RuntimeError(f"Missing env var {key_var} (set it in app/physics_solution/.env).")
    kwargs: dict = {"api_key": api_key}
    base_url = COMMERCIAL_BASE_URL.get(provider)
    if base_url:
        kwargs["base_url"] = base_url
    return AsyncOpenAI(**kwargs)


async def complete(
    client: AsyncOpenAI,
    messages: list[dict],
    *,
    model: str = COMMERCIAL_MODEL_FLASH,
    temperature: float = 0.0,
    thinking_off: bool = True,
) -> str:
    """Single chat completion -> text. Empty string on a returned None content."""
    extra_body = dict(_THINKING_OFF) if thinking_off else {}
    resp = await client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        extra_body=extra_body,
    )
    return resp.choices[0].message.content or ""


async def run_batch(
    items: Sequence[Any],
    build_messages: Callable[[Any], list[dict]],
    parse: Callable[[Any, str], Any | None],
    *,
    model: str = COMMERCIAL_MODEL_FLASH,
    concurrency: int = 10,
    temperature: float = 0.0,
    max_retries: int = 2,
    on_progress: Callable[[list[Any]], None] | None = None,
    save_every: int = 50,
    provider: str = COMMERCIAL_PROVIDER,
) -> list[Any]:
    """Run `build_messages -> complete -> parse` over items with bounded concurrency.

    - `parse(item, text)` returns a record dict (or None to drop on parse failure).
    - Each call retries up to `max_retries` times with exponential backoff on a
      transient API error (rate-limit / network), so we don't lose items.
    - `on_progress(results_so_far)` is called every `save_every` completed items
      (and once at the end), so callers checkpoint to disk incrementally — a crash
      mid-run loses at most `save_every` items, and a re-run can skip done ids.
    Returns the list of non-None parsed records (order not guaranteed).
    """
    client = make_client(provider)
    sem = asyncio.Semaphore(concurrency)
    results: list[Any] = []
    done = 0

    async def _one(item: Any) -> Any | None:
        async with sem:
            last_err: Exception | None = None
            for attempt in range(max_retries + 1):
                try:
                    text = await complete(
                        client, build_messages(item), model=model, temperature=temperature
                    )
                    return parse(item, text)
                except Exception as e:  # network / rate-limit / API error
                    last_err = e
                    if attempt < max_retries:
                        await asyncio.sleep(2 ** attempt)  # 1s, 2s, ...
            return {"__error__": str(last_err), "__item__": item}

    tasks = [asyncio.create_task(_one(it)) for it in items]
    for fut in asyncio.as_completed(tasks):
        rec = await fut
        done += 1
        if rec is not None:
            results.append(rec)
        if on_progress is not None and done % save_every == 0:
            on_progress(results)
            print(f"  [checkpoint] {done}/{len(tasks)} done, {len(results)} records saved")
    if on_progress is not None:
        on_progress(results)
    return results
