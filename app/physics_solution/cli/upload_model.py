"""Upload a model artefact to the Laplaces-Red-Devils HF org.

Two modes:

1. Push the *upstream* base weights (baseline versions, no finetune):
       python -m app.physics_solution.cli.upload_model \\
           --version-num 1 --strategy zeroshot \\
           --results app/physics_solution/results/v01_zeroshot.json
   The upstream snapshot is downloaded into a local cache dir, the model
   card is written next to it, then the whole folder is uploaded.

2. Push a *local* model directory (after finetune or merge):
       python -m app.physics_solution.cli.upload_model \\
           --version-num 4 --strategy lora \\
           --local-dir runs/v04_lora/merged \\
           --results app/physics_solution/results/v04_lora.json

The model card pulls **everything** out of the results JSON's `summary`
field plus live env info (GPU name, VRAM, torch/transformers versions).
The corresponding results JSON + CSV are staged under `reports/` in the
HF repo so the metrics are reproducible from a single URL.

Naming convention:
    Laplaces-Red-Devils/physics-v{NN:02d}-{strategy}-{base-tag}
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from huggingface_hub import snapshot_download

from app.physics_solution import config
from app.physics_solution.shared.upload.hf import (
    VersionMeta,
    collect_env_info,
    load_token,
    now_utc,
    per_domain_breakdown,
    push,
)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--version-num", type=int, required=True)
    p.add_argument("--strategy", required=True,
                   help="zeroshot | fewshot | rag | lora | lora-rag | ...")
    p.add_argument("--base-tag", default=config.BASE_TAG,
                   help="Short tag used in the repo name.")
    p.add_argument("--base-model-id", default=config.BASE_MODEL_ID,
                   help="Upstream HF id (recorded in the model card).")
    p.add_argument("--local-dir", default=None,
                   help="Local model dir. If omitted, snapshot the upstream "
                        "base-model-id and push that.")
    p.add_argument("--description", default="",
                   help="Free-text describing the strategy. Empty -> a default.")
    p.add_argument("--notes", default="",
                   help="Extra notes appended to the model card.")
    p.add_argument("--results", default=None,
                   help="Path to a results JSON from inference.py (used to "
                        "populate ALL metrics + config fields on the card).")
    p.add_argument("--test-seed", type=int, default=42,
                   help="Seed used when building the test sample.")
    p.add_argument("--org", default=config.HF_ORG)
    p.add_argument("--public", action="store_true",
                   help="Push as a public repo (default: private).")
    p.add_argument("--snapshot-dir", default=".hf_snapshots",
                   help="Where to download upstream snapshots when --local-dir is unset.")
    return p.parse_args()


def load_results(path: str | None) -> tuple[dict, list[dict]]:
    """Return (summary, rows). Empty dicts if path missing."""
    if not path:
        return {}, []
    p = Path(path)
    if not p.exists():
        print(f"WARNING: results file not found at {p}")
        return {}, []
    data = json.loads(p.read_text(encoding="utf-8"))
    return data.get("summary", {}) or {}, data.get("rows", []) or []


def count_fewshot_pool() -> int | None:
    """Count examples in the v02 few-shot pool, if any."""
    p = Path("app/physics_solution/versions/v02_fewshot/examples.json")
    if not p.exists():
        return None
    try:
        return len(json.loads(p.read_text(encoding="utf-8")))
    except Exception:
        return None


def main() -> None:
    args = parse_args()
    token = load_token()

    if args.local_dir:
        local_dir = Path(args.local_dir)
        if not local_dir.exists():
            raise SystemExit(f"--local-dir does not exist: {local_dir}")
    else:
        snap_root = Path(args.snapshot_dir)
        snap_root.mkdir(parents=True, exist_ok=True)
        local_dir = Path(
            snapshot_download(
                repo_id=args.base_model_id,
                token=token,
                local_dir=str(snap_root / args.base_model_id.replace("/", "__")),
                local_dir_use_symlinks=False,
            )
        )
        print(f"Snapshotted {args.base_model_id} -> {local_dir}")

    summary, rows = load_results(args.results)
    env = collect_env_info()
    per_dom_acc, per_dom_cnt = per_domain_breakdown(rows) if rows else ({}, {})

    description = args.description or (
        f"Strategy `{args.strategy}` applied on top of {args.base_model_id}. "
        f"See app/physics_solution/versions/v{args.version_num:02d}_*/ for code."
    )

    meta = VersionMeta(
        # identity
        version_num=args.version_num,
        strategy=args.strategy,
        base=args.base_tag,
        description=description,
        base_model_id=args.base_model_id,
        # metrics
        test_accuracy=summary.get("accuracy"),
        test_n=summary.get("n"),
        test_correct=summary.get("correct"),
        mean_latency_s=summary.get("mean_latency_s"),
        per_domain_accuracy=per_dom_acc,
        per_domain_count=per_dom_cnt,
        # inference config (mirrors runner.summary fields)
        dtype=summary.get("dtype"),
        effective_dtype=summary.get("effective_dtype"),
        batch_size=summary.get("batch_size"),
        max_new_tokens=config.MAX_NEW_TOKENS,
        temperature=config.TEMPERATURE,
        assistant_prefix=summary.get("assistant_prefix"),
        n_examples=summary.get("n_examples"),
        # hardware (live capture)
        device=env.get("device"),
        gpu_name=env.get("gpu_name"),
        gpu_vram_gb=env.get("gpu_vram_gb"),
        cuda_version=env.get("cuda_version"),
        torch_version=env.get("torch_version"),
        transformers_version=env.get("transformers_version"),
        python_version=env.get("python_version"),
        # data
        test_file=config.TEST_FILE,
        test_seed=args.test_seed,
        fewshot_pool_size=count_fewshot_pool(),
        # misc
        timestamp_utc=now_utc(),
        notes=args.notes,
    )

    # Stage the results JSON + CSV under reports/ on the HF repo.
    extra_files: list[str] = []
    if args.results:
        json_path = Path(args.results)
        csv_path = json_path.with_suffix(".csv")
        if json_path.exists():
            extra_files.append(str(json_path))
        if csv_path.exists():
            extra_files.append(str(csv_path))

    repo_id = push(
        local_model_dir=local_dir,
        meta=meta,
        org=args.org,
        private=not args.public,
        token=token,
        extra_files=extra_files,
    )
    print(f"Pushed -> https://huggingface.co/{repo_id}")
    print(f"  model card includes:")
    print(f"    - test_accuracy: {meta.test_accuracy}")
    print(f"    - test_n: {meta.test_n}")
    print(f"    - batch_size: {meta.batch_size}")
    print(f"    - gpu: {meta.gpu_name} ({meta.gpu_vram_gb} GB)")
    print(f"    - torch: {meta.torch_version}, transformers: {meta.transformers_version}")
    print(f"    - per-domain accuracy across {len(meta.per_domain_accuracy)} domains")


if __name__ == "__main__":
    main()
