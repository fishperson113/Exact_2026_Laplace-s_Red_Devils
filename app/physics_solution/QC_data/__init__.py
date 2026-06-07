"""Content-level data QC for the v06 SFT set (BTC golden + Vietjack).

A deeper pass than Phase-1's Step-0 `filter` (which only drops figure/underspecified
problems). This one detects *mechanical corruption* in the problem STATEMENT — OCR
misreads, dropped math symbols (π, √, exponents), garbled numbers/units, lost MCQ
options — using DeepSeek-v4-pro, with the gold answer as a detection/repair signal.

Per problem the verdict is CLEAN / FIX / DROP:
  - CLEAN  keep as-is (a merely HARD problem is still clean).
  - FIX    repair only the corrupted token (preserve BTC wording/format), keep gold.
  - DROP   unrepairable (lost data/options, or statement-vs-gold physically inconsistent).

The gold is used ONLY to detect/repair; the stored question is the corrected statement,
so a downstream solver never sees gold and never learns to "guess the author's intent".

Run: `python -m app.physics_solution.QC_data.run_qc` (see run_qc.py / README.md).
Output lands in `app/physics_solution/QC_data/gold/`.
"""
