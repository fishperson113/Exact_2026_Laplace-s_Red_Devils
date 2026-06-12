"""Logic track (Task Type 1) pipeline over vLLM.

Same two-stage flow as ``app/logic_solution/pipeline/ensemble.py`` (NL -> FOL,
then NL + FOL + options + Q -> answer), but the two models are served by vLLM
over HTTP instead of loaded in-process. Prompts and parsers are reused VERBATIM
from ``app/logic_solution`` (the authoritative logic config) so the served
behaviour matches the in-process eval that produced the validated scores.

Stage 1 (FOL): SYSTEM_PROMPT_FOL + 1-indexed NL premises -> {"premises_fol": [...]}.
  Greedy, repetition_penalty=1.2 (mirrors fol_model.py — the FOL model loops without it).
Stage 2 (QA): SYSTEM_PROMPT_QA + 0-indexed NL + 0-indexed FOL + options + Q
  -> reasoning steps (Rule:/Fact:/Derive:/Conclusion:) then a final JSON
  {"premises_used", "explanation", "answer"}. The QA model EMITS premises_used and
  the reasoning steps itself; we parse and surface them (no separate solver).

Public API
----------
    async def run_logic_pipeline(premises_nl, question, options, deadline) -> dict
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
    format_nl_block,        # FOL stage (1-indexed)
    format_premises_nl,     # QA stage (0-indexed)
    format_premises_fol,    # QA stage (0-indexed)
    format_options,         # QA stage (A./B./... or free-form notice)
)
from app.logic_solution.utils.postprocess import clean_explanation
from app.model.llm_client import fol_llm, qa_llm

# FOL model loops without a repetition penalty (mirrors fol_model.py generate()).
_FOL_REPETITION_PENALTY = 1.2


async def run_logic_pipeline(
    premises_nl: list[str],
    question: str,
    options: list[str] | None,
    deadline: float,
) -> dict:
    """Solve a Type-1 logic question. Returns BTC fields (answer/explanation/fol/
    premises_used/reasoning_steps) plus P3 fields (cot/confidence) and timing."""
    t_start = time.time()
    options = options or []

    # ---- Stage 1: NL premises -> FOL (1-indexed NL, greedy, rep-penalty) ----
    fol_user = USER_TEMPLATE_FOL.format(premises_nl=format_nl_block(premises_nl))
    fol_raw = await fol_llm.chat(
        [
            {"role": "system", "content": SYSTEM_PROMPT_FOL},
            {"role": "user", "content": fol_user},
        ],
        temperature=0.0,
        max_tokens=settings.fol_max_tokens,
        repetition_penalty=_FOL_REPETITION_PENALTY,
    )
    fol_list = parse_fol(fol_raw)

    if time.time() >= deadline:
        return _timeout_result(t_start, fol_list)

    # ---- Stage 2: NL + FOL + options + question -> answer + explanation ----
    # premises/FOL are 0-indexed here to match the model's 0-based premises_used.
    qa_user = USER_TEMPLATE_QA.format(
        premises_nl_block=format_premises_nl(premises_nl),
        premises_fol_block=format_premises_fol(fol_list),
        options_block=format_options(options),
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
    premises_used = qa_out["premises_used"]
    reasoning_steps = qa_out["reasoning_steps"]

    return {
        "answer": answer,
        "explanation": explanation,
        "fol": "\n".join(fol_list),
        "premises_used": premises_used,
        "reasoning_steps": reasoning_steps,
        "cot": "\n".join(reasoning_steps) if reasoning_steps else explanation,
        "confidence": 0.9 if answer and answer not in ("Unknown", "Uncertain", "") else 0.3,
        "solve_method": "fol_qa",
        "elapsed_s": time.time() - t_start,
        "domain": "logic",
    }


def _timeout_result(t_start: float, fol_list: list[str]) -> dict:
    return {
        "answer": "",
        "explanation": "Request timed out before a result could be computed.",
        "fol": "\n".join(fol_list),
        "premises_used": [],
        "reasoning_steps": [],
        "cot": "",
        "confidence": 0.0,
        "solve_method": "timeout",
        "elapsed_s": time.time() - t_start,
        "domain": "logic",
    }
