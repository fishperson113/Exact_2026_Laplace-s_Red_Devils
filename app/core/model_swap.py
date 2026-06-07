"""Sleep-mode swap manager (SERVE_MODE=triple).

When the 3 distinct Qwen3.5-4B models can't co-reside on one 24GB GPU, each vLLM
server runs with ``--enable-sleep-mode`` (+ ``VLLM_SERVER_DEV_MODE=1``). Before
routing a request, the gateway calls :func:`ensure_awake` to wake the server(s)
that task needs and sleep the rest, so only one "active group" holds VRAM:

    logic   -> {fol, qa}   (both awake together for the FOL then QA stages)
    physics -> {physics}

A swap happens only when the task TYPE changes (a few seconds: sleep the old
group's GPU memory, then wake the new group). At competition concurrency 1 this
is safe; an ``asyncio.Lock`` serialises swaps if requests overlap.

No-op when ``settings.sleep_swap_enabled`` is False (shared mode: one server
serves all roles, so there is nothing to swap).
"""
from __future__ import annotations

import asyncio

from app.core.config import settings
from app.model.llm_client import fol_llm, physics_llm, qa_llm

_GROUPS: dict[str, list] = {
    "logic": [fol_llm, qa_llm],
    "physics": [physics_llm],
}
_lock = asyncio.Lock()
_current: str | None = None  # which group is currently awake


async def ensure_awake(group: str) -> None:
    """Make ``group`` the active (awake) group; sleep the others. No-op in shared mode."""
    global _current
    if not settings.sleep_swap_enabled or group == _current:
        return
    async with _lock:
        if group == _current:  # re-check after acquiring the lock
            return
        target = _GROUPS[group]
        target_roots = {c.server_root for c in target}
        others = [
            c
            for name, clients in _GROUPS.items()
            if name != group
            for c in clients
            if c.server_root not in target_roots
        ]
        # Sleep the others FIRST (free their VRAM), THEN wake the target — else
        # the new group's weights won't fit alongside the old group's.
        for c in others:
            try:
                await c.sleep(level=1)
            except Exception:  # noqa: BLE001 — best-effort; pipeline call will surface real errors
                pass
        for c in target:
            try:
                await c.wake_up()
            except Exception:  # noqa: BLE001
                pass
        _current = group
