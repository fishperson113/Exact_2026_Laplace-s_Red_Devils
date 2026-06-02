# Hướng dẫn thu thập dữ liệu Pre-training Vật lý

> **Mục đích:** Thu thập corpus văn bản vật lý (lý thuyết, ví dụ mẫu, bài giải chi tiết) để **pre-train tiếp** model AI trước khi fine-tune.
> **Khác gì với fine-tuning data?** Fine-tune cần đề + đáp số chính xác (CSV). Pre-train cần **văn bản dài, giải thích chi tiết** — không cần format chuẩn, chỉ cần nội dung đúng và phong phú.

---

## 1. Pre-training là gì và tại sao cần?

### Vấn đề hiện tại

Model Qwen 3.5 4B là model đa năng — nó biết nhiều thứ nhưng **không chuyên sâu vật lý lớp 11 VN**. Kết quả hiện tại:

- **35/60 câu đúng (58.3%)** trên bộ test tĩnh điện
- **9/25 lỗi là ZERO_ANSWER** — model hiểu sai hướng vector → tính ra kết quả = 0
- **5/25 lỗi WRONG_COMPUTATION** — model set up bài toán sai từ đầu

### Pre-training giúp gì?

```
                 Kiến thức chung        Kiến thức vật lý       Giải bài cụ thể
Model gốc  ──────────────────────────►  (yếu ở đây)
                                            │
Pre-train  ─────────────────────────────────┤  ◄── BƯỚC NÀY
(đọc sách lý thuyết, ví dụ mẫu)            │
                                            ▼
Fine-tune  ──────────────────────────────────────────────────►  (mạnh ở đây)
(học format đề + code Python)
```

**Pre-training = "cho model đọc sách vật lý"** trước khi dạy nó giải bài. Giúp model:
- Hiểu sâu hơn về vector, hệ tọa độ, quy ước dấu
- Nắm chắc công thức và khi nào dùng công thức nào
- Biết cách phân tích hình học trong bài tĩnh điện
- Quen với thuật ngữ vật lý tiếng Anh (gốc dịch từ tiếng Việt)

---

## 2. Bạn cần thu thập những gì?

### 3 loại dữ liệu, xếp theo ưu tiên:

| # | Loại | Mô tả | Ưu tiên | Mục tiêu |
|---|------|-------|:-------:|:--------:|
| A | **Bài giải mẫu có lời giải chi tiết** | Đề bài + lời giải từng bước (có giải thích tại sao) | 🔴 Cao nhất | 200-500 bài |
| B | **Lý thuyết + công thức có ví dụ** | Đoạn sách giáo khoa giải thích khái niệm + ví dụ minh họa | 🟡 Trung bình | 50-100 đoạn |
| C | **Tóm tắt công thức + bảng tra** | Bảng tổng hợp công thức theo chủ đề, bảng hằng số | 🟢 Thấp | 10-20 trang |

---

## 3. Loại A — Bài giải mẫu (ƯU TIÊN CAO NHẤT)

### Format: Đoạn văn bản tự do

Không cần CSV — chỉ cần copy nguyên đoạn text vào file `.txt` hoặc `.md`. Mỗi bài một khối, cách nhau bằng dòng trống.

### Ví dụ mẫu lý tưởng

````
## Problem: Net electric field from two charges at a triangle vertex

Two point charges q1 = +4 μC and q2 = -3 μC are placed at two vertices A and B of an equilateral triangle with side length a = 10 cm. Find the electric field at the third vertex C.

### Solution

**Step 1: Set up coordinate system.**
Place A at the origin, B at (a, 0) = (0.1, 0) m.
For an equilateral triangle, C is at (a/2, a√3/2) = (0.05, 0.0866) m.

**Step 2: Convert units to SI.**
- q1 = +4 × 10⁻⁶ C
- q2 = -3 × 10⁻⁶ C
- a = 0.10 m
- k = 9 × 10⁹ N·m²/C²

**Step 3: Calculate electric field from q1 at C.**
Distance r1 = a = 0.10 m (equilateral triangle, all sides equal).
E1 = k × |q1| / r1² = 9 × 10⁹ × 4 × 10⁻⁶ / 0.01 = 3.6 × 10⁶ V/m

Direction: q1 is positive → E1 points AWAY from A toward C.
Unit vector from A to C: (0.05, 0.0866) / 0.10 = (0.5, 0.866)
E1x = 3.6 × 10⁶ × 0.5 = 1.8 × 10⁶ V/m
E1y = 3.6 × 10⁶ × 0.866 = 3.118 × 10⁶ V/m

**Step 4: Calculate electric field from q2 at C.**
Distance r2 = a = 0.10 m.
E2 = k × |q2| / r2² = 9 × 10⁹ × 3 × 10⁻⁶ / 0.01 = 2.7 × 10⁶ V/m

Direction: q2 is negative → E2 points TOWARD B from C.
Unit vector from C to B: (0.05, -0.0866) / 0.10 = (0.5, -0.866)
E2x = 2.7 × 10⁶ × 0.5 = 1.35 × 10⁶ V/m
E2y = 2.7 × 10⁶ × (-0.866) = -2.338 × 10⁶ V/m

**Step 5: Vector sum.**
Ex = E1x + E2x = 1.8 × 10⁶ + 1.35 × 10⁶ = 3.15 × 10⁶ V/m
Ey = E1y + E2y = 3.118 × 10⁶ + (-2.338 × 10⁶) = 0.78 × 10⁶ V/m

**Step 6: Magnitude.**
E = √(Ex² + Ey²) = √((3.15 × 10⁶)² + (0.78 × 10⁶)²) = 3.245 × 10⁶ V/m

**Answer: E ≈ 3.25 × 10⁶ V/m**

Key concepts used:
- Electric field from point charge: E = k|q|/r²
- Positive charge → field away, negative charge → field toward
- Vector decomposition into x, y components
- Pythagorean theorem for magnitude
````

### Tại sao format này tốt cho pre-training?

1. **Có hệ tọa độ rõ ràng** (Step 1) — model học cách set up tọa độ
2. **Convert đơn vị SI** (Step 2) — model học μC → C, cm → m
3. **Giải thích hướng vector** (Step 3-4) — "q1 positive → E1 points AWAY" — đây là chỗ model hay sai nhất
4. **Phân tích thành phần Fx, Fy** rồi tổng hợp — pattern chính cần học
5. **Có "Key concepts used"** — giúp model liên kết concept với bài tập

### Dạng bài cần tập trung (nhóm model hay sai)

#### 🔴 Nhóm 1: Vector decomposition cho 3+ điện tích (chiếm 9/25 lỗi)

Model thường tính E = 0 hoặc F = 0 vì phân tích vector sai hướng. Cần nhiều bài giải mẫu cho:

- **3 điện tích ở 3 đỉnh tam giác** — tìm F hoặc E tại 1 đỉnh
- **4 điện tích ở 4 đỉnh hình vuông** — tìm F hoặc E tại tâm hoặc 1 đỉnh
- **3+ điện tích trên đường thẳng** — tìm lực tổng hợp lên 1 điện tích
- **Điện tích trên trục và điểm ngoài trục** — cần phân tích góc

Trong lời giải, **nhấn mạnh rõ ràng**:
- Hướng lực: "q1 dương → lực đẩy → hướng ra xa q1"
- Hướng trường: "q2 âm → E hướng VỀ PHÍA q2"
- Dấu thành phần: "E2y = -2.7 × 10⁶ (hướng xuống, dấu âm)"
- Kiểm tra: "Hai thành phần y triệt tiêu một phần (không hoàn toàn) vì E1y > E2y"

#### 🔴 Nhóm 2: Bài tìm vị trí cân bằng

- 2 điện tích cùng dấu → điểm cân bằng nằm giữa
- 2 điện tích trái dấu → điểm cân bằng nằm ngoài, phía điện tích nhỏ hơn
- Cần giải thích **tại sao** điểm cân bằng nằm ở đó (không chỉ tính)

#### 🟡 Nhóm 3: Bài cho đáp án symbolic

- "Tìm q3 để E tại D bằng 0" → đáp án: `-2√2 q`
- "Tìm vị trí x để F = 0" → đáp án: `d / (1 + √(q2/q1))`
- Lời giải cần giữ nguyên ký hiệu, không thay số

---

## 4. Loại B — Lý thuyết + Công thức có ví dụ

### Format: Đoạn văn bản giải thích khái niệm

Copy nguyên đoạn sách giáo khoa hoặc trang web giải thích lý thuyết. Mỗi đoạn nên có **ít nhất 1 ví dụ minh họa kèm theo**.

### Chủ đề cần thu thập (xếp theo ưu tiên)

#### 🔴 Ưu tiên cao — Model yếu nhất ở đây

| Chủ đề | Nội dung cần có | Tại sao cần |
|--------|-----------------|-------------|
| **Nguyên lý chồng chất lực/trường** | Cách cộng vector lực Coulomb, cách cộng vector E-field | 9/25 lỗi do vector sai |
| **Quy ước hướng điện trường** | E hướng ra xa Q+ / về phía Q− , khi nào cùng chiều / ngược chiều | Model hay đảo dấu |
| **Phân tích lực trong hệ tọa độ Oxy** | Đặt hệ tọa độ, chiếu lên Ox Oy, cộng thành phần | Pattern chính model cần học |
| **Lực Coulomb — bài toán 3+ điện tích** | Setup hình, tính từng cặp, tổng hợp | Dạng bài khó nhất |
| **Điện trường tổng hợp tại 1 điểm** | Tính E từ nhiều nguồn, vẽ vector, cộng | Tương tự lực nhưng cho E |
| **Cân bằng điện tích trên đường thẳng** | Điều kiện E = 0, F = 0, cách tìm vị trí | Model sai setup phương trình |

#### 🟡 Ưu tiên trung bình

| Chủ đề | Nội dung cần có |
|--------|-----------------|
| **Mạch RLC nối tiếp — cộng hưởng** | Điều kiện cộng hưởng, f₀ = 1/(2π√LC), ý nghĩa |
| **Cảm ứng điện từ — Định luật Faraday** | EMF = -dΦ/dt, cuộn dây, từ thông biến thiên |
| **Năng lượng tụ điện và cuộn cảm** | W = ½CV², W = ½LI², dao động LC |
| **Tụ điện — ghép nối tiếp / song song** | Công thức ghép tụ, có điện môi |

#### 🟢 Ưu tiên thấp (đã có đủ data)

| Chủ đề | Nội dung cần có |
|--------|-----------------|
| Sai số phép đo | Sai số tuyệt đối, sai số tương đối |
| Mạch DC đơn giản | Ohm, Kirchhoff, mạch cầu |

### Ví dụ đoạn lý thuyết tốt

```
## Superposition Principle for Electric Fields

When multiple point charges are present, the total electric field at any point
is the VECTOR SUM of the individual fields produced by each charge.

E_total = E_1 + E_2 + E_3 + ...

IMPORTANT: This is a vector equation. You cannot simply add magnitudes.
You must decompose each field into x and y components, add components
separately, then find the resultant magnitude.

Direction rules:
- Positive charge: E points AWAY from the charge (radially outward)
- Negative charge: E points TOWARD the charge (radially inward)

Common mistake: Students often forget that for a negative charge at position A,
the electric field at point P points FROM P TOWARD A, not from A toward P.

Example: Two charges q1 = +2 μC at origin and q2 = -3 μC at (4 cm, 0).
Find E at point P = (0, 3 cm).

[... lời giải chi tiết ...]
```

---

## 5. Loại C — Bảng tổng hợp công thức

### Format: Bảng hoặc danh sách

Ít ưu tiên hơn nhưng vẫn hữu ích. Thu thập bảng tóm tắt công thức theo chương.

### Ví dụ

```
## Electrostatics Formula Sheet

| Formula | Name | Unit | Notes |
|---------|------|------|-------|
| F = k|q1||q2|/r² | Coulomb's Law | N | k = 9 × 10⁹ N·m²/C² |
| E = k|q|/r² | Electric field (point charge) | V/m | Direction: away from +, toward - |
| E = F/q₀ | Definition of E-field | V/m | q₀ is test charge |
| V = kq/r | Electric potential (point charge) | V | Scalar, can be negative |
| A = q(V_A - V_B) | Work by electric force | J | A > 0 if charge moves "downhill" |
| W = qV | Potential energy | J | Energy of charge q at potential V |
| E = U/d | Uniform field between plates | V/m | U = voltage, d = separation |
| C = εS/d | Parallel-plate capacitor | F | ε = ε₀εᵣ |
| W = ½CV² = ½QU = Q²/2C | Energy in capacitor | J | Three equivalent forms |

Unit conversions:
- 1 μC = 10⁻⁶ C, 1 nC = 10⁻⁹ C, 1 pC = 10⁻¹² C
- 1 cm = 0.01 m, 1 mm = 0.001 m
- 1 kV/m = 10³ V/m, 1 MV/m = 10⁶ V/m
- 1 μF = 10⁻⁶ F, 1 nF = 10⁻⁹ F, 1 pF = 10⁻¹² F

Constants:
- k = 9 × 10⁹ N·m²/C² (Coulomb constant)
- ε₀ = 8.854 × 10⁻¹² F/m (vacuum permittivity)
- e = 1.6 × 10⁻¹⁹ C (elementary charge)
- π ≈ 3.14159
```

---

## 6. Nguồn thu thập

### 6.1 Sách giải bài tập (nguồn tốt nhất cho Loại A)

**Tiếng Việt (dịch sang tiếng Anh):**
- **"Giải bài tập Vật lý 11"** — NXB Giáo dục (có lời giải từng bước)
- **"Bài tập Vật lý 11 nâng cao"** — dạng bài khó, nhiều hình học
- **"Phương pháp giải bài tập Vật lý 11"** — sách của Vũ Thanh Khiết, Nguyễn Đức Hiệp
- **Đề thi HSG Vật lý tỉnh/thành** — bài khó có lời giải chi tiết

**Tiếng Anh (dùng trực tiếp):**
- **"Physics: Principles with Applications" (Giancoli)** — Chapter 16-21, end-of-chapter solutions
- **"University Physics" (Young & Freedman)** — Chapter 21-31, worked examples
- **"Fundamentals of Physics" (Halliday/Resnick)** — Chapter 21-33
- **OpenStax University Physics Vol 2** — Chapter 5-12, free PDF, có solutions manual
- **Chegg / Slader** — lời giải chi tiết cho các sách trên

**Trang web lời giải:**
- **Loigiaihay.com** — Giải chi tiết SGK + SBT Vật lý 11
- **Vietjack.com** — Phương pháp giải + bài mẫu theo dạng
- **Khan Academy** — Video + practice với explanations
- **Physics Classroom** — Tutorials + practice problems with solutions
- **Hyperphysics** — Concept maps + worked examples

### 6.2 Sách giáo khoa (nguồn tốt cho Loại B)

- **SGK Vật lý 11** (bộ Kết nối tri thức) — phần lý thuyết + ví dụ mẫu
- **OpenStax University Physics Vol 2** — free, tiếng Anh, có ví dụ mẫu trong mỗi section
- **MIT OCW 8.02 lecture notes** — Electricity and Magnetism

### 6.3 Trang tổng hợp công thức (nguồn cho Loại C)

- **Physicsfomulas.com**
- **Tờ formula sheet** trong SGK hoặc cuối sách bài tập
- **Wikipedia** — các bài về Coulomb's Law, Electric Field, Capacitance...

---

## 7. Cách dịch từ tiếng Việt sang tiếng Anh

### Quy trình khuyên dùng

1. Copy đoạn tiếng Việt
2. Dán vào ChatGPT/Claude với prompt: *"Dịch đoạn giải bài tập vật lý sau sang tiếng Anh. Giữ nguyên các ký hiệu toán học, số liệu, và đơn vị. Dùng thuật ngữ vật lý chuẩn."*
3. Kiểm tra lại: đơn vị, số liệu, ký hiệu có đúng không
4. Paste vào file thu thập

### Bảng thuật ngữ quan trọng

| Tiếng Việt | Tiếng Anh | Ghi chú |
|------------|-----------|---------|
| Lực tương tác tĩnh điện | Electrostatic force | |
| Cường độ điện trường | Electric field strength / Electric field intensity | |
| Điện trường tổng hợp | Net electric field / Resultant electric field | |
| Nguyên lý chồng chất | Superposition principle | |
| Hiệu điện thế | Potential difference / Voltage | |
| Điện thế | Electric potential | Khác với hiệu điện thế! |
| Công của lực điện | Work done by electric force | |
| Vị trí cân bằng | Equilibrium position | |
| Tụ điện phẳng | Parallel-plate capacitor | |
| Ghép nối tiếp / song song | Series / parallel combination | |
| Điện dung tương đương | Equivalent capacitance | |
| Hằng số điện môi | Dielectric constant / Relative permittivity | |
| Mạch RLC nối tiếp | Series RLC circuit | |
| Tổng trở | Impedance | |
| Cộng hưởng | Resonance | |
| Hệ số công suất | Power factor | cos(φ) |
| Suất điện động cảm ứng | Induced EMF / Induced electromotive force | |
| Từ thông | Magnetic flux | |
| Tự cảm / Hỗ cảm | Self-inductance / Mutual inductance | |
| Sai số tuyệt đối / tương đối | Absolute error / Relative error | |
| Hướng ra xa / hướng về phía | Away from / toward | Quan trọng cho E-field direction |

---

## 8. Quy tắc khi thu thập

### ✅ NÊN

1. **Bài giải phải chi tiết** — có giải thích "tại sao", không chỉ công thức → số
2. **Giải thích hướng vector rõ ràng** — "E points away from positive charge", "force is attractive so it points toward q2"
3. **Vẽ / mô tả hệ tọa độ** — "Place q1 at origin, q2 at (d, 0)"
4. **Ghi rõ đổi đơn vị SI** — "5 μC = 5 × 10⁻⁶ C", "8 cm = 0.08 m"
5. **Giữ nguyên các ký hiệu đặc biệt** — √, π, ×, ², ³
6. **Thu nhiều bài tĩnh điện có hình học** — tam giác, hình vuông, đường thẳng

### ❌ KHÔNG

1. **Không thu bài chỉ có đề + đáp số** (thiếu lời giải) — đã có guide riêng cho dạng đó
2. **Không thu bài Vật lý 12** (quang, hạt nhân, lượng tử) — ngoài phạm vi
3. **Không thu lý thuyết suông không có ví dụ** — phải có ít nhất 1 bài minh họa
4. **Không thu bài trắc nghiệm** — chỉ tự luận có lời giải
5. **Không cần đảm bảo format CSV** — text tự do trong file `.txt` hoặc `.md` là OK

---

## 9. Cấu trúc file nộp

Tạo folder theo tên chủ đề, mỗi file chứa nhiều bài/đoạn:

```
pretrain_data/
├── solutions/                          ← Loại A: Bài giải mẫu
│   ├── LD_coulomb_force_solutions.md   ← Bài lực Coulomb có lời giải
│   ├── LD_electric_field_solutions.md  ← Bài điện trường có lời giải
│   ├── LD_equilibrium_solutions.md     ← Bài cân bằng có lời giải
│   ├── CH_rlc_circuit_solutions.md     ← Bài mạch RLC
│   ├── DDT_induction_solutions.md      ← Bài cảm ứng điện từ
│   └── ...
├── theory/                             ← Loại B: Lý thuyết + ví dụ
│   ├── electrostatics_theory.md
│   ├── circuits_theory.md
│   ├── induction_theory.md
│   └── ...
└── formulas/                           ← Loại C: Bảng công thức
    ├── electrostatics_formulas.md
    ├── circuits_formulas.md
    └── ...
```

### Quy ước đặt tên
- Prefix domain: `LD_`, `DT_`, `CH_`, `NL_`, `TD_`, `DDT_`, `THCB_`, `CHLT_`
- Dùng tiếng Anh cho tên file
- Mỗi file nên chứa **5-20 bài/đoạn** cùng chủ đề

---

## 10. Số lượng mục tiêu

| Loại | Ưu tiên | Mục tiêu | Tương đương |
|------|:-------:|:--------:|-------------|
| A — Bài giải mẫu | 🔴 | 200-500 bài | ~200-500 KB text |
| B — Lý thuyết + ví dụ | 🟡 | 50-100 đoạn | ~100-200 KB text |
| C — Bảng công thức | 🟢 | 10-20 trang | ~20-50 KB text |
| **Tổng** | | | **~300-750 KB text** |

### Phân bổ theo chủ đề (Loại A):

| Domain | Số bài giải cần | Tập trung vào |
|--------|:---------------:|----------------|
| **LD** (Lực điện) | 80-150 | Vector force, 3+ charges, geometry |
| **DT** (Điện trường) | 50-100 | Superposition E-field, direction |
| **CH** (Mạch xoay chiều) | 30-60 | RLC, impedance, resonance |
| **CHLT** (Cộng hưởng Y/N) | 15-30 | Yes/No resonance conditions |
| **DDT** (Cảm ứng) | 20-40 | Faraday, EMF, inductance |
| **NL** (Năng lượng) | 15-30 | Energy in C/L, LC oscillation |
| **TD** (Tụ điện) | 15-30 | Capacitance, dielectric, series/parallel |
| **THCB** (Sai số) | 10-20 | Measurement error, basic DC |

---

## 11. So sánh: Pre-training data vs Fine-tuning data

| | Pre-training | Fine-tuning |
|---|---|---|
| **Mục đích** | Model hiểu kiến thức vật lý | Model học format đề → code Python |
| **Format** | Text tự do (lời giải, lý thuyết) | CSV chuẩn (question, answer, unit, domain) |
| **Cần đáp số chính xác?** | Tốt nhất là có, nhưng lời giải chi tiết quan trọng hơn | **Bắt buộc** — đáp số phải chính xác |
| **Cần lời giải?** | **Có** — càng chi tiết càng tốt | **Không** — chỉ cần đề + đáp số |
| **Ngôn ngữ** | Tiếng Anh | Tiếng Anh |
| **Số lượng** | 200-500 bài + theory | 200-400 câu |
| **Ai xử lý sau?** | Mình sẽ format thành corpus cho training | Mình dùng DeepSeek viết code Python |
| **Guide riêng** | File này | `DATA_COLLECTION_GUIDE.md` |

> **Bạn có thể thu cả hai loại cùng lúc!** Nếu bạn thấy bài tập có lời giải → copy cả lời giải (pre-train) VÀ ghi đề + đáp số vào CSV (fine-tune).

---

*Cảm ơn bạn! Dữ liệu pre-training giúp model "hiểu" vật lý, còn fine-tuning giúp model "giải" bài tập. Cả hai đều cần thiết.* 🙏
