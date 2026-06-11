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

Input format (BTC — đủ 5 trường):
    [{"query_id": "T1_0001", "type": "type1", "query": "...",
      "premises": ["...", "..."], "options": ["...", ...]}]

Output format (BTC Unified Output Schema §4.1 — LUÔN là JSON list, đủ 6 trường):
    [{"query_id": "T1_0001", "answer": "No", "unit": "",
      "explanation": "...", "premises_used": [0, 1],
      "reasoning": {"type": "fol", "steps": ["Rule: ...", "Fact: ...", "Conclusion: ..."]}}]
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
        help="Path to input JSON file (list of {query_id, type, query, premises, options})"
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

    # ── Load input (format BTC, 5 trường) ──────────────────────────────────────
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
        query_id = sample["query_id"]
        premises = sample["premises"]
        query    = sample["query"]
        options  = sample["options"]

        print(f"[{i+1:3d}/{len(samples)}] {query_id} Running...", flush=True)

        out = pipeline.run(premises, query, options=options)

        # Unified Output Schema BTC: query_id → answer → unit → explanation
        #                            → premises_used → reasoning{type, steps}
        submission = format_submission(
            query_id        = query_id,
            answer          = out.answer,
            explanation     = out.explanation,
            premises_used   = out.premises_used,
            reasoning_steps = out.reasoning.get("steps", []),
            options         = options,
            unit            = out.unit,
        )
        results.append(submission)

        # Log tiến độ
        warn = " !! SLOW" if out.total_latency_sec > slow_threshold else ""
        print(
            f"         answer={submission['answer'][:40]:40s} "
            f"| FOL:{out.fol_latency_sec:.1f}s  "
            f"QA:{out.qa_latency_sec:.1f}s  "
            f"Total:{out.total_latency_sec:.1f}s{warn}",
            flush=True,
        )
        # Observability: hiện reasoning steps model vừa sinh (nguyên văn)
        steps = submission["reasoning"]["steps"]
        if steps:
            print(f"         reasoning[fol] {len(steps)} steps:", flush=True)
            for j, step in enumerate(steps, 1):
                print(f"           {j}. {step}", flush=True)

    # ── Save output (LUÔN là JSON list — kể cả 1 query) ────────────────────────
    output_path = args.output or str(ROOT / "outputs" / "results.json")
    save_output(results, output_path)

    print(f"\n{'='*60}")
    print(f"  Done! {len(results)} samples processed.")
    print(f"  Output: {output_path}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
