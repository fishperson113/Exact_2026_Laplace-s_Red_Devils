"""Compare old prompt (RTX 3090) vs new code-first prompt (RTX 4090) results."""
import json
from pathlib import Path
from collections import Counter

base_dir = Path(__file__).parent / "output"
old_file = base_dir / "results_golden_rtx3090_old_prompt.json"
new_file = base_dir / "results.json"

with open(old_file, "r", encoding="utf-8") as f:
    old_data = json.load(f)
with open(new_file, "r", encoding="utf-8") as f:
    new_data = json.load(f)

old_rows = {r["id"]: r for r in old_data["rows"]}
new_rows = {r["id"]: r for r in new_data["rows"]}

all_ids = sorted(set(old_rows.keys()) | set(new_rows.keys()))

# Categories
correct_to_wrong = []  # Regression
wrong_to_correct = []  # Improvement
both_correct = []
both_wrong = []

for qid in all_ids:
    old = old_rows.get(qid)
    new = new_rows.get(qid)
    if not old or not new:
        continue
    o_correct = old["is_correct"]
    n_correct = new["is_correct"]
    if o_correct and not n_correct:
        correct_to_wrong.append(qid)
    elif not o_correct and n_correct:
        wrong_to_correct.append(qid)
    elif o_correct and n_correct:
        both_correct.append(qid)
    else:
        both_wrong.append(qid)

print("=" * 70)
print("REGRESSION ANALYSIS: Old Prompt (3090) vs New Code-First (4090)")
print("=" * 70)
print(f"\nTotal questions: {len(all_ids)}")
print(f"  Both correct:        {len(both_correct)}")
print(f"  Both wrong:          {len(both_wrong)}")
print(f"  REGRESSION (->wrong): {len(correct_to_wrong)}")
print(f"  IMPROVEMENT (->right):{len(wrong_to_correct)}")
print(f"\nNet change: {len(wrong_to_correct) - len(correct_to_wrong):+d}")

# Analyze regressions
print("\n" + "=" * 70)
print("REGRESSIONS (was correct, now wrong)")
print("=" * 70)

regression_methods = Counter()
regression_patterns = []

for qid in correct_to_wrong:
    old = old_rows[qid]
    new = new_rows[qid]
    old_method = old["extra"].get("solve_method", "unknown")
    new_method = new["extra"].get("solve_method", "unknown")
    regression_methods[new_method] += 1

    # Check for repetition in raw_completion
    raw = new["extra"].get("raw_completion", "") or ""
    has_repetition = False
    if raw:
        lines = raw.split("\n")
        if len(lines) > 20:
            # Check if many consecutive lines are very similar
            repeated = 0
            for i in range(1, min(len(lines), 100)):
                if lines[i] == lines[i-1] and len(lines[i].strip()) > 5:
                    repeated += 1
            if repeated > 10:
                has_repetition = True

    has_no_code = new["extra"].get("generated_code") is None

    pattern = []
    if new_method == "timeout":
        pattern.append("TIMEOUT")
    if has_repetition:
        pattern.append("REPETITION_LOOP")
    if has_no_code:
        pattern.append("NO_CODE_GENERATED")
    if new_method == "code_execution" and new["pred_numeric"] is not None:
        pattern.append("WRONG_ANSWER")
    if new_method == "failed":
        pattern.append("FAILED")

    pattern_str = "+".join(pattern) if pattern else "UNKNOWN"
    regression_patterns.append((qid, pattern_str, old["extra"].get("solve_method"), new_method))

    print(f"\n  {qid}: {pattern_str}")
    print(f"    Old method: {old_method} | New method: {new_method}")
    print(f"    Old time: {old['elapsed_s']:.1f}s | New time: {new['elapsed_s']:.1f}s")
    if old.get("completion"):
        print(f"    Old answer: {old['completion'][:80]}")
    if new.get("completion"):
        print(f"    New answer: {new['completion'][:80]}")
    print(f"    Gold: {old['gold_answer']} {old.get('gold_unit', '')}")

print("\n\nRegression by new solve_method:")
for method, count in regression_methods.most_common():
    print(f"  {method}: {count}")

# Pattern summary
print("\n\nRegression patterns:")
pattern_counts = Counter(p[1] for p in regression_patterns)
for pat, count in pattern_counts.most_common():
    print(f"  {pat}: {count}")

# Timeout analysis
print("\n" + "=" * 70)
print("TIMEOUT ANALYSIS")
print("=" * 70)

old_timeouts = [qid for qid, r in old_rows.items() if r["extra"].get("solve_method") == "timeout"]
new_timeouts = [qid for qid, r in new_rows.items() if r["extra"].get("solve_method") == "timeout"]

print(f"\nOld timeouts: {len(old_timeouts)} | New timeouts: {len(new_timeouts)}")
print(f"New timeouts that were NOT timeout before: {set(new_timeouts) - set(old_timeouts)}")
print(f"Old timeouts that are NOT timeout now: {set(old_timeouts) - set(new_timeouts)}")

# Check repetition in new timeouts
print("\nRepetition check in NEW timeouts:")
for qid in sorted(new_timeouts):
    new = new_rows[qid]
    raw = new["extra"].get("raw_completion", "") or ""
    code = new["extra"].get("generated_code")
    lines = raw.split("\n")

    # Detect repetition
    repeated_count = 0
    for i in range(1, min(len(lines), 200)):
        if lines[i] == lines[i-1] and len(lines[i].strip()) > 3:
            repeated_count += 1

    has_code = code is not None
    print(f"  {qid}: lines={len(lines)}, repeated_lines={repeated_count}, has_code={has_code}, time={new['elapsed_s']:.1f}s")

# Latency comparison
print("\n" + "=" * 70)
print("LATENCY COMPARISON")
print("=" * 70)

old_times = [r["elapsed_s"] for r in old_rows.values() if r["extra"].get("solve_method") == "code_execution"]
new_times = [r["elapsed_s"] for r in new_rows.values() if r["extra"].get("solve_method") == "code_execution"]

if old_times:
    print(f"\nOld (code_execution only): mean={sum(old_times)/len(old_times):.1f}s, "
          f"median={sorted(old_times)[len(old_times)//2]:.1f}s, n={len(old_times)}")
if new_times:
    print(f"New (code_execution only): mean={sum(new_times)/len(new_times):.1f}s, "
          f"median={sorted(new_times)[len(new_times)//2]:.1f}s, n={len(new_times)}")

# Token length proxy: check raw_completion length
print("\n" + "=" * 70)
print("COMPLETION LENGTH (proxy for token usage)")
print("=" * 70)

old_lens = [len(r["extra"].get("raw_completion", "") or "") for r in old_rows.values()]
new_lens = [len(r["extra"].get("raw_completion", "") or "") for r in new_rows.values()]

print(f"\nOld: mean={sum(old_lens)/len(old_lens):.0f} chars, max={max(old_lens)}")
print(f"New: mean={sum(new_lens)/len(new_lens):.0f} chars, max={max(new_lens)}")

# Improvements detail
print("\n" + "=" * 70)
print("IMPROVEMENTS (was wrong, now correct)")
print("=" * 70)
for qid in wrong_to_correct:
    old = old_rows[qid]
    new = new_rows[qid]
    print(f"\n  {qid}:")
    print(f"    Old method: {old['extra'].get('solve_method')} | New method: {new['extra'].get('solve_method')}")
    print(f"    Gold: {old['gold_answer']}")
