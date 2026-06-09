"""BTC 2026 competition endpoint — POST /predict (Submission Guide §2-4).

ONE endpoint, both task types, routed by the ``type`` field:

    type == "type1" -> logic pipeline  (FOL + QA)   -> answer + premises_used
    type == "type2" -> physics pipeline (ensemble)  -> answer + unit

Returns a JSON **list** with one result object per query (one query per request,
so a single-element list). Never raises to the grader: any failure becomes a
schema-valid empty-answer result (a 500 during the slot = lost points).
"""

from __future__ import annotations

import time
import traceback

from fastapi import APIRouter

from app.api.schemas import PredictRequest
from app.core.config import settings
from app.core.model_swap import ensure_awake
from app.core.pipeline import solve_physics
from app.core.pipeline_logic import run_logic_pipeline

router = APIRouter()


@router.post("/predict")
async def predict(request: PredictRequest) -> list[dict]:
    t0 = time.time()
    deadline = t0 + settings.question_timeout_s - 2.0
    qid = request.query_id
    # Route by `type`; fall back to premises-presence if type is missing/odd.
    is_logic = request.type == "type1" or (request.type != "type2" and bool(request.premises))
    try:
        if is_logic:
            await ensure_awake("logic")            # no-op unless sleep-swap on
            res = await run_logic_pipeline(request.premises, request.query, deadline)
            return [_shape_type1(qid, res, request.premises, request.options)]
        await ensure_awake("physics")
        res = await solve_physics(request.query, deadline)
        return [_shape_type2(qid, res)]
    except Exception as exc:  # noqa: BLE001 — never 500 the grader
        traceback.print_exc()
        return [_error(qid, is_logic, exc)]


# --------------------------------------------------------------------------- #
#  Output shaping to the unified result schema                                #
# --------------------------------------------------------------------------- #
def _steps_from_text(text: str, limit: int = 12) -> list[str]:
    """Split a CoT/explanation blob into short reasoning steps."""
    if not text:
        return []
    lines = [ln.strip(" -*\t") for ln in text.replace("\r", "").split("\n")]
    steps = [ln for ln in lines if ln]
    return steps[:limit]


def _coerce_to_option(answer: str, options: list[str]) -> str:
    """Type-1 choice answer MUST be exactly one of the options. Best-effort match."""
    if not options:
        return answer
    a = (answer or "").strip()
    for o in options:                                   # exact
        if a == o:
            return o
    al = a.lower()
    for o in options:                                   # case-insensitive
        if al == o.lower():
            return o
    for o in options:                                   # containment either way
        ol = o.lower()
        if ol and (ol in al or al in ol):
            return o
    return options[0]                                   # last resort: never empty


def _shape_type1(qid: str, res: dict, premises: list[str], options: list[str]) -> dict:
    answer = _coerce_to_option(res.get("answer", ""), options)
    fol = res.get("fol", "") or ""
    steps = _steps_from_text(fol) or _steps_from_text(res.get("cot", ""))
    # premises_used: no symbolic solver tracks this yet -> heuristic = all premises.
    # (Better than empty for P2 when most premises are load-bearing; flagged for a
    # real used-premise tracker.)
    premises_used = list(range(len(premises))) if premises else []
    return {
        "query_id": qid,
        "answer": answer,
        "unit": "",
        "explanation": res.get("explanation") or "No explanation produced.",
        "premises_used": premises_used,
        "reasoning": {"type": "fol", "steps": steps} if steps else None,
    }


def _shape_type2(qid: str, res: dict) -> dict:
    steps = res.get("reasoning_steps") or _steps_from_text(res.get("cot", ""))
    return {
        "query_id": qid,
        "answer": res.get("answer", "") or "",
        "unit": res.get("unit", "") or "",
        "explanation": res.get("explanation") or "No explanation produced.",
        "premises_used": [],
        "reasoning": {"type": "cot", "steps": steps} if steps else None,
    }


def _error(qid: str, is_logic: bool, exc: Exception) -> dict:
    return {
        "query_id": qid,
        "answer": "",
        "unit": "",
        "explanation": f"pipeline error: {type(exc).__name__}: {exc}",
        "premises_used": [],
        "reasoning": None,
    }
