"""Concurrent batch evaluation client — calls /ask API endpoint.

Usage examples
--------------
# Sequential (1 request at a time) — matches real competition conditions:
python -m app.physics_solution.cli.eval_api \\
    --api-url https://xxx.trycloudflare.com \\
    --test-file app/physics_solution/data/golden/deepseek-v4-pro_golden_data.csv \\
    --concurrency 1

# Parallel (8 concurrent) — fast batch eval, keeps GPU busy:
python -m app.physics_solution.cli.eval_api \\
    --api-url https://xxx.trycloudflare.com \\
    --test-file app/physics_solution/data/golden/deepseek-v4-pro_golden_data.csv \\
    --concurrency 8 \\
    --out app/physics_solution/versions/v05_best_vLLM/output/results_golden.json
"""

from __future__ import annotations

import argparse
import asyncio
import json
import time
from pathlib import Path

import httpx
import pandas as pd
from tqdm import tqdm

from app.physics_solution.shared.eval import scorer as evaluator


# ---------------------------------------------------------------------------
# Scoring helper (reconstruct completion string from structured response)
# ---------------------------------------------------------------------------

def _score_response(response: dict, gold_answer: str, gold_unit: str) -> dict:
    """Score a /ask API response against gold answer."""
    answer = response.get("answer", "")
    unit = response.get("unit", "")
    # Reconstruct the completion format the scorer expects
    completion = f"FINAL ANSWER: {answer}\nUNIT: {unit}" if answer else ""
    result = evaluator.score(completion, gold_answer, gold_unit)
    extracted = evaluator.extract(completion)
    pred_numeric = (
        result.pred_value if isinstance(result.pred_value, float) else extracted.numeric
    )
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


# ---------------------------------------------------------------------------
# Async evaluation
# ---------------------------------------------------------------------------

async def _evaluate_async(
    api_url: str,
    rows: list[dict],
    concurrency: int,
    request_timeout: float,
    pbar: tqdm,
) -> list[evaluator.RowResult]:
    semaphore = asyncio.Semaphore(concurrency)
    results: list[evaluator.RowResult | None] = [None] * len(rows)

    async with httpx.AsyncClient(
        base_url=api_url,
        timeout=httpx.Timeout(request_timeout),
    ) as client:

        async def process(idx: int, row: dict) -> None:
            async with semaphore:
                qid = str(row.get("id", ""))
                question = str(row["question"])
                gold_answer = str(row.get("answer", ""))
                gold_unit = str(row.get("unit", ""))

                t0 = time.time()
                try:
                    resp = await client.post("/ask", json={"question": question})
                    resp.raise_for_status()
                    data = resp.json()
                except Exception as exc:
                    data = {
                        "answer": "",
                        "unit": "",
                        "explanation": "",
                        "cot": "",
                        "solve_method": "api_error",
                        "elapsed_s": time.time() - t0,
                        "domain": None,
                        "answer_type": None,
                        "generated_code": None,
                        "execution_stdout": str(exc),
                    }

                scored = _score_response(data, gold_answer, gold_unit)
                results[idx] = evaluator.RowResult(
                    id=qid,
                    question=question,
                    gold_answer=gold_answer,
                    gold_unit=gold_unit,
                    completion=scored["completion"],
                    pred_numeric=scored["pred_numeric"],
                    pred_unit=scored["pred_unit"],
                    is_correct=scored["is_correct"],
                    elapsed_s=data.get("elapsed_s", time.time() - t0),
                    extra={
                        "solve_method": data.get("solve_method", ""),
                        "raw_answer": scored["raw_answer"],
                        "answer_type": scored["answer_type"],
                        "partial_correct": scored["partial_correct"],
                        "scoring_notes": scored["scoring_notes"],
                        "routed_domain": data.get("domain"),
                        "routed_answer_type": data.get("answer_type"),
                        "generated_code": data.get("generated_code"),
                        "execution_stdout": data.get("execution_stdout"),
                    },
                )
                pbar.update(1)

        await asyncio.gather(*[process(i, row) for i, row in enumerate(rows)])

    return [r for r in results if r is not None]


# ---------------------------------------------------------------------------
# CLI entrypoint
# ---------------------------------------------------------------------------

def main() -> None:
    p = argparse.ArgumentParser(description="Concurrent batch eval via /ask API")
    p.add_argument("--api-url", required=True, help="Base URL, e.g. https://xxx.trycloudflare.com")
    p.add_argument(
        "--test-file",
        default="app/physics_solution/data/golden/deepseek-v4-pro_golden_data.csv",
    )
    p.add_argument("--out", default=None, help="Output JSON path (default: auto)")
    p.add_argument(
        "--concurrency",
        type=int,
        default=1,
        help="Concurrent requests (1 = sequential, 8 = parallel). Default: 1",
    )
    p.add_argument("--limit", type=int, default=None, help="Cap number of rows")
    p.add_argument(
        "--request-timeout",
        type=float,
        default=65.0,
        help="HTTP timeout per request in seconds (default: 65)",
    )
    args = p.parse_args()

    df = pd.read_csv(args.test_file)
    if args.limit:
        df = df.head(args.limit)
    rows = df.to_dict("records")

    api_url = args.api_url.rstrip("/")
    print(f"Evaluating {len(rows)} questions | concurrency={args.concurrency} | api={api_url}")

    pbar = tqdm(total=len(rows))
    t_wall_start = time.time()
    results = asyncio.run(
        _evaluate_async(api_url, rows, args.concurrency, args.request_timeout, pbar)
    )
    pbar.close()
    wall_elapsed = time.time() - t_wall_start

    summary = evaluator.summarise(results)
    summary.update(
        api_url=api_url,
        concurrency=args.concurrency,
        wall_elapsed_s=round(wall_elapsed, 2),
        throughput_qpm=round(len(results) / wall_elapsed * 60, 1),
    )

    out_path = (
        Path(args.out)
        if args.out
        else Path("app/physics_solution/versions/v05_best_vLLM/output/results_api.json")
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

    print(f"\nAccuracy : {summary['correct']}/{summary['n']} = {summary['accuracy']:.3f}")
    print(f"Wall time: {wall_elapsed:.1f}s  |  throughput: {summary['throughput_qpm']:.1f} q/min")
    print(f"Wrote     {out_path}")


if __name__ == "__main__":
    main()
