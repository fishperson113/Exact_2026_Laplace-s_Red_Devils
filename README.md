# Exact 2026 — Laplace's Red Devils

Solution for **EXACT 2026, Task Type 2 (Physics)**: solve Vietnamese-origin
physics problems (electrostatics, circuits, capacitors, energy, induction,
measurement) with **Qwen3.5-4B** by generating and executing Python code, then
parsing the printed answer.

> A mock Task Type 1 (logic) route exists at `/logic/ask`, but Physics is the focus.

## Stack

| Concern | Choice |
|---|---|
| Model | Qwen3.5-4B |
| Serving | **vLLM** (OpenAI-compatible endpoint) |
| API gateway | **FastAPI** (`app/main.py`, exposes `/ask`) |
| Solve strategy | Classify → generate Python → execute → parse answer |
| Dependency mgmt | `uv` (`uv.lock` / `pyproject.toml`) |
| Dev environment | WSL Ubuntu (Python 3.12) |

> ℹ️ Earlier revisions of this project used Ollama + LangGraph for a "math QA"
> design. That is **gone** — the live stack is vLLM + FastAPI with the physics
> code-execution pipeline described here. `CLAUDE.md` and `docs/` are the
> authoritative references.

## Run environment

Develop and run from **WSL Ubuntu**, not native Windows / Git Bash:

```bash
wsl                                                  # default distro = Ubuntu
cd /mnt/d/Git/Exact_2026_Laplace-s_Red_Devils
uv sync                                              # build the Linux venv
```

The committed `.venv` (if any) is a Windows venv and is unusable in Linux.
Heavy GPU work (vLLM serving, fine-tune) runs on a remote Linux GPU box.

## Two execution paths

The model is run in two completely separate ways:

### 1. Batch eval (model loaded in-process — Colab / GPU box)

Loads the HF model directly and scores a test CSV.

```bash
# smoke test
python -m app.physics_solution.cli.inference --version v05_best --limit 10
# full golden run
python -m app.physics_solution.cli.inference --version v05_code_execution
```

Versions are dispatched via the `VERSIONS` dict in
`app/physics_solution/cli/inference.py` to `versions/<vNN>/run.py::run(args)`.
Results land in `versions/<vNN>/output/results*.{json,csv}`.

To run on a remote GPU box and pull results back (from Windows PowerShell):

```powershell
.\scripts\run_and_pull.ps1 -HostAddr <ip> -Port <port> [-Limit 10]
```

### 2. Production serving (vLLM + FastAPI)

vLLM serves the model over an OpenAI-compatible endpoint; FastAPI exposes `/ask`.
`app/core/pipeline.py` dynamically loads
`versions/{PIPELINE_VERSION}/pipeline.py::solve()` (default `v05_best_vLLM`).

```bash
# on the GPU host (boots vLLM if needed, starts uvicorn, opens a cloudflared tunnel)
bash scripts/start_server.sh

# evaluate the running server (--concurrency 1 mirrors competition conditions)
python -m app.physics_solution.cli.eval_api --api-url <url> --concurrency 1
```

See `app/physics_solution/README_GPU_SETUP.md` for the Vast AI vLLM setup.

## Endpoints

| Method | Path | Description |
|---|---|---|
| `GET` | `/` | Service info + available tracks |
| `POST` | `/ask` | Solve a physics question (Task Type 2) |
| `GET` | `/health` | Liveness (checks vLLM reachability) |
| `POST` | `/logic/ask` | Task Type 1 logic route (mock) |

**`POST /ask`**

```jsonc
// Request
{ "question": "Two charges q1=2e-6 C and q2=-3e-6 C are 0.5 m apart..." }

// Response (QAResponse)
{
  "answer": "...",
  "unit": "...",
  "explanation": "",
  "cot": "",
  "solve_method": "code_execution",   // or "failed" / "timeout" / "api_error"
  "elapsed_s": 4.2,
  "domain": "LDDT",
  "answer_type": "numeric",
  "generated_code": "import math\n...",
  "execution_stdout": "FINAL ANSWER: ...\nUNIT: ..."
}
```

## Configuration

- **Batch / training side:** `app/physics_solution/config.py` is the single
  source of truth (model id, dtype, batch size, generation params, test-file
  paths, HF org, DeepSeek golden-data settings). CLI flags override ad-hoc.
- **Serving side:** `app/core/config.py` reads `.env` — key vars:

| Variable | Default | Description |
|---|---|---|
| `VLLM_BASE_URL` | `http://localhost:18000/v1` | OpenAI-compatible vLLM endpoint |
| `VLLM_MODEL` | `Qwen/Qwen3.5-4B` | Served model id |
| `PIPELINE_VERSION` | `v05_best_vLLM` | Which version's `pipeline.py` to serve |
| `QUESTION_TIMEOUT_S` | `60.0` | Per-question wall-clock budget |
| `LANGSMITH_API_KEY` | — | Optional tracing (no-op if blank) |

Copy `.env.example` to `.env` to start.

## Pipeline & status

Current best is **v05_best**: classify → generate Python → execute → parse,
**58.3% on the 60-question golden set**. Each strategy is a self-contained folder
under `app/physics_solution/versions/`. The active branch `Nguyen/v06_finetune`
adds Continue-Pre-Training (CPT) + SFT fine-tuning.

## Data assets

- `app/physics_solution/data/golden/deepseek-v4-pro_golden_data.csv` — 1,352 rows
  of DeepSeek-rewritten CoT (`id, question, cot, answer, unit`).
- `data/pretrain_processed/lop-*.md` — 2,261 QC'd Vietnamese worked solutions for
  CPT (catalog in `DATA_CATALOG.md`).

## More docs

- `CLAUDE.md` — conventions and architecture for contributors / AI agents
- `docs/strategy/TYPE2_PHYSICS.md`, `docs/eda/TYPE2_PHYSICS_EDA.md` — strategy & EDA
- `docs/guides/{FINETUNE,UNSLOTH,PRETRAIN_DATA,DATA_COLLECTION}_GUIDE.md` — fine-tuning
- `app/physics_solution/versions/v06_finetune/V06_HANDOFF_PROMPT.md` — v06 context
