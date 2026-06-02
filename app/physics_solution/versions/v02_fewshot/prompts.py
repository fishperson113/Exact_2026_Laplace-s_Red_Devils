"""v02 prompt template — few-shot with a messages placeholder."""

from __future__ import annotations

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


def build_template() -> ChatPromptTemplate:
    """Same as zero-shot but with a `few_shot_messages` placeholder that
    the runner fills per-question with HumanMessage / AIMessage pairs."""
    return ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template(PHYSICS_SYSTEM_EN),
            MessagesPlaceholder("few_shot_messages", optional=True),
            HumanMessagePromptTemplate.from_template(ZEROSHOT_USER_TEMPLATE),
        ]
    )
