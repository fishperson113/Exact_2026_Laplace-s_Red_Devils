#!/usr/bin/env python3
"""Generate the one-page solution.pdf for the EXACT 2026 submission (Guide section 8)."""
from fpdf import FPDF

TEAM = "Laplace's Red Devils"
OUT = "/home/nguyen/projects/Exact_2026_Laplace-s_Red_Devils/submission/solution.pdf"

pdf = FPDF(format="A4")
pdf.set_auto_page_break(auto=True, margin=10)
pdf.add_page()
pdf.set_margins(12, 10, 12)

def h(txt, size=12):
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Helvetica", "B", size)
    pdf.set_text_color(20, 50, 110)
    pdf.multi_cell(pdf.epw, 5.2, txt)
    pdf.set_text_color(0, 0, 0)

def p(txt, size=8.3, style=""):
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Helvetica", style, size)
    pdf.multi_cell(pdf.epw, 3.9, txt)

def gap(x=1.2):
    pdf.ln(x)

# Title
pdf.set_font("Helvetica", "B", 14)
pdf.set_text_color(10, 30, 90)
pdf.set_x(pdf.l_margin); pdf.multi_cell(pdf.epw, 6, f"EXACT 2026 - Solution Description - Team \"{TEAM}\"")
pdf.set_text_color(0, 0, 0)
pdf.set_font("Helvetica", "I", 8)
pdf.set_x(pdf.l_margin); pdf.multi_cell(pdf.epw, 4, "Task Type 1 (Logic-Based Educational Queries) + Task Type 2 (Physics). One /predict endpoint, routed by `type`. All LLMs self-hosted via vLLM.")
gap()

# 1. Datasets
h("1. Datasets used")
p("Type 2 - Physics (training only; external/synthetic models used for data generation are declared, never at inference):", style="B")
p("- EXACT 2026 official dataset (EXACT2026_dataset_2026-05-15): 1,352 valid rows (id, question, cot, answer, unit). "
  "Source: competition organizers (machine-translated VN->EN). Used to build execution-verified Program-of-Thought (PoT) SFT trajectories. "
  "Sample: \"A 2 uF capacitor is charged to 12 V; find the stored energy.\" -> answer 1.44e-4, unit J.")
p("- Self-generated + teacher-residual PoT trajectories: ~2,846 execution-verified trajectories over ~1,505 problems, sampled on-policy from "
  "Qwen3.5-4B and completed by DeepSeek/Claude for the residual (external models, TRAINING ONLY). Each: reasoning preamble -> Python -> executed -> FINAL ANSWER/UNIT.")
p("- Vietjack worked physics solutions (grades 10-12), source vietjack.com (crawled), VN->EN translated; supplementary SFT.")
gap()
p("Type 1 - Logic (two-stage FOL -> QA):", style="B")
p("- MALLS-v0.1 (NL -> First-Order-Logic pairs, GPT-4-generated; LogicLLaMA, Yang et al. 2023): 5,000 samples for Stage-1 FOL continued-pretrain. "
  "Sample: \"Every student attends classes.\" -> \"forall x (AttendsClasses(x))\".")
p("- EXACT 2026 official logic training data (organizer): Stage-2 FOL fine-tune + QA (CoT-augmented) training (NL premises + options + question -> answer, premises_used, reasoning).")
gap()

# 2. Approach
h("2. Approach and method")
p("A single POST /predict endpoint reads the `type` field and routes internally; it returns the unified JSON list schema "
  "(query_id, answer, unit, explanation, premises_used, reasoning).")
p("Type 2 (physics): the base Qwen3.5-4B + SFT LoRA emits a short reasoning preamble then ONE Python block; the code is executed in a sandbox "
  "(allowed imports + timeout) and the printed FINAL ANSWER / UNIT is parsed. A pooled self-consistency vote (SFT solver + base model) improves robustness; "
  "the base model writes the natural-language explanation. Answers/units are canonicalized to ASCII per notation_mapping.csv (e.g. ohm, uF, V/m; scientific notation as e-notation).")
p("Type 1 (logic): Stage 1 - the FOL model translates the NL premises into First-Order-Logic formulas. Stage 2 - the QA model reasons over those FOL "
  "formulas in ordered steps (Rule / Fact / Derive / Conclusion) and outputs the chosen option (verbatim), the 0-based premises_used indices it actually cited, and an explanation.")
gap()

# 3. Model size
h("3. Model size calculation (within the 8B-class limit, Guide section 6.3)")
p("Every LLM is a Qwen3.5-4B (a 4B-class model). Two LLMs are served, on two vLLM servers on one GPU:")
p("- vLLM server A (id base): Qwen3.5-4B base = 4.21B language params. Hosts Type-2 solving (judge/explainer) and Type-1 stage-2 QA. "
  "Two PEFT LoRA adapters are loaded on this single base: id sft (Type-2 primary solver) and id qa = v04-QA-CoT (Type-1 stage-2); each ~0.02B delta, no extra base.")
p("- vLLM server B (id fol): Qwen3.5-4B FOL model (fol-v06-cot-augmented) = 4.21B language params. Type-1 stage-1 NL->FOL.")
p("Each composite checkpoint additionally carries ~0.45B visual/MTP weights that are part of the published Qwen3.5-4B and the vLLM-servable architecture; "
  "they are never used for our text-only physics/logic inference. LoRA adapters are PEFT deltas on the shared base, not separate models.", style="I")
gap()
p("Peak GPU residency: Type 2 -> 1 model (~4.2B). Type 1 -> 2 models (FOL + base) = two Qwen3.5-4B in parallel, ~8B-class, "
  "exactly the configuration the Q&A allows (\"two 4B models in parallel, combined 8B, within the limit\"). "
  "Served with vLLM 0.22.1 (self-hosted, OpenAI-compatible); each vLLM server exposes /v1/models. No third-party inference APIs at serving time. "
  "Non-LLM tools (sandboxed Python execution, parsers) do not count toward the limit.", style="")

pdf.output(OUT)
print("wrote", OUT)
