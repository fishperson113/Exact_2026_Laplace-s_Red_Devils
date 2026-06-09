# colab_setup — run v07 SFT on Google Colab (A100)

Validated 2026-06-07 on a Colab **A100-40GB** (driver 580, torch 2.10/cu128, Py 3.12):
install → Unsloth load of Qwen3.5-4B (`qwen3_5`) → `train_on_responses_only` → eval_loss
→ save adapter all work end-to-end.

## The proven stack (why the pins)
`requirements.txt` is copied verbatim from the FOL model's environment — the same pins
that trained **Qwen/Qwen3.5-4B** with Unsloth. The load-bearing ones:

```
torch==2.10.0  transformers==5.5.0  trl==0.24.0  peft==0.19.1
unsloth==2026.5.6  unsloth_zoo==2026.5.4  bitsandbytes==0.49.2  xformers==0.0.35
```

- **transformers 5.5.0** is the floor for `qwen3_5` support. 4.57.x (stable) only has
  `qwen3_next`; the model ships **no remote code**, so an older transformers can't load it.
- **flash-linear-attention / causal-conv1d are NOT required.** They're absent from the pins;
  Unsloth/tf5 uses a torch fallback. `setup_colab.sh` installs them best-effort (speed only).
- Unsloth logs `Qwen3_5 does not support SDPA — switching to fast eager` — expected, harmless.

## How to use (SSH or notebook)

The flow the box expects (per the project): SSH in, `cd /content`, then:

```bash
echo 'export LD_LIBRARY_PATH=/usr/lib64-nvidia:/usr/local/nvidia/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
echo 'export PATH=/usr/local/nvidia/bin:/usr/local/cuda/bin:$PATH' >> ~/.bashrc
source ~/.bashrc            # nvidia-smi works after this
```

Then run (or copy the cells from `train_v07.ipynb` into the Colab notebook):

```bash
bash app/physics_solution/versions/v07_final_version/colab_setup/setup_colab.sh
```

This creates an **isolated uv venv at `/content/v07_env`** (so Colab's own jupyter is never
clobbered) and installs the pinned stack. Training/eval are then run with
`/content/v07_env/bin/python` — which works from a notebook via `!`.

Everything else (train, merge+push, eval) is in `train_v07.ipynb`.

## Inference-only quickstart (verify results on a fresh GPU)

The same `/content/v07_env` is all you need to *infer* (eval.py / self_consistency.py use plain
`transformers.AutoModelForCausalLM`, not Unsloth). On a new Colab box:

```bash
# 0. nvidia libs on path
echo 'export LD_LIBRARY_PATH=/usr/lib64-nvidia:/usr/local/nvidia/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc && source ~/.bashrc
# 1. clone + env (skip if repo already at /content)
cd /content && git clone <repo> Exact_2026_Laplace-s_Red_Devils 2>/dev/null; cd Exact_2026_Laplace-s_Red_Devils
git fetch origin && git reset --hard origin/Nguyen/submition_v1
bash app/physics_solution/versions/v07_final_version/colab_setup/setup_colab.sh   # builds /content/v07_env (~5 min)
# 2. token (the deploy merged repo is PRIVATE)
export HF_TOKEN=<hf_token>; export HUGGING_FACE_HUB_TOKEN=$HF_TOKEN
# 3. run
export LD_LIBRARY_PATH=/usr/lib64-nvidia:$LD_LIBRARY_PATH PYTORCH_ALLOC_CONF=expandable_segments:True PYTHONPATH=.
PY=/content/v07_env/bin/python; M=app.physics_solution.versions.v07_final_version
DEPLOY=Laplaces-Red-Devils/physics-v07c-sft-qwen3.5-4b-merged
$PY -m $M.eval             --model $DEPLOY --sets both --max-new-tokens 2048 --batch-size 32   # expect 0.857 / 0.717
$PY -m $M.self_consistency --model $DEPLOY --sets both --k 5 --temperature 0.7 --prob-batch 6  # expect 0.875 / 0.817
```

Expected (think-OFF): greedy **val 0.857 / golden 0.717**, SC K=5 **0.875 / 0.817**. SC has
sampling variance (±1–2 problems run-to-run). Output naming: see
[`../train/runs/README.md`](../train/runs/README.md). ⚠️ **Pull `runs/*.json` + `/content/*.log`
to local immediately after each run** — Colab boxes get terminated without warning (we lost the
base-SC dump that way).

## Notes
- Base weights (~8 GB, bnb-4bit) download on first run; cached afterwards.
- `merge_push.py` merges on CPU and pushes the **adapter** and a **merged** repo to
  `Laplaces-Red-Devils/*` (needs `HF_TOKEN`). vLLM serves the merged repo.
