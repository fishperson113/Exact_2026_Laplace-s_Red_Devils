"""Shared prompt utilities used by multiple versions."""

from __future__ import annotations

from langchain_core.messages import AIMessage, HumanMessage

from app.physics_solution.shared.prompts.system import ZEROSHOT_USER_TEMPLATE


def fewshot_messages_from(examples: list[dict]) -> list:
    """Build the alternating Human/AI messages for a list of few-shot examples.

    Each example is a dict from `versions/v02_fewshot/input/examples.json`:
        {"question": ..., "formatted_assistant": ..., "prefix": ...}
    """
    msgs: list = []
    for ex in examples:
        msgs.append(HumanMessage(content=ZEROSHOT_USER_TEMPLATE.format(question=ex["question"])))
        msgs.append(AIMessage(content=ex["formatted_assistant"]))
    return msgs
