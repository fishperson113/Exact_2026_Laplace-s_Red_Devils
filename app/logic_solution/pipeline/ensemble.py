"""
pipeline/ensemble.py
--------------------
EnsemblePipeline: gộp FOLModel + QAModel thành 1 pipeline hoàn chỉnh.

Flow:
  premises_nl + question
        ↓  Stage 1 (FOLModel)
    fol_list
        ↓  Stage 2 (QAModel)
  {"answer", "explanation", "fol"}   ← chuẩn output BTC
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field

from pipeline.fol_model import FOLModel
from pipeline.qa_model  import QAModel


@dataclass
class PipelineOutput:
    """Kết quả đầu ra theo đúng thứ tự field BTC yêu cầu."""
    answer:      str
    explanation: str
    fol:         str          # FOL premises join bằng "\n"

    # reasoning object (BTC §4.4): {"type": "cot"|"fol", "steps": [...]}
    reasoning:   dict = field(default_factory=lambda: {"type": "fol", "steps": []})

    # Metadata (không nằm trong output BTC)
    fol_latency_sec:   float = 0.0
    qa_latency_sec:    float = 0.0
    total_latency_sec: float = 0.0
    fol_raw:           str   = ""
    fol_list:          list[str] = field(default_factory=list)

    def to_submission(self) -> dict:
        """Trả về dict đúng format nộp BTC: answer → explanation → fol."""
        return {
            "answer":      self.answer,
            "explanation": self.explanation,
            "fol":         self.fol,
        }


class EnsemblePipeline:
    """FOLModel + QAModel — nhận (premises_nl, question) → PipelineOutput."""

    def __init__(self, cfg: dict):
        fol_cfg = cfg["fol_model"]
        qa_cfg  = cfg["qa_model"]
        inf_cfg = cfg.get("inference", {})
        load_8bit = inf_cfg.get("load_in_8bit", True)

        qa_thinking = qa_cfg.get("enable_thinking", False)

        self.fol_model       = FOLModel(fol_cfg["hub_repo_id"], load_in_8bit=load_8bit)
        self.qa_model        = QAModel(
            qa_cfg["hub_repo_id"],
            load_in_8bit    = load_8bit,
            enable_thinking = qa_thinking,
            temperature     = qa_cfg.get("temperature", 0.6),
            top_p           = qa_cfg.get("top_p", 0.95),
            top_k           = qa_cfg.get("top_k", 20),
        )
        self.fol_max_tokens  = fol_cfg.get("max_new_tokens", 400)
        # Think mode cần nhiều token hơn (think + JSON answer).
        self.qa_max_tokens   = (
            qa_cfg.get("thinking_max_new_tokens", 1024) if qa_thinking
            else qa_cfg.get("max_new_tokens", 200)
        )

    def run(self, premises_nl: list[str], question: str) -> PipelineOutput:
        """
        Full 2-stage inference.

        Stage 1 — FOLModel:  premises_nl → fol_list
        Stage 2 — QAModel:   premises_nl + fol_list + question → answer + explanation
        """
        t_start = time.perf_counter()

        # ── Stage 1: NL → FOL ─────────────────────────────────────────────────
        t0 = time.perf_counter()
        fol_list, fol_raw = self.fol_model.generate(premises_nl, self.fol_max_tokens)
        fol_latency = time.perf_counter() - t0

        # ── Stage 2: NL + FOL + Q → answer + explanation ──────────────────────
        t0 = time.perf_counter()
        qa_out = self.qa_model.generate(premises_nl, fol_list, question, self.qa_max_tokens)
        qa_latency = time.perf_counter() - t0

        total = time.perf_counter() - t_start

        # ── Assemble output (thứ tự: answer → explanation → fol) ──────────────
        fol_str = "\n".join(fol_list)   # list → string cho field "fol"

        return PipelineOutput(
            answer      = qa_out["answer"],
            explanation = qa_out["explanation"],
            fol         = fol_str,
            reasoning   = qa_out.get("reasoning", {"type": "fol", "steps": []}),
            fol_latency_sec   = round(fol_latency, 3),
            qa_latency_sec    = round(qa_latency,  3),
            total_latency_sec = round(total,        3),
            fol_raw  = fol_raw,
            fol_list = fol_list,
        )
