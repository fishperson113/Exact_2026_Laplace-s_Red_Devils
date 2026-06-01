"""Ensemble Pipeline: FOL Model → QA COT Model → answer + explanation.

Flow:
  1. FOL Model (HF Hub) sinh FOL từ NL premises
  2. QA Model (LoRA checkpoint) nhận NL + FOL + question → answer + explanation

Hỗ trợ 2 mode:
  - Evaluate: có gold answer → tính accuracy
  - Inference: không có gold → chỉ sinh answer

Usage:
    # Evaluate trên test set (có gold)
    python -m models.Ensemble_Model.inference --config configs/ensemble_model.yaml --mode evaluate

    # Inference (không có gold, chỉ sinh answer)
    python -m models.Ensemble_Model.inference --config configs/ensemble_model.yaml --mode inference --input data.json
"""
from __future__ import annotations

import argparse
import ast
import json
import re
import time
from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd
import torch
import yaml
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

from data.prompts import (
    SYSTEM_PROMPT_FOL_SFT,
    USER_TEMPLATE_FOL_SFT,
    format_nl_block_numbered,
)
from models.QA_model.prepare_data import (
    SYSTEM_PROMPT_QA_COT,
    USER_TEMPLATE_QA_COT,
    format_premises_fol,
    format_premises_nl,
)


# ─── Config ──────────────────────────────────────────────────────────────────

def load_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def resolve_project_root() -> Path:
    return Path(__file__).resolve().parents[3]


# ─── Result Dataclass ────────────────────────────────────────────────────────

@dataclass
class EnsembleResult:
    answer: str
    explanation: str
    premises_fol: list[str]
    fol_latency_sec: float = 0.0
    qa_latency_sec: float = 0.0
    total_latency_sec: float = 0.0
    fol_raw_output: str = ""


# ─── FOL Model ───────────────────────────────────────────────────────────────

class FOLModel:
    """Load FOL model từ HF Hub (merged) và sinh FOL từ NL."""

    def __init__(self, hub_repo_id: str, load_in_8bit: bool = True):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"[FOL] Loading: {hub_repo_id}")

        load_kwargs = {"trust_remote_code": True, "device_map": "auto"}
        if load_in_8bit and self.device == "cuda":
            load_kwargs["quantization_config"] = BitsAndBytesConfig(load_in_8bit=True)
        else:
            load_kwargs["torch_dtype"] = torch.bfloat16

        self.tokenizer = AutoTokenizer.from_pretrained(hub_repo_id, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(hub_repo_id, **load_kwargs)
        self.model.eval()
        print(f"[FOL] Loaded on {self.device}")

    def generate(self, premises_nl: list[str], max_new_tokens: int = 650) -> tuple[list[str], str]:
        """NL premises → FOL premises. Returns (fol_list, raw_output)."""
        nl_block = format_nl_block_numbered(premises_nl)
        user_msg = USER_TEMPLATE_FOL_SFT.format(premises_nl=nl_block)

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT_FOL_SFT},
            {"role": "user", "content": user_msg},
        ]
        text = self.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = self.tokenizer(
            text, return_tensors="pt", truncation=True, max_length=3500
        ).to(self.model.device)

        with torch.no_grad():
            out = self.model.generate(
                **inputs, max_new_tokens=max_new_tokens, do_sample=False, repetition_penalty=1.2,
            )
        raw = self.tokenizer.decode(
            out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True
        ).strip()

        return self._parse_fol(raw), raw

    @staticmethod
    def _parse_fol(text: str) -> list[str]:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            try:
                parsed = json.loads(match.group())
                if "premises_fol" in parsed and isinstance(parsed["premises_fol"], list):
                    return [str(f).strip() for f in parsed["premises_fol"]]
            except json.JSONDecodeError:
                pass
        lines = []
        for line in text.split("\n"):
            line = line.strip().lstrip("0123456789.)-  ")
            if any(c in line for c in "∀∃→∧∨¬↔") or re.match(r"\w+\(", line):
                lines.append(line)
        return lines


# ─── QA Model ────────────────────────────────────────────────────────────────

class QAModel:
    """Load QA model (base + LoRA adapter) và sinh answer + explanation."""

    def __init__(self, base_model_name: str, lora_path: str, load_in_8bit: bool = True):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"[QA] Loading base: {base_model_name}")
        print(f"[QA] Loading LoRA: {lora_path}")

        load_kwargs = {"trust_remote_code": True, "device_map": "auto"}
        if load_in_8bit and self.device == "cuda":
            load_kwargs["quantization_config"] = BitsAndBytesConfig(load_in_8bit=True)
        else:
            load_kwargs["torch_dtype"] = torch.bfloat16

        self.tokenizer = AutoTokenizer.from_pretrained(base_model_name, trust_remote_code=True)
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        base_model = AutoModelForCausalLM.from_pretrained(base_model_name, **load_kwargs)
        self.model = PeftModel.from_pretrained(base_model, lora_path)
        self.model.eval()
        print(f"[QA] Loaded on {self.device}")

    def generate(self, premises_nl: list[str], premises_fol: list[str], question: str,
                 max_new_tokens: int = 200) -> dict[str, str]:
        """NL + FOL + question → {"answer": "...", "explanation": "..."}."""
        user_content = USER_TEMPLATE_QA_COT.format(
            premises_nl_block=format_premises_nl(premises_nl),
            premises_fol_block=format_premises_fol(premises_fol),
            question=question,
        )
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT_QA_COT},
            {"role": "user", "content": user_content},
        ]
        text = self.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = self.tokenizer(
            text, return_tensors="pt", truncation=True, max_length=4096
        ).to(self.model.device)

        with torch.no_grad():
            out = self.model.generate(
                **inputs, max_new_tokens=max_new_tokens, do_sample=False,
            )
        raw = self.tokenizer.decode(
            out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True
        ).strip()

        return self._parse_output(raw)

    @staticmethod
    def _parse_output(text: str) -> dict[str, str]:
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
        for label in ("A", "B", "C", "D", "Yes", "No", "Unknown"):
            if label in text:
                return {"answer": label, "explanation": text}
        return {"answer": "Unknown", "explanation": text}


# ─── Ensemble Pipeline ────────────────────────────────────────────────────────

class EnsemblePipeline:
    """FOL Model + QA Model → answer + explanation."""

    def __init__(self, cfg: dict):
        fol_cfg = cfg["fol_model"]
        qa_cfg = cfg["qa_model"]
        inf_cfg = cfg.get("inference", {})

        load_8bit = inf_cfg.get("load_in_8bit", True)

        self.fol = FOLModel(
            hub_repo_id=fol_cfg["hub_repo_id"],
            load_in_8bit=load_8bit,
        )
        self.qa = QAModel(
            base_model_name=qa_cfg["base_model_name"],
            lora_path=qa_cfg["lora_path"],
            load_in_8bit=load_8bit,
        )
        self.fol_max_new_tokens = fol_cfg.get("max_new_tokens", 650)
        self.qa_max_new_tokens = qa_cfg.get("max_new_tokens", 200)

    def run(self, premises_nl: list[str], question: str) -> EnsembleResult:
        """Full pipeline: NL → FOL → answer + explanation."""
        t_start = time.perf_counter()

        # Stage 1: FOL
        t0 = time.perf_counter()
        premises_fol, fol_raw = self.fol.generate(premises_nl, self.fol_max_new_tokens)
        fol_latency = time.perf_counter() - t0

        # Stage 2: QA
        t0 = time.perf_counter()
        qa_output = self.qa.generate(premises_nl, premises_fol, question, self.qa_max_new_tokens)
        qa_latency = time.perf_counter() - t0

        total = time.perf_counter() - t_start

        return EnsembleResult(
            answer=qa_output["answer"],
            explanation=qa_output["explanation"],
            premises_fol=premises_fol,
            fol_latency_sec=fol_latency,
            qa_latency_sec=qa_latency,
            total_latency_sec=total,
            fol_raw_output=fol_raw,
        )


# ─── Data Loading ─────────────────────────────────────────────────────────────

def load_test_csv(data_dir: Path) -> pd.DataFrame:
    return pd.read_csv(data_dir / "processed" / "test.csv", encoding="utf-8")


def parse_list_field(value) -> list[str]:
    if pd.isna(value) or not str(value).strip():
        return []
    try:
        return ast.literal_eval(str(value))
    except (ValueError, SyntaxError):
        return []


def load_inference_json(path: str) -> list[dict]:
    """Load input JSON cho inference mode (không có gold).
    Format: [{"premises_nl": [...], "question": "..."}, ...]
    """
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# ─── Evaluate Mode ────────────────────────────────────────────────────────────

def evaluate(pipeline: EnsemblePipeline, cfg: dict):
    """Evaluate trên test.csv (có gold answer) → accuracy + latency."""
    project_root = resolve_project_root()
    data_dir = project_root / "data"
    output_dir = Path(cfg.get("output_dir", str(project_root / "outputs" / "ensemble")))
    output_dir.mkdir(parents=True, exist_ok=True)

    df = load_test_csv(data_dir)
    slow_threshold = cfg.get("inference", {}).get("slow_threshold_sec", 60)

    print(f"\n{'='*70}")
    print(f"  ENSEMBLE EVALUATE — {len(df)} samples")
    print(f"  Slow threshold: {slow_threshold}s")
    print(f"{'='*70}\n")

    correct = 0
    total = 0
    results = []
    slow_samples = []

    for i, row in df.iterrows():
        premises_nl = parse_list_field(row["premises_nl"])
        question = str(row["question"])
        gold_answer = str(row["answer"]).strip()

        result = pipeline.run(premises_nl, question)

        is_correct = result.answer.strip().upper() == gold_answer.upper()
        correct += int(is_correct)
        total += 1

        status = "✓" if is_correct else "✗"
        latency_warn = ""
        if result.total_latency_sec > slow_threshold:
            latency_warn = " ⚠️ SLOW"
            slow_samples.append(i)

        print(
            f"  [{i+1:3d}/{len(df)}] {status} pred={result.answer:8s} gold={gold_answer:8s} "
            f"| FOL:{result.fol_latency_sec:.1f}s QA:{result.qa_latency_sec:.1f}s "
            f"Total:{result.total_latency_sec:.1f}s{latency_warn}"
        )

        results.append({
            "idx": i,
            "question": question[:100],
            "gold_answer": gold_answer,
            "pred_answer": result.answer,
            "explanation": result.explanation,
            "correct": is_correct,
            "premises_fol_generated": result.premises_fol,
            "fol_latency_sec": round(result.fol_latency_sec, 3),
            "qa_latency_sec": round(result.qa_latency_sec, 3),
            "total_latency_sec": round(result.total_latency_sec, 3),
        })

    # Summary
    accuracy = correct / total if total > 0 else 0
    avg_total = sum(r["total_latency_sec"] for r in results) / total if total > 0 else 0
    avg_fol = sum(r["fol_latency_sec"] for r in results) / total if total > 0 else 0
    avg_qa = sum(r["qa_latency_sec"] for r in results) / total if total > 0 else 0

    summary = {
        "accuracy": accuracy,
        "correct": correct,
        "total": total,
        "avg_total_latency_sec": round(avg_total, 3),
        "avg_fol_latency_sec": round(avg_fol, 3),
        "avg_qa_latency_sec": round(avg_qa, 3),
        "slow_samples_count": len(slow_samples),
        "slow_sample_indices": slow_samples,
    }

    print(f"\n{'='*70}")
    print(f"  RESULTS")
    print(f"{'='*70}")
    print(f"  Accuracy     : {correct}/{total} = {accuracy:.1%}")
    print(f"  Avg latency  : {avg_total:.2f}s/sample (FOL:{avg_fol:.2f}s + QA:{avg_qa:.2f}s)")
    if slow_samples:
        print(f"  ⚠️  SLOW (>{slow_threshold}s): {len(slow_samples)} samples — indices: {slow_samples}")
    print(f"{'='*70}\n")

    # Save
    log = {"summary": summary, "results": results}
    log_path = output_dir / "ensemble_eval_results.json"
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(log, f, ensure_ascii=False, indent=2)
    print(f"[Log] Saved to: {log_path}")

    return log


# ─── Inference Mode ───────────────────────────────────────────────────────────

def inference(pipeline: EnsemblePipeline, input_path: str, cfg: dict):
    """Inference (không có gold) → sinh answer + explanation."""
    output_dir = Path(cfg.get("output_dir", str(resolve_project_root() / "outputs" / "ensemble")))
    output_dir.mkdir(parents=True, exist_ok=True)

    data = load_inference_json(input_path)
    slow_threshold = cfg.get("inference", {}).get("slow_threshold_sec", 60)

    print(f"\n{'='*70}")
    print(f"  ENSEMBLE INFERENCE — {len(data)} samples")
    print(f"{'='*70}\n")

    results = []
    slow_samples = []

    for i, item in enumerate(data):
        premises_nl = item["premises_nl"]
        question = item["question"]

        result = pipeline.run(premises_nl, question)

        latency_warn = ""
        if result.total_latency_sec > slow_threshold:
            latency_warn = " ⚠️ SLOW"
            slow_samples.append(i)

        print(
            f"  [{i+1:3d}/{len(data)}] answer={result.answer:8s} "
            f"| FOL:{result.fol_latency_sec:.1f}s QA:{result.qa_latency_sec:.1f}s "
            f"Total:{result.total_latency_sec:.1f}s{latency_warn}"
        )

        results.append({
            "idx": i,
            "premises_nl": premises_nl,
            "question": question,
            "answer": result.answer,
            "explanation": result.explanation,
            "premises_fol_generated": result.premises_fol,
            "fol_latency_sec": round(result.fol_latency_sec, 3),
            "qa_latency_sec": round(result.qa_latency_sec, 3),
            "total_latency_sec": round(result.total_latency_sec, 3),
        })

    avg_total = sum(r["total_latency_sec"] for r in results) / len(results) if results else 0

    print(f"\n{'='*70}")
    print(f"  Avg latency: {avg_total:.2f}s/sample")
    if slow_samples:
        print(f"  ⚠️  SLOW (>{slow_threshold}s): {len(slow_samples)} samples — indices: {slow_samples}")
    print(f"{'='*70}\n")

    out_path = output_dir / "ensemble_inference_results.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"[Log] Saved to: {out_path}")

    return results


# ─── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Ensemble: FOL + QA Pipeline")
    parser.add_argument("--config", type=str, default="configs/ensemble_model.yaml")
    parser.add_argument("--mode", type=str, default="evaluate", choices=["evaluate", "inference"])
    parser.add_argument("--input", type=str, default=None, help="Input JSON for inference mode")
    args = parser.parse_args()

    cfg = load_config(args.config)
    pipeline = EnsemblePipeline(cfg)

    if args.mode == "evaluate":
        evaluate(pipeline, cfg)
    elif args.mode == "inference":
        if not args.input:
            raise ValueError("--input required for inference mode")
        inference(pipeline, args.input, cfg)


if __name__ == "__main__":
    main()
