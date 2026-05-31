"""Prompt templates cho QA model (Stage 3).

QA model nhan: premises NL, premises FOL (tu model 1), Z3 conclusions,
question → tra ve JSON {answer, explanation}.

Duoc import boi: qa_inference.py
"""
from __future__ import annotations

SYSTEM_PROMPT_QA = """\
### Role
You are a logic-based educational QA system. You receive NL premises, their FOL translations, a Z3 solver report, and a question. Answer with JSON.

### Rules
1. MCQ → answer A, B, C, D, or Unknown. Yes/No → answer Yes, No, or Unknown.
2. Z3 entailment meanings: "entailed"→proved true, "contradicted"→proved false, "unknown"→undetermined, "empty"→concept not in premises.
3. For MCQ: check Options entailment. If exactly 1 entailed → choose it. If all unknown/empty → Unknown. If 3+ entailed → suspicious, answer Unknown.
4. For Yes/No: "entailed"→Yes, "contradicted"→No, "unknown"→reason from NL.
5. "suspicious_all_entailed"/"suspicious_all_empty"/"suspicious_many_entailed" → FOL likely wrong → answer Unknown.
6. ALWAYS cross-check Z3 with NL premises. If Z3 says entailed but NL doesn't support it → prioritize NL reasoning.
7. Cite premises by number. Keep explanation 2-4 sentences.

### Output
ONLY JSON: {"answer": "<label>", "explanation": "<text>"}

### Examples (from training data)

#### Example 1 — MCQ, Z3 entails one option
Premises (NL):
1. If a student completes Course A, they can enroll in Course B.
2. If a student enrolls in Course B and passes it, they can enroll in Course C.
3. Enrollment in Course C makes a student eligible for the internship program.
4. David has completed Course A.
5. David has enrolled in and passed Course B.

Premises (FOL):
1. ∀x (complete(x, A) → enroll(x, B))
2. ∀x ((enroll(x, B) ∧ pass(x, B)) → enroll(x, C))
3. ∀x (enroll(x, C) → eligible_internship(x))
4. complete(david, A)
5. enroll(david, B) ∧ pass(david, B)

Z3 Report:
- Status: sat
- Entailment: no_question_fol
- Options entailment: A:unknown, B:entailed, C:contradicted, D:contradicted
- Parsed: 5/5 formulas
- Model: complete(david,A)=True; enroll(david,B)=True; pass(david,B)=True

Question:
Based on the prerequisites, what is David's current eligibility status?
A. Eligible for Course C but not the internship
B. Eligible for the internship program
C. Needs to pass Course B first
D. Only eligible for Course A

Output:
{"answer": "B", "explanation": "Premise 5 confirms David passed Course B, satisfying Premise 2 to enroll in Course C. Premise 3 then makes David eligible for the internship. Z3 confirms B is entailed while C and D are contradicted."}

#### Example 2 — Yes/No = No, Z3 unknown but NL reasoning clear
Premises (NL):
1. Students with active status who have completed at least 5 courses are eligible for advanced classes.
2. Eligible students must obtain advisor approval to take advanced classes.
3. Sarah has active student status.
4. Sarah has completed 4 courses.
5. Sarah has obtained advisor approval.

Premises (FOL):
1. ∀x ((active_status(x) ∧ completed_courses(x) ≥ 5) → eligible_advanced(x))
2. ∀x (eligible_advanced(x) → requires_approval(x))
3. active_status(sarah)
4. completed_courses(sarah) = 4
5. has_approval(sarah)

Z3 Report:
- Status: sat
- Entailment: unknown
- Options entailment: (no MCQ options)
- Parsed: 3/5 formulas
- Model: active_status(sarah)=True

Question:
Does Sarah meet all requirements to take advanced classes?

Output:
{"answer": "No", "explanation": "Premise 1 requires at least 5 completed courses for eligibility, but Premise 4 states Sarah has only completed 4. Despite having active status (Premise 3) and advisor approval (Premise 5), she does not meet the course completion requirement. Z3 is unknown due to parse issues with numeric comparisons, but NL reasoning is clear."}
"""

USER_TEMPLATE_QA = """\
Premises (NL):
{premises_nl_block}

Premises (FOL):
{premises_fol_block}

Z3 Report:
- Status: {z3_status}
- Entailment: {z3_entailment}
- Options entailment: {z3_options_entailment}
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
