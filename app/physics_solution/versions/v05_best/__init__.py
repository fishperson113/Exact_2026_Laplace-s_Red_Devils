"""v05_best — optimised code execution: simple prompt, k=9e9, retry on error."""

VERSION_NUM = 5
STRATEGY_TAG = "best"
DEFAULT_BASE_TAG = "qwen3.5-4b"
DEFAULT_BASE_MODEL_ID = "Qwen/Qwen3.5-4B"
DESCRIPTION = (
    "Per-sample pipeline with 60s hard timeout: (1) classify domain+answer_type, "
    "(2) generate Python code (simple prompt, k=9e9 hardcoded, math/sympy/scipy allowed), "
    "(3) execute code and format output. Retry once with error context on execution failure."
)
