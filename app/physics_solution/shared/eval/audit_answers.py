"""Audit the original dataset answers using a commercial LLM.

Samples N rows from full_test.csv, sends question + answer + unit to the LLM,
and asks it to verify whether the given answer is correct. Outputs a CSV report.

Usage (from repo root):
    python -m app.physics_solution.shared.eval.audit_answers
    python -m app.physics_solution.shared.eval.audit_answers --provider openai --model gpt-5.4-mini --n 100
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import random
import re
import sys
import time
from pathlib import Path

from openai import OpenAI

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

from app.physics_solution.config import (
    COMMERCIAL_API_KEY_ENV,
    COMMERCIAL_BASE_URL,
    COMMERCIAL_MODEL,
    COMMERCIAL_PROVIDER,
    GOLDEN_DIR,
    GOLDEN_SAVE_EVERY,
    TEST_FILE,
    repo_root,
)

# ------------------------------------------------------------------ prompts

SYSTEM_PROMPT = """\
You are a physics answer verifier. You will receive a physics question and a proposed answer (with unit).

Your task:
1. Solve the problem yourself (show brief work, 2-4 lines max).
2. Compare your answer with the proposed answer.
3. Respond with EXACTLY this JSON (no other text):
{"verdict": "correct" or "incorrect", "your_answer": "<your computed value>", "your_unit": "<unit>", "reason": "<one sentence explanation if incorrect, empty string if correct>"}
"""

USER_TEMPLATE = """\
Question: {question}

Proposed answer: {answer}
Proposed unit: {unit}"""

# ------------------------------------------------------------------ parsing

def parse_verdict(text: str) -> dict:
    """Extract JSON verdict from LLM response."""
    try:
        m = re.search(r"\{.*\}", text, re.DOTALL)
        if m:
            return json.loads(m.group(0))
    except (json.JSONDecodeError, AttributeError):
        pass
    return {"verdict": "parse_error", "your_answer": "", "your_unit": "", "reason": f"Could not parse: {text[:200]}"}


# ------------------------------------------------------------------ I/O

def load_test_data(path: Path) -> list[dict]:
    with open(path, "r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def _model_slug(model_name: str) -> str:
    return model_name.replace("/", "_").replace("\\", "_").replace(" ", "_")


# ------------------------------------------------------------------ main

def main() -> None:
    parser = argparse.ArgumentParser(description="Audit original dataset answers via LLM")
    parser.add_argument("--provider", default=COMMERCIAL_PROVIDER)
    parser.add_argument("--model", default=COMMERCIAL_MODEL)
    parser.add_argument("--n", type=int, default=100, help="Number of rows to sample")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for sampling")
    parser.add_argument("--delay", type=float, default=1.0, help="Seconds between API calls")
    args = parser.parse_args()

    root = repo_root()
    test_path = root / TEST_FILE
    out_path = root / GOLDEN_DIR / f"{_model_slug(args.model)}_audit_{args.n}.csv"

    api_key_var = COMMERCIAL_API_KEY_ENV.get(args.provider)
    if not api_key_var:
        sys.exit(f"Unknown provider: {args.provider}")
    api_key = os.environ.get(api_key_var)
    if not api_key:
        sys.exit(f"Missing env var {api_key_var}. Check your .env file.")

    base_url = COMMERCIAL_BASE_URL.get(args.provider)
    client_kwargs: dict = {"api_key": api_key}
    if base_url:
        client_kwargs["base_url"] = base_url
    client = OpenAI(**client_kwargs)

    all_data = load_test_data(test_path)
    random.seed(args.seed)
    sampled = random.sample(all_data, min(args.n, len(all_data)))
    print(f"Sampled {len(sampled)} rows from {len(all_data)} total.\n")

    # Resume support
    existing_ids: set[str] = set()
    results: list[dict] = []
    if out_path.exists():
        with open(out_path, "r", encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                existing_ids.add(row["id"])
                results.append(row)
        print(f"Resuming: {len(existing_ids)} already audited.")

    pending = [r for r in sampled if r["id"] not in existing_ids]
    print(f"{len(pending)} remaining to audit.\n")

    out_fields = ["id", "question", "original_answer", "original_unit",
                  "verdict", "llm_answer", "llm_unit", "reason"]
    processed_since_save = 0

    for i, row in enumerate(pending):
        qid = row["id"]
        print(f"[{i + 1}/{len(pending)}] {qid} ... ", end="", flush=True)

        try:
            resp = client.chat.completions.create(
                model=args.model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": USER_TEMPLATE.format(
                        question=row["question"],
                        answer=row["answer"],
                        unit=row["unit"],
                    )},
                ],
                temperature=0.0,
            )
            text = resp.choices[0].message.content or ""
            v = parse_verdict(text)

            results.append({
                "id": qid,
                "question": row["question"],
                "original_answer": row["answer"],
                "original_unit": row["unit"],
                "verdict": v.get("verdict", ""),
                "llm_answer": v.get("your_answer", ""),
                "llm_unit": v.get("your_unit", ""),
                "reason": v.get("reason", ""),
            })
            processed_since_save += 1
            print(v.get("verdict", "?"))

        except Exception as e:
            print(f"ERROR: {e}")
            processed_since_save += 1

        if processed_since_save >= GOLDEN_SAVE_EVERY:
            _save(out_path, out_fields, results)
            print(f"  -> Saved {len(results)} rows")
            processed_since_save = 0

        if i < len(pending) - 1:
            time.sleep(args.delay)

    _save(out_path, out_fields, results)

    # Summary
    correct = sum(1 for r in results if r["verdict"] == "correct")
    incorrect = sum(1 for r in results if r["verdict"] == "incorrect")
    other = len(results) - correct - incorrect
    print(f"\nDone. {len(results)} rows audited -> {out_path}")
    print(f"  Correct:   {correct}/{len(results)} ({correct/len(results)*100:.1f}%)")
    print(f"  Incorrect: {incorrect}/{len(results)} ({incorrect/len(results)*100:.1f}%)")
    if other:
        print(f"  Other:     {other}")


def _save(path: Path, fields: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()
