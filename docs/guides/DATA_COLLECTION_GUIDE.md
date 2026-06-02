# Hướng dẫn thu thập dữ liệu bài tập Vật lý

> **Mục đích:** Thu thập thêm bài tập vật lý (câu hỏi + đáp án) để fine-tune model AI giải bài.
> **Người thu thập:** Không cần biết code — chỉ cần copy/paste bài tập vào file CSV.

---

## 1. Bối cảnh dự án

Chúng mình đang xây hệ thống AI giải bài tập vật lý cho cuộc thi **EXACT 2026**. Hệ thống dùng model **Qwen 3.5 4B** (model nhỏ, chạy trên 1 GPU) để:

1. Đọc đề bài tiếng Anh
2. Sinh code Python tính toán
3. Chạy code lấy đáp án

**Kết quả hiện tại:** Model giải đúng **35/60 câu (58.3%)** trên bộ test vàng — cần cải thiện lên **>70%** thông qua fine-tuning với thêm dữ liệu.

**Dữ liệu hiện có:** 1,352 câu (đã có sẵn từ BTC). Phân bố **không đều** và model yếu ở một số dạng bài cụ thể → cần thu thập thêm đúng dạng bài model hay sai.

---

## 2. Cấp học & phạm vi kiến thức

### Cấp học: **Vật lý 11 (lớp 11 Việt Nam)**, tương đương AP Physics / A-Level Physics

### 6 chủ đề chính (xếp theo mức ưu tiên thu thập)

| # | Mã | Chủ đề | Mô tả | Có sẵn | Cần thêm | Ưu tiên |
|---|-----|--------|-------|:------:|:--------:|:-------:|
| 1 | **LD** | Lực điện / Tĩnh điện | Lực Coulomb, cân bằng điện, lực giữa nhiều điện tích | 397 | **50-100** | 🔴 Cao |
| 2 | **DT** | Điện trường & Điện thế | Cường độ điện trường, hiệu điện thế, công của lực điện | 68 | **50-80** | 🔴 Cao |
| 3 | **CHLT** | Cộng hưởng mạch điện | Câu hỏi Có/Không về điều kiện cộng hưởng RLC | 20 | **30-50** | 🔴 Cao |
| 4 | **DDT** | Cảm ứng điện từ | Suất điện động cảm ứng, từ thông, cuộn cảm | 130 | **30-50** | 🟡 Trung bình |
| 5 | **CH** | Mạch điện xoay chiều | Mạch RLC, tổng trở, công suất, hệ số công suất | 290 | 20-30 | 🟢 Thấp |
| 6 | **NL** | Năng lượng điện | Năng lượng tụ điện, cuộn cảm, dao động LC | 190 | 20-30 | 🟢 Thấp |
| 7 | **TD** | Tụ điện | Điện dung, ghép tụ nối tiếp/song song, điện môi | 177 | 20-30 | 🟢 Thấp |
| 8 | **THCB** | Sai số & Mạch DC | Sai số phép đo, mạch điện 1 chiều đơn giản | 80 | 10-20 | 🟢 Thấp |

### Tại sao LD và DT ưu tiên cao nhất?

Model sai **nhiều nhất ở bài tĩnh điện có hình học phức tạp** — khi đề bài đặt nhiều điện tích ở các vị trí khác nhau (tam giác, hình vuông, đường thẳng) và hỏi lực tổng hợp hoặc điện trường tổng hợp. Model thường:
- Phân tích vector sai hướng → ra kết quả = 0 (9/25 câu sai)
- Tính sai góc giữa các lực → sai đáp số (5/25 câu sai)
- Không xử lý được đáp án dạng biểu thức (`-2√2 q`)

---

## 3. Mẫu dữ liệu cần thu thập

### Format CSV: 4 cột

| Cột | Mô tả | Ví dụ |
|-----|-------|-------|
| `question` | Đề bài **bằng tiếng Anh** | "Two charges q1 = 5 μC and q2 = -3 μC are placed 8 cm apart..." |
| `answer` | Đáp số (số thuần, ký hiệu khoa học, hoặc Yes/No) | `21.09`, `5.07 * 10^{-6}`, `Yes` |
| `unit` | Đơn vị | `N`, `V/m`, `J`, `-` (nếu không có đơn vị) |
| `domain` | Mã chủ đề (xem bảng trên) | `LD`, `DT`, `CH`, `NL`, `TD`, `DDT`, `THCB`, `CHLT` |

### Ví dụ cụ thể

**Ví dụ 1 — LD (Lực Coulomb 2 điện tích, đơn giản):**
```
question: Two charges, q1 = -2.4 × 10^-6 C and q2 = -2.1 × 10^-6 C, are separated by 7.5 cm. Point M lies on the line connecting the two charges but outside the segment between them, and is located 11.9 cm to the left of charge q1. Calculate the net electric field at M. Give your answer rounded to three decimal places.
answer: 2.027 * 10^{6}
unit: V/m
domain: LD
```

**Ví dụ 2 — LD (3 điện tích, hình học, model hay sai):**
```
question: Two charges q1 = +7 × 10^-8 C and q2 = -6 × 10^-8 C are placed at points A and B, 10 cm apart in air. A third charge q3 = +8 × 10^-8 C is placed at point C, such that the distance from C to A is 7 cm and the distance from C to B is 5 cm. Calculate the net electrostatic force on q3.
answer: 0.023
unit: N
domain: LD
```

**Ví dụ 3 — DT (Điện trường tổng hợp):**
```
question: A point charge q = 10 nC is placed at the origin. Determine the electric field strength at a point 5 cm away in vacuum.
answer: 36000
unit: V/m
domain: DT
```

**Ví dụ 4 — CHLT (Có/Không, cộng hưởng):**
```
question: An RLC series circuit has R = 100 Ω, L = 0.5 H, and C = 8 μF. Is the resonant frequency of this circuit equal to 80 Hz?
answer: No
unit: -
domain: CHLT
```

**Ví dụ 5 — THCB (Nhiều giá trị):**
```
question: A student measures a resistor five times and gets 47.2, 47.5, 47.3, 47.4, 47.1 Ω. Calculate the mean value and the absolute error.
answer: 47.3; 0.12
unit: Ω; Ω
domain: THCB
```

---

## 4. Dạng bài ƯU TIÊN thu thập (model hay sai)

### 4.1 🔴 Bài tĩnh điện có hình học (LD, DT) — **Ưu tiên #1**

Đây là nhóm model sai nhiều nhất. Cần tập trung thu thập:

**a) 3+ điện tích đặt tại các đỉnh tam giác / hình vuông / lục giác:**
- Tìm lực tổng hợp / điện trường tổng hợp tại 1 điểm
- Bài yêu cầu phân tích thành phần vector (Fx, Fy) rồi tổng hợp
- Đáp án thường ở dạng khoa học: `3.29 * 10^{6}` V/m

**b) Điện tích trên đường thẳng — tìm vị trí cân bằng:**
- 2-3 điện tích trên 1 đường thẳng, tìm điểm E = 0 hoặc F = 0
- Cần xét dấu và hướng cẩn thận

**c) Bài có đáp án dạng biểu thức:**
- Ví dụ: "Tìm điện tích q3 để điện trường tại D bằng 0" → đáp án: `-2√2 q`
- Model code không xử lý được dạng symbolic → cần dữ liệu train

**d) Bài đặt điện tích trong điện trường đều:**
- Tính công, hiệu điện thế, năng lượng
- Kết hợp lực Coulomb + điện trường ngoài

### 4.2 🔴 Câu hỏi Có/Không cộng hưởng (CHLT) — **Ưu tiên #2**

Hiện chỉ có **20 câu** — quá ít. Dạng câu hỏi:
- "Mạch RLC nối tiếp có R = ..., L = ..., C = .... Tần số cộng hưởng có bằng X Hz không?"
- "Để xảy ra cộng hưởng, điện dung C phải bằng bao nhiêu? So sánh với giá trị cho trước."

### 4.3 🟡 Cảm ứng điện từ (DDT)

- Tính suất điện động cảm ứng khi từ thông thay đổi
- Cuộn dây trong từ trường biến thiên
- Tự cảm, hỗ cảm

### 4.4 Các dạng đáp án đặc biệt (mọi chủ đề)

| Dạng đáp án | Ví dụ | Ghi chú |
|-------------|-------|---------|
| Số thuần | `5.07`, `300` | Chiếm 72% — đã có nhiều |
| Ký hiệu khoa học | `2.45 * 10^{-3}` | Chiếm 17.5% — cần thêm |
| Nhiều giá trị | `0.6; 1.2` | Chiếm 1.9% — **cần thêm nhiều** |
| Có/Không | `Yes`, `No` | Chiếm 1.6% — **cần thêm nhiều** |
| Biểu thức | `-2√2 q`, `W₀sin²(ωt)` | Rất hiếm — cần thêm |

---

## 5. Nguồn thu thập gợi ý

### 5.1 Sách giáo khoa & Sách bài tập Việt Nam (dịch sang tiếng Anh)

> **Cách làm:** Copy bài tập tiếng Việt → dùng ChatGPT/Google Translate dịch sang tiếng Anh → chỉnh sửa thuật ngữ cho chuẩn.

- **SGK Vật lý 11** (bộ Kết nối tri thức / Cánh diều / Chân trời sáng tạo)
- **Sách bài tập Vật lý 11**
- **Sách "Giải bài tập Vật lý 11"** các NXB
- **Đề thi giữa kỳ / cuối kỳ lớp 11** (trên Violet, VnDoc, HOC247)
- **Đề thi HSG Vật lý cấp tỉnh** (phần tĩnh điện, mạch xoay chiều)

**Lưu ý dịch:**
- `μC` = microcoulomb, `nC` = nanocoulomb, `pF` = picofarad
- `Cường độ điện trường` = Electric field strength
- `Hiệu điện thế` = Potential difference / Voltage
- `Lực tương tác tĩnh điện` = Electrostatic force
- `Tụ điện phẳng` = Parallel-plate capacitor
- `Cộng hưởng` = Resonance
- `Suất điện động cảm ứng` = Induced EMF
- `Hằng số điện môi` = Dielectric constant

### 5.2 Trang web tiếng Anh (dùng trực tiếp)

- **Physics Classroom** (physicsclassroom.com) — bài tập có lời giải
- **Khan Academy** — Electrostatics, Circuits practice
- **OpenStax University Physics Vol 2** — Chapter 5-12 (Electricity & Magnetism), end-of-chapter problems
- **HyperPhysics** (hyperphysics.phy-astr.gsu.edu) — Example problems
- **Brilliant.org** — Physics problems (cần tài khoản)
- **MIT OpenCourseWare 8.02** — Problem sets (Electricity and Magnetism)

### 5.3 Trang web tiếng Việt (cần dịch)

- **VnDoc.com** — Bài tập Vật lý 11 theo chương
- **HOC247.net** — Đề thi, bài tập tự luận Vật lý 11
- **Loigiaihay.com** — Giải bài tập SGK Vật lý 11
- **Violet.vn** — Đề kiểm tra Vật lý 11
- **Vietjack.com** — Lý thuyết + Bài tập Vật lý 11

---

## 6. Quy tắc khi thu thập

### ✅ NÊN

1. **Đề bài phải bằng tiếng Anh** — nếu nguồn gốc tiếng Việt thì dịch trước
2. **Phải có đáp số chính xác** — bạn hoặc nguồn sách phải cho đáp án đúng
3. **Ghi rõ đơn vị** — `N`, `V/m`, `J`, `Ω`, `A`, `W`, `F`, `H`, `C`, `%`
4. **Ghi rõ domain** — dùng mã LD/DT/CH/CHLT/NL/TD/DDT/THCB
5. **Ưu tiên bài có hình học** — tam giác, hình vuông, lục giác, đường thẳng
6. **Ký hiệu khoa học viết thống nhất:** `2.45 * 10^{-3}` hoặc `2.45e-3`
7. **Nhiều giá trị phân cách bằng `;`** ví dụ: `47.3; 0.12`

### ❌ KHÔNG

1. **Không thu bài trắc nghiệm** (A/B/C/D) — hệ thống chỉ giải tự luận
2. **Không thu bài thiếu đáp án** — phải có đáp số
3. **Không thu bài quá dài** (>100 từ trong đề) — model 4B xử lý kém với đề dài
4. **Không thu bài Vật lý 12** (Quang học, Hạt nhân, Lượng tử) — ngoài phạm vi thi
5. **Không thu bài chỉ hỏi lý thuyết** (ví dụ: "Phát biểu định luật Coulomb") — hệ thống chỉ tính toán

---

## 7. Thống kê lỗi model hiện tại (để biết cần thu thập gì)

### Model sai 25/60 câu. Phân bố lỗi:

```
ZERO_ANSWER (9 câu):   Code chạy nhưng ra 0  → do phân tích vector SAI HƯỚNG
WRONG_COMPUTATION (5):  Tính sai logic         → do set up bài toán sai
NO_CODE (4):            Không sinh được code   → đề quá phức tạp hoặc đáp án dạng text
TIMEOUT (3):            Quá 60 giây            → code quá phức tạp, chạy lâu
CLOSE_MISS (2):         Gần đúng (sai <2%)     → tính đúng nhưng làm tròn sai
EXEC_FAILED (1):        Code lỗi syntax        → sinh code bị lỗi cú pháp
FACTOR_2_ERROR (1):     Sai gấp đôi            → quên nhân 2 hoặc chia 2
```

### Insight quan trọng:
- **9/25 lỗi là ZERO_ANSWER** — model tính lực/trường = 0 khi đáp án thật ≠ 0
- Tất cả lỗi đều ở domain **LD/DT (tĩnh điện)** vì bộ test chỉ có domain này
- Bài mà model trả lời **trong <10 giây → 100% đúng**
- Bài mà model mất **>50 giây → chỉ 9% đúng** (nghĩa là model "biết" khi nào nó không giải được)

---

## 8. Số lượng mục tiêu

| Ưu tiên | Domain | Số câu cần thêm | Dạng bài tập trung |
|:--------:|--------|:----------------:|---------------------|
| 🔴 | LD (Lực điện) | 50-100 | 3+ điện tích, hình học, vector |
| 🔴 | DT (Điện trường) | 50-80 | Điện trường tổng hợp, siêu vị trí |
| 🔴 | CHLT (Cộng hưởng) | 30-50 | Có/Không cộng hưởng, so sánh tần số |
| 🟡 | DDT (Cảm ứng) | 30-50 | Faraday, suất điện động, cuộn cảm |
| 🟢 | CH, NL, TD, THCB | 10-30 mỗi loại | Bổ sung đa dạng |

**Tổng mục tiêu: ~200-400 câu mới**

> Sau khi thu thập xong, mình sẽ dùng DeepSeek (AI mạnh) để viết lại lời giải dưới dạng code Python, rồi fine-tune model nhỏ. Bạn chỉ cần thu thập đề + đáp số, không cần viết lời giải.

---

## 9. Template file CSV

Tạo file `collected_data.csv` với format:

```csv
question,answer,unit,domain
"Two point charges q1 = 5 μC and q2 = -3 μC are 8 cm apart in vacuum. Calculate the magnitude of the electrostatic force between them.",21.09,N,LD
"A series RLC circuit has R = 100 Ω, L = 0.5 H, and C = 8 μF. Is the resonant frequency equal to 80 Hz?",No,-,CHLT
```

**Lưu ý format:**
- Dùng dấu `"` bọc question nếu trong đề có dấu `,`
- Đáp án ký hiệu khoa học: `2.45 * 10^{-3}` (dùng `*` và `^{}`)
- Nhiều đáp án: `47.3; 0.12` (dùng `;` phân cách)
- Không có đơn vị: dùng `-`

---

*Cảm ơn bạn rất nhiều! Dữ liệu này sẽ giúp model giải vật lý tốt hơn đáng kể.* 🙏
