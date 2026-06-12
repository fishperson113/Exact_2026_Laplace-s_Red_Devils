from .prompt import (
    SYSTEM_PROMPT_FOL,
    USER_TEMPLATE_FOL,
    SYSTEM_PROMPT_QA,
    USER_TEMPLATE_QA,
    format_nl_block,        # FOL stage (1-indexed)
    format_premises_nl,     # QA stage (0-indexed)
    format_premises_fol,    # QA stage (0-indexed)
    format_options,         # QA stage (A./B./... hoặc thông báo free-form)
)
