"""LangChain prompt templates for the physics solver.

Two builders:

- `build_zeroshot_template()` — system + user, no examples.
- `build_fewshot_template(examples, n_per_question)` — system + K worked
  examples + user. The example selection (by domain prefix) happens at
  chain-build time inside the runner; here we just expose templates.
"""

from __future__ import annotations

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)

from app.physics_solution.shared.prompts.system import (
    PHYSICS_SYSTEM_EN,
    ZEROSHOT_USER_TEMPLATE,
)


def build_zeroshot_template() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template(PHYSICS_SYSTEM_EN),
            HumanMessagePromptTemplate.from_template(ZEROSHOT_USER_TEMPLATE),
        ]
    )


def build_fewshot_template() -> ChatPromptTemplate:
    """Same as zero-shot but with a `few_shot_messages` placeholder that
    the runner fills per-question with HumanMessage / AIMessage pairs."""
    return ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template(PHYSICS_SYSTEM_EN),
            MessagesPlaceholder("few_shot_messages", optional=True),
            HumanMessagePromptTemplate.from_template(ZEROSHOT_USER_TEMPLATE),
        ]
    )


def fewshot_messages_from(examples: list[dict]) -> list:
    """Build the alternating Human/AI messages for a list of few-shot examples.

    Each example is a dict from `versions/v02_fewshot/examples.json`:
        {"question": ..., "formatted_assistant": ..., "prefix": ...}
    """
    msgs: list = []
    for ex in examples:
        msgs.append(HumanMessage(content=ZEROSHOT_USER_TEMPLATE.format(question=ex["question"])))
        msgs.append(AIMessage(content=ex["formatted_assistant"]))
    return msgs
