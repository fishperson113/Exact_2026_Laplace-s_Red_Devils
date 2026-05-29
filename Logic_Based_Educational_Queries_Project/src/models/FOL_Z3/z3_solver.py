"""Stage 2: Parse FOL formulas va chay Z3 solver de kiem tra logic.

Input:  list[str] premises FOL + str question (FOL)
Output: Z3Result (satisfiability + entailment check)

Z3 lam 2 viec:
  1. Consistency check: premises co mau thuan nhau khong? (sat/unsat)
  2. Entailment check:  premises co suy ra duoc question khong?
     - premises ∧ ¬question → unsat  ⟹  ENTAILED  (Yes)
     - premises ∧  question → unsat  ⟹  CONTRADICTED (No)
     - Ca hai sat                    ⟹  UNKNOWN

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
    entailment: str = "unknown"          # entailed / contradicted / unknown / error
    conclusions: list[str] = field(default_factory=list)  # Model assignments (khi sat)
    raw_status: str = "unknown"          # sat / unsat / unknown / error


class Z3Solver:
    """Parse FOL va chay Z3: consistency check + entailment check."""

    def __init__(self, cfg: FOLz3Config):
        self.timeout_ms = cfg.z3_timeout_ms
        self.max_premises = cfg.z3_max_premises

    def solve(self, premises_fol: list[str], question_fol: str = "") -> Z3Result:
        """Parse premises FOL, check consistency, roi check entailment voi question_fol."""
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

        import z3

        # --- 1. Consistency check: premises co mau thuan? ---
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

        # Model assignments (khi sat)
        conclusions = []
        if is_consistent and result == z3.sat:
            model = solver.model()
            for decl in model.decls():
                val = model[decl]
                conclusions.append(f"{decl.name()} = {val}")

        # --- 2. Entailment check: premises ⊨ question? ---
        entailment = "unknown"
        if is_consistent and question_fol.strip():
            q_expr = safe_fol_string_to_z3(question_fol, cache)
            if q_expr is not None:
                entailment = self._check_entailment(z3_exprs, q_expr)

        return Z3Result(
            premises_parsed=parsed_ok,
            premises_failed=parsed_fail,
            is_consistent=is_consistent,
            entailment=entailment,
            conclusions=conclusions,
            raw_status=status,
        )

    def _check_entailment(self, premises_z3: list, question_z3) -> str:
        """Check premises ⊨ question bang Z3.

        - premises ∧ ¬question → unsat  ⟹  "entailed"
        - premises ∧  question → unsat  ⟹  "contradicted"
        - Ca hai sat                    ⟹  "unknown"
        """
        import z3

        # Check: premises ∧ ¬question
        s1 = z3.Solver()
        s1.set("timeout", self.timeout_ms)
        for p in premises_z3:
            s1.add(p)
        s1.add(z3.Not(question_z3))
        r1 = s1.check()

        if r1 == z3.unsat:
            return "entailed"      # ¬Q khong the xay ra → premises suy ra Q

        # Check: premises ∧ question
        s2 = z3.Solver()
        s2.set("timeout", self.timeout_ms)
        for p in premises_z3:
            s2.add(p)
        s2.add(question_z3)
        r2 = s2.check()

        if r2 == z3.unsat:
            return "contradicted"  # Q khong the xay ra → premises phu dinh Q

        return "unknown"           # Ca hai deu co the → khong ket luan duoc

    def solve_safe(self, premises_fol: list[str], question_fol: str = "") -> Z3Result:
        """Nhu solve() nhung fallback khi Z3 khong kha dung."""
        try:
            return self.solve(premises_fol, question_fol)
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
