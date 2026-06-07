"""F-pre: accuracy eval of the fine-tuned model on BOTH val_56 and the 60 golden.

For each problem: build the SAME inference prompt used in SFT (GEN_SYSTEM + plain
problem block), greedy-generate reasoning+code, extract the code, execute it
sandboxed, and score the executed stdout (`FINAL ANSWER:` / `UNIT:`) with the
shared scorer. Reports accuracy for each set and writes a JSON.

    PYTHONPATH=. <venv>/bin/python -m \
      app.physics_solution.versions.v07_final_version.eval \
      --model <merged_dir|hub_repo> [--limit N]
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from app.physics_solution.shared.eval import scorer as evaluator
from app.physics_solution.versions.v05_best.code_executor import execute_code, extract_code
from app.physics_solution.versions.v06_finetune.data_pipeline.prompts import build_gen_messages

HERE = Path(__file__).resolve().parent
VAL = HERE / "val_56.jsonl"
GOLDEN = HERE.parent.parent / "data" / "golden" / "golden_60.csv"


def _load_val() -> list[dict]:
    rows = [json.loads(l) for l in open(VAL) if l.strip()]
    return [{"id": r["id"], "question": r["question"], "domain": r["domain"],
             "answer_type": r["answer_type"], "gold_answer": r["gold_answer"],
             "gold_unit": r.get("gold_unit", "")} for r in rows]


def _load_golden() -> list[dict]:
    out = []
    with open(GOLDEN, newline="") as fh:
        for r in csv.DictReader(fh):
            at = evaluator.detect_answer_type(r["answer"]).value
            out.append({"id": r["id"], "question": r["question"], "domain": r.get("domain", ""),
                        "answer_type": at, "gold_answer": r["answer"], "gold_unit": r.get("unit", "")})
    return out


def _generate(model, tokenizer, prob: dict, max_new_tokens: int) -> str:
    msgs = build_gen_messages(prob["question"], prob["domain"], prob["answer_type"])
    prompt = tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=False,
                             pad_token_id=tokenizer.pad_token_id or tokenizer.eos_token_id)
    return tokenizer.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)


def _eval_set(model, tokenizer, probs: list[dict], name: str, max_new_tokens: int) -> dict:
    n_ok = 0
    rows = []
    for i, p in enumerate(probs):
        completion = _generate(model, tokenizer, p, max_new_tokens)
        code = extract_code(completion)
        stdout = ""
        if code:
            res = execute_code(code)
            stdout = res.stdout or ""
        sc = evaluator.score(stdout, p["gold_answer"], p["gold_unit"])
        n_ok += int(sc.is_correct)
        rows.append({"id": p["id"], "correct": sc.is_correct, "gold": p["gold_answer"],
                     "pred": str(sc.pred_value), "had_code": bool(code)})
        if (i + 1) % 10 == 0:
            print(f"  [{name}] {i+1}/{len(probs)} acc={n_ok/(i+1):.3f}", flush=True)
    acc = n_ok / len(probs) if probs else 0.0
    print(f"[eval] {name}: {n_ok}/{len(probs)} = {acc:.3f}")
    return {"name": name, "n": len(probs), "correct": n_ok, "accuracy": round(acc, 4), "rows": rows}


def run_eval(model_path: str, limit: int | None = None, max_new_tokens: int = 1024) -> dict:
    tok = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    tok.padding_side = "left"
    model = AutoModelForCausalLM.from_pretrained(
        model_path, torch_dtype="auto", device_map="auto", trust_remote_code=True)
    model.eval()

    val, golden = _load_val(), _load_golden()
    if limit:
        val, golden = val[:limit], golden[:limit]
    summary = {
        "model": model_path,
        "val_56": _eval_set(model, tok, val, "val_56", max_new_tokens),
        "golden_60": _eval_set(model, tok, golden, "golden_60", max_new_tokens),
    }
    out = HERE / "train" / "runs" / "eval_results.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, indent=2))
    print(f"[eval] val_56={summary['val_56']['accuracy']} "
          f"golden_60={summary['golden_60']['accuracy']} -> {out}")
    return summary


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, help="merged dir or hub repo id")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--max-new-tokens", type=int, default=1024)
    args = ap.parse_args()
    run_eval(args.model, limit=args.limit, max_new_tokens=args.max_new_tokens)
