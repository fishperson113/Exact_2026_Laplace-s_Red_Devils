"""QA Stage 2 Inference: Load trained model, generate answers from NL + FOL.

This is the production inference module. At competition time:
  1. Model 1 generates FOL from NL (existing FOLInference)
  2. This module takes NL + FOL → answer + explanation via COT reasoning

Usage:
    # As module
    from models.QA_model.inference import QACOTInference
    qa = QACOTInference.from_yaml("configs/qa_model.yaml")
    result = qa.predict(premises_nl, premises_fol, question)

    # CLI evaluation
    python -m models.QA_model.inference --config configs/qa_model.yaml --split test
"""
from __future__ import annotations

import argparse
import json
import re
import time
from dataclasses import dataclass
from pathlib import Path

import torch
import yaml
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

from .prepare_data import (
    SYSTEM_PROMPT_QA_COT,
    USER_TEMPLATE_QA_COT,
    build_qa_dataset_dict,
    format_premises_fol,
    format_premises_nl,
)


@dataclass
class QAResult:
    answer: str
    explanation: str
    raw_output: str
    latency_sec: float = 0.0


class QACOTInference:
    """Load trained QA COT model and generate answers."""

    def __init__(self, model_path: str, max_new_tokens: int = 512, load_in_8bit: bool = True):
        self.max_new_tokens = max_new_tokens
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        print(f"[QA-COT] Loading model: {model_path}")
        load_kwargs = {
            "trust_remote_code": True,
            "device_map": "auto" if self.device == "cuda" else "cpu",
        }
        if load_in_8bit and self.device == "cuda":
            load_kwargs["quantization_config"] = BitsAndBytesConfig(load_in_8bit=True)
        else:
            load_kwargs["torch_dtype"] = torch.bfloat16

        self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(model_path, **load_kwargs)
        self.model.eval()
        print(f"[QA-COT] Model loaded on {self.device}")

    @classmethod
    def from_yaml(cls, config_path: str) -> QACOTInference:
        with open(config_path, "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f)

        model_cfg = cfg["model"]
        inference_cfg = cfg.get("inference", {})

        model_path = inference_cfg.get("model_path", model_cfg.get("hub_repo_id", model_cfg["name"]))
        max_new_tokens = inference_cfg.get("max_new_tokens", 512)
        load_in_8bit = inference_cfg.get("load_in_8bit", True)

        return cls(model_path=model_path, max_new_tokens=max_new_tokens, load_in_8bit=load_in_8bit)

    def predict(self, premises_nl: list[str], premises_fol: list[str], question: str) -> QAResult:
        """Generate answer + explanation from NL + FOL + question."""
        user_content = USER_TEMPLATE_QA_COT.format(
            premises_nl_block=format_premises_nl(premises_nl),
            premises_fol_block=format_premises_fol(premises_fol),
            question=question,
        )
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT_QA_COT},
            {"role": "user", "content": user_content},
        ]

        # enable_thinking=False: đầu ra cuối phải là JSON thuần, không có <think>.
        try:
            text = self.tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True, enable_thinking=False
            )
        except TypeError:
            text = self.tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True
            )
        inputs = self.tokenizer(
            text, return_tensors="pt", truncation=True, max_length=4096
        ).to(self.model.device)

        gen_kwargs = dict(
            **inputs,
            max_new_tokens=self.max_new_tokens,
            do_sample=False,
            repetition_penalty=1.1,
        )
        t0 = time.perf_counter()
        with torch.no_grad():
            try:
                out = self.model.generate(**gen_kwargs, tokenizer=self.tokenizer, stop_strings=["}"])
            except TypeError:
                out = self.model.generate(**gen_kwargs)
        latency = time.perf_counter() - t0

        generated = self.tokenizer.decode(
            out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True
        ).strip()

        parsed = self._parse_output(generated)
        return QAResult(
            answer=parsed["answer"],
            explanation=parsed["explanation"],
            raw_output=generated,
            latency_sec=latency,
        )

    @staticmethod
    def _parse_output(text: str) -> dict[str, str]:
        """Parse JSON {"answer": "...", "explanation": "..."} from model output."""
        # 1. JSON object đầy đủ
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            try:
                parsed = json.loads(match.group())
                if "answer" in parsed:
                    return {
                        "answer": str(parsed["answer"]).strip(),
                        "explanation": str(parsed.get("explanation", "")).strip(),
                    }
            except json.JSONDecodeError:
                pass

        # 2. JSON cụt/lỗi: moi "answer": "..." (và explanation nếu có)
        m = re.search(r'"answer"\s*:\s*"([^"]+)"', text)
        if m:
            answer = m.group(1).strip()
            em = re.search(r'"explanation"\s*:\s*"(.*)', text, re.DOTALL)
            explanation = em.group(1).strip().rstrip('"}').strip() if em else ""
            return {"answer": answer, "explanation": explanation}

        # 3. Last-resort (KHÔNG dump text thô, KHÔNG đoán bừa chữ "A" trong văn xuôi):
        #    a) label đi kèm cue "answer/đáp án/conclusion"
        m2 = re.search(
            r"(?:answer|final answer|đáp án|conclusion)\D{0,15}\b(Yes|No|Unknown|[ABCD])\b",
            text, re.I,
        )
        if m2:
            return {"answer": m2.group(1), "explanation": ""}
        #    b) Yes/No/Unknown đứng độc lập
        for label in ("Unknown", "Yes", "No"):
            if re.search(rf"\b{label}\b", text):
                return {"answer": label, "explanation": ""}
        #    c) Không rõ → Unknown (không gán bừa A/B/C/D)
        return {"answer": "Unknown", "explanation": ""}


# ─── Evaluation ──────────────────────────────────────────────────────────────

def evaluate_split(qa: QACOTInference, data_dir: Path, split: str = "test", max_samples: int | None = None):
    """Evaluate model on a dataset split. Print accuracy + per-sample results."""
    ds_dict = build_qa_dataset_dict(data_dir)
    dataset = ds_dict[split]

    if max_samples:
        dataset = dataset.select(range(min(max_samples, len(dataset))))

    print(f"\n{'='*60}")
    print(f"  Evaluating on [{split}] — {len(dataset)} samples")
    print(f"{'='*60}\n")

    correct = 0
    total = 0
    results = []

    for i, sample in enumerate(dataset):
        messages = sample["messages"]
        user_msg = messages[1]["content"]
        gold_msg = messages[2]["content"]

        # Parse gold answer
        gold_parsed = qa._parse_output(gold_msg)
        gold_answer = gold_parsed["answer"]

        # Parse user content to extract NL, FOL, question
        nl_lines, fol_lines, question = _parse_user_content(user_msg)

        result = qa.predict(nl_lines, fol_lines, question)
        is_correct = result.answer.strip().upper() == gold_answer.strip().upper()
        correct += int(is_correct)
        total += 1

        status = "✓" if is_correct else "✗"
        print(f"  [{i+1:3d}] {status} pred={result.answer:8s} gold={gold_answer:8s} ({result.latency_sec:.2f}s)")

        results.append({
            "idx": i,
            "predicted": result.answer,
            "gold": gold_answer,
            "correct": is_correct,
            "explanation": result.explanation,
            "latency_sec": result.latency_sec,
        })

    accuracy = correct / total if total > 0 else 0
    avg_latency = sum(r["latency_sec"] for r in results) / total if total > 0 else 0

    print(f"\n{'─'*60}")
    print(f"  Accuracy: {correct}/{total} = {accuracy:.1%}")
    print(f"  Avg latency: {avg_latency:.2f}s / sample")
    print(f"{'─'*60}\n")

    return {"accuracy": accuracy, "correct": correct, "total": total, "results": results}


def _parse_user_content(user_content: str) -> tuple[list[str], list[str], str]:
    """Extract NL premises, FOL premises, question from user message."""
    sections = re.split(r"\n(?=Premises \((?:NL|FOL)\):|Question:)", user_content)

    nl_lines = []
    fol_lines = []
    question = ""

    for section in sections:
        section = section.strip()
        if section.startswith("Premises (NL):"):
            body = section[len("Premises (NL):"):].strip()
            for line in body.split("\n"):
                m = re.match(r"^\d+\.\s*(.+)$", line.strip())
                if m:
                    nl_lines.append(m.group(1))
        elif section.startswith("Premises (FOL):"):
            body = section[len("Premises (FOL):"):].strip()
            for line in body.split("\n"):
                m = re.match(r"^\d+\.\s*(.+)$", line.strip())
                if m:
                    fol_lines.append(m.group(1))
        elif section.startswith("Question:"):
            question = section[len("Question:"):].strip()

    return nl_lines, fol_lines, question


# ─── CLI ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="QA COT Inference / Evaluation")
    parser.add_argument("--config", type=str, default="configs/qa_model.yaml")
    parser.add_argument("--split", type=str, default="test", choices=["train", "dev", "test"])
    parser.add_argument("--max-samples", type=int, default=None)
    parser.add_argument("--output", type=str, default=None, help="Save results JSON to path")
    args = parser.parse_args()

    with open(args.config, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    project_root = Path(__file__).resolve().parents[3]
    data_dir = project_root / "data"

    qa = QACOTInference.from_yaml(args.config)
    eval_result = evaluate_split(qa, data_dir, split=args.split, max_samples=args.max_samples)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(eval_result, f, ensure_ascii=False, indent=2)
        print(f"Results saved to: {output_path}")


if __name__ == "__main__":
    main()
