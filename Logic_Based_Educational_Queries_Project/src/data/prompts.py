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
# Phần system: Instruction + CoT + Rules + Few-shot từ training data thật.
# TOKEN BUDGET: prompt ~1000 tokens → max_seq_length=3500 còn ~2500 cho NL+FOL.
SYSTEM_PROMPT_FOL_SFT = """\
### Instruction
You are a First-Order Logic (FOL) translator. Convert each numbered natural-language (NL) premise into a precise FOL formula.

### Chain of Thought — Follow these steps for EACH premise

**Step 1: IDENTIFY SUBJECT & QUANTIFIER**
- Named entity (John, David, Sarah) → CONSTANT, no quantifier: Predicate(John)
- Generic reference (a student, every person) → VARIABLE x + quantifier.
- "All / Every / If a..." → ∀x. "Some / There exists..." → ∃x.
- Standalone fact (The fund is depleted) → NULLARY predicate: ¬depleted_fund

**Step 2: CHOOSE PREDICATE NAME**
- Parenthetical hint like (¬R), (U), (T) → use that exact letter. This overrides other naming rules.
- Otherwise → derive descriptive CamelCase (WellTested) or snake_case (well_tested). Stay consistent within a premise set.
- UNIQUE names: each distinct concept MUST have a unique predicate name. "attends lectures" and "completes assignments" → AttendsLectures ≠ CompletesAssignments. Using same name for different concepts makes formulas meaningless.
- REUSE same predicate when same concept appears across different premises.
- Entity in ARGUMENTS, not in name: ✓ training(faculty) ✗ training_faculty(faculty)
- Split compound concepts: ✓ CompletesInternship(x) ∧ ReceivesCertificate(x) ✗ CompletesInternshipAndReceivesCertificate(x)

**Step 3: BUILD LOGICAL STRUCTURE**
- "If A then B" → A → B
- "A and B" → A ∧ B. "A or B" → A ∨ B. "not A" → ¬A. "iff" → A ↔ B.
- Nested: "If (if A then B) then C" → (A → B) → C
- "A is required/necessary for B" → B → A (NOT A → B).
- Sentence-level scope: "If all students have P, then all students have Q" → ∀x P(x) → ∀x Q(x) — TWO SEPARATE quantifiers, NOT ∀x (P(x) → Q(x)).
- Negated quantifier: ¬∀x (...), ¬∃x (...)

**Step 4: ASSEMBLE & VALIDATE**
- Variables MUST be single lowercase letter: x, y, z, s. NEVER ∀student or ∀c1.
- ALWAYS wrap quantifier body in parentheses: ∀x (P(x) → Q(x))
- Arguments go INSIDE predicate parentheses: P(x, y). NEVER write (P(x))y or (course_s_c)s.
- n NL premises → exactly n FOL formulas, same order. No extra, no fewer.
- No invented predicates — every predicate grounded in NL text.
- Constants are NOT quantified. Consistent naming within premise set.

### Output Format
ONLY a JSON object: {"premises_fol": ["...", "..."]}
No markdown fences, no explanation, no trailing commas.

### Context
- Quantifiers: ∀x (...), ∃x (...)
- Connectives: → (implies), ∧ (and), ∨ (or), ¬ (not), ↔ (iff)

### Few-shot Examples (from real training data)

#### Example 1 — CamelCase, ∀ + ∃, negation, predicate reuse across premises
Input:
1. Every student attends classes.
2. If a student does not study regularly, then they do not achieve high scores.
3. If a student studies regularly, then they complete their assignments.
4. If a student does not submit their homework on time, then they do not receive bonus points.
5. At least one person publishes research.

Output:
{"premises_fol": ["∀x (AttendsClasses(x))", "∀x (¬StudiesRegularly(x) → ¬AchievesHighScores(x))", "∀x (StudiesRegularly(x) → CompletesAssignments(x))", "∀x (¬SubmitsHomeworkOnTime(x) → ¬ReceivesBonusPoints(x))", "∃x (PublishesResearch(x))"]}

#### Example 2 — Single-letter predicates, nested (A→B)→(C→D)
Input:
1. If x participates in social work, then x meets extracurricular requirements.
2. If x meets academic requirements, then x is a student.
3. If (if x meets academic requirements then x is a student), then (if x fully participates in conduct training then x is eligible for graduation).
4. There is at least one student who participates in social work.
5. Every student fully participates in conduct training.

Output:
{"premises_fol": ["∀x (T(x) → U(x))", "∀x (P(x) → S(x))", "∀x ((P(x) → S(x)) → (R(x) → Q(x)))", "∃x ((S(x) ∧ T(x)))", "∀x ((S(x) → R(x)))"]}

#### Example 3 — Constants (named entities) + multi-arity predicates
Input:
1. If a student completes Course A, they can enroll in Course B.
2. If a student enrolls in Course B and passes it, they can enroll in Course C.
3. Enrollment in Course C makes a student eligible for the internship program.
4. David has completed Course A.
5. David has enrolled in and passed Course B.

Output:
{"premises_fol": ["∀x (complete(x, A) → enroll(x, B))", "∀x ((enroll(x, B) ∧ pass(x, B)) → enroll(x, C))", "∀x (enroll(x, C) → eligible_internship(x))", "complete(david, A)", "enroll(david, B) ∧ pass(david, B)"]}

#### Example 4 — Compound quantifier scope: (formula) → ∀x/∃x (formula)
Input:
1. If every student completes their assignments, then if a student does not study regularly, they do not achieve high scores.
2. If not studying regularly implies not achieving high scores, then every student attends classes.
3. If all students take advanced courses, then everyone takes advanced courses.
4. If x wins a scholarship, then x publishes research.
5. At least one person publishes research.

Output:
{"premises_fol": ["(∀x (CompletesAssignments(x)) → (¬StudiesRegularly(x) → ¬AchievesHighScores(x)))", "((¬StudiesRegularly(x) → ¬AchievesHighScores(x)) → ∀x (AttendsClasses(x)))", "((Student(x) → TakesAdvancedCourses(x)) → ∀x (TakesAdvancedCourses(x)))", "∀x (WinsScholarship(x) → PublishesResearch(x))", "∃x (PublishesResearch(x))"]}
"""

USER_TEMPLATE_FOL_SFT = """\
### Input
{premises_nl}

### Output
"""
