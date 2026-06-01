# Hướng dẫn Fine-tune v06 — CPT + Sinh code + SFT cho Qwen 3.5 4B

> **Mục đích:** Hướng dẫn quy trình fine-tune mô hình cho v06, từ dữ liệu thô đã sẵn sàng đến model biết tự sinh code Python giải vật lý.
> **Khác gì `UNSLOTH_GUIDE.md`?** File đó dạy *cơ chế* Unsloth (cài đặt, LoRA, export). File này dạy *chiến lược cụ thể của dự án*: dùng data nào, theo trình tự nào, hyperparameter nào, đánh giá ra sao so với v05_best.
> **Dành cho:** đội Model (nhánh `Nguyen/v06_finetune`).

---

## 0. TL;DR — Đọc 1 phút

```
Data ĐÃ SẴN SÀNG (không phải đi cào nữa):
  • CPT corpus  → data/pretrain_processed/lop-*.md   (2.261 lời giải tiếng Việt)
  • Golden CoT  → app/physics_solution/data/golden/deepseek-v4-pro_golden_data.csv (1.352 dòng)

Pipeline v06:
  Giai đoạn 0  CPT (tùy chọn)   → tăng nền tảng lập luận vật lý tiếng Việt
  Giai đoạn 1  Sinh code        → DeepSeek viết Python cho 1.352 câu, chạy + verify
  Giai đoạn 2  Xử lý data       → lọc, chia train/val (val PHẢI có 60 câu golden)
  Giai đoạn 3  SFT              → Unsloth/QLoRA, base = CPT hoặc Qwen gốc
  Giai đoạn 4  Đánh giá         → so với v05_best (58.3%), mục tiêu >70%

Bài học sống còn từ v05: 4B chỉ thắng khi code NGẮN, TRỰC TIẾP. Đừng train kiểu
SETUP + lý luận LaTeX dài — budget token quá nhỏ, model sẽ timeout.
```

---

## 1. Bối cảnh & mục tiêu

Hiện tại pipeline **v05_best** dùng prompt đơn giản (~1.200 ký tự) + 1 ví dụ code inline để ép Qwen 3.5 4B sinh Python → chạy → parse đáp số. Kết quả: **35/60 = 58.3%** trên golden tĩnh điện.

**Mục tiêu v06:** fine-tune để model **tự nội hoá** phong cách sinh code của v05_best, nhờ đó:
- Bỏ được ví dụ inline + prompt dài → tiết kiệm token → ít timeout hơn.
- Sinh code đúng hơn ở các domain khó (tĩnh điện có hình học vector).
- Đẩy golden từ 58.3% lên **>70%**.

Hai đòn bẩy:
1. **CPT (Continue Pre-Training):** học thêm "kiến thức thô" vật lý tiếng Việt từ 2.261 lời giải → lập luận tốt hơn.
2. **SFT (Supervised Fine-Tuning):** học chính xác mẫu input→code Python từ data DeepSeek sinh ra.

---

## 2. Bản đồ dữ liệu (đã có sẵn trong repo)

### 2.1 CPT corpus — `data/pretrain_processed/`
- **2.261 lời giải chất lượng cao** (lọc từ 74.807 mẫu thô, giữ lại 3.02%).
- Nguồn: Vietjack, lớp 6–12, bài tự luận có lời giải. Đã loại câu phụ thuộc hình/đồ thị/bảng và rác trắc nghiệm.
- File theo lớp: `lop-6_high_quality.md` … `lop-12_high_quality.md`. Catalog: `DATA_CATALOG.md`.
- Định dạng: mỗi bài là 1 block `## Problem` → `**Question:**` → `### Solution`.
- **Lưu ý chọn lát:** chỉ **lớp 11 (270)** + **lớp 12 (1.130)** sát domain thi (điện học). Lớp 6–10 phần lớn lệch chủ đề → có thể bỏ hoặc giảm trọng số. (Riêng đo lường/mạch DC ở lớp 9–10 thì trùng domain THCB, giữ lại được.)

### 2.2 Golden CoT — `app/physics_solution/data/golden/deepseek-v4-pro_golden_data.csv`
- **1.352 dòng**: `id, question, cot, answer, unit`. Đây là input cho Giai đoạn 1.
- Phân bố domain (theo prefix `id`) — **trải cả lớp 11 và lớp 12, KHÔNG chỉ lớp 11**:

| Domain (prefix) | Số dòng | Chủ đề | Lớp |
|---|---|---|---|
| LD + DT | 465 | Điện tích, điện trường, lực Coulomb | 11 |
| TD | 177 | Tụ điện | 11 |
| THCB | 80 | Sai số phép đo, mạch DC | 10–11 |
| CH + CHLT | 310 | Mạch RLC, dòng xoay chiều | 12 |
| NL | 190 | Năng lượng tụ/cuộn, dao động LC | 12 |
| DDT | 130 | Cảm ứng điện từ, ống dây | 11–12 |

→ Lớp 11 ≈ 722 dòng (53%), lớp 12 ≈ 630 dòng (47%).

### 2.3 Loại đáp án (answer type) — phải xử lý hết khi sinh code
numeric (~72%), sci_notation (~17.5%), text (~3.7%), mixed (~2.7%), multi_value (~1.9%), yes_no (~1.6%).

---

## 3. Giai đoạn 0 — CPT (tùy chọn nhưng nên thử)

> Mục tiêu: cho model "ngấm" cách lập luận vật lý tiếng Việt trước khi học sinh code.

1. **Gộp corpus:** nối `data/pretrain_processed/lop-11_high_quality.md` + `lop-12_high_quality.md` (và phần THCB của lớp 9–10 nếu muốn) thành 1 file text. Mỗi block `## Problem` là một "document".
2. **Pack sequence:** tokenize bằng tokenizer Qwen, gom thành chuỗi ~2.048 token, objective causal LM thường (không mask gì cả).
3. **Train nhẹ với Unsloth:** LoRA trên tập module rộng hơn SFT, **LR thấp (~5e-5 → 1e-4)**, **1 epoch** thường đủ với ~1.400 mẫu. Đây là warm-up, không phải sự kiện chính → giữ rẻ.
4. **Lưu weights** làm BASE cho Giai đoạn 3.
5. **A/B bắt buộc:** nếu CPT base **không** cải thiện golden so với Qwen gốc → **bỏ CPT**, SFT thẳng từ stock. Đừng cố giữ một bước không có tác dụng.

---

## 4. Giai đoạn 1 — Sinh data code bằng DeepSeek V4 Pro

> Mục tiêu: với mỗi trong 1.352 câu, có 1 đoạn Python NGẮN, ĐÚNG, đã verify.

1. **API:** DeepSeek V4 Pro đã cấu hình trong `config.py` (`COMMERCIAL_PROVIDER="deepseek"`, `COMMERCIAL_MODEL="deepseek-v4-pro"`, key trong env `DEEPSEEK_API_KEY`). Có thể chỉnh từ `shared/eval/gen_golden.py` (đã có async batch call).
2. **Yêu cầu code DeepSeek sinh ra** (đúng phong cách v05_best):
   - Chỉ `import math / sympy / numpy` hoặc `from scipy import constants`.
   - Khai báo mọi giá trị đầu bài ở đầu, **đổi sang đơn vị SI**.
   - Comment công thức trước mỗi phép tính.
   - In đúng `FINAL ANSWER: <value>` và `UNIT: <unit>`.
   - **Hằng số hardcode** (`k = 9e9`, `epsilon_0 = 8.854e-12`…) — tin cậy hơn import với model 4B.
   - **NGẮN: 15–30 dòng**, không phải 50+.
3. **Execute + verify:** chạy code bằng `versions/v05_best/code_executor.py` (subprocess, timeout 10s, chỉ cho phép import an toàn), so đáp số với gold bằng `shared/eval/scorer.py`.
4. **Retry thông minh:** nếu code lỗi hoặc đáp số sai → feed lại lỗi cho DeepSeek thử lại 1 lần (như v05_best làm).
5. **Gắn cờ** các câu sai không sửa được → review tay (đừng đưa rác vào training set).
6. **Output mỗi dòng:** `(question, domain, answer_type, formula_hints, python_code, answer, unit)` đã verify đúng.

> Lưu ý domain khó: **LDDT (tĩnh điện)** dễ sai setup toạ độ + phân tích vector. Đây là 9/25 lỗi ZERO_ANSWER của v05_best → ưu tiên chất lượng code ở domain này.

---

## 5. Giai đoạn 2 — Xử lý & chia data

1. **Validate lại toàn bộ:** chỉ giữ dòng mà code chạy được và đáp số khớp gold.
2. **Chia stratified theo CẢ domain VÀ answer_type:**
   - Train ~90% (oversample domain hiếm, vd CHLT chỉ 20 dòng).
   - Val ~10% — **bắt buộc chứa đủ 60 câu golden** để so trực tiếp với v05_best.
3. **Convert sang Qwen chat template:**
   - **System:** CODEGEN_SYSTEM rút gọn — **bỏ ví dụ inline** (model sẽ tự học mẫu).
   - **User:** `DOMAIN: {domain}\nANSWER TYPE: {answer_type}\nREFERENCE:\n{formula_hints}\nPROBLEM:\n{question}\nWrite a Python script to solve this.`
   - **Assistant:** đoạn Python đã verify (output DeepSeek).

---

## 6. Giai đoạn 3 — SFT với Unsloth/QLoRA

> Cơ chế cài đặt Unsloth chi tiết: xem `UNSLOTH_GUIDE.md`. Dưới đây là cấu hình riêng cho v06.

- **Base model:** weights CPT (nếu CPT có ích) hoặc `Qwen/Qwen3.5-4B` gốc.
- **Phương pháp:** LoRA/QLoRA 4-bit.
- **Tham số khởi điểm (tune sau):**

| Tham số | Giá trị bắt đầu | Ghi chú |
|---|---|---|
| LoRA rank `r` | 16 | tăng 32 nếu underfit |
| `lora_alpha` | 16–32 | ~ bằng `r` |
| learning rate | 2e-4 | SFT |
| epochs | 3 | theo dõi val, dừng sớm nếu overfit |
| max_seq_len | 2048 | đủ cho code ngắn |
| batch (effective) | 16–32 | dùng grad accumulation |
| `repetition_penalty` (inference) | 1.15 | phá vòng lặp degenerate |

- **Bài học sống còn:** train trên code **NGẮN, TRỰC TIẾP**. KHÔNG train mẫu SETUP + lý luận LaTeX dài → 4B sẽ ngốn hết token rồi timeout (đúng lỗi prompt ToRA: 48.3%, 23 timeout).

---

## 7. Giai đoạn 4 — Inference & đánh giá

1. **Pipeline inference:** copy từ `versions/v05_best/run.py`, giữ nguyên:
   - Logic retry-on-error.
   - Inject formula hints theo domain (từ `formulas.yaml`) — **vẫn cần** lúc inference.
   - Code execution + scoring.
   - Chỉ khác: **system prompt ngắn hơn** (bỏ ví dụ inline).
2. **Đánh giá:** chạy 60 câu golden, so với v05_best.
   - Baseline: **35/60 = 58.3%**.
   - **Mục tiêu: >70%** (>42/60).
   - So thêm: số timeout (v05_best = 3), số `failed` (v05_best = 5).

---

## 8. Checklist

- [ ] Giai đoạn 0: gộp corpus lớp 11+12 → CPT → A/B vs stock → quyết định giữ/bỏ
- [ ] Giai đoạn 1: sinh code DeepSeek cho 1.352 câu, execute + verify, retry, gắn cờ lỗi
- [ ] Giai đoạn 2: lọc dòng đúng, chia stratified, val chứa 60 golden, convert chat template
- [ ] Giai đoạn 3: SFT Unsloth (base CPT/stock), theo dõi val loss
- [ ] Giai đoạn 4: inference prompt ngắn, đo golden, so v05_best, mục tiêu >70%
- [ ] Export HF-compatible (vLLM production) — xem `UNSLOTH_GUIDE.md`

---

## 9. File tham chiếu

| File | Vai trò |
|---|---|
| `data/pretrain_processed/` + `DATA_CATALOG.md` | Corpus CPT (đã sẵn sàng) |
| `app/physics_solution/data/golden/deepseek-v4-pro_golden_data.csv` | Input sinh code (1.352 dòng) |
| `versions/v05_best/prompts.py` | CODEGEN_SYSTEM gốc cần rút gọn |
| `versions/v05_best/code_executor.py` | Execute + parse đáp số |
| `versions/v05_best/formula_kb.py` + `input/formulas.yaml` | Formula hints theo domain |
| `versions/v05_best/run.py` | Pipeline mẫu để adapt |
| `shared/eval/scorer.py` | Chấm điểm đa loại đáp án |
| `shared/eval/gen_golden.py` | Async batch call DeepSeek (adapt được) |
| `config.py` | API DeepSeek, model ID (`Qwen/Qwen3.5-4B`) |
| `docs/guides/UNSLOTH_GUIDE.md` | Cơ chế Unsloth/LoRA/export |
| `docs/guides/PRETRAIN_DATA_GUIDE.md` / `DATA_COLLECTION_GUIDE.md` | Cách data được thu thập |
| `app/physics_solution/versions/v06_finetune/V06_HANDOFF_PROMPT.md` | Handoff đầy đủ |
