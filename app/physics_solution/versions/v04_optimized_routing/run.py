"""v04 runner — optimized routing + routed few-shot (2-pass pipeline).

Same architecture as v03 but with an improved classification prompt
(see prompts.py and ROUTING_PROMPT_DESIGN.md for details).
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
)
from app.physics_solution.shared.model.loader import LoadedModel, load_model
from app.physics_solution.shared.prompts.helpers import fewshot_messages_from
from app.physics_solution.shared.prompts.system import ASSISTANT_PREFIX
from app.physics_solution.shared.router import RouteResult, classify_batch
from app.physics_solution.shared.runtime.tracing import setup_tracing
from app.physics_solution.versions.v04_optimized_routing.prompts import (
    build_routed_template,
    CLASSIFY_SYSTEM,
    CLASSIFY_EXAMPLES,
)
from app.physics_solution.versions.v04_optimized_routing import (
    DEFAULT_BASE_MODEL_ID,
    DESCRIPTION,
    STRATEGY_TAG,
    VERSION_NUM,
)


HERE = Path(__file__).resolve().parent
# v04 shares fewshot examples with v03 (same curated pool).
_V03_EXAMPLES = Path(__file__).resolve().parent.parent / "v03_routed_fewshot" / "input" / "examples.json"
EXAMPLES_PATH = HERE / "input" / "examples.json"
PREFIX_RE = re.compile(r"^([A-Z]+)")
N_EXAMPLES_DEFAULT = 2


def _load_examples() -> list[dict]:
    # Try v04's own examples first, fall back to v03's.
    for path in [EXAMPLES_PATH, _V03_EXAMPLES]:
        if path.exists():
            return json.loads(path.read_text(encoding="utf-8"))
    raise FileNotFoundError(
        f"No examples.json found. Run "
        "`python -m app.physics_solution.versions.v03_routed_fewshot.select_fewshot --k 2` "
        "or copy examples.json into v04_optimized_routing/input/."
    )


def _select_examples(
    pool: list[dict],
    route: RouteResult,
    qid: str,
    n: int,
) -> list[dict]:
    """Pick n examples matching (domain, answer_type), falling back gracefully."""
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

    # ---- Pass 1: classify all questions (using v04 optimized prompt)
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

    # ---- Pass 2: solve with routed prompts
    print(f"\n--- Pass 2: solving {len(rows)} questions ---")
    render = RenderPrompt(loaded, assistant_prefix=prefix)
    llm = HFBatchedLLM(
        loaded,
        max_new_tokens=args.max_new_tokens,
        temperature=args.temperature,
        assistant_prefix=prefix,
    )

    completions: list[str] = []
    elapsed_per_row: list[float] = []
    pbar = tqdm(total=len(rows))

    for i in range(0, len(rows), batch_size):
        chunk_rows = rows[i : i + batch_size]
        chunk_routes = routes[i : i + batch_size]

        rendered_prompts: list[str] = []
        for row, route in zip(chunk_rows, chunk_routes):
            qid = str(row.get("id", ""))
            question = str(row["question"])

            examples = _select_examples(pool, route, qid, n_examples)
            template = build_routed_template(route.domain, route.answer_type)

            template_input = {
                "question": question,
                "few_shot_messages": fewshot_messages_from(examples),
            }
            prompt_value = template.invoke(template_input)
            rendered = render.invoke(prompt_value)
            rendered_prompts.append(rendered)

        t0 = time.time()
        chunk_completions = llm.batch(rendered_prompts)
        batch_elapsed = time.time() - t0
        per_row = batch_elapsed / len(chunk_rows)

        completions.extend(chunk_completions)
        elapsed_per_row.extend([per_row] * len(chunk_rows))
        pbar.update(len(chunk_rows))

    pbar.close()

    # ---- Score + assemble results
    extra_meta = {"n_examples": n_examples, "classify_elapsed_s": classify_elapsed}
    results: list[evaluator.RowResult] = []
    for row, completion, elapsed_s, route in zip(rows, completions, elapsed_per_row, routes):
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
                extra={
                    "raw_answer": scored["raw_answer"],
                    "answer_type": scored.get("answer_type", ""),
                    "partial_correct": scored.get("partial_correct", False),
                    "scoring_notes": scored.get("scoring_notes", ""),
                    "routed_domain": route.domain,
                    "routed_answer_type": route.answer_type,
                    "route_confidence": route.confidence,
                    **extra_meta,
                },
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
        description=DESCRIPTION,
        classify_elapsed_s=classify_elapsed,
        n_examples=n_examples,
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
    print(f"Wrote {out_path}")
    print(f"Wrote {out_path.with_suffix('.csv')}")
    print(f"\nAccuracy: {summary['correct']}/{summary['n']} = {summary['accuracy']:.3f}")
    print(f"Mean latency (per question, amortised): {summary['mean_latency_s']:.2f} s")

    correct_routes = sum(
        1 for row, route in zip(rows, routes)
        if PREFIX_RE.match(str(row.get("id", "")))
        and PREFIX_RE.match(str(row.get("id", ""))).group(1) == route.domain
    )
    print(f"Routing accuracy (domain vs ID prefix): {correct_routes}/{len(rows)} = {correct_routes/len(rows):.3f}")

    return summary
