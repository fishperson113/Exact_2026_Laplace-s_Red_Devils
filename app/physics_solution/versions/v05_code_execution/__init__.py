"""v05 — code execution: generate Python code to solve physics problems numerically."""

VERSION_NUM = 5
STRATEGY_TAG = "code_execution"
DEFAULT_BASE_TAG = "qwen3.5-4b"
DEFAULT_BASE_MODEL_ID = "Qwen/Qwen3.5-4B"
DESCRIPTION = (
    "3-stage pipeline: (1) Router classifies domain+answer_type, "
    "(2) Code Generator produces Python code to compute the answer, "
    "(3) Execute code and format output. Falls back to direct LLM "
    "solve for text-based answers or when code execution fails."
)
