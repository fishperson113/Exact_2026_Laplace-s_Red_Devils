from __future__ import annotations

# --- SFT: trả lời trắc nghiệm / Yes-No + explanation ---
SYSTEM_PROMPT_SFT = """\
You are an expert in formal logic and educational reasoning. Given premises in natural language (and optionally first-order logic), answer the question with the correct label and a clear explanation that cites relevant premises when appropriate.
"""

USER_TEMPLATE_SFT = """\
{premises_block}

Question:
{question}
"""

ASSISTANT_TEMPLATE_SFT = """\
Answer: {answer}

Explanation: {explanation}
"""

PREMISES_FOL_HEADER = "Premises (FOL):"
PREMISES_NL_HEADER = "Premises (NL):"

# --- Bước pipeline: NL → FOL (LLM) — chỉnh prompt tại đây ---
SYSTEM_PROMPT_NL_TO_FOL = """\
You translate natural-language premises into first-order logic (FOL).
Output ONLY numbered FOL lines, one formula per line, no markdown fences.
Use the same alphabet of predicates as in similar logic benchmarks when possible.
"""

USER_TEMPLATE_NL_TO_FOL = """\
Natural language premises:
{nl_block}

Task: write the equivalent FOL premises (numbered list).
"""


# --- Solver → giải thích (gợi ý prompt khi có engine bên ngoài) ---
SYSTEM_PROMPT_EXPLAIN_FROM_SOLVER = """\
You explain a logic question for students. You are given solver metadata (status, model) and optional proof sketch.
Write a concise educational explanation; cite premises by number when relevant.
"""

USER_TEMPLATE_EXPLAIN_FROM_SOLVER = """\
Premises (NL):
{nl_block}

Question:
{question}

Solver output:
{solver_summary}

Gold answer (for teacher alignment, optional): {gold_answer}
"""


def format_nl_block_numbered(premises_nl: list[str]) -> str:
    if not premises_nl:
        return "(none)"
    return "\n".join(f"{i}. {p}" for i, p in enumerate(premises_nl, 1))


# --- SFT: NL premises → JSON premises_fol (cùng độ dài danh sách) ---
SYSTEM_PROMPT_FOL_SFT = """\
You translate numbered natural-language premises into first-order logic (FOL).
Output exactly one JSON object with key "premises_fol" whose value is a list of strings: one FOL formula per premise, in the same order and with the same length as the numbered NL premises. No markdown fences, no extra commentary.
"""
