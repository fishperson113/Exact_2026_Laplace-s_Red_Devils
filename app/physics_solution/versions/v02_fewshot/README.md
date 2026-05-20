# v02 — Few-shot in-context learning

Same upstream Qwen weights as v01, but each prompt is preceded by **K
worked examples** (default K=2) from the training set, served as prior
user/assistant turns so the model can imitate both the reasoning style
and the strict `FINAL ANSWER:` / `UNIT:` output format.

## Why this matters

- v01 frequently misses the output format. Few-shot examples anchor it.
- Examples are picked per **domain prefix** (LD / CH / TD / …) so the
  model sees a problem of the same type before solving the real one.
- No fine-tuning — fastest way to lift baseline accuracy.

## Run

```bash
# 1. Curate examples once (drops anything in sample_test.csv to avoid leakage)
python -m app.physics_solution.versions.v02_fewshot.select_fewshot --k 2

# 2. Inference
python -m app.physics_solution.cli.inference \
    --version v02_fewshot \
    --test-file app/physics_solution/data/sample_test.csv \
    --dtype fp16 --device cpu --limit 5

# 3. Push
python -m app.physics_solution.cli.upload_model \
    --version-num 2 --strategy fewshot --base-tag qwen3.5-4b \
    --base-model-id Qwen/Qwen3.5-4B \
    --results app/physics_solution/versions/v02_fewshot/output/results.json
```

## Files

- `select_fewshot.py` — curates `input/examples.json` from the dataset.
- `input/examples.json` — generated; one entry per chosen example.
- `prompts.py` — builds the chat template with few-shot placeholder.
- `run.py` — version entry point exposed to `cli/inference.py`.

## Knobs

- `--k` in `select_fewshot.py`: examples per domain.
- `n_examples` is hard-coded to 2 in `run.py` for now. Promote it to a CLI
  flag when we want to sweep.
