# Hướng Dẫn Fine-tune với Unsloth (Colab Pro → Ollama)

Dành cho đội **Model** (Nguyên + Sơn). Toàn bộ pipeline từ Colab đến khi BE có thể `ollama pull` về dùng.

---

## Tổng quan flow

```
Google Colab Pro
  └─ 1. Cài Unsloth
  └─ 2. Load Qwen 2.5-Math 7B (4-bit)
  └─ 3. Chuẩn bị dataset
  └─ 4. Fine-tune với SFTTrainer
  └─ 5. Export GGUF + push HuggingFace Hub
          │
          ▼
  HuggingFace Hub
  hf.co/laplaces-red-devils/<model>:Q4_K_M
          │
          ▼
  Team BE đổi .env → docker compose restart → done
```

---

## Bước 1 — Cài đặt

Chạy cell đầu tiên trong notebook:

```bash
pip install "unsloth[colab]" -q
pip install trl datasets huggingface_hub -q
```

---

## Bước 2 — Load model + apply LoRA

```python
from unsloth import FastLanguageModel
import torch

MAX_SEQ_LENGTH = 2048   # tăng nếu reasoning trace dài
LORA_RANK = 32          # sweet spot: đủ expressive, không OOM trên T4

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/Qwen2.5-Math-7B",   # version Unsloth đã optimize
    max_seq_length = MAX_SEQ_LENGTH,
    load_in_4bit = True,                        # bắt buộc cho Colab T4 (16GB)
)

model = FastLanguageModel.get_peft_model(
    model,
    r = LORA_RANK,
    target_modules = [
        "q_proj", "k_proj", "v_proj", "o_proj",
        "gate_proj", "up_proj", "down_proj",
    ],
    lora_alpha = LORA_RANK * 2,                 # *2 tăng tốc train
    lora_dropout = 0,
    bias = "none",
    use_gradient_checkpointing = "unsloth",     # giảm thêm VRAM
    random_state = 3407,
)
```

> **Lưu ý `load_in_4bit`:** Nếu được cấp A100/H100, đổi thành `False` để train fp16 — accuracy tốt hơn.

---

## Bước 3 — Chuẩn bị dataset

Dataset cần theo dạng instruction tuning. Format chuẩn cho bài toán cuộc thi:

```python
# Mỗi sample trong dataset cần có dạng:
{
  "instruction": "Cho mạch điện gồm R1=10Ω và R2=20Ω mắc song song...",
  "output": json.dumps({
    "answer": "B",
    "explanation": "Điện trở tương đương mạch song song: 1/R = 1/R1 + 1/R2...",
    "cot": ["Bước 1: Xác định cấu trúc mạch...", "Bước 2: Áp dụng công thức..."],
    "confidence": 0.92
  }, ensure_ascii=False)
}
```

**Load dataset từ HuggingFace:**

```python
from datasets import load_dataset

dataset = load_dataset("your-org/your-dataset", split="train")
```

**Hoặc từ file local (JSON):**

```python
from datasets import Dataset
import json

with open("dataset.json") as f:
    data = json.load(f)

dataset = Dataset.from_list(data)
```

**Áp dụng chat template (quan trọng với Qwen):**

```python
def format_sample(sample):
    messages = [
        {"role": "system", "content": "Bạn là AI giải bài thi vật lý và quy định học vụ. Trả lời theo JSON."},
        {"role": "user",   "content": sample["instruction"]},
        {"role": "assistant", "content": sample["output"]},
    ]
    return {"text": tokenizer.apply_chat_template(messages, tokenize=False)}

dataset = dataset.map(format_sample)
```

---

## Bước 4 — Fine-tune

```python
from trl import SFTTrainer, SFTConfig

trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    args = SFTConfig(
        output_dir = "./output",

        # Batch size — T4 16GB: batch=2, grad_accum=8 ~ effective batch 16
        per_device_train_batch_size = 2,
        gradient_accumulation_steps = 8,

        num_train_epochs = 3,           # hoặc dùng max_steps cho dataset nhỏ
        # max_steps = 200,

        learning_rate = 2e-4,
        warmup_ratio = 0.05,
        lr_scheduler_type = "cosine",

        optim = "adamw_8bit",           # optimizer 8-bit tiết kiệm VRAM
        weight_decay = 0.01,

        logging_steps = 10,
        save_steps = 100,
        seed = 3407,

        dataset_text_field = "text",
        max_seq_length = MAX_SEQ_LENGTH,
        report_to = "none",             # đổi thành "wandb" nếu muốn tracking
    ),
)

trainer.train()
```

### Ước tính thời gian train (Colab T4)

| Dataset size | Epochs | Ước tính |
|---|---|---|
| 1,000 samples | 3 | ~30–45 phút |
| 5,000 samples | 3 | ~2.5–3.5 giờ |
| 10,000 samples | 3 | ~5–7 giờ |

> Colab Pro timeout sau ~12h — chia nhỏ hoặc dùng `save_steps` để checkpoint.

---

## ⚠️ Bước 5 — Export GGUF + Push HuggingFace Hub (BƯỚC THEN CHỐT)

> **Đây là bước duy nhất nối đội Model với đội BE.**
> Nếu bước này không được làm đúng, toàn bộ pipeline của BE bị tắc — không có cách nào để Ollama tự động pull model mới về.

---

### Tại sao bước này là then chốt?

Sau khi train xong trên Colab, model nằm trong **RAM của session Colab đó** — session tắt là mất. Vấn đề là Colab không phải server, BE không thể kết nối vào đó để lấy model ra. Cần một điểm trung gian.

**HuggingFace Hub là điểm trung gian đó.** Và Ollama hỗ trợ pull trực tiếp từ HF Hub qua prefix `hf.co/` — không cần thêm bất kỳ bước deploy hay server nào.

---

### Nếu KHÔNG có bước này — pipeline thủ công cực khổ ra sao

```
Không có HuggingFace Hub:

  Colab train xong
    └─ download weight về máy local (~14GB fp16 hoặc ~4GB GGUF)
    └─ copy file qua máy BE (SCP / USB / Google Drive???)
    └─ BE phải tự convert sang GGUF bằng llama.cpp (phức tạp, dễ lỗi)
    └─ BE phải mount file GGUF vào Docker volume thủ công
    └─ Mỗi lần model update: lặp lại toàn bộ quy trình trên
    └─ Không có versioning, không biết đang chạy model nào
```

So với khi **CÓ** HuggingFace Hub:

```
  Colab train xong
    └─ push_to_hub_gguf(...)   ← 1 dòng, Unsloth lo hết
    └─ Báo BE tên model
    └─ BE đổi OLLAMA_MODEL trong .env
    └─ docker compose restart  ← Ollama tự pull về, xong
```

---

### Code — 1 dòng duy nhất

```python
from huggingface_hub import login

login(token="YOUR_HF_TOKEN")   # tạo tại hf.co/settings/tokens (role: write)

model.push_to_hub_gguf(
    "laplaces-red-devils/qwen25math-v1-physics",
    tokenizer,
    quantization_method = "q4_k_m",
    token = "YOUR_HF_TOKEN",
)
```

Unsloth tự động xử lý toàn bộ pipeline nội bộ:
1. Merge LoRA adapter vào base model
2. Convert từ PyTorch → GGUF
3. Quantize xuống `q4_k_m` (~4.1 GB)
4. Upload lên HuggingFace Hub

**Không cần cài llama.cpp, không cần convert thủ công, không cần hiểu GGUF là gì.**

---

### Kiểm tra sau khi push

Vào link sau để xác nhận file đã có trên HF Hub trước khi báo BE:

```
https://huggingface.co/laplaces-red-devils/qwen25math-v1-physics/tree/main
```

Phải thấy file `qwen25math-v1-physics.Q4_K_M.gguf` tồn tại.

---

### Fallback — nếu push_to_hub_gguf bị timeout

```python
# Bước 1: Save GGUF local trước
model.save_pretrained_gguf("./qwen25math-v1", tokenizer, quantization_method="q4_k_m")

# Bước 2: Upload thủ công
from huggingface_hub import HfApi
api = HfApi()
api.upload_file(
    path_or_fileobj = "./qwen25math-v1/qwen25math-v1.Q4_K_M.gguf",
    path_in_repo   = "qwen25math-v1.Q4_K_M.gguf",
    repo_id        = "laplaces-red-devils/qwen25math-v1-physics",
    repo_type      = "model",
    token          = "YOUR_HF_TOKEN",
)
```

---

## Bước 6 — Thông báo cho Team BE

Sau khi push xong, báo cho BE:

```
Model mới đã sẵn sàng:
  HF repo : laplaces-red-devils/qwen25math-v1-physics
  GGUF tag: Q4_K_M
  File    : qwen25math-v1-physics.Q4_K_M.gguf

Cập nhật .env:
  OLLAMA_MODEL=hf.co/laplaces-red-devils/qwen25math-v1-physics:Q4_K_M
```

---

## Convention đặt tên model

```
laplaces-red-devils/qwen25math-<version>-<focus>

Ví dụ:
  laplaces-red-devils/qwen25math-v1-physics      ← focus vật lý mạch điện
  laplaces-red-devils/qwen25math-v1-logic        ← focus quy định học vụ
  laplaces-red-devils/qwen25math-v2-full         ← train trên toàn bộ dataset
  laplaces-red-devils/acemath-v1-full            ← nếu swap sang AceMath
```

---

## Quantization — khi nào dùng cái gì

| Method | Size (7B) | RAM | Nên dùng khi |
|---|---|---|---|
| `q4_k_m` | ~4.1 GB | ~6 GB | **Default — luôn dùng cái này** |
| `q5_k_m` | ~5.1 GB | ~8 GB | Muốn accuracy cao hơn, RAM đủ |
| `q8_0` | ~7.7 GB | ~10 GB | Testing, so sánh với baseline |
| `f16` | ~14 GB | ~18 GB | Chỉ khi debug, không dùng cho deploy |

---

## Troubleshooting

**CUDA out of memory:**
```python
# Giảm batch size
per_device_train_batch_size = 1
gradient_accumulation_steps = 16   # giữ effective batch = 16

# Hoặc giảm sequence length
MAX_SEQ_LENGTH = 1024
```

**Colab disconnect giữa chừng:**
```python
# Thêm vào SFTConfig để checkpoint thường xuyên
save_steps = 50
save_total_limit = 3   # chỉ giữ 3 checkpoint gần nhất
```

---

## Tham khảo

- Unsloth notebooks: https://github.com/unslothai/notebooks
- Qwen 2.5 Math model: https://huggingface.co/Qwen/Qwen2.5-Math-7B
- AceMath (alternative): https://huggingface.co/nvidia/AceMath-7B-Instruct
- HF token settings: https://huggingface.co/settings/tokens
- Interface contract với BE: xem `MODEL_CONTRACT.md`

---

## Kết luận — MLOps Pipeline của Team

Toàn bộ flow trên thực chất là một **MLOps pipeline thu nhỏ** — đủ 3 phase cốt lõi mà không over-engineer cho bài toán competition.

```
TRAIN  ──────────────→  PACKAGE  ──────────────→  DEPLOY
Colab Pro                HF Hub                   Ollama + Docker
(Nguyên + Sơn)          (artifact registry)       (Dương + Quang)
```

Mỗi concern MLOps đều được cover:

| MLOps Concern | Giải pháp |
|---|---|
| Reproducible training | Unsloth + seed cố định (`3407`) |
| Model versioning | HF Hub repo + naming convention (`v1`, `v2`, `v2-full`) |
| Artifact registry | HF Hub lưu GGUF — có thể rollback về version cũ bất kỳ lúc nào |
| Deployment | `OLLAMA_MODEL` trong `.env` → `docker compose restart` |
| Infra as config | `docker-compose.yml` + `entrypoint.sh` — infra đóng băng sau tuần 1 |
| Team decoupling | Model team và BE team không cần sync trực tiếp, giao tiếp qua HF Hub |

**Vòng lặp cải tiến model** trong 4 tuần thực chiến:

```
Dataset mới / augmentation
        ↓
  Retrain trên Colab
        ↓
  push_to_hub_gguf (version mới)
        ↓
  BE đổi OLLAMA_MODEL → restart
        ↓
  Chạy test → đánh giá metric
        ↓
  (lặp lại)
```

Thiết kế này cho phép **đội Model iterate độc lập** — mỗi lần có model tốt hơn chỉ mất ~5 phút để BE có phiên bản mới, không cần họp, không cần deploy thủ công.

Diagram đầy đủ: xem `MLOPS_DIAGRAM.md`
