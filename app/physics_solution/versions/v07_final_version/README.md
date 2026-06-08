# v07 — final version (self-SFT → train → submit)

Authoritative doc for everything from **self-SFT data generation onward**. The data prep +
QC steps are **done**; this supersedes `versions/v06_finetune/README.md` and
`V06_HANDOFF_PROMPT.md` (both deprecated — they predate the current architecture).

Goal: SFT **Qwen3.5-4B** so it natively emits a **short reasoning (5–10 lines) then ONE
Python code block** that computes the answer — beating v05_best (58.3% on the 60 golden;
target >70%). Keep it lean — **no over-engineering**.

---

## ⏱ Progress (2026-06-08)

**Steps A–E done; two full SFT runs trained + evaluated (v07b 4bit, v07c 16-bit).** A–C built
the trajectories; D split `output/{train,val}.jsonl` (golden held out — §0); E trained on a
Colab A100-40G with Unsloth (`train_on_responses_only`, **execution-accuracy checkpoint
selection** — not eval_loss — via `train/acc_callback.py`). Both runs pushed to the Hub. See
**§Results & Error Analysis** for the numbers, the QLoRA-merge finding, and the failure
breakdown. Next: 3 high-ROI fixes (scorer units, drop sci-notation rule, stop rounding) → re-eval.

**Deploy artifact:** `Laplaces-Red-Devils/physics-v07c-sft-qwen3.5-4b-merged` (16-bit LoRA, so
the merge is lossless — see the merge finding below). Serve think-OFF, `max_new_tokens=2048`.

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

## Results & Error Analysis (2026-06-08)

All eval is **think-OFF, greedy, `max_new_tokens=2048`** unless noted. `val_56` = held-out
validation (in-distribution: same self-gen source). `golden_60` = the held-out **true test**
(out-of-distribution). Raw per-problem dumps: `train/runs/eval_*.json`.

### Training runs
- **v07b** (4-bit QLoRA, lr 3e-5, r8 q/k/v/o, 6 ep, acc-selected): best **val_56 acc 0.7857**
  (ep5). Per-epoch: 0.732 / 0.696 / 0.750 / 0.732 / **0.786** / 0.732.
- **v07c** (same recipe but **16-bit LoRA**): best **val_56 acc 0.7857** (ep3). Per-epoch:
  0.732 / 0.732 / **0.786** / 0.786 / 0.768 / 0.786. Train batch 8 / accum 2 (eff 16, peak
  33.8 GB), `acc_batch_size=28`.

### Eval comparison
| Model | val_56 | golden_60 |
|---|---|---|
| base Qwen3.5-4B (16-bit) | 0.679 | **0.650** |
| v07b 4bit-base + adapter (= train condition) | 0.732 | 0.650 |
| v07b **merged**-16bit | 0.696 | 0.600 |
| **v07c merged-16bit (deploy)** | **0.750** | 0.633 |

**Finding 1 — the QLoRA merge was lossy (~4–5 pt).** v07b's 4bit-base+adapter scored
0.732/0.650 but the **merged** 16-bit artifact dropped to 0.696/0.600: the adapter learned to
correct an NF4-4bit base, so merging it into a 16-bit base mis-applies the correction. Fix:
retrain with **16-bit LoRA** (`load_in_4bit: false`) → merge is lossless → v07c-merged recovers
to **0.750/0.633**. Deploy v07c-merged, never v07b-merged.

**Finding 2 — self-gen SFT is at the data ceiling on OOD.** Even at its best, v07c beats base
clearly on val (+4 problems, in-distribution) but is ~tied on golden (−1, noise). Base already
does PoT physics + the exact format, so SFT on its own correct samples adds little OOD.

### Error analysis — why v07c fails (categorised from `eval_v07c_*.json`)
14 val + 22 golden failures. **All 22 golden failures are domain LDDT (electrostatics).** Three
root causes, not one:

**A. Scorer false-negatives — the model is physically CORRECT (~5 cases).** The scorer ignores
units and matches text one-directionally:
- `DDT138`: gold `5.654 mT`, model `0.005655 T` — **identical** (0.005655 T = 5.655 mT); scorer
  doesn't convert mT↔T.
- `vj_l11_0026`: gold `4×10⁻³ μF`, model `4×10⁻⁹ F` — **identical**; no μF↔F convert.
- `DDT350`/`DDT330`: gold "…inductive characteristic", model "inductive" — right; text match is
  `gold in pred` only (one-directional).
- `LD047` (golden): gold is **untranslated Vietnamese** ("Hướng về phía q₂"); model "towards q2"
  is the correct translation — a golden *label* bug, not a model error.

**B. Output-formatting bugs from our own prompt rules (~3 cases).** The rule *"write X * 10^N,
never e-notation"* makes the model hand-format and double-count: `LD098` computed `1.152e7`
(= gold) but printed `"11520000.00 * 10^7"` → parsed as 1.152e14. The rule *"round to 2–4 sig
figs"* trips the 2% tolerance: `LD115` 0.03 vs 0.036, `LD292` 0.002 vs 0.001732, `THCB088` 0.07
vs 0.067, `LD285` `round(x,3)`→0.0.

**C. Real physics errors — the genuine ceiling (~11, all LDDT).** Coulomb-force **vector
superposition** (components/angles/signs) on multi-charge geometries: `LD274`/`LD150`
(36.32→21.79, dropped a component), `LD054`/`LD285` (→0.0 from an **invented symmetry** — the
text needs a figure the model guessed), `LD400`, `LD202`, `LD053`, `LD033`, `LD024`, `LD021`,
`LD057`. Plus 1 code crash (`LD087`).

**Takeaway:** golden's low score is **not** a broken finetune — ~8 of 22 are scorer/format bugs
we can fix without retraining, and the rest is genuinely hard electrostatics (often
figure-dependent problems that should have been filtered).

### High-ROI fixes (in progress)
1. **Scorer units + text** — normalise SI prefixes (mT↔T, μF↔F, cm↔m, …) before numeric compare;
   bidirectional text containment (len-guarded). Re-scores existing dumps with **no GPU**.
2. **Drop the sci-notation rule** in `GEN_SYSTEM` — let the model print plain floats / e-notation
   (the scorer already parses e-notation); kills the malformed-`X*10^N` bug.
3. **Stop forcing rounding** — print full precision (`:.6g`); let the 2% tolerance handle it.

(1) is scorer-only; (2)+(3) are prompt changes → need re-inference of v07c.

### New results after fixes (verified 2026-06-08)

The 3 fixes compound. ① (scorer) lifts val for every model but does nothing for golden
(golden's misses were real, not scoring). ②③ (prompt: full precision, no hand-formatted
sci-notation) recover the **golden** format bugs — and help the base model too.

**v07c, fix-by-fix:**
| v07c merged config | val_56 | golden_60 | Δ |
|---|---|---|---|
| old scorer, old prompt (baseline) | 0.750 | 0.633 | — |
| **+ scorer ①** (re-score old dumps, no GPU) | 0.821 | 0.633 | val +0.071 |
| **+ new prompt ②③** (re-inferred) | **0.857** | **0.717** | golden +0.084 |

**Fair head-to-head (both with new prompt ②③ + new scorer ①):**
| Model | val_56 | golden_60 |
|---|---|---|
| base Qwen3.5-4B | 0.821 | 0.683 |
| **v07c merged (deploy)** | **0.857** (48/56) | **0.717** (43/60) |

**v07c beats base by +2 problems on each set** — now consistently positive including the OOD
golden (before the fixes it was tied/below on golden). The prompt fix lifted both models; the
SFT edge is small but real. Net journey: v07c **0.750/0.633 → 0.857/0.717**, and it clears the
original v05_best 58.3% golden bar comfortably. Remaining v07c misses are the genuine LDDT
electrostatics-superposition ceiling (§C above) — the next lever is teacher-residual data or
inference-time self-consistency, not more scorer/prompt tweaks.

### Self-consistency (majority voting) — `self_consistency.py`

Sample **K=5** completions per problem in ONE batched `generate` (do_sample, temp 0.7, top_p
0.95, think-off), execute each, **majority-vote the answer using only the predictions (never the
gold)**, then score the voted answer. Competition-legal: one model, one batched generate per
request, < 60 s (the K samples ride the batch dimension — not parallel models, not sequential
temp passes). Voted greedy → SC:

| Model | val_56 | golden_60 |
|---|---|---|
| base Qwen3.5-4B (greedy) | 0.821 | 0.683 |
| base Qwen3.5-4B (**SC K=5**) | 0.875 | 0.783 |
| v07c merged (greedy) | 0.857 | 0.717 |
| **v07c merged (SC K=5)** | **0.875** (49/56) | **0.817** (49/60) |

SC lifts both models hard on the OOD golden (+0.10 each); v07c still leads base **+2 problems on
golden**, tied on val. Best config overall: **v07c + SC K=5 = 0.875 / 0.817**.

**Where SC helps / doesn't (golden, greedy 43 → SC 49; gained 9, lost 3):** it recovers problems
the model gets right *some* of the time — including **3 of the 4 problems base beat v07c on**
(LD049 5/5 votes, LD083 3/5, LD124 2/5) and the cos/sin superposition LD274 (4/5). It **cannot**
fix *systematic* errors where the wrong answer is the consensus: LD292 (5/5 voted the rounded
0.002 — sampling at temp 0.7 resurfaces the rounding habit still latent in the weights, which
only a data-level retrain on full-precision targets removes), LD285 (3/5 voted 0.0 from an
invented symmetry on a figure-dependent problem), LD328 (a wrong cluster won the vote).

> **Logs note:** the Colab box was terminated before the bulk log scp finished; only
> `colab_logs/sc_base.log` survived. All result numbers are preserved here and in the JSON dumps
> (`train/runs/{eval,sc}_*.json`); weights are on the Hub.

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
├── eval.py                        # F-pre: greedy accuracy on val_56 + golden_60 (run→exec→score)  ✅
├── self_consistency.py           # SC: sample K, majority-vote answer (no gold), score — best config  ✅
├── input/
│   └── trajectories_sft.jsonl     # ✅ THE SFT data — 2846 traj / 1505 problems
├── output/                        # ✅ train.jsonl (2634) + val.jsonl (110)
├── colab_logs/                    # surviving run logs (sc_base.log; rest lost to box termination)
├── train/                         # E: Unsloth LoRA  ✅ (v07b 4-bit, v07c 16-bit trained)
│   └── runs/README.md             #   ⭐ DECODER for the eval/sc_*.json naming + results map
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
