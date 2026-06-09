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
| **v07_ensemble_vLLM** | **`ensemble_vLLM`** | **CURRENT serving** — SFT + BASE in parallel, BASE judges (see below) |

## Production serving — BTC `/predict` + physics ensemble (CURRENT)

The competition endpoint is **`POST /predict`** (BTC 2026 Submission Guide): one
endpoint, route by the `type` field, return a JSON **list** of result objects
(`{query_id, answer, unit, explanation, premises_used, reasoning}`). Implemented in
[`app/api/routes/predict.py`](../../app/api/routes/predict.py) (`type2` → physics
ensemble; `type1` → logic, output shaped best-effort). Legacy `/ask` kept for tooling.

**Type 2 ensemble** ([`versions/v07_ensemble_vLLM/pipeline.py`](versions/v07_ensemble_vLLM/pipeline.py)):
two 4B models served **in parallel** (BTC allows 2×4B = 8B active) —

1. **classify** → (domain, answer_type)  [one fast BASE call]
2. **SFT (v07c) and BASE (Qwen3.5-4B) each self-consistency-sample K=5 in parallel**
   (`asyncio.gather` over two vLLM servers → wall-time ≈ max, not sum), execute each
   sample's code, majority-vote each model's answer.
3. **agree** (scorer-equivalent) → done; else **BASE judges** which final answer is
   correct (text only, **no code, no vote counts shown**) → pick SFT or BASE.
4. explanation + CoT `reasoning.steps` built from the chosen solution (no extra call).

Deadline-safe: if the 60 s budget is nearly spent after sampling, skip the judge and
fall back to the SFT vote. The judge reuses the already-running BASE model (no extra
params). *Offline finding:* the ensemble is a recall ("vét") play — self-consistency
ties the single models (~0.875 val), oracle ceiling only +3 on golden; the real lever
is better DATA on the ~13 both-fail problems. Offline harness (non-serving):
[`versions/v07_final_version/ensemble.py`](versions/v07_final_version/ensemble.py).

**Bring-up** (RTX 5090 32 GB or any CUDA-13 box):
```bash
SERVE_MODE=physics_ensemble bash scripts/serve_all.sh start
#   SFT  :18000 (served "physics")  +  BASE :18004 (served "base"), both resident,
#   --gpu-memory-utilization 0.45 each, no sleep-swap. Gateway :9000 /predict.
```
Endpoints/config: SFT=`Laplaces-Red-Devils/physics-v07c-sft-qwen3.5-4b-merged`,
BASE=`Qwen/Qwen3.5-4B`; knobs in [`app/core/config.py`](../../app/core/config.py)
(`vllm_*` = SFT, `judge_*` = BASE+judge, `ensemble_k`). Each vLLM exposes its own
`/v1/models` for committee verification.

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
