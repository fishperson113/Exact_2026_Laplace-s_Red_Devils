"""FOL_Z3 Pipeline — Orchestrator ket noi 3 stages + timing log.

Stage 1: FOLInference  — NL premises -> FOL premises  (fol_inference.py)
Stage 2: Z3Solver      — FOL premises -> Z3Result     (z3_solver.py)
Stage 3: QAInference   — FOL + Z3 + question -> JSON  (qa_inference.py)

Duoc import boi: __init__.py
Import tu:       .config, .fol_inference, .z3_solver, .qa_inference
"""
from __future__ import annotations

import re
import time
from dataclasses import dataclass, field
from pathlib import Path

from .config import FOLz3Config
from .fol_inference import FOLInference
from .z3_solver import Z3Result, Z3Solver
from .qa_inference import QAInference


@dataclass
class TimingLog:
    """Thoi gian inference tung stage (giay)."""
    fol_sec: float = 0.0       # Stage 1: FOL inference
    z3_sec: float = 0.0        # Stage 2: Z3 solving
    qa_sec: float = 0.0        # Stage 3: QA inference
    total_sec: float = 0.0     # Tong thoi gian 1 sample


@dataclass
class PipelineResult:
    """Ket qua cuoi cung tu pipeline."""
    answer: str                    # A / B / C / D / Yes / No / Unknown
    explanation: str               # Giai thich tu QA model
    premises_fol: list[str]        # FOL output tu Stage 1
    question_fol: str              # FOL cua question (tu Stage 1)
    z3_result: Z3Result            # Z3 output tu Stage 2
    options_fol: dict[str, str] = field(default_factory=dict)  # MCQ: {"A":"FOL",...}
    timing: TimingLog = field(default_factory=TimingLog)


def parse_mcq_options(question: str) -> dict[str, str]:
    """Tach lua chon A/B/C/D tu question text MCQ.

    Returns {"A": "option text", ...}. Dict rong neu khong phai MCQ.
    """
    options = {}
    for line in question.split("\n"):
        m = re.match(r"^\s*([A-D])[.):\s]+(.+)$", line.strip())
        if m:
            options[m.group(1)] = m.group(2).strip()
    return options


class FOLz3Pipeline:
    """Pipeline: FOL Model -> Z3 Solver -> QA Model -> JSON {answer, explanation}."""

    def __init__(self, cfg: FOLz3Config):
        self.cfg = cfg
        self.qa = QAInference(cfg)

        if cfg.use_fol:
            self.fol = FOLInference(cfg)
            self.z3 = Z3Solver(cfg)
            print("[Pipeline] All 3 stages loaded (FOL + Z3 + QA).")
        else:
            self.fol = None
            self.z3 = None
            print("[Pipeline] Baseline mode (QA only, no FOL/Z3).")

    @classmethod
    def from_yaml(cls, yaml_path: str | Path) -> FOLz3Pipeline:
        """Tao pipeline tu YAML config file."""
        cfg = FOLz3Config.from_yaml(yaml_path)
        return cls(cfg)

    def run(self, premises_nl: list[str], question: str) -> PipelineResult:
        """Chay pipeline theo cfg.use_fol:
        - True:  NL -> FOL -> Z3 -> QA (full pipeline)
        - False: NL -> QA (baseline, khong FOL/Z3)
        """
        t_start = time.perf_counter()
        timing = TimingLog()

        if not self.cfg.use_fol:
            # Baseline: chi NL -> QA
            t0 = time.perf_counter()
            qa_output = self.qa.generate_baseline(premises_nl, question)
            timing.qa_sec = time.perf_counter() - t0
            timing.total_sec = time.perf_counter() - t_start

            return PipelineResult(
                answer=qa_output["answer"],
                explanation=qa_output["explanation"],
                premises_fol=[],
                question_fol="",
                z3_result=Z3Result(
                    premises_parsed=[], premises_failed=[],
                    raw_status="skipped",
                ),
                options_fol={},
                timing=timing,
            )

        # Full pipeline: NL -> FOL -> Z3 -> QA
        # Stage 1a: premises NL -> FOL
        t0 = time.perf_counter()
        premises_fol = self.fol.generate(premises_nl)
        # Stage 1b: question NL -> FOL (dung chung model, reuse predicates)
        question_fol = self.fol.generate_question_fol(question, premises_fol)
        # Stage 1c: MCQ options -> FOL (neu la trac nghiem)
        mcq_options = parse_mcq_options(question)
        options_fol = {}
        if mcq_options:
            options_fol = self.fol.generate_options_fol(mcq_options, premises_fol)
        timing.fol_sec = time.perf_counter() - t0

        # Stage 2: FOL -> Z3 consistency + entailment
        t0 = time.perf_counter()
        z3_result = self.z3.solve_safe(premises_fol, question_fol)
        timing.z3_sec = time.perf_counter() - t0

        # Stage 3: FOL + Z3 + question -> answer + explanation
        t0 = time.perf_counter()
        qa_output = self.qa.generate(
            premises_nl=premises_nl,
            premises_fol=premises_fol,
            z3_result=z3_result,
            question=question,
        )
        timing.qa_sec = time.perf_counter() - t0

        timing.total_sec = time.perf_counter() - t_start

        return PipelineResult(
            answer=qa_output["answer"],
            explanation=qa_output["explanation"],
            premises_fol=premises_fol,
            question_fol=question_fol,
            z3_result=z3_result,
            options_fol=options_fol,
            timing=timing,
        )

    def run_with_gold_fol(
        self,
        premises_nl: list[str],
        premises_fol: list[str],
        question: str,
        question_fol: str = "",
        options_fol: dict[str, str] | None = None,
    ) -> PipelineResult:
        """Chay pipeline voi FOL da co san (skip Stage 1).

        Huu ich khi evaluate voi gold FOL tu dataset.
        question_fol: FOL cua question (neu co) de Z3 check entailment.
        options_fol: {"A":"FOL_A",...} cho MCQ (neu co).
        """
        t_start = time.perf_counter()
        timing = TimingLog()

        # Stage 2: FOL -> Z3 + entailment check
        t0 = time.perf_counter()
        z3_result = self.z3.solve_safe(premises_fol, question_fol)
        timing.z3_sec = time.perf_counter() - t0

        # Stage 3
        t0 = time.perf_counter()
        qa_output = self.qa.generate(
            premises_nl=premises_nl,
            premises_fol=premises_fol,
            z3_result=z3_result,
            question=question,
        )
        timing.qa_sec = time.perf_counter() - t0

        timing.total_sec = time.perf_counter() - t_start

        return PipelineResult(
            answer=qa_output["answer"],
            explanation=qa_output["explanation"],
            premises_fol=premises_fol,
            question_fol=question_fol,
            z3_result=z3_result,
            options_fol=options_fol or {},
            timing=timing,
        )

    @staticmethod
    def summarize_timing(results: list[PipelineResult]) -> dict:
        """Tinh thoi gian trung binh tung stage tren tap test.

        Returns dict voi avg + tung stage (giay).
        In ra bang tom tat.
        """
        n = len(results)
        if n == 0:
            return {}

        sum_fol = sum(r.timing.fol_sec for r in results)
        sum_z3 = sum(r.timing.z3_sec for r in results)
        sum_qa = sum(r.timing.qa_sec for r in results)
        sum_total = sum(r.timing.total_sec for r in results)

        stats = {
            "n_samples": n,
            "avg_fol_sec": sum_fol / n,
            "avg_z3_sec": sum_z3 / n,
            "avg_qa_sec": sum_qa / n,
            "avg_total_sec": sum_total / n,
            "total_all_sec": sum_total,
        }

        print(f"\n{'='*50}")
        print(f"  Timing Summary ({n} samples)")
        print(f"{'='*50}")
        print(f"  Stage 1 (FOL) : {stats['avg_fol_sec']:7.3f}s avg")
        print(f"  Stage 2 (Z3)  : {stats['avg_z3_sec']:7.3f}s avg")
        print(f"  Stage 3 (QA)  : {stats['avg_qa_sec']:7.3f}s avg")
        print(f"  {'─'*40}")
        print(f"  Total / sample: {stats['avg_total_sec']:7.3f}s avg")
        print(f"  Total all     : {stats['total_all_sec']:7.1f}s")
        print(f"{'='*50}\n")

        return stats
