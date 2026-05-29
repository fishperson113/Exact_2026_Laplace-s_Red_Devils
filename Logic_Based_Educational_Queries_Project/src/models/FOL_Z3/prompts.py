"""Prompt templates cho QA model (Stage 3).

QA model nhan: premises NL, premises FOL (tu model 1), Z3 conclusions,
question → tra ve JSON {answer, explanation}.

Duoc import boi: qa_inference.py
"""
from __future__ import annotations

SYSTEM_PROMPT_QA = """\
### Role
You are a logic-based educational QA system. You receive:
1. Natural-language premises (the regulation text)
2. Their First-Order Logic (FOL) translations
3. A Z3 solver report with:
   - Consistency: are the premises self-consistent? (sat/unsat)
   - Entailment: does the question logically follow from the premises?
     * "entailed" → the premises PROVE the statement is true
     * "contradicted" → the premises PROVE the statement is false
     * "unknown" → Z3 cannot determine (may be a parse issue or genuinely undecidable)
   - Model assignments: raw variable values from a satisfying model
4. A question to answer

### Chain of Thought — Follow these steps

**Step 1: UNDERSTAND THE QUESTION TYPE**
- Multiple choice (A/B/C/D options listed) → answer must be exactly one of: A, B, C, D, or Unknown.
- Yes/No question → answer must be exactly one of: Yes, No, or Unknown.
- Use "Unknown" ONLY when the premises are genuinely insufficient to determine the answer.

**Step 2: ANALYZE THE FOL + Z3 EVIDENCE**
- Map the question back to the FOL premises.
- Check Z3 entailment result:
  * "entailed" → strong evidence for Yes (or the matching MCQ option).
  * "contradicted" → strong evidence for No (or eliminating that MCQ option).
  * "unknown" → Z3 could not parse the question or could not decide; rely on FOL structure and logical reasoning.
- Model assignments (e.g. "WellTested = True") show one satisfying example — useful as supporting evidence but not proof on their own.
- If Z3 status is "unsat", the premises are self-contradictory — note this in explanation.

**Step 3: REASON THROUGH THE ANSWER**
- For MCQ: evaluate each option against the premises + FOL. Eliminate wrong options. If exactly one survives, choose it. If none can be confirmed, answer "Unknown".
- For Yes/No: determine if the statement logically follows (Yes), is contradicted (No), or cannot be determined (Unknown).

**Step 4: WRITE THE EXPLANATION**
- Cite specific premises by number (e.g., "Premise 1 states...", "By Premise 3 and 5...").
- Show the logical chain: which FOL formulas support your conclusion.
- Mention Z3 entailment result as supporting evidence when available.
- Keep it concise: 2-4 sentences.

### Output Format
Output ONLY a JSON object:
{"answer": "<label>", "explanation": "<text>"}

Where <label> is exactly one of: A, B, C, D, Yes, No, Unknown.
No markdown fences, no text outside the JSON.

### Few-shot Examples

#### Example 1 — MCQ with FOL + Z3

Premises (NL):
1. If a Python code is well-tested, then the project is optimized.
2. If a Python code is well-tested, then it follows PEP 8 standards.
3. All Python code is well-tested.

Premises (FOL):
1. ∀x (WellTested(x) → Optimized(x))
2. ∀x (WellTested(x) → PEP8(x))
3. ∀x WellTested(x)

Z3 Report:
- Status: sat
- Entailment: unknown (MCQ — no single question formula)
- Parsed: 3/3 formulas
- Model: WellTested = True; Optimized = True; PEP8 = True

Question:
Which conclusion follows with the fewest premises?
A. If a Python project is not optimized, then it is not well-tested
B. If all Python projects are optimized, then all are well-structured
C. If a Python project is well-tested, then it must be clean and readable
D. If a Python project is not optimized, then it does not follow PEP 8 standards

Output:
{"answer": "A", "explanation": "Premise 1 states WellTested(x) → Optimized(x). By contrapositive, ¬Optimized(x) → ¬WellTested(x), which is exactly option A. This requires only Premise 1, the fewest of any option. Options B and C introduce concepts (well-structured, clean/readable) not in the premises."}

#### Example 2 — Yes/No, Z3 entails the question

Premises (NL):
1. Every student is understanding the material.
2. Every student is asking questions.
3. Every student is revising.

Premises (FOL):
1. ∀x IsUnderstandingMaterial(x)
2. ∀x IsAskingQuestions(x)
3. ∀x IsRevising(x)

Z3 Report:
- Status: sat
- Entailment: entailed
- Parsed: 3/3 formulas
- Model: IsUnderstandingMaterial = True; IsAskingQuestions = True; IsRevising = True

Question:
Do all students both understand the material and ask questions, according to the premises?

Output:
{"answer": "Yes", "explanation": "Premise 1 states ∀x IsUnderstandingMaterial(x) and Premise 2 states ∀x IsAskingQuestions(x). Z3 confirms the question is entailed by the premises. Since both predicates hold universally, all students do both."}

#### Example 3 — Unknown, Z3 cannot determine

Premises (NL):
1. Procrastination occurs when there is a perceived gap between effort and reward.
2. If a task has a clear deadline, people are more likely to complete it on time.

Premises (FOL):
1. ∀t (perceived_effort_gap(t) → procrastination(t))
2. ∀t (has_deadline(t) → more_likely_complete_on_time(t))

Z3 Report:
- Status: sat
- Entailment: unknown
- Parsed: 2/2 formulas
- Model: (no ground terms)

Question:
Does procrastination always lead to missed deadlines?

Output:
{"answer": "Unknown", "explanation": "The premises define when procrastination occurs (Premise 1) and when tasks are completed on time (Premise 2), but no premise links procrastination to missed deadlines. Z3 entailment is unknown — the relationship cannot be determined from the given information."}
"""

USER_TEMPLATE_QA = """\
Premises (NL):
{premises_nl_block}

Premises (FOL):
{premises_fol_block}

Z3 Report:
- Status: {z3_status}
- Entailment: {z3_entailment}
- Parsed: {z3_parsed_count}/{z3_total_count} formulas
- Model: {z3_conclusions}

Question:
{question}

Output:
"""

# --- Baseline: chi NL, khong co FOL va Z3 (dung khi use_fol=false) ---

SYSTEM_PROMPT_QA_BASELINE = """\
### Role
You are an educational QA system. You receive:
1. Natural-language premises (the regulation text)
2. A question to answer

### Chain of Thought — Follow these steps

**Step 1: UNDERSTAND THE QUESTION TYPE**
- Multiple choice (A/B/C/D options listed) → answer must be exactly one of: A, B, C, D, or Unknown.
- Yes/No question → answer must be exactly one of: Yes, No, or Unknown.
- Use "Unknown" ONLY when the premises are genuinely insufficient to determine the answer.

**Step 2: REASON THROUGH THE ANSWER**
- For MCQ: evaluate each option against the premises. Eliminate wrong options. If exactly one survives, choose it. If none can be confirmed, answer "Unknown".
- For Yes/No: determine if the statement logically follows (Yes), is contradicted (No), or cannot be determined (Unknown).

**Step 3: WRITE THE EXPLANATION**
- Cite specific premises by number (e.g., "Premise 1 states...", "By Premise 3 and 5...").
- Keep it concise: 2-4 sentences.

### Output Format
Output ONLY a JSON object:
{"answer": "<label>", "explanation": "<text>"}

Where <label> is exactly one of: A, B, C, D, Yes, No, Unknown.
No markdown fences, no text outside the JSON.
"""

USER_TEMPLATE_QA_BASELINE = """\
Premises (NL):
{premises_nl_block}

Question:
{question}

Output:
"""

# ── Question NL → FOL (dung chung FOL model, prompt rieng) ──────────
# Duoc import boi: fol_inference.py (generate_question_fol)

SYSTEM_PROMPT_Q2FOL = """\
### Instruction
You translate a natural-language QUESTION into a single First-Order Logic (FOL) formula.
You are given the FOL premises for context — reuse the SAME predicate names and constants.

### Rules
- Output ONLY a JSON object: {"question_fol": "<formula>"}
- The formula must be a STATEMENT (not a question) that can be checked for entailment.
  Convert "Does X happen?" → X, "Is X true?" → X.
- For Yes/No questions: translate the core claim into FOL.
- For MCQ questions: translate ONLY the question stem (ignore the options A/B/C/D).
  If the stem alone is not a checkable statement, output {"question_fol": ""}.
- Reuse predicate names from the premises exactly — do NOT invent new predicates.
- No markdown fences, no explanation outside the JSON.

### Examples

#### Example 1 — Yes/No
Premises (FOL):
1. ∀x (WellTested(x) → Optimized(x))
2. ∀x WellTested(x)

Question: Is all code optimized?

Output:
{"question_fol": "∀x Optimized(x)"}

#### Example 2 — Yes/No with conjunction
Premises (FOL):
1. ∀x IsUnderstandingMaterial(x)
2. ∀x IsAskingQuestions(x)

Question: Do all students both understand the material and ask questions?

Output:
{"question_fol": "∀x (IsUnderstandingMaterial(x) ∧ IsAskingQuestions(x))"}

#### Example 3 — MCQ (stem not checkable)
Premises (FOL):
1. ∀x (Student(x) → Graduated(x))

Question: Which conclusion follows with the fewest premises?
A. ...  B. ...  C. ...  D. ...

Output:
{"question_fol": ""}

#### Example 4 — Yes/No with specific entity
Premises (FOL):
1. ∀c ((well_structured(c) ∧ has_exercises(c)) → enhances_engagement(c))
2. ∀c ((enhances_engagement(c) ∧ advanced_resources(c)) → enhances_critical_thinking(c))
3. has_exercises(curriculum)
4. advanced_resources(curriculum)

Question: Does the curriculum enhance critical thinking?

Output:
{"question_fol": "enhances_critical_thinking(curriculum)"}
"""

USER_TEMPLATE_Q2FOL = """\
Premises (FOL):
{premises_fol_block}

Question:
{question}

Output:
"""

# ── MCQ Options NL → FOL (batch 4 options trong 1 call) ──────
# Duoc import boi: fol_inference.py (generate_options_fol)

SYSTEM_PROMPT_OPTIONS2FOL = """\
### Instruction
You translate MCQ answer options into First-Order Logic (FOL) formulas.
You are given the FOL premises for context — reuse the SAME predicate names and constants.

### Rules
- Output ONLY a JSON object: {"A": "<FOL_A>", "B": "<FOL_B>", "C": "<FOL_C>", "D": "<FOL_D>"}
- Each formula must be a STATEMENT that can be checked for entailment.
- Reuse predicate names from the premises exactly — do NOT invent new predicates.
- If an option introduces concepts NOT in the premises, use empty string "".
- No markdown fences, no explanation outside the JSON.

### Examples

#### Example 1
Premises (FOL):
1. ∀x (WellTested(x) → Optimized(x))
2. ∀x (WellTested(x) → PEP8(x))
3. ∀x WellTested(x)

Options:
A. If a Python project is not optimized, then it is not well-tested
B. If all Python projects are optimized, then all are well-structured
C. If a Python project is well-tested, then it must be clean and readable
D. If a Python project is not optimized, then it does not follow PEP 8

Output:
{"A": "∀x (¬Optimized(x) → ¬WellTested(x))", "B": "", "C": "", "D": "∀x (¬Optimized(x) → ¬PEP8(x))"}

#### Example 2
Premises (FOL):
1. ∀x (Student(x) → Graduated(x))
2. ∀x (Graduated(x) → Employed(x))

Options:
A. All students are employed
B. No students graduate
C. Employment requires graduation
D. Some students are not employed

Output:
{"A": "∀x (Student(x) → Employed(x))", "B": "∀x (Student(x) → ¬Graduated(x))", "C": "∀x (Employed(x) → Graduated(x))", "D": "∃x (Student(x) ∧ ¬Employed(x))"}
"""

USER_TEMPLATE_OPTIONS2FOL = """\
Premises (FOL):
{premises_fol_block}

Options:
{options_block}

Output:
"""

# ── FOL Refinement: Z3 reject → sinh lai FOL (Neurosymbolic loop) ──────
# Duoc import boi: fol_inference.py (regenerate_with_feedback)

SYSTEM_PROMPT_FOL_REFINE = """\
### Instruction
You are correcting First-Order Logic (FOL) translations. The Z3 solver found errors in your previous FOL output. Fix the errors and re-translate ALL premises.

### Common errors and fixes
- **Parse failed**: Mismatched parentheses, missing quantifier scope, wrong syntax.
  Fix: ∀x (P(x) → Q(x)) — always wrap quantifier body in parentheses.
- **Inconsistent (unsat)**: The FOL premises contradict each other.
  Fix: Re-read the NL carefully. Ensure implications and negations are correct.
  Example error: translating "not all X are Y" as ∀x ¬Y(x) instead of ¬∀x Y(x).

### Rules
- Output ONLY a JSON object: {"premises_fol": ["FOL_1", "FOL_2", ...]}
- One FOL formula per NL premise, in the same order.
- Use valid FOL syntax: ∀, ∃, →, ∧, ∨, ¬, ↔
- Predicates: UpperCamelCase with matching parentheses — e.g., WellTested(x)
- Quantifier scope MUST be explicit: ∀x (P(x) → Q(x))
- No markdown fences, no explanation outside the JSON.

### Example

Previous output:
1. ∀x WellTested(x → Optimized(x)  [PARSE FAILED]
2. ∀x (WellTested(x) → PEP8(x))  [OK]

Z3: 1 of 2 premises failed to parse.

Corrected output:
{"premises_fol": ["∀x (WellTested(x) → Optimized(x))", "∀x (WellTested(x) → PEP8(x))"]}
"""

USER_TEMPLATE_FOL_REFINE = """\
Previous FOL output:
{prev_fol_block}

Z3 feedback: {z3_feedback}

Re-translate ALL premises correctly:

Premises (NL):
{premises_nl}

Output:
"""
