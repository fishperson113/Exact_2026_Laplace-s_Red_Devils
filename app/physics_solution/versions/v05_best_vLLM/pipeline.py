"""v05_best_vLLM async pipeline: classify → codegen → execute → retry.

Reuses all prompt/formula logic from v05_best. LLM calls go to vLLM via
VLLMClient.chat() — no local model loading, no tokenizer needed.

Public API
----------
    async def solve(question, client, deadline) -> dict
"""

from __future__ import annotations

import time

from app.physics_solution.shared.router import _parse_route
from app.physics_solution.versions.v05_best.code_executor import (
    ExecutionResult,
    extract_code,
)
from app.physics_solution.versions.v05_best.formula_kb import get_formula_hints
from app.physics_solution.versions.v05_best.prompts import (
    CLASSIFY_EXAMPLES,
    CLASSIFY_SYSTEM,
    build_codegen_prompt,
)
from app.physics_solution.versions.v05_best_vLLM.code_executor import execute_code_async


def _build_classify_messages(question: str) -> list[dict]:
    """Build classify chat messages without a tokenizer.

    vLLM applies the chat template server-side, so we pass raw message dicts.
    """
    msgs: list[dict] = [{"role": "system", "content": CLASSIFY_SYSTEM}]
    for ex in CLASSIFY_EXAMPLES:
        msgs.append({"role": "user", "content": ex["q"]})
        msgs.append({"role": "assistant", "content": ex["a"]})
    msgs.append({"role": "user", "content": question})
    return msgs


def _build_explanation(
    question: str,
    code: str | None,
    answer: str,
    unit: str,
    route_domain: str,
    route_answer_type: str,
) -> str:
    """Construct a human-readable explanation from available information."""
    parts: list[str] = []
    parts.append(f"Domain: {route_domain} | Answer type: {route_answer_type}")
    if code:
        # Extract comment lines from generated code as reasoning steps
        steps = [
            line.lstrip("# ").strip()
            for line in code.splitlines()
            if line.strip().startswith("#") and line.strip() != "#"
        ]
        if steps:
            parts.append("Reasoning steps:")
            for i, step in enumerate(steps[:8], 1):   # cap at 8 steps
                parts.append(f"  Step {i}: {step}")
    parts.append(f"Result: {answer} {unit}")
    return "\n".join(parts)


async def solve(question: str, client, deadline: float) -> dict:
    """Full async pipeline. Returns a dict matching QAResponse fields.

    Parameters
    ----------
    question : str
        The physics problem text.
    client : VLLMClient
        Async HTTP client for vLLM.
    deadline : float
        time.time() value after which we give up and return timeout result.
    """
    t_start = time.time()

    # ------------------------------------------------------------------
    # 1. Classify
    # ------------------------------------------------------------------
    classify_msgs = _build_classify_messages(question)
    classify_raw = await client.chat(classify_msgs, max_tokens=50, temperature=0.0)
    route = _parse_route(classify_raw)

    if time.time() >= deadline:
        return _timeout_result(t_start, route)

    # ------------------------------------------------------------------
    # 2. Codegen
    # ------------------------------------------------------------------
    formula_hints = get_formula_hints(route.domain)
    codegen_msgs = build_codegen_prompt(
        question, route.domain, route.answer_type, formula_hints
    )
    completion = await client.chat(codegen_msgs, max_tokens=2000, temperature=0.0)

    if time.time() >= deadline:
        return _timeout_result(t_start, route)

    # ------------------------------------------------------------------
    # 3. Extract + execute
    # ------------------------------------------------------------------
    code = extract_code(completion)
    exec_result = None
    retry_count = 0

    if code is None:
        # No code block — model failed to generate code
        exec_result = None
    else:
        exec_result = await execute_code_async(code, timeout=10)

        # ------------------------------------------------------------------
        # 4. Retry once on execution failure
        # ------------------------------------------------------------------
        if not exec_result.success and time.time() < deadline:
            retry_count = 1
            error_feedback = (
                f"The previous code produced an error:\n"
                f"stderr: {exec_result.stderr}\n"
                f"stdout: {exec_result.stdout}\n\n"
                f"Fix the code and try again."
            )
            retry_msgs = codegen_msgs + [
                {"role": "assistant", "content": completion},
                {"role": "user", "content": error_feedback},
            ]
            completion = await client.chat(retry_msgs, max_tokens=2000, temperature=0.0)
            code = extract_code(completion)
            if code is not None:
                exec_result = await execute_code_async(code, timeout=10)
            else:
                exec_result = ExecutionResult(
                    success=False,
                    stdout="",
                    stderr="no code block in retry",
                    answer=None,
                    unit=None,
                    error_type="parse",
                )

    elapsed = time.time() - t_start

    # ------------------------------------------------------------------
    # 5. Format result
    # ------------------------------------------------------------------
    if time.time() >= deadline:
        return _timeout_result(t_start, route)

    if exec_result is not None and exec_result.success and exec_result.answer is not None:
        unit = exec_result.unit or "-"
        answer = exec_result.answer
        explanation = _build_explanation(
            question, code, answer, unit, route.domain, route.answer_type
        )
        return {
            "answer": answer,
            "unit": unit,
            "explanation": explanation,
            "cot": completion,
            "confidence": 0.9,
            "solve_method": "code_execution",
            "elapsed_s": elapsed,
            "domain": route.domain,
            "answer_type": route.answer_type,
            "generated_code": code,
            "execution_stdout": exec_result.stdout,
        }

    # Failed — model generated code but it didn't produce a valid answer
    return {
        "answer": "",
        "unit": "",
        "explanation": f"Code execution failed. Domain: {route.domain}.",
        "cot": completion,
        "confidence": 0.0,
        "solve_method": "failed",
        "elapsed_s": elapsed,
        "domain": route.domain,
        "answer_type": route.answer_type,
        "generated_code": code,
        "execution_stdout": exec_result.stdout if exec_result else "",
    }


def _timeout_result(t_start: float, route) -> dict:
    return {
        "answer": "",
        "unit": "",
        "explanation": "Request timed out before a result could be computed.",
        "cot": "",
        "confidence": 0.0,
        "solve_method": "timeout",
        "elapsed_s": time.time() - t_start,
        "domain": route.domain if route else None,
        "answer_type": route.answer_type if route else None,
        "generated_code": None,
        "execution_stdout": "",
    }
