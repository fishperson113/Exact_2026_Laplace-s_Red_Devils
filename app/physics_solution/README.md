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
ensemble; `type1` → logic FOL→QA). Each vLLM server exposes its own **`GET /v1/models`**
(BTC §6.3 wants one per server); the gateway additionally proxies an aggregated
`/v1/models` ([`app/api/routes/models.py`](../../app/api/routes/models.py)) for convenience.
`submission/urls.txt` lists 3 URLs: gateway `/predict` + the two engines' `/v1/models`. Legacy `/ask` kept.

### Full stack = two vLLM servers on one GPU (`SERVE_MODE=combined`)

Model set matches [`app/logic_solution/config.yaml`](../logic_solution/config.yaml) (the
authoritative logic config). **Two** vLLM servers; the physics base also hosts the logic
stage-2 QA as a second LoRA adapter:

| vLLM server | Port | Model / adapters | Roles | Params |
|---|---|---|---|---|
| base + 2 LoRA | :18000 | base `Qwen3.5-4B` + `sft` + `qa` (ids `base`,`sft`,`qa`) | type2 solver/judge; type1 stage-2 QA | ~4B (+ tiny adapters) |
| fol | :18001 | `fol-v06-cot-augmented` (grafted composite, id `fol`) | type1 stage-1 NL→FOL | ~4B |

`sft` = `physics-v07c-sft-qwen3.5-4b`; `qa` = `v04-QA-CoT` (both LoRA on the shared base);
`fol` = `fol-v06-cot-augmented-fol-pretrain-malls-qwen3.5-4` (full finetune). Because `qa`
shares :18000 with physics, only `fol` would ever be sleep-swapped.

**`RESIDENT_ALL=1` (default).** Peak GPU residency is ~8B either way (base 4B + fol 4B; the
adapters are tiny PEFT deltas), which the organizer explicitly allows ("two 4B models in
parallel"). So both servers stay awake — no sleep/wake, no per-type swap cost. `RESIDENT_ALL=0`
falls back to sleep-swapping `fol` by type for tighter GPUs
([`app/core/model_swap.py`](../../app/core/model_swap.py)).

**The graft step (load-bearing).** The FOL full finetune ships as the text-only arch
`Qwen3_5ForCausalLM` / `qwen3_5_text`, which **vLLM 0.22.1 cannot serve** — it registers only
the composite `Qwen3_5ForConditionalGeneration`. So `fol` is **grafted onto the composite base**
by [`scripts/graft_text_to_composite.py`](../../scripts/graft_text_to_composite.py) (overwrite the
426 `model.language_model.*` tensors, keep the base's vision tower + mtp + config; vision is dead
weight, never exercised). `sft` and `qa` are LoRA adapters served directly on the base (no graft).
`serve_all.sh combined` runs this automatically (idempotent, to `/dev/shm/models/fol-composite`).

Measured on RTX 5090 32 GB through public tunnels (VRAM ~26.7/32 GB): **type2 ~7–9 s** (correct:
2µF@12V→1.44e-4 J, 4∥6Ω@12V→5 A), **type1 ~2–4 s** (`No`/`Yes`, premises_used=[0,1] emitted by the
QA model, FOL+QA steps), all ≪ 60 s.

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

### Results — final 3-run experiment (RTX 5090, CUDA graphs)

Each config run **3×** on both sets with **identical samples feeding all 3 configs per run**, so the
only difference is the voting strategy (full report + per-problem log:
[`output/FINAL_EXPERIMENT.md`](versions/v07_ensemble_vLLM/output/FINAL_EXPERIMENT.md)):

| config | val_56 (mean [min..max]) | golden_60 (mean [min..max]) |
|---|---|---|
| single SFT (K=5) | 0.863 [0.839..0.893] | 0.783 [0.767..0.800] |
| single BASE (K=5) | 0.833 [0.786..0.875] | 0.778 [0.767..0.800] |
| **pooled ENSEMBLE (10-vote)** | **0.869 [0.857..0.893]** | **0.789 [0.783..0.800]** |

Latency (ensemble, graphs): median **6.5 s**, p90 14.9 s, max 20.3 s — all ≪ 60 s.

**Decision: KEEP the ensemble** — but know it's a near-tie, not a win:
- Ensemble beats the best single model by only **+0.6pt** (within run variance). We keep it because
  it is **nearly free** (BASE is already loaded as the explainer; its 5 samples batch in parallel
  with SFT's on the one engine) and gives a slightly **higher floor** (golden min 0.783 vs SFT 0.767).
- **SFT ≥ BASE everywhere** (so SFT is the better single model). Domain split: SFT clearly stronger on
  **DDT (+0.07), TD (+0.10)**, tie elsewhere; the val-LDDT BASE edge is n=6 noise (golden LDDT n=60 is
  tied). → **domain-weighting collapses to "use SFT"; not worth it.**
- The two models are **87–92% redundant** (both produce a correct sample); the complementary slice is
  ~3–6% and **5–7% are `none`** (neither solves). An LLM **judge cannot pick** the right answer
  (anonymous 4/13, self-review 3/13 on disagreements, both below random) → judge writes the
  explanation/CoT only, never selects.
- **The real lever is DATA/coverage**, not voting: pooled-10 golden ORACLE ≈ 0.92 but the vote often
  picks a systematic-error majority over a correct minority. (Consistent across the oracle-0.917 /
  minority-lost finding and the 3-run experiment.)

Measurement scripts: [`final_experiment.py`](versions/v07_ensemble_vLLM/final_experiment.py) (the
3-run report), [`measure_pool.py`](versions/v07_ensemble_vLLM/measure_pool.py),
[`versions/v07_final_version/ensemble.py`](versions/v07_final_version/ensemble.py).

**Bring-up** (RTX 5090 32 GB or any CUDA-13 box; **transformers 5.10 + vLLM 0.22.1**):
```bash
# FULL competition stack — both task types, two vLLM servers (resident by default):
HF_TOKEN=hf_... SERVE_MODE=combined bash scripts/serve_all.sh start
#   grafts fol -> composite (idempotent); serves base+LoRA(sft,qa) :18000 + fol :18001,
#   both awake (RESIDENT_ALL=1); gateway :9000 (/predict + /v1/models); warms BOTH types.
#   3 cloudflared tunnels -> submission/urls.txt (gateway + :18000 + :18001, BTC §6.3).

# Physics-only (testing): SERVE_MODE=physics_ensemble (CUDA graphs, no swap).
```
Models: BASE=`Qwen/Qwen3.5-4B` + LoRA `sft`=`Laplaces-Red-Devils/physics-v07c-sft-qwen3.5-4b`
+ LoRA `qa`=`Laplaces-Red-Devils/v04-QA-CoT`; `fol`=`Laplaces-Red-Devils/fol-v06-cot-augmented-fol-pretrain-malls-qwen3.5-4`
(grafted on-box). Knobs in [`app/core/config.py`](../../app/core/config.py). Each vLLM server
exposes its own `/v1/models` (:18000 → base,sft,qa; :18001 → fol) for committee verification.

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
