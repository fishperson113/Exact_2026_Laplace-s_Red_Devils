"""
run.py — Entry point duy nhất của logic_solution
-------------------------------------------------
Usage:
    # Chạy trên file input JSON
    python run.py --input data/sample_input.json

    # Chỉ định file output
    python run.py --input data/sample_input.json --output outputs/results.json

    # Dùng config khác
    python run.py --input data/sample_input.json --config config.yaml

Input format (Type 1 — BTC):
    [{"premises-NL": ["...", "..."], "question": "..."}]

Output format (BTC):
    [{"answer": "A", "explanation": "...", "fol": "..."}]
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import yaml
from dotenv import load_dotenv

# ── Setup path ─────────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))   # để import pipeline/, prompts/, utils/

# ── Load .env (HF_TOKEN) ───────────────────────────────────────────────────────
load_dotenv(ROOT / ".env")
hf_token = os.getenv("HF_TOKEN", "")
if hf_token and hf_token != "hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx":
    os.environ["HUGGING_FACE_HUB_TOKEN"] = hf_token

# ── Local imports (sau khi set sys.path) ──────────────────────────────────────
from pipeline.ensemble  import EnsemblePipeline          # noqa: E402
from utils.io           import load_input, save_output   # noqa: E402
from utils.postprocess  import format_submission         # noqa: E402


# ══════════════════════════════════════════════════════════════════════════════
# Main
# ══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Logic Solution — Ensemble inference pipeline (Type 1)"
    )
    parser.add_argument(
        "--input",  type=str, required=True,
        help="Path to input JSON file (list of {premises-NL, question})"
    )
    parser.add_argument(
        "--output", type=str, default=None,
        help="Path to output JSON file (default: outputs/results.json)"
    )
    parser.add_argument(
        "--config", type=str, default=str(ROOT / "config.yaml"),
        help="Path to YAML config file"
    )
    args = parser.parse_args()

    # ── Load config ────────────────────────────────────────────────────────────
    with open(args.config, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    slow_threshold = cfg.get("inference", {}).get("slow_threshold_sec", 60)

    # ── Load input ─────────────────────────────────────────────────────────────
    samples = load_input(args.input)
    print(f"\n{'='*60}")
    print(f"  LOGIC SOLUTION — {len(samples)} samples")
    print(f"  Config : {args.config}")
    print(f"  Input  : {args.input}")
    print(f"{'='*60}\n")

    # ── Load pipeline (models) ─────────────────────────────────────────────────
    pipeline = EnsemblePipeline(cfg)

    # ── Inference ──────────────────────────────────────────────────────────────
    results = []

    for i, sample in enumerate(samples):
        premises_nl = sample["premises_nl"]
        question    = sample["question"]

        print(f"[{i+1:3d}/{len(samples)}] Running...", flush=True)

        out = pipeline.run(premises_nl, question)

        # Đảm bảo đúng format BTC: answer → explanation → fol
        submission = format_submission(
            answer      = out.answer,
            explanation = out.explanation,
            fol         = out.fol,
        )
        results.append(submission)

        # Log tiến độ
        warn = " !! SLOW" if out.total_latency_sec > slow_threshold else ""
        print(
            f"         answer={submission['answer']:8s} "
            f"| FOL:{out.fol_latency_sec:.1f}s  "
            f"QA:{out.qa_latency_sec:.1f}s  "
            f"Total:{out.total_latency_sec:.1f}s{warn}",
            flush=True,
        )
        # Observability: hiện CoT model vừa sinh (reasoning.steps + raw think nếu có)
        steps = out.reasoning.get("steps", [])
        if steps:
            print(f"         reasoning[{out.reasoning.get('type')}] {len(steps)} steps:", flush=True)
            for j, step in enumerate(steps, 1):
                print(f"           {j}. {step}", flush=True)

    # ── Save output ────────────────────────────────────────────────────────────
    output_path = args.output or str(ROOT / "outputs" / "results.json")
    save_output(results, output_path)

    print(f"\n{'='*60}")
    print(f"  Done! {len(results)} samples processed.")
    print(f"  Output: {output_path}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
