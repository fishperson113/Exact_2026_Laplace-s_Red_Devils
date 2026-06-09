# Physics Solution — Task Type 2 sandbox

This folder is where we try different strategies (zero-shot, few-shot, RAG,
LoRA fine-tune, RAG+finetune, ...) for **EXACT 2026 Task Type 2**. Each
strategy is its own subfolder under [`versions/`](versions/), with a
shared library under [`shared/`](shared/) and a single source of config in
[`config.py`](config.py).

> Background: [docs/strategy/TYPE2_PHYSICS.md](../../docs/strategy/TYPE2_PHYSICS.md)
> . [docs/eda/TYPE2_PHYSICS_EDA.md](../../docs/eda/TYPE2_PHYSICS_EDA.md)
> . [EXACT_Materials/EXTRACT_Slides.md](../../EXACT_Materials/EXTRACT_Slides.md)
> . Qwen3.5 best-practices: [docs/qwen3_5.md](docs/qwen3_5.md)

## Layout

```
app/physics_solution/
├── README.md                          # this file
├── requirements.txt
├── config.py                          # single source of truth for all knobs
├── __init__.py
├── .env, .gitignore
│
├── docs/
│   └── qwen3_5.md                     # Qwen3.5 model card / best-practices
│
├── cli/
│   ├── __init__.py
│   ├── inference.py                   # top-level CLI dispatcher
│   ├── upload_model.py                # HF push CLI (full metadata logging)
│   └── prepare_sample.py             # build sample_test.csv (stratified)
│
├── shared/
│   ├── __init__.py                    # re-exports common symbols
│   ├── model/
│   │   ├── loader.py                  # load tokenizer + model (bf16/fp16/int8/fp8)
│   │   └── batched_llm.py            # HFBatchedLLM (Runnable) + RenderPrompt
│   ├── prompts/
│   │   ├── system.py                  # PHYSICS_SYSTEM_EN + base templates
│   │   └── helpers.py                 # fewshot_messages_from() utility
│   ├── eval/
│   │   └── scorer.py                  # answer extraction + numeric scoring
│   ├── runtime/
│   │   ├── runner.py                  # LCEL chain — prompt | render | llm
│   │   └── tracing.py                # LangSmith setup (no-op when key missing)
│   ├── upload/
│   │   └── hf.py                      # VersionMeta + push() + model-card template
│   └── colab/
│       └── setup.py                   # one-call Colab env setup + FLA installer
│
├── data/
│   ├── raw/                           # pointer to EXACT_Materials/Datasets/
│   ├── test/
│   │   └── sample_test.csv            # generated test set (973 pure-numeric)
│   └── golden/                        # placeholder for stage 4 output
│
├── eda/
│   ├── scripts/
│   │   └── error_analysis.py          # classify wrong rows into fail modes
│   └── notebooks/
│       └── error_analysis.ipynb
│
└── versions/
    ├── _template/                     # reference template for new versions
    │   ├── README.md
    │   ├── __init__.py, run.py, prompts.py
    │   ├── input/.gitkeep
    │   └── output/.gitkeep
    │
    ├── v01_zeroshot_baseline/
    │   ├── __init__.py, run.py, prompts.py, run.ipynb, README.md
    │   ├── input/.gitkeep
    │   └── output/                    # results.json + results.csv
    │
    └── v02_fewshot/
        ├── __init__.py, run.py, prompts.py, run.ipynb, README.md
        ├── select_fewshot.py          # curate examples from training data
        ├── input/
        │   └── examples.json          # generated few-shot pool
        └── output/
            ├── results.json
            └── results.csv
```

## Naming convention

HF repos: `Laplaces-Red-Devils/physics-v{NN:02d}-{strategy}-{base}`.

| Version | Tag | Status |
|---|---|---|
| v01 | `zeroshot` | Done — Qwen3.5-4B base, no examples |
| v02 | `fewshot` | Done — K examples per domain prefix |
| v05_best | `best` | Done — classify → codegen → execute → parse (58.3% on 60 golden) |
| v05_best_vLLM | `best_vLLM` | Done — v05_best served async over vLLM (`pipeline.py::solve`) |
| v06_finetune | `pot` | Done — SFT data pipeline (PoT trajectories) |
| v07_final_version | `self-sft` | Done — SFT Qwen3.5-4B (v07c merged); eval/self-consistency harness |
| **v07_ensemble_vLLM** | **`ensemble_vLLM`** | **CURRENT serving** — physics group of `SERVE_MODE=combined` (pooled SFT+BASE vote, BASE writes explanation; see below) |

## Production serving — BTC `/predict`, both task types (CURRENT)

The competition endpoint is **`POST /predict`** (BTC 2026 Submission Guide): one
endpoint, route by the `type` field, return a JSON **list** of result objects
(`{query_id, answer, unit, explanation, premises_used, reasoning}`). Implemented in
[`app/api/routes/predict.py`](../../app/api/routes/predict.py) (`type2` → physics
ensemble; `type1` → logic FOL→QA). The gateway also proxies **`GET /v1/models`**
([`app/api/routes/models.py`](../../app/api/routes/models.py)) — it aggregates every
vLLM engine's model list into one OpenAI-compatible response, so a **single public
URL** covers both BTC-required endpoints (`/predict` + `/v1/models`). Legacy `/ask` kept.

### Full stack = per-type models on one GPU, sleep-swapped (`SERVE_MODE=combined`)

The four serving weights exceed the ≤8B that may be GPU-resident at once, so each
vLLM runs with `--enable-sleep-mode` and the gateway wakes the group a request needs
and sleeps the rest ([`app/core/model_swap.py`](../../app/core/model_swap.py), keyed
by the `type` field):

| Group (type) | Engine(s) | Models | GPU-resident |
|---|---|---|---|
| **physics** (type2) | :18000 | base `Qwen3.5-4B` + LoRA `sft` (ids `base`,`sft`) | ~4B |
| **logic** (type1) | :18001 + :18002 | `fol` + `qa` (two full Qwen3.5-4B) | ~8B (organizer-permitted 2×4B) |

**The graft step (load-bearing).** All three finetunes (physics-merged, fol-pretrain,
qa) ship as the text-only arch `Qwen3_5ForCausalLM` / model_type `qwen3_5_text`, which
**vLLM 0.22.1 cannot serve** — it registers only the composite `Qwen3_5ForConditionalGeneration`.
The physics SFT is served as a **LoRA adapter** on the composite base (adapter keys are
already in the `model.language_model.*` namespace). The two **logic** models are full
finetunes (no shared base), so each is **grafted onto the composite base** by
[`scripts/graft_text_to_composite.py`](../../scripts/graft_text_to_composite.py): take
the base composite, overwrite its 426 `model.language_model.*` tensors with the
finetune's, keep the base's vision tower + mtp + config → a valid composite checkpoint
vLLM serves text-only (vision is dead weight, never exercised). `serve_all.sh combined`
runs this automatically (idempotent, to `/dev/shm/models/{fol,qa}-composite`).

Measured on RTX 5090 (eager, swap-safe): **type2 ~17–18s** (correct: 2µF@12V→1.44e-4 J,
4∥4Ω→2Ω), **type1 ~2.6s including the physics→logic swap** (`Yes`, premises_used=[0,1],
FOL steps emitted). Swaps are cheap (sleep-level-1 wake from CPU RAM).

### Type 2 ensemble (physics)

**Type 2 ensemble** ([`versions/v07_ensemble_vLLM/pipeline.py`](versions/v07_ensemble_vLLM/pipeline.py)) —
**ONE vLLM hosts the BASE `Qwen/Qwen3.5-4B` + the SFT (v07c) as a LoRA adapter** (`--enable-lora`,
ids `base`+`sft` on one `/v1/models`; ~4B total ≪ 8B). The text-only MERGED checkpoint is arch
`Qwen3_5ForCausalLM`/`qwen3_5_text` which **vLLM 0.22.1 cannot serve** (only the composite
`Qwen3_5ForConditionalGeneration`); the adapter's keys match the composite base, so LoRA serving
is the working path. Per query:

1. **classify** → (domain, answer_type)  [one fast BASE call]
2. **BASE and SFT each sample K=5 concurrently** (`asyncio.gather` → one engine, vLLM
   continuous-batches all 10 sequences together), execute each sample's code.
3. **Pooled vote**: cluster all 10 answers (scorer tolerance), **majority cluster wins**.
4. **explanation + CoT** written by the BASE model for the chosen answer (does NOT change it).

Deadline-safe (skip explanation → use the chosen solution's own reasoning if the 60 s budget is
nearly spent).

### Results & the hard finding (RTX 5090, matches offline)

| config | val_56 | golden_60 | latency median / max |
|---|---|---|---|
| single SFT (SC K=5) | 0.875 | 0.78–0.82* | — |
| single BASE (SC K=5) | 0.875 | 0.75–0.80* | — |
| **pooled ensemble (10-vote)** | **0.875** | **0.733** | **~9–11 s / ~23 s** |

*single-model SC bounces ±4 problems run-to-run (temp 0.7 sampling variance).

**The ensemble does NOT beat a single model**, and **majority voting leaves a lot on the table**:
- An LLM **judge cannot select** the right answer — anonymous framing 4/13, self-review framing
  3/13 on disagreements (both **below random**); a same-class 4B can't adjudicate physics it
  couldn't solve. The judge is therefore used **only to write the explanation/CoT**, not to pick.
- **Pooled-10 golden: accuracy 0.733 but ORACLE 0.917** (55/60 problems have ≥1 correct sample),
  and **minority-lost = 11** — in 11 problems the majority cluster is WRONG while a *minority*
  cluster holds the correct answer (a systematic error, e.g. a rounding habit, dominates the vote).
  → **The bottleneck is SELECTION, not voting.** The model already reaches the answer ~92% of the
  time; the lever is making the correct method the *majority* — i.e. **better DATA / training**
  (teacher-residual on the systematic-error problems) or an **external verifier** — NOT more
  voting or judging.

Offline harness (non-serving) + measurement scripts:
[`versions/v07_final_version/ensemble.py`](versions/v07_final_version/ensemble.py),
[`versions/v07_ensemble_vLLM/measure_pool.py`](versions/v07_ensemble_vLLM/measure_pool.py),
`investigate_ensemble.py`.

**Bring-up** (RTX 5090 32 GB or any CUDA-13 box; **transformers 5.10 + vLLM 0.22.1**):
```bash
# FULL competition stack — both task types, per-type models, sleep-swap:
HF_TOKEN=hf_... SERVE_MODE=combined bash scripts/serve_all.sh start
#   grafts fol/qa -> composite (idempotent), serves physics base+LoRA :18000 +
#   fol :18001 + qa :18002 (all sleep-mode), gateway :9000 (/predict + /v1/models),
#   warms BOTH types. Committee: GET <url>/v1/models lists base,sft,fol,qa.

# Physics-only (testing): SERVE_MODE=physics_ensemble (CUDA graphs, no swap).
```
Models: physics BASE=`Qwen/Qwen3.5-4B` + adapter `Laplaces-Red-Devils/physics-v07c-sft-qwen3.5-4b`;
logic `fol`=`Laplaces-Red-Devils/fol-pretrain-malls-qwen3.5-4b`, `qa`=`Laplaces-Red-Devils/fol-v06-cot-augmented-fol-pretrain-malls-qwen3.5-4`
(both grafted on-box). Knobs in [`app/core/config.py`](../../app/core/config.py). The
gateway `/v1/models` proxy lists all four ids for committee verification.

## Quickstart (Colab)

Open the per-version notebook (`versions/v0X_*/run.ipynb`) on Colab. It:

1. Mounts Google Drive and chdirs to the repo.
2. `pip install -r requirements.txt`.
3. Installs Qwen3.5 fast-attention kernels.
4. Loads `.env` (HF_TOKEN + optional LANGSMITH_API_KEY) and wires LangSmith.
5. Builds `data/test/sample_test.csv` (default 973 pure-numeric questions).
6. Runs inference — **all knobs come from `config.py`**, no flags needed.
7. Pushes the artefact + rich model card to HF.
8. Open [`eda/notebooks/error_analysis.ipynb`](eda/notebooks/error_analysis.ipynb) to drill into wrong rows.

## Config (edit `config.py`, not notebooks)

```python
BASE_MODEL_ID  = "Qwen/Qwen3.5-4B"
DTYPE          = "bf16"          # bf16 / fp16 / fp32 / int8 / fp8
DEVICE         = "cuda"
BATCH_SIZE     = 100             # full-eval default; drop to 8 for batch=1 latency
MAX_NEW_TOKENS = 640
TEMPERATURE    = 0.0             # greedy for math
LANGSMITH_PROJECT = "exact26-physics-type2"
```

CLI flags still override (`--limit 5 --batch-size 4 --dtype fp16`).

## Adding a new version

1. Copy `versions/_template/` to `versions/v{NN}_{strategy}/`.
2. Edit `__init__.py` with version metadata.
3. Customize `prompts.py` and `run.py`.
4. Register it in [`cli/inference.py`](cli/inference.py)'s `VERSIONS` dict.
5. Copy a sibling's `run.ipynb` and adjust the `--version` argument.
6. Push with `cli/upload_model.py` once you have results.

## Hardware notes

- **A100 40 GB**: `BATCH_SIZE=100` is comfortable.
- **L4 22.5 GB**: drop to `BATCH_SIZE=32-64` if OOM.
- **T4 16 GB**: `DTYPE="fp16"` + `BATCH_SIZE=8`.
- **CPU local**: very slow (>30 s/Q on 4B fp16). Smoke-test only.
