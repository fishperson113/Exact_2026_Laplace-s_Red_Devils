"""v05 runner — 3-stage code execution pipeline with fallback to direct solve.

Pipeline per question:
  1. Route: classify_batch() → (domain, answer_type)
  2. For code-friendly answer types: generate code → execute → format
     With one retry on execution failure, then fallback to direct solve.
  3. For text answer types: direct solve using v03/v04-style routed few-shot.
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
    RenderPrompt,
    HFBatchedLLM,
    _apply_chat_template_no_think,
)
from app.physics_solution.shared.model.loader import LoadedModel, load_model
from app.physics_solution.shared.prompts.helpers import fewshot_messages_from
from app.physics_solution.shared.prompts.system import ASSISTANT_PREFIX
from app.physics_solution.shared.router import RouteResult, classify_batch
from app.physics_solution.shared.runtime.tracing import setup_tracing
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
    build_routed_template,
    should_use_code_execution,
)


HERE = Path(__file__).resolve().parent
_V03_EXAMPLES = Path(__file__).resolve().parent.parent / "v03_routed_fewshot" / "input" / "examples.json"
EXAMPLES_PATH = HERE / "input" / "examples.json"
PREFIX_RE = re.compile(r"^([A-Z]+)")
N_EXAMPLES_DEFAULT = 2


def _load_examples() -> list[dict]:
    for path in [EXAMPLES_PATH, _V03_EXAMPLES]:
        if path.exists():
            return json.loads(path.read_text(encoding="utf-8"))
    raise FileNotFoundError(
        "No examples.json found. Copy examples.json into v05_code_execution/input/ "
        "or ensure v03_routed_fewshot/input/examples.json exists."
    )


def _select_examples(
    pool: list[dict],
    route: RouteResult,
    qid: str,
    n: int,
) -> list[dict]:
    safe = [ex for ex in pool if str(ex.get("id", "")) != qid]

    exact = [ex for ex in safe if ex.get("prefix") == route.domain and ex.get("answer_type") == route.answer_type]
    if len(exact) >= n:
        return exact[:n]

    domain_match = [ex for ex in safe if ex.get("prefix") == route.domain]
    if len(domain_match) >= n:
        return (exact + [e for e in domain_match if e not in exact])[:n]

    type_match = [ex for ex in safe if ex.get("answer_type") == route.answer_type]
    combined = exact + [e for e in domain_match if e not in exact] + [e for e in type_match if e not in exact and e not in domain_match]
    if len(combined) >= n:
        return combined[:n]

    return (combined + [e for e in safe if e not in combined])[:n]


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


def _solve_with_code(
    question: str,
    domain: str,
    answer_type: str,
    loaded: LoadedModel,
    llm: HFBatchedLLM,
    render: RenderPrompt,
) -> dict:
    """Attempt code-generation solve. Returns metadata dict with solve outcome."""
    formula_hints = get_formula_hints(domain)
    msgs = build_codegen_prompt(question, domain, answer_type, formula_hints)
    rendered = _apply_chat_template_no_think(loaded.tokenizer, msgs)

    t0 = time.time()
    completion = llm.invoke(rendered)
    gen_elapsed = time.time() - t0

    code = extract_code(completion)
    if code is None:
        return {
            "success": False,
            "rendered_prompt": rendered,
            "completion": completion,
            "generated_code": None,
            "execution_stdout": "",
            "execution_stderr": "no code block found",
            "retry_count": 0,
            "elapsed_s": gen_elapsed,
        }

    exec_result = execute_code(code)
    retry_count = 0

    if not exec_result.success:
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
        "generated_code": code,
        "execution_stdout": exec_result.stdout,
        "execution_stderr": exec_result.stderr,
        "retry_count": retry_count,
        "elapsed_s": gen_elapsed,
    }


def _solve_direct(
    question: str,
    route: RouteResult,
    qid: str,
    pool: list[dict],
    n_examples: int,
    loaded: LoadedModel,
    llm: HFBatchedLLM,
    render: RenderPrompt,
    prefix: str,
) -> dict:
    """Direct solve using v03/v04-style routed few-shot."""
    examples = _select_examples(pool, route, qid, n_examples)
    template = build_routed_template(route.domain, route.answer_type)

    template_input = {
        "question": question,
        "few_shot_messages": fewshot_messages_from(examples),
    }
    prompt_value = template.invoke(template_input)
    rendered = render.invoke(prompt_value)

    t0 = time.time()
    completion = llm.invoke(rendered)
    elapsed = time.time() - t0

    return {
        "rendered_prompt": rendered,
        "completion": completion,
        "elapsed_s": elapsed,
    }


def run(args) -> dict:
    version_id = f"v{VERSION_NUM:02d}_{STRATEGY_TAG}"
    setup_tracing(version=version_id)

    model_id = args.model_id or DEFAULT_BASE_MODEL_ID
    batch_size = max(1, int(getattr(args, "batch_size", 1) or 1))
    n_examples = getattr(args, "n_examples", None) or N_EXAMPLES_DEFAULT
    prefix = ASSISTANT_PREFIX

    print(
        f"[{version_id}] loading {model_id} dtype={args.dtype} "
        f"device={args.device} batch_size={batch_size}"
    )
    loaded: LoadedModel = load_model(model_id, dtype=args.dtype, device=args.device)

    pool = _load_examples()
    print(f"[{version_id}] loaded {len(pool)} few-shot examples")

    df = pd.read_csv(args.test_file)
    if args.limit:
        df = df.head(args.limit)
    rows = df.to_dict("records")
    print(f"[{version_id}] running on {len(rows)} questions")

    # ---- Pass 1: classify all questions (batched)
    print(f"\n--- Pass 1: classifying {len(rows)} questions ---")
    questions = [str(r["question"]) for r in rows]
    t0 = time.time()
    routes = classify_batch(
        questions, loaded, batch_size=batch_size,
        system_prompt=CLASSIFY_SYSTEM, examples=CLASSIFY_EXAMPLES,
    )
    classify_elapsed = time.time() - t0
    print(f"Classification done in {classify_elapsed:.1f}s")

    domain_counts: dict[str, int] = {}
    type_counts: dict[str, int] = {}
    for route in routes:
        domain_counts[route.domain] = domain_counts.get(route.domain, 0) + 1
        type_counts[route.answer_type] = type_counts.get(route.answer_type, 0) + 1
    print(f"Domain distribution: {domain_counts}")
    print(f"Answer type distribution: {type_counts}")

    code_eligible = sum(1 for r in routes if should_use_code_execution(r.answer_type))
    print(f"Code execution eligible: {code_eligible}/{len(rows)}")

    # ---- Pass 2+3: solve each question
    print(f"\n--- Pass 2+3: solving {len(rows)} questions ---")
    render = RenderPrompt(loaded, assistant_prefix=prefix)
    llm = HFBatchedLLM(
        loaded,
        max_new_tokens=args.max_new_tokens,
        temperature=args.temperature,
        assistant_prefix=prefix,
    )

    extra_meta = {"n_examples": n_examples, "classify_elapsed_s": classify_elapsed}
    results: list[evaluator.RowResult] = []
    method_counts = {"code_execution": 0, "direct_solve": 0, "fallback": 0}

    pbar = tqdm(total=len(rows))
    for row, route in zip(rows, routes):
        qid = str(row.get("id", ""))
        question = str(row["question"])
        gold_answer = str(row.get("answer", ""))
        gold_unit = str(row.get("unit", ""))

        solve_method: str
        extra: dict = {}

        if should_use_code_execution(route.answer_type):
            code_result = _solve_with_code(
                question, route.domain, route.answer_type,
                loaded, llm, render,
            )

            if code_result["success"]:
                solve_method = "code_execution"
                completion = code_result["completion"]
                elapsed_s = code_result["elapsed_s"]
                extra = {
                    "rendered_prompt": code_result["rendered_prompt"],
                    "generated_code": code_result["generated_code"],
                    "execution_stdout": code_result["execution_stdout"],
                    "execution_stderr": code_result["execution_stderr"],
                    "retry_count": code_result["retry_count"],
                }
            else:
                solve_method = "fallback"
                direct = _solve_direct(
                    question, route, qid, pool, n_examples,
                    loaded, llm, render, prefix,
                )
                completion = direct["completion"]
                elapsed_s = code_result["elapsed_s"] + direct["elapsed_s"]
                extra = {
                    "rendered_prompt": direct["rendered_prompt"],
                    "generated_code": code_result.get("generated_code"),
                    "execution_stdout": code_result["execution_stdout"],
                    "execution_stderr": code_result["execution_stderr"],
                    "retry_count": code_result["retry_count"],
                    "code_prompt": code_result["rendered_prompt"],
                }
        else:
            solve_method = "direct_solve"
            direct = _solve_direct(
                question, route, qid, pool, n_examples,
                loaded, llm, render, prefix,
            )
            completion = direct["completion"]
            elapsed_s = direct["elapsed_s"]
            extra = {
                "rendered_prompt": direct["rendered_prompt"],
                "generated_code": None,
                "execution_stdout": "",
                "execution_stderr": "",
                "retry_count": 0,
            }

        method_counts[solve_method] += 1

        scored = _score(completion, gold_answer, gold_unit)
        extra.update({
            "solve_method": solve_method,
            "raw_answer": scored["raw_answer"],
            "answer_type": scored.get("answer_type", ""),
            "partial_correct": scored.get("partial_correct", False),
            "scoring_notes": scored.get("scoring_notes", ""),
            "routed_domain": route.domain,
            "routed_answer_type": route.answer_type,
            "route_confidence": route.confidence,
            **extra_meta,
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

    # ---- Summary
    summary = evaluator.summarise(results)
    summary.update(
        version=version_id,
        model_id=model_id,
        dtype=args.dtype,
        effective_dtype=loaded.effective_dtype,
        batch_size=batch_size,
        assistant_prefix=prefix,
        description=DESCRIPTION,
        classify_elapsed_s=classify_elapsed,
        n_examples=n_examples,
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
        1 for row, route in zip(rows, routes)
        if PREFIX_RE.match(str(row.get("id", "")))
        and PREFIX_RE.match(str(row.get("id", ""))).group(1) == route.domain
    )
    print(f"Routing accuracy (domain vs ID prefix): {correct_routes}/{len(rows)} = {correct_routes/len(rows):.3f}")

    return summary
