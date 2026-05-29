"""Chay FOL_Z3 pipeline tren test set, xuat ket qua, upload len HF Hub.

Input:  data/processed/test.csv (premises_nl, question, answer)
Output:
  results/{suffix}_predictions.json       — per-sample predictions (metrics)
  results/{suffix}_inference_output.json  — chi tiet NL+FOL paired, FOL_Ques, ans_gt/pred (error analysis)
  results/{suffix}_report.json            — accuracy + timing summary
  + upload HF Hub

Cach chay:
  cd src && PYTHONPATH=. python -m models.FOL_Z3.run_inference --config configs/fol_z3.yaml

Duoc goi boi: scripts/run_fol_z3_inference.sh
Import tu:     .pipeline, data.dataset
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
from datetime import datetime, timezone
from pathlib import Path

import yaml

from data.dataset import read_split_csv
from data.ingestion import project_root

from .pipeline import FOLz3Pipeline


def load_test_data(processed_dir: Path) -> list[dict]:
    """Doc test.csv thanh list[dict] voi premises_nl, premises_fol, question, answer."""
    df = read_split_csv(processed_dir, "test")
    samples = []
    for _, row in df.iterrows():
        # premises_fol ground truth (tu dataset goc)
        fol_gt = list(row["premises_fol"]) if "premises_fol" in row.index else []

        samples.append({
            "record_id": int(row.get("record_id", -1)),
            "q_idx": int(row.get("q_idx", -1)),
            "premises_nl": list(row["premises_nl"]),
            "premises_fol_gt": fol_gt,
            "question": str(row["question"]),
            "gold_answer": str(row.get("answer", "")),
            "gold_explanation": str(row.get("explanation", "")),
        })
    return samples


def _build_hub_report(
    cfg,
    accuracy: float,
    n_samples: int,
    n_correct: int,
    timing_stats: dict,
    config_path: str,
) -> dict:
    """Tao report dict de luu JSON + upload Hub."""
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "mode": "fol_z3" if cfg.use_fol else "baseline",
        "accuracy": accuracy,
        "n_correct": n_correct,
        "n_samples": n_samples,
        "avg_inference_sec_per_sample": timing_stats.get("avg_total_sec", 0),
        "avg_fol_sec": timing_stats.get("avg_fol_sec", 0),
        "avg_z3_sec": timing_stats.get("avg_z3_sec", 0),
        "avg_qa_sec": timing_stats.get("avg_qa_sec", 0),
        "total_inference_sec": timing_stats.get("total_all_sec", 0),
        "config": {
            "fol_model": cfg.fol_hub_repo_id,
            "qa_model": cfg.qa_model_name,
            "use_fol": cfg.use_fol,
            "z3_timeout_ms": cfg.z3_timeout_ms,
            "load_in_8bit": cfg.load_in_8bit,
            "device": cfg.device,
        },
        "config_file": config_path,
    }


def _build_inference_output(
    samples: list[dict], results: list
) -> list[dict]:
    """Tao list chi tiet tung mau cho error analysis.

    Moi mau co:
    - premises: list[{nl, fol_gt, fol}] — NL + FOL ground truth + FOL predicted
    - question, FOL_Ques (string cho Yes/No, dict A/B/C/D cho MCQ)
    - ans_gt, explan_gt, ans_pred, explan_pred
    - fol_consistency, z3_entailment, z3_conclusions, timing
    """
    records = []
    for s, r in zip(samples, results):
        fol_gt_list = s.get("premises_fol_gt", [])

        # Ghep NL + FOL_GT + FOL_pred tung premise
        premises_paired = []
        for j, nl in enumerate(s["premises_nl"]):
            fol_gt = fol_gt_list[j] if j < len(fol_gt_list) else ""
            fol_pred = r.premises_fol[j] if j < len(r.premises_fol) else ""
            premises_paired.append({
                "nl": nl,
                "fol_gt": fol_gt,
                "fol": fol_pred,
            })

        # FOL_Ques: dict {"A":..,"B":..} cho MCQ, string cho Yes/No
        if r.options_fol:
            fol_ques = r.options_fol
        else:
            fol_ques = r.question_fol

        records.append({
            "record_id": s["record_id"],
            "q_idx": s["q_idx"],
            "premises": premises_paired,
            "question": s["question"],
            "FOL_Ques": fol_ques,
            "fol_consistency": r.z3_result.raw_status,
            "z3_entailment": r.z3_result.entailment,
            "z3_options_entailment": r.z3_result.options_entailment,
            "z3_conclusions": r.z3_result.conclusions,
            "ans_gt": s["gold_answer"],
            "explan_gt": s["gold_explanation"],
            "ans_pred": r.answer,
            "explan_pred": r.explanation,
            "timing_fol": r.timing.fol_sec,
            "timing_z3": r.timing.z3_sec,
            "timing_qa": r.timing.qa_sec,
            "timing_total": r.timing.total_sec,
        })
    return records


def _upload_to_hub(cfg, output_dir: Path, config_yaml_path: Path):
    """Upload results + config len HF Hub."""
    hf_token = (
        os.environ.get("HF_TOKEN")
        or os.environ.get("HUGGINGFACE_HUB_TOKEN")
        or ""
    ).strip()
    if not hf_token:
        print("[Hub] Khong tim thay HF_TOKEN — bo qua upload.")
        return

    from huggingface_hub import HfApi

    api = HfApi(token=hf_token)
    repo_id = cfg.hub_repo_id

    # Tao repo neu chua co
    api.create_repo(repo_id, repo_type="dataset", private=cfg.hub_private, exist_ok=True)

    suffix = "fol_z3" if cfg.use_fol else "baseline"

    # Upload files
    files_to_upload = [
        (output_dir / f"{suffix}_predictions.json", f"{suffix}_predictions.json"),
        (output_dir / f"{suffix}_inference_output.json", f"{suffix}_inference_output.json"),
        (output_dir / f"{suffix}_report.json", f"{suffix}_report.json"),
    ]

    # Upload config yaml
    if config_yaml_path.is_file():
        files_to_upload.append((config_yaml_path, f"configs/{config_yaml_path.name}"))

    uploaded = []
    for local_path, repo_path in files_to_upload:
        if not local_path.is_file():
            continue
        api.upload_file(
            path_or_fileobj=str(local_path),
            path_in_repo=repo_path,
            repo_id=repo_id,
            repo_type="dataset",
        )
        uploaded.append(repo_path)

    # Upload README
    readme_content = _build_readme(cfg, output_dir, suffix)
    readme_path = output_dir / "README.md"
    readme_path.write_text(readme_content, encoding="utf-8")
    api.upload_file(
        path_or_fileobj=str(readme_path),
        path_in_repo="README.md",
        repo_id=repo_id,
        repo_type="dataset",
    )
    uploaded.append("README.md")

    print(f"[Hub] Uploaded {len(uploaded)} files to {repo_id}")
    print(f"[Hub] https://huggingface.co/datasets/{repo_id}")


def _build_readme(cfg, output_dir: Path, suffix: str) -> str:
    """Tao README.md cho HF Hub dataset repo."""
    report_path = output_dir / f"{suffix}_report.json"
    report = {}
    if report_path.is_file():
        with open(report_path, "r", encoding="utf-8") as f:
            report = json.load(f)

    acc = report.get("accuracy", 0)
    n = report.get("n_samples", 0)
    n_correct = report.get("n_correct", 0)
    avg_time = report.get("avg_inference_sec_per_sample", 0)
    avg_fol = report.get("avg_fol_sec", 0)
    avg_z3 = report.get("avg_z3_sec", 0)
    avg_qa = report.get("avg_qa_sec", 0)
    mode = report.get("mode", suffix)

    return f"""---
tags:
  - exact-2026
  - fol-z3
  - logic-reasoning
---

# FOL_Z3 Pipeline Results

## Summary

| Metric | Value |
|--------|-------|
| **Mode** | {mode} |
| **Test Accuracy** | {acc:.4f} ({n_correct}/{n}) |
| **Avg Inference / sample** | {avg_time:.3f}s |
| **Avg FOL (Stage 1)** | {avg_fol:.3f}s |
| **Avg Z3 (Stage 2)** | {avg_z3:.3f}s |
| **Avg QA (Stage 3)** | {avg_qa:.3f}s |

## Config

| Param | Value |
|-------|-------|
| FOL Model | `{cfg.fol_hub_repo_id}` |
| QA Model | `{cfg.qa_model_name}` |
| use_fol | {cfg.use_fol} |
| Z3 timeout | {cfg.z3_timeout_ms}ms |
| load_in_8bit | {cfg.load_in_8bit} |

## Files

- `{suffix}_report.json` — accuracy + timing summary
- `{suffix}_predictions.json` — per-sample predictions
- `{suffix}_inference_output.json` — detailed output for error analysis (NL+FOL paired, FOL_Ques, ans_gt/pred)
- `configs/fol_z3.yaml` — pipeline config
"""


def run(config_path: str):
    """Chay pipeline tren test set."""
    root = project_root()
    config_abs = Path(config_path)
    if not config_abs.is_absolute():
        config_abs = root / config_path

    print(f"[Run] Config: {config_abs}")
    pipe = FOLz3Pipeline.from_yaml(config_abs)

    # Load test data
    processed_dir = root / "data" / "processed"
    samples = load_test_data(processed_dir)
    print(f"[Run] Test samples: {len(samples)}")
    print(f"[Run] Mode: {'FOL + Z3 + QA' if pipe.cfg.use_fol else 'Baseline (QA only)'}")
    print()

    # Run inference
    results = []
    correct = 0
    for i, s in enumerate(samples):
        result = pipe.run(
            premises_nl=s["premises_nl"],
            question=s["question"],
        )

        is_correct = result.answer.strip().upper() == s["gold_answer"].strip().upper()
        if is_correct:
            correct += 1

        results.append(result)

        status = "OK" if is_correct else "WRONG"
        ent_info = result.z3_result.entailment
        if result.z3_result.options_entailment:
            opts_str = " ".join(
                f"{k}:{v}" for k, v in sorted(result.z3_result.options_entailment.items())
            )
            ent_info = f"opts[{opts_str}]"
        print(
            f"[{i+1}/{len(samples)}] {status} "
            f"pred={result.answer} gold={s['gold_answer']} "
            f"ent={ent_info} "
            f"fol={result.timing.fol_sec:.1f}s z3={result.timing.z3_sec:.1f}s "
            f"qa={result.timing.qa_sec:.1f}s total={result.timing.total_sec:.1f}s"
        )

    # Summary
    acc = correct / len(samples) if samples else 0
    print(f"\n{'='*50}")
    print(f"  Accuracy: {correct}/{len(samples)} = {acc:.4f}")
    print(f"{'='*50}")

    timing_stats = FOLz3Pipeline.summarize_timing(results)

    # Export
    output_dir = root / "results"
    output_dir.mkdir(parents=True, exist_ok=True)
    suffix = "fol_z3" if pipe.cfg.use_fol else "baseline"

    # 1. Predictions (per-sample)
    predictions = []
    for s, r in zip(samples, results):
        predictions.append({
            "record_id": s["record_id"],
            "q_idx": s["q_idx"],
            "question": s["question"],
            "gold_answer": s["gold_answer"],
            "pred_answer": r.answer,
            "pred_explanation": r.explanation,
            "premises_fol": r.premises_fol,
            "question_fol": r.question_fol,
            "options_fol": r.options_fol,
            "fol_consistency": r.z3_result.raw_status,
            "z3_entailment": r.z3_result.entailment,
            "z3_options_entailment": r.z3_result.options_entailment,
            "z3_conclusions": r.z3_result.conclusions,
            "timing_fol": r.timing.fol_sec,
            "timing_z3": r.timing.z3_sec,
            "timing_qa": r.timing.qa_sec,
            "timing_total": r.timing.total_sec,
        })

    pred_path = output_dir / f"{suffix}_predictions.json"
    with open(pred_path, "w", encoding="utf-8") as f:
        json.dump(predictions, f, indent=2, ensure_ascii=False)
    print(f"[Run] Predictions: {pred_path}")

    # 2. Inference output (chi tiet, phuc vu phan tich loi)
    inference_output = _build_inference_output(samples, results)
    output_path = output_dir / f"{suffix}_inference_output.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(inference_output, f, indent=2, ensure_ascii=False)
    print(f"[Run] Inference output: {output_path}")

    # 3. Report (summary)
    report = _build_hub_report(
        pipe.cfg, acc, len(samples), correct, timing_stats, str(config_abs)
    )
    report_path = output_dir / f"{suffix}_report.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"[Run] Report: {report_path}")

    # 4. Upload to Hub
    if pipe.cfg.hub_push_results:
        print("\n[Hub] Uploading results...")
        _upload_to_hub(pipe.cfg, output_dir, config_abs)


def main():
    parser = argparse.ArgumentParser(description="FOL_Z3 Pipeline Inference")
    parser.add_argument(
        "--config",
        default="configs/fol_z3.yaml",
        help="Path to fol_z3.yaml config file",
    )
    args = parser.parse_args()
    run(args.config)


if __name__ == "__main__":
    main()
