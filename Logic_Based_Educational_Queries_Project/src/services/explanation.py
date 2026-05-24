from __future__ import annotations

from data.prompts import (
    SYSTEM_PROMPT_EXPLAIN_FROM_SOLVER,
    USER_TEMPLATE_EXPLAIN_FROM_SOLVER,
    format_nl_block_numbered,
)
from services.solvers.base import SolverResult


def build_explain_from_solver_messages(
    premises_nl: list[str],
    question: str,
    solver: SolverResult,
    gold_answer: str = "",
) -> list[dict[str, str]]:
    """Tin nhắn để LLM sinh explanation từ output solver (bước 3 pipeline)."""
    nl_block = format_nl_block_numbered(premises_nl)
    solver_summary = f"status={solver.status}\n{solver.summary}"
    if solver.raw:
        solver_summary += f"\nraw:\n{solver.raw}"
    return [
        {"role": "system", "content": SYSTEM_PROMPT_EXPLAIN_FROM_SOLVER.strip()},
        {
            "role": "user",
            "content": USER_TEMPLATE_EXPLAIN_FROM_SOLVER.format(
                nl_block=nl_block,
                question=question,
                solver_summary=solver_summary,
                gold_answer=gold_answer or "(not provided)",
            ),
        },
    ]
