"""FOL BLEU: n-gram overlap score giữa gold và predicted FOL strings.

Tokenize FOL thành word-level tokens rồi tính BLEU-4 (sentence-level).
"""
from __future__ import annotations

import re

_FOL_TOKEN_RE = re.compile(
    r"(∀|∃|→|↔|∧|∨|¬|[(),]|[A-Za-z_][A-Za-z0-9_]*)"
)


def tokenize_fol_for_bleu(fol_str: str) -> list[str]:
    """Tách FOL string thành tokens cho BLEU.

    >>> tokenize_fol_for_bleu('∀x (A(x) → B(x))')
    ['∀', 'x', '(', 'A', '(', 'x', ')', '→', 'B', '(', 'x', ')', ')']
    """
    return _FOL_TOKEN_RE.findall(fol_str)


def _ngram_precision(ref: list[str], hyp: list[str], n: int) -> float:
    """Tính modified n-gram precision (clipped)."""
    if len(hyp) < n or len(ref) < n:
        return 0.0
    from collections import Counter
    ref_ngrams = Counter(tuple(ref[i:i + n]) for i in range(len(ref) - n + 1))
    hyp_ngrams = Counter(tuple(hyp[i:i + n]) for i in range(len(hyp) - n + 1))
    clipped = sum(min(c, ref_ngrams.get(ng, 0)) for ng, c in hyp_ngrams.items())
    total = sum(hyp_ngrams.values())
    return clipped / total if total > 0 else 0.0


def _brevity_penalty(ref_len: int, hyp_len: int) -> float:
    """BLEU brevity penalty."""
    import math
    if hyp_len == 0:
        return 0.0
    if hyp_len >= ref_len:
        return 1.0
    return math.exp(1 - ref_len / hyp_len)


def _manual_bleu4(ref: list[str], hyp: list[str]) -> float:
    """BLEU-4 tính tay (không cần nltk), smoothing +1."""
    import math
    if not ref or not hyp:
        return 0.0
    weights = (0.25, 0.25, 0.25, 0.25)
    log_avg = 0.0
    for n, w in enumerate(weights, 1):
        p = _ngram_precision(ref, hyp, n)
        # Add-1 smoothing cho n > 1 khi precision = 0
        if p == 0 and n > 1:
            denom = max(len(hyp) - n + 2, 1)
            p = 1.0 / denom
        if p > 0:
            log_avg += w * math.log(p)
        else:
            return 0.0
    bp = _brevity_penalty(len(ref), len(hyp))
    return bp * math.exp(log_avg)


def _safe_sentence_bleu(reference_tokens: list[str], hypothesis_tokens: list[str]) -> float:
    """BLEU-4 sentence-level với smoothing, trả 0.0 nếu lỗi."""
    if not reference_tokens or not hypothesis_tokens:
        return 0.0
    try:
        from nltk.translate.bleu_score import SmoothingFunction, sentence_bleu
        smoothing = SmoothingFunction().method1
        return float(
            sentence_bleu(
                [reference_tokens],
                hypothesis_tokens,
                weights=(0.25, 0.25, 0.25, 0.25),
                smoothing_function=smoothing,
            )
        )
    except (ImportError, TypeError, Exception):
        # Fallback: tính BLEU-4 tay (nltk lỗi hoặc chưa cài)
        return _manual_bleu4(reference_tokens, hypothesis_tokens)


def fol_bleu_single(gold_fol: str, pred_fol: str) -> float:
    """BLEU-4 giữa 1 cặp FOL formula (gold vs predicted)."""
    ref = tokenize_fol_for_bleu(gold_fol)
    hyp = tokenize_fol_for_bleu(pred_fol)
    return _safe_sentence_bleu(ref, hyp)


def fol_bleu_record(gold_list: list[str], pred_list: list[str]) -> float:
    """Trung bình BLEU trên từng cặp premise.

    Nếu predicted thiếu premise → 0 cho dòng thiếu.
    Nếu predicted thừa → bỏ qua dòng thừa, chia cho len(gold).
    """
    n = len(gold_list)
    if n == 0:
        return 0.0
    scores = []
    for i in range(n):
        if i < len(pred_list):
            scores.append(fol_bleu_single(gold_list[i], pred_list[i]))
        else:
            scores.append(0.0)
    return sum(scores) / n
