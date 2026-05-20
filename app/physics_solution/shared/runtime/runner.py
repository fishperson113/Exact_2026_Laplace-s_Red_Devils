"""LangChain-based inference loop, shared across versions.

Each version's `run.py` provides:
    - version metadata (number, strategy tag, default base model)
    - a `build_inputs(row) -> dict` mapping a dataset row to template vars
    - a `prompt_template: ChatPromptTemplate`

This module wires those into an LCEL chain and runs `chain.batch()`.
LangSmith tracing is automatic when the env vars are present.
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Callable

import pandas as pd
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from tqdm import tqdm

from app.physics_solution.shared.eval import scorer as evaluator
from app.physics_solution.shared.model.batched_llm import HFBatchedLLM, RenderPrompt
from app.physics_solution.shared.model.loader import LoadedModel, load_model
from app.physics_solution.shared.prompts.system import ASSISTANT_PREFIX
from app.physics_solution.shared.runtime.tracing import setup_tracing


InputBuilder = Callable[[dict], dict]
"""build_inputs(row_dict) -> chain_input_dict.

The dataset row is a dict (one record from CSV). Return whatever the
prompt template needs: at minimum `{"question": ...}`, plus
`{"few_shot_messages": [...]}` for v02-style versions."""


def _to_float(s) -> float | None:
    try:
        return float(str(s).strip())
    except (ValueError, TypeError):
        return None


def _score(completion: str, gold_answer: str, gold_unit: str) -> dict:
    extracted = evaluator.extract(completion)
    gold = _to_float(gold_answer)
    correct = gold is not None and evaluator.numeric_close(extracted.numeric, gold)
    return {
        "completion": completion,
        "pred_numeric": extracted.numeric,
        "pred_unit": extracted.raw_unit,
        "raw_answer": extracted.raw_answer,
        "is_correct": correct,
        "gold_numeric": gold,
        "gold_unit": gold_unit,
    }


def run_solver(
    args,
    *,
    version_num: int,
    strategy_tag: str,
    default_model_id: str,
    description: str,
    prompt_template: ChatPromptTemplate,
    build_inputs: InputBuilder,
    extra_meta: dict | None = None,
    assistant_prefix: str | None = None,
) -> dict:
    """Run inference over args.test_file. Returns the summary dict."""
    version_id = f"v{version_num:02d}_{strategy_tag}"
    setup_tracing(version=version_id)

    model_id = args.model_id or default_model_id
    batch_size = max(1, int(getattr(args, "batch_size", 1) or 1))
    prefix = ASSISTANT_PREFIX if assistant_prefix is None else assistant_prefix
    print(
        f"[{version_id}] loading {model_id} dtype={args.dtype} "
        f"device={args.device} batch_size={batch_size} prefix={prefix!r}"
    )
    loaded: LoadedModel = load_model(model_id, dtype=args.dtype, device=args.device)

    # ---- The LCEL chain. Read top-to-bottom:
    # 1. The dataset row → template variables (question, few_shot_messages...)
    # 2. ChatPromptTemplate fills the messages.
    # 3. RenderPrompt turns the messages into a tokenizer-rendered string.
    # 4. HFBatchedLLM batches everything through `generate_batch`.
    render_runnable = RenderPrompt(loaded, assistant_prefix=prefix)
    llm = HFBatchedLLM(
        loaded,
        max_new_tokens=args.max_new_tokens,
        temperature=args.temperature,
        assistant_prefix=prefix,
    )
    chain = (
        RunnableLambda(build_inputs).with_config(run_name=f"{version_id}_build_inputs")
        | prompt_template
        | render_runnable.with_config(run_name=f"{version_id}_render")
        | llm.with_config(run_name=f"{version_id}_generate")
    )
    chain = chain.with_config(run_name=f"{version_id}_solve_one")

    df = pd.read_csv(args.test_file)
    if args.limit:
        df = df.head(args.limit)
    rows = df.to_dict("records")
    print(f"Running on {len(rows)} questions (batch_size={batch_size})")

    extra_meta = dict(extra_meta or {})

    # Process in chunks so each `chain.batch(...)` is one batched GPU call.
    completions: list[str] = []
    elapsed_per_row: list[float] = []
    pbar = tqdm(total=len(rows))
    for i in range(0, len(rows), batch_size):
        chunk = rows[i : i + batch_size]
        t0 = time.time()
        chunk_completions = chain.batch(chunk)
        batch_elapsed = time.time() - t0
        per_row = batch_elapsed / len(chunk)
        completions.extend(chunk_completions)
        elapsed_per_row.extend([per_row] * len(chunk))
        pbar.update(len(chunk))
    pbar.close()

    # ---- Score + assemble results.
    results: list[evaluator.RowResult] = []
    for row, completion, elapsed_s in zip(rows, completions, elapsed_per_row):
        qid = str(row.get("id", ""))
        question = str(row["question"])
        gold_answer = str(row.get("answer", ""))
        gold_unit = str(row.get("unit", ""))
        scored = _score(completion, gold_answer, gold_unit)
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
                extra={"raw_answer": scored["raw_answer"], **extra_meta},
            )
        )

    summary = evaluator.summarise(results)
    summary.update(
        version=version_id,
        model_id=model_id,
        dtype=args.dtype,
        effective_dtype=loaded.effective_dtype,
        batch_size=batch_size,
        assistant_prefix=prefix,
        description=description,
        **extra_meta,
    )

    out_path = (
        Path(args.out)
        if args.out
        else Path(f"app/physics_solution/results/{version_id}.json")
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
    print(f"Wrote {out_path}")
    print(f"Wrote {out_path.with_suffix('.csv')}")
    print(f"\nAccuracy: {summary['correct']}/{summary['n']} = {summary['accuracy']:.3f}")
    print(f"Mean latency (per question, amortised): {summary['mean_latency_s']:.2f} s")
    return summary
