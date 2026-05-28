"""Education Logic endpoints (Task Type 1) — placeholder.

Wire up a real pipeline when the logic track is ready. For now returns
a mock response so the API contract is stable and eval tooling can be
built against it.
"""

from __future__ import annotations

import time

from fastapi import APIRouter

from app.api.schemas import LogicAskRequest, LogicQAResponse

router = APIRouter(prefix="/logic", tags=["logic"])


@router.post("/ask", response_model=LogicQAResponse)
async def logic_ask(request: LogicAskRequest) -> LogicQAResponse:
    """Solve an education-logic question.

    TODO: replace mock with real pipeline import, same pattern as physics:
        from app.core.pipeline_logic import run_logic_pipeline
        return await run_logic_pipeline(request)
    """
    t0 = time.time()
    return LogicQAResponse(
        answer="A",
        explanation="[mock] Pipeline not yet implemented for education logic.",
        cot="",
        confidence=0.0,
        solve_method="mock",
        elapsed_s=time.time() - t0,
        domain="logic",
    )


@router.get("/health")
async def logic_health() -> dict:
    """Health check for the logic track — always ok while mocked."""
    return {"status": "ok", "track": "logic", "pipeline": "mock"}
