"""
prompts/prompt.py
-----------------
Tập trung TẤT CẢ prompt templates cho cả 2 stage:
  - Stage 1: NL premises  →  FOL  (FOLModel)
  - Stage 2: NL + FOL + Question  →  answer + explanation  (QAModel)

ĐỒNG BỘ 1:1 với prompt đã dùng khi TRAIN:
  - SYSTEM_PROMPT_FOL  == src/data/prompts.py::SYSTEM_PROMPT_FOL_SFT
  - SYSTEM_PROMPT_QA   == src/models/QA_model/prepare_data.py::SYSTEM_PROMPT_QA_COT
Prompt inference PHẢI khớp prompt train, nếu lệch model sẽ trả lời kém.
Để chỉnh prompt, chỉ cần sửa file này — không động vào pipeline/.
"""

# ══════════════════════════════════════════════════════════════════════════════
# STAGE 1 — FOL Model:  NL premises → {"premises_fol": ["...", ...]}
# ══════════════════════════════════════════════════════════════════════════════

SYSTEM_PROMPT_FOL = """\
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

USER_TEMPLATE_FOL = """\
### Input
{premises_nl}

### Output
"""


# ══════════════════════════════════════════════════════════════════════════════
# STAGE 2 — QA Model:  NL + FOL + Options + Question → reasoning steps + JSON
#
# ĐỒNG BỘ 1:1 với src/models/QA_model/prepare_data.py::SYSTEM_PROMPT_QA_COT
# (bản QA v3: reasoning steps Rule:/Fact:/Derive:/Conclusion: rồi JSON cuối,
#  "answer" ĐỨNG CUỐI, MCQ trả VERBATIM option text, nhãn yes/no "Uncertain").
# Sửa prompt train thì copy lại vào đây — KHÔNG import chéo để package tự chứa.
# ══════════════════════════════════════════════════════════════════════════════

SYSTEM_PROMPT_QA = """\
### Role
You are a logic-based educational QA system. You are given natural-language premises (indexed from 0), their First-Order Logic (FOL) translations, the answer options, and a question.

### How to read options (follow this convention ABSOLUTELY)
- If options is non-empty, it is a choice question. Your answer must be exactly one of the listed options (copy the full option text verbatim — NOT the letter).
- If options is empty ([]), the answer is free-form (a number or a short text). Return the value directly in answer.
For a yes/no question the options are ["Yes", "No", "Uncertain"]; choose "Uncertain" only when the premises are genuinely insufficient.

### Output
First, reason in ordered steps, working over the First-Order Logic (FOL) premises — reason on the FOL formulas, not the natural-language text. Each step starts with exactly one prefix:
- Rule:        a conditional/quantified FOL formula taken from a given FOL premise.
- Fact:        a ground FOL fact taken from a given FOL premise.
- Derive:      an intermediate FOL inference (contrapositive, modus ponens, a numeric comparison, or combining earlier steps).
- Conclusion:  the final result — exactly one, as the last step.
Write every Rule:/Fact:/Derive: step in FOL notation (∀ ∃ → ¬ ∧ ∨ ↔ < > =). Every Rule:/Fact: must be taken from the given FOL premises only — never invent one. The "premises_used" list must contain exactly the 0-based indices of the FOL premises you cited in your Rule:/Fact: steps.
Then, on the final line, output ONE JSON object with the "answer" field LAST:
{"premises_used": [<0-based indices of premises used>], "explanation": "<concise justification>", "answer": "<answer>"}
The "answer" MUST follow the "How to read options" convention above.

### Handling premises that state information is absent/unknown
Some FOL lines are NOT formulas but a marker such as
"(no FOL — premise only states that information is absent/unknown)".
Such a line is still a REAL premise and you MUST treat it as citable:
- Treat the corresponding fact as UNDETERMINED — do NOT derive a negation from it.
- If your conclusion relies on this absence of information, write a Fact: step that
  references it in words, e.g. "Fact: premise i states whether <X> is unknown",
  and INCLUDE that premise's 0-based index in "premises_used" (this is the one
  allowed exception to the "FOL-notation only" rule above).
- The answer is "Uncertain" unless OTHER premises decide the question.
"""

USER_TEMPLATE_QA = """\
Premises (NL):
{premises_nl_block}

Premises (FOL):
{premises_fol_block}

Options:
{options_block}

Question:
{question}
"""


# ══════════════════════════════════════════════════════════════════════════════
# Helpers — format text blocks
#   - FOL stage (Stage 1): 1-indexed (khớp SYSTEM_PROMPT_FOL few-shot khi train)
#   - QA  stage (Stage 2): 0-indexed (khớp premises_used 0-based khi train QA v3)
# ══════════════════════════════════════════════════════════════════════════════

def format_nl_block(premises: list[str]) -> str:
    """FOL stage — ['P1', 'P2'] → '1. P1\\n2. P2' (1-indexed, đúng prompt FOL train)."""
    if not premises:
        return "(none)"
    return "\n".join(f"{i}. {p}" for i, p in enumerate(premises, 1))


def format_premises_nl(premises: list[str]) -> str:
    """QA stage — 0-indexed, khớp premises_used (0-based) để model không lệch chỉ số."""
    return "\n".join(f"{i}. {p}" for i, p in enumerate(premises))


def format_premises_fol(premises: list[str]) -> str:
    """QA stage — 0-indexed, khớp premises_used (0-based)."""
    return "\n".join(f"{i}. {p}" for i, p in enumerate(premises))


_OPT_LETTERS = "ABCDEFGHIJ"


def format_options(options: list[str]) -> str:
    """Hiển thị options có letter (A./B./...) cho model dễ tham chiếu trong reasoning.
    options RỖNG → ghi rõ free-form (đúng quy ước BTC: answer là number/text)."""
    if not options:
        return "(empty — choice set is empty; the answer is free-form: a number or a short text)"
    return "\n".join(f"{_OPT_LETTERS[i]}. {o}" for i, o in enumerate(options))
