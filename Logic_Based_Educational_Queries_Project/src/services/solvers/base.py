from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass
class SolverResult:
    status: str  # e.g. "sat", "unsat", "unknown", "skipped"
    summary: str  # văn bản ngắn cho LLM giải thích
    raw: str | None = None


class SymbolicSolver(Protocol):
    """Z3 / Prover9 / engine tùy chỉnh — cùng interface."""

    def prove_or_model(self, fol_formulas: list[str], question: str) -> SolverResult: ...
