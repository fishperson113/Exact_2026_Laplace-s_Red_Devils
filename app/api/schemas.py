from typing import Optional
from pydantic import BaseModel, Field


# ============================================================== #
#  Task Type 2: Physics                                          #
# ============================================================== #

class AskRequest(BaseModel):
    question: str


class QAResponse(BaseModel):
    answer: str
    unit: str
    explanation: str
    cot: str
    confidence: Optional[float] = Field(None, ge=0.0, le=1.0)
    solve_method: str                       # "code_execution" | "failed" | "timeout"
    elapsed_s: float
    # debug fields — populated when pipeline has extra info
    domain: Optional[str] = None
    answer_type: Optional[str] = None
    generated_code: Optional[str] = None
    execution_stdout: Optional[str] = None


# ============================================================== #
#  Task Type 1: Education Logic (placeholder — adapt later)      #
# ============================================================== #

class LogicAskRequest(BaseModel):
    """Input for an education-logic question (Task Type 1).

    Adapt fields when the real spec is finalized. Current shape mirrors
    the physics track so the eval tooling is reusable.
    """
    question: str
    choices: Optional[list[str]] = Field(
        None,
        description="Answer choices for multiple-choice questions (A/B/C/D).",
    )


class LogicQAResponse(BaseModel):
    """Output for education-logic questions.

    Fields intentionally parallel QAResponse so eval_api.py / scorer can
    be reused with minimal changes.
    """
    answer: str                             # e.g. "A", "B", or free-text
    explanation: str
    cot: str
    confidence: Optional[float] = Field(None, ge=0.0, le=1.0)
    solve_method: str                       # "direct" | "cot" | "failed" | "timeout"
    elapsed_s: float
    domain: Optional[str] = None            # e.g. "logic", "math_reasoning", "reading"
