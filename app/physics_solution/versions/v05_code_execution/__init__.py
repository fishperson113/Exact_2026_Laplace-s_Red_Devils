"""v05 — code execution: generate Python code to solve physics problems numerically."""

VERSION_NUM = 5
STRATEGY_TAG = "code_execution"
DEFAULT_BASE_TAG = "qwen3.5-4b"
DEFAULT_BASE_MODEL_ID = "Qwen/Qwen3.5-4B"
DESCRIPTION = (
    "Per-sample pipeline with 60s hard timeout: (1) classify domain+answer_type, "
    "(2) generate Python code to compute the answer, "
    "(3) execute code and format output. One retry on failure, no fallback."
)
