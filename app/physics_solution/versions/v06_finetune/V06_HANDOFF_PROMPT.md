# V06 Handoff Prompt

## Context: EXACT 2026 Physics Competition — v06: Data Generation + Fine-tune

I'm working on a physics problem-solving system for a competition. The system uses **Qwen 3.5 4B** to solve **English** physics problems (electrostatics, circuits, capacitors, energy, induction, measurement) by **generating and executing Python code**. The organizer's data is machine-translated from Vietnamese; everything competition-facing is English.

**v06 goal:** fine-tune Qwen so it natively emits **multi-step Program-of-Thought (PoT) trajectories** — `reason → Python → run → observe → … → FINAL ANSWER / UNIT` — without long prompts or few-shot examples, beating the v05_best baseline (58.3% on 60 golden, target >70%). The PoT format also feeds P2 (explanation) and P3 (cot + tool logs) scoring.

### What we have now (v05_best — current best)

**Pipeline:** Classify question → Generate Python code → Execute → Parse answer (60s timeout per question)

**v05_best accuracy: 35/60 golden = 58.3%** (with scorer bug fix applied)

**Key architectural decisions proven by experiment:**
1. **Simple, short prompts win for 4B models.** A verbose ToRA-style prompt (3620 chars, SETUP step, few-shot Q&A pairs) scored 48.3% with 23/60 timeouts. A simple direct prompt (~1200 chars, one inline code example) scored 58.3% with only 3 timeouts. The 4B model interprets verbose instructions like "SETUP (1-3 lines)" as permission to write extensive LaTeX reasoning, exhausting its token budget before generating code. **Implication for v06:** PoT is multi-step, but keep each step tight (short code + a brief reason line, not LaTeX walls) and watch the 60s budget.
2. **Hardcoded constants beat library imports.** `k = 9e9` in generated code is far more reliable than `k_e = 1 / (4 * const.pi * const.epsilon_0)` for a 4B model.
3. **`repetition_penalty=1.15`** in HuggingFace `generate()` breaks degenerate repetition loops.
4. **Retry once on execution error** by feeding error context back to the model.
5. **Formula hints per domain** (from `formulas.yaml`) injected into the codegen prompt help significantly.

**Solve method breakdown (60 golden questions):**
- `code_execution`: 52 (87%) — model generated valid code that ran successfully
- `failed`: 5 (8%) — code extraction or execution failed even after retry
- `timeout`: 3 (5%) — exceeded 60s budget
- All 60 golden questions are LDDT (electrostatics). Routing accuracy: 100%.

**v05_best prompt style (the computational core to preserve inside each PoT step):**
```
System: "You are a physics solver. Write a self-contained Python script..."
- Allowed imports: math, sympy, scipy.constants, numpy
- Define all given values at top with SI unit conversions
- Key formula as comment before each computation
- Print FINAL ANSWER: <value> and UNIT: <unit>

User: "DOMAIN: {domain}\nANSWER TYPE: {answer_type}\n\nREFERENCE:\n{formula_hints}\n\nPROBLEM:\n{question}\n\nWrite a Python script to solve this."
```

### Version history and error analysis

| Version | Prompt Style | Accuracy (60q) | Timeouts | Key Issue |
|---------|-------------|-----------------|----------|-----------|
| v05 old prompt | Direct + CoT fallback | 36/60 = 60.0% | few | Baseline |
| v05 code-first | Direct, no CoT | 28/60 = 46.7% | 16 | Removed CoT killed planning |
| v05 ToRA | Verbose SETUP + few-shots | 29/60 = 48.3% | 23 | Token bloat from verbose prompt |
| **v05_best** | **Simple direct + retry** | **35/60 = 58.3%** | **3** | **Current best** |

**Error patterns in v05_best (25 wrong of 60):**
- Most failures are LDDT (electrostatics with geometry) — wrong coordinate setup, wrong force/field decomposition, sign errors.
- 5 `failed`: model couldn't generate parseable code at all.
- 3 `timeout`: classification + codegen exceeded 60s.
- Some questions want text answers (e.g. `-2√2 q`) that pure code execution can't produce — no fallback for these yet.
- Classifier labels 48/60 as `text` but they're actually numeric — harmless now (codegen runs regardless) but watch it.

**Scorer bug fixed:** `_SCI_DOT_RE` in `scorer.py` falsely matched plain decimals like `957.1068` as `957 . 10^68`. Fixed by requiring `^`. Turned 1 FALSE into TRUE (LD083).

## DATA ASSETS — three sources, different roles (don't conflate them)

> **Two `data/` trees:** the pretrain corpora live at **repo-root** `data/`; the
> golden/test CSVs live at `app/physics_solution/data/`. Once the corpora are
> normalized they'll be moved under `app/physics_solution/data/` too.

| Path | What | Lang | Role | Status |
|---|---|---|---|---|
| `app/physics_solution/data/golden/deepseek-v4-pro_golden_data.csv` | 1,352 organizer (BTC) train rows (`id, question, cot, answer, unit`), DeepSeek-rewritten CoT | EN (translated from VN) | **SFT** | ready, but CoT must be converted into PoT code-gen trajectories |
| `data/pretrain_corpus/` | English physics textbooks (OpenStax, Giancoli, Young & Freedman, Fundamentals), 451 golden markdown across 4 schemas + `prepare_*.py` per source | EN | **Parked — was the CPT corpus; not used in v06 (SFT-only)** | complex multi-schema; left as-is for a possible future CPT experiment |
| `data/pretrain_processed/` | 2,261 QC'd Vietjack worked solutions (lớp 6–12); v06 uses **lớp 10–12** (physics-dense) | VN | **SFT** (after VN→EN + answer/unit extraction) | processed, format fairly good; needs translation + label extraction |

- `data/pretrain_corpus/DATA_CATALOG.md` — its `app/data/...` source paths are **stale**; real files live under `data/pretrain_corpus/<source>/{golden,processed}/`. This corpus was the CPT source; **v06 is SFT-only, so it's unused** (parked for a possible future CPT experiment).
- `data/pretrain_processed/DATA_CATALOG.md` — built from `data/vietjack_physics_spider/vietjack_physics_spider.rar` (74,807 raw → 2,261 after strict QC) via `scripts/filter_dataset.py` + `scripts/generate_catalog.py`. Figure/graph/table-dependent questions already removed. Grade skew: lớp 12 = 1,130, lớp 11 = 270, lớp 10 = 547.
- More Vietnamese data is being crawled and will be translated to English later (same reason the BTC set is VN→EN: expand the VN pool, then translate).

**Domain / answer-type distribution (BTC 1,352, for stratified split + balancing):**
- Domains: LDDT (electrostatics, 465 — hardest), CH/CHLT (AC/RLC circuits, 310; CHLT has yes_no), NL (energy/LC, 190), TD (capacitors, 177), DDT (induction/solenoids, 130), THCB (measurement/DC, 80; multi-value common).
- Answer types: numeric 72%, sci_notation 17.5%, text 3.7%, mixed 2.7%, multi_value 1.9%, yes_no 1.6%.

## DATA-PROCESSING PIPELINE (the heart of v06)

The task is fine-tuning a model to **generate code**. **v06 is SFT-only** — CPT is
dropped from scope (the `data/pretrain_corpus/` textbook corpus is parked for a
possible future experiment, not part of this plan). Nothing is SFT-ready as-is.

### SFT (code-gen, execution-verified)
Sources: **BTC golden + Vietjack (lớp 10–12)**, normalized to **one** format matching the BTC inference format. Strategy: **self-gen first, teacher residual**, with **multi-step PoT** targets, gated by execution.

**Step 0 — Filter first (DeepSeek).** Drop samples that reference a figure/image or are underspecified (unsolvable from text alone). Run this *before* any code-gen so we don't waste compute. (Vietjack already dropped figure-dependent ones; BTC may still have some.)

**Step 1 — Normalize / ingest.**
- BTC golden: already `(id, question, cot, answer, unit)` in EN — convert the CoT into PoT code-gen targets (Steps 2–3). Keep `answer`/`unit` as gold.
- Vietjack: needs (a) a **single VN→EN translation pass** (dedicated DeepSeek prompt, output shaped exactly like BTC `question`), and (b) **`answer`/`unit` extraction** — Vietjack's answer + unit are embedded in the solution text, not labeled fields. DeepSeek extracts them (and may consult them to write code), but we **still execute** and require the code's answer + unit to match the extracted gold via `scorer.py`.

**Step 2 — Route 1: self-gen (primary).** Sample multiple PoT trajectories from **Qwen 3.5 4B** at several temperatures (augmentation — any *correct method* counts). Execute; keep trajectories whose final answer matches gold via `shared/eval/scorer.py`. On-policy data → best convergence, least forgetting. **Self-gen sampling needs a GPU** (Vast AI vLLM endpoint), not the local box.

**Step 3 — Routes 2 & 3: teacher residual.** For problems Qwen can't solve in K samples, hand off to **DeepSeek (teacher)**: keep the correct prefix of Qwen's trajectory and let the teacher continue to a verified-correct trajectory in the same format. Failures retry with error feedback (consistent format). *v1 shortcut* if strict prefix-splicing is fiddly: give DeepSeek the problem + Qwen's failed attempt as a hint and have it write a full correct PoT trajectory.

**Step 4 — Guards (both routes).**
- Reject **spurious-correct** code (must *compute*, not echo/hardcode the gold) — important for yes_no / multi-choice / low-entropy numerics.
- Dedup; cap trajectories per problem (RFT over-produces easy problems); oversample rare domains (CHLT…).
- **Execution gate is universal:** run every script sandboxed via v05's `code_executor.py` (subprocess + allowed imports `math/sympy/numpy/scipy.constants` + timeout). Only execution-verified trajectories enter SFT.

**Step 5 — Split.** Stratify by domain AND answer_type. Train ~90% (oversample underrepresented domains); val ~10% that **MUST include the 60 golden questions** for direct comparison with v05_best.

> **Why this shape:** Route 1 (Qwen's own correct samples) is the highest-value data and directly mitigates the forgetting / distribution-shift risk of distilling a much larger teacher (DeepSeek ≫ 4B). Teacher data is confined to the residual Qwen can't reach. Consider iterating **ReST-EM style** later: after the first SFT, re-run Route 1 from the improved model so self-gen covers more and teacher shrinks.

### Phase F — Fine-tuning (SFT)
- Base: **stock Qwen 3.5 4B** (no CPT warm-up in v06).
- Unsloth LoRA/QLoRA. Anti-forgetting: LoRA (not full-FT), low LR, ≤ a few epochs, optionally mix in a little general/instruction data. Start rank=16, lr=2e-4, ~3 epochs.
- Training format: Qwen chat template. System = shortened CODEGEN system (drop the inline example — the model will have learned the pattern). User = `DOMAIN / ANSWER TYPE / REFERENCE (formula hints) / PROBLEM / Write a Python script to solve this.` Assistant = the verified PoT trajectory.
- Formula hints (`formulas.yaml`) still injected at inference; few-shot + verbose system text removed.

### Phase G — Inference pipeline
- Adapt v05_best's `run.py` / `pipeline.py` for the fine-tuned model: shorter system prompt, same retry-on-error, same formula-hint injection, same execution + scoring. Target >70% on 60 golden.

## WHERE EACH STEP RUNS

| Step | Machine | Notes |
|---|---|---|
| Data prep (orchestration, DeepSeek teacher/translate/filter, run+score code) | **Local WSL box** | No local GPU. DeepSeek via `config.py` (`COMMERCIAL_PROVIDER=deepseek`, `COMMERCIAL_MODEL=deepseek-v4-pro`, key `DEEPSEEK_API_KEY`, base `https://api.deepseek.com`). |
| Route-1 Qwen self-gen sampling | **Vast AI** (vLLM endpoint) | Sampling 4B needs a GPU. |
| Training (SFT) | **Vast AI** (A100 / RTX 6000) | Unsloth LoRA/QLoRA. |
| Inference + scoring | **Vast AI** (vLLM template) | `README_GPU_SETUP.md`. |

**All GPU work is on Vast AI** (training, self-gen, serving) — one environment for consistency; setup in `README_GPU_SETUP.md`.

*Fallback (optional):* you can also SSH into a Colab GPU over Tailscale — `ssh -o StrictHostKeyChecking=no root@<tailscale-ip>` (root IP rotates each session, user provides it) → `cd /content/`. It's a generic Linux GPU box with **no preinstalled vLLM template** (prepare a setup script locally: uv, vLLM, deps; SSH in; run it). Prefer Vast AI.

### Technical constraints
- Competition: model ≤8B total params, self-host with vLLM, ≤60s/request, sequential models only, no 3rd-party inference APIs at inference, code execution allowed/encouraged. Use dataset `EXACT2026_dataset_2026-05-15` (1,352 valid rows).
- External/synthetic data (DeepSeek) allowed for **training only** — declare in the Data Disclosure Document; never at inference.
- Existing async DeepSeek batching: `shared/eval/gen_golden.py` — adapt for code-gen / translation / filtering.
- Code execution for verification: reuse `code_executor.py` (subprocess, 10s timeout, allowed imports only).

### Key files
- `docs/strategy/TYPE2_PHYSICS.md`, `docs/eda/TYPE2_PHYSICS_EDA.md` — strategy + EDA
- `docs/guides/{UNSLOTH,PRETRAIN_DATA,DATA_COLLECTION}_GUIDE.md` — Unsloth/LoRA + data background (the old Colab-notebook training flow is superseded — all GPU work runs on Vast AI now)
- `app/physics_solution/versions/v05_best/{prompts.py,code_executor.py,formula_kb.py,run.py,input/formulas.yaml,output/results_golden_60.json}` — the working baseline to build on
- `app/physics_solution/shared/{model/loader.py,model/batched_llm.py,eval/scorer.py,router.py,eval/gen_golden.py}` — shared infra
- `app/physics_solution/config.py`, `app/physics_solution/cli/inference.py` — central config + dispatcher

### What I need from you
> Data is collected, not finetune-ready. You are building the **processing + training** pipelines, not collecting data.

1. **Create the v06 pipeline scaffolding** under `app/physics_solution/versions/v06_finetune/`.
2. **SFT data pipeline:** filter → normalize (incl. Vietjack VN→EN + answer/unit extraction) → Route-1 self-gen (Qwen, multi-temp, execution-verified) → Route-2/3 teacher residual (DeepSeek) → guards → stratified split (val includes the 60 golden).
3. **SFT training (Unsloth/QLoRA)** + an eval script comparing the fine-tuned model vs v05_best on golden.
4. **Inference pipeline** adapted from v05_best for the fine-tuned model.

Start by reading the key files to understand the full context, then create a plan before coding.

---
