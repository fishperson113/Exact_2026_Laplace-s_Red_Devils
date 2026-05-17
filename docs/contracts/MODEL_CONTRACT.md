# Model ↔ Backend Interface Contract

Interface duy nhất giữa đội **Model** (Nguyên + Sơn) và đội **Backend** (Dương + Quang) là **Ollama HTTP API**.

Hai đội làm việc hoàn toàn độc lập. Khi model mới sẵn sàng, BE không cần đổi một dòng code nào — chỉ cần thay biến `OLLAMA_MODEL` trong `.env`.

---

## Sơ đồ giao tiếp

```
┌─────────────────────────────────┐     ┌─────────────────────────────────┐
│         TEAM MODEL              │     │         TEAM BACKEND            │
│       (Nguyên + Sơn)            │     │        (Dương + Quang)          │
│                                 │     │                                  │
│  Colab Pro                      │     │  FastAPI                         │
│    └─ Unsloth fine-tune         │     │    └─ app/model/llm_client.py    │
│    └─ export GGUF (q4_k_m)      │     │         └─ POST /api/generate    │
│    └─ push HuggingFace Hub      │     │                                  │
└──────────────┬──────────────────┘     └──────────────┬───────────────────┘
               │                                        │
               │  hf.co/laplaces-red-devils/model       │  HTTP :11434
               └───────────────┐    ┌───────────────────┘
                               ▼    ▼
                        ┌─────────────────┐
                        │     OLLAMA      │
                        │  (Docker self-  │
                        │   hosted)       │
                        │  :11434         │
                        └─────────────────┘
```

---

## Trách nhiệm từng đội

### Team Model — output duy nhất cần giao

| Deliverable | Format | Nơi upload |
|---|---|---|
| Fine-tuned model | `.gguf` (quantization: `q4_k_m`) | HuggingFace Hub |
| Tên repo HF | `laplaces-red-devils/<tên-model>` | Thông báo cho BE |

Không cần giao code, không cần giao weight HF safetensors, không cần setup server. **Chỉ cần file `.gguf` trên HF Hub.**

### Team Backend — không cần đụng khi model thay đổi

BE chỉ giao tiếp với Ollama qua HTTP. Khi model team giao model mới:

1. Team model thông báo tên model HF (vd: `laplaces-red-devils/qwen-exact2026`)
2. BE đổi 1 dòng trong `.env`:

```bash
OLLAMA_MODEL=hf.co/laplaces-red-devils/qwen-exact2026:Q4_K_M
```

3. Restart Docker:

```bash
docker compose restart
```

Ollama tự pull model mới. Xong.

---

## Ollama API — interface duy nhất

BE gọi endpoint sau của Ollama:

```
POST http://localhost:11434/api/generate
```

### Request schema

```json
{
  "model": "hf.co/laplaces-red-devils/qwen-exact2026:Q4_K_M",
  "prompt": "<system prompt + context + question>",
  "stream": false,
  "options": {
    "temperature": 0.1,
    "num_predict": 1024
  }
}
```

### Response schema (Ollama trả về)

```json
{
  "model": "hf.co/laplaces-red-devils/qwen-exact2026:Q4_K_M",
  "response": "...",
  "done": true,
  "total_duration": 1234567890,
  "eval_count": 256
}
```

BE lấy field `response` để parse ra output theo format cuộc thi.

---

## Format output cuộc thi (BE chịu trách nhiệm parse)

Model sinh ra raw text. BE (`app/validation/`) chịu trách nhiệm parse và đóng gói thành format nộp:

```json
{
  "answer": "B",
  "explanation": "...",
  "fol": "∀x (Resistor(x) → ...)",
  "cot": ["Step 1: ...", "Step 2: ..."],
  "premises": ["Ohm's law: V=IR", "..."],
  "confidence": 0.92
}
```

Chỉ `answer` và `explanation` là **bắt buộc**. Còn lại optional.

---

## Workflow đổi model (step-by-step)

```
Team Model (Colab)
  1. Train xong
  2. Chạy: model.push_to_hub_gguf("laplaces-red-devils/<tên>", tokenizer,
                                    quantization_method="q4_k_m", token=HF_TOKEN)
  3. Báo BE: tên model HF + quantization tag

Team Backend
  4. Mở .env, đổi OLLAMA_MODEL=hf.co/laplaces-red-devils/<tên>:Q4_K_M
  5. docker compose restart
  6. Smoke test: curl http://localhost:11434/api/tags
  7. Chạy test pipeline end-to-end
```

---

## Conventions đặt tên model trên HuggingFace Hub

```
laplaces-red-devils/qwen25math-<version>-<dataset>

Ví dụ:
  laplaces-red-devils/qwen25math-v1-physics
  laplaces-red-devils/qwen25math-v2-full
  laplaces-red-devils/acemath-v1-logic
```

Quantization tag luôn là `Q4_K_M` trừ khi có lý do đặc biệt.

---

## Môi trường

| Biến | Mô tả | Ví dụ |
|---|---|---|
| `OLLAMA_MODEL` | Model Ollama sẽ pull khi start | `hf.co/laplaces-red-devils/qwen25math-v1:Q4_K_M` |
| `OLLAMA_BASE_URL` | Ollama API URL | `http://localhost:11434` |

File tham chiếu: `.env.example`, `docker-compose.yml`, `entrypoint.sh`
