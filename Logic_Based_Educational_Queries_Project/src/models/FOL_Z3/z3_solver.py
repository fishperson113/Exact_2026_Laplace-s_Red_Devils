"""Stage 2: Parse FOL formulas va chay Z3 solver de kiem tra logic.

Input:  list[str] premises FOL + str question
Output: Z3Result (satisfiability, entailment checks, conclusions)

Duoc import boi: pipeline.py
Import tu:       evaluation.fol_parser, evaluation.fol_z3_translator
"""
from __future__ import annotations

from dataclasses import dataclass, field

from .config import FOLz3Config


@dataclass
class Z3Result:
    """Ket qua tu Z3 solver."""
    premises_parsed: list[str]           # FOL da parse thanh cong
    premises_failed: list[str]           # FOL parse that bai
    is_consistent: bool | None = None    # Tap premises co nhat quan?
    conclusions: list[str] = field(default_factory=list)  # Cac ket luan Z3 rut ra
    raw_status: str = "unknown"          # sat / unsat / unknown / error


class Z3Solver:
    """Parse FOL va chay Z3 de kiem tra tinh nhat quan + suy dien."""

    def __init__(self, cfg: FOLz3Config):
        self.timeout_ms = cfg.z3_timeout_ms
        self.max_premises = cfg.z3_max_premises

    def solve(self, premises_fol: list[str], question: str = "") -> Z3Result:
        """Parse premises FOL va chay Z3 satisfiability check."""
        from evaluation.fol_z3_translator import safe_fol_string_to_z3

        cache: dict = {}
        parsed_ok = []
        parsed_fail = []
        z3_exprs = []

        for fol in premises_fol[: self.max_premises]:
            expr = safe_fol_string_to_z3(fol, cache)
            if expr is not None:
                z3_exprs.append(expr)
                parsed_ok.append(fol)
            else:
                parsed_fail.append(fol)

        if not z3_exprs:
            return Z3Result(
                premises_parsed=parsed_ok,
                premises_failed=parsed_fail,
                raw_status="no_valid_premises",
            )

        # Check satisfiability
        import z3

        solver = z3.Solver()
        solver.set("timeout", self.timeout_ms)
        for expr in z3_exprs:
            solver.add(expr)

        result = solver.check()
        if result == z3.sat:
            status = "sat"
            is_consistent = True
        elif result == z3.unsat:
            status = "unsat"
            is_consistent = False
        else:
            status = "unknown"
            is_consistent = None

        # Rut ra conclusions tu Z3 model (neu sat)
        conclusions = []
        if is_consistent and result == z3.sat:
            model = solver.model()
            for decl in model.decls():
                val = model[decl]
                conclusions.append(f"{decl.name()} = {val}")

        return Z3Result(
            premises_parsed=parsed_ok,
            premises_failed=parsed_fail,
            is_consistent=is_consistent,
            conclusions=conclusions,
            raw_status=status,
        )

    def solve_safe(self, premises_fol: list[str], question: str = "") -> Z3Result:
        """Nhu solve() nhung fallback khi Z3 khong kha dung."""
        try:
            return self.solve(premises_fol, question)
        except ImportError:
            return Z3Result(
                premises_parsed=[],
                premises_failed=premises_fol,
                raw_status="z3_not_installed",
            )
        except Exception as e:
            return Z3Result(
                premises_parsed=[],
                premises_failed=premises_fol,
                raw_status=f"error: {type(e).__name__}",
            )
