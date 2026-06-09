"""F-pre: accuracy eval of the fine-tuned model on val_56 and the 60 golden.

For each problem: build the SAME inference prompt used in SFT (GEN_SYSTEM + plain
problem block), generate reasoning+code (BATCHED), extract the code, execute it
sandboxed, and score the executed stdout (`FINAL ANSWER:`/`UNIT:`) with the
shared scorer. Saves each set's results immediately (partial-safe) and dumps the
full generations for debugging.

    PYTHONPATH=. <venv>/bin/python -m \
      app.physics_solution.versions.v07_final_version.eval \
      --model <merged_dir|hub_repo> [--sets both|val|golden] [--batch-size 16] [--limit N]
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
OUT_DIR = HERE / "train" / "runs"


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


def _prompt(tokenizer, p: dict, thinking: bool) -> str:
    msgs = build_gen_messages(p["question"], p["domain"], p["answer_type"])
    # Qwen3.5's template defaults thinking ON (suffix `<|im_start|>assistant\n<think>\n`).
    # think OFF matches the training distribution (we trained short-reasoning+code, no <think>)
    # and avoids no_code on easy problems; think ON helps hard reasoning but needs more budget.
    try:
        return tokenizer.apply_chat_template(
            msgs, tokenize=False, add_generation_prompt=True, enable_thinking=thinking)
    except TypeError:
        return tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)


@torch.no_grad()
def _generate_batch(model, tokenizer, prompts: list[str], max_new_tokens: int) -> list[str]:
    enc = tokenizer(prompts, return_tensors="pt", padding=True, truncation=True,
                    max_length=2048).to(model.device)
    out = model.generate(**enc, max_new_tokens=max_new_tokens, do_sample=False,
                         pad_token_id=tokenizer.pad_token_id or tokenizer.eos_token_id,
                         eos_token_id=tokenizer.eos_token_id)
    gen = out[:, enc["input_ids"].shape[1]:]  # left-padded -> same input width for all
    return tokenizer.batch_decode(gen, skip_special_tokens=True)


def _eval_set(model, tokenizer, probs: list[dict], name: str, max_new_tokens: int,
              batch_size: int, thinking: bool) -> dict:
    n_ok = 0
    rows = []
    for s in range(0, len(probs), batch_size):
        batch = probs[s:s + batch_size]
        completions = _generate_batch(model, tokenizer,
                                      [_prompt(tokenizer, p, thinking) for p in batch],
                                      max_new_tokens)
        for p, completion in zip(batch, completions):
            code = extract_code(completion)
            stdout, err = "", ""
            if code:
                res = execute_code(code)
                stdout = res.stdout or ""
                err = getattr(res, "stderr", "") or getattr(res, "error", "") or ""
            sc = evaluator.score(stdout, p["gold_answer"], p["gold_unit"])
            n_ok += int(sc.is_correct)
            # failure bucket for quick triage
            if sc.is_correct:
                bucket = "ok"
            elif not code:
                bucket = "no_code"
            elif not stdout.strip():
                bucket = "exec_failed"
            else:
                bucket = "wrong_answer"
            rows.append({"id": p["id"], "correct": sc.is_correct, "bucket": bucket,
                         "answer_type": p["answer_type"], "domain": p["domain"],
                         "gold": p["gold_answer"], "gold_unit": p["gold_unit"],
                         "pred": str(sc.pred_value), "pred_unit": sc.pred_unit,
                         "had_code": bool(code), "exec_stdout": stdout[:800],
                         "exec_err": err[:300], "completion": completion[:2000]})
        done = s + len(batch)
        print(f"  [{name}] {done}/{len(probs)} acc={n_ok/done:.3f}", flush=True)
    acc = n_ok / len(probs) if probs else 0.0
    from collections import Counter
    buckets = dict(Counter(r["bucket"] for r in rows))
    print(f"[eval] {name}: {n_ok}/{len(probs)} = {acc:.3f} | buckets={buckets}")
    res = {"name": name, "n": len(probs), "correct": n_ok, "accuracy": round(acc, 4),
           "buckets": buckets, "rows": rows}
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / f"eval_{name}.json").write_text(json.dumps(res, indent=2, ensure_ascii=False))
    print(f"[eval] saved {OUT_DIR / f'eval_{name}.json'}")
    return res


def run_eval(model_path: str, sets: str = "both", limit: int | None = None,
             max_new_tokens: int = 1024, batch_size: int = 16, thinking: bool = False) -> dict:
    tok = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    tok.padding_side = "left"
    model = AutoModelForCausalLM.from_pretrained(
        model_path, torch_dtype="auto", device_map="auto", trust_remote_code=True)
    model.eval()
    print(f"[eval] thinking={thinking} max_new_tokens={max_new_tokens} batch_size={batch_size}")

    summary = {"model": model_path}
    if sets in ("both", "val"):
        v = _load_val()[: limit or None]
        summary["val_56"] = _eval_set(model, tok, v, "val_56", max_new_tokens, batch_size, thinking)
    if sets in ("both", "golden"):
        g = _load_golden()[: limit or None]
        summary["golden_60"] = _eval_set(model, tok, g, "golden_60", max_new_tokens, batch_size, thinking)

    out = OUT_DIR / "eval_results.json"
    out.write_text(json.dumps({k: (v if k == "model" else {kk: vv for kk, vv in v.items() if kk != "rows"})
                               for k, v in summary.items()}, indent=2))
    msg = " ".join(f"{k}={summary[k]['accuracy']}" for k in ("val_56", "golden_60") if k in summary)
    print(f"[eval] DONE {msg} -> {out}")
    return summary


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, help="merged dir or hub repo id")
    ap.add_argument("--sets", choices=["both", "val", "golden"], default="both")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--max-new-tokens", type=int, default=1024)
    ap.add_argument("--batch-size", type=int, default=16)
    ap.add_argument("--thinking", action="store_true", help="enable Qwen <think> (default off)")
    args = ap.parse_args()
    run_eval(args.model, sets=args.sets, limit=args.limit, max_new_tokens=args.max_new_tokens,
             batch_size=args.batch_size, thinking=args.thinking)
