"""Top-level inference dispatcher.

Defaults come from `app.physics_solution.config`. CLI flags override.
Inside a Colab notebook you can run with zero flags:

    !python -m app.physics_solution.cli.inference --version v02_fewshot

To override one knob ad-hoc:

    !python -m app.physics_solution.cli.inference --version v02_fewshot --limit 10

Permanent changes belong in `config.py`, not in notebook cells.
"""

from __future__ import annotations

import argparse
from importlib import import_module

from app.physics_solution import config


VERSIONS = {
    "v01_zeroshot_baseline":  "app.physics_solution.versions.v01_zeroshot_baseline.run",
    "v02_fewshot":            "app.physics_solution.versions.v02_fewshot.run",
    "v03_routed_fewshot":     "app.physics_solution.versions.v03_routed_fewshot.run",
    "v04_optimized_routing":  "app.physics_solution.versions.v04_optimized_routing.run",
    "v05_code_execution":     "app.physics_solution.versions.v05_code_execution.run",
}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Physics Type 2 inference dispatcher")
    p.add_argument(
        "--version",
        required=True,
        choices=sorted(VERSIONS),
        help="Which solution version to run (folder name under versions/).",
    )
    p.add_argument("--model-id", default=config.BASE_MODEL_ID)
    p.add_argument("--test-file", default=config.TEST_FILE)
    p.add_argument("--out", default=None)
    p.add_argument(
        "--dtype",
        choices=["fp32", "fp16", "bf16", "int8", "fp8"],
        default=config.DTYPE,
    )
    p.add_argument("--device", default=config.DEVICE)
    p.add_argument("--max-new-tokens", type=int, default=config.MAX_NEW_TOKENS)
    p.add_argument("--temperature", type=float, default=config.TEMPERATURE)
    p.add_argument("--limit", type=int, default=config.LIMIT)
    p.add_argument(
        "--n-examples",
        type=int,
        default=None,
        help="Number of few-shot examples per question (v02+). "
             "None = use version default.",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()
    module_path = VERSIONS[args.version]
    module = import_module(module_path)
    module.run(args)


if __name__ == "__main__":
    main()
