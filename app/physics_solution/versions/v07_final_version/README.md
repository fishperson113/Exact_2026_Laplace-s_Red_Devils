# v07 — final version (self-SFT → train → submit)

Authoritative doc for everything from **self-SFT data generation onward**. The data prep +
QC steps are **done**; this supersedes `versions/v06_finetune/README.md` and
`V06_HANDOFF_PROMPT.md` (both deprecated — they predate the current architecture).

Goal: SFT **Qwen3.5-4B** so it natively emits a **short reasoning (5–10 lines) then ONE
Python code block** that computes the answer — beating v05_best (58.3% on the 60 golden;
target >70%). Keep it lean — **no over-engineering**.

---

## ⏱ Progress (2026-06-07)

**Steps A–D done; E modules built + smoke-tested.** A–C (data-gen) built the trajectory set;
D (build_sft) wrote `output/{train,val}.jsonl` (chat-message, golden held out — §0); **E (train)
modules are built and smoke-passed on a Colab A100-40G** (Unsloth loads Qwen3.5-4B `qwen3_5` on
tf5, `train_on_responses_only`, eval_loss, save adapter — all green). Next: the **full SFT run**
(3 epochs) + merge/push + accuracy eval.

**Proven environment (don't re-derive):** Qwen3.5-4B needs **transformers ≥ 5.5.0** (4.57.x only
has `qwen3_next`; the model ships no remote code) + **unsloth 2026.5.6 / torch 2.10 / trl 0.24 /
peft 0.19** — exactly the FOL model's pins, copied to `colab_setup/requirements.txt`.
**fla/causal-conv1d are NOT required** (torch fallback; installed best-effort only). Run via the
isolated venv `/content/v07_env`. See `colab_setup/`.

The clean SFT data:
```
app/physics_solution/versions/v07_final-version/input/trajectories_sft.jsonl
```
- **2846 trajectories · 1505 / 1584 problems (95%)** · all v06 format (5–10 line reasoning +
  ONE code block) · execution-verified.
- Cap = **2 diverse** solves/problem (`guards --cap 2 --select diverse`): the cleanest solve
  (on-policy, lowest temp) + the most code-different valid solve. Histogram `{1:164, 2:1341}`.
- Routes: `self_gen` 2291 + `self_gen_hinted` 555 (the old DeepSeek-teacher route is gone).
- Each row carries: `id, source_id, question, domain, answer_type, gold_answer, gold_unit,
  dataset_source, assistant` (reasoning+code text), `code`, `provenance{route,gen_model,
  temperature,retry_count,hint_source}`. **For SFT, the target = the `assistant` field**
  (system=`GEN_SYSTEM`, user=problem block).
- 79 problems unsolved (`output/hinted_failed.jsonl`): 51 have no hint (unsolvable from text),
  28 had a hint but still failed — acceptable, not in the SFT set.

How it was built (for the record, don't re-run unless regenerating): `selfgen --k 4
--concurrency 64` → `hinted --concurrency 64` → `guards --cap 2 --select diverse`, all with
`VLLM_MODEL=physics` on the Vast box (tuned vLLM: `MAX_NUM_SEQS=64 ENFORCE_EAGER=0`).

---

## 0. The source dataset (data-gen input — A–C done, kept for reference)

```
app/physics_solution/versions/v06_finetune/input/self_gen_dataset.jsonl
```
**1584** QC-clean problems (the canonical problem set; **don't duplicate it**). Each row:
```json
{"id","question","domain","answer_type","gold_answer","gold_unit","dataset_source",
 "hint_code","hint_source"}
```
- `question` is the cleaned statement (corrupted ones were fixed or dropped during QC).
- `hint_code` (1550/1584 have one) = a verified reference solve (DeepSeek/Claude) used **only**
  as a method hint for the hinted route — external data, **declare in the Data Disclosure Doc**,
  never shown at inference.

**Validation set:** [val_56.jsonl](val_56.jsonl) — 56 stratified problems (6 domains ×
4 answer types). **Rebuilt by `make_val.py`** (2026-06-07): the original 56 went stale —
17 of them were dropped by the execution QC (no trajectory → no eval-loss signal). Those 17
are replaced with same-`(domain, answer_type)` problems that **do** have a trajectory and are
**not** in golden_60 (deterministic by sorted id). Every val problem now has ≥1 trajectory.

**Split (honest eval), done in `build_sft.py`:**
- `source_id ∈ golden_60` → **DROPPED** from the SFT files (102 traj). 56/60 golden have
  trajectories; training on them would contaminate the golden score. Golden is the held-out
  test, evaluated by *running* the model on `golden_60.csv` (CLAUDE.md mandates holding it out).
- `source_id ∈ val_56` → `output/val.jsonl` (eval-loss + accuracy).
- otherwise → `output/train.jsonl`.

Result: **train 2634 traj / 1393 problems · val 110 traj / 56 problems** (leak-guarded:
train ∩ val = train ∩ golden = ∅).

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
| **A. self-gen** (Route 1) | `data_pipeline/selfgen.py` | Qwen multi-temp → reasoning+code → execute → keep correct (dedup); retry once on a code error and keep only the **clean final** reasoning+code. Too few correct (`--min-keep`) → residual. | ✅ **done** |
| **B. hinted** (residual) | `data_pipeline/hinted.py` | For the residual, show Qwen the `hint_code` as a METHOD reference; Qwen re-derives its OWN reasoning+code → execute-verify. **No API.** On-policy. | ✅ **done** |
| **C. guards** | `data_pipeline/guards.py` | spurious-reject (echo/hardcode) + dedup + cap **2 diverse/problem** (`--select diverse`: cleanest + most code-different). → `input/trajectories_sft.jsonl` | ✅ **done** |
| **D. build_sft** | `v07_final_version/{make_val,build_sft}.py` | `make_val.py` rebuilds val_56 (dropped/golden-safe); `build_sft.py` splits by val ids, drops golden, → `output/{train,val}.jsonl` as chat `messages` (system=`GEN_SYSTEM`, user=PLAIN problem block, assistant=`assistant` field). | ✅ **done** |
| **E. SFT train** | `v07_final_version/train/` + `colab_setup/` | Unsloth QLoRA on `train.jsonl` (token-CE, train-on-completion, prompt masked); save adapter+tokenizer → merge → push **adapter + merged** to Hub w/ metrics card (`merge_push.py`); eval via `eval.py`. | 🟡 **built + smoke-passed; full run pending** |
| **F. inference + explanation/cot** | `v07_final_version/` (to build) | see §3 | ⏳ todo |

**A–C already ran** (see Progress block at top). The exact commands used, for regeneration only:
```bash
# on Vast box (tuned vLLM on :18000, served name = physics)
VLLM_MODEL=physics PYTHONPATH=. python -m ...data_pipeline.selfgen --k 4 --concurrency 64
VLLM_MODEL=physics PYTHONPATH=. python -m ...data_pipeline.hinted  --concurrency 64
VLLM_MODEL=physics PYTHONPATH=. python -m ...data_pipeline.guards  --cap 2 --select diverse
```
Outputs live in `v06_finetune/output/`; the SFT set is copied to `v07_final-version/input/trajectories_sft.jsonl`.

### E note — save LoRA so it reloads *exactly* (don't skip this)
The submission serves via vLLM, so the trained weights MUST reload deterministically. Drive
training from a **YAML config** (model / lora / training / eval / hub sections — copy the shape
of [`Logic_Based_Educational_Queries_Project/configs/qa_model.yaml`](../../../../Logic_Based_Educational_Queries_Project/configs/qa_model.yaml)).
On finish: save the **LoRA adapter + tokenizer** to a versioned dir AND **merge-and-save** a
full model (vLLM serves the merged model cleanly), then **push both to the Hub**
(`Laplaces-Red-Devils/...`, the org used in `app/core/config.py`). Record base-model id, LoRA
rank/alpha/target_modules, and the exact chat template in the config so loading is reproducible.

> **Code location:** the folder was **renamed** `v07_final-version` → **`v07_final_version`**
> (underscore) so this one importable package holds the README/data AND the runnable Python.
> Add it to the `VERSIONS` dict in `cli/inference.py` if you wire a batch eval. Data-gen modules
> stay in `v06_finetune/data_pipeline/` (reused, don't move).

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
v07_final_version/                 # one importable package: docs + data + code
├── README.md                      # this file (authoritative)
├── __init__.py
├── val_56.jsonl                   # the 56-problem validation set (rebuilt; split key)
├── make_val.py                    # D-pre: rebuild val_56 (drop-stale + golden-safe)  ✅
├── build_sft.py                   # D: split → output/{train,val}.jsonl (chat messages)  ✅
├── eval.py                        # F-pre: accuracy on val_56 + golden_60 (run→exec→score)  ✅
├── input/
│   └── trajectories_sft.jsonl     # ✅ THE SFT data — 2846 traj / 1505 problems
├── output/                        # ✅ train.jsonl (2634) + val.jsonl (110)
├── train/                         # E: Unsloth QLoRA  ✅ (smoke-passed)
│   ├── sft_model.py               #   Unsloth load qwen3_5 + LoRA (tf5 flex-attn/tokenizer fixes)
│   ├── sft_data.py                #   messages → chat-template text
│   ├── train.py                   #   SFTTrainer + train_on_responses_only + save + merge/push
│   ├── merge_push.py              #   PEFT merge (CPU) + push adapter & merged + metrics card
│   └── configs/sft.yaml           #   single source of truth for hyperparams/hub
├── colab_setup/                   # E: how to run on Colab  ✅
│   ├── requirements.txt           #   proven pins (torch2.10/tf5.5/unsloth2026.5.6)
│   ├── setup_colab.sh             #   uv venv /content/v07_env + install + best-effort fla/conv1d
│   ├── train_v07.ipynb            #   notebook to copy onto the Colab notebook (logs each step)
│   └── README.md                  #   environment notes + gotchas
└── explain.py                     # F: explanation + cot writer pass (todo)
```
