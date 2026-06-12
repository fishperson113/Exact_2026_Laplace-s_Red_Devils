# Logic Based Educational Queries — Solution (Team Laplace's Red Devils)

Giải pháp EXACT 2026 cho bài toán **Logic Based Educational Queries**: từ tiền đề ngôn ngữ tự nhiên (NL) + câu hỏi → suy luận theo logic bậc nhất (FOL) → đáp án + giải thích.

Kiến trúc gồm **2 model fine-tune nối tiếp**, huấn luyện theo **curriculum 2 giai đoạn** và tăng cường dữ liệu (data augmentation) ở cả hai khâu:

```text
                ┌──────────────────────────────────────────────────────────────┐
                │                      TỔNG QUAN GIẢI PHÁP                       │
                └──────────────────────────────────────────────────────────────┘

  Model 1 — FOL Translator                          Model 2 — QA CoT Reasoner
  (NL premises → premises_fol)                      (NL + FOL + question → reasoning → answer)
  Qwen3.5-4B + LoRA                                 Qwen3.5-4B + LoRA

  ┌───────────────┐   pretrain   ┌───────────────┐   SFT        ┌───────────────┐   SFT
  │  MALLS 28K    │ ───────────▶ │  Stage 1:     │ ───────────▶ │  Stage 2:     │       │
  │ (augmented)   │   5K random  │  FOL pretrain │  target ~630 │  FOL fine-tune│       ▼
  └───────────────┘              └───────────────┘              └───────────────┘   QA CoT model
                                                                                     (reasoning
                                                                  ▲                   augmented bằng
                                                                  │                   Claude Sonnet 4.6)
                                                       Data augmentation Stage 2
                                                       (reasoning steps theo FOL)
```

**Diễn giải:** Model 1 học dịch câu chữ (NL) sang công thức logic (FOL); Model 2 đọc công thức logic đó để suy luận ra đáp án kèm giải thích. Mỗi model được huấn luyện riêng, rồi nối lại thành một dây chuyền khi trả lời thực tế.

> **Nguyên tắc cốt lõi — train trên GOLD FOL, chỉ ghép khi inference:** Cả hai model được **huấn luyện ĐỘC LẬP trên GOLD FOL** của ban tổ chức (teacher forcing). Cụ thể, Model 2 (QA) được train với trường `premises_fol` là **FOL chuẩn (gold)** trong dữ liệu, **KHÔNG phải** FOL do Model 1 dự đoán. **Chỉ ở bước inference**, hai model mới được **ghép nối tiếp**: Model 1 sinh FOL → đưa FOL đó cho Model 2. Cách tách biệt này tránh để sai số của Model 1 lan vào quá trình train Model 2 (mỗi model học từ tín hiệu sạch nhất).

> Vì sao 2 giai đoạn (cho Model 1)? MALLS có ~28K cặp NL→FOL còn bộ chính thức chỉ ~630 record (ratio ~88:1). Gộp 1 lần sẽ khiến dữ liệu target "chìm" → pretrain trên MALLS để model nắm **cú pháp FOL tổng quát** trước, rồi fine-tune trên target để học **format JSON / multi-premise / cách đặt tên** của ban tổ chức.

---

## Flow A — Data Augmentation cho Pretrain FOL (MALLS)

**Mục tiêu:** chuẩn hoá bộ ngoài MALLS-v0.1 về đúng format target và gộp lại làm dữ liệu warmup cho Stage 1.

Notebook: [`notebooks/prepare_augmented_data.ipynb`](notebooks/prepare_augmented_data.ipynb) · Loader: [`src/data/fol_dataset.py`](src/data/fol_dataset.py)

```text
  MALLS-v0.1-train.json (27K)   MALLS-v0.1-test.json (1K)
            │                            │
            └──────────────┬─────────────┘
                           ▼
              ┌──────────────────────────┐
              │ Chuẩn hoá về format target│   {NL, FOL}  →  {premises_nl:[NL], premises_fol:[FOL]}
              │ - constants: lower→Capital │   normalize_malls_constants()
              │ - lọc len(NL)==len(FOL)>0  │
              └─────────────┬─────────────┘
                            ▼
              ┌──────────────────────────┐
              │  GỘP train + test         │   → data/processed/malls_v01_normalized.json  (28,284 mẫu)
              │  thành 1 file duy nhất     │
              └─────────────┬─────────────┘
                            ▼
              shuffle(seed=3407) → lấy RANDOM 5,000 mẫu
              (cân bằng chi phí huấn luyện + giữ tính khách quan; đặt null = dùng cả ~27K)
```

**Diễn giải:** Bước này lấy một bộ dữ liệu NL→FOL có sẵn bên ngoài (MALLS), chỉnh về cùng định dạng với dữ liệu cuộc thi, gộp lại và rút gọn còn 5.000 mẫu để "dạy vỡ lòng" cho model cách viết FOL trước khi vào dữ liệu chính.

**Vì sao gộp train+test rồi lấy random 5K:** Stage 1 chỉ là *warmup* để model "hiểu FOL", **không đo hiệu suất** ở giai đoạn này (metric cuối được đo ở Stage 2 trên target). Gộp cả 2 split tránh thiên lệch theo một phân phối split, còn lấy ngẫu nhiên 5K (thay vì toàn bộ 28K) để **cân bằng chi phí GPU** mà vẫn đủ đa dạng — việc lấy mẫu ngẫu nhiên có seed cố định đảm bảo tái lập và khách quan.

---

## Flow B — Pretrain FOL (Stage 1) trên MALLS

Script: [`src/models/fol_model/pretrain.py`](src/models/fol_model/pretrain.py) · Config: [`configs/fol_pretrain.yaml`](configs/fol_pretrain.yaml) · Chạy: `cd src && python -m models.fol_model.pretrain`

```text
  malls_v01_normalized.json ──(random 5K, seed 3407)──▶ Qwen3.5-4B + LoRA
            │                                                   │  Unsloth + TRL SFTTrainer
            │                                                   │  train_on_responses_only (loss CHỈ trên FOL)
            │                                                   ▼
            │                                          LoRA adapter (pretrain_lora)
            │                                                   │  merge LoRA vào base
            ▼                                                   ▼
       Stage 2 (Flow B-2)  ◀──── push HF Hub: Laplaces-Red-Devils/fol-pretrain-malls-qwen3.5-4b
```

**Diễn giải:** Giai đoạn 1 (pretrain) — Qwen3.5-4B gắn LoRA, luyện trên 5.000 mẫu MALLS để nắm cú pháp FOL tổng quát. Kết quả được đẩy lên Hugging Face Hub làm điểm khởi đầu cho giai đoạn 2.

| Nhóm | Tham số | Giá trị |
|---|---|---|
| **Model** | base / max_seq_len / gen_max_new_tokens | `Qwen/Qwen3.5-4B` / 3500 / 512 |
| **LoRA** | r / alpha / dropout | 8 / 16 / 0.05 |
| **Data** | nguồn / giới hạn train / dev | MALLS gộp / **5,000 random (seed 3407)** / *không tách dev, eval tắt* |
| **Train** | epochs / LR / warmup / weight_decay | 3 (cố định, no early-stop) / 2e-4 / 0.05 / 0.01 |
| | batch | 2 × grad_accum 4 → **effective 8** |
| | precision / quantization / optimizer | bf16 + grad checkpointing / load_in_8bit / AdamW 8-bit |
| | seed / đặc thù Unsloth | 3407 / `train_on_responses_only` |

Output: merge LoRA + push Hub làm **base model cho Stage 2**.

---

## Flow B-2 — Fine-tune FOL (Stage 2) trên bộ chính thức

Script: [`src/models/fol_model/train.py`](src/models/fol_model/train.py) · Config: [`configs/fol_model.yaml`](configs/fol_model.yaml) · Chạy: `make train-fol`

Base model = checkpoint pretrain trên Hub (KHÔNG phải Qwen gốc). Train trên `data/processed/{train,dev,test}.csv` (bộ chính thức của ban tổ chức), lọc giữ record có `len(premises_nl)==len(premises_fol)>0`. Mục tiêu (target) khi train là **GOLD `premises_fol`** của ban tổ chức — model học `premises_nl → gold premises_fol`.

| Nhóm | Tham số | Giá trị |
|---|---|---|
| **Model** | base | `Laplaces-Red-Devils/fol-pretrain-malls-qwen3.5-4b` |
| **LoRA** | r / alpha / dropout | 8 / 16 / 0.08 |
| **Train** | epochs / LR / warmup | 25 / 3e-5 (thấp hơn Stage 1 để không "quên" MALLS) / 0.05 |
| | batch / precision / quant | eff. 8 (2×4) / bf16 / load_in_8bit + Unsloth |
| | early stopping | patience 5 trên dev, `load_best_model_at_end` |
| **Best model** | metric | **`eval_rm_score`** (xem dưới), greater_is_better |

### Metric chọn best model: RM (Reasoning Match)

Thay cho exact-match (quá khắt khe: `∀x (A→B)` vs `∀x (¬B→¬A)` tương đương logic nhưng bị tính sai), Stage 2 chọn best model theo **RM (Reward Model)** của LogicLLaMA.

> **Nguồn:** Yang, Xiong, Payani, Shareghi, Fekri — *"Harnessing the Power of Large Language Models for Natural Language to First-Order Logic Translation"* (arXiv:2305.15541, ACL 2024) — bài báo giới thiệu **MALLS** + **LogicLLaMA**. Công thức nằm ở **§4.2.3 "FOL evaluation and reward design"**, đoạn *Reward design*:
>
> ```
> RM(x_FOL, x'_FOL) = ω · LE(R, R') + (1 − ω) · BLEU(x_FOL, x'_FOL)
> ```
>
> Paper đặt **ω = 0.7**. Bản triển khai của nhóm dùng **ω = 0.6** (`rm_le_weight: 0.6`, `rm_bleu_weight: 0.4` trong `fol_model.yaml`) — nâng nhẹ trọng số BLEU để ổn định việc chọn best model trên bộ target nhỏ.

```text
   RM = 0.6 × LE  +  0.4 × FOL-BLEU
        │              │
        │              └─ FOL BLEU-4: n-gram overlap giữa gold & predicted FOL
        │                 (tokenize theo ký hiệu ∀ ∃ → ¬ ∧ ∨ ↔ + predicate)
        └─ LE (Logical Equivalence) qua Z3: gold ↔ pred là tautology?
           parse FOL → Z3 expr → check Not(gold==pred) == unsat → LE=1, ngược lại 0
           (parse fail / timeout → LE=0, RM vẫn có BLEU làm fallback)
```

**Diễn giải:** Thay vì bắt model viết FOL giống hệt đáp án mẫu, ta chấm bằng RM: phần lớn điểm dựa trên "có tương đương logic không" (LE — kiểm bằng solver Z3), phần còn lại dựa trên độ giống chữ (BLEU). Nhờ vậy một công thức viết khác nhưng đúng logic vẫn được điểm cao, giúp chọn được model tốt nhất công bằng hơn.

Code: [`src/evaluation/fol_rm.py`](src/evaluation/fol_rm.py), [`fol_le.py`](src/evaluation/fol_le.py), [`fol_bleu.py`](src/evaluation/fol_bleu.py), [`fol_z3_translator.py`](src/evaluation/fol_z3_translator.py). Trọng số chỉnh tại `rm_le_weight` / `rm_bleu_weight`; tính RM mỗi epoch trên tối đa `best_model_rm_max_samples` (mặc định 50) mẫu dev cho nhanh.

Sau train: merge LoRA + push Hub, tải lại merged từ Hub và greedy trên N mẫu test ngẫu nhiên (`hub_reload_random_test_n`).

---

## Flow C — Data Augmentation cho QA Stage 2 (reasoning steps theo FOL)

**Mục tiêu:** bổ sung **chuỗi suy luận FOL (chain-of-thought)** vào dữ liệu QA để Model 2 học *reason theo FOL trước, chốt answer sau* — thay vì đoán đáp án.

Script: [`src/data/build_reasoning_dataset.py`](src/data/build_reasoning_dataset.py) · Model augmentation: **Claude Sonnet 4.6** (`claude-sonnet-4-6`)

```text
  Phase 1 — DETERMINISTIC (không gọi API)
  ────────────────────────────────────────
  1 record (premise set) ──flatten──▶ N rows (1 row / câu hỏi)
        giữ record_id + q_idx (split theo record để tránh leak)
        premises_used: 1-based → 0-based
        used_fol = [premises_fol[i] for i in premises_used]
        → rows đã flatten (chưa có reasoning)

  Phase 2 — CLAUDE SONNET 4.6 (sinh reasoning + validate)
  ────────────────────────────────────────
  với mỗi row, đưa cho Claude:  used_fol + question + correct answer + explanation
        │
        ▼  prompt yêu cầu sinh JSON {"steps": [...]} theo taxonomy:
        │     "Rule:"       luật điều kiện/lượng từ — TỪ used_fol
        │     "Fact:"       sự kiện cụ thể        — TỪ used_fol
        │     "Derive:"     suy luận trung gian (contrapositive, modus ponens, so sánh số…)
        │     "Conclusion:" đúng 1, đứng CUỐI, khớp correct answer
        ▼
  Tự kiểm tra (validate): mỗi bước đúng format · có đúng 1 Conclusion ở cuối ·
                          không bịa ra công thức ngoài các premise đã cho
        ▼
  → bộ dữ liệu Stage 2 đã augment với field "reasoning" = {"type": "fol", "steps": [...]}
```

**Diễn giải:** Pha 1 tách mỗi câu hỏi thành một dòng riêng (chưa có lời giải). Pha 2 nhờ **Claude Sonnet 4.6** viết chuỗi suy luận từng bước dựa trên các công thức FOL + lời giải thích mẫu, rồi tự kiểm tra để loại các bước sai/bịa trước khi thêm vào bộ dữ liệu Stage 2.

**Căn cứ sinh reasoning (trích prompt `build_reasoning_dataset.py`):** mỗi step được suy ra từ **các premise FOL đã dùng (`used_fol`)** + **explanation gốc** + **correct answer** — Claude không được bịa predicate ngoài `used_fol`, và `Conclusion:` phải khớp đáp án đúng.

```text
SYSTEM (rút gọn):
  "You are given: a list of FOL premises that ARE USED to answer a question,
   the question, the correct answer, and a prose explanation of why it is correct.
   Produce a step-by-step FOL derivation ... EVERY step starts with:
     Rule:  / Fact:  → MUST come from one of the given USED premises
     Derive:        → suy luận trung gian (contrapositive, modus ponens, so sánh số…)
     Conclusion:    → đúng 1, đứng CUỐI, MUST logically correspond to the correct answer
   Rule/Fact steps must paraphrase the GIVEN used premises only (do not invent predicates)."

USER (template):
  USED PREMISES (FOL):   {used_fol}     ← các premise FOL được dùng để trả lời
  QUESTION:              {question}
  CORRECT ANSWER:        {answer}       ← chốt Conclusion phải khớp
  EXPLANATION:           {explanation}  ← căn cứ suy luận
  Return JSON: {"steps": [...]}
```

> Lưu ý: prompt cấp cho Claude là **bản FOL của các premise đã dùng (`used_fol`)** chứ không phải NL gốc — để chuỗi suy luận thao tác trực tiếp trên công thức FOL; `explanation` (prose) + `answer` là hai căn cứ ràng buộc tính hợp lệ. `validate_steps()` sau đó kiểm tra predicate trong Rule/Fact phải truy về được `used_fol` (chống bịa).

**Các trường bổ sung vào tập train/dev/test** (export qua `notebooks/eda_reasoning_flat.ipynb` → `data/processed/*.csv`):

| Trường | Nguồn | Ý nghĩa |
|---|---|---|
| `premises_used` | Phase 1 | chỉ số 0-based các premise được dùng để trả lời |
| `reasoning` = `{type, steps}` | Phase 2 (Claude Sonnet 4.6) | chuỗi suy luận `Rule:/Fact:/Derive:/Conclusion:` đã validate |

> `used_fol` chỉ là biến **trung gian trong Phase 1** để dựng prompt cho Claude (gom các công thức FOL theo `premises_used`), **không** được ghi vào CSV train/dev/test.

### Train QA Stage 2 (CoT Reasoner)

Script: [`src/models/QA_model/train.py`](src/models/QA_model/train.py) · Prepare: [`src/models/QA_model/prepare_data.py`](src/models/QA_model/prepare_data.py) · Config: [`configs/qa_model.yaml`](configs/qa_model.yaml)

> **Nhắc lại — train trên GOLD FOL:** input lúc train chứa `premises_fol` là **FOL chuẩn (gold)** từ CSV của ban tổ chức, **không phải** FOL do Model 1 sinh. Model 2 chỉ "gặp" FOL của Model 1 ở bước inference (mục dưới).

Target của model = `reasoning.steps` (mỗi dòng 1 step) **rồi dòng cuối là JSON với `answer` ĐỨNG CUỐI**:

```text
  System: vai trò QA logic, quy ước đọc options + format step Rule/Fact/Derive/Conclusion
  User:   Premises (NL) + Premises (FOL) + Options + Question
  Asst:   Rule: ...                              ← reasoning steps (CoT theo FOL)
          Fact: ...
          Derive: ...
          Conclusion: ...
          {"premises_used": [...], "explanation": "...", "answer": "..."}   ← answer LAST
```

**Diễn giải:** Model 2 được dạy "suy luận trước, chốt đáp án sau": xuất các bước Rule/Fact/Derive/Conclusion rồi mới đến dòng JSON chứa đáp án ở cuối — để đáp án là kết quả của suy luận chứ không phải đoán.

| Nhóm | Tham số | Giá trị |
|---|---|---|
| **Model** | base / max_seq_len / gen_max_new_tokens | `Qwen/Qwen3.5-4B` / 3000 / 1000 (answer ở cuối → cần rộng) |
| **LoRA** | r / alpha / dropout / target_modules | 8 / 16 / 0.05 / q,k,v,o_proj |
| **Train** | epochs / LR / batch | 10 / 2e-5 / eff. 8 (2×4) |
| | loss | `completion_only_loss` (chỉ tính loss trên phần assistant) |
| | early stopping | patience 4 theo **`eval_accuracy`** trên dev, `load_best_model_at_end` |
| | precision / quant / seed | bf16 + grad checkpointing / load_in_8bit / 42 |

---

## Inference — Ensemble Pipeline

Script: [`src/models/Ensemble_Model/inference.py`](src/models/Ensemble_Model/inference.py) · Config: [`configs/ensemble_model.yaml`](configs/ensemble_model.yaml)

Hai model nối tiếp: Model 1 dịch NL→FOL, Model 2 nhận NL + FOL (do Model 1 sinh) + câu hỏi → reasoning + đáp án.

> **Đây là điểm KHÁC với lúc train:** ở train, Model 2 dùng GOLD FOL của ban tổ chức (teacher forcing); ở inference, Model 2 dùng **FOL do Model 1 dự đoán**. Hai model được huấn luyện riêng rồi mới ghép tại đây.

```text
  premises_nl + question
        │
        ▼
  ┌──────────────────────┐   {"premises_fol": ["∀x ...", ...]}
  │ Model 1 — FOL (Hub)  │ ─────────────────────────────────┐
  │ Qwen3.5-4B + LoRA    │                                   │
  └──────────────────────┘                                   ▼
                                              ┌──────────────────────────┐
                                              │ Model 2 — QA CoT (LoRA)  │
       premises_nl + question ───────────────▶│ reason theo FOL → JSON   │
                                              └─────────────┬────────────┘
                                                            ▼
                                          {premises_used, explanation, answer}
```

**Diễn giải:** Khi trả lời thật, câu hỏi đi qua Model 1 để ra công thức FOL, rồi cả NL lẫn FOL được đưa sang Model 2 để suy luận ra đáp án và giải thích cuối cùng. Hỗ trợ 2 chế độ: *evaluate* (có đáp án mẫu → tính accuracy) và *inference* (không có đáp án → chỉ sinh kết quả).

---

## Bản inference đóng gói — folder `logic_solution/`

Để ban tổ chức chạy trực tiếp mà **không phụ thuộc mã huấn luyện**, toàn bộ pipeline inference (Model 1 → Model 2) đã được **gói gọn vào một folder self-contained `logic_solution/`** (trong repo: `app/logic_solution/`). Chỉ cần một entry point `run.py`: đọc file input theo định dạng BTC → ghi file output theo Unified Output Schema BTC.

```text
logic_solution/
├── run.py              # entry point duy nhất: input BTC → output BTC
├── config.yaml         # chọn 2 model trên Hub + token limit + chế độ decode
├── prompts/prompt.py   # prompt 2 stage — ĐỒNG BỘ 1:1 (byte-identical) với prompt lúc train
├── pipeline/
│   ├── fol_model.py    # Stage 1: NL → FOL
│   ├── qa_model.py     # Stage 2: NL + FOL + question → reasoning + answer
│   └── ensemble.py     # nối 2 stage thành 1 pipeline
└── parsing.py          # bóc JSON (premises_fol / answer) từ output model
```

**Đảm bảo nhất quán train ↔ inference (đã đối chiếu):**

| Hạng mục | Trạng thái |
|---|---|
| Prompt FOL & QA | **Trùng từng byte** với prompt lúc train (`SYSTEM_PROMPT_FOL == SYSTEM_PROMPT_FOL_SFT`, `SYSTEM_PROMPT_QA == SYSTEM_PROMPT_QA_COT`) |
| Ràng buộc `n` NL → đúng `n` FOL, cùng thứ tự | Có sẵn trong prompt FOL của gói → giữ alignment chỉ số `premises_used` |
| Decode | Greedy + no-think — khớp flow Ensemble lúc train/eval |
| Model triển khai | FOL `Laplaces-Red-Devils/fol-v06-cot-augmented-...-qwen3.5-4` · QA `Laplaces-Red-Devils/v04-QA-CoT` (load từ Hub) |
| Input / Output | Đúng schema BTC: input 5 trường (`query_id/type/query/premises/options`) → output 6 trường (`query_id/answer/unit/explanation/premises_used/reasoning`) |

**Diễn giải:** Đây là bản "đóng hộp" của đúng pipeline ở trên để nộp/triển khai. Vì prompt và chế độ giải mã được giữ **y hệt lúc huấn luyện**, model gặp đúng phân phối dữ liệu nó từng học → tránh tụt chất lượng do lệch prompt.

```bash
cd logic_solution
python run.py --input data/sample_input.json --output outputs/results.json
```

---

## Chuẩn bị môi trường & chạy nhanh

```bash
cd Logic_Based_Educational_Queries_Project
python -m venv .venv && .venv\Scripts\activate      # Windows
pip install -r requirements.txt && pip install -e .
cp .env.example .env                                 # điền HF_TOKEN
```

| Lệnh | Ý nghĩa |
|------|---------|
| `make data` | Export `data/processed/*.csv` (+ split metadata) |
| `python -m models.fol_model.pretrain` | Stage 1 — pretrain FOL trên MALLS 5K (Flow B) |
| `make train-fol` | Stage 2 — fine-tune FOL trên target + RM metric + push Hub (Flow B-2) |
| Augment reasoning (Flow C) | Sinh chuỗi suy luận cho Stage 2 bằng **Claude Sonnet 4.6** |
| `python -m models.QA_model.train --config configs/qa_model.yaml` | Train QA CoT Stage 2 |
| `python -m models.Ensemble_Model.inference ...` | Inference end-to-end |

> Siêu tham số nằm ở `configs/*.yaml` (file theo Git); secret (`HF_TOKEN`) chỉ đặt trong `.env` — **không commit**.

---

## Cấu trúc thư mục (rút gọn)

```text
configs/                 # fol_pretrain.yaml · fol_model.yaml · qa_model.yaml · ensemble_model.yaml
data/
├── external/MALLS-v0/   # bộ ngoài MALLS-v0.1 (train + test)
├── processed/           # *.csv (target) + malls_v01_normalized.json (augmented) + qa reasoning
└── raw/                 # JSON gốc của ban tổ chức
src/
├── data/                # fol_dataset.py · build_reasoning_dataset.py (augment) · prompts.py
├── evaluation/          # fol_rm.py · fol_le.py (Z3) · fol_bleu.py · fol_z3_translator.py
└── models/
    ├── fol_model/       # pretrain.py (Stage 1) · train.py (Stage 2) · RM eval
    ├── QA_model/        # prepare_data.py · train.py (CoT Stage 2)
    └── Ensemble_Model/  # inference.py (FOL → QA)
notebooks/               # prepare_augmented_data.ipynb · eda_reasoning_flat.ipynb · *_pipeline_official.ipynb
docs/                    # DESIGN_FOL_RM_AND_STAGE2.md · PRETRAIN_MALLS_SUMMARY.md
```
