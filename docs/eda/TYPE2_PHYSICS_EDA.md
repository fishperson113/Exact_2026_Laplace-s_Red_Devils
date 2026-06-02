# EDA Report — Physics Problems (Dataset 2026-05-15)

> **Dataset:** `EXACT_Materials/Datasets/EXACT2026_dataset_2026-05-15/Physics_Problems_Text_Only.csv`
> **Ngay phan tich:** 2026-05-17
> **Rows:** 1,352 | **Columns:** `id`, `question`, `cot`, `answer`, `unit`

---

## 1. Tong quan

| Metric | Value |
|---|---|
| Total rows | 1,352 |
| Null values | `unit`: 14 null, con lai: 0 |
| Empty strings | 0 |
| Duplicate questions | 4 rows (2 cau hoi trung) |
| Unique domains (prefix) | 8 |

---

## 2. Phan phoi theo Domain (ID Prefix)

```
PREFIX   COUNT    %      MO TA (suy tu noi dung)
------   -----   -----  -------------------------
LD       397     29.4%  Luc dien / Tinh dien (Coulomb forces, electric fields)
CH       290     21.4%  Mach dien / Dien dung (RLC circuits, resonance)
NL       190     14.1%  Nang luong (Energy in capacitors/inductors, LC oscillations)
TD       177     13.1%  Tu dien (Capacitor calculations: charge, energy, capacitance)
DDT      130      9.6%  Dien & Dien truong (Solenoids, EMF, inductance)
THCB      80      5.9%  Tong hop co ban (Basic circuits, measurement errors)
DT        68      5.0%  Dien truong (Electric field strength, potential)
CHLT      20      1.5%  Chat luong thong tin (Yes/No resonance questions) ← IT NHAT
```

### Mat can bang du lieu

- **LD chiem gan 30%** trong khi **CHLT chi co 20 mau (1.5%)**
- CHLT va DT can data augmentation de model khong bi bias

---

## 3. Phan loai Answer — INSIGHT QUAN TRONG

Dataset KHONG chi co dap an so. Co **6 loai answer khac nhau**:

| Loai Answer | So luong | % | Vi du |
|---|---|---|---|
| **Pure numeric** | 973 | 72.0% | `5.07`, `300`, `0.072` |
| **Scientific notation** | 237 | 17.5% | `24.45 × 10^-3`, `5.162 × 10⁶` |
| **Text-only** | 50 | 3.7% | `Doubled`, `maximum`, `Conservation of energy` |
| **Mixed text+number** | 37 | 2.7% | `Rtd = 20.0`, `I_total = 1.5`, `W_C = W₀sin²(ωt)` |
| **Multi-value** (;) | 25 | 1.9% | `0.6; 1.2`, `36;12`, `I₁ = 0.5; I₂ = 1.0` |
| **Yes/No** | 21 | 1.6% | `Yes`, `No` |
| **Contains sqrt** | 6 | 0.4% | `9\sqrt{3} × 10^-27`, `\sqrt{2} × F₀` |
| **Other** | 3 | 0.2% | `10/3`, `100π` |

### Answer type phan bo theo domain:

```
PREFIX   pure_numeric  scientific  text_only  mixed  multi_val  yes_no  sqrt
------   -----------  ----------  ---------  -----  ---------  ------  ----
CH       289           0           0          1      0          0       0
CHLT       0           0           0          0      0         20       0    ← 100% Yes/No
DDT       78          21          24          6      0          1       0    ← Da dang nhat
DT        39          23           0          3      0          0       3
LD       201         191           0          2      0          0       3    ← 48% scientific
NL       160           0          19         10      0          0       0    ← 10% text
TD       167           2           3          1      2          0       0
THCB      39           0           4         14     23          0       0    ← 29% multi-value
```

### Nhan xet chinh:

1. **CHLT la hoan toan Yes/No** — can classifier rieng, khong can tinh toan
2. **LD co 48% answer la scientific notation** — se normalize ve numeric trong preprocessing
3. **THCB co 29% multi-value answers** (vd: `0.6; 1.2` voi unit `cm; %`) — can xu ly dac biet
4. **DDT va NL co answer dang text** (vd: `Doubled`, `Conservation of energy`) — can generate text, khong phai so
5. **Scientific notation co 2 format KHAC NHAU**: caret `10^-3` (206 rows) vs superscript `10⁻³` (37 rows) — se normalize tat ca ve float trong preprocessing

---

## 4. Phan tich Unit

### 4.1 Phan phoi unit (55 unique units!)

**Top 15:**
```
UNIT      COUNT    DOMAIN CHINH
----      -----    -------------
N          248     LD (luc Coulomb)
V/m        171     LD, DT (dien truong)
- (dash)    84     CHLT, CH (unitless, Yes/No)
V           76     CH, DDT, TD (dien ap)
J           70     NL, DDT (nang luong)
Ω           68     CH (dien tro)
A           63     CH, THCB (dong dien)
W           61     CH, DDT (cong suat)
— (em-dash) 42     DDT, NL, TD, THCB (unitless)
μF          41     CH, NL (dien dung — U+03BC)
nC          40     TD (dien tich nano)
pF          40     TD (dien dung pico)
%           39     THCB (sai so)
mJ          37     NL, DDT (nang luong milli)
nJ          35     TD (nang luong nano)
```

### 4.2 Van de Unit

**a) Dash inconsistency: `-` vs `—` (em-dash)**

```
PREFIX   - (U+002D)   — (U+2014)
------   ----------   ----------
CH       41            0
CHLT     20            0
DDT       0           27
LD        4            0
NL       19            7
TD        0            4
THCB      0            4
```

→ **Can normalize thanh 1 ky tu duy nhat** (vd: `"-"` hoac `"unitless"`)

**b) mu/micro inconsistency: `μ` (U+03BC) vs `µ` (U+00B5)**

| Variant | Count |
|---|---|
| μF (Greek mu, U+03BC) | 41 |
| µF (Micro sign, U+00B5) | 14 |

→ **2 ky tu KHAC NHAU** nhung nhin giong het. Can normalize.

**c) 14 rows co unit = NaN:**

```
ID       Answer                         Prefix  Van de
TD013    5.28                           TD      Thieu unit (co le la nC hoac pF?)
DT047    formula                        DT      Answer la cong thuc, ko co unit
TD369    Do not change                  TD      Answer la text
TD373    50%                            TD      Unit nen la %
TD377    the voltage is halfed          TD      Answer la text
TD380    decreases by 4 times           TD      Answer la text
TD386    decreases by half              TD      Answer la text
DDT327   0.60                           DDT     Thieu unit
DDT337   0.60                           DDT     Thieu unit
DDT343   0.40                           DDT     Thieu unit
CH371    1.12                           CH      Thieu unit
CH372    1.00                           CH      Thieu unit
CH373    1.77                           CH      Thieu unit
CH374    2.11                           CH      Thieu unit
```

**d) Vietnamese con sot lai trong unit:** `lần` (2 rows: TD367, NL127)

**e) Multi-unit format:** `cm; %`, `A; A; A`, `μC; μJ` — 25 rows (THCB chu yeu)

---

## 5. Phan tich Question & CoT

### 5.1 Do dai Question

| Metric | Characters | Words | Est. Tokens |
|---|---|---|---|
| Min | 31 | 6 | ~8 |
| Mean | 172 | 34 | ~43 |
| Median | 155 | 30 | ~39 |
| P95 | — | — | ~76 |
| Max | 493 | 96 | ~123 |

### 5.2 Do dai CoT

| Metric | Characters | Steps | Est. Tokens |
|---|---|---|---|
| Min | 92 | 2 | ~23 |
| Mean | 581 | 4.9 | ~145 |
| Median | 481 | 4 | ~120 |
| P95 | — | — | ~296 |
| Max | 1,747 | 13 | ~437 |

**P95 tong (Q + CoT) ~ 350 tokens** — thoai mai trong context window.

### 5.3 Do kho uoc tinh theo domain (CoT steps)

```
PREFIX   Steps (mean)   Steps (mode)   Range        Nhan xet
------   -----------    -----------    -----        --------
CHLT     8.8            9              6-11         Kho nhat (nhieu buoc suy luan logic)
DDT      6.8            6              3-13         Kho, da dang
DT       5.2            5              4-8          Trung binh
LD       5.2            5              4-10         Trung binh, nhung nhieu bai
NL       4.8            4              2-11         Trung binh, bien dong lon
CH       4.3            4              3-8          De-trung binh
TD       4.1            4              3-7          De
THCB     4.0            4              2-8          De nhat
```

### 5.4 Question length theo domain

```
PREFIX   Q Words (mean)   Nhan xet
------   ---------------  --------
DT       52               Cau hoi dai nhat (mo ta setup phuc tap)
LD       48               Cau hoi dai (nhieu charge, vi tri)
CH       31               Trung binh
TD       31               Trung binh
CHLT     25               Ngan
NL       24               Ngan
DDT      22               Ngan
THCB     20               Ngan nhat
```

---

## 6. Phan tich Answer so hoc (chi 973 pure numeric)

### 6.1 Thong ke co ban

| Metric | Value |
|---|---|
| Min | -1.77 |
| 25th percentile | 1.20 |
| Median | 10.0 |
| Mean | 14,941 |
| 75th percentile | 86.6 |
| Max | 6,300,000 |
| Std | 243,887 |

### 6.2 Phan bo do lon

```
Range           Count
-1K to -1           1
-1 to 0            18
0 to 1             215    ← ~22%, rat nhieu so nho
1 to 1K            700    ← ~72%, da so
1K to 1M            36
1M to 1B             3
```

### 6.3 Theo domain

```
PREFIX   n     Min      Median    Mean        Max         Nhan xet
------   ---   ------   ------    --------    ---------   --------
CH       289   0.04     53.1      115.6       1,600       Tap trung 1-1000
DDT       78   0        16.0      317.1       4,000       Bien dong lon
DT        39   0        245.9     355,000     6,300,000   Co outlier cuc lon!
LD       201   0        7.8       3,014       432,000     Nhieu so nho (<10)
NL       160   0        0.9       86.7        1,800       Rat nhieu so <1
TD       167   -1.77    20.3      78.5        1,200       Tap trung
THCB      39   0.1      0.83      1.43        10          Tat ca so nho
```

### 6.4 Answer am (chi 1)

- **TD391:** answer = -1.77, unit = μJ

---

## 7. Van de can xu ly truoc khi Fine-tune

### 7.1 Muc do uu tien CAO (Anh huong truc tiep den Correctness)

| # | Van de | So luong | Giai phap |
|---|---|---|---|
| 1 | **Scientific notation khong nhat quan** (`10^-3` vs `10⁻³` vs `× 10` vs `x 10`) | 237 | Normalize tat ca ve dang so thuan (float) trong preprocessing — merge vao Numeric |
| 2 | **Answer khong phai so** (text, formula, Yes/No, multi-value) | 142 (10.5%) | Classifier phan loai truoc → routing strategy khac nhau |
| 3 | **14 rows thieu unit** | 14 | Dien unit thu cong hoac suy tu context |
| 4 | **Multi-value answers** (`0.6; 1.2`) | 25 | Output parser phai handle format `value1; value2` |
| 5 | **CoT co the sai** (da biet tu CHANGELOG) | Unknown | Cross-check toan bo bang LLM thuong mai + SymPy |

### 7.2 Muc do uu tien TRUNG BINH (Anh huong den chat luong training)

| # | Van de | So luong | Giai phap |
|---|---|---|---|
| 6 | **Dash unit inconsistency** (`-` vs `—`) | 126 | Normalize thanh `"-"` hoac `"unitless"` |
| 7 | **Mu/micro inconsistency** (`μ` vs `µ`) | 55 | Normalize ve 1 ky tu |
| 8 | **Vietnamese remnants** (`lần`, `Hướng về phía q₂`) | 3 | Dich sang English |
| 9 | **2 duplicate questions** | 4 rows | Kiem tra answer co giong nhau khong, de-dup |
| 10 | **Mat can bang domain** (CHLT=20 vs LD=397) | — | Data augmentation cho domain nho |

### 7.3 Muc do uu tien THAP (Nice-to-have)

| # | Van de | Giai phap |
|---|---|---|
| 11 | CoT ngan nhat chi 92 chars (2 steps) | Sinh lai CoT chi tiet hon |
| 12 | DT co outlier answer len 6.3M | Kiem tra tinh hop ly |

---

## 8. Kien nghi cho Pipeline Inference

Dua tren EDA, pipeline inference can xu ly **4 loai bai toan KHAC NHAU**:

> **Ghi chu:** Scientific notation (237 rows) se duoc **chuan hoa ve dang so thuan** trong buoc
> preprocessing data (vd: `24.45 × 10^-3` → `0.02445`), nen merge chung vao nhanh Numeric.

```
                         Question Input
                              │
                              ▼
                     ┌─────────────────┐
                     │   Classifier     │
                     │   (rule-based    │
                     │   hoac model)    │
                     └─────┬───────────┘
                           │
          ┌────────────────┼───────┬──────────┐
          ▼                ▼       ▼          ▼
      [Numeric]         [Yes/No] [Text]  [Multi-val]
      1210 rows          21 rows 87 rows  25 rows
      (incl. SciNot       │       │          │
       da normalize)      │       │          │
          │                │       │          │
          ▼                ▼       ▼          ▼
      PoT+Calc           Logic   Reason   PoT+Parse
      → float            → Y/N   → text   → val1;val2
          │                │       │          │
          └────────────────┴───────┴──────────┘
                           │
                           ▼
                   Response Formatter

---

## 9. Duplicate Questions

| Question (truncated) | IDs | Same answer? |
|---|---|---|
| Three identical charges q=1.2×10^-6 C at vertices... | LD302, LD303 | Can verify |
| A capacitor with capacitance of 5 μF charged to 20V... | TD368, TD369 | TD368=numeric, TD369="Do not change" → KHAC! |

**TD368 vs TD369:** Cung question nhung answer hoan toan khac → co the la 2 phan khac nhau cua cung 1 bai.

---

## 10. Key Takeaways cho doi

1. **28% answer KHONG PHAI la so don thuan** — pipeline khong the chi tra ve 1 float + 1 unit
2. **Scientific notation** (237 rows, 2+ formats khac nhau) — se **chuan hoa ve numeric** trong preprocessing, khong con la loai rieng trong pipeline
3. **CHLT la domain dac biet** (100% Yes/No) — co the dung rule-based + formula check thay vi LLM
4. **THCB yeu cau multi-value output** — format `val1; val2` voi `unit1; unit2`
5. **Domain imbalance nghiem trong** — CHLT (20) vs LD (397) = 20x chenh lech
6. **Co 14 rows thieu unit** — can report BTC hoac fill thu cong
7. **Token budget thoai mai** — P95 tong chi ~350 tokens, du room cho few-shot + tool logs trong context 262K
8. **2 rows Vietnamese con sot** trong unit field — can fix
