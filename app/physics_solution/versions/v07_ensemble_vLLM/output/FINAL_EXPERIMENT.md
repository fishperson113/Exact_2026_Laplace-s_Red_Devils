# FINAL ensemble decision — SFT-only vs BASE-only vs ENSEMBLE

K=5 samples/side, 3 runs/config, identical samples feed all 3 configs per run (so differences are purely the voting strategy). Explanation/CoT is the same downstream BASE step in all configs (skipped here; does not affect the answer).

## 1. Accuracy per config (mean over runs [min..max])

| set | SFT-only | BASE-only | ENSEMBLE |
|---|---|---|---|
| val (n=56) | 0.863 [0.839..0.893] | 0.833 [0.786..0.875] | 0.869 [0.857..0.893] |
| golden (n=60) | 0.783 [0.767..0.800] | 0.778 [0.767..0.800] | 0.789 [0.783..0.800] |

## 2. Does ENSEMBLE beat the best single model?

- **val**: ensemble 0.869 vs best-single 0.863 (SFT 0.863 / BASE 0.833) → Δ=+0.006 → **ENSEMBLE WINS**
- **golden**: ensemble 0.789 vs best-single 0.783 (SFT 0.783 / BASE 0.778) → Δ=+0.006 → **ENSEMBLE WINS**

## 3. Where does the correct answer come from? (ensemble runs)

Per problem-instance, which side produced ANY correct sample:

| set | both | sft_only | base_only | none |
|---|---|---|---|---|
| val | 155 (92%) | 3 (2%) | 2 (1%) | 8 (5%) |
| golden | 157 (87%) | 5 (3%) | 5 (3%) | 13 (7%) |

*sft_only/base_only > 0 means that model uniquely solves problems the other misses → a reason to ensemble. If ~all 'both', the two are redundant.*

## 4. Domain specialization — SFT vs BASE accuracy by domain

(vote accuracy averaged over all runs; Δ = SFT − BASE; +Δ = SFT stronger)

| set | domain | n | SFT | BASE | ENS | Δ(SFT−BASE) | who |
|---|---|---|---|---|---|---|---|
| val | CH | 14 | 0.93 | 0.90 | 0.93 | +0.02 | tie |
| val | DDT | 14 | 0.79 | 0.71 | 0.79 | +0.07 | SFT |
| val | LDDT | 6 | 0.61 | 0.72 | 0.67 | -0.11 | BASE |
| val | NL | 5 | 1.00 | 1.00 | 1.00 | +0.00 | tie |
| val | TD | 7 | 0.95 | 0.86 | 0.90 | +0.10 | SFT |
| val | THCB | 10 | 0.90 | 0.87 | 0.93 | +0.03 | tie |
| golden | LDDT | 60 | 0.78 | 0.78 | 0.79 | +0.01 | tie |

## 5. Latency (ensemble sampling, CUDA graphs)

- mean 7.8s · median 6.5s · p90 14.9s · max 20.3s (n=348 solves)

*Single-model configs sample K not 2K, so they run a bit faster; all ≪ 60s.*

## 6. Recommendation / interpretation

**Ensemble vs single = effectively a TIE.** Ensemble beats the best single model by only
**+0.6pt** on both sets (val 0.869 vs SFT 0.863; golden 0.789 vs SFT 0.783) — well inside the
run-to-run variance (the [min..max] ranges overlap heavily). Ensembling does **not** meaningfully
raise accuracy.

**Why:** the two models are **largely redundant** — on 87–92% of problem-instances *both* SFT and
BASE already produce a correct sample. The genuinely complementary slice (`sft_only` + `base_only`)
is tiny: ~3% on val, ~6% on golden. And 5–7% are `none` (neither solves) — a hard ceiling no amount
of voting fixes. The pooled vote only converts a fraction of the complementary slice into wins,
hence the ~0.6pt.

**SFT ≥ BASE as a single model** on both sets (SFT 0.863/0.783 vs BASE 0.833/0.778). So if you want
one model, **pick SFT**. The ensemble's one mild plus: a slightly **higher floor** (golden ENS min
0.783 vs SFT min 0.767) — marginally more stable across runs.

**Domain specialization (val, the only multi-domain set):**
- **SFT clearly stronger on `DDT` (+0.07) and `TD` (+0.10).**
- `LDDT` shows BASE +0.11 on val — but that is **n=6 (noise)**; on golden `LDDT` (n=60) the two are
  **tied (0.78/0.78)**, so discount the val-LDDT signal.
- `CH`, `NL`, `THCB` ≈ tied.
→ Reliable specialization is **SFT > BASE on DDT/TD, tie elsewhere**. There is **no domain where
BASE reliably beats SFT**, so domain-weighting collapses to "trust SFT more" = "use SFT". Expected
upside **<1pt**, not worth the complexity now.

**Verdict:**
1. The ensemble is **nearly free** (BASE is already loaded as the explainer; its 5 samples run in
   parallel with SFT's on the one engine) and gives +0.6pt + a higher floor → **keep it if you want
   max robustness at ~no extra cost.**
2. If you prefer **simplicity/lower latency**, **SFT-only K=5 + BASE explainer** loses only ~0.6pt
   and halves the samples.
3. **Do NOT invest in domain-weighting** — the only reliable signal is "SFT ≥ BASE everywhere".
4. The real accuracy lever stays **DATA/coverage** (the 5–7% `none` + selecting the right cluster
   among samples both models already produce), not the voting strategy. *(Consistent with the earlier
   oracle-0.917 / minority-lost finding.)*
