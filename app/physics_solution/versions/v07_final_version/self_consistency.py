"""Self-consistency (majority voting) eval.

For each problem, sample K completions in ONE batched `generate` call (do_sample, temp>0),
execute each, then **majority-vote the answer using only the predictions (never the gold)** and
score the voted answer. Competition-legal: ONE model, ONE batched generate per request, <60 s
(K samples ride the batch dimension — not parallel models, not sequential temp passes).

    PYTHONPATH=. <venv>/bin/python -m \
      app.physics_solution.versions.v07_final_version.self_consistency \
      --model <merged|hub> [--sets both|val|golden] [--k 5] [--temperature 0.7] [--prob-batch 6]
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from app.physics_solution.shared.eval import scorer as evaluator
from app.physics_solution.versions.v05_best.code_executor import execute_code, extract_code
from app.physics_solution.versions.v07_final_version.eval import _load_val, _load_golden, _prompt

OUT_DIR = Path(__file__).resolve().parent / "train" / "runs"


@torch.no_grad()
def _sample_k(model, tok, prompts, k, max_new_tokens, temperature, top_p):
    """Return, per prompt, a list of K sampled completions (one batched generate)."""
    enc = tok(prompts, return_tensors="pt", padding=True, truncation=True,
              max_length=2048).to(model.device)
    out = model.generate(
        **enc, max_new_tokens=max_new_tokens, do_sample=True,
        temperature=temperature, top_p=top_p, num_return_sequences=k,
        pad_token_id=tok.pad_token_id or tok.eos_token_id, eos_token_id=tok.eos_token_id)
    gen = out[:, enc["input_ids"].shape[1]:]            # left-padded -> same input width
    texts = tok.batch_decode(gen, skip_special_tokens=True)
    # HF groups the K returns per input contiguously: [p0_s0..p0_s{k-1}, p1_s0, ...]
    return [texts[i * k:(i + 1) * k] for i in range(len(prompts))]


def _exec_answer(completion):
    code = extract_code(completion)
    stdout = execute_code(code).stdout or "" if code else ""
    ext = evaluator.extract(stdout)
    return stdout, ext.numeric, (ext.raw_answer or "").strip().lower()


def _vote(completions):
    """Majority vote over K predictions (NO gold). Returns (representative_stdout, votes, K).

    Numeric answers are clustered by the scorer's relative tolerance; the largest cluster wins.
    If text answers are the plurality, vote on the normalised FINAL ANSWER string."""
    rows = [dict(zip(("stdout", "num", "txt"), _exec_answer(c))) for c in completions]
    numeric = [r for r in rows if r["num"] is not None]
    text = [r for r in rows if r["num"] is None and r["txt"]]

    if numeric and len(numeric) >= len(text):
        clusters: list[tuple[float, list]] = []
        for r in numeric:
            for cl in clusters:
                if evaluator.numeric_close(r["num"], cl[0]):
                    cl[1].append(r)
                    break
            else:
                clusters.append((r["num"], [r]))
        clusters.sort(key=lambda cl: len(cl[1]), reverse=True)
        win = clusters[0][1]
        return win[0]["stdout"], len(win), len(completions)

    if text:
        keys = Counter(r["txt"] for r in text)
        best, votes = keys.most_common(1)[0]
        rep = next(r for r in text if r["txt"] == best)
        return rep["stdout"], votes, len(completions)

    return (rows[0]["stdout"] if rows else ""), 0, len(completions)


def run(model_path, sets="both", k=5, temperature=0.7, top_p=0.95,
        max_new_tokens=2048, prob_batch=6, limit=None, thinking=False):
    tok = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    tok.padding_side = "left"
    model = AutoModelForCausalLM.from_pretrained(
        model_path, torch_dtype="auto", device_map="auto", trust_remote_code=True)
    model.eval()
    print(f"[sc] model={model_path} K={k} temp={temperature} top_p={top_p} "
          f"thinking={thinking} prob_batch={prob_batch}", flush=True)

    datasets = {}
    if sets in ("both", "val"):
        datasets["val_56"] = _load_val()[: limit or None]
    if sets in ("both", "golden"):
        datasets["golden_60"] = _load_golden()[: limit or None]

    summary = {"model": model_path, "k": k, "temperature": temperature}
    for name, probs in datasets.items():
        n_ok = 0
        rows = []
        for s in range(0, len(probs), prob_batch):
            batch = probs[s:s + prob_batch]
            ksets = _sample_k(model, tok, [_prompt(tok, p, thinking) for p in batch],
                              k, max_new_tokens, temperature, top_p)
            for p, comps in zip(batch, ksets):
                rep_stdout, votes, total = _vote(comps)
                sc = evaluator.score(rep_stdout, p["gold_answer"], p["gold_unit"])
                n_ok += int(sc.is_correct)
                rows.append({"id": p["id"], "correct": sc.is_correct,
                             "votes": f"{votes}/{total}", "answer_type": p["answer_type"],
                             "domain": p["domain"], "gold": p["gold_answer"],
                             "gold_unit": p["gold_unit"], "pred": str(sc.pred_value)})
            done = s + len(batch)
            print(f"  [{name}] {done}/{len(probs)} acc={n_ok / done:.3f}", flush=True)
        acc = n_ok / len(probs) if probs else 0.0
        print(f"[sc] {name}: {n_ok}/{len(probs)} = {acc:.3f}")
        summary[name] = {"n": len(probs), "correct": n_ok, "accuracy": round(acc, 4), "rows": rows}
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        (OUT_DIR / f"sc_{name}.json").write_text(json.dumps(summary[name], indent=2, ensure_ascii=False))

    msg = " ".join(f"{n}={summary[n]['accuracy']}" for n in ("val_56", "golden_60") if n in summary)
    print(f"[sc] DONE {msg}")
    return summary


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--sets", choices=["both", "val", "golden"], default="both")
    ap.add_argument("--k", type=int, default=5)
    ap.add_argument("--temperature", type=float, default=0.7)
    ap.add_argument("--top-p", type=float, default=0.95)
    ap.add_argument("--max-new-tokens", type=int, default=2048)
    ap.add_argument("--prob-batch", type=int, default=6, help="problems per generate (×K seqs)")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--thinking", action="store_true")
    args = ap.parse_args()
    run(args.model, sets=args.sets, k=args.k, temperature=args.temperature, top_p=args.top_p,
        max_new_tokens=args.max_new_tokens, prob_batch=args.prob_batch, limit=args.limit,
        thinking=args.thinking)
