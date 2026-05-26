"""v05 runner — per-sample classify-then-solve pipeline with code execution.

Pipeline per question (60s hard timeout):
  1. Classify: classify_question() -> (domain, answer_type)
  2. Generate Python code -> execute -> format answer
     One retry on execution failure; no fallback to LLM direct solve.
"""

from __future__ import annotations

import json
import re
import time
from pathlib import Path

import pandas as pd
from tqdm import tqdm

from app.physics_solution.shared.eval import scorer as evaluator
from app.physics_solution.shared.model.batched_llm import (
    HFBatchedLLM,
    _apply_chat_template_no_think,
)
from app.physics_solution.shared.model.loader import LoadedModel, load_model
from app.physics_solution.shared.prompts.system import ASSISTANT_PREFIX
from app.physics_solution.shared.router import RouteResult, classify_question
from app.physics_solution.shared.runtime.tracing import setup_tracing, traceable
from app.physics_solution.versions.v05_code_execution import (
    DEFAULT_BASE_MODEL_ID,
    DESCRIPTION,
    STRATEGY_TAG,
    VERSION_NUM,
)
from app.physics_solution.versions.v05_code_execution.code_executor import (
    ExecutionResult,
    extract_code,
    execute_code,
    format_answer,
)
from app.physics_solution.versions.v05_code_execution.formula_kb import get_formula_hints
from app.physics_solution.versions.v05_code_execution.prompts import (
    CLASSIFY_SYSTEM,
    CLASSIFY_EXAMPLES,
    build_codegen_prompt,
    should_use_code_execution,
)


QUESTION_TIMEOUT_S = 60.0
PREFIX_RE = re.compile(r"^([A-Z]+)")


def _score(completion: str, gold_answer: str, gold_unit: str) -> dict:
    result = evaluator.score(completion, gold_answer, gold_unit)
    extracted = evaluator.extract(completion)
    pred_numeric = result.pred_value if isinstance(result.pred_value, float) else extracted.numeric
    return {
        "completion": completion,
        "pred_numeric": pred_numeric,
        "pred_unit": result.pred_unit,
        "raw_answer": extracted.raw_answer,
        "is_correct": result.is_correct,
        "answer_type": result.detected_answer_type.value,
        "partial_correct": result.partial_correct,
        "scoring_notes": result.notes,
    }


@traceable(name="solve_with_code", run_type="chain")
def _solve_with_code(
    question: str,
    domain: str,
    answer_type: str,
    loaded: LoadedModel,
    llm: HFBatchedLLM,
    deadline: float,
) -> dict:
    """Generate code, execute, retry once if failed. Respects deadline."""
    formula_hints = get_formula_hints(domain)
    msgs = build_codegen_prompt(question, domain, answer_type, formula_hints)
    rendered = _apply_chat_template_no_think(loaded.tokenizer, msgs)

    t0 = time.time()
    completion = llm.invoke(rendered)
    gen_elapsed = time.time() - t0

    raw_completion = completion

    code = extract_code(completion)
    if code is None:
        return {
            "success": False,
            "rendered_prompt": rendered,
            "completion": completion,
            "raw_completion": raw_completion,
            "generated_code": None,
            "execution_stdout": "",
            "execution_stderr": "no code block found",
            "retry_count": 0,
            "elapsed_s": gen_elapsed,
        }

    exec_result = execute_code(code)
    retry_count = 0

    if not exec_result.success and time.time() < deadline:
        retry_count = 1
        error_feedback = (
            f"The previous code produced an error:\n"
            f"stderr: {exec_result.stderr}\n"
            f"stdout: {exec_result.stdout}\n\n"
            f"Fix the code and try again."
        )
        retry_msgs = msgs + [
            {"role": "assistant", "content": completion},
            {"role": "user", "content": error_feedback},
        ]
        rendered_retry = _apply_chat_template_no_think(loaded.tokenizer, retry_msgs)

        t0 = time.time()
        completion = llm.invoke(rendered_retry)
        raw_completion += "\n\n--- RETRY ---\n\n" + completion
        gen_elapsed += time.time() - t0

        code = extract_code(completion)
        if code is not None:
            exec_result = execute_code(code)
        else:
            exec_result = ExecutionResult(
                success=False, stdout="", stderr="no code block in retry",
                answer=None, unit=None, error_type="parse",
            )

    if exec_result.success and exec_result.answer is not None:
        unit = exec_result.unit or "-"
        formatted = format_answer(exec_result.answer, unit)
        return {
            "success": True,
            "rendered_prompt": rendered,
            "completion": formatted,
            "raw_completion": raw_completion,
            "generated_code": code,
            "execution_stdout": exec_result.stdout,
            "execution_stderr": exec_result.stderr,
            "retry_count": retry_count,
            "elapsed_s": gen_elapsed,
        }

    return {
        "success": False,
        "rendered_prompt": rendered,
        "completion": completion,
        "raw_completion": raw_completion,
        "generated_code": code,
        "execution_stdout": exec_result.stdout,
        "execution_stderr": exec_result.stderr,
        "retry_count": retry_count,
        "elapsed_s": gen_elapsed,
    }


def run(args) -> dict:
    version_id = f"v{VERSION_NUM:02d}_{STRATEGY_TAG}"
    setup_tracing(version=version_id)

    model_id = args.model_id or DEFAULT_BASE_MODEL_ID
    prefix = ASSISTANT_PREFIX

    print(f"[{version_id}] loading {model_id} dtype={args.dtype} device={args.device}")
    loaded: LoadedModel = load_model(model_id, dtype=args.dtype, device=args.device)

    df = pd.read_csv(args.test_file)
    if args.limit:
        df = df.head(args.limit)
    rows = df.to_dict("records")
    print(f"[{version_id}] running on {len(rows)} questions")

    llm = HFBatchedLLM(
        loaded,
        max_new_tokens=args.max_new_tokens,
        temperature=args.temperature,
        assistant_prefix=prefix,
    )

    results: list[evaluator.RowResult] = []
    method_counts = {"code_execution": 0, "failed": 0, "timeout": 0}
    domain_counts: dict[str, int] = {}
    type_counts: dict[str, int] = {}
    routes_for_summary: list[RouteResult] = []

    @traceable(name="process_question", run_type="chain")
    def _process_question(qid: str, question: str, reference: dict) -> dict:
        """Classify + solve + score within 60s budget. Single LangSmith chain."""
        gold_answer = reference["answer"]
        gold_unit = reference["unit"]

        t_start = time.time()
        deadline = t_start + QUESTION_TIMEOUT_S

        route = classify_question(
            question, loaded,
            system_prompt=CLASSIFY_SYSTEM, examples=CLASSIFY_EXAMPLES,
        )
        classify_elapsed = time.time() - t_start

        if time.time() >= deadline:
            scored = _score("", gold_answer, gold_unit)
            return {
                "result": f"{'TRUE' if scored['is_correct'] else 'FALSE'} | timeout",
                "route": route,
                "classify_elapsed_s": classify_elapsed,
                "solve_method": "timeout",
                "completion": "",
                "is_correct": scored["is_correct"],
                "scored": scored,
                "elapsed_s": time.time() - t_start,
                "extra": {
                    "rendered_prompt": "",
                    "raw_completion": "",
                    "generated_code": None,
                    "execution_stdout": "",
                    "execution_stderr": "timeout after classification",
                    "retry_count": 0,
                },
            }

        code_result = _solve_with_code(
            question, route.domain, route.answer_type,
            loaded, llm, deadline,
        )

        total_elapsed = time.time() - t_start

        if total_elapsed > QUESTION_TIMEOUT_S:
            solve_method = "timeout"
            completion = ""
        elif code_result["success"]:
            solve_method = "code_execution"
            completion = code_result["completion"]
        else:
            solve_method = "failed"
            completion = ""

        scored = _score(completion, gold_answer, gold_unit)

        return {
            "result": f"{'TRUE' if scored['is_correct'] else 'FALSE'} | {solve_method}",
            "route": route,
            "classify_elapsed_s": classify_elapsed,
            "solve_method": solve_method,
            "completion": completion,
            "is_correct": scored["is_correct"],
            "scored": scored,
            "elapsed_s": total_elapsed,
            "extra": {
                "rendered_prompt": code_result["rendered_prompt"],
                "raw_completion": code_result["raw_completion"],
                "generated_code": code_result["generated_code"],
                "execution_stdout": code_result["execution_stdout"],
                "execution_stderr": code_result["execution_stderr"],
                "retry_count": code_result["retry_count"],
            },
        }

    pbar = tqdm(total=len(rows))
    for row in rows:
        qid = str(row.get("id", ""))
        question = str(row["question"])
        gold_answer = str(row.get("answer", ""))
        gold_unit = str(row.get("unit", ""))

        result_dict = _process_question(qid, question, {"answer": gold_answer, "unit": gold_unit})
        route = result_dict["route"]
        solve_method = result_dict["solve_method"]
        completion = result_dict["completion"]
        elapsed_s = result_dict["elapsed_s"]
        extra = result_dict["extra"]
        scored = result_dict["scored"]

        domain_counts[route.domain] = domain_counts.get(route.domain, 0) + 1
        type_counts[route.answer_type] = type_counts.get(route.answer_type, 0) + 1
        routes_for_summary.append(route)
        method_counts[solve_method] += 1

        extra.update({
            "solve_method": solve_method,
            "raw_answer": scored["raw_answer"],
            "answer_type": scored.get("answer_type", ""),
            "partial_correct": scored.get("partial_correct", False),
            "scoring_notes": scored.get("scoring_notes", ""),
            "routed_domain": route.domain,
            "routed_answer_type": route.answer_type,
            "route_confidence": route.confidence,
            "classify_elapsed_s": result_dict["classify_elapsed_s"],
        })

        results.append(
            evaluator.RowResult(
                id=qid,
                question=question,
                gold_answer=gold_answer,
                gold_unit=gold_unit,
                completion=scored["completion"],
                pred_numeric=scored["pred_numeric"],
                pred_unit=scored["pred_unit"],
                is_correct=scored["is_correct"],
                elapsed_s=elapsed_s,
                extra=extra,
            )
        )
        pbar.update(1)

    pbar.close()

    print(f"\nDomain distribution: {domain_counts}")
    print(f"Answer type distribution: {type_counts}")
    code_eligible = sum(1 for r in routes_for_summary if should_use_code_execution(r.answer_type))
    print(f"Code execution eligible: {code_eligible}/{len(rows)}")

    summary = evaluator.summarise(results)
    summary.update(
        version=version_id,
        model_id=model_id,
        dtype=args.dtype,
        effective_dtype=loaded.effective_dtype,
        assistant_prefix=prefix,
        description=DESCRIPTION,
        method_counts=method_counts,
    )

    out_path = (
        Path(args.out)
        if args.out
        else Path(f"app/physics_solution/versions/{version_id}/output/results.json")
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(
            {"summary": summary, "rows": [r.__dict__ for r in results]},
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    pd.DataFrame([r.__dict__ for r in results]).to_csv(
        out_path.with_suffix(".csv"), index=False
    )
    print(f"\nWrote {out_path}")
    print(f"Wrote {out_path.with_suffix('.csv')}")
    print(f"\nAccuracy: {summary['correct']}/{summary['n']} = {summary['accuracy']:.3f}")
    print(f"Mean latency (per question): {summary['mean_latency_s']:.2f} s")
    print(f"Solve methods: {method_counts}")

    correct_routes = sum(
        1 for row, route in zip(rows, routes_for_summary)
        if PREFIX_RE.match(str(row.get("id", "")))
        and PREFIX_RE.match(str(row.get("id", ""))).group(1) == route.domain
    )
    print(f"Routing accuracy (domain vs ID prefix): {correct_routes}/{len(rows)} = {correct_routes/len(rows):.3f}")

    return summary
