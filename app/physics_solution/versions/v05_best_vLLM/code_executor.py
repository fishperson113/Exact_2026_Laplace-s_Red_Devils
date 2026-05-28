"""Async code executor for v05_best_vLLM.

Reuses all parsing logic from v05_best.code_executor; adds execute_code_async()
using asyncio subprocesses so the event loop is not blocked during code execution.
Other requests can proceed while Python code runs.
"""

from __future__ import annotations

import asyncio
import os
import sys
import tempfile

# Re-export everything from v05_best so import paths are interchangeable
from app.physics_solution.versions.v05_best.code_executor import (  # noqa: F401
    ExecutionResult,
    extract_code,
    format_answer,
    _ALLOWED_IMPORTS,
    _CODE_BLOCK_RE,
    _E_NOTATION_RE,
    _FINAL_RE,
    _IMPORT_RE,
    _UNIT_RE,
)


async def execute_code_async(code: str, timeout: int = 10) -> ExecutionResult:
    """Non-blocking equivalent of execute_code() using asyncio subprocesses.

    Yields the event loop during subprocess execution, allowing other /ask
    requests to progress (classify / codegen calls to vLLM) concurrently.
    """
    imports = _IMPORT_RE.findall(code)
    disallowed = [m for m in imports if m not in _ALLOWED_IMPORTS]
    if disallowed:
        code = f"# WARNING: disallowed imports detected: {disallowed}\n" + code

    fd, path = tempfile.mkstemp(suffix=".py", prefix="exec_async_")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(code)

        try:
            proc = await asyncio.create_subprocess_exec(
                sys.executable,
                path,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            stdout_b, stderr_b = await asyncio.wait_for(
                proc.communicate(), timeout=timeout
            )
        except asyncio.TimeoutError:
            try:
                proc.kill()
            except ProcessLookupError:
                pass
            return ExecutionResult(
                success=False,
                stdout="",
                stderr="Execution timed out",
                answer=None,
                unit=None,
                error_type="timeout",
            )

        stdout = stdout_b.decode("utf-8", errors="replace")
        stderr = stderr_b.decode("utf-8", errors="replace")

        if proc.returncode != 0:
            err_type = "syntax" if "SyntaxError" in stderr else "runtime"
            return ExecutionResult(
                success=False,
                stdout=stdout,
                stderr=stderr,
                answer=None,
                unit=None,
                error_type=err_type,
            )

        ans_match = _FINAL_RE.search(stdout)
        unit_match = _UNIT_RE.search(stdout)
        answer = ans_match.group(1).strip() if ans_match else None
        unit = unit_match.group(1).strip() if unit_match else None

        if answer is None:
            return ExecutionResult(
                success=False,
                stdout=stdout,
                stderr=stderr,
                answer=None,
                unit=unit,
                error_type="parse",
            )

        return ExecutionResult(
            success=True,
            stdout=stdout,
            stderr=stderr,
            answer=answer,
            unit=unit,
            error_type=None,
        )
    finally:
        try:
            os.unlink(path)
        except OSError:
            pass
