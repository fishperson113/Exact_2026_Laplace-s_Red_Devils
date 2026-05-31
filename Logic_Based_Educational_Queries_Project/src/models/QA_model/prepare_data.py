"""Prepare SFT dataset for QA Stage 2: NL + FOL → COT answer + explanation.

Load raw dataset + split IDs → build chat messages (system/user/assistant) → save as HF Dataset.

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

def load_raw_data(data_dir: Path) -> list[dict]:
    raw_path = data_dir / "raw" / "Logic_Based_Educational_Queries.json"
    with open(raw_path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_split_ids(data_dir: Path) -> dict[str, list[int]]:
    split_path = data_dir / "processed" / "split_record_ids.json"
    with open(split_path, "r", encoding="utf-8") as f:
        return json.load(f)


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


def expand_records_to_samples(records: list[dict]) -> list[dict]:
    """Expand records (multi-question) into individual QA samples.

    Each record has N questions → N samples, each sharing the same premises.
    The `idx` field contains premise indices per question (1-indexed lists),
    but we use ALL premises for each question (model sees full context).
    """
    samples = []
    for record in records:
        premises_nl = record["premises-NL"]
        premises_fol = record["premises-FOL"]
        questions = record["questions"]
        answers = record["answers"]
        explanations = record["explanation"]

        for q_idx in range(len(questions)):
            messages = build_messages_for_sample(
                premises_nl=premises_nl,
                premises_fol=premises_fol,
                question=questions[q_idx],
                answer=answers[q_idx],
                explanation=explanations[q_idx],
            )
            samples.append({"messages": messages})
    return samples


def build_qa_dataset_dict(data_dir: Path) -> DatasetDict:
    """Build train/dev/test DatasetDict from raw data + split IDs."""
    raw_data = load_raw_data(data_dir)
    split_ids = load_split_ids(data_dir)

    splits = {}
    for split_name, record_indices in split_ids.items():
        records = [raw_data[i] for i in record_indices if i < len(raw_data)]
        samples = expand_records_to_samples(records)
        splits[split_name] = Dataset.from_list(samples)
        print(f"  [{split_name}] {len(records)} records → {len(samples)} QA samples")

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
