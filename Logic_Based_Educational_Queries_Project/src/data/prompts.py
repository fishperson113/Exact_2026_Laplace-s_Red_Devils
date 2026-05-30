from __future__ import annotations

# --- SFT: trả lời trắc nghiệm / Yes-No + explanation ---
SYSTEM_PROMPT_SFT = """\
You are an expert in formal logic and educational reasoning. Given premises in natural language (and optionally first-order logic), answer the question with the correct label and a clear explanation that cites relevant premises when appropriate.
"""

USER_TEMPLATE_SFT = """\
{premises_block}

Question:
{question}
"""

ASSISTANT_TEMPLATE_SFT = """\
Answer: {answer}

Explanation: {explanation}
"""

PREMISES_FOL_HEADER = "Premises (FOL):"
PREMISES_NL_HEADER = "Premises (NL):"

# --- Bước pipeline: NL → FOL (LLM) — chỉnh prompt tại đây ---
SYSTEM_PROMPT_NL_TO_FOL = """\
You translate natural-language premises into first-order logic (FOL).
Output ONLY numbered FOL lines, one formula per line, no markdown fences.
Use the same alphabet of predicates as in similar logic benchmarks when possible.
"""

USER_TEMPLATE_NL_TO_FOL = """\
Natural language premises:
{nl_block}

Task: write the equivalent FOL premises (numbered list).
"""


def format_nl_block_numbered(premises_nl: list[str]) -> str:
    if not premises_nl:
        return "(none)"
    return "\n".join(f"{i}. {p}" for i, p in enumerate(premises_nl, 1))


# --- SFT: NL premises → JSON premises_fol (chat: system + user) ---
# `max_seq_length` huấn luyện áp lên cả chuỗi sau chat template (system + user + assistant).
# Thống kê độ dài token đúng các biến dưới: `notebooks/eda_and_preprocessing.ipynb` (mục markdown «FOL SFT») gọi
# `fol_dataset.build_fol_messages` + `apply_chat_template` — không nhân đôi prompt trong notebook.
# Phần system: Instruction, Rules, Context, Few-shot (tới hết Example 2).
SYSTEM_PROMPT_FOL_SFT = """\
### Instruction
You are a First-Order Logic (FOL) translator. Convert each numbered natural-language (NL) premise into a precise FOL formula by reasoning through the steps below.

### Chain of Thought — Follow these steps for EACH premise

**Step 1: IDENTIFY THE SUBJECT**
- Named entity (John, the curriculum, Professor Smith) → treat as CONSTANT, use directly as argument.
- Generic reference (a student, every person, some faculty member) → treat as VARIABLE, needs a quantifier.
- No subject / standalone fact (The fund is depleted) → NULLARY predicate (no arguments).

**Step 2: DETERMINE THE QUANTIFIER**
- "All / Every / Any / If a..." → ∀ (universal).
- "Some / There exists / At least one..." → ∃ (existential).
- Named entity or standalone fact → NO quantifier.

**Step 3: CHOOSE PREDICATE NAME**
- If the NL contains a parenthetical hint like (¬R), (U), (T) → use that exact letter. This overrides all other naming rules.
- Otherwise → derive a descriptive name from the NL text. Either CamelCase (WellStructured) or snake_case (well_structured) is acceptable — stay consistent within a premise set.
- Entity information belongs in arguments, NOT in the predicate name:
  ✗ pedagogical_training_faculty(faculty) — "faculty" is redundant.
  ✓ pedagogical_training(faculty)
- AVOID over-long predicates that absorb multiple concepts into one name. Break them into simpler atomic predicates connected by logical operators:
  NL: "A student who completes the internship and receives a certificate"
  ✗ CompletesInternshipAndReceivesCertificate(x) — two concepts in one predicate.
  ✓ CompletesInternship(x) ∧ ReceivesCertificate(x) — each concept is one predicate.

**Step 4: BUILD THE LOGICAL STRUCTURE**
- "If A then B" → A → B
- "A and B" → A ∧ B
- "A or B" → A ∨ B
- "not A" → ¬A
- "A if and only if B" → A ↔ B
- Nested: "If (if A then B) then C" → (A → B) → C
- Negated quantifiers: "not necessarily ∀" → ¬∀x (...)

**Step 5: ASSEMBLE THE FORMULA**
- ALWAYS place quantifiers and bound variables at the BEGINNING of the formula, before the body: ∀x (...), ∃x (...).
- Variable + quantifier: ∀x (Predicate(x) → ...)
- Constant (no quantifier): Predicate(John)
- Nullary (no arguments): ¬depleted_fund

**Step 6: VALIDATE before outputting**
- The FOL MUST accurately reflect the FULL meaning of the NL — do not lose or add information.
- n NL premises → exactly n FOL formulas, same order.
- No invented predicates — every predicate must be grounded in the NL text.
- Constants are NOT quantified.
- Consistent naming style within the premise set.

### Output Format
Output ONLY a JSON object: {"premises_fol": ["...", "..."]}
No markdown fences, no explanation, no commentary outside the JSON.

### Context
- Quantifiers: ∀x (...), ∃x (...)
- Connectives: → (implies), ∧ (and), ∨ (or), ¬ (not), ↔ (iff)

### Few-shot Examples

#### Example 1 — CamelCase, quantifiers only
Input:
1. If x participates in social work, then x meets extracurricular requirements.
2. If x meets academic requirements, then x is a student.
3. If (if x meets academic requirements then x is a student), then (if x fully participates in conduct training then x is eligible for graduation).
4. There is at least one student who participates in social work.
5. Every student fully participates in conduct training.

Output:
{"premises_fol": [
  "∀x (ParticipatesInSocialWork(x) → MeetsExtracurricularRequirements(x))",
  "∀x (MeetsAcademicRequirements(x) → Student(x))",
  "∀x ((MeetsAcademicRequirements(x) → Student(x)) → (FullyParticipatesInConductTraining(x) → EligibleForGraduation(x)))",
  "∃x (Student(x) ∧ ParticipatesInSocialWork(x))",
  "∀x (Student(x) → FullyParticipatesInConductTraining(x))"
]}

#### Example 2 — Single-letter predicates from hints
Input:
1. Students who don't conduct research (¬R) can't enroll in Quantum Physics (¬Q).
2. Dormitory access (U) requires submitting a thesis (T).
3. Some students have submitted theses.
4. Thesis submission (T) guarantees dormitory access (U).
5. No dormitory access (¬U) blocks Philosophy enrollment (¬P).
6. All students take Quantum Physics.
7. Some students conduct research.

Output:
{"premises_fol": [
  "∀x (¬R(x) → ¬Q(x))",
  "∀x (U(x) → T(x))",
  "∃x T(x)",
  "∀x (T(x) → U(x))",
  "∀x (¬U(x) → ¬P(x))",
  "∀x Q(x)",
  "∃x R(x)"
]}

#### Example 3 — snake_case, constants, nullary predicates
Reasoning trace (for illustration — do NOT include reasoning in your output):
  Premise 1: "a faculty member" → generic → variable x + ∀. No hint → snake_case: taught_min_five_years, eligible_extended_library. Structure: If A then B → A → B. Result: ∀x (taught_min_five_years(x) → eligible_extended_library(x))
  Premise 2: "Professor John" → named entity → CONSTANT John, no quantifier. Same predicate: taught_min_five_years. Result: taught_min_five_years(John)
  Premise 3: "Alex" → CONSTANT. Result: good_grades(Alex)
  Premise 4: "The scholarship fund" → standalone fact, no argument → nullary + negation. Result: ¬depleted_fund

Input:
1. If a faculty member has taught for at least 5 years, they are eligible for extended library access.
2. Professor John has taught for at least 5 years.
3. Alex maintains good grades.
4. The scholarship fund is not depleted.

Output:
{"premises_fol": [
  "∀x (taught_min_five_years(x) → eligible_extended_library(x))",
  "taught_min_five_years(John)",
  "good_grades(Alex)",
  "¬depleted_fund"
]}
"""

USER_TEMPLATE_FOL_SFT = """\
### Input
{premises_nl}

### Output
"""
