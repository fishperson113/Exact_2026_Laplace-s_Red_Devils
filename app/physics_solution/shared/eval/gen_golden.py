"""Generate golden data by reformatting original CoT via commercial LLM.

Reads full_test.csv (question + CoT + answer + unit), asks the LLM to rewrite
the CoT into Qwen-style format (Step N, LaTeX math, FINAL ANSWER / UNIT).
Uses async concurrent calls for speed.

Usage (from repo root):
    python -m app.physics_solution.shared.eval.gen_golden
    python -m app.physics_solution.shared.eval.gen_golden --batch-size 20 --limit 50
"""

from __future__ import annotations

import argparse
import asyncio
import csv
import os
import re
import sys
from pathlib import Path

from openai import AsyncOpenAI

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

# ------------------------------------------------------------------ helpers


def _model_slug(model_name: str) -> str:
    return model_name.replace("/", "_").replace("\\", "_").replace(" ", "_")


def golden_output_path(model_name: str) -> Path:
    return repo_root() / GOLDEN_DIR / f"{_model_slug(model_name)}_golden_data.csv"


# ------------------------------------------------------------------ prompts

SYSTEM_PROMPT = """\
You are a physics solution formatter. You will receive a physics question, its correct answer, unit, and an existing chain-of-thought solution.

Your task: rewrite the chain-of-thought into the exact format below. The answer and unit are already correct — do NOT change them. Only rewrite the reasoning steps.

FORMAT RULES:
- Write 3-6 concise steps. Each step: "Step N: <one-sentence description with inline computation>".
- Use LaTeX inline math with $...$: e.g. $F = k \\frac{|q_1 q_2|}{r^2}$, $\\sqrt{LC}$, $2\\pi$, $\\times$, $\\cdot$.
- Keep each step short: state what you compute and the result value. No lengthy derivations.
- End with exactly two lines:
  FINAL ANSWER: <value>
  UNIT: <unit>

ANSWER FORMAT (for FINAL ANSWER line):
- If |exponent| < 4: write a plain decimal, rounded to at most 4 decimal places. Examples: 0.495, 25, 0.0012, 150.
- If |exponent| >= 4: use $a \\times 10^{n}$ notation. Examples: $5.07 \\times 10^{-6}$, $2.027 \\times 10^{6}$.
- Yes/No questions: answer Yes or No.
- Multiple values: separate with semicolons (e.g. 0.6; 1.2).
- No unit: write UNIT: N/A.

IMPORTANT: Preserve the original answer value exactly. Only reformat the CoT reasoning.
"""

FEWSHOT_EXAMPLES = [
    {
        "user": """\
Question: An RLC series circuit consists of R = 100 Ω, L = 0.25 H, and C = 100 μF. The circuit is connected to an AC source with frequency f = 31.8 Hz. Is the circuit at resonance?
Answer: Yes
Unit: N/A
Original CoT: Step 1: Identify the given values. Step 2: Use the resonance formula. Step 3: Calculate and compare. Step 4: The frequency matches. Step 5: The answer is Yes.""",
        "assistant": """\
Step 1: Calculate the resonant frequency using the formula $f_0 = \\frac{1}{2\\pi\\sqrt{LC}}$ with $L=0.25$ H and $C=100 \\times 10^{-6}$ F.
Step 2: Compute the product $LC = 2.5 \\times 10^{-5}$ and its square root, which is approximately $0.005$.
Step 3: Divide $1$ by $2\\pi \\times 0.005$ to find the resonant frequency, resulting in approximately $31.83$ Hz.
Step 4: Compare the calculated frequency ($31.83$ Hz) with the given frequency ($31.8$ Hz) to confirm they match within reasonable precision.
FINAL ANSWER: Yes
UNIT: N/A""",
    },
    {
        "user": """\
Question: Two charges q1 and q2 are placed at points A and B, 2 cm apart. The net electric field is zero at point M, which is 6 cm from A and 8 cm from B. If q1 + q2 = 7 × 10^-8 C, find q2.
Answer: -9 × 10^-8
Unit: C
Original CoT: Step 1: Set up the field equation. Step 2: Find ratio. Step 3: Determine signs. Step 4: Solve for q2.""",
        "assistant": """\
Step 1: Since the net electric field at point M is zero, the magnitudes of the fields from $q_1$ and $q_2$ must be equal, implying $|q_1|/r_1^2 = |q_2|/r_2^2$.
Step 2: Substituting the distances $r_1 = 6$ cm and $r_2 = 8$ cm, we find the ratio $|q_1|/|q_2| = (6/8)^2 = 9/16$.
Step 3: Since $6 + 8 = 14 \\neq 2$, M lies outside segment AB, so charges must have opposite signs. Let $q_1 = +16k$ and $q_2 = -9k$.
Step 4: From $q_1 + q_2 = 7k = 7 \\times 10^{-8}$ C, we get $k = 10^{-8}$ C, therefore $q_2 = -9 \\times 10^{-8}$ C.
FINAL ANSWER: $-9 \\times 10^{-8}$
UNIT: C""",
    },
]

USER_TEMPLATE = """\
Question: {question}
Answer: {answer}
Unit: {unit}
Original CoT: {cot}"""

# ------------------------------------------------------------------ parsing

_FINAL_RE = re.compile(r"FINAL\s*ANSWER\s*:\s*([^\n]+)", re.IGNORECASE)
_UNIT_RE = re.compile(r"UNIT\s*:\s*([^\n]+)", re.IGNORECASE)


def _strip_latex(s: str) -> str:
    s = s.strip()
    if s.startswith("$") and s.endswith("$"):
        s = s[1:-1].strip()
    s = s.replace("\\times", "*")
    return s


def parse_response(text: str) -> tuple[str, str, str]:
    ans_match = _FINAL_RE.search(text)
    unit_match = _UNIT_RE.search(text)
    answer = _strip_latex(ans_match.group(1)) if ans_match else ""
    unit = unit_match.group(1).strip() if unit_match else ""
    cot_end = ans_match.start() if ans_match else len(text)
    cot = text[:cot_end].strip()
    return cot, answer, unit


# ------------------------------------------------------------------ I/O

FIELDS = ["id", "question", "cot", "answer", "unit"]


def load_existing(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    rows = {}
    with open(path, "r", encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            rows[row["id"]] = row
    return rows


def save_rows(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def load_test_data(path: Path) -> list[dict]:
    with open(path, "r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


# ------------------------------------------------------------------ async API

async def call_api(
    client: AsyncOpenAI,
    model: str,
    row: dict,
    semaphore: asyncio.Semaphore,
) -> dict | None:
    async with semaphore:
        messages: list[dict] = [{"role": "system", "content": SYSTEM_PROMPT}]
        for ex in FEWSHOT_EXAMPLES:
            messages.append({"role": "user", "content": ex["user"]})
            messages.append({"role": "assistant", "content": ex["assistant"]})
        messages.append({"role": "user", "content": USER_TEMPLATE.format(
            question=row["question"],
            answer=row["answer"],
            unit=row.get("unit", ""),
            cot=row.get("cot", ""),
        )})

        try:
            resp = await client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.0,
                extra_body={"thinking": {"type": "disabled"}},
            )
            text = resp.choices[0].message.content or ""
            cot, answer, unit = parse_response(text)
            return {
                "id": row["id"],
                "question": row["question"],
                "cot": cot,
                "answer": answer,
                "unit": unit,
            }
        except Exception as e:
            print(f"  ERROR {row['id']}: {e}")
            return None


async def process_batch(
    client: AsyncOpenAI,
    model: str,
    batch: list[dict],
    semaphore: asyncio.Semaphore,
) -> list[dict]:
    tasks = [call_api(client, model, row, semaphore) for row in batch]
    results = await asyncio.gather(*tasks)
    return [r for r in results if r is not None]


# ------------------------------------------------------------------ main

async def async_main() -> None:
    parser = argparse.ArgumentParser(description="Generate golden data (CoT reformat)")
    parser.add_argument("--provider", default=COMMERCIAL_PROVIDER)
    parser.add_argument("--model", default=COMMERCIAL_MODEL)
    parser.add_argument("--limit", type=int, default=None, help="Process only first N rows")
    parser.add_argument("--batch-size", type=int, default=10, help="Concurrent API calls")
    args = parser.parse_args()

    root = repo_root()
    test_path = root / TEST_FILE
    out_path = golden_output_path(args.model)

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
    client = AsyncOpenAI(**client_kwargs)

    test_data = load_test_data(test_path)
    if args.limit:
        test_data = test_data[: args.limit]

    existing = load_existing(out_path)
    all_rows: list[dict] = list(existing.values())
    pending = [r for r in test_data if r["id"] not in existing]
    print(f"Total: {len(test_data)} | Already done: {len(existing)} | Pending: {len(pending)}")
    if not pending:
        print("Nothing to do.")
        return

    semaphore = asyncio.Semaphore(args.batch_size)
    processed = 0

    for i in range(0, len(pending), GOLDEN_SAVE_EVERY):
        chunk = pending[i : i + GOLDEN_SAVE_EVERY]
        print(f"\nBatch {i // GOLDEN_SAVE_EVERY + 1}: processing {len(chunk)} rows "
              f"({i + 1}-{min(i + len(chunk), len(pending))}/{len(pending)}) ...")

        results = await process_batch(client, args.model, chunk, semaphore)
        all_rows.extend(results)
        processed += len(results)

        save_rows(out_path, all_rows)
        print(f"  Saved {len(all_rows)} total rows ({len(results)}/{len(chunk)} succeeded)")

    print(f"\nDone. {processed} new rows processed. Total {len(all_rows)} rows in {out_path}")


def main() -> None:
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
