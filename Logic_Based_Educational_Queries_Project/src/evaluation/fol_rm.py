"""RM (Reasoning Match) = 0.7 × LE + 0.3 × FOL BLEU.

Theo LogicLLaMA (Doan et al.) — metric tổng hợp cho FOL model.
"""
from __future__ import annotations

import logging
from typing import Any

from .fol_bleu import fol_bleu_record
from .fol_le import _z3_available, le_record, le_record_no_z3

_LOG = logging.getLogger(__name__)

# Trọng số mặc định (LogicLLaMA paper)
DEFAULT_LE_WEIGHT = 0.7
DEFAULT_BLEU_WEIGHT = 0.3


def rm_record(
    gold_list: list[str],
    pred_list: list[str],
    *,
    le_weight: float = DEFAULT_LE_WEIGHT,
    bleu_weight: float = DEFAULT_BLEU_WEIGHT,
) -> dict[str, float]:
    """RM cho 1 record (1 danh sách premises).

    Returns dict với keys: rm_score, le_score, fol_bleu.
    """
    bleu = fol_bleu_record(gold_list, pred_list)
    if _z3_available():
        le = le_record(gold_list, pred_list)
    else:
        _LOG.warning(
            "z3-solver chưa cài — fallback LE = string match (kém chính xác). "
            "Cài: pip install z3-solver"
        )
        le = le_record_no_z3(gold_list, pred_list)
    rm = le_weight * le + bleu_weight * bleu
    return {"rm_score": rm, "le_score": le, "fol_bleu": bleu}


def rm_dataset(
    records: list[dict[str, Any]],
    *,
    gold_key: str = "gold_premises_fol",
    pred_key: str = "pred_premises_fol",
    le_weight: float = DEFAULT_LE_WEIGHT,
    bleu_weight: float = DEFAULT_BLEU_WEIGHT,
) -> dict[str, float]:
    """RM trung bình trên toàn dataset.

    Parameters
    ----------
    records : list[dict]
        Mỗi dict cần có ``gold_key`` và ``pred_key`` là list[str].

    Returns
    -------
    dict với keys: rm_score, le_score, fol_bleu, n_records.
    """
    if not records:
        return {"rm_score": 0.0, "le_score": 0.0, "fol_bleu": 0.0, "n_records": 0}
    rm_scores: list[float] = []
    le_scores: list[float] = []
    bleu_scores: list[float] = []
    for rec in records:
        gold = rec.get(gold_key, [])
        pred = rec.get(pred_key, [])
        if not isinstance(gold, list) or not isinstance(pred, list):
            rm_scores.append(0.0)
            le_scores.append(0.0)
            bleu_scores.append(0.0)
            continue
        r = rm_record(gold, pred, le_weight=le_weight, bleu_weight=bleu_weight)
        rm_scores.append(r["rm_score"])
        le_scores.append(r["le_score"])
        bleu_scores.append(r["fol_bleu"])
    n = len(records)
    return {
        "rm_score": sum(rm_scores) / n,
        "le_score": sum(le_scores) / n,
        "fol_bleu": sum(bleu_scores) / n,
        "n_records": n,
    }
