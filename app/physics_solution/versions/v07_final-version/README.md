# v07 — final version (self-SFT → train → submit)

Authoritative doc for everything from **self-SFT data generation onward**. The data prep +
QC steps are **done**; this supersedes `versions/v06_finetune/README.md` and
`V06_HANDOFF_PROMPT.md` (both deprecated — they predate the current architecture).

Goal: SFT **Qwen3.5-4B** so it natively emits a **short reasoning (5–10 lines) then ONE
Python code block** that computes the answer — beating v05_best (58.3% on the 60 golden;
target >70%). Keep it lean — **no over-engineering**.

---

## 0. THE data file (single source of truth)

```
app/physics_solution/versions/v06_finetune/input/self_gen_dataset.jsonl
```
**1584** QC-clean problems. **Do not reference any other dataset file.** Each row:
```json
{"id","question","domain","answer_type","gold_answer","gold_unit","dataset_source",
 "hint_code","hint_source"}
```
- `question` is the cleaned statement (corrupted ones were fixed or dropped during QC).
- `hint_code` (1550/1584 have one) = a verified reference solve (DeepSeek/Claude) used **only**
  as a method hint for the hinted route — external data, **declare in the Data Disclosure Doc**,
  never shown at inference.

**Validation set:** [val_56.jsonl](val_56.jsonl) — 56 stratified problems (6 domains ×
4 answer types), described in
[v06_finetune/PHASE2_EDA.md](../v06_finetune/PHASE2_EDA.md). It is the original
`problems_strat.jsonl` 56, except `DDT145` + `vj_l11_0005` were filtered out by QC and
replaced with same-domain/type problems (`DDT209`, `DDT138`). **Train = the other 1528;
val = these 56** (split by id in build_sft).

---

## 1. The one prompt (no prompt-picking)

To save time we skip the prompt-search and use ONE general prompt for every route:
**`data_pipeline/prompts.py::GEN_SYSTEM`** — "reason in 5–10 short lines, then ONE Python
code block; hardcode physical constants; NO HARDCODING of computed values; yes_no with ~1%
tolerance; print `FINAL ANSWER:` / `UNIT:`." `build_gen_messages` (plain) and
`build_hinted_messages` (shows a reference solve) share it, so **every route emits the same
shape**.

---

## 2. Pipeline (what to run, in order)

The data-gen code is the current, working set under
**`versions/v06_finetune/data_pipeline/`** (reused as-is). Run on the GPU box (Qwen via vLLM
on `:18000`); the execution gate runs locally in-process (scipy/sympy, no GPU).

| Step | Module | What | Status |
|---|---|---|---|
| **A. self-gen** (Route 1) | `data_pipeline/selfgen.py` | Qwen multi-temp → reasoning+code → execute → keep correct (dedup); retry once on a code error and keep only the **clean final** reasoning+code (not the error transcript). Too few correct (`--min-keep`) → residual. | ✅ updated |
| **B. hinted** (residual) | `data_pipeline/hinted.py` | For the residual, show Qwen the `hint_code` as a METHOD reference; Qwen re-derives its OWN reasoning+code → execute-verify. **No API.** On-policy ⇒ less domain shift. | ✅ new |
| **C. guards** | `data_pipeline/guards.py` | spurious-reject (echo/hardcode) + dedup + cap **top-4 per problem** (prefers self_gen > hinted). → `output/trajectories_sft.jsonl` | ✅ updated |
| **D. build_sft** | `v07` (to build) | split by the 56 val ids → `train.jsonl` / `val.jsonl`, formatted as the Qwen chat template (system=`GEN_SYSTEM`, user=problem block, assistant=reasoning+code). | ⏳ todo |
| **E. SFT train** | `v07/train/` (to build) | Unsloth QLoRA on `train.jsonl`; eval on `val_56` + the 60 golden. | ⏳ todo |
| **F. inference + explanation/cot** | `v07` (to build) | see §3 | ⏳ todo |

Run A→C (the data-gen the other chat executes):
```bash
# on Vast (vLLM serving Qwen3.5-4B on :18000); reads the canonical dataset by default
PYTHONPATH=. python -m app.physics_solution.versions.v06_finetune.data_pipeline.selfgen --concurrency 48
#   -> output/trajectories_selfgen.jsonl  +  output/selfgen_residual.jsonl (carries hint_code)
PYTHONPATH=. python -m app.physics_solution.versions.v06_finetune.data_pipeline.hinted   --concurrency 32
#   -> output/trajectories_hinted.jsonl   +  output/hinted_failed.jsonl
PYTHONPATH=. python -m app.physics_solution.versions.v06_finetune.data_pipeline.guards   --cap 4
#   -> output/trajectories_sft.jsonl      +  output/guards_rejected.jsonl
```
Every stage auto-saves and resumes (skips done ids). Local GPU-free smoke first:
`python -m ...selfgen --stub --limit 30`.

> **Note on code location:** the runnable data-gen modules stay in `v06_finetune/data_pipeline/`
> (they work and are interdependent — moving them is needless churn). This `v07_final-version/`
> folder holds the authoritative docs + `val_56.jsonl` + the new steps D–F. The folder name has
> a hyphen (not import-safe); put any new **runnable** Python either in
> `v06_finetune/data_pipeline/` or a renamed `v07_final_version/` package.

---

## 3. Submission needs answer + explanation + cot (post-hoc, §F — to build)

The competition row requires **`answer`** (+ unit), **`explanation`** (P2 score), and
**`cot`** (P3 score) — not just the answer. Plan (no extra training):

1. The fine-tuned model solves: short reasoning → code → execute → parse `answer` + `unit`.
2. Feed `(reasoning + code + executed answer)` to a **plain Qwen** (same served model, a second
   pass) to WRITE:
   - **`explanation`** — a clean, human-readable solution writeup, and
   - **`cot`** — the step-by-step chain-of-thought (the tool/exec log + reasoning).
3. Assemble the submission row: `{answer, unit, explanation, cot, confidence}`.

This is an **inference-time** add-on (sequential single-model passes — allowed; ≤60 s/request).
Build it in §F; keep the writer prompt short. (Documented here for now per the plan.)

---

## 4. Conventions that still hold (load-bearing)
- **Short reasoning, tight code.** The 4B burns its budget on LaTeX walls → timeouts. Cap the
  reasoning at 5–10 lines.
- **Hardcode constants** (`k=9e9`, `mu_0`, …); **NO HARDCODING** of computed/intermediate
  values (sympy symbolic OK when no numbers given).
- **Scorer format** `FINAL ANSWER: <value>` + `UNIT: <unit>` everywhere (gen, training target,
  pipeline output). `shared/eval/scorer.py` handles numeric / sci_notation / yes_no /
  multi_value / text / mixed.
- **Evaluate on `val_56` + the 60 golden** (`data/golden/`), report both.
- All hint/teacher-origin data is external → **Data Disclosure Document**; never at inference.

## Layout
```
v07_final-version/
├── README.md        # this file (authoritative)
├── val_56.jsonl     # the 56-problem validation set
└── (to build: build_sft, train/sft_unsloth, explain — steps D–F)
```
