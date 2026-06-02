# Design: FOL Model Selection via RM metric & Stage-2 Neuro-Symbolic Pipeline

> **Tác giả**: Team Laplace's Red Devils
> **Ngày tạo**: 2026-05-27
> **Trạng thái**: Draft — chờ review & implement

---

## 1. Overview — Tổng quan

Tài liệu này mô tả hai thay đổi chính trong pipeline:

1. **Thay đổi metric chọn best model cho FOL Model (Model 1)**: từ `exact_match_rate` sang **RM = 0.7 × LE + 0.3 × FOL BLEU** (theo LogicLLaMA).
2. **Thiết kế Stage 2**: pipeline neuro-symbolic kết hợp Model 1 (sinh FOL) + Solver (Z3) + base LLM (sinh explanation) để trả lời MCQ / Yes-No-Unknown.

```
┌──────────────────────────────────────────────────────────┐
│                    OVERALL PIPELINE                       │
│                                                           │
│  NL premises + Question                                   │
│       │                                                   │
│       ▼                                                   │
│  ┌──────────┐     ┌──────────┐     ┌──────────────────┐  │
│  │ Model 1  │────▶│  Solver  │────▶│  Base LLM        │  │
│  │ Qwen 3B  │ FOL │  (Z3)    │proof│  (Qwen 3B base)  │  │
│  │ + LoRA   │     │          │trace│  NO fine-tune     │  │
│  └──────────┘     └──────────┘     └──────────────────┘  │
│   Fine-tuned       Symbolic         Viết explanation      │
│   NL → FOL         reasoning        từ proof trace        │
│                                                           │
│  Train metric: RM = 0.7 × LE + 0.3 × FOL BLEU           │
└──────────────────────────────────────────────────────────┘
```

---

## 2. Current State — Hiện trạng

### 2.1 Model 1 (FOL) — hiện tại

| Thuộc tính | Giá trị hiện tại |
|---|---|
| Base model | `Qwen/Qwen2.5-3B-Instruct` |
| Metric chọn best model | `eval_exact_match_rate` |
| Cách tính | JSON `premises_fol` — so khớp string từng formula (whitespace-normalized) |
| File liên quan | `src/models/fol_model/generation_fol_eval.py` → `_lists_exact_match()` |

**Hạn chế của exact match**:

```
Gold:      ∀x (A(x) → B(x))
Predicted: ∀x (¬B(x) → ¬A(x))

Exact match: 0   ← SAI — vì hai formula TƯƠNG ĐƯƠNG LOGIC
```

Exact match quá khắt khe — formula đúng về logic nhưng viết khác thì bị tính sai.

### 2.2 Model 2 (Logic) — hiện tại

- Fine-tuned Qwen riêng, nhận FOL + NL + Question → sinh Answer + Explanation.
- Metric: `eval_accuracy` (so khớp answer label).
- **Vấn đề**: Model 2 phải tự "suy luận" — không đảm bảo tính đúng đắn logic.

---

## 3. New Metric: RM — Reasoning Match

### 3.1 Definition — Định nghĩa

Theo LogicLLaMA (Doan et al.):

```
RM = 0.7 × LE + 0.3 × FOL_BLEU
```

| Thành phần | Ý nghĩa | Trọng số |
|---|---|---|
| **LE** (Logical Equivalence) | Hai formula có cùng ý nghĩa logic không | 0.7 |
| **FOL BLEU** | N-gram overlap giữa gold và predicted FOL strings | 0.3 |

LE quan trọng hơn vì: viết khác không sao, miễn đúng logic.

### 3.2 FOL BLEU — Chi tiết tính toán

FOL BLEU là BLEU score tiêu chuẩn (sacrebleu / nltk), áp dụng trên FOL string đã tokenize:

**Bước 1**: Tokenize FOL string thành word-level tokens:

```python
def tokenize_fol_for_bleu(fol_str: str) -> list[str]:
    """
    '∀x (Student(x) → Graduated(x))'
    → ['∀', 'x', '(', 'Student', '(', 'x', ')', '→', 'Graduated', '(', 'x', ')', ')']
    """
    pattern = re.compile(
        r"(∀|∃|→|∧|∨|¬|↔|[(),]|[A-Za-z][A-Za-z0-9_]*)"
    )
    return pattern.findall(fol_str)
```

**Bước 2**: Tính BLEU cho từng cặp premise (gold vs predicted):

```python
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

def fol_bleu_single(gold_fol: str, pred_fol: str) -> float:
    ref_tokens = tokenize_fol_for_bleu(gold_fol)
    hyp_tokens = tokenize_fol_for_bleu(pred_fol)
    if not ref_tokens or not hyp_tokens:
        return 0.0
    smoothing = SmoothingFunction().method1
    return sentence_bleu(
        [ref_tokens], hyp_tokens,
        weights=(0.25, 0.25, 0.25, 0.25),  # BLEU-4
        smoothing_function=smoothing,
    )
```

**Bước 3**: Trung bình trên tất cả premises của 1 record:

```python
def fol_bleu_record(gold_list: list[str], pred_list: list[str]) -> float:
    n = len(gold_list)
    if n == 0:
        return 0.0
    scores = []
    for i in range(n):
        if i < len(pred_list):
            scores.append(fol_bleu_single(gold_list[i], pred_list[i]))
        else:
            scores.append(0.0)  # premise thiếu → 0
    return sum(scores) / n
```

### 3.3 LE (Logical Equivalence) — Chi tiết tính toán

#### 3.3.1 Per-premise LE (dùng Z3)

```python
from z3 import Solver, Not, unsat

def le_single_z3(gold_z3, pred_z3) -> float:
    """
    LE = 1.0 nếu gold ↔ pred là tautology (tương đương logic).
    LE = 0.0 nếu không.
    """
    s = Solver()
    s.set("timeout", 5000)  # 5s timeout
    s.add(Not(gold_z3 == pred_z3))   # tìm phản ví dụ
    result = s.check()
    if result == unsat:
        return 1.0   # không có phản ví dụ → tương đương
    else:
        return 0.0   # có phản ví dụ hoặc timeout → không tương đương
```

#### 3.3.2 Per-record LE

```python
def le_record(gold_fol_list: list[str], pred_fol_list: list[str]) -> float:
    """
    Tính LE trung bình trên từng cặp premise.
    Nếu số lượng premises không khớp → premises thiếu/thừa = 0.
    """
    n = len(gold_fol_list)
    if n == 0:
        return 0.0
    predicates_cache = {}
    scores = []
    for i in range(n):
        if i >= len(pred_fol_list):
            scores.append(0.0)
            continue
        try:
            gold_z3 = fol_string_to_z3(gold_fol_list[i], predicates_cache)
            pred_z3 = fol_string_to_z3(pred_fol_list[i], predicates_cache)
            scores.append(le_single_z3(gold_z3, pred_z3))
        except (ParseError, Z3Exception):
            scores.append(0.0)  # parse fail → 0
    return sum(scores) / n
```

#### 3.3.3 Fallback khi Z3 không parse được

Nếu FOL string quá phức tạp hoặc parser chưa hỗ trợ → fallback sang truth table sampling trên propositional fragment, hoặc LE = 0 cho cặp đó (conservative).

### 3.4 RM tổng hợp

```python
def rm_record(gold_fol_list: list[str], pred_fol_list: list[str]) -> float:
    le = le_record(gold_fol_list, pred_fol_list)
    bleu = fol_bleu_record(gold_fol_list, pred_fol_list)
    return 0.7 * le + 0.3 * bleu

def rm_dataset(records: list[dict]) -> float:
    """Trung bình RM trên toàn bộ dataset."""
    scores = []
    for rec in records:
        gold = rec["gold_premises_fol"]
        pred = rec["pred_premises_fol"]
        scores.append(rm_record(gold, pred))
    return sum(scores) / len(scores) if scores else 0.0
```

---

## 4. Best Model Selection — Chọn model tốt nhất

### 4.1 Thay đổi config

File: `configs/fol_model.yaml`

```yaml
training:
  # CŨ:
  # metric_for_best_model: eval_exact_match_rate

  # MỚI:
  metric_for_best_model: eval_rm_score
  greater_is_better: true
```

### 4.2 Thay đổi trong trainer

File mới: `src/models/fol_model/fol_rm_metric.py`

Hàm `compute_rm_on_split()` được gọi mỗi epoch trong custom trainer callback:

```python
def compute_rm_on_split(
    cfg, model, tokenizer, ds, max_samples=None
) -> dict[str, float]:
    """
    1. Greedy generate FOL cho mỗi sample.
    2. Parse gold + predicted → list[str].
    3. Tính LE (Z3) + FOL BLEU cho từng record.
    4. RM = 0.7 * LE + 0.3 * BLEU.
    """
    # ... (tương tự fol_exact_match_rate nhưng thêm LE + BLEU)
    return {
        "rm_score": rm_avg,
        "le_score": le_avg,
        "fol_bleu": bleu_avg,
        "exact_match_rate": em_rate,  # vẫn log để so sánh
    }
```

### 4.3 Early stopping

Giữ nguyên `early_stopping_patience: 5`, nhưng metric chuyển sang `eval_rm_score`:

```
Epoch 1:  eval_rm = 0.12  ← best
Epoch 2:  eval_rm = 0.25  ← best
Epoch 3:  eval_rm = 0.41  ← best
Epoch 4:  eval_rm = 0.39  patience = 1
Epoch 5:  eval_rm = 0.43  ← best (reset patience)
...
Epoch 15: eval_rm = 0.55  ← best
Epoch 16: eval_rm = 0.53  patience = 1
...
Epoch 20: eval_rm = 0.52  patience = 5 → STOP
```

### 4.4 Backward compatibility — Tương thích ngược

- Vẫn log `exact_match_rate` song song → so sánh với RM.
- Config `metric_for_best_model` cho phép chuyển về `eval_exact_match_rate` nếu cần.
- RM > exact match trong mọi trường hợp (RM ≥ exact match vì LE cho điểm cả khi viết khác nhưng đúng logic).

---

## 5. FOL Parser Module — Module parse FOL

### 5.1 Vị trí file

```
src/
├── evaluation/
│   ├── metrics.py              # hiện có: answer accuracy
│   ├── fol_parser.py           # MỚI: tokenize + parse FOL → AST
│   ├── fol_z3_translator.py    # MỚI: AST → Z3 expression
│   ├── fol_bleu.py             # MỚI: FOL BLEU score
│   └── fol_le.py               # MỚI: Logical Equivalence (Z3)
│   └── fol_rm.py               # MỚI: RM = 0.7*LE + 0.3*BLEU
```

### 5.2 Grammar hỗ trợ

FOL grammar phù hợp với dataset `Logic_Based_Educational_Queries`:

```
formula     := quantified | implication
quantified  := QUANT VAR '(' formula ')'    -- ∀x (...)
             | QUANT VAR formula             -- ∀x ... (không có ngoặc bao ngoài)
implication := disjunction ('→' disjunction | '↔' disjunction)?
disjunction := conjunction ('∨' conjunction)*
conjunction := unary ('∧' unary)*
unary       := '¬' unary | atom
atom        := PREDICATE '(' arglist ')'     -- Student(x), R(x)
             | '(' formula ')'              -- nhóm ngoặc
arglist     := term (',' term)*
term        := VAR | CONSTANT

QUANT       := '∀' | '∃'
VAR         := [a-z]                        -- biến: x, y, z
CONSTANT    := [a-z][a-z0-9_]+             -- hằng: john, mary
PREDICATE   := [A-Z][a-zA-Z0-9_]*          -- vị từ: Student, R, PassedExam
```

### 5.3 Các trường hợp đặc biệt cần xử lý

| Pattern trong dataset | Ví dụ | Xử lý |
|---|---|---|
| Predicate CamelCase dài | `ParticipatesInSocialWork(x)` | Regex `[A-Z][a-zA-Z0-9_]*` |
| Predicate 1 ký tự | `R(x)`, `Q(x)` | Cùng regex |
| Ground atom (không quantifier) | `Student(John)` | Parser: atom đứng một mình |
| Nested quantifier | `∀x ∃y Loves(x,y)` | Recursive descent tự xử lý |
| Quantifier-level implication | `(∀x(T(x)→U(x)) → ∀x(¬R(x)→¬Q(x)))` | Quantified bên trong `()` → parse_formula đệ quy |
| Predicate nhiều argument | `Teaches(x, y)` | arglist xử lý comma |

### 5.4 Error handling

```python
class FOLParseError(ValueError):
    """Không parse được FOL string."""
    pass

def safe_fol_to_z3(fol_str: str, cache: dict) -> z3.ExprRef | None:
    """Parse FOL → Z3; trả None nếu thất bại (thay vì raise)."""
    try:
        tokens = tokenize(fol_str)
        ast = FOLParser(tokens).parse_formula()
        return ast_to_z3(ast, cache, {})
    except (FOLParseError, Exception):
        return None
```

Khi LE gặp parse error → LE = 0 cho cặp đó → RM fallback dùng FOL BLEU (vẫn tính được vì BLEU chỉ cần string).

---

## 6. Stage 2 — Neuro-Symbolic Inference Pipeline

### 6.1 Architecture — Kiến trúc

```
Input: premises_nl (list[str]) + question (str)
                │
  ──────────────┼──────────────────────────────────
  STAGE 1       │        Fine-tuned
                ▼
         ┌─────────────┐
         │  Model 1     │  Qwen 3B + LoRA (FOL)
         │  NL → FOL    │  metric: RM score
         └──────┬──────┘
                │  {"premises_fol": ["∀x ...", ...]}
                ▼
  ──────────────┼──────────────────────────────────
  STAGE 2       │        No training needed
                ▼
         ┌─────────────┐
         │  FOL Parser  │  fol_parser.py
         │  str → Z3    │
         └──────┬──────┘
                │  Z3 expressions
                ▼
         ┌─────────────┐
         │  Z3 Solver   │
         │              │
         │  Với MCQ:    │  thử entail từng choice A/B/C/D
         │  Với Y/N/U:  │  thử entail conclusion + negation
         └──────┬──────┘
                │  {answer, used_premises, status}
                │
        ┌───────┴────────┐
        │                │
   solved ✓         unsolved / timeout
        │                │
        ▼                ▼
  ┌──────────┐    ┌──────────────┐
  │ Base LLM │    │ Fallback:    │
  │ Qwen 3B  │    │ Model 2 LLM  │
  │ (no LoRA)│    │ hoặc heuristic│
  │ explain  │    └──────────────┘
  └──────┬───┘
         │
         ▼
  Answer + Explanation
```

### 6.2 Solver Logic — Chi tiết giải bài

#### 6.2.1 Yes / No / Unknown

```python
def solve_yes_no(premises_z3: list, conclusion_z3) -> str:
    """
    Kiểm tra conclusion có được entail từ premises không.

    Returns: "Yes" | "No" | "Unknown"
    """
    s = Solver()
    s.set("timeout", 10000)   # 10s

    for p in premises_z3:
        s.add(p)

    # Thử chứng minh conclusion: premises ∧ ¬conclusion → unsat?
    s.push()
    s.add(Not(conclusion_z3))
    r1 = s.check()
    s.pop()

    if r1 == unsat:
        return "Yes"  # ¬conclusion mâu thuẫn → conclusion đúng

    # Thử chứng minh ¬conclusion: premises ∧ conclusion → unsat?
    s.push()
    s.add(conclusion_z3)
    r2 = s.check()
    s.pop()

    if r2 == unsat:
        return "No"   # conclusion mâu thuẫn → conclusion sai

    return "Unknown"  # cả hai đều sat → không kết luận được
```

#### 6.2.2 MCQ (A / B / C / D)

```python
def solve_mcq(premises_z3: list, choices_z3: dict[str, Any]) -> str | None:
    """
    choices_z3 = {"A": z3_expr_A, "B": z3_expr_B, ...}

    Returns: "A"/"B"/"C"/"D" hoặc None nếu không giải được.
    """
    entailed = []
    for label, choice_z3 in choices_z3.items():
        s = Solver()
        s.set("timeout", 5000)
        for p in premises_z3:
            s.add(p)
        s.add(Not(choice_z3))
        if s.check() == unsat:
            entailed.append(label)

    if len(entailed) == 1:
        return entailed[0]   # chỉ 1 choice được entail → đáp án
    elif len(entailed) > 1:
        return entailed[0]   # nhiều choice → lấy đầu tiên (hoặc log warning)
    else:
        return None           # không entail được → fallback LLM
```

#### 6.2.3 MCQ — Thách thức thực tế

Với MCQ, **answer choices cũng cần FOL hoá**. Có 2 cách:

| Cách | Mô tả | Ưu/nhược |
|---|---|---|
| Model 1 dịch luôn | Đưa answer choices vào prompt Model 1 → sinh FOL cho chúng | Cần thêm prompt, có thể sai |
| Rule-based matching | So khớp NL choice với NL premise → tìm FOL tương ứng | Nhanh nhưng không cover mọi trường hợp |

**Đề xuất**: Mở rộng prompt Model 1 để dịch cả answer choices khi câu hỏi là MCQ.

### 6.3 Explanation Generation — Sinh giải thích

#### 6.3.1 Z3 Unsat Core → Used Premises

```python
def get_proof_trace(premises_z3, conclusion_z3, premises_nl):
    """Tìm tập premises tối thiểu dùng để chứng minh."""
    s = Solver()
    s.set("unsat_core", True)

    labels = []
    for i, p in enumerate(premises_z3):
        label = Bool(f"p{i}")
        labels.append(label)
        s.assert_and_track(p, label)

    s.add(Not(conclusion_z3))
    assert s.check() == unsat

    core = s.unsat_core()  # [p0, p2, p5] — chỉ premises cần thiết
    used_indices = [int(str(lbl).replace("p", "")) for lbl in core]
    used_nl = [premises_nl[i] for i in used_indices]
    return used_indices, used_nl
```

#### 6.3.2 Base LLM viết explanation (không cần fine-tune)

```python
EXPLAIN_SYSTEM = """Bạn là giáo viên logic. Giải thích ngắn gọn chuỗi suy luận
dẫn đến kết luận, trích dẫn đúng số premise đã dùng."""

EXPLAIN_USER = """
Tiên đề được sử dụng trong chứng minh:
{used_premises_block}

Kết luận: {conclusion} — {status}

Hãy giải thích chuỗi suy luận bằng ngôn ngữ tự nhiên.
"""

def generate_explanation(
    base_model, tokenizer, used_premises_nl, conclusion, answer
):
    """Dùng base Qwen 3B (KHÔNG LoRA) để viết explanation."""
    block = "\n".join(
        f"- Premise {i+1}: {p}" for i, p in enumerate(used_premises_nl)
    )
    messages = [
        {"role": "system", "content": EXPLAIN_SYSTEM},
        {"role": "user", "content": EXPLAIN_USER.format(
            used_premises_block=block,
            conclusion=conclusion,
            status="ĐÚNG" if answer == "Yes" else "SAI" if answer == "No" else answer,
        )},
    ]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    # Greedy generate
    enc = tokenizer(prompt, return_tensors="pt", truncation=True)
    out = base_model.generate(**enc.to(device), max_new_tokens=256, do_sample=False)
    return tokenizer.decode(out[0, enc["input_ids"].shape[1]:], skip_special_tokens=True)
```

### 6.4 Fallback Strategy — Khi solver thất bại

```
Solver thất bại (timeout / parse error / unknown)
         │
         ▼
┌─────────────────────────────────────────┐
│ Fallback options (chọn 1):              │
│                                          │
│ A. Model 2 LoRA (nếu đã train)          │
│    → đưa FOL+NL+Q vào, sinh answer      │
│                                          │
│ B. Base LLM heuristic                    │
│    → đưa NL premises + question          │
│    → Qwen 3B base sinh answer            │
│    → confidence thấp hơn solver          │
│                                          │
│ C. Return "Unknown" + flag               │
│    → log cho human review                │
└─────────────────────────────────────────┘
```

### 6.5 Evaluation — Đánh giá Stage 2

| Metric | Đo cái gì | Công thức |
|---|---|---|
| **Answer Accuracy** | Tỉ lệ answer đúng | `correct / total` |
| **Solver Coverage** | Tỉ lệ bài solver giải được | `solved / total` |
| **Solver Accuracy** | Accuracy chỉ trên bài solver giải | `correct_solved / solved` |
| **Explanation ROUGE** | Chất lượng explanation vs ground truth | ROUGE-L score |

Kỳ vọng:
- Solver accuracy > LLM-only accuracy (khi FOL đúng, solver chắc chắn đúng).
- Solver coverage < 100% (một số bài quá phức tạp hoặc FOL sai).
- Overall accuracy = solver_coverage × solver_accuracy + (1 - solver_coverage) × fallback_accuracy.

---

## 7. Implementation Plan — Kế hoạch triển khai

### Phase 1: FOL Parser + Metrics (tuần 1)

```
[ ] src/evaluation/fol_parser.py       — tokenizer + recursive descent parser
[ ] src/evaluation/fol_z3_translator.py — AST → Z3 expressions
[ ] src/evaluation/fol_bleu.py         — FOL BLEU score
[ ] src/evaluation/fol_le.py           — Logical Equivalence via Z3
[ ] src/evaluation/fol_rm.py           — RM = 0.7*LE + 0.3*BLEU
[ ] tests/test_fol_parser.py           — unit tests
[ ] requirements.txt                   — thêm z3-solver, nltk (nếu chưa có)
```

### Phase 2: Tích hợp RM vào training loop (tuần 1-2)

```
[ ] src/models/fol_model/trainer_rm.py — custom callback tính RM mỗi epoch
[ ] configs/fol_model.yaml             — đổi metric_for_best_model → eval_rm_score
[ ] Chạy lại training FOL model với RM metric
[ ] So sánh: best model theo RM vs best model theo exact match
```

### Phase 3: Solver + Stage 2 Pipeline (tuần 2-3)

```
[ ] src/services/symbolic_solver.py    — Z3 solver cho Yes/No/Unknown + MCQ
[ ] src/models/pipeline.py             — nối Model 1 → Parser → Solver → Explanation
[ ] Đánh giá solver coverage + accuracy trên test set
[ ] Đánh giá explanation quality (ROUGE vs ground truth)
```

### Phase 4: Fallback + Integration (tuần 3-4)

```
[ ] Fallback logic khi solver thất bại
[ ] End-to-end evaluation trên full test set
[ ] So sánh: pipeline (Model 1 + Solver) vs (Model 1 + Model 2 LoRA)
[ ] Viết report kết quả
```

---

## 8. Dependencies — Thư viện cần thêm

```
z3-solver>=4.12       # SMT solver (pip install z3-solver)
nltk>=3.8             # BLEU score (pip install nltk)
rouge-score>=0.1      # ROUGE cho explanation eval (pip install rouge-score)
lark>=1.1             # (tuỳ chọn) parser generator thay recursive descent
```

---

## 9. Risks & Mitigations — Rủi ro & giải pháp

| Rủi ro | Mức độ | Giải pháp |
|---|---|---|
| FOL parser không cover hết grammar | Trung bình | Fallback: LE = 0 cho cặp parse-fail; cải tiến parser dần |
| Z3 timeout trên FOL phức tạp | Thấp | Timeout 5-10s; fallback FOL BLEU only |
| RM chậm hơn exact match khi eval | Trung bình | Giới hạn `best_model_rm_max_samples` (vd. 30 sample) |
| MCQ choices khó FOL hoá | Cao | Phase 1-2 tập trung Yes/No/Unknown trước; MCQ phase 3-4 |
| Base LLM explanation quality | Thấp | Đánh giá ROUGE; nếu kém → train LoRA explain |

---

## 10. Summary — Tóm tắt

1. **Metric mới (RM)**: công bằng hơn exact match — formula viết khác nhưng đúng logic vẫn được điểm cao.
2. **Stage 2 (Solver)**: đáp án có bảo đảm logic (soundness) — không phụ thuộc vào khả năng suy luận của LLM.
3. **Chỉ 1 lần fine-tune**: LoRA FOL (Model 1). Solver + base LLM không cần training.
4. **Giải thích có cơ sở**: explanation dựa trên proof trace (Z3 unsat core) — trích dẫn đúng premises.
5. **Fallback an toàn**: khi solver thất bại → LLM backup → luôn có answer.
