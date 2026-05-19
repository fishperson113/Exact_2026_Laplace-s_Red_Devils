# Physics Solution — Task Type 2 sandbox

This folder is where we try different strategies (zero-shot, few-shot, RAG,
LoRA fine-tune, RAG+finetune, …) for **EXACT 2026 Task Type 2**. Each
strategy is its own subfolder under [`versions/`](versions/), with a
shared library under [`shared/`](shared/) and a single source of config in
[`config.py`](config.py).

> Background: [docs/strategy/TYPE2_PHYSICS.md](../../docs/strategy/TYPE2_PHYSICS.md)
> · [docs/eda/TYPE2_PHYSICS_EDA.md](../../docs/eda/TYPE2_PHYSICS_EDA.md)
> · [EXACT_Materials/EXTRACT_Slides.md](../../EXACT_Materials/EXTRACT_Slides.md)
> · Qwen3.5 best-practices: [Qwen3_5.MD](Qwen3_5.MD)

## Layout

```
app/physics_solution/
├── .env                    # HF_TOKEN, LANGSMITH_API_KEY (gitignored). See .env.example
├── README.md               # this file
├── Qwen3_5.MD              # Qwen3.5 model card / best-practices reference
├── requirements.txt
├── config.py               # **single source of truth** for all knobs
├── colab_setup.py          # one-call Colab env setup + FLA installer
├── inference.py            # top-level CLI dispatcher
├── upload_model.py         # top-level HF push CLI (full metadata logging)
├── data/
│   ├── prepare_sample.py   # build sample_test.csv (stratified, default n=973)
│   └── sample_test.csv     # generated test set
├── shared/
│   ├── config.py
│   ├── prompts.py          # system + user templates (PHYSICS_SYSTEM_EN)
│   ├── lc_prompts.py       # LangChain ChatPromptTemplate builders
│   ├── lc_model.py         # HFBatchedLLM (Runnable) + RenderPrompt
│   ├── model_loader.py     # load tokenizer + model (bf16/fp16/int8/fp8)
│   ├── runner.py           # LCEL chain — prompt | render | llm — shared loop
│   ├── tracing.py          # LangSmith setup (no-op when key missing)
│   ├── evaluator.py        # answer extraction + numeric scoring
│   └── hf_uploader.py      # VersionMeta + push() + rich model-card template
├── versions/
│   ├── v01_zeroshot_baseline/
│   │   ├── __init__.py     # version metadata
│   │   ├── run.py          # exposes run(args)
│   │   ├── run.ipynb       # Colab notebook (Drive-direct)
│   │   └── README.md
│   └── v02_fewshot/
│       ├── __init__.py
│       ├── run.py
│       ├── run.ipynb
│       ├── select_fewshot.py   # curate examples.json from training data
│       ├── examples.json       # generated few-shot pool
│       └── README.md
├── eda/
│   ├── error_analysis.py   # classify wrong rows into fail modes
│   └── error_analysis.ipynb
└── results/                # per-run JSON + CSV (gitignored typically)
```

## Naming convention

HF repos: `Laplaces-Red-Devils/physics-v{NN:02d}-{strategy}-{base}`.

| Version | Tag | Status |
|---|---|---|
| v01 | `zeroshot` | **Done** — Qwen3.5-4B base, no examples |
| v02 | `fewshot` | **Done** — K examples per domain prefix |
| v03 | `rag` | Planned — formula KB + retriever |
| v04 | `lora` | Planned — LoRA fine-tune on golden CoT |
| v05 | `lora-rag` | Planned — stack |
| v06 | `pot` | Planned — Program-of-Thought (Python tool) |
| v07 | `lora-rag-pot` | Planned — full stack |

## Quickstart (Colab)

Open the per-version notebook (`versions/v0X_*/run.ipynb`) on Colab. It:

1. Mounts Google Drive and chdirs to the repo (no copy — runs directly off Drive).
2. `pip install -r requirements.txt`.
3. Installs Qwen3.5 fast-attention kernels (`flash-linear-attention` + pre-built `causal-conv1d`).
4. Loads `.env` (HF_TOKEN + optional LANGSMITH_API_KEY) and wires LangSmith.
5. Builds `data/sample_test.csv` (default 973 pure-numeric questions, stratified by domain).
6. Runs inference — **all knobs come from `config.py`**, no flags needed.
7. Pushes the artefact + rich model card to HF.
8. Open [`eda/error_analysis.ipynb`](eda/error_analysis.ipynb) to drill into wrong rows.

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

1. Make a folder `versions/v{NN}_{strategy}/` with `__init__.py` exposing
   `VERSION_NUM`, `STRATEGY_TAG`, `DEFAULT_BASE_MODEL_ID`, `DESCRIPTION`.
2. Add `run.py` exposing `def run(args) -> dict`. Most versions are a thin
   wrapper around `shared.runner.run_solver(...)` — pass a prompt template
   (from `shared.lc_prompts`) and an `InputBuilder` callable that maps a
   dataset row to template variables.
3. Register it in [`inference.py`](inference.py)'s `VERSIONS` dict.
4. Copy a sibling's `run.ipynb` and adjust the `--version` argument.
5. Push with `upload_model.py` once you have results.

## Hardware notes

- **A100 40 GB**: `BATCH_SIZE=100` is comfortable.
- **L4 22.5 GB**: drop to `BATCH_SIZE=32-64` if OOM.
- **T4 16 GB**: `DTYPE="fp16"` + `BATCH_SIZE=8`.
- **CPU local**: very slow (>30 s/Q on 4B fp16). Smoke-test only.
- `causal-conv1d` only has pre-built wheels for torch ≤ 2.6. If the Colab
  default torch is newer, `install_fast_kernels()` falls back to the torch
  attention implementation (~3× slower but functionally identical).
