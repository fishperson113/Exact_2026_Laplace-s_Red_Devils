from typing import Optional, List
from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    question: str


class QAResponse(BaseModel):
    answer: str
    explanation: str
    fol: Optional[str] = None
    cot: Optional[List[str]] = None
    premises: Optional[List[str]] = None
    confidence: Optional[float] = Field(None, ge=0.0, le=1.0)
