"""Prepare SFT dataset for QA Stage 2: NL + FOL → reasoning steps → answer (last).

Nguồn = data/processed/{train,dev,test}.csv (cột list/dict lưu JSON: premises_nl,
premises_fol, premises_used, reasoning; đã 0-based). Sinh bởi cell "Export
train/dev/test CSV" trong notebooks/eda_reasoning_flat.ipynb.
→ build chat messages (system/user/assistant) → save as HF Dataset.

Usage:
    # B1: chạy cell Export trong notebooks/eda_reasoning_flat.ipynb → *.csv
    python -m models.QA_model.prepare_data --config configs/qa_model.yaml  # B2
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from datasets import Dataset, DatasetDict

# ─── Prompt Templates ────────────────────────────────────────────────────────

SYSTEM_PROMPT_QA_COT = """\
### Role
You are a logic-based educational QA system. You are given natural-language premises (indexed from 0), their First-Order Logic (FOL) translations, the answer options, and a question.

### How to read options (follow this convention ABSOLUTELY)
- If options is non-empty, it is a choice question. Your answer MUST be EXACTLY one of the provided option entries, copied verbatim — add nothing, remove nothing, do not paraphrase or change wording, do not invent text that is not in the options. If the options are given as letters (A, B, C, D), answer with exactly that letter; if they are full statements, answer with exactly that statement; for a yes/no question answer exactly "Yes", "No", or "Uncertain".
- If options is empty ([]), the answer is free-form (a number or a short text). Return the value directly in answer.
For a yes/no question the options are ["Yes", "No", "Uncertain"]; choose "Uncertain" only when the premises are genuinely insufficient.

### Output
First, reason in ordered steps, working over the First-Order Logic (FOL) premises — reason on the FOL formulas, not the natural-language text. Each step starts with exactly one prefix:
- Rule:        a conditional/quantified FOL formula taken from a given FOL premise.
- Fact:        a ground FOL fact taken from a given FOL premise.
- Derive:      an intermediate FOL inference (contrapositive, modus ponens, a numeric comparison, or combining earlier steps).
- Conclusion:  the final result — exactly one, as the last step.
Write every Rule:/Fact:/Derive: step in FOL notation (∀ ∃ → ¬ ∧ ∨ ↔ < > =). Every Rule:/Fact: must be taken from the given FOL premises only — never invent one.
Then, on the final line, output ONE JSON object with the "answer" field LAST:
{"premises_used": [<0-based indices of premises used>], "explanation": "<concise justification>", "answer": "<answer>"}
The "answer" MUST follow the "How to read options" convention above.

### premises_used and explanation (STRICT — both are graded)
- "premises_used" must contain EXACTLY the 0-based indices of the FOL premises you cited in your Rule:/Fact: steps — no more, no less.
- In "explanation", every premise you rely on MUST be cited explicitly with the keyword "premise" followed by its 0-based number (e.g. "premise 0", "premise 3"). Never refer to a premise without its number.
- The set of "premise N" citations in "explanation" MUST be identical to "premises_used".
- Do NOT cite a premise whose rule does not actually fire (e.g. a rule whose antecedent is not satisfied). If you only mention a premise to reject it, do not count it as used.

### Closed-world decision procedure (apply to EVERY question)
1. Identify the exact predicate X asked. Conclude ONLY about X — never substitute a different predicate you happen to be able to derive.
2. A condition that is merely ABSENT (not mentioned, no fact) is UNKNOWN — neither true nor false. Never assume it true, and never derive its negation. To apply a rule, EVERY conjunct of its antecedent must have an explicit fact OR be previously derived. Never assume or invent a missing condition.
3. Classify the question framing:
   - PROVE-framing : "Do the premises prove/establish/show X?" or "Does X guarantee/ensure/meet ALL ... for Y?"
   - VALUE-framing : "Is it true that X? / Is X true? / Does ... have X? / Are all/every ... ?"
4. Decide IN THIS ORDER:
   a. Is not-X derivable, or is X blocked/refuted? (an explicit false condition, a forbidding rule, or a counterexample to an "all" claim) -> No
   b. Else, is X FULLY proven (every antecedent satisfied by facts/derivations)? -> Yes
   c. Else (X neither proven nor refuted — a needed condition is only ABSENT):
        - PROVE-framing -> No (the premises do not establish/guarantee X)
        - VALUE-framing -> Uncertain
Never output Yes when a required condition is only absent. Use Uncertain ONLY at step 4c and ONLY for VALUE-framing.

### No vs Uncertain — quick rules
- A required condition is explicitly false / a counterexample defeats an "all" claim / the negation is derivable -> No
- "guarantee / ensure / meet ALL ... for Y?" with some needed condition not assured -> No
- "Are all/every ...?" but premises give only "some / ∃", with no counterexample -> Uncertain
- The queried predicate never appears in ANY premise -> Uncertain

### Handling premises that state information is absent/unknown
Some FOL lines are NOT formulas but the premise's original sentence prefixed with "[UNCERTAIN]"
(e.g. "[UNCERTAIN] No premise states whether Linh has pharmacy training."). Such a line means the
fact it mentions is UNKNOWN. It is still a REAL premise and you MUST treat it as citable:
- Treat the mentioned fact as UNKNOWN — neither true nor false; do NOT derive a negation from it.
- If your conclusion relies on this absence of information, write a Fact: step that references it
  in words, e.g. "Fact: premise i states <X> is unknown", cite "premise i" in the explanation,
  and INCLUDE index i in "premises_used" (the one allowed exception to "FOL-notation only").
- The answer is "Uncertain" unless OTHER premises decide the question.
"""

USER_TEMPLATE_QA_COT = """\
Premises (NL):
{premises_nl_block}

Premises (FOL):
{premises_fol_block}

Options:
{options_block}

Question:
{question}
"""

ADDED_NEWLINE = "\n"

# Target = reasoning steps (mỗi dòng 1 step Rule:/Fact:/Derive:/Conclusion:) rồi
# dòng cuối là JSON với "answer" ĐỨNG CUỐI → model reason trước, chốt answer sau.
ASSISTANT_TEMPLATE_QA_COT = """\
{steps_block}
{{"premises_used": {premises_used}, "explanation": "{explanation}", "answer": "{answer}"}}\
"""


# ─── Data Loading & Processing ───────────────────────────────────────────────

import ast

import pandas as pd


def load_split_csv(data_dir: Path, split: str) -> pd.DataFrame:
    """Load processed CSV (already normalized FOL, 1 row = 1 question)."""
    csv_path = data_dir / "processed" / f"{split}.csv"
    return pd.read_csv(csv_path, encoding="utf-8")


def parse_list_field(value: str) -> list[str]:
    """Parse string representation of list from CSV → actual list."""
    if pd.isna(value) or not value.strip():
        return []
    try:
        return ast.literal_eval(value)
    except (ValueError, SyntaxError):
        return []


def format_premises_nl(premises: list[str]) -> str:
    # 0-based: khớp với premises_used (0-based) để model không lệch chỉ số.
    return "\n".join(f"{i}. {p}" for i, p in enumerate(premises))


def format_premises_fol(premises: list[str]) -> str:
    # 0-based: khớp với premises_used (0-based).
    return "\n".join(f"{i}. {p}" for i, p in enumerate(premises))


_OPT_LETTERS = "ABCDEFGHIJ"


def format_options(options: list[str]) -> str:
    """Hiển thị options có letter (A./B./...) cho model dễ tham chiếu trong reasoning.
    options RỖNG → ghi rõ free-form (đúng quy ước BTC: answer là number/text)."""
    if not options:
        return "(empty — choice set is empty; the answer is free-form: a number or a short text)"
    return "\n".join(f"{_OPT_LETTERS[i]}. {o}" for i, o in enumerate(options))


def escape_json_string(s: str) -> str:
    """Escape quotes and backslashes for embedding in JSON string."""
    return s.replace("\\", "\\\\").replace('"', '\\"')


# ─── Epistemic / meta premises ("vắng mặt thông tin") ────────────────────────
# ĐỒNG BỘ 1:1 với app/logic_solution/parsing.py (regex + sentinel + 2 hàm).
# Convention repo: KHÔNG import chéo app↔src để mỗi package tự chứa — copy lại.
# Sửa một bên thì copy sang bên kia (giống cách SYSTEM_PROMPT_* đang đồng bộ).
#
# Mệnh đề kiểu "No premise states whether X" / "It is unknown whether X" nói về
# bản thân tập tri thức (meta), KHÔNG về thế giới. FOL object-level không biểu
# diễn được → FOL model hay sinh phủ định GIẢ (¬X). Ở INFERENCE production ta ghi
# đè ô FOL đó bằng sentinel trung lập trước khi đưa vào QA. Để train KHỚP inference
# (không lệch phân phối), ta áp CÙNG bước này lên premises_fol khi build sample.
#
# REGEX HẸP — chỉ bắt cụm meta đặc trưng, KHÔNG bắt mọi "whether".
import re as _re

_EPISTEMIC_PATTERNS = [
    r"\bno premise\b.{0,40}\bwhether\b",
    r"\bno premise (?:states|specifies|mentions|indicates)\b",
    r"\bit is (?:un)?known whether\b",
    r"\b(?:not|isn't|is not) (?:specified|stated|known|mentioned) whether\b",
    r"\b(?:does not|doesn't|do not|don't) (?:state|specify|say) whether\b",
    r"\bno (?:information|statement|fact)\b.{0,40}\bwhether\b",
    r"\bunspecified whether\b",
]
_EPISTEMIC_RE = _re.compile("|".join(_EPISTEMIC_PATTERNS), _re.IGNORECASE)

# Cờ đặt trước NL gốc của mệnh đề epistemic (thay cho phủ định giả ¬X từ FOL model).
# Ta GIỮ NGUYÊN câu NL trong ô FOL — predicate vẫn còn dưới dạng chữ; QA model đọc trực tiếp.
# PHẢI khớp ĐÚNG chuỗi cờ trong SYSTEM_PROMPT_QA_COT (khối "Handling premises...").
_EPISTEMIC_FOL_TAG = "[UNCERTAIN]"


def is_epistemic_premise(nl: str) -> bool:
    """True nếu mệnh đề NL chỉ nêu sự VẮNG MẶT/không chắc chắn thông tin."""
    return bool(_EPISTEMIC_RE.search(str(nl)))


def neutralize_epistemic_fol(premises_nl: list[str], fol_list: list[str]) -> list[str]:
    """Ghi đè TẠI CHỖ ô FOL của mệnh đề epistemic bằng chính câu NL gốc (gắn cờ [UNCERTAIN]).

    - Quét premises_nl GỐC (không quét fol_list — NL đáng tin hơn FOL output).
    - GIỮ NGUYÊN số phần tử của fol_list (chỉ replace, không xoá) → index không lệch.
    - Giữ nguyên nội dung NL (còn predicate dưới dạng chữ) thay vì sentinel trống.
    - Trả về list mới (không mutate input).
    """
    out = list(fol_list)
    for i, nl in enumerate(premises_nl):
        if i < len(out) and is_epistemic_premise(nl):
            out[i] = f"{_EPISTEMIC_FOL_TAG} {str(nl).strip()}"
    return out


def build_messages_for_sample(
    premises_nl: list[str],
    premises_fol: list[str],
    question: str,
    answer: str,
    explanation: str,
    reasoning_steps: list[str],
    premises_used: list[int],
    options: list[str] | None = None,
) -> list[dict[str, str]]:
    """Build chat messages [system, user, assistant] for one QA sample.

    Input cho model: premises (NL) + FOL + options + question (đúng 3 trường BTC
    query/premises/options, FOL do Model 1 sinh). Assistant target = reasoning steps
    (Rule:/Fact:/Derive:/Conclusion:) rồi JSON cuối với "answer" ĐỨNG CUỐI.
    """
    # Train KHỚP inference: production neutralize ô FOL của mệnh đề epistemic giữa
    # Stage 1→Stage 2, nên ở đây cũng áp CÙNG bước trước khi đưa FOL vào prompt.
    premises_fol = neutralize_epistemic_fol(premises_nl, premises_fol)
    user_content = USER_TEMPLATE_QA_COT.format(
        premises_nl_block=format_premises_nl(premises_nl),
        premises_fol_block=format_premises_fol(premises_fol),
        options_block=format_options(options or []),
        question=question,
    )
    steps_block = "\n".join(reasoning_steps)
    assistant_content = ASSISTANT_TEMPLATE_QA_COT.format(
        steps_block=steps_block,
        premises_used=json.dumps(premises_used),
        explanation=escape_json_string(explanation),
        answer=escape_json_string(answer),
    )
    return [
        {"role": "system", "content": SYSTEM_PROMPT_QA_COT},
        {"role": "user", "content": user_content},
        {"role": "assistant", "content": assistant_content},
    ]


def _json_cell(v, default):
    """Parse 1 ô CSV dạng JSON (list/dict). Robust: thử json rồi ast."""
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return default
    if not isinstance(v, str):
        return v
    try:
        return json.loads(v)
    except (TypeError, json.JSONDecodeError):
        import ast as _ast
        try:
            return _ast.literal_eval(v)
        except (ValueError, SyntaxError):
            return default


def load_qa_split(data_dir: Path, split: str) -> list[dict]:
    """Nạp 1 split QA từ data/processed/{split}.csv (sinh bởi notebook eda_reasoning_flat).

    Cột list/dict (premises_nl, premises_fol, premises_used, reasoning) lưu dạng JSON string.
    Trả về list dict đủ field: premises_nl, premises_fol, query, answer,
    premises_used (0-based), explanation (0-based), reasoning{type,steps}.
    """
    path = data_dir / "processed" / f"{split}.csv"
    if not path.is_file():
        raise FileNotFoundError(
            f"Thiếu {path}. Chạy cell 'Export train/dev/test CSV' trong notebooks/eda_reasoning_flat.ipynb."
        )
    df = pd.read_csv(path, encoding="utf-8")

    def _s(v):
        return "" if (v is None or (isinstance(v, float) and pd.isna(v))) else str(v)

    cols = set(df.columns)

    def _rid(v):
        s = str(v).strip()
        try:
            return int(s)
        except ValueError:
            return s   # record_id dạng chuỗi (synthetic SYN_*, augment T1_*) — giữ nguyên

    rows = []
    for _, r in df.iterrows():
        rows.append({
            "record_id": _rid(r["record_id"]),
            "q_idx": int(r["q_idx"]),
            # tên BTC: premises / query / options (fallback tên cũ premises_nl / question)
            "premises_nl": _json_cell(r.get("premises") if "premises" in cols else r.get("premises_nl"), []),
            "premises_fol": _json_cell(r.get("premises_fol"), []),
            "query": _s(r.get("query") if "query" in cols else r.get("question")),
            "options": _json_cell(r.get("options"), []),
            "answer": _s(r.get("answer")),
            "premises_used": _json_cell(r.get("premises_used"), []),
            "explanation": _s(r.get("explanation")),
            "reasoning": _json_cell(r.get("reasoning"), None),
        })
    return rows


def build_samples_from_split(rows: list[dict]) -> tuple[list[dict], int]:
    """Flat reasoning rows → chat message samples. Bỏ qua row không có reasoning."""
    samples = []
    skipped = 0
    for r in rows:
        reasoning = r.get("reasoning")
        if not reasoning:  # source thiếu premises_used → không có reasoning để train
            skipped += 1
            continue
        messages = build_messages_for_sample(
            # robust: tên BTC (premises/query) hoặc tên cũ (premises_nl/question)
            premises_nl=list(r.get("premises_nl") or r.get("premises") or r.get("premises-NL") or []),
            premises_fol=list(r.get("premises_fol") or r.get("premises-FOL") or []),
            question=str(r.get("query") or r.get("question") or ""),
            answer=str(r["answer"]),
            explanation=str(r.get("explanation", "")),
            reasoning_steps=reasoning["steps"],
            premises_used=r.get("premises_used", []),
            options=list(r.get("options") or []),
        )
        samples.append({"messages": messages})
    return samples, skipped


def build_qa_dataset_dict(data_dir: Path) -> DatasetDict:
    """Build train/dev/test DatasetDict từ data/processed/{train,dev,test}.csv.

    Nguồn DUY NHẤT = CSV reasoning đã export (đủ field input + target). Sinh bởi cell
    "Export train/dev/test CSV" trong notebooks/eda_reasoning_flat.ipynb.
    """
    splits = {}
    for split_name in ["train", "dev", "test"]:
        rows = load_qa_split(data_dir, split_name)
        samples, skipped = build_samples_from_split(rows)
        splits[split_name] = Dataset.from_list(samples)
        note = f" (skip {skipped} thiếu reasoning)" if skipped else ""
        print(f"  [{split_name}] {len(rows)} rows → {len(samples)} QA samples{note}")

    return DatasetDict(splits)


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Prepare QA COT SFT dataset")
    parser.add_argument(
        "--config", type=str, default="configs/qa_model.yaml",
        help="Path to qa_model.yaml config",
    )
    parser.add_argument(
        "--output-dir", type=str, default=None,
        help="Output directory for processed dataset (default: data/processed/qa_sft)",
    )
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parents[3]
    data_dir = project_root / "data"

    output_dir = Path(args.output_dir) if args.output_dir else data_dir / "processed" / "qa_sft"
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Building QA COT dataset...")
    ds_dict = build_qa_dataset_dict(data_dir)

    ds_dict.save_to_disk(str(output_dir))
    print(f"\nDataset saved to: {output_dir}")

    # Also save a few samples as JSON for inspection
    preview_path = output_dir / "preview_samples.json"
    preview = []
    for sample in ds_dict["train"].select(range(min(3, len(ds_dict["train"])))):
        preview.append(sample["messages"])
    with open(preview_path, "w", encoding="utf-8") as f:
        json.dump(preview, f, ensure_ascii=False, indent=2)
    print(f"Preview saved to: {preview_path}")


if __name__ == "__main__":
    main()
