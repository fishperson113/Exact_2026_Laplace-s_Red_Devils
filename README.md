# Exact 2026 QA Backend — Laplace's Red Devils

A math QA backend with explainable AI output, built on FastAPI + LangGraph + Ollama + Redis.

---

## Architecture

```
[load_history] → [generate] → [parse] → [save_memory] → END
```

All pipeline nodes live in `app/core/pipeline.py::_build_graph()`.  
New features are added by inserting nodes — existing nodes are never modified.

### Layer overview

| Layer | Role |
|---|---|
| **API** (`app/api/`) | HTTP interface — routes, schemas, middleware |
| **Core** (`app/core/`) | LangGraph pipeline, config |
| **Model** (`app/model/`) | Ollama async client, prompt templates |
| **Memory** (`app/memory/`) | Redis — conversation history per session |
| **Retrieval** (`app/retrieval/`) | Pinecone stub — not yet active |
| **Validation** (`app/validation/`) | JSON → `QAResponse` parsing |

---

## Tech Stack

| Concern | Choice |
|---|---|
| API framework | FastAPI |
| Pipeline orchestration | LangGraph (`StateGraph`) |
| LLM | Ollama (self-hosted, `qwen2.5-math:7b`) |
| Short-term memory | Redis 7 |
| Vector store | Pinecone (stub — not yet active) |
| Runtime | Python 3.11 |

---

## Project Structure

```
.
├── app/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── ask.py          # POST /ask
│   │   │   ├── health.py       # GET /health
│   │   │   └── dev.py          # GET|DELETE /dev/history
│   │   ├── middleware/
│   │   └── schemas.py          # AskRequest, QAResponse
│   │
│   ├── core/
│   │   ├── pipeline.py         # Graph definition + all nodes (entry point)
│   │   └── config.py           # Settings from .env
│   │
│   ├── model/
│   │   ├── llm_client.py       # Ollama async client
│   │   └── prompts/
│   │       └── qa_system.py    # Base prompt + build_prompt()
│   │
│   ├── memory/
│   │   └── redis_client.py     # get_history(), append()
│   │
│   ├── retrieval/
│   │   └── retriever.py        # Pinecone stub — fill when ready
│   │
│   ├── validation/
│   │   └── parser.py           # JSON → QAResponse
│   │
│   └── main.py
│
├── Dockerfile                  # Ollama service (pulls model on start)
├── Dockerfile.api              # FastAPI service
├── docker-compose.yml          # Orchestrates ollama + redis + api
├── entrypoint.sh               # Ollama startup: serve → pull model
├── .env.example
└── README.md
```

---

## Getting Started

### 1. Configure environment

```bash
cp .env.example .env
```

Mở `.env` và set `OLLAMA_MODEL`. Model mặc định để test end-to-end:

```
OLLAMA_MODEL=qwen2.5:7b
```

Có thể thay bằng bất kỳ model Ollama nào khác tùy mục đích thử nghiệm. Sản phẩm cuối sẽ dùng model do đội AI tự train — sẽ cập nhật khi có.

Các biến khác (`OLLAMA_BASE_URL`, `REDIS_URL`) được docker-compose tự inject cho internal networking — không cần sửa.

### 2. Build và start toàn bộ stack

```bash
docker compose up -d --build
```

Ba service sẽ khởi động theo thứ tự:
1. `ollama` — khởi động server, tự pull model qua `OLLAMA_MODEL` (lần đầu mất vài phút)
2. `redis` — sẵn sàng khi ping OK
3. `api` — chờ ollama + redis healthy rồi mới start

### 3. Kiểm tra liveness

```bash
curl http://localhost:8000/health
```

### 4. Gửi câu hỏi

```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "Tính đạo hàm của x^2 + 3x"}'
```

### 5. Reset lịch sử hội thoại (dev)

```bash
curl -X POST http://localhost:8000/dev/reset
```

### Dừng stack

```bash
docker compose down
```

Dữ liệu Ollama model và Redis được giữ trong Docker volumes (`ollama_data`, `redis_data`).  
Để xóa luôn volumes: `docker compose down -v`

---

## GPU (optional)

Mặc định Ollama chạy CPU. Để enable GPU, bỏ comment phần `deploy` trong `docker-compose.yml`:

```yaml
# deploy:
#   resources:
#     reservations:
#       devices:
#         - driver: nvidia
#           count: all
#           capabilities: [gpu]
```

---

## Endpoints

| Method | Path | Description |
|---|---|---|
| `GET` | `/` | Root — kiểm tra backend đang chạy |
| `POST` | `/ask` | Gửi câu hỏi, nhận câu trả lời |
| `GET` | `/health` | Liveness check (Ollama + Redis) |
| `POST` | `/dev/reset` | Xóa lịch sử hội thoại hiện tại |

### Request / Response

**`POST /ask`**

```json
// Request
{ "question": "Tính đạo hàm của x^2 + 3x" }

// Response
{
  "answer": "...",
  "explanation": "...",
  "fol": "...",          // optional — first-order logic form
  "cot": ["..."],        // optional — chain-of-thought steps
  "premises": ["..."],   // optional — premises used
  "confidence": 0.95     // optional — [0.0, 1.0]
}
```

---

## Environment Variables

| Variable | Default | Description |
|---|---|---|
| `OLLAMA_MODEL` | *(xem .env.example)* | Model để pull và serve |
| `OLLAMA_BASE_URL` | `http://ollama:11434` | URL Ollama API (tự inject bởi docker-compose) |
| `REDIS_URL` | `redis://redis:6379` | Redis connection URL (tự inject bởi docker-compose) |
| `SESSION_TTL` | `3600` | TTL lịch sử hội thoại (giây) |
| `MAX_HISTORY_TURNS` | `5` | Số lượt hội thoại giữ trong memory |
| `PINECONE_API_KEY` | — | Pinecone API key (chưa dùng) |
| `PINECONE_INDEX` | — | Pinecone index name (chưa dùng) |
| `EMBED_MODEL` | `nomic-embed-text` | Embedding model (chưa dùng) |
