from __future__ import annotations

from services.solvers.base import SolverResult


class Z3SolverIfAvailable:
    """
    Stub mở rộng: cài `z3-solver` và parse FOL → Z3 AST khi team sẵn sàng.
    Hiện tại luôn trả unknown để không phá training notebook.
    """

    def prove_or_model(self, fol_formulas: list[str], question: str) -> SolverResult:  # noqa: ARG002
        return SolverResult(
            status="unknown",
            summary=(
                "Z3 bridge not implemented for this FOL syntax. "
                f"Received {len(fol_formulas)} formulas; integrate parsing in services.solvers.z3_solver."
            ),
            raw=None,
        )
