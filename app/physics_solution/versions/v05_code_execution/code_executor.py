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


def execute_code(code: str, timeout: int = 10) -> ExecutionResult:
    """Run code in a subprocess, parse FINAL ANSWER / UNIT from stdout."""
    imports = _IMPORT_RE.findall(code)
    non_math = [m for m in imports if m != "math"]
    if non_math:
        warning = f"# WARNING: non-math imports detected: {non_math}\n"
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


# ------------------------------------------------------------------ tests

if __name__ == "__main__":
    passed = 0
    total = 0

    def check(label: str, condition: bool):
        global passed, total
        total += 1
        if condition:
            passed += 1
            print(f"  [PASS] {label}")
        else:
            print(f"  [FAIL] {label}")

    # --- extract_code ---
    print("=== extract_code ===")

    check("python tag",
          extract_code("Here:\n```python\nimport math\nprint(1)\n```\n") == "import math\nprint(1)")

    check("no language tag",
          extract_code("```\nprint(2)\n```") == "print(2)")

    check("multiple blocks (takes last)",
          extract_code("```python\nx=1\n```\ntext\n```python\nx=2\n```") == "x=2")

    check("no code block returns None",
          extract_code("Just some text without any code") is None)

    check("empty input",
          extract_code("") is None)

    # --- execute_code ---
    print("\n=== execute_code ===")

    r = execute_code('import math\nF = math.pi\nprint(f"FINAL ANSWER: {F}")\nprint("UNIT: rad")')
    check("happy path: success", r.success is True)
    check("happy path: answer parsed", r.answer is not None and "3.14159" in r.answer)
    check("happy path: unit parsed", r.unit == "rad")
    check("happy path: no error", r.error_type is None)

    r = execute_code("def foo(\n  pass")
    check("syntax error: not success", r.success is False)
    check("syntax error: type", r.error_type == "syntax")

    r = execute_code("x = 1 / 0")
    check("runtime error: not success", r.success is False)
    check("runtime error: type", r.error_type == "runtime")

    r = execute_code("while True: pass", timeout=2)
    check("timeout: not success", r.success is False)
    check("timeout: type", r.error_type == "timeout")

    r = execute_code('print("hello world")')
    check("no FINAL ANSWER: parse error", r.success is False)
    check("no FINAL ANSWER: type", r.error_type == "parse")

    r = execute_code(
        'print("debug info")\nprint("more debug")\n'
        'print("FINAL ANSWER: 42.0")\nprint("UNIT: m")'
    )
    check("extra output: success", r.success is True)
    check("extra output: answer", r.answer == "42.0")
    check("extra output: unit", r.unit == "m")

    r = execute_code('print("FINAL ANSWER: 5.4e-06")\nprint("UNIT: C")')
    check("sci notation: success", r.success is True)
    check("sci notation: answer", r.answer == "5.4e-06")

    # --- format_answer ---
    print("\n=== format_answer ===")

    check("plain number",
          format_answer("42.0", "m") == "FINAL ANSWER: 42.0\nUNIT: m")

    check("e-notation negative exp",
          format_answer("5.4e-06", "C") == "FINAL ANSWER: 5.4 * 10^{-6}\nUNIT: C")

    check("e-notation positive exp",
          format_answer("5.4e+06", "Hz") == "FINAL ANSWER: 5.4 * 10^{6}\nUNIT: Hz")

    check("e-notation no sign",
          format_answer("3.0e8", "m/s") == "FINAL ANSWER: 3.0 * 10^{8}\nUNIT: m/s")

    check("already plain",
          format_answer("5400000.0", "N") == "FINAL ANSWER: 5400000.0\nUNIT: N")

    # --- end-to-end: extract + execute + format ---
    print("\n=== end-to-end ===")

    llm_output = """Here's the solution:

```python
import math

q1 = 2e-6
q2 = -3e-6
r = 0.10
k = 9e9

F = k * abs(q1) * abs(q2) / r**2

print(f"FINAL ANSWER: {F}")
print(f"UNIT: N")
```
"""
    code = extract_code(llm_output)
    check("e2e: code extracted", code is not None)
    if code:
        r = execute_code(code)
        check("e2e: execution success", r.success is True)
        check("e2e: answer close to 5.4", abs(float(r.answer) - 5.4) < 1e-6)
        check("e2e: unit correct", r.unit == "N")
        if r.answer and r.unit:
            fmt = format_answer(r.answer, r.unit)
            check("e2e: formatted has FINAL ANSWER",
                  fmt.startswith("FINAL ANSWER:") and "UNIT: N" in fmt)

    print(f"\n{'='*40}\n{passed}/{total} tests passed")
