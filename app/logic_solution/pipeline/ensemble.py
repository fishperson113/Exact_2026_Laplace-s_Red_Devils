"""
pipeline/ensemble.py
--------------------
EnsemblePipeline: gộp FOLModel + QAModel thành 1 pipeline hoàn chỉnh.

Flow:
  premises + options + query
        ↓  Stage 1 (FOLModel):  premises (NL) → fol_list
        ↓  Stage 2 (QAModel):   NL + FOL + options + query → steps + JSON
  Unified Output Schema (BTC §4.1):
  {"query_id", "answer", "unit", "explanation", "premises_used",
   "reasoning": {"type": "fol", "steps": [...]}}
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field

from parsing import neutralize_epistemic_fol
from pipeline.fol_model import FOLModel
from pipeline.qa_model  import QAModel


@dataclass
class PipelineOutput:
    """Kết quả 1 query — đủ nguyên liệu cho Unified Output Schema BTC."""
    answer:        str
    explanation:   str
    premises_used: list[int] = field(default_factory=list)
    reasoning:     dict = field(default_factory=lambda: {"type": "fol", "steps": []})
    unit:          str = ""    # trường của Type 2 (physics) — logic luôn để rỗng

    # Metadata (không nằm trong output BTC)
    fol_latency_sec:   float = 0.0
    qa_latency_sec:    float = 0.0
    total_latency_sec: float = 0.0
    fol_raw:           str   = ""
    fol_list:          list[str] = field(default_factory=list)


class EnsemblePipeline:
    """FOLModel + QAModel — nhận (premises_nl, question, options) → PipelineOutput."""

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
        self.fol_max_tokens  = fol_cfg.get("max_new_tokens", 768)
        # QA v3: answer ĐỨNG CUỐI sau reasoning steps → budget phải đủ rộng
        # (phân phối target: P95~480, P99~600, max~793) kẻo cắt mất answer.
        self.qa_max_tokens   = (
            qa_cfg.get("thinking_max_new_tokens", 1024) if qa_thinking
            else qa_cfg.get("max_new_tokens", 1000)
        )

    def run(
        self,
        premises_nl: list[str],
        question:    str,
        options:     list[str] | None = None,
    ) -> PipelineOutput:
        """
        Full 2-stage inference.

        Stage 1 — FOLModel:  premises_nl → fol_list
        Stage 2 — QAModel:   premises_nl + fol_list + options + question
                             → answer + explanation + premises_used + reasoning
        """
        t_start = time.perf_counter()

        # ── Stage 1: NL → FOL ─────────────────────────────────────────────────
        t0 = time.perf_counter()
        fol_list, fol_raw = self.fol_model.generate(premises_nl, self.fol_max_tokens)
        fol_latency = time.perf_counter() - t0

        # ── Gỡ phủ định-giả ở mệnh đề epistemic trước khi đưa vào QA ──────────
        # FOL model dịch "No premise states whether X" thành ¬X (fact giả). Quét
        # NL gốc, thay ô FOL đó bằng note trung lập (giữ index n-to-n). fol_raw
        # (debug) giữ nguyên; chỉ fol_list đưa vào QA là bản đã neutralize.
        fol_list = neutralize_epistemic_fol(premises_nl, fol_list)

        # ── Stage 2: NL + FOL + options + Q → steps + JSON ────────────────────
        t0 = time.perf_counter()
        qa_out = self.qa_model.generate(
            premises_nl, fol_list, question,
            options=options, max_new_tokens=self.qa_max_tokens,
        )
        qa_latency = time.perf_counter() - t0

        total = time.perf_counter() - t_start

        return PipelineOutput(
            answer        = qa_out["answer"],
            explanation   = qa_out["explanation"],
            premises_used = qa_out["premises_used"],
            reasoning     = qa_out["reasoning"],
            fol_latency_sec   = round(fol_latency, 3),
            qa_latency_sec    = round(qa_latency,  3),
            total_latency_sec = round(total,        3),
            fol_raw  = fol_raw,
            fol_list = fol_list,
        )
