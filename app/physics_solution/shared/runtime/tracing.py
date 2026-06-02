"""LangSmith tracing setup.

Use this from any version's `run.py`:

    from app.physics_solution.shared.tracing import setup_tracing, traceable

    setup_tracing(project_name="exact26-physics-type2", version="v01_zeroshot")

    @traceable(name="solve_question", run_type="chain")
    def solve_one(qid, question, ...): ...

If `LANGSMITH_API_KEY` is not set in the environment, `setup_tracing` is a
no-op and `traceable` becomes the identity decorator — so the code runs
unmodified locally without LangSmith installed.
"""

from __future__ import annotations

import os
from typing import Callable

# Safe import — keep the codebase usable without langsmith installed.
try:
    from langsmith import traceable as _traceable  # type: ignore

    _HAS_LANGSMITH = True
except Exception:  # pragma: no cover

    def _traceable(*args, **kwargs):  # type: ignore
        # Support both @traceable and @traceable(name=...) forms.
        if args and callable(args[0]):
            return args[0]

        def _deco(fn: Callable) -> Callable:
            return fn

        return _deco

    _HAS_LANGSMITH = False


# Re-export under the public name.
traceable = _traceable


def setup_tracing(
    project_name: str = "exact26-physics-type2",
    version: str | None = None,
    enabled: bool | None = None,
) -> bool:
    """Configure env vars for LangSmith. Returns True if tracing is on.

    Reads `LANGSMITH_API_KEY` from the env (Colab Secrets pump this in via
    `os.environ['LANGSMITH_API_KEY'] = userdata.get('LANGSMITH_API_KEY')`).
    """
    if not _HAS_LANGSMITH:
        if enabled:
            print("[tracing] langsmith not installed — skipping setup.")
        return False

    api_key = os.environ.get("LANGSMITH_API_KEY")
    if not api_key:
        if enabled:
            print("[tracing] LANGSMITH_API_KEY missing — skipping setup.")
        return False

    if enabled is False:
        return False

    os.environ["LANGSMITH_TRACING"] = "true"
    # The newer client name; keep the legacy var in sync for compatibility.
    os.environ.setdefault("LANGCHAIN_TRACING_V2", "true")
    os.environ["LANGSMITH_PROJECT"] = project_name
    os.environ.setdefault("LANGCHAIN_PROJECT", project_name)
    if version:
        os.environ["LANGSMITH_SESSION"] = version

    print(f"[tracing] LangSmith ON — project={project_name} version={version}")
    return True
