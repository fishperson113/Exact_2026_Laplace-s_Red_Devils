# v01 — Zero-shot baseline (Qwen3.5-4B)

The simplest possible end-to-end: load the upstream Qwen weights, feed the
strict-format physics prompt from [shared/prompts.py](../../shared/prompts.py),
parse `FINAL ANSWER: …` from the completion, score against the gold numeric.

## Why this version exists

- Establishes the **accuracy floor** every later strategy must beat.
- Validates the whole plumbing (data → model → extractor → results → HF push)
  before we touch fine-tuning.
- Cheap to re-run any time we change extractor logic or prompt phrasing.

## Run it

```bash
# 1. Prepare 50 stratified numeric-only questions (only needs to run once)
python -m app.physics_solution.data.prepare_sample --n 50 --seed 42

# 2. Inference
python -m app.physics_solution.inference \
    --version v01_zeroshot_baseline \
    --test-file app/physics_solution/data/sample_test.csv \
    --dtype fp16 \
    --device cpu

# 3. (Optional) Push to HF as Laplaces-Red-Devils/physics-v01-zeroshot-qwen3.5-4b
python -m app.physics_solution.upload_model \
    --version-num 1 \
    --strategy zeroshot \
    --base-tag qwen3.5-4b \
    --base-model-id Qwen/Qwen3.5-4B \
    --results app/physics_solution/results/v01_zeroshot.json
```

## Expected output

- `app/physics_solution/results/v01_zeroshot.json` — summary + per-row.
- `app/physics_solution/results/v01_zeroshot.csv` — same data in tabular form.

## Known limitations

- CPU + fp16 inference on a 4B model is **very slow** (often >30 s/question).
  Move to Colab GPU before testing larger sweeps.
- No tool calling, no SymPy verification, no RAG context. Those are v02+.
