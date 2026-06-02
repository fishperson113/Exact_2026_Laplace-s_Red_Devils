# FOL Model — NL to First-Order Logic

## 1. Overview

FOL Model (Model 1) fine-tune Qwen2.5-3B-Instruct voi LoRA de dich premises ngon ngu tu nhien (NL) sang First-Order Logic (FOL).

**Input**:
```
1. If a student passes the exam, they graduate.
2. John passed the exam.
```

**Output**:
```json
{"premises_fol": [
  "∀x (PassesExam(x) → Graduates(x))",
  "PassesExam(John)"
]}
```

---

## 2. Training Pipeline

```
data/processed/train.csv
      │
      ▼
┌──────────────┐
│ Qwen 3B      │  Hoc: NL → JSON {"premises_fol": [...]}
│ + LoRA       │
└──────┬───────┘
       │
  Moi epoch
       │
       ▼
┌──────────────────────────────────────┐
│  FolDevRMForBestModelCallback        │
│                                       │
│  1. Model greedy generate tren dev    │
│  2. Parse JSON → gold_list, pred_list │
│  3. Tinh FOL BLEU (fol_bleu.py)      │
│  4. Tinh LE (fol_le.py)              │
│  5. RM = 0.7 x LE + 0.3 x BLEU      │
│  6. Ghi eval_rm_score vao metrics    │
└──────────────────────────────────────┘
       │
       ▼
Trainer chon checkpoint co eval_rm_score cao nhat
Early stopping: 5 epoch khong cai thien → dung
```

### Hyperparameters

| Param | Gia tri | Ly do |
|---|---|---|
| `lora_r` | 16 | LogicLLaMA paper |
| `lora_alpha` | 32 | Ratio alpha/r = 2 |
| `lora_dropout` | 0.05 | 0.2 qua cao, overly regularized |
| `learning_rate` | 2e-4 | LogicLLaMA dung 3e-4, 2e-4 an toan |
| `num_train_epochs` | 15 | Co early stopping patience=5 |
| `metric_for_best_model` | eval_rm_score | RM cong bang hon exact match |

---

## 3. Best Model Selection — Metric RM

### 3.1 Tai sao khong dung Exact Match?

```
Gold:      ∀x (A(x) → B(x))
Predicted: ∀x (¬B(x) → ¬A(x))

Exact match: 0   ← SAI — hai formula TUONG DUONG LOGIC
RM:          cao  ← DUNG — LE nhan ra tuong duong, BLEU ghi nhan overlap
```

### 3.2 Cong thuc RM

Theo LogicLLaMA (Doan et al.):

```
RM = 0.7 x LE + 0.3 x FOL_BLEU
```

| Thanh phan | Do cai gi | Trong so |
|---|---|---|
| **LE** (Logical Equivalence) | Hai formula co cung y nghia logic khong | 0.7 |
| **FOL BLEU** | N-gram overlap giua gold va predicted FOL strings | 0.3 |

### 3.3 FOL BLEU — Cach tinh

**Buoc 1**: Tokenize FOL string thanh tokens:

```
"∀x (A(x) → B(x))"
→ ["∀", "x", "(", "A", "(", "x", ")", "→", "B", "(", "x", ")", ")"]
```

**Buoc 2**: Tinh n-gram precision (n = 1, 2, 3, 4):

```
N-gram = nhom n token lien tiep.

1-gram: ["∀"], ["x"], ["("], ...
2-gram: ["∀","x"], ["x","("], ...
3-gram: ["∀","x","("], ...
4-gram: ["∀","x","(","A"], ...

Precision(n) = so n-gram khop / tong n-gram cua predicted
```

**Buoc 3**: BLEU-4:

```
BLEU = BP x exp(0.25 x log(P1) + 0.25 x log(P2) + 0.25 x log(P3) + 0.25 x log(P4))

BP = brevity penalty (phat khi predicted ngan hon gold)
```

**Vi du**:

| Truong hop | BLEU |
|---|---|
| Gold va Pred giong het | 1.0 |
| `A(x) → B(x)` vs `¬B(x) → ¬A(x)` | ~0.28 (tokens khac nhieu) |
| Gold va Pred hoan toan khac | 0.0 |

**Han che**: BLEU chi do text, khong hieu logic. Vi vay can LE.

### 3.4 LE (Logical Equivalence) — Cach tinh

LE do **nghia logic** giong nhau khong — bu cho han che cua BLEU.

#### Khong co Z3 (fallback)

So khop string sau khi normalize whitespace. Giong exact match — kem chinh xac:

```
"∀x (A(x) → B(x))" == "∀x (A(x) → B(x))" → LE = 1
"∀x (A(x) → B(x))" != "∀x (¬B(x) → ¬A(x))" → LE = 0  ← sai
```

#### Co Z3 (`pip install z3-solver`)

De Z3 doc duoc FOL string, can 3 buoc:

```
FOL string → [Tokenizer] → tokens → [Parser] → AST → [Translator] → Z3
```

Chi tiet xem Section 4 (FOL Parser).

Z3 kiem tra:

```python
solver.add(Not(gold_z3 == pred_z3))   # thu tim phan vi du
result = solver.check()

# unsat → KHONG co phan vi du → tuong duong → LE = 1
# sat   → CO phan vi du → khong tuong duong → LE = 0
```

### 3.5 RM tren nhieu premises

Voi 1 record co n premises:

```
Gold: [φ₁, φ₂, ..., φₙ]
Pred: [ψ₁, ψ₂, ..., ψₙ]

LE   = (1/n) x Σ LE(φᵢ, ψᵢ)      ← trung binh tung cap
BLEU = (1/n) x Σ BLEU(φᵢ, ψᵢ)    ← trung binh tung cap
RM   = 0.7 x LE + 0.3 x BLEU
```

Tren toan dataset: trung binh RM cua tat ca records.

---

## 4. FOL Parser — Chi tiet

### 4.1 AST la gi?

AST = **Abstract Syntax Tree** (Cay cu phap truu tuong).

La "cay" bieu dien **cau truc** cua mot formula — tach tung thanh phan ra thanh node cha-con, may doc duoc.

**Vi du**: `∀x (Student(x) ∧ PassedExam(x) → Graduated(x))`

```
        QuantNode(∀, x)             ← "voi moi x"
              │
        BinaryNode(→)              ← "suy ra"
         ┌────┴────┐
    BinaryNode(∧)  PredicateNode    ← "Graduated(x)"
     ┌────┴────┐     
PredicateNode  PredicateNode
Student(x)     PassedExam(x)
```

FOL string chi la text — may khong hieu. AST la so do — may doc duoc.

### 4.2 Cac loai AST Node

| Node | Y nghia | Vi du |
|---|---|---|
| `PredicateNode(name, args)` | Vi tu | `Student(x)`, `R(John)` |
| `NotNode(child)` | Phu dinh | `¬A(x)` |
| `BinaryNode(op, left, right)` | Phep noi 2 ve | `A(x) → B(x)`, `A(x) ∧ B(x)` |
| `QuantNode(quant, var, body)` | Luong tu | `∀x (...)`, `∃x (...)` |

### 4.3 Pipeline: String → AST

#### Buoc 1: Tokenizer

Tach chuoi thanh tung "manh" co nghia:

```
"∀x (Student(x) → Graduated(x))"
                    ↓
["∀", "x", "(", "Student", "(", "x", ")", "→", "Graduated", "(", "x", ")", ")"]
```

Regex:
```python
pattern = r"(∀|∃|→|↔|∧|∨|¬|[(),]|[A-Za-z_][A-Za-z0-9_]*)"
```

Moi loai token:

| Token | Loai |
|---|---|
| `∀` `∃` | Quantifier (luong tu) |
| `→` `∧` `∨` `¬` `↔` | Connective (phep noi) |
| `Student` `Graduated` | Predicate (vi tu) — chu hoa dau |
| `x` `y` `z` | Variable (bien) — chu thuong 1 ky tu |
| `John` | Constant (hang) — ten rieng |
| `(` `)` `,` | Dau cau |

#### Buoc 2: Parser (Recursive Descent)

Parser doc tokens **tu trai sang phai**, goi cac ham de quy theo thu tu uu tien:

```
_parse_formula()          ← bat dau: kiem tra ∀/∃ truoc
  │
  ├→ _parse_quantified()  ← doc ∀x rồi doc body (de quy)
  │
  └→ _parse_implication() ← doc ve trai, neu thay → thi doc ve phai
       │
       └→ _parse_disjunction() ← doc ∨ (or)
            │
            └→ _parse_conjunction() ← doc ∧ (and)
                 │
                 └→ _parse_unary() ← doc ¬ (not)
                      │
                      └→ _parse_atom() ← doc Predicate(args) hoac (formula)
```

**Thu tu uu tien** (thap → cao):

```
→ / ↔     (yeu nhat — xu ly truoc)
∨
∧
¬
Predicate / ()  (manh nhat — xu ly sau cung)
```

Giong toan: `+` yeu hon `×`, nen `×` duoc gom truoc.

**Trace vi du**: `∀x (A(x) → B(x))`

```
Tokens: [∀, x, (, A, (, x, ), →, B, (, x, ), )]

1. _parse_formula(): thay "∀" → goi _parse_quantified()
2. _parse_quantified(): doc "∀", doc "x", goi _parse_formula() cho body
3. _parse_formula(): thay "(", khong phai ∀/∃ → goi _parse_implication()
4. _parse_implication() → _parse_disjunction() → ... → _parse_atom()
5. _parse_atom(): thay "(" → doc ( formula )
6.   Ben trong: _parse_formula() → _parse_implication()
7.     _parse_disjunction() → ... → _parse_atom(): doc "A(x)" → PredicateNode
8.     Thay "→" → doc ve phai: _parse_formula()
9.     _parse_atom(): doc "B(x)" → PredicateNode
10.    Tra ve: BinaryNode(→, A(x), B(x))
11. Doc ")" → dong nhom ngoac
12. Tra ve: QuantNode(∀, x, BinaryNode(→, A(x), B(x)))
```

### 4.4 AST → Z3

Duyet cay AST, chuyen tung node:

```
QuantNode(∀, x, body)      → z3.ForAll(x, ...)
QuantNode(∃, x, body)      → z3.Exists(x, ...)
BinaryNode(→, left, right)  → z3.Implies(left, right)
BinaryNode(∧, left, right)  → z3.And(left, right)
BinaryNode(∨, left, right)  → z3.Or(left, right)
BinaryNode(↔, left, right)  → z3.Eq(left, right)
NotNode(child)               → z3.Not(child)
PredicateNode(name, args)    → z3.Function(name)(args...)
```

---

## 5. File Structure

```
src/models/fol_model/
├── README.md                  ← file nay
├── train.py                   ← Training loop + FolDevRMForBestModelCallback
├── generation_fol_eval.py     ← fol_rm_score() — generate + tinh RM
├── unsloth_sft.py             ← Unsloth model loading (VRAM optimization)
├── experiment_log.py          ← Ghi log experiment
├── fol_preflight.py           ← Baseline truoc fine-tune
├── hub_reload_eval.py         ← Eval sau khi push Hub
├── tokenizer_fix.py           ← Fix EOS/PAD token

src/evaluation/
├── fol_parser.py              ← Tokenizer + Recursive Descent Parser → AST
├── fol_z3_translator.py       ← AST → Z3 expression (can pip install z3-solver)
├── fol_bleu.py                ← FOL BLEU score
├── fol_le.py                  ← Logical Equivalence (Z3 hoac fallback string match)
├── fol_rm.py                  ← RM = 0.7 x LE + 0.3 x BLEU

configs/
└── fol_model.yaml             ← Hyperparameters + metric_for_best_model: eval_rm_score

src/services/
└── config_fol.py              ← FolSFTConfig (rm_le_weight, rm_bleu_weight, ...)
```

---

## 6. Code Flow — Moi Epoch

```
train.py :: trainer.train()
  │
  ├→ Forward + backward (SFT loss tren train set)
  │
  └→ on_evaluate() [FolDevRMForBestModelCallback]
       │
       └→ fol_rm_score(cfg, model, tokenizer, dev_dataset, max_samples=30)
            │
            ├→ model.generate() tren 30 mau dev (greedy, batch)
            │
            ├→ _parse_premises_fol_list(gold_text) → gold_list: list[str]
            ├→ _parse_premises_fol_list(pred_text) → pred_list: list[str]
            │
            ├→ fol_bleu_record(gold_list, pred_list) → bleu: float
            │    └→ fol_bleu_single() cho tung cap premise
            │         └→ tokenize_fol_for_bleu() → tokens
            │         └→ _manual_bleu4() hoac nltk sentence_bleu()
            │
            ├→ le_record(gold_list, pred_list) → le: float
            │    └→ le_single_from_strings() cho tung cap
            │         ├→ [co z3] fol_string_to_z3() → Z3 expr
            │         │    └→ parse_fol() → AST → ast_to_z3() → Z3
            │         │    └→ le_single_z3(gold_z3, pred_z3)
            │         └→ [ko z3] string match (normalized)
            │
            └→ RM = 0.7 * le + 0.3 * bleu
            └→ metrics["eval_rm_score"] = RM

  Trainer: so sanh eval_rm_score voi best → luu checkpoint neu cao hon
  EarlyStoppingCallback: dem patience
```

---

## 7. Dependencies

```bash
# Bat buoc
pip install transformers trl peft bitsandbytes accelerate

# Cho RM metric
pip install nltk          # FOL BLEU (co fallback neu khong cai)
pip install z3-solver     # LE chinh xac (co fallback string match neu khong cai)

# Cho Unsloth (tiet kiem VRAM)
pip install unsloth
```

---

## 8. Quick Start

### CLI

```bash
cd src/
PYTHONPATH=. python -m models.fol_model.train
```

### Notebook

```python
from services.config_fol import FolSFTConfig
from models.fol_model.train import run_training

cfg = FolSFTConfig.from_env()
result = run_training(cfg)
```

### Environment overrides

```bash
FOL_NUM_TRAIN_EPOCHS=10        # ghi de so epoch
FOL_METRIC_FOR_BEST_MODEL=eval_exact_match_rate  # quay ve exact match
FOL_BEST_MODEL_RM_MAX_SAMPLES=50                 # tang so mau dev cho RM
FOL_RM_LE_WEIGHT=0.8           # tang trong so LE
FOL_RM_BLEU_WEIGHT=0.2         # giam trong so BLEU
FOL_DEBUG_MAX_TRAIN_SAMPLES=10 # test nhanh luong
```
