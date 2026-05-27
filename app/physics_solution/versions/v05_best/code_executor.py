"""Execute LLM-generated Python code and parse structured output."""

from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass


_CODE_BLOCK_RE = re.compile(r"```(?:python)?\s*\n(.*?)```", re.DOTALL)
_FINAL_RE = re.compile(r"FINAL\s*ANSWER\s*:\s*(.+)", re.IGNORECASE)
_UNIT_RE = re.compile(r"UNIT\s*:\s*(.+)", re.IGNORECASE)
_IMPORT_RE = re.compile(r"^\s*(?:import|from)\s+(\w+)", re.MULTILINE)
_E_NOTATION_RE = re.compile(r"^([+-]?\d+(?:\.\d+)?)[eE]([+-]?\d+)$")


@dataclass
class ExecutionResult:
    success: bool
    stdout: str
    stderr: str
    answer: str | None
    unit: str | None
    error_type: str | None


def extract_code(llm_output: str) -> str | None:
    """Extract Python code from the last markdown code block in llm_output."""
    blocks = _CODE_BLOCK_RE.findall(llm_output)
    if not blocks:
        return None
    return blocks[-1].strip()


_ALLOWED_IMPORTS = {"math", "sympy", "scipy", "numpy"}


def execute_code(code: str, timeout: int = 10) -> ExecutionResult:
    """Run code in a subprocess, parse FINAL ANSWER / UNIT from stdout."""
    imports = _IMPORT_RE.findall(code)
    disallowed = [m for m in imports if m not in _ALLOWED_IMPORTS]
    if disallowed:
        warning = f"# WARNING: disallowed imports detected: {disallowed}\n"
        code = warning + code

    fd, path = tempfile.mkstemp(suffix=".py", prefix="exec_")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(code)

        try:
            proc = subprocess.run(
                [sys.executable, path],
                capture_output=True,
                text=True,
                timeout=timeout,
            )
        except subprocess.TimeoutExpired:
            return ExecutionResult(
                success=False, stdout="", stderr="Execution timed out",
                answer=None, unit=None, error_type="timeout",
            )

        stdout = proc.stdout
        stderr = proc.stderr

        if proc.returncode != 0:
            err_type = "syntax" if "SyntaxError" in stderr else "runtime"
            return ExecutionResult(
                success=False, stdout=stdout, stderr=stderr,
                answer=None, unit=None, error_type=err_type,
            )

        ans_match = _FINAL_RE.search(stdout)
        unit_match = _UNIT_RE.search(stdout)

        answer = ans_match.group(1).strip() if ans_match else None
        unit = unit_match.group(1).strip() if unit_match else None

        if answer is None:
            return ExecutionResult(
                success=False, stdout=stdout, stderr=stderr,
                answer=None, unit=unit, error_type="parse",
            )

        return ExecutionResult(
            success=True, stdout=stdout, stderr=stderr,
            answer=answer, unit=unit, error_type=None,
        )
    finally:
        try:
            os.unlink(path)
        except OSError:
            pass


def format_answer(answer: str, unit: str) -> str:
    """Format answer + unit for competition output, converting e-notation."""
    m = _E_NOTATION_RE.match(answer.strip())
    if m:
        mantissa, exponent = m.group(1), m.group(2)
        exponent_val = int(exponent)
        if exponent_val >= 0:
            exponent_str = str(exponent_val)
        else:
            exponent_str = str(exponent_val)
        answer = f"{mantissa} * 10^{{{exponent_str}}}"

    return f"FINAL ANSWER: {answer}\nUNIT: {unit}"
