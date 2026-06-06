"""Single competition endpoint. BTC may only hit one URL, so POST /ask
handles BOTH task types and routes internally by request shape:

    premises-NL present  -> Task Type 1 (logic, FOL+QA pipeline)
    question only        -> Task Type 2 (physics, code-exec pipeline)

Response shape differs per type (physics returns unit; logic returns fol),
so response_model is left open and a plain dict is returned.

The handler NEVER raises to the client: any pipeline/backend failure is caught
and returned as a schema-valid, empty-answer result so the grader always gets
parseable JSON (a 500 during scoring = lost points).
"""

import time
import traceback

from fastapi import APIRouter

from app.api.schemas import UnifiedAskRequest
from app.core.config import settings
from app.core.pipeline import solve_physics
from app.core.pipeline_logic import run_logic_pipeline

router = APIRouter()


@router.post("/ask")
async def ask(request: UnifiedAskRequest) -> dict:
    t0 = time.time()
    # Reserve 2s safety margin so the server can always return a response
    deadline = t0 + settings.question_timeout_s - 2.0

    # Route by presence of premises: non-empty -> Type 1 (logic), else Type 2.
    is_logic = bool(request.premises_nl)
    try:
        if is_logic:
            return await run_logic_pipeline(
                request.premises_nl, request.question, deadline
            )
        return await solve_physics(request.question, deadline)
    except Exception as exc:  # noqa: BLE001 — never 500 the grader
        traceback.print_exc()
        return _error_result(is_logic, exc, time.time() - t0)


def _error_result(is_logic: bool, exc: Exception, elapsed: float) -> dict:
    explanation = f"pipeline error: {type(exc).__name__}: {exc}"
    if is_logic:
        return {
            "answer": "",
            "explanation": explanation,
            "fol": "",
            "cot": "",
            "confidence": 0.0,
            "solve_method": "failed",
            "elapsed_s": elapsed,
            "domain": "logic",
        }
    return {
        "answer": "",
        "unit": "",
        "explanation": explanation,
        "cot": "",
        "confidence": 0.0,
        "solve_method": "failed",
        "elapsed_s": elapsed,
        "domain": "physics",
    }
