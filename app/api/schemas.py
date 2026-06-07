from typing import Optional
from pydantic import AliasChoices, BaseModel, ConfigDict, Field


# ============================================================== #
#  Unified request — single /ask endpoint for BOTH task types    #
# ============================================================== #

class UnifiedAskRequest(BaseModel):
    """One request shape for the single competition endpoint.

    Routing is by the *presence* of premises (done in routes/ask.py):
        Type 1 (logic):   {"premises-NL": ["...", ...], "question": "..."}
        Type 2 (physics): {"question": "..."}

    BTC sends the hyphenated key ``premises-NL``; we also accept the
    underscore variants for internal/eval tooling.
    """

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    question: str
    premises_nl: Optional[list[str]] = Field(
        default=None,
        validation_alias=AliasChoices("premises-NL", "premises_nl", "premises_NL"),
    )


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
#  Task Type 1: Education Logic                                  #
# ============================================================== #

class LogicQAResponse(BaseModel):
    """Output for education-logic questions.

    BTC submission fields are answer/explanation/fol; cot/confidence feed P3.
    """
    answer: str                             # "A".."D" | "Yes"/"No" | "Unknown"
    explanation: str
    fol: str                                # FOL premises, joined by "\n"
    cot: str = ""
    confidence: Optional[float] = Field(None, ge=0.0, le=1.0)
    solve_method: str = "fol_qa"            # "fol_qa" | "timeout"
    elapsed_s: float = 0.0
    domain: Optional[str] = "logic"
