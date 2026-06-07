"""Physics pipeline dispatcher — dynamic import from configured version.

Set PIPELINE_VERSION env var (or .env) to switch between versions:
    PIPELINE_VERSION=v05_best_vLLM   (default)

Each version must provide:
    app/physics_solution/versions/{version}/pipeline.py
        async def solve(question: str, client: VLLMClient, deadline: float) -> dict
"""

from __future__ import annotations

import time
from importlib import import_module

from app.api.schemas import AskRequest, QAResponse
from app.core.config import settings
from app.model.llm_client import physics_llm

# Lazily imported on first physics request so a LOGIC-ONLY gateway (physics
# vLLM not served, scipy/sympy not installed) still starts cleanly. The physics
# version module pulls in the code-exec stack, which logic deployments don't need.
_pipeline_mod = None


def _get_pipeline_mod():
    global _pipeline_mod
    if _pipeline_mod is None:
        _pipeline_mod = import_module(
            f"app.physics_solution.versions.{settings.pipeline_version}.pipeline"
        )
    return _pipeline_mod


async def solve_physics(question: str, deadline: float) -> dict:
    """Run the configured physics version. Returns a dict of QAResponse fields."""
    return await _get_pipeline_mod().solve(question, physics_llm, deadline)


async def run_qa_pipeline(request: AskRequest) -> QAResponse:
    """Back-compat wrapper for the standalone physics-only /ask path."""
    # Reserve 2s safety margin so the server can always return a response
    deadline = time.time() + settings.question_timeout_s - 2.0
    result = await solve_physics(request.question, deadline)
    return QAResponse(**result)
