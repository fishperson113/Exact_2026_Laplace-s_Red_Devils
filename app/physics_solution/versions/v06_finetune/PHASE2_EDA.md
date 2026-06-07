# v06 Phase 2 — Trajectory-generation EDA (stratified de-risk)

Run **2026-06-01** on a Vast RTX 3090 to de-risk the full 1671-problem run before
committing GPU hours. Setup details + host fixes: [VAST_BRINGUP_NOTES.md](VAST_BRINGUP_NOTES.md).

## Setup
- **56 stratified problems** (`input/problems_strat.jsonl`): all 6 domains + every answer
  type (numeric 34, yes_no 8, multi_value 8, text 6) + 5 Vietjack-sourced.
- **vLLM** `Qwen/Qwen3.5-4B` bf16, 8192-ctx, `--enforce-eager`, thread-capped (RTX 3090).
- **selfgen** K=8 over temps `[0.2,0.5,0.8,1.0]`, retry-once-on-error; **teacher** `deepseek-v4-pro`.

## 1. Self-gen solve rate (Route 1, K=8 multi-sample)
**37/56 (66%) solved by Qwen alone.** Residual (19) → teacher.

| Domain | solved | | Answer type | solved |
|---|---|---|---|---|
| LDDT | 6/6 | | numeric | 27/34 (79%) |
| NL | 5/5 | | multi_value | 6/8 (75%) |
| THCB | 9/10 | | yes_no | 3/8 (38%) |
| CH | 8/14 | | **text** | **1/6 (17%)** |
| TD | 3/7 (43%) | | | |
| DDT | 6/14 (43%) | | | |

## 2. Per-temperature pass@1 (single sample, probe over all 56)
Raw per-sample success (no dedup, no retry) — measures "draw ONE sample at temp T":

| Temp | pass@1 |
|---|---|
| **0.2** | **31/56 = 55.4%** |
| 0.5 | 29/56 = 51.8% |
| 0.8 | 24/56 = 42.9% |
| 1.0 | 29/56 = 51.8% |
| overall | 113/224 = 50.4% |

By answer type (pass@1, all temps): numeric **62.5%**, multi_value **59.4%**,
yes_no **25.0%**, text **4.2%**.

> Low temperature (0.2) is the most reliable single sample; T=0.8 dips. Multi-sampling
> (K=8) lifts the per-problem solve rate to 66% (§1) vs ~50% pass@1. A numeric-only probe
> (n=5, 24 problems) gave the same shape: T=0.2 73%, T=0.5 76%, T=0.8 68%, T=1.0 68%,
> pass@5 ≈ 80–83% everywhere.

## 3. Teacher (Route 2/3) recovery
**19/19 residual solved (100%)** by deepseek-v4-pro → combined coverage **56/56**. The
residual it cleaned up was exactly the hard tail: DDT/TD induction-capacitor + yes_no/text.

## 4. Guards → final SFT set
**230 candidates → 153 trajectories kept.** Spurious rejected: `literal_final_answer` 14,
`gold_hardcoded_literal` 1 (teacher). Coverage **51/56** (5 problems whose only trajectories
were literal echoes were correctly dropped). Kept distribution: by domain CH 33 / DDT 30 /
THCB 34 / LDDT 20 / NL 20 / TD 16; by answer_type numeric 109 / multi_value 26 / yes_no 12 /
text 6; by route self_gen 139 / teacher_rewrite 14; ≤4 per problem (cap).

> **Guard bug found & fixed here** (the point of the de-risk): the original
> `gold-as-literal` / `no-computation` checks ran on *all* routes and false-flagged **64**
> good self-gen trajectories — e.g. resonance problems where the *given* `Z = 60.0` equals
> the answer (Z=R), an innocent literal. Self-gen never sees gold, so those checks are now
> **teacher-only**; `yes_no` keeps a comparison-required check on all routes (a correct
> Yes/No is otherwise a 50/50 coin flip). This raised kept 108 → 153 and coverage 40 → 51.

## Takeaways for the full 1671 run
- **Text answers are ~hopeless for code-gen** (4% pass@1) — expect to lean on the teacher,
  or consider excluding pure-text targets from the SFT objective.
- **DDT / TD / yes_no / text concentrate the residual** → the DeepSeek teacher is essential
  (it recovered 100% of this subset's residual; cost scales with residual size).
- **Low temps are more sample-efficient** — could weight sampling toward 0.2–0.5, or trim
  the temp set, to cut GPU time on the full run.
- **Guards are now safe for self-gen** — no more false rejection of valid identity/given-based
  answers; only genuine literal-echoes (15/230 here) are dropped.
- Self-gen ~66% + teacher backfill ⇒ near-full coverage expected on the 1671 set, but the
  teacher (API cost) will carry the harder ~34%.
