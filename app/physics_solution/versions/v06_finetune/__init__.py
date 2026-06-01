"""v06_finetune — fine-tune Qwen3.5-4B to natively emit PoT code-gen.

Trains the model on execution-verified Program-of-Thought trajectories
(short reason + a single Python block that prints FINAL ANSWER / UNIT),
so it solves physics problems without long prompts or few-shot examples.

Inference reuses the v05_best shape: 1 code block + retry-once-on-error.
The new work is the data + training pipelines (see data_pipeline/ + train/).
"""

VERSION_NUM = 6
STRATEGY_TAG = "finetune"
DEFAULT_BASE_TAG = "qwen3.5-4b"
DEFAULT_BASE_MODEL_ID = "Qwen/Qwen3.5-4B"
DESCRIPTION = (
    "Fine-tuned (Unsloth QLoRA) Qwen3.5-4B on execution-verified PoT code-gen "
    "trajectories. Inference: classify domain+answer_type, generate one Python "
    "script (short reason + code), execute, retry once on error. Trained from "
    "self-gen (Route-1, on-policy) + DeepSeek teacher residual (Route-2/3)."
)
