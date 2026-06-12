# QC_data — execution-grounded data QC (BTC + Vietjack)

Cleans the v06 SFT input of **broken problem statements** — OCR misreads (`√3/2` ↔
`3√2`), dropped symbols (a missing `π`, `√`, exponent, unit), truncated text, lost MCQ
options — so the fine-tuned model never learns to "guess/fix the problem".

Motivation: an audit of the 19 problems Qwen couldn't solve (the DeepSeek teacher had to
rescue) found ~30% were **broken source data**, not hard physics — the teacher was
silently reverse-engineering the intended number from gold. We clean that up front.

## How it works — every verdict is backed by code that ran

A judgment-only pass (just *reading* the statement) reliably keeps clean data clean but
**misses subtle numeric corruption** (you can't spot a missing `π` without doing the
math). So QC is **execution-grounded** — per problem:

| Stage | What | Outcome |
|---|---|---|
| **1. Solve as-written** | DeepSeek writes code for the problem **as stated** (gold-free prompt) → we execute it in the same local sandbox + scorer as Phase-2 (`pot_common.verify`) and compare to gold | matches gold → **CLEAN** (+ the verified solve is kept as bonus teacher data) |
| **2. Diagnose** | on a mismatch, DeepSeek sees the gold + the failed attempt and decides | **FIX** (repair a corrupted number/symbol/unit, return the corrected statement) or **DROP** (unrepairable / would need guessing intent / the gold itself looks wrong) |
| **3. Confirm FIX** | re-solve the **corrected** statement gold-free | computes gold → **FIX** accepted; else **DROP** (`fix_unconfirmed`) |

The solver never sees gold, so CLEAN/FIX are genuine: the text really computes the answer.
A FIX that would inject the gold value into the statement is rejected (`fix_leaked_gold`).
DeepSeek runs **thinking-ON** by default (solving + diagnosing need reasoning).

Validated on the known-bad ids: judgment-only missed the missing-π / OCR cases
(single-call variance); execution-grounding catches them because the as-written solve
actually disagrees with gold.

## Cost / runtime

Every problem costs ≥1 thinking-on solve; broken ones cost up to ~5 calls (solve+retry,
diagnose, confirm). So it's slower than a judgment pass — **run `--source vietjack` first**
(353, the noisy source) before the BTC 1318. Raise `--concurrency` to compensate.

## Run

Lean venv with `openai` (`.venv/bin/python`); `DEEPSEEK_API_KEY` in `app/physics_solution/.env`.

```bash
PYTHONPATH=. .venv/bin/python -m app.physics_solution.QC_data.run_qc --source vietjack --concurrency 12
PYTHONPATH=. .venv/bin/python -m app.physics_solution.QC_data.run_qc --concurrency 16   # full BTC+VJ
PYTHONPATH=. .venv/bin/python -m app.physics_solution.QC_data.run_qc --limit 20         # smoke
PYTHONPATH=. .venv/bin/python -m app.physics_solution.QC_data.run_qc --selftest         # offline, no API
```

Resumable + checkpointed every `--save-every` (re-run skips ids already in
`qc_verdicts.jsonl`; API-errored ids are not cached, so they retry). `--fresh` redoes all.

## Inputs / outputs

- **in:** `versions/v06_finetune/input/problems_all.jsonl` (1671 ProblemSpecs; `--input` to override)
- **out:** `gold/`
  - `problems_qc.jsonl` — cleaned set (CLEAN + FIX). **Drop-in replacement for
    `problems_all.jsonl` as the Phase-2 self-gen input.**
  - `qc_dropped.jsonl` — DROP audit (id, error_type, reason, original question)
  - `qc_verdicts.jsonl` — full per-problem record **incl. the verified solve code** (resume
    cache; harvestable as teacher trajectories later)
  - `qc_report.md` — counts: verdict × source × domain × error_type

## Files

- `qc_filter.py` — the two prompts (`SOLVE_SYSTEM`, `DIAGNOSE_SYSTEM`) + `parse_diagnose` +
  `apply_verdict` + `gold_leaked` (pure; no API/heavy deps)
- `run_qc.py` — the 3-stage orchestration (`qc_one`) + driver
- `qc_smoke.py` — offline logic test (`--selftest`)

## Notes for the next stage

- After QC, point Phase-2 self-gen at `QC_data/gold/problems_qc.jsonl` and run `--fresh`.
- The verified solves in `qc_verdicts.jsonl` are DeepSeek (teacher) data — declare in the
  Data Disclosure Document if reused; never let them reach inference.
- Group-2 "rounding" noise (yes_no flips from exact `==`) is **not** a statement defect → it
  stays CLEAN here; handle it via the Phase-2 prompt-tolerance change, not QC.
