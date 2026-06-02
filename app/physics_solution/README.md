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
| v01 | `zeroshot` | **Done** — Qwen3.5-4B base, no examples |
| v02 | `fewshot` | **Done** — K examples per domain prefix |
| v03 | `rag` | Planned — formula KB + retriever |
| v04 | `lora` | Planned — LoRA fine-tune on golden CoT |
| v05 | `lora-rag` | Planned — stack |
| v06 | `pot` | Planned — Program-of-Thought (Python tool) |
| v07 | `lora-rag-pot` | Planned — full stack |

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
