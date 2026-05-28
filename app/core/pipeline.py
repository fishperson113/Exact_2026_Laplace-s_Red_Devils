"""Core pipeline dispatcher — dynamic import from configured version.

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
from app.model.llm_client import llm

# Load once at startup — fails fast if version is misconfigured
_pipeline_mod = import_module(
    f"app.physics_solution.versions.{settings.pipeline_version}.pipeline"
)


async def run_qa_pipeline(request: AskRequest) -> QAResponse:
    # Reserve 2s safety margin so the server can always return a response
    deadline = time.time() + settings.question_timeout_s - 2.0
    result: dict = await _pipeline_mod.solve(request.question, llm, deadline)
    return QAResponse(**result)
