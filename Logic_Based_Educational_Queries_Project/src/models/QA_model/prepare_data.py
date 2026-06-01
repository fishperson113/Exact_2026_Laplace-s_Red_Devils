"""Prepare SFT dataset for QA Stage 2: NL + FOL → COT answer + explanation.

Load processed CSVs (normalized FOL) → build chat messages (system/user/assistant) → save as HF Dataset.

Usage:
    python -m models.QA_model.prepare_data --config configs/qa_model.yaml
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from datasets import Dataset, DatasetDict

# ─── Prompt Templates ────────────────────────────────────────────────────────

SYSTEM_PROMPT_QA_COT = """\
### Role
You are a logic-based educational QA system. You receive natural-language premises, \
their First-Order Logic (FOL) translations, and a question. Your job is to reason \
step-by-step through the logical structure and answer the question.

### Chain of Thought — Follow these steps

**Step 1: IDENTIFY LOGICAL CHAINS**
- Read the FOL premises to identify implication chains (A → B → C → ...).
- Group related premises into chains. Note which premises belong to which chain.

**Step 2: DETERMINE QUESTION TYPE**
- Multiple choice (A/B/C/D) → evaluate each option against the logical chains.
- Yes/No → determine if the statement follows from, is contradicted by, or cannot be determined from the premises.

**Step 3: EVALUATE & REASON**
- For MCQ: check each option — does it follow from a chain? Is it a valid contrapositive? Does it conflate separate chains?
- For Yes/No: trace whether the full chain connects the antecedent to the consequent without gaps.
- Cite specific premise numbers in your reasoning.

**Step 4: ANSWER**
- MCQ → exactly one of: A, B, C, D, or Unknown.
- Yes/No → exactly one of: Yes, No, or Unknown.
- Use "Unknown" ONLY when premises are genuinely insufficient.

### Output Format
Output ONLY a JSON object:
{"answer": "<label>", "explanation": "<your step-by-step reasoning citing premises>"}

No markdown fences, no text outside the JSON.
"""

USER_TEMPLATE_QA_COT = """\
Premises (NL):
{premises_nl_block}

Premises (FOL):
{premises_fol_block}

Question:
{question}
"""

ASSISTANT_TEMPLATE_QA_COT = """\
{{"answer": "{answer}", "explanation": "{explanation}"}}\
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
    return "\n".join(f"{i}. {p}" for i, p in enumerate(premises, 1))


def format_premises_fol(premises: list[str]) -> str:
    return "\n".join(f"{i}. {p}" for i, p in enumerate(premises, 1))


def escape_json_string(s: str) -> str:
    """Escape quotes and backslashes for embedding in JSON string."""
    return s.replace("\\", "\\\\").replace('"', '\\"')


def build_messages_for_sample(
    premises_nl: list[str],
    premises_fol: list[str],
    question: str,
    answer: str,
    explanation: str,
) -> list[dict[str, str]]:
    """Build chat messages [system, user, assistant] for one QA sample."""
    user_content = USER_TEMPLATE_QA_COT.format(
        premises_nl_block=format_premises_nl(premises_nl),
        premises_fol_block=format_premises_fol(premises_fol),
        question=question,
    )
    assistant_content = ASSISTANT_TEMPLATE_QA_COT.format(
        answer=escape_json_string(answer),
        explanation=escape_json_string(explanation),
    )
    return [
        {"role": "system", "content": SYSTEM_PROMPT_QA_COT},
        {"role": "user", "content": user_content},
        {"role": "assistant", "content": assistant_content},
    ]


def build_samples_from_csv(df: pd.DataFrame) -> list[dict]:
    """Convert CSV DataFrame → list of chat message samples."""
    samples = []
    for _, row in df.iterrows():
        premises_nl = parse_list_field(row["premises_nl"])
        premises_fol = parse_list_field(row["premises_fol"])
        question = str(row["question"])
        answer = str(row["answer"])
        explanation = str(row["explanation"])

        messages = build_messages_for_sample(
            premises_nl=premises_nl,
            premises_fol=premises_fol,
            question=question,
            answer=answer,
            explanation=explanation,
        )
        samples.append({"messages": messages})
    return samples


def build_qa_dataset_dict(data_dir: Path) -> DatasetDict:
    """Build train/dev/test DatasetDict from processed CSVs (normalized FOL)."""
    splits = {}
    for split_name in ["train", "dev", "test"]:
        df = load_split_csv(data_dir, split_name)
        samples = build_samples_from_csv(df)
        splits[split_name] = Dataset.from_list(samples)
        print(f"  [{split_name}] {len(df)} rows → {len(samples)} QA samples")

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
