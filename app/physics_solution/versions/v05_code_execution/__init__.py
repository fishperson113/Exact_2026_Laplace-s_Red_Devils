"""v05 — code execution: generate Python code to solve physics problems numerically."""

VERSION_NUM = 5
STRATEGY_TAG = "code_execution"
DEFAULT_BASE_TAG = "qwen3.5-4b"
DEFAULT_BASE_MODEL_ID = "Qwen/Qwen3.5-4B"
DESCRIPTION = (
    "Three-pass pipeline: Pass 1 classifies (domain, answer_type); "
    "Pass 2 generates Python code using domain-specific formula hints; "
    "Pass 3 executes the code in a sandbox and extracts the numeric answer."
)
