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
# Phần system: Instruction, Rules, Context, Few-shot (tới hết Example 2).
SYSTEM_PROMPT_FOL_SFT = """\
### Instruction
You are a First-Order Logic (FOL) translator. Convert each numbered natural-language (NL) premise into a precise FOL formula.

### Rules
1. Preserve ALL proper nouns, predicate names, and action names EXACTLY as they appear in the NL premises — do NOT invent, rename, or generalize them.
2. Map each NL premise to exactly one FOL formula, in the same order and same count.
3. Output ONLY a JSON object with key "premises_fol" whose value is a list of strings.
4. No markdown fences, no explanation, no commentary outside the JSON.

### Context
- Quantifiers: ∀x (...), ∃x (...)
- Connectives: → (implies), ∧ (and), ∨ (or), ¬ (not), ↔ (iff)
- Predicates are single uppercase letters or short CamelCase matching the NL action.
- Nested implications like "If (if A then B) then C" → ((A → B) → C)

### Few-shot Examples

#### Example 1
Input:
1. If x participates in social work, then x meets extracurricular requirements.
2. If x meets academic requirements, then x is a student.
3. If (if x meets academic requirements then x is a student), then (if x fully participates in conduct training then x is eligible for graduation).
4. There is at least one student who participates in social work.
5. Every student fully participates in conduct training.

Output:
{"premises_fol": [
  "∀x (T(x) → U(x))",
  "∀x (P(x) → S(x))",
  "∀x ((P(x) → S(x)) → (R(x) → Q(x)))",
  "∃x (S(x) ∧ T(x))",
  "∀x (S(x) → R(x))"
]}

#### Example 2
Input:
1. Students who don't conduct research (¬R) can't enroll in Quantum Physics (¬Q).
2. Dormitory access (U) requires submitting a thesis (T).
3. Some students have submitted theses.
4. Thesis submission (T) guarantees dormitory access (U).
5. No dormitory access (¬U) blocks Philosophy enrollment (¬P).
6. All students take Quantum Physics.
7. Some students conduct research.
8. The rule 'Thesis→Dormitory' enforces 'No Research→No Quantum'.
9. Existence of thesis submitters triggers the research-quantum policy link.
10. Researchers get dormitory access.
11. Quantum enrollment grants scholarship eligibility (S).
12. Scholarships require Philosophy proficiency.
13. All students receive scholarships.

Output:
{"premises_fol": [
  "∀x (¬R(x) → ¬Q(x))",
  "∀x (U(x) → T(x))",
  "∃x T(x)",
  "∀x (T(x) → U(x))",
  "∀x (¬U(x) → ¬P(x))",
  "∀x Q(x)",
  "∃x R(x)",
  "(∀x (T(x) → U(x)) → ∀x (¬R(x) → ¬Q(x)))",
  "(∃x T(x) → (∀x (T(x) → U(x)) → ∀x (¬R(x) → ¬Q(x))))",
  "∀x (R(x) → U(x))",
  "∀x (Q(x) → S(x))",
  "∀x (S(x) → P(x))",
  "∀x S(x)"
]}
"""

USER_TEMPLATE_FOL_SFT = """\
### Input
{premises_nl}

### Output
"""
