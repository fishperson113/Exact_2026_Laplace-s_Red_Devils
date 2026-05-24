# Plan — EDA Logic_Based_Educational_Queries

> **Phạm vi:** Chỉ dataset Type 1 — [`app/data/raw/Logic_Based_Educational_Queries.json`](../app/data/raw/Logic_Based_Educational_Queries.json)  
> **Nguồn tham chiếu:** EXACT 2026 Kick-off Slides (Type 1: slide 16–19, 27)  
> **Trạng thái:** Plan để build — **chưa chạy EDA / notebook**

---

## 1. Mục tiêu

1. Khám phá dữ liệu logic (FOL + NL) phục vụ fine-tune / pipeline neurosymbolic (Z3 + LLM).
2. Map mỗi hạng mục EDA → **Key Challenges Type 1** (slide 19).
3. Thu thập **chỉ số định lượng** (mean, P50, P90, phân phối) — đối chiếu benchmark BTC (slide 17).
4. Đầu ra: checklist đã điền số + notebook `02_EDA_Dataset_Logic.ipynb` (khi implement).

---

## 2. Benchmark BTC (đối chiếu sau EDA)

| Chỉ số | Giá trị slide 17 |
|--------|------------------|
| Số record (mẫu) | 411 |
| Tổng câu hỏi | 808 |
| Câu hỏi / mẫu (trung bình) | ~1.97 |
| NL premise / mẫu (trung bình) | ~10.8 |
| Loại câu | 358 MCQ, 216 Yes/No/Uncertain, 234 Open-ended |
| Có FOL | 99% record |
| Có explanation | 100% |

---

## 3. Grain phân tích

- **Mẫu (record):** 1 phần tử JSON = 1 bộ `premises` + nhiều `questions`.
- **Câu hỏi (flatten):** 1 dòng = 1 cặp `(record_id, q_idx)` với `question`, `answer`, `explanation`, `idx[q_idx]`.

```text
record_id | q_idx | n_premises_nl | n_premises_used | question | answer | explanation | ...
```

---

## 4. Mục bắt buộc — Số câu hỏi / 1 mẫu

> Đo trên **411 record** trước khi flatten. Không suy từ benchmark — phải tính từ file JSON.

| ID | Chỉ số | Cách đo | Cột kết quả |
|----|--------|---------|-------------|
| **Q1** | `questions_per_record` mỗi mẫu | `len(questions)` | list 411 giá trị |
| **Q2** | Min / Max / Mean / Median | `describe()` trên Q1 | |
| **Q3** | Histogram phân phối | đếm mẫu có 1, 2, 3, … câu | % mỗi bin |
| **Q4** | Mode (số câu phổ biến nhất) | `value_counts().idxmax()` | |
| **Q5** | Tổng câu flatten | `sum(len(questions))` | đối chiếu **808** |
| **Q6** | Record outlier | `argmax(questions_per_record)` + `record_id` | |
| **Q7** | Liên hệ độ khó | mean `len(idx[i])` theo số câu/mẫu (1 vs 2 vs ≥3) | tùy chọn |

**Công thức kiểm tra:** `sum(Q1) == Q5 == 808` (nếu lệch → báo lỗi parse / file khác bản release).

**Deliverable gợi ý:** 1 biểu đồ bar/histogram `questions_per_record` + 1 dòng tóm tắt:

```text
"Một mẫu trung bình có X câu (P50=Y, max=Z). __% mẫu có đúng 1 câu, __% có 2 câu."
```

---

## 5. Checklist EDA — map theo Challenge (slide 19)

### A. Reasoning Challenges

#### A1. Multi-step inference (nhiều clause)

| ID | Chỉ số | Cách đo |
|----|--------|---------|
| A1.1 | Số premise NL / mẫu | `len(premises-NL)` — đối chiếu ~10.8 |
| A1.2 | Số premise NL **dùng** / câu | `len(idx[q])` |
| A1.3 | Tỷ lệ premise dùng / tổng | `len(idx)/n_premises` |
| A1.4 | Số bước suy luận trong explanation | đếm "Premise N", "step", "→" |
| A1.5 | Số clause if-then trong NL | regex `if.*then` |
| A1.6 | Độ sâu chuỗi (heuristic) | đếm "therefore", "thus", "implies" |

#### A2. Negation & exceptions

| ID | Chỉ số | Cách đo |
|----|--------|---------|
| A2.1 | % premise NL có phủ định | `not`, `never`, `without` |
| A2.2 | % premise FOL có `¬` | |
| A2.3 | % câu hỏi có phủ định | |
| A2.4 | % mẫu có exception | `unless`, `except`, `only if` |

#### A3. No vs Uncertain

| ID | Chỉ số | Cách đo |
|----|--------|---------|
| A3.1 | Phân bố nhãn | Yes / No / Unknown / A–D / khác |
| A3.2 | % Unknown | |
| A3.3 | Unknown theo loại câu | MCQ vs Y/N |
| A3.4 | `len(idx)` theo nhãn | Unknown vs Yes vs No |
| A3.5 | Open-ended / nhãn lạ | answer không chuẩn |

#### A4. So sánh số trong NL

| ID | Chỉ số | Cách đo |
|----|--------|---------|
| A4.1 | % câu có số / so sánh | `\d+`, `more than`, `GPA`, … |
| A4.2 | % premise có ngưỡng | |
| A4.3 | Unknown × có số | cross-tab |

---

### B. Explanation Challenges

#### B1. FOL derivation

| ID | Chỉ số | Cách đo |
|----|--------|---------|
| B1.1 | % mẫu có FOL | đối chiếu 99% |
| B1.2 | Hai notation | `∀x` vs `ForAll(x,` |
| B1.3 | FOL lỗi / encoding | ``, `forall` ASCII |
| B1.4 | `len(NL) == len(FOL)` | |
| B1.5 | Loại FOL | universal / existential / fact |

#### B2. Explanation khớp proof

| ID | Chỉ số | Cách đo |
|----|--------|---------|
| B2.1 | Độ dài explanation (từ) | mean, P50, P90 |
| B2.2 | Theo loại câu | MCQ / Y-N / open |
| B2.3 | Token (Qwen tokenizer) | premise + Q + explanation |
| B2.4 | % vượt 2048 token | |

#### B3. Nhất quán answer ↔ explanation

| ID | Chỉ số | Cách đo |
|----|--------|---------|
| B3.1 | MCQ: option khớp answer | |
| B3.2 | Y/N: kết luận khớp nhãn | |
| B3.3 | Unknown: "cannot determine" | |
| B3.4 | Outlier answer dài | `len(answer) > 20` |

#### B4. Trích dẫn premise (`idx`)

| ID | Chỉ số | Cách đo |
|----|--------|---------|
| B4.1 | `idx` hợp lệ | index ∈ [1, n_premises] |
| B4.2 | Số premise cite trong explanation | regex `Premise (\d+)` |
| B4.3 | Khớp cite vs `idx` | overlap / subset |
| B4.4 | Under-citation / over-citation rate | |

---

### C. Schema & integrity

| ID | Kiểm tra |
|----|----------|
| C1 | 411 record load OK |
| C2 | `len(questions)==len(answers)==len(explanation)==len(idx)` mọi mẫu |
| C3 | `len(premises-FOL)==len(premises-NL)` |
| C4 | Không list rỗng / null |
| C5 | Duplicate question / premise set |

---

### D. Loại câu hỏi

| ID | Kiểm tra |
|----|----------|
| D1 | MCQ: có `A.` / `B.` / "strongest conclusion" |
| D2 | Y/N: "Does it follow" |
| D3 | Đếm theo rule team — đối chiếu 358 / 216 / 234 (có thể chồng loại) |

---

## 6. Liên hệ tiêu chí chấm (slide 12)

| Tiêu chí | EDA hỗ trợ |
|----------|------------|
| **P1 Correctness** | A3, A4, D |
| **P2 Explanation** | B2, B3 |
| **P3 Reasoning depth** | A1, B1, B4, **Q** |

---

## 7. Tóm tắt định lượng (điền sau khi chạy EDA)

```text
- Câu / mẫu: mean=__, P50=__, max=__ (__% mẫu 1 câu, __% 2 câu)
- Premise NL / mẫu: mean=__ (BTC ~10.8)
- Premise dùng / câu Y/N: P50=__, P90=__
- Premise dùng / câu MCQ: P50=__, P90=__
- % Unknown: __
- % explanation cite khớp idx: __
- % mẫu vượt 2048 token: __
```

---

## 8. Quyết định pipeline (sau EDA)

- [ ] Ngưỡng premise tối đa cho context / Z3: ___
- [ ] Xử lý `Unknown`: train / abstain / ___
- [ ] Chuẩn hóa FOL (`∀` vs `ForAll`): ___
- [ ] Format output cite premise: ___

---

## 9. Artifacts cần build (thứ tự)

| # | Artifact | Mô tả |
|---|----------|--------|
| 1 | [`docs/PLAN_EDA_Logic.md`](PLAN_EDA_Logic.md) | File này — plan tổng |
| 2 | `app/notebooks/EDA_Logic_Checklist_TEMPLATE.md` | Bản checklist tick-box (copy từ mục 4–5) |
| 3 | `app/notebooks/02_EDA_Dataset_Logic.ipynb` | Code chạy EDA + plots |
| 4 | `app/figures/EDA_summary_Logic.png` | Figure tổng hợp (optional) |
| 5 | `app/data/processed/logic_flat.csv` | Bảng flatten (optional, sau EDA) |

---

## 10. Gợi ý kỹ thuật (không chạy ngay)

1. **Flatten trước** mọi phân tích nhãn / premise dùng.
2. Slide: loại câu 358+216+234 > 808 → ghi rõ rule phân loại (có thể 1 câu thuộc nhiều loại).
3. Record đầu có FOL encoding lỗi (`forall` thay `∀`) — liệt kê toàn bộ trong B1.3.
4. `idx` là ground truth premise cần dùng — metric B4 quan trọng cho P3.
5. Câu nhiều bước thường đi kèm mẫu 2 câu — xem correlation **Q7** với A1.2.

---

## 11. Tham chiếu schema JSON

```json
{
  "idx": [[1], [7, 10]],
  "premises-FOL": ["∀x ...", "..."],
  "premises-NL": ["If ...", "..."],
  "questions": ["...", "..."],
  "answers": ["Unknown", "Yes"],
  "explanation": ["...", "..."]
}
```

---

*Cập nhật lần cuối: theo workshop EXACT 2026 (May 2026). Chưa thực hiện EDA trên dữ liệu thật.*
