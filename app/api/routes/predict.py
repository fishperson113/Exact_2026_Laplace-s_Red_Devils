"""BTC 2026 competition endpoint — POST /predict (Submission Guide §2-4).

ONE endpoint, both task types, routed by the ``type`` field:

    type == "type1" -> logic pipeline  (FOL + QA)   -> answer + premises_used
    type == "type2" -> physics pipeline (ensemble)  -> answer + unit

Returns a JSON **list** with one result object per query (one query per request,
so a single-element list). Never raises to the grader: any failure becomes a
schema-valid empty-answer result (a 500 during the slot = lost points).
"""

from __future__ import annotations

import re
import time
import traceback

from fastapi import APIRouter

from app.api.schemas import PredictRequest
from app.core.config import settings
from app.core.model_swap import ensure_awake
from app.core.pipeline import solve_physics
from app.core.pipeline_logic import run_logic_pipeline
from app.physics_solution.shared.eval.normalizer import normalize_answer, normalize_unit

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
            res = await run_logic_pipeline(
                request.premises, request.query, request.options, deadline
            )
            return [_shape_type1(qid, res, request.premises, request.options, request.query)]
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


_LABEL_RE = re.compile(r"^\s*(?:option\s*)?([A-Za-z])\s*[.):]?\s*$", re.I)


def _coerce_to_option(answer: str, options: list[str], query: str = "") -> str:
    """Type-1 choice answer MUST be exactly one of the options. Best-effort match.

    Handles the common case where options are bare letter labels (["A","B","C","D"]) while
    the full statements live in the query: the QA model copies the chosen statement verbatim,
    so we map that text back to its letter via the "X. <statement>" lines in the query. Plain
    substring containment is restricted to options >=3 chars, so a single-letter option like
    "A" can't false-match the letter 'a' inside any English answer (that bug returned "A" for
    a correct statement-answer)."""
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
    # "Option B" / "B." / "B)" / bare "B" -> the matching letter option
    m = _LABEL_RE.match(a)
    if m:
        for o in options:
            if o.strip().lower() == m.group(1).lower():
                return o

    def _pick_letter(letter: str) -> str | None:
        for o in options:
            if o.strip().lower() == letter.lower():
                return o
        return None

    # letter-label options + a statement answer -> map via the query's "A. <stmt>" lines
    if query and all(re.fullmatch(r"[A-Za-z]", o.strip() or " ") for o in options):
        ar = al.rstrip(". ")
        labeled = [
            (L, s.strip().lower().rstrip(". "))
            for L, s in re.findall(r"(?mi)^\s*([A-Za-z])[.)]\s+(.+?)\s*$", query)
        ]
        for L, sl in labeled:                           # 1) exact statement match wins
            if sl and sl == ar and _pick_letter(L):
                return _pick_letter(L)
        best, best_len = None, 10**9                     # 2) else SHORTEST containing stmt
        for L, sl in labeled:                            #    (avoids "...false that <B>" wrapper)
            if sl and (sl in al or ar in sl) and len(sl) < best_len:
                best, best_len = L, len(sl)
        if best and _pick_letter(best):
            return _pick_letter(best)
    # word-boundary containment for multi-char options (Yes/No/Uncertain/full statements);
    # single-letter options are excluded here so 'a' can't match inside any English text.
    for o in options:
        ol = o.lower().strip()
        if len(ol) >= 2 and re.search(r"\b" + re.escape(ol) + r"\b", al):
            return o
    return options[0]                                   # last resort: never empty


def _shape_type1(qid: str, res: dict, premises: list[str], options: list[str], query: str = "") -> dict:
    answer = _coerce_to_option(res.get("answer", ""), options, query)
    # reasoning.steps: the QA model emits Rule:/Fact:/Derive:/Conclusion: lines; use
    # them verbatim, falling back to the FOL block or explanation if it emitted none.
    steps = (
        res.get("reasoning_steps")
        or _steps_from_text(res.get("fol", "") or "")
        or _steps_from_text(res.get("cot", ""))
    )
    # premises_used: the QA model is trained to emit the 0-based indices it cited.
    # Use those; fall back to "all premises" only when the model returned none (better
    # than empty for the 50%-weighted premises_used score when premises are load-bearing).
    premises_used = res.get("premises_used") or (
        list(range(len(premises))) if premises else []
    )
    # reasoning.fol: the FINAL FOL list (post-neutralize) the QA model reasoned over,
    # surfaced alongside type/steps for Stage-1 debugging (BTC ignores extra keys).
    fol_list = res.get("fol_list") or []
    reasoning = None
    if steps:
        reasoning = {"type": "fol", "steps": steps}
        if fol_list:
            reasoning["fol"] = fol_list
    return {
        "query_id": qid,
        "answer": answer,
        "unit": "",
        "explanation": res.get("explanation") or "No explanation produced.",
        "premises_used": premises_used,
        "reasoning": reasoning,
    }


def _shape_type2(qid: str, res: dict) -> dict:
    steps = res.get("reasoning_steps") or _steps_from_text(res.get("cot", ""))
    # Canonicalize to the convention declared in submission/notation_mapping.csv:
    # value -> plain decimal / e-notation, unit -> ASCII (ohm, uF, deg), no-unit -> "N/A".
    return {
        "query_id": qid,
        "answer": normalize_answer(res.get("answer", "") or ""),
        "unit": normalize_unit(res.get("unit", "") or ""),
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
