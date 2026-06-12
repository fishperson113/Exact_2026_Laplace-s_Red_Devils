"""BTC-required ``GET /v1/models`` proxy on the gateway.

The Submission Guide asks the committee to verify the served models via an
OpenAI-compatible ``/v1/models`` endpoint. Our stack runs TWO vLLM engines:
:18000 (base + sft + qa LoRA adapters — physics + logic stage 2) and :18001
(fol — logic stage 1). This route aggregates every engine's ``/v1/models`` into
ONE list so a single public URL (the gateway) exposes both ``POST /predict`` and
``GET /v1/models`` — no second tunnel needed. ``qa_base_url`` resolves to the same
:18000 root as physics, so the set below dedups to the two real engines. A
sleeping engine still answers ``/v1/models`` (process alive, weights offloaded),
so the list is complete regardless of which group is awake.
"""

from __future__ import annotations

import httpx
from fastapi import APIRouter

from app.core.config import settings

router = APIRouter()

# Distinct engine endpoints (dedup by server root; base+sft share :18000).
_ENGINE_URLS = {
    settings.vllm_base_url,   # physics: base + sft
    settings.fol_base_url,    # logic stage 1
    settings.qa_base_url,     # logic stage 2
}


@router.get("/v1/models")
async def list_models() -> dict:
    data: list[dict] = []
    seen: set[str] = set()
    async with httpx.AsyncClient(timeout=5.0) as client:
        for base in _ENGINE_URLS:
            try:
                r = await client.get(f"{base.rstrip('/')}/models")
                for m in r.json().get("data", []):
                    mid = m.get("id")
                    if mid and mid not in seen:
                        seen.add(mid)
                        data.append(m)
            except Exception:  # noqa: BLE001 — skip an unreachable/down engine
                continue
    return {"object": "list", "data": data}
