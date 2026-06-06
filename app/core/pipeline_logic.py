"""Logic track (Task Type 1) pipeline over vLLM.

Same two-stage flow as ``logic_solution/pipeline/ensemble.py`` (NL -> FOL,
then NL+FOL+Q -> answer), but the two models are served by vLLM over HTTP
instead of loaded in-process. Prompts and parsers are reused verbatim.

Public API
----------
    async def run_logic_pipeline(premises_nl, question, deadline) -> dict
"""

from __future__ import annotations

import time

from app.core.config import settings
from app.logic_solution.parsing import parse_fol, parse_qa_output
from app.logic_solution.prompts import (
    SYSTEM_PROMPT_FOL,
    USER_TEMPLATE_FOL,
    SYSTEM_PROMPT_QA,
    USER_TEMPLATE_QA,
    format_nl_block,
    format_fol_block,
)
from app.logic_solution.utils.postprocess import clean_explanation
from app.model.llm_client import fol_llm, qa_llm


async def run_logic_pipeline(
    premises_nl: list[str], question: str, deadline: float
) -> dict:
    """Solve a Type-1 logic question. Returns BTC fields (answer/explanation/fol)
    plus P3 fields (cot/confidence) and timing."""
    t_start = time.time()

    # ---- Stage 1: NL premises -> FOL ----
    fol_user = USER_TEMPLATE_FOL.format(premises_nl=format_nl_block(premises_nl))
    fol_raw = await fol_llm.chat(
        [
            {"role": "system", "content": SYSTEM_PROMPT_FOL},
            {"role": "user", "content": fol_user},
        ],
        temperature=0.0,
        max_tokens=settings.fol_max_tokens,
    )
    fol_list = parse_fol(fol_raw)

    if time.time() >= deadline:
        return _timeout_result(t_start, fol_list)

    # ---- Stage 2: NL + FOL + question -> answer + explanation ----
    qa_user = USER_TEMPLATE_QA.format(
        premises_nl_block=format_nl_block(premises_nl),
        premises_fol_block=format_fol_block(fol_list),
        question=question,
    )
    qa_raw = await qa_llm.chat(
        [
            {"role": "system", "content": SYSTEM_PROMPT_QA},
            {"role": "user", "content": qa_user},
        ],
        temperature=0.0,
        max_tokens=settings.qa_max_tokens,
    )
    qa_out = parse_qa_output(qa_raw)
    explanation = clean_explanation(qa_out["explanation"])
    answer = qa_out["answer"]

    return {
        "answer": answer,
        "explanation": explanation,
        "fol": "\n".join(fol_list),
        "cot": explanation,
        "confidence": 0.9 if answer and answer != "Unknown" else 0.3,
        "solve_method": "fol_qa",
        "elapsed_s": time.time() - t_start,
        "domain": "logic",
    }


def _timeout_result(t_start: float, fol_list: list[str]) -> dict:
    return {
        "answer": "",
        "explanation": "Request timed out before a result could be computed.",
        "fol": "\n".join(fol_list),
        "cot": "",
        "confidence": 0.0,
        "solve_method": "timeout",
        "elapsed_s": time.time() - t_start,
        "domain": "logic",
    }
