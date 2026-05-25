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
You are a First-Order Logic (FOL) translator. Convert each numbered natural-language (NL) premise into a precise FOL formula.

### Rules
1. Predicate names MUST be derived EXACTLY from the NL text — use full CamelCase (e.g. "UserFriendly", "CompatibleWithEcosystem"). NEVER abbreviate to single letters (e.g. U, C, E are FORBIDDEN unless the NL itself uses that letter).
2. Map each NL premise to exactly one FOL formula, in the same order and same count.
3. Output ONLY a JSON object with key "premises_fol" whose value is a list of strings.
4. No markdown fences, no explanation, no commentary outside the JSON.
5. NEVER introduce predicates not grounded in the NL text — do not add extra predicates (e.g. D(x) for "device") unless explicitly stated.
6. If a premise contains a parenthetical hint like "(¬R)" or "(U)", use that exact predicate letter — this overrides Rule 1.

### Context
- Quantifiers: ∀x (...), ∃x (...)
- Connectives: → (implies), ∧ (and), ∨ (or), ¬ (not), ↔ (iff)
- Nested implications: "If (if A then B) then C" → ((A → B) → C)
- Negated quantifiers: "not necessarily ∃" → ¬∃x (...), "not necessarily ∀" → ¬∀x (...)

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
  "∀x (ParticipatesInSocialWork(x) → MeetsExtracurricularRequirements(x))",
  "∀x (MeetsAcademicRequirements(x) → Student(x))",
  "∀x ((MeetsAcademicRequirements(x) → Student(x)) → (FullyParticipatesInConductTraining(x) → EligibleForGraduation(x)))",
  "∃x (Student(x) ∧ ParticipatesInSocialWork(x))",
  "∀x (Student(x) → FullyParticipatesInConductTraining(x))"
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
