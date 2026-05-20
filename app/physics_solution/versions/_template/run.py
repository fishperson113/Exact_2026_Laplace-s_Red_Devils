"""Version runner template. Customize imports and build_inputs."""

from __future__ import annotations

from app.physics_solution.shared.runtime.runner import run_solver

# Update this import to match your version folder name.
from app.physics_solution.versions._template import (
    DEFAULT_BASE_MODEL_ID,
    DESCRIPTION,
    STRATEGY_TAG,
    VERSION_NUM,
)
from app.physics_solution.versions._template.prompts import build_template


def _build_inputs(row: dict) -> dict:
    return {"question": str(row["question"])}


def run(args) -> dict:
    return run_solver(
        args,
        version_num=VERSION_NUM,
        strategy_tag=STRATEGY_TAG,
        default_model_id=DEFAULT_BASE_MODEL_ID,
        description=DESCRIPTION,
        prompt_template=build_template(),
        build_inputs=_build_inputs,
    )
