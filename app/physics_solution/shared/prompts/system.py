"""Shared prompt templates for Physics Type 2 solutions.

Design notes:
- Long rule-style system prompts make Qwen-family models echo the rules
  back as a "Thinking Process: Analyze the Request:" preamble. We use a
  short declarative tone instead, demonstrate the format inline, and let
  few-shot examples (v02) anchor the rest.
- Median CoT in the training data is 4 steps. We aim for similar.
"""

PHYSICS_SYSTEM_EN = """You are a physics tutor for electrical circuits and electrostatics. You answer in English using SI units.

Write a short numbered reasoning chain, then the final answer. Use this format exactly:

Step 1: <one short sentence>
Step 2: <one short sentence>
...
FINAL ANSWER: <plain decimal, no unit>
UNIT: <unit symbol>

Keep it tight: 3-5 steps is usually enough. Commit to one reading of the problem; do not enumerate alternatives. Stop after the UNIT line."""


ZEROSHOT_USER_TEMPLATE = """{question}"""


# Optional assistant-turn prefill. Empty = let the model start naturally.
# Set to "Step 1:" to hard-force the opening token if a model keeps
# echoing the rules back as a preamble.
ASSISTANT_PREFIX = ""


def build_zeroshot_messages(question: str) -> list[dict]:
    """Return a chat-message list compatible with tokenizer.apply_chat_template."""
    return [
        {"role": "system", "content": PHYSICS_SYSTEM_EN},
        {"role": "user", "content": ZEROSHOT_USER_TEMPLATE.format(question=question)},
    ]


def build_zeroshot_raw_prompt(question: str) -> str:
    """Fallback when the tokenizer has no chat template (base models)."""
    return (
        PHYSICS_SYSTEM_EN
        + "\n\n"
        + ZEROSHOT_USER_TEMPLATE.format(question=question)
        + "\n\nSolution:\n"
    )
