# V06 Handoff Prompt
> Copy the prompt below (between the `---` markers) into a new Claude session.

---

## Context: EXACT 2026 Physics Competition — v06: Data Generation + Fine-tune

I'm working on a physics problem-solving system for a competition. The system uses **Qwen 3.5 4B** to solve Vietnamese-translated-to-English physics problems (electrostatics, circuits, capacitors, energy, induction, measurement) by generating and executing Python code.

### What we have now (v05_best — current best)

**Pipeline:** Classify question → Generate Python code → Execute → Parse answer (60s timeout per question)

**v05_best accuracy: 35/60 golden = 58.3%** (with scorer bug fix applied)

**Key architectural decisions proven by experiment:**
1. **Simple, short prompts win for 4B models.** A verbose ToRA-style prompt (3620 chars, SETUP step, few-shot Q&A pairs) scored 48.3% with 23/60 timeouts. A simple direct prompt (~1200 chars, one inline code example) scored 58.3% with only 3 timeouts. The 4B model interprets verbose instructions like "SETUP (1-3 lines)" as permission to write extensive LaTeX reasoning, exhausting its token budget before generating code.
2. **Hardcoded constants beat library imports.** `k = 9e9` in generated code is far more reliable than `k_e = 1 / (4 * const.pi * const.epsilon_0)` for a 4B model.
3. **`repetition_penalty=1.15`** in HuggingFace `generate()` breaks degenerate repetition loops.
4. **No fallback to direct LLM text solve.** When code extraction fails (no ```python block), we give up. When code execution errors, we retry once by feeding error context back to the LLM.
5. **Formula hints per domain** (from `formulas.yaml`) are injected into the codegen prompt and help significantly.

**Solve method breakdown (60 golden questions):**
- `code_execution`: 52 (87%) — model generated valid code that ran successfully
- `failed`: 5 (8%) — code extraction or execution failed even after retry
- `timeout`: 3 (5%) — exceeded 60s budget
- All 60 golden questions are in the LDDT domain (electrostatics). Routing accuracy: 100%.

**v05_best prompt style (this is what works):**
```
System: "You are a physics solver. Write a self-contained Python script..."
- Allowed imports: math, sympy, scipy.constants, numpy
- Define all given values at top with SI unit conversions
- Key formula as comment before each computation
- Print FINAL ANSWER: <value> and UNIT: <unit>
- One inline code example (Coulomb's law, 8 lines)
- ~1200 chars total

User: "DOMAIN: {domain}\nANSWER TYPE: {answer_type}\n\nREFERENCE:\n{formula_hints}\n\nPROBLEM:\n{question}\n\nWrite a Python script to solve this."
```

### Version history and error analysis

| Version | Prompt Style | Accuracy (60q) | Timeouts | Key Issue |
|---------|-------------|-----------------|----------|-----------|
| v05 old prompt | Direct + CoT fallback | 36/60 = 60.0% | few | Baseline |
| v05 code-first | Direct, no CoT | 28/60 = 46.7% | 16 | Removed CoT killed planning |
| v05 ToRA | Verbose SETUP + few-shots | 29/60 = 48.3% | 23 | Token bloat from verbose prompt |
| **v05_best** | **Simple direct + retry** | **35/60 = 58.3%** | **3** | **Current best** |

**Error patterns in v05_best (25 wrong answers out of 60):**
- Most failures are in LDDT (electrostatics with geometry) — wrong coordinate setup, wrong force/field direction decomposition, sign errors
- 5 `failed` questions: model couldn't generate parseable code at all
- 3 `timeout` questions: classification + codegen exceeded 60s
- Some questions require text answers (e.g., `-2√2 q`) that code execution can't produce — v05_best has no fallback for these
- Answer type routing issue: classifier labels 48/60 questions as `text` but they are actually numeric — the codegen prompt still works because it generates Python regardless, but this mis-classification could cause problems in future versions

**Scorer bug fixed:** `_SCI_DOT_RE` regex in `scorer.py` had optional `^` that falsely matched plain decimals like `957.1068` as `957 . 10^68`. Fixed by requiring `^`. This turned 1 FALSE into TRUE (LD083).

### Key files to read for full context

**Strategy & data:**
- `docs/strategy/TYPE2_PHYSICS.md` — Competition strategy, constraints (model ≤8B, 60s timeout, self-host with vLLM)
- `docs/eda/TYPE2_PHYSICS_EDA.md` — EDA of 1,352-row training dataset: domain distribution, answer types, data quality
- `docs/guides/PRETRAIN_DATA_GUIDE.md` — how the pre-training corpus was scoped/collected
- `docs/guides/DATA_COLLECTION_GUIDE.md` — how the fine-tune data was scoped/collected
- `docs/guides/UNSLOTH_GUIDE.md` — LoRA/QLoRA fine-tuning with Unsloth on Colab
- `EXACT_Materials/Datasets/EXACT2026_dataset_2026-05-15/Physics_Problems_Text_Only/Physics_Problems_Text_Only.csv` — The 1,352-row training dataset (id, question, cot, answer, unit)
- `app/physics_solution/data/golden/deepseek-v4-pro_golden_data.csv` — 1,352 rows of DeepSeek-rewritten CoT (already generated)
- **`data/pretrain_processed/`** — READY CPT corpus: 2,261 Vietnamese worked solutions (`lop-6…12_high_quality.md`) + `DATA_CATALOG.md`
- **`data/vietjack_physics_spider/vietjack_physics_spider.rar`** — raw spider archive (74,807 samples before filtering)
- `scripts/filter_dataset.py`, `scripts/generate_catalog.py` — QC filter + catalog generation for the pretrain corpus

**v05_best implementation (the working baseline to build on):**
- `app/physics_solution/versions/v05_best/__init__.py` — Version metadata
- `app/physics_solution/versions/v05_best/prompts.py` — **The prompt that works:** CODEGEN_SYSTEM (~1200 chars), CLASSIFY_SYSTEM, `build_codegen_prompt()`
- `app/physics_solution/versions/v05_best/code_executor.py` — Code extraction + subprocess execution + answer parsing
- `app/physics_solution/versions/v05_best/formula_kb.py` — Formula hints per domain with hardcoded constants (k=9e9, epsilon_0, etc.)
- `app/physics_solution/versions/v05_best/input/formulas.yaml` — Domain formula definitions
- `app/physics_solution/versions/v05_best/run.py` — Full pipeline: classify → codegen → execute → retry on error → score
- `app/physics_solution/versions/v05_best/output/results_golden_60.json` — Latest results with per-question detail

**Shared infrastructure:**
- `app/physics_solution/shared/model/loader.py` — Model loading + generation (repetition_penalty=1.15)
- `app/physics_solution/shared/model/batched_llm.py` — HFBatchedLLM wrapper, Qwen3.5 thinking mode disabled
- `app/physics_solution/shared/eval/scorer.py` — Multi-type scoring (numeric, sci_notation, yes_no, multi_value, text, mixed)
- `app/physics_solution/shared/router.py` — Question classifier (domain + answer_type)
- `app/physics_solution/shared/eval/gen_golden.py` — Existing async batch API calls to DeepSeek (can be adapted)
- `app/physics_solution/config.py` — Central config: DeepSeek V4 Pro API, model IDs, paths
- `app/physics_solution/cli/inference.py` — CLI dispatcher (v05_best already registered)

### DATA ASSETS — NOW READY (merged from main, 2026-05-30)

Two data sources have been collected and processed. They live in the repo:

**1. Pre-training corpus (for Continue Pre-Training / CPT)** — `data/pretrain_processed/`
- **2,261 high-quality Vietnamese worked solutions** filtered from 74,807 raw scraped samples (3.02% retention after strict QC).
- Source: Vietjack physics (lớp 6–12 essay/MCQ problems with full solutions).
- Per-grade markdown: `lop-6_high_quality.md` … `lop-12_high_quality.md`. Catalog: `data/pretrain_processed/DATA_CATALOG.md`.
- Grade distribution skews to upper grades: lớp 12 = 1,130, lớp 11 = 270, lớp 10 = 547 (these are the physics-dense grades matching our electrostatics/circuits domains).
- Format: each problem is a self-contained markdown block — `## Problem` → `**Question:**` → `### Solution` (Vietnamese reasoning + formulas).
- QC rules already applied: solution >200 chars, must contain numbers + math operators + reasoning keywords ("Ta có", "Áp dụng", "Suy ra"); **figure/graph/table-dependent questions removed** (no visual context for the model); MCQ noise stripped.
- Raw spider archive: `data/vietjack_physics_spider/vietjack_physics_spider.rar`. Filter script: `scripts/filter_dataset.py`, catalog gen: `scripts/generate_catalog.py`.
- **Intended use:** raw-corpus CPT to strengthen the model's Vietnamese physics reasoning/computation BEFORE SFT. NOT directly SFT-ready (it's a corpus, not instruction/response pairs).

**2. Fine-tune CoT data** — `app/physics_solution/data/golden/`
- `deepseek-v4-pro_golden_data.csv` — 1,352 rows of DeepSeek-rewritten CoT (id, question, cot, answer, unit).
- Plus the original `Physics_Problems_Text_Only.csv` (1,352 rows) as ground truth.
- These feed Phase 1 code-generation: DeepSeek writes Python for each, we execute + verify against gold.

**This v06 branch (`Nguyen/v06_finetune`) focuses on:** data processing → DeepSeek LLM normalization → code generation → CPT + SFT fine-tuning. Inference-pipeline polish stays minimal (reuse v05_best).

### What v06 needs to do

**Goal:** (a) Optionally **continue-pretrain (CPT)** Qwen 3.5 4B on the 2,261-sample Vietnamese physics corpus to deepen reasoning, then (b) generate high-quality code-generation training data for ALL 1,352 questions using DeepSeek V4 Pro API, then (c) **fine-tune (SFT)** so the model natively produces clean, correct Python code matching the v05_best prompt style — without needing long prompts or few-shot examples at inference time.

**Critical lesson from v05 experiments: The fine-tuned model must learn to generate SHORT, DIRECT Python code.** Do NOT train it on verbose SETUP+reasoning patterns — the 4B model's token budget is too small. The training data format should match what v05_best's simple prompt produces: imports → given values with SI conversions → formula comments → computation → print FINAL ANSWER + UNIT.

**Phase 0: Continue Pre-Training (CPT) — optional but recommended**
1. Data is READY: `data/pretrain_processed/lop-*.md` (2,261 samples). No collection needed.
2. Concatenate the per-grade markdown into a plain-text corpus (one document per `## Problem` block; keep Vietnamese reasoning intact).
3. Light packing: tokenize with the Qwen tokenizer, pack into ~2k-token sequences, mask nothing (standard causal LM objective).
4. Train with Unsloth in CPT mode (LoRA on a wider module set than SFT, lower LR, 1 epoch is usually enough on 2k samples). Keep it cheap — this is a warm-up, not the main event.
5. Save the CPT adapter/merged weights as the BASE for Phase 3 SFT. If CPT doesn't move golden accuracy, skip it and SFT from stock Qwen.

**Phase 1: Data Generation**
1. Use DeepSeek V4 Pro API (already configured in `config.py`: `COMMERCIAL_PROVIDER = "deepseek"`, `COMMERCIAL_MODEL = "deepseek-v4-pro"`, API key in env var `DEEPSEEK_API_KEY`). Input rows are READY in `app/physics_solution/data/golden/deepseek-v4-pro_golden_data.csv`.
2. For each of the 1,352 questions, generate a Python solution that:
   - Uses only `import math`, `import sympy`, `import numpy`, or `from scipy import constants`
   - Defines all given values at top with SI unit conversions
   - Has formula comments before computations
   - Prints exactly `FINAL ANSWER: <value>` and `UNIT: <unit>`
   - Uses hardcoded constants where possible (k=9e9, epsilon_0=8.854e-12, etc.)
   - Is SHORT — aim for 15-30 lines, not 50+
3. Execute each generated code and verify the answer matches the gold answer (using `scorer.py`)
4. Smart retry logic: if code errors or answer doesn't match gold, retry with error feedback (like v05_best does)
5. Flag unrepairable mismatches for manual review
6. Domain-specific considerations:
   - LD/DT → LDDT (465 rows): Electrostatics — coordinate setup, vector decomposition, Coulomb's law. Hardest domain.
   - CH/CHLT (310 rows): AC/RLC circuits — impedance, resonance, phase. Include yes_no for CHLT.
   - NL (190 rows): Energy, power, LC oscillations
   - TD (177 rows): Standalone capacitor calculations
   - DDT (130 rows): Electromagnetic induction, solenoids
   - THCB (80 rows): Measurement errors, basic DC circuits. Multi-value answers common.
7. Handle answer types: numeric (72%), sci_notation (17.5%), text (3.7%), mixed (2.7%), multi_value (1.9%), yes_no (1.6%)

**Phase 2: Data Processing & Splitting**
- Parse and validate all generated solutions (code executes, answer matches gold)
- Stratified split by domain AND answer_type
- Training: ~90% (oversample underrepresented domains like CHLT with 20 rows)
- Validation: ~10% (must include the 60 golden test questions for direct comparison with v05_best)

**Phase 3: Fine-tuning (SFT)**
- Base: the Phase 0 CPT weights if CPT helped, otherwise stock Qwen 3.5 4B
- Model: Qwen 3.5 4B, LoRA/QLoRA with Unsloth
- GPU: RTX 3090/4090 (24GB) or A100 on Colab
- Training format: Qwen chat template with:
  - System message: shortened CODEGEN_SYSTEM (remove the inline example — the model will have learned the pattern)
  - User message: `DOMAIN: {domain}\nANSWER TYPE: {answer_type}\nREFERENCE:\n{formula_hints}\nPROBLEM:\n{question}\nWrite a Python script to solve this.`
  - Assistant message: the generated Python code solution (the DeepSeek output)
- The fine-tuned model still needs formula hints injected at inference time (domain-specific from `formulas.yaml`)
- But few-shot examples and verbose system prompts can be REMOVED — the model will have internalized the code-generation pattern
- Key hyperparameters to tune: LoRA rank, learning rate, epochs (start with rank=16, lr=2e-4, 3 epochs)

**Phase 4: Inference pipeline**
- Adapt v05_best's `run.py` for the fine-tuned model
- Shorter system prompt (no inline example needed)
- Same retry-on-error logic
- Same formula hints injection
- Same code execution + scoring pipeline
- Target: >70% on 60 golden questions (up from 58.3%)

### Technical constraints
- DeepSeek V4 Pro API: see `config.py` for all connection details
- Existing `gen_golden.py` already does async batch API calls to DeepSeek — can be adapted for code generation
- Python code execution for verification: `code_executor.py` (subprocess with 10s timeout, allowed imports only)
- Competition deadline: Phase 1 eval Jun 1-2, Phase 2 Jun 5-7
- vLLM for production inference (model must be HF-compatible)

### What I need from you

> Data is already collected — both the CPT corpus (`data/pretrain_processed/`) and the fine-tune CoT rows (`app/physics_solution/data/golden/`). You are NOT collecting data; you are processing it and building pipelines.

1. **Create v06 directory structure** (`app/physics_solution/versions/v06_finetune/`)
2. **(Optional) Build the CPT pipeline:**
   - Concatenate `data/pretrain_processed/lop-*.md` into a packed plain-text corpus
   - Unsloth CPT (causal LM, LoRA, low LR, ~1 epoch) → save weights as SFT base
   - Quick A/B: does CPT base beat stock Qwen on golden? If not, skip and SFT from stock.
3. **Build the code-gen data pipeline (DeepSeek normalization):**
   - Script to generate Python solutions via DeepSeek V4 Pro API for all 1,352 questions (input rows ready in `deepseek-v4-pro_golden_data.csv`)
   - Prompt for DeepSeek that produces SHORT, direct Python code (matching v05_best output style)
   - Execution + verification pipeline (run code, compare with gold answer via scorer)
   - Retry logic for failed/mismatched answers
   - Output: verified `(question, domain, answer_type, formula_hints, python_code, answer, unit)` tuples
4. **Build the data processing pipeline:**
   - Validate all generated solutions
   - Stratified train/val split (val MUST include the 60 golden questions)
   - Convert to Qwen chat template format for fine-tuning
5. **Build the SFT fine-tuning pipeline:**
   - Unsloth/QLoRA setup for Qwen 3.5 4B (base = CPT weights or stock)
   - Training script with proper hyperparameters
   - Evaluation script to compare fine-tuned model vs v05_best on golden data
6. **Build the inference pipeline for the fine-tuned model** (adapted from v05_best's `run.py` with shorter prompts)

Start by reading the key files listed above to understand the full context, then create a plan before coding.

---
