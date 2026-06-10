# Tóm tắt Pretrain Stage 1 — MALLS (NL → FOL)

> Nguồn cấu hình: [`configs/fol_pretrain.yaml`](../configs/fol_pretrain.yaml) · Script: [`src/models/fol_model/pretrain.py`](../src/models/fol_model/pretrain.py)

## 1. Bộ dữ liệu được chọn — MALLS

**MALLS** (*large language **M**odel gener**A**ted natural-**L**anguage-to-first-order-**L**ogic pair**S***): tập các cặp **Câu tự nhiên (NL) → Logic bậc nhất (FOL)**, sinh tự động bằng GPT-4 và lọc kiểm tra tính hợp lệ cú pháp (từ paper LogicLLaMA, Yang et al., 2023).

| Hạng mục | Giá trị |
|---|---|
| Phiên bản dùng | **MALLS-v0.1** (đã lọc từ bản gốc 34K) |
| Tổng số cặp | ~28K (27K auto-verified + 1K human-verified) |
| File dùng để train | `data/processed/malls_v01_normalized.json` |
| Định dạng mỗi mẫu | `{ "NL": <câu>, "FOL": <luật logic> }` |
| Ngôn ngữ / License | English / CC-BY-NC-4.0 |

## 2. Số lượng mẫu pretrain

- **Giới hạn train: 5.000 mẫu** (`max_train_samples: 5000`), lấy ngẫu nhiên từ ~27K (shuffle seed 3407).
  *(Đặt `null` sẽ dùng toàn bộ ~27K mẫu.)*
- Pretrain **không tách dev / không eval** — chỉ tập trung học dịch NL → FOL, để dành đánh giá cho Stage 2.
  *(Tham số `val_ratio: 0.02` trong config bị bỏ qua ở giai đoạn pretrain.)*

## 3. Mô hình & chi tiết kỹ thuật

**Base model: `Qwen/Qwen3.5-4B`** — fine-tune theo **LoRA (PEFT)** trên framework **Unsloth + TRL SFTTrainer**.

| Nhóm | Tham số | Giá trị |
|---|---|---|
| **Model** | max_seq_length | 3.500 |
| | gen_max_new_tokens | 512 |
| **LoRA** | r / alpha / dropout | 8 / 16 / 0.05 |
| **Training** | epochs | 3 (cố định, no early stopping) |
| | batch size (train) | 2 × grad_accum 4 → **effective 8** |
| | learning_rate | 2e-4 |
| | warmup_ratio / weight_decay | 0.05 / 0.01 |
| | precision | bf16 + gradient checkpointing |
| | quantization | load_in_8bit, optimizer AdamW 8-bit |
| | seed | 3407 |
| | đặc thù Unsloth | `train_on_responses_only` (chỉ tính loss trên phần FOL output) |

## 4. Quy trình khái quát

```
MALLS-v0.1 (~27K)  ──(lấy 5K ngẫu nhiên)──►  Qwen3.5-4B + LoRA (Unsloth/SFT)
        │                                              │ 3 epochs, train-on-responses-only
        │                                              ▼
        │                                    LoRA adapter (pretrain_lora)
        │                                              │ merge LoRA vào base
        ▼                                              ▼
   Stage 2 fine-tune  ◄──── push lên HF Hub: Laplaces-Red-Devils/fol-pretrain-malls-qwen3.5-4b
   (trên target dataset)        (làm base model cho Stage 2)
```

**Mục đích:** Stage 1 giúp model học **cơ bản cách dịch NL → FOL** từ MALLS; model trung gian này sau đó được merge LoRA, đẩy lên Hugging Face Hub để làm base cho **Stage 2** fine-tune trên dataset mục tiêu chính thức ([`configs/fol_model.yaml`](../configs/fol_model.yaml)).
