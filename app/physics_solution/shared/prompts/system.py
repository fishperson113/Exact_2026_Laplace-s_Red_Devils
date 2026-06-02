"""Shared prompt templates for Physics Type 2 solutions.

Design notes:
- Long rule-style system prompts make Qwen-family models echo the rules
  back as a "Thinking Process: Analyze the Request:" preamble. We use a
  short declarative tone instead, demonstrate the format inline, and let
  few-shot examples (v02) anchor the rest.
- Median CoT in the training data is 4 steps. We aim for similar.
"""

PHYSICS_SYSTEM_EN = """You are a physics tutor for electrical circuits and electrostatics. You answer in English using SI units.

Write a short numbered reasoning chain using LaTeX inline math ($...$), then the final answer. Format:

Step 1: <one short sentence>
Step 2: <one short sentence>
...
FINAL ANSWER: <answer>
UNIT: <unit symbol, or - if dimensionless>

For large/small numbers (|exponent| >= 4), write a * 10^{{n}}. NEVER use e-notation.
WRONG: 2.97e6 | RIGHT: 2.97 * 10^{{6}}

Example:
Step 1: Calculate $E_1 = k|q_1|/r_1^2 = 1.525 * 10^6$ V/m.
Step 2: Calculate $E_2 = k|q_2|/r_2^2 = 5.022 * 10^5$ V/m.
Step 3: Net field $E = E_1 + E_2 = 2.027 * 10^6$ V/m.
FINAL ANSWER: 2.027 * 10^{{6}}
UNIT: V/m

Keep it tight: 3-5 steps. Commit to one reading of the problem. Stop after the UNIT line."""


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
