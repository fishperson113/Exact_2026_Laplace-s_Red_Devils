"""Version-specific prompt template. Customize build_template()."""

from __future__ import annotations

from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

from app.physics_solution.shared.prompts.system import (
    PHYSICS_SYSTEM_EN,
    ZEROSHOT_USER_TEMPLATE,
)


def build_template() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template(PHYSICS_SYSTEM_EN),
            HumanMessagePromptTemplate.from_template(ZEROSHOT_USER_TEMPLATE),
        ]
    )
