"""Ensemble ("vét") eval: base + v07 each self-consistency-vote, then agree-or-judge.

Per problem:
  1. base samples K -> internal majority vote -> (answer_b, solution_b)
  2. v07  samples K -> internal majority vote -> (answer_v, solution_v)
  3. if answer_b == answer_v (scorer agreement) -> chosen = that answer (no judge)
     else: Qwen(base) READS both solutions + their two final answers and PICKS one
           (text judgement only, **NEVER runs code**) -> chosen = A or B
  4. (--explain) Qwen(base) writes the final answer + explanation + CoT for the chosen
     answer (production P2/P3 output; does not change the scored P1 value).

P1 is scored on the chosen candidate's executed answer. Competition-legal: base(4B) +
v07(4B) = 8B active at once (served in parallel); the judge reuses the already-loaded
base model, so no extra parameters.

    PYTHONPATH=. <venv>/bin/python -m \
      app.physics_solution.versions.v07_final_version.ensemble \
      --base Qwen/Qwen3.5-4B --ft <merged|hub> \
      [--sets both|val|golden] [--k 5] [--prob-batch 8] [--explain] [--limit N]
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from app.physics_solution.shared.eval import scorer as evaluator
from app.physics_solution.versions.v05_best.code_executor import execute_code, extract_code
from app.physics_solution.versions.v07_final_version.eval import _load_val, _load_golden, _prompt
from app.physics_solution.versions.v07_final_version.self_consistency import _sample_k

OUT_DIR = Path(__file__).resolve().parent / "train" / "runs"


# ---------------------------------------------------------------------------- voting
def _exec_row(completion: str) -> dict:
    code = extract_code(completion)
    stdout = (execute_code(code).stdout or "") if code else ""
    ext = evaluator.extract(stdout)
    return {"comp": completion, "stdout": stdout, "num": ext.numeric,
            "txt": (ext.raw_answer or "").strip().lower()}


def _vote_full(completions: list[str]) -> tuple[dict, int, int]:
    """Majority vote (NO gold). Returns (representative_row, votes, K).

    Numeric answers cluster by the scorer's relative tolerance; the largest cluster wins.
    Representative row keeps the winning completion + its stdout so the judge can read it."""
    rows = [_exec_row(c) for c in completions]
    numeric = [r for r in rows if r["num"] is not None]
    text = [r for r in rows if r["num"] is None and r["txt"]]

    if numeric and len(numeric) >= len(text):
        clusters: list[dict] = []
        for r in numeric:
            for cl in clusters:
                if evaluator.numeric_close(r["num"], cl["key"]):
                    cl["rows"].append(r)
                    break
            else:
                clusters.append({"key": r["num"], "rows": [r]})
        clusters.sort(key=lambda cl: len(cl["rows"]), reverse=True)
        win = clusters[0]["rows"]
        return win[0], len(win), len(completions)

    if text:
        keys = Counter(r["txt"] for r in text)
        best, votes = keys.most_common(1)[0]
        rep = next(r for r in text if r["txt"] == best)
        return rep, votes, len(completions)

    return (rows[0] if rows else {"comp": "", "stdout": "", "num": None, "txt": ""}), 0, len(completions)


def _agree(a: dict, b: dict) -> bool:
    """Do the two models' voted answers match (scorer-equivalent)?"""
    if a["num"] is not None and b["num"] is not None:
        return evaluator.numeric_close(a["num"], b["num"])
    if a["num"] is None and b["num"] is None:
        return bool(a["txt"]) and a["txt"] == b["txt"]
    return False


# ---------------------------------------------------------------------------- judge
def _final_lines(stdout: str) -> str:
    keep = [ln.strip() for ln in stdout.splitlines()
            if "FINAL ANSWER" in ln.upper() or ln.upper().lstrip().startswith("UNIT")]
    return " | ".join(keep) if keep else (stdout.strip()[-160:] or "(no output)")


def _solution_block(rep: dict, max_chars: int = 1400) -> str:
    """Reasoning + code (trimmed) + the actually computed final answer line(s).

    NOTE: deliberately does NOT expose the self-consistency vote counts — vote
    confidence is an unreliable signal (a model can be 5/5 confident yet wrong),
    so the judge must decide purely from the physics, not from agreement counts."""
    body = (rep.get("comp") or "").strip()[:max_chars]
    return f"{body}\n>>> Computed final answer: {_final_lines(rep.get('stdout', ''))}"


def _judge_prompt(tok, question: str, rep_a: dict, rep_b: dict) -> str:
    user = (
        "You are grading two independent physics solutions that reached DIFFERENT final "
        "answers. Decide which FINAL ANSWER is physically correct. Reason briefly, but DO "
        "NOT run or simulate code — judge from the physics and the reported results.\n\n"
        f"PROBLEM:\n{question.strip()}\n\n"
        f"=== Solution A ===\n{_solution_block(rep_a)}\n\n"
        f"=== Solution B ===\n{_solution_block(rep_b)}\n\n"
        "Which final answer is correct? Respond with EXACTLY one letter on the last line: "
        "`A` or `B`."
    )
    msgs = [{"role": "user", "content": user}]
    try:
        return tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True,
                                       enable_thinking=False)
    except TypeError:
        return tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)


_AB = re.compile(r"\b([AB])\b")


def _parse_choice(text: str) -> str | None:
    # prefer the LAST standalone A/B (the prompt asks for it on the last line)
    hits = _AB.findall(text.upper())
    return hits[-1] if hits else None


@torch.no_grad()
def _generate_greedy(model, tok, prompts: list[str], max_new_tokens: int) -> list[str]:
    enc = tok(prompts, return_tensors="pt", padding=True, truncation=True,
              max_length=3072).to(model.device)
    out = model.generate(**enc, max_new_tokens=max_new_tokens, do_sample=False,
                         pad_token_id=tok.pad_token_id or tok.eos_token_id,
                         eos_token_id=tok.eos_token_id)
    gen = out[:, enc["input_ids"].shape[1]:]
    return tok.batch_decode(gen, skip_special_tokens=True)


def _explain_prompt(tok, question: str, rep: dict) -> str:
    user = (
        f"PROBLEM:\n{question.strip()}\n\n"
        f"A verified solution computed this result:\n{_solution_block(rep)}\n\n"
        "Write a clear physics EXPLANATION and a step-by-step chain of thought (CoT) that "
        "leads to this answer. End with two lines exactly:\nFINAL ANSWER: <value>\nUNIT: <unit>"
    )
    msgs = [{"role": "user", "content": user}]
    try:
        return tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True,
                                       enable_thinking=False)
    except TypeError:
        return tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)


# ---------------------------------------------------------------------------- loading
def _load(path: str):
    tok = AutoTokenizer.from_pretrained(path, trust_remote_code=True)
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    tok.padding_side = "left"
    model = AutoModelForCausalLM.from_pretrained(
        path, torch_dtype="auto", device_map="auto", trust_remote_code=True)
    model.eval()
    return tok, model


# ---------------------------------------------------------------------------- run
def run(base_path: str, ft_path: str, sets: str = "both", k: int = 5,
        temperature: float = 0.7, top_p: float = 0.95, max_new_tokens: int = 2048,
        prob_batch: int = 8, limit: int | None = None, explain: bool = False,
        judge_tokens: int = 256, default_pick: str = "B"):
    tok_b, model_b = _load(base_path)
    tok_v, model_v = _load(ft_path)
    print(f"[ens] base={base_path} ft={ft_path} K={k} temp={temperature} "
          f"prob_batch={prob_batch} explain={explain} default_pick={default_pick}", flush=True)

    datasets = {}
    if sets in ("both", "val"):
        datasets["val_56"] = _load_val()[: limit or None]
    if sets in ("both", "golden"):
        datasets["golden_60"] = _load_golden()[: limit or None]

    summary = {"base": base_path, "ft": ft_path, "k": k}
    for name, probs in datasets.items():
        recs: list[dict] = []  # one per problem, in order
        for s in range(0, len(probs), prob_batch):
            batch = probs[s:s + prob_batch]
            kb = _sample_k(model_b, tok_b, [_prompt(tok_b, p, False) for p in batch],
                           k, max_new_tokens, temperature, top_p)
            kv = _sample_k(model_v, tok_v, [_prompt(tok_v, p, False) for p in batch],
                           k, max_new_tokens, temperature, top_p)
            for p, cb, cv in zip(batch, kb, kv):
                rb, vb, _ = _vote_full(cb)
                rv, vv, _ = _vote_full(cv)
                recs.append({"p": p, "rb": rb, "rv": rv, "vb": vb, "vv": vv,
                             "agree": _agree(rb, rv)})
            print(f"  [{name}] sampled {min(s + len(batch), len(probs))}/{len(probs)}", flush=True)

        # --- judge the disagreements (greedy, base only, NO code) -----------------
        dis = [r for r in recs if not r["agree"]]
        if dis:
            jp = [_judge_prompt(tok_b, r["p"]["question"], r["rb"], r["rv"]) for r in dis]
            jouts = []
            for s in range(0, len(jp), prob_batch):
                jouts += _generate_greedy(model_b, tok_b, jp[s:s + prob_batch], judge_tokens)
            for r, jo in zip(dis, jouts):
                r["choice"] = _parse_choice(jo) or default_pick
                r["judge_raw"] = jo.strip()[:200]

        # --- pick chosen rep + score ---------------------------------------------
        n_ok = 0
        rows = []
        for r in recs:
            p = r["p"]
            if r["agree"]:
                chosen, src = r["rb"], "agree"
            else:
                src = r.get("choice", default_pick)
                chosen = r["rb"] if src == "A" else r["rv"]
            sc = evaluator.score(chosen["stdout"], p["gold_answer"], p["gold_unit"])
            n_ok += int(sc.is_correct)
            # ---- verbose per-problem voting trace -------------------------------
            bf = _final_lines(r["rb"]["stdout"]); vf = _final_lines(r["rv"]["stdout"])
            if r["agree"]:
                decision = "AGREE"
            else:
                jr = r.get("judge_raw", "").replace("\n", " ")
                decision = f"JUDGE->{src}({'base' if src == 'A' else 'v07'})  judge:\"{jr[:90]}\""
            mark = "OK " if sc.is_correct else "XX "
            print(f"    {mark}{p['id']:<11} base[{r['vb']}/{k}]={bf[:46]:<46} "
                  f"v07[{r['vv']}/{k}]={vf[:46]:<46} | {decision} | gold={p['gold_answer']}",
                  flush=True)
            row = {"id": p["id"], "correct": sc.is_correct, "agree": r["agree"], "chosen": src,
                   "base_votes": f"{r['vb']}/{k}", "v07_votes": f"{r['vv']}/{k}",
                   "answer_type": p["answer_type"], "domain": p["domain"],
                   "gold": p["gold_answer"], "gold_unit": p["gold_unit"],
                   "pred": str(sc.pred_value),
                   "base_final": _final_lines(r["rb"]["stdout"]),
                   "v07_final": _final_lines(r["rv"]["stdout"])}
            if not r["agree"]:
                row["judge_raw"] = r.get("judge_raw", "")
            if explain:
                ep = _explain_prompt(tok_b, p["question"], chosen)
                row["explanation_cot"] = _generate_greedy(model_b, tok_b, [ep], max_new_tokens)[0]
            rows.append(row)

        acc = n_ok / len(probs) if probs else 0.0
        n_agree = sum(r["agree"] for r in recs)
        agree_ok = sum(1 for r, row in zip(recs, rows) if r["agree"] and row["correct"])
        judge_ok = sum(1 for r, row in zip(recs, rows) if not r["agree"] and row["correct"])
        print(f"[ens] {name}: {n_ok}/{len(probs)} = {acc:.3f} | "
              f"agree {n_agree}/{len(probs)} (correct {agree_ok}) | "
              f"judged {len(probs) - n_agree} (correct {judge_ok})")
        summary[name] = {"n": len(probs), "correct": n_ok, "accuracy": round(acc, 4),
                         "agree": n_agree, "agree_correct": agree_ok,
                         "judged": len(probs) - n_agree, "judge_correct": judge_ok, "rows": rows}
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        (OUT_DIR / f"ens_{name}.json").write_text(json.dumps(summary[name], indent=2, ensure_ascii=False))
        print(f"[ens] saved {OUT_DIR / f'ens_{name}.json'}")

    msg = " ".join(f"{n}={summary[n]['accuracy']}" for n in ("val_56", "golden_60") if n in summary)
    print(f"[ens] DONE {msg}")
    return summary


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True, help="base model (also the judge), e.g. Qwen/Qwen3.5-4B")
    ap.add_argument("--ft", required=True, help="fine-tuned model (merged dir or hub repo)")
    ap.add_argument("--sets", choices=["both", "val", "golden"], default="both")
    ap.add_argument("--k", type=int, default=5)
    ap.add_argument("--temperature", type=float, default=0.7)
    ap.add_argument("--top-p", type=float, default=0.95)
    ap.add_argument("--max-new-tokens", type=int, default=2048)
    ap.add_argument("--prob-batch", type=int, default=8)
    ap.add_argument("--judge-tokens", type=int, default=256)
    ap.add_argument("--default-pick", choices=["A", "B"], default="B",
                    help="fallback when the judge emits no clear A/B (B=fine-tuned)")
    ap.add_argument("--explain", action="store_true", help="also generate explanation+CoT")
    ap.add_argument("--limit", type=int, default=None)
    args = ap.parse_args()
    run(args.base, args.ft, sets=args.sets, k=args.k, temperature=args.temperature,
        top_p=args.top_p, max_new_tokens=args.max_new_tokens, prob_batch=args.prob_batch,
        limit=args.limit, explain=args.explain, judge_tokens=args.judge_tokens,
        default_pick=args.default_pick)
