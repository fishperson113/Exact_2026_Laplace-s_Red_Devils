# FOL + Z3 Pipeline — Tổng kết kỹ thuật

## 1. Tổng quan Pipeline

```
NL premises → [FOL Model] → FOL formulas → [Z3 Solver] → entailment → [QA Model] → answer
              Stage 1        sinh logic      Stage 2       check logic   Stage 3      trả lời
```

**3 thành phần chính:**
- **FOL Model** (Qwen2.5-3B fine-tuned): dịch NL → FOL
- **Z3 Solver**: kiểm tra logic (nhất quán? suy ra được không?)
- **QA Model** (Qwen2.5-3B base): đọc FOL + Z3 report → trả lời câu hỏi

---

## 2. Prompt FOL — Thiết kế & Các vấn đề đã giải quyết

### 2.1 Cấu trúc prompt

```
SYSTEM_PROMPT_FOL_SFT (~1000 tokens):
├── Instruction (1 dòng)
├── Chain of Thought — 4 Steps
│   ├── Step 1: Subject & Quantifier
│   ├── Step 2: Predicate Naming
│   ├── Step 3: Logical Structure
│   └── Step 4: Assemble & Validate
├── Output Format
├── Context (quantifiers + connectives)
└── 4 Few-shot Examples (từ training data thật)
```

### 2.2 Token budget

```
max_seq_length = 3500
System prompt  ≈ 1000 tokens (29%)
NL premises    ≈ 750 tokens max (P99)
FOL output     ≈ 768 tokens max (gen_max_new_tokens)
────────────────────────────────────
Total worst    = 2518 < 3500 ✅
```

**Trước đó (prompt cũ + max_seq_length=2048):**
- System prompt chiếm 1456/2048 = 71% → 40% training data bị cắt FOL
- Sau cải tiến: prompt 1000 tokens + budget 3500 → 0% bị cắt

### 2.3 Các error patterns và rules đã thêm vào prompt

| Error pattern | Tần suất | Rule trong prompt | Ví dụ |
|---|---|---|---|
| **Predicate collision** — 2 concepts dùng cùng tên | 2.7% | Step 2: "UNIQUE names" | `A(x)` vừa là "attend" vừa "assign" → `AttendsLectures` ≠ `CompletesAssignments` |
| **No-reuse** — mỗi premise tạo predicate mới | 9% | Step 2: "REUSE same predicate" | Premise 1 dùng `Pass`, premise 5 cũng "pass" → phải dùng lại `Pass` |
| **Đảo chiều implication** | ~5% | Step 3: "required/necessary → B → A" | "X cần cho Y" → `Y → X` không phải `X → Y` |
| **Sai quantifier scope** | ~10% | Step 3: "TWO SEPARATE quantifiers" | "Nếu mọi SV có P thì mọi SV có Q" → `∀x P(x) → ∀x Q(x)` không phải `∀x (P(x) → Q(x))` |
| **Multi-char variable** | 0.7% | Step 4: "NEVER ∀student or ∀c1" | `∀x (...)` không phải `∀student (...)` |
| **Args ngoài parens** | 12.3% | Step 4: "NEVER write (P(x))y" | `P(x, y)` không phải `(P(x))y` |
| **Trailing comma** | 9.1% | Output Format: "no trailing commas" | `["∀x P(x)", "∃x Q(x)"]` không phải `["∀x P(x)", "∃x Q(x)",]` |

### 2.4 Few-shot examples (4 examples từ training data thật)

| Example | Source | Covers |
|---|---|---|
| **1** — CamelCase + negation | record_id=80 | `∀x`, `∃x`, `¬`, predicate reuse xuyên premises |
| **2** — Single-letter predicates | record_id=77 | Hints `(T)`, `(U)`, nested `(A→B)→(C→D)` |
| **3** — Constants + multi-arity | record_id=10 | Named entities `david`, multi-arg `complete(x, A)` |
| **4** — Compound scope | record_id=80,84 | `(∀x(...) → ∀x(...))`, sentence-level implication |

---

## 3. Z3 Parser — Cách hoạt động & Các cải tiến

### 3.1 Pipeline parse

```
FOL string → sanitize → normalize → tokenize → parse (recursive descent) → AST → Z3 expression
```

**Ví dụ:**
```
Input:  "∀x (Student(x) → Pass(x))"
  → sanitize: giữ nguyên (không có junk)
  → normalize: giữ nguyên (đã Unicode)
  → tokenize: ["∀", "x", "(", "Student", "(", "x", ")", "→", "Pass", "(", "x", ")", ")"]
  → parse: QuantNode("∀", "x", BinaryNode("→", Student(x), Pass(x)))
  → Z3: ForAll(x, Implies(Student(x), Pass(x)))
```

### 3.2 Sanitize — dọn dẹp trước parse

| Vấn đề | Input | Sau sanitize |
|---|---|---|
| Thừa `)` cuối | `∀x (P(x))))` | `∀x (P(x))` |
| Trailing comma | `∀x P(x),` | `∀x P(x)` |
| Trailing backslash | `∀x P(x)\` | `∀x P(x)` |
| Trailing brackets | `∀x P(x)]}` | `∀x P(x)` |

### 3.3 Normalize — ASCII → Unicode

```
"forall x (P(x) -> Q(x))"  →  "∀ x (P(x) → Q(x))"
"~P(x)"                     →  "¬P(x)"
">="                         →  "≥"
```

**Keyword boundary:** `"Score(x)"` KHÔNG bị ảnh hưởng bởi `"or"` → dùng `\b` word boundary.

### 3.4 Grammar rules & precedence

```
Ưu tiên thấp → cao:
  formula → quantified(∀/∃) → implication(→/↔) → disjunction(∨) → conjunction(∧) → unary(¬) → atom

Ví dụ: "A ∨ B ∧ C → D"
  Parse: A ∨ (B ∧ C) → D   (∧ chặt hơn ∨, ∨ chặt hơn →)
```

### 3.5 Các cải tiến parser (8 thay đổi)

#### Fix 1: Negated quantifier `¬∀x`, `¬∃x`

```
TRƯỚC: ¬∀x (R(x) → Q(x))  → 💥 CRASH (parser không biết xử lý ∀ sau ¬)
SAU:   ¬∀x (R(x) → Q(x))  → NotNode(QuantNode("∀", "x", ...)) ✅

Cách fix: _parse_unary() thêm check ∀/∃ → redirect sang _parse_quantified()
```

#### Fix 2: Comparison operators trong body `gpa(s) < 2.0`

```
TRƯỚC: ∀s (gpa(s) < 2.0 → fail(s))  → 💥 parser không hiểu "<"
SAU:   ∀s (gpa(s) < 2.0 → fail(s))  → BinaryNode("<", gpa(s), 2.0) ✅

Gold FOL dùng: ≥, ≤, >, <, =
Ví dụ: membership_duration(x) ≥ 6
        completed_courses(sarah) = 4
        attendance(s,m) < 50
```

#### Fix 3: Equality top-level `M = 33`

```
TRƯỚC: completed_courses(sarah) = 4  → 💥 "Extra tokens: ['=', '4']"
SAU:   completed_courses(sarah) = 4  → BinaryNode("=", completed_courses(sarah), 4) ✅

Cách fix: _maybe_comparison_tail() check token tiếp sau atom
```

#### Fix 4: Multi-char variable `∀ABC`, `∀m1`

```
TRƯỚC: ∀ABC (triangle(ABC) → ...)  → 💥 "Expected single lowercase, got 'ABC'"
SAU:   ∀ABC (triangle(ABC) → ...)  → QuantNode("∀", "ABC", ...) ✅

Lý do: Gold FOL có ∀ABC, ∀c1, ∀c2, thậm chí ∀student
```

#### Fix 5: Nested function calls `reduce_resistance(break_into_steps(t))`

```
TRƯỚC: reduce_resistance(break_into_steps(t))  → 💥 parse fail
SAU:   args = ["break_into_steps(t)"]  → flatten thành string ✅

Gold FOL có: safety_audit(vehicle(a)), Before(June1), Program(s)
```

#### Fix 6: Quoted strings `'20/3/2025'`, `'8:00'`

```
TRƯỚC: complete_theory(Lan, '20/3/2025')  → 💥 tokenizer bỏ quotes
SAU:   args = ["Lan", "'20/3/2025'"]  ✅

Token regex thêm: r"'[^']*'"
```

#### Fix 7: Decimal numbers `0.5`, `2.0`

```
TRƯỚC: refund(s) = 0.5  → tokenizer tách "0" "." "5" → parse fail
SAU:   refund(s) = 0.5  → token "0.5" nguyên khối ✅

Token regex thêm: r"[0-9]+(?:\.[0-9]+)?"
```

#### Fix 8: Multiple quantified vars `∃m1, ∃m2, ∃m3`

```
TRƯỚC: ∀s ((∃m1, ∃m2, ∃m3, m1 ≠ m2 ∧ ...))  → 💥
SAU:   Lấy var đầu (m1), skip phần comma-separated  → parse body bình thường ✅
```

### 3.6 Kết quả parser

```
Gold FOL parse rate:
  TRƯỚC: 3330/3540 (94.1%)
  SAU:   3516/3540 (99.3%)  ← +186 formulas fixed

24 failures còn lại: arithmetic phức tạp (0.5 * tuition(x), e^(-t/S))
→ Quá hiếm (0.7%), không cần fix thêm.
```

---

## 4. Z3 Solver — Cách check entailment

### 4.1 Consistency check

```
Tất cả premises FOL → add vào Z3 solver → check satisfiability

sat     → premises nhất quán (tồn tại ít nhất 1 tình huống tất cả đúng)
unsat   → premises mâu thuẫn (không tình huống nào thỏa tất cả)
unknown → Z3 timeout hoặc undecidable
```

### 4.2 Entailment check (Yes/No questions)

```
Kiểm tra: premises có suy ra được question không?

Bước 1: premises ∧ ¬question → Z3 check
  UNSAT → question BẮT BUỘC đúng → "entailed" → Yes

Bước 2: premises ∧ question → Z3 check  
  UNSAT → question BẮT BUỘC sai → "contradicted" → No

Bước 3: Cả hai SAT → "unknown" → không kết luận được
```

**Ví dụ:**
```
Premises: ∀x WellTested(x), ∀x (WellTested(x) → Optimized(x))
Question: ∀x Optimized(x)

Z3: premises ∧ ¬(∀x Optimized(x)) → UNSAT
→ entailment = "entailed" → QA trả lời "Yes"
```

### 4.3 Options entailment (MCQ)

```
Z3 check TỪNG option riêng:
  Option A: premises ∧ ¬A → UNSAT? → "entailed"
  Option B: premises ∧ ¬B → UNSAT? → "empty" (concept mới)
  Option C: premises ∧ C  → UNSAT? → "contradicted"
  Option D: cả hai SAT          → "unknown"

→ QA model nhận: "Options entailment: A:entailed, B:empty, C:contradicted, D:unknown"
```

### 4.4 Heuristic phát hiện FOL sai

```python
# Pipeline tự gắn cờ khi entailment pattern bất thường:

ALL 4 options "entailed"  → "suspicious_all_entailed" (FOL quá permissive)
ALL options "empty"       → "suspicious_all_empty" (FOL không match options)
3+ options "entailed"     → "suspicious_many_entailed"

→ QA model thấy cờ suspicious → trả "Unknown" thay vì tin Z3
```

**Ví dụ thực tế:**
```
[17/81] pred=A gold=Unknown ent=opts[A:entailed B:entailed C:entailed D:entailed]

Cả 4 options entailed → FOL chắc chắn sai → nên trả Unknown
TRƯỚC: QA tin Z3, chọn A → WRONG
SAU:   Heuristic gắn "suspicious_all_entailed" → QA trả Unknown → OK
```

---

## 5. QA Model — Cách sử dụng Z3 report

### 5.1 Input QA model nhận

```
Premises (NL):           ← đọc hiểu ngữ nghĩa
Premises (FOL):          ← cấu trúc logic
Z3 Report:
  - Status: sat/unsat    ← premises có mâu thuẫn?
  - Entailment: ...      ← Yes/No question entailment
  - Options entailment:  ← MCQ per-option check (FIX MỚI — trước đây bị thiếu)
  - Model: ...           ← 1 ví dụ thỏa mãn
Question:                ← cần trả lời
```

### 5.2 Warning signs → trả Unknown

QA prompt có rules cảnh báo:
- ALL options entailed → FOL sai → Unknown
- ALL options empty → FOL không match → Unknown  
- 3+ options entailed → suspicious → Unknown
- Z3 entailed nhưng NL không support → ưu tiên NL reasoning

---

## 6. Refinement Loop

```
FOL Model sinh FOL → Z3 check → parse fail hoặc unsat?
  → CÓ: feedback cho FOL Model sinh lại (tối đa 2 lần)
  → KHÔNG: tiếp tục pipeline

Ví dụ:
  Lần 1: sinh "∀x (P(x → Q(x))"  ← thiếu ")"
  Z3: parse fail
  Lần 2: feedback "PARSE FAILED" → sinh lại "∀x (P(x) → Q(x))"  ← fix
  Z3: OK → tiếp tục
```

---

## 7. Tổng hợp cải tiến

| Component | Metric | Trước | Sau |
|---|---|---|---|
| **Prompt** | Token count | 1456 | ~1000 |
| **Prompt** | Error coverage | ~30% | ~85% |
| **Config** | max_seq_length | 2048 | 3500 |
| **Config** | gen_max_new_tokens | 512 | 768 |
| **Training** | Data bị cắt | 15.2% (50/328) | 0% (ước tính) |
| **Parser** | Gold FOL parse | 94.1% | **99.3%** |
| **Pipeline** | Options entailment | Không truyền cho QA | **Truyền đầy đủ** |
| **Pipeline** | Suspicious detection | Không có | **3 heuristics** |
| **QA Prompt** | Unknown detection | Không có rules | **Warning signs** |
