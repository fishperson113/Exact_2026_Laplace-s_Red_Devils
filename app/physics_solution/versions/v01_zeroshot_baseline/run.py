"""v01 runner — zero-shot baseline via the LangChain LCEL pipeline."""

from __future__ import annotations

from app.physics_solution.shared.lc_prompts import build_zeroshot_template
from app.physics_solution.shared.runner import run_solver
from app.physics_solution.versions.v01_zeroshot_baseline import (
    DEFAULT_BASE_MODEL_ID,
    DESCRIPTION,
    STRATEGY_TAG,
    VERSION_NUM,
)


def _build_inputs(row: dict) -> dict:
    """Dataset row -> chain template variables. Zero-shot only needs the question."""
    return {"question": str(row["question"])}


def run(args) -> dict:
    return run_solver(
        args,
        version_num=VERSION_NUM,
        strategy_tag=STRATEGY_TAG,
        default_model_id=DEFAULT_BASE_MODEL_ID,
        description=DESCRIPTION,
        prompt_template=build_zeroshot_template(),
        build_inputs=_build_inputs,
    )
