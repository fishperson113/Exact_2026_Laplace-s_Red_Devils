from __future__ import annotations

from services.solvers.base import SolverResult, SymbolicSolver


class NoOpSolver:
    """Placeholder: không gọi engine; vẫn cho phép pipeline chạy và gen explanation từ LLM."""

    def prove_or_model(self, fol_formulas: list[str], question: str) -> SolverResult:  # noqa: ARG002
        return SolverResult(
            status="skipped",
            summary="No symbolic solver configured; reasoning left to the language model.",
            raw=None,
        )
