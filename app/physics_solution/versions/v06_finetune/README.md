# v06_finetune

Fine-tune **Qwen3.5-4B** (Unsloth QLoRA) so it natively emits **Program-of-Thought
code-gen** — a short reason + one self-contained Python script that prints
`FINAL ANSWER:` / `UNIT:` — without long prompts or few-shot examples. Target:
beat v05_best (58.3% on the 60 golden) and exceed **70%**.

The model design is unchanged from v05_best; **the new work is the data + training
pipelines.** See [V06_HANDOFF_PROMPT.md](V06_HANDOFF_PROMPT.md) for full background.

## Locked design decisions (v06 kickoff)

| Decision | Choice | Why |
|---|---|---|
| **PoT shape** | **1 code block + short reason, retry once on error** (same as v05_best — NOT multi-turn tool-use) | 60s budget + the proven "short prompts win for 4B" lesson. Reuses `v05_best/code_executor.py` as-is. |
| **Val scope** | Keep the exact **60 LDDT golden** (v05_best parity) **and** a broader stratified multi-domain val; report both | The committed 60-golden set is 100% electrostatics — narrow target can hide regressions in other domains. |
| **Build order** | **SFT first** (full SFT→eval cycle), CPT only as an A/B experiment afterward | SFT is the proven lever; don't block on CPT corpus processing. |
| **Vietjack scope** | Filter to the **6 competition domains only** (LDDT/CH/NL/TD/DDT/THCB) | Vietjack lop-10..12 has off-domain physics (pendulum, nuclear, optics) that would shift the distribution. |

Self-gen runs on **vLLM** (fast), not HF. Every self-gen sample is
**execution-verified**: keep only code that runs and whose answer matches gold
(via `shared/eval/scorer.py`). Wrong answers → retry with error feedback; if still
wrong after K samples → hand off to the **DeepSeek teacher** (Route-2/3).

## Domain taxonomy

The golden CSV has 8 id prefixes; the canonical 6-way map is reused from
`shared/router.py` (do not redefine):

```
LD, DT -> LDDT     CHLT -> CH     DDT -> DDT (NB: distinct from DT!)
CH, NL, TD, THCB -> themselves
```

`data_pipeline/taxonomy.py` exposes `domain_from_id()` / `canonicalize_domain()`.

## Layout

```
v06_finetune/
├── __init__.py              # version metadata (VERSION_NUM=6, ...)
├── README.md                # this file
├── V06_HANDOFF_PROMPT.md    # full background / rationale
├── input/                   # version inputs (SFT JSONL config, etc.)
├── output/                  # eval results land here (run.py)
├── data_pipeline/
│   ├── schema.py            # ProblemSpec / Trajectory / Provenance + JSONL I/O  [Phase 0 ✓]
│   ├── taxonomy.py          # canonical domain map                                [Phase 0 ✓]
│   ├── extract_golden60.py  # -> data/golden/golden_60.csv                        [Phase 0 ✓]
│   ├── filter.py            # Step-0: drop figure/underspecified (DeepSeek)       [Phase 1]
│   ├── vietjack_normalize.py# domain-filter -> VN->EN -> answer/unit extract      [Phase 1]
│   ├── vllm_client.py       # async vLLM client (n-sampling, thinking off)        [Phase 2 ✓]
│   ├── pot_common.py        # execution gate: verify/make_trajectory/checkpoint   [Phase 2 ✓]
│   ├── selfgen.py           # Route-1: Qwen via vLLM, multi-temp, exec-verified   [Phase 2 ✓]
│   ├── teacher.py           # Route-2/3: DeepSeek-pro residual                    [Phase 2 ✓]
│   ├── guards.py            # spurious-correct reject, dedup, cap                 [Phase 2 ✓]
│   ├── pot_smoke.py         # local GPU-free harness test                         [Phase 2 ✓]
│   └── build_sft.py         # stratified split + Qwen chat-template JSONL         [Phase 3]
├── train/
│   ├── sft_unsloth.py       # SFT QLoRA (Vast AI)                                 [Phase 4]
│   └── cpt_unsloth.py       # optional CPT warm-up (Vast AI, A/B)                 [Phase 6]
├── prompts.py               # shortened CODEGEN system (no inline example)        [Phase 5]
├── pipeline.py              # solve() — vLLM serving                              [Phase 5]
└── run.py                   # run(args) — batch eval; register in cli/inference   [Phase 5]
```

## Phases & where they run

| Phase | Deliverable | Machine | Status |
|---|---|---|---|
| **0. Scaffolding** | folders, `schema.py`, `taxonomy.py`, `golden_60.csv` | Local | **done** |
| **1. Filter + Normalize** | Step-0 filter; Vietjack domain-filter + VN→EN + answer/unit; one unified format | Local + DeepSeek | **done** |
| **2. Trajectories** | Route-1 self-gen (Qwen vLLM, multi-temp) → exec-verify → Route-2/3 teacher residual → guards | Vast AI + Local | code ready; run pending |
| **3. Build SFT set** | stratified split (val ⊇ 60 golden + multi-domain slice) → JSONL | Local | todo |
| **4. Train SFT** | Unsloth QLoRA; eval vs v05_best on `golden_60` + broad val | Vast AI | todo |
| **5. Inference** | `pipeline.py` + `run.py`, register in `cli/inference.py` | Vast AI | todo |
| **6. CPT (A/B)** | concat/pack `pretrain_corpus` → CPT warm-up → compare | Vast AI | optional |

## Trajectory schema (the cross-stage contract)

`data_pipeline/schema.py` defines:

- **`ProblemSpec`** — a normalized, filter-passed problem (`id, question, domain,
  answer_type, gold_answer, gold_unit, dataset_source, meta`). Output of Phase 1.
- **`Trajectory`** — an execution-verified PoT sample for SFT: the `assistant`
  turn (short reason + code block), extracted `code`, the executed
  `exec_answer`/`exec_unit`/`exec_stdout`, the scorer verdict `is_correct` (must
  be `True`), and a `Provenance` block (`route`, `gen_model`, `temperature`,
  `retry_count`, ...). Provenance feeds the **Data Disclosure Document** — teacher
  (DeepSeek) data must be declared and must never reach inference.

Stages read/write JSONL via `write_jsonl` / `read_jsonl`.

## Phase 1 results (run 2026-06-01, `deepseek-v4-flash`)

`input/problems_all.jsonl` = **1671 ProblemSpecs** (BTC 1318 + Vietjack 353).
Combined domains: LDDT 538, CH 420, NL 236, TD 189, DDT 174, THCB 114.

- **BTC**: 1318 kept / 1352 (34 dropped — all legit: theory/definition Q's with no
  computable answer, or truly missing data/figure-refs). A first filter pass dropped
  70 but false-dropped resonance problems (Z=R / cosφ=1 / P=U²/R), so the prompt was
  given explicit physics guidance and the 70 were re-run → 36 reclaimed (incl. all 12
  resonance). Pass-1 audit preserved at `output/btc_dropped_pass1.jsonl`.
- **Vietjack**: 353 kept / 1947 (903 keyword pre-filter + 664 DeepSeek off-domain +
  26 unsolvable). lop-10 contributed **0** (all mechanics/thermo — off our 6 domains).
  Answers are **unverified** (`meta.answer_unverified=true`) — the Phase-2 execution
  gate is what validates them.
- Drop audits: `output/btc_dropped.jsonl`, `output/vietjack_dropped.jsonl`.

## Environments

Phase-1 data prep runs on a **lightweight local venv** (no torch/vLLM):
`uv venv && uv pip install openai python-dotenv numpy scipy sympy tqdm`.
Needs `DEEPSEEK_API_KEY` in `app/physics_solution/.env` (gitignored).

## Run

```bash
# Phase 0 (stdlib only)
PYTHONPATH=. python3 -m app.physics_solution.versions.v06_finetune.data_pipeline.extract_golden60

# Phase 1 (needs the venv + DEEPSEEK_API_KEY); auto-saves every 50, resumes on re-run
PYTHONPATH=. .venv/bin/python -m app.physics_solution.versions.v06_finetune.data_pipeline.btc_normalize --concurrency 12
PYTHONPATH=. .venv/bin/python -m app.physics_solution.versions.v06_finetune.data_pipeline.vietjack_normalize --grades 10 11 12 --concurrency 12
PYTHONPATH=. .venv/bin/python -m app.physics_solution.versions.v06_finetune.data_pipeline.combine
```

## Phase 2 — trajectory generation (Run)

Pipeline modules (`data_pipeline/`): `vllm_client` (async vLLM, `n`-sampling, thinking
off), `pot_common` (the execution gate — `verify`/`make_trajectory`/checkpoint, GPU-free
and reused by both routes), `selfgen` (Route 1), `teacher` (Route 2/3), `guards`
(spurious-reject + dedup + cap), `pot_smoke` (local harness test). Every stage
**auto-saves every 50 and resumes** by skipping ids already in its output (re-run without
`--fresh`) — interrupt-safe.

**0. Local pre-flight (no GPU):**
```bash
PYTHONPATH=. .venv/bin/python -m app.physics_solution.versions.v06_finetune.data_pipeline.pot_smoke
PYTHONPATH=. .venv/bin/python -m ...selfgen --stub --limit 30   # exercises loop/checkpoint/resume; clean up output/ after
```

**1. On Vast** (pull `main`; `scp app/physics_solution/.env` over for `DEEPSEEK_API_KEY`).
vLLM template serves Qwen on `:18000`; code execution needs scipy/sympy:
```bash
uv pip install --system scipy sympy   # numpy/pyyaml/openai/tqdm already in the template
curl -s http://localhost:18000/v1/models   # confirm the model id

# Route 1 — self-gen (GPU). Executes generated code on this box; never sees gold.
PYTHONPATH=. python -m ...selfgen --limit 20 --concurrency 32        # smoke first
PYTHONPATH=. python -m ...selfgen --concurrency 48                   # full run
#   -> output/trajectories_selfgen.jsonl  +  output/selfgen_residual.jsonl

# Route 2/3 — DeepSeek-pro teacher on the residual (API; runs here since .env is here)
PYTHONPATH=. python -m ...teacher --concurrency 8
#   -> output/trajectories_teacher.jsonl  +  output/teacher_failed.jsonl

# Step 4 — guards -> the final SFT set (+ audit + distribution report)
PYTHONPATH=. python -m ...guards --cap 4
#   -> output/trajectories_sft.jsonl  +  output/guards_rejected.jsonl
```

**2. Back to local** (Vast has no git → rsync the results):
```bash
rsync -avz -e "ssh -p <PORT>" \
  root@<HOST>:/root/project/app/physics_solution/versions/v06_finetune/output/ \
  app/physics_solution/versions/v06_finetune/output/
```

Notes: `selfgen` samples K=8 over temps `[0.2,0.5,0.8,1.0]`, retries **once on execution
error**, dedups by normalized-code hash, and stores all distinct correct samples (guards
does the per-problem cap). Qwen never sees gold; the teacher does (as a self-check target)
but `guards` rejects hardcoded/echoed answers. The gate is **value-level** (units are not
gated — too noisy). `teacher` uses `deepseek-v4-pro` (NOT flash). Vietjack's unverified
gold is validated here by construction (its trajectory only survives if executed code
matches the extracted gold).
