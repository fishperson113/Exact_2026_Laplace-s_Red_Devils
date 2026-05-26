# Ollama → vLLM Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace Ollama with vLLM as the LLM backend, switching the client to the OpenAI-compatible SDK while removing all Ollama-specific files and config.

**Architecture:** `llm_client.py` is rewritten to use `AsyncOpenAI` pointed at the vLLM server (`/v1/chat/completions`). The pipeline and prompt layer are untouched — the client wraps the existing plain-string prompt into a messages list internally. All Ollama naming in config, env, and Docker is replaced with `vllm_*` equivalents.

**Tech Stack:** Python 3.11, FastAPI, LangGraph, `openai` SDK (AsyncOpenAI), vLLM (`vllm/vllm-openai` Docker image), Redis, Docker Compose.

---

## File Map

| Action | File | What changes |
|--------|------|--------------|
| Modify | `app/model/llm_client.py` | Replace `OllamaClient` (httpx) with `VLLMClient` (AsyncOpenAI) |
| Modify | `app/core/config.py` | Rename `ollama_*` → `vllm_*` settings |
| Modify | `app/api/routes/health.py` | Rename `ollama` key → `vllm` in health response |
| Modify | `.env` | Rename `OLLAMA_*` → `VLLM_*` keys |
| Modify | `docker-compose.yml` | Swap `ollama` service → `vllm` service |
| Modify | `requirements.txt` | Add `openai>=1.0.0`, remove `httpx` |
| Delete | `Dockerfile` | Ollama-specific image, no longer needed |
| Delete | `entrypoint.sh` | Ollama pull-on-startup script, no longer needed |

---

### Task 1: Update `requirements.txt`

**Files:**
- Modify: `requirements.txt`

- [ ] **Step 1: Replace `httpx` with `openai` in requirements**

Open `requirements.txt` and replace its contents with:

```
fastapi>=0.111.0
uvicorn[standard]>=0.29.0
openai>=1.0.0
redis>=5.0.4
pydantic>=2.7.0
pydantic-settings>=2.2.0

# Orchestration
langgraph>=0.2.0
langchain-core>=0.3.0

# Retrieval (optional — Pinecone disabled if PINECONE_API_KEY not set)
pinecone>=3.0.0
```

Note: `httpx` is removed because `OllamaClient` used it directly. The `openai` SDK bundles its own HTTP layer (`httpx` internally), so no direct usage remains.

- [ ] **Step 2: Commit**

```bash
git add requirements.txt
git commit -m "chore: swap httpx for openai sdk (vllm migration)"
```

---

### Task 2: Rename settings in `config.py`

**Files:**
- Modify: `app/core/config.py`

- [ ] **Step 1: Replace `ollama_*` fields with `vllm_*`**

Replace the full contents of `app/core/config.py` with:

```python
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    vllm_model: str = "Qwen/Qwen2.5-Math-7B-Instruct"
    vllm_base_url: str = "http://localhost:8000/v1"

    redis_url: str = "redis://localhost:6379"
    session_ttl: int = 3600
    max_history_turns: int = 5

    pinecone_api_key: Optional[str] = None
    pinecone_index: Optional[str] = None
    embed_model: str = "nomic-embed-text"


settings = Settings()
```

- [ ] **Step 2: Commit**

```bash
git add app/core/config.py
git commit -m "chore: rename ollama_* settings to vllm_* in config"
```

---

### Task 3: Rewrite `llm_client.py` using `AsyncOpenAI`

**Files:**
- Modify: `app/model/llm_client.py`

- [ ] **Step 1: Write the failing test**

Create `tests/model/test_llm_client.py`:

```python
import pytest
from unittest.mock import AsyncMock, MagicMock, patch


@pytest.mark.asyncio
async def test_generate_returns_string():
    """VLLMClient.generate() should return the assistant message content."""
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = '{"answer": "42"}'

    with patch("app.model.llm_client.AsyncOpenAI") as MockClient:
        instance = MockClient.return_value
        instance.chat = MagicMock()
        instance.chat.completions = MagicMock()
        instance.chat.completions.create = AsyncMock(return_value=mock_response)

        from app.model.llm_client import VLLMClient
        client = VLLMClient()
        result = await client.generate("What is 6x7?")

    assert result == '{"answer": "42"}'


@pytest.mark.asyncio
async def test_is_alive_returns_true_on_success():
    """is_alive() should return True when /v1/models responds 200."""
    mock_response = MagicMock()
    mock_response.status_code = 200

    with patch("app.model.llm_client.AsyncOpenAI") as MockClient:
        instance = MockClient.return_value
        instance.models = MagicMock()
        instance.models.list = AsyncMock(return_value=mock_response)

        from app.model.llm_client import VLLMClient
        client = VLLMClient()
        result = await client.is_alive()

    assert result is True


@pytest.mark.asyncio
async def test_is_alive_returns_false_on_exception():
    """is_alive() should return False when the server is unreachable."""
    with patch("app.model.llm_client.AsyncOpenAI") as MockClient:
        instance = MockClient.return_value
        instance.models = MagicMock()
        instance.models.list = AsyncMock(side_effect=Exception("connection refused"))

        from app.model.llm_client import VLLMClient
        client = VLLMClient()
        result = await client.is_alive()

    assert result is False
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
pytest tests/model/test_llm_client.py -v
```

Expected: `ImportError` or `AttributeError` — `VLLMClient` does not exist yet.

- [ ] **Step 3: Rewrite `llm_client.py`**

Replace the full contents of `app/model/llm_client.py` with:

```python
from openai import AsyncOpenAI

from app.core.config import settings


class VLLMClient:
    def __init__(self):
        self._client = AsyncOpenAI(
            base_url=settings.vllm_base_url,
            api_key="dummy",  # vLLM does not require a real API key
        )
        self._model = settings.vllm_model

    async def generate(
        self,
        prompt: str,
        temperature: float = 0.1,
        max_tokens: int = 1024,
    ) -> str:
        response = await self._client.chat.completions.create(
            model=self._model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
            extra_body={"guided_json": True},  # vLLM structured output hint
        )
        return response.choices[0].message.content

    async def is_alive(self) -> bool:
        try:
            await self._client.models.list()
            return True
        except Exception:
            return False


llm = VLLMClient()
```

Note: `extra_body={"guided_json": True}` is a vLLM hint for JSON output mode — equivalent to Ollama's `"format": "json"`. If your vLLM version doesn't support it, remove that line safely.

- [ ] **Step 4: Run tests to verify they pass**

```bash
pytest tests/model/test_llm_client.py -v
```

Expected: all 3 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add app/model/llm_client.py tests/model/test_llm_client.py
git commit -m "feat: replace OllamaClient with VLLMClient using openai sdk"
```

---

### Task 4: Update `.env`

**Files:**
- Modify: `.env`

- [ ] **Step 1: Rename `OLLAMA_*` keys**

Replace the full contents of `.env` with:

```env
VLLM_MODEL=Qwen/Qwen2.5-Math-7B-Instruct
VLLM_BASE_URL=http://localhost:8000/v1

# Redis
REDIS_URL=redis://localhost:6379
SESSION_TTL=3600
MAX_HISTORY_TURNS=5

# Pinecone (optional — skip to disable retrieval)
PINECONE_API_KEY=
PINECONE_INDEX=

# Embedding
EMBED_MODEL=nomic-embed-text
```

- [ ] **Step 2: Commit**

```bash
git add .env
git commit -m "chore: rename OLLAMA_* env vars to VLLM_* in .env"
```

---

### Task 5: Swap Ollama → vLLM in `docker-compose.yml`

**Files:**
- Modify: `docker-compose.yml`

- [ ] **Step 1: Replace `ollama` service with `vllm`**

Replace the full contents of `docker-compose.yml` with:

```yaml
services:
  vllm:
    image: vllm/vllm-openai:latest
    container_name: vllm
    runtime: nvidia          # requires nvidia-container-toolkit on the host
    environment:
      - HUGGING_FACE_HUB_TOKEN=${HUGGING_FACE_HUB_TOKEN:-}
    command:
      - "--model"
      - "${VLLM_MODEL:-Qwen/Qwen2.5-Math-7B-Instruct}"
      - "--dtype"
      - "auto"
      - "--max-model-len"
      - "4096"
    volumes:
      - vllm_cache:/root/.cache/huggingface
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-sf", "http://localhost:8000/v1/models"]
      interval: 15s
      timeout: 5s
      retries: 20
      start_period: 120s

  redis:
    image: redis:7-alpine
    container_name: redis
    volumes:
      - redis_data:/data
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 3s
      retries: 5

  api:
    build:
      context: .
      dockerfile: Dockerfile.api
    container_name: api
    ports:
      - "8000:8000"
    env_file: .env
    environment:
      - VLLM_BASE_URL=http://vllm:8000/v1
      - REDIS_URL=redis://redis:6379
    depends_on:
      vllm:
        condition: service_healthy
      redis:
        condition: service_healthy
    restart: unless-stopped

volumes:
  vllm_cache:
  redis_data:
```

Note: `HUGGING_FACE_HUB_TOKEN` is optional — only needed for gated models. Add it to `.env` if required. The `api` service port stays `8000` but vLLM also uses `8000` internally — they're on different containers so no conflict. The `api` container accesses vLLM via `http://vllm:8000/v1` (Docker internal network).

- [ ] **Step 2: Commit**

```bash
git add docker-compose.yml
git commit -m "feat: replace ollama service with vllm in docker-compose"
```

---

### Task 6: Fix health route — rename `ollama` → `vllm`

**Files:**
- Modify: `app/api/routes/health.py`

- [ ] **Step 1: Write the failing test**

Create `tests/api/test_health.py`:

```python
import pytest
from unittest.mock import AsyncMock, patch
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_response_has_vllm_key():
    """Health endpoint must return 'vllm' key, not 'ollama'."""
    with patch("app.api.routes.health.llm.is_alive", new_callable=AsyncMock, return_value=True), \
         patch("app.api.routes.health.memory.is_alive", new_callable=AsyncMock, return_value=True):
        response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "vllm" in data
    assert "ollama" not in data
    assert data["vllm"] == "up"
    assert data["redis"] == "up"
    assert data["status"] == "ok"


def test_health_degraded_when_vllm_down():
    with patch("app.api.routes.health.llm.is_alive", new_callable=AsyncMock, return_value=False), \
         patch("app.api.routes.health.memory.is_alive", new_callable=AsyncMock, return_value=True):
        response = client.get("/health")
    data = response.json()
    assert data["status"] == "degraded"
    assert data["vllm"] == "down"
```

- [ ] **Step 2: Run test to verify it fails**

```bash
pytest tests/api/test_health.py -v
```

Expected: FAIL — response still contains `"ollama"` key.

- [ ] **Step 3: Update health route**

Replace the full contents of `app/api/routes/health.py` with:

```python
from fastapi import APIRouter
from app.model.llm_client import llm
from app.memory.redis_client import memory

router = APIRouter()


@router.get("/health")
async def health() -> dict:
    vllm_ok = await llm.is_alive()
    redis_ok = await memory.is_alive()
    return {
        "status": "ok" if (vllm_ok and redis_ok) else "degraded",
        "vllm": "up" if vllm_ok else "down",
        "redis": "up" if redis_ok else "down",
    }
```

- [ ] **Step 4: Run test to verify it passes**

```bash
pytest tests/api/test_health.py -v
```

Expected: both tests PASS.

- [ ] **Step 5: Commit**

```bash
git add app/api/routes/health.py tests/api/test_health.py
git commit -m "fix: rename ollama → vllm key in health route"
```

---

### Task 7: Delete Ollama-specific files

**Files:**
- Delete: `Dockerfile`
- Delete: `entrypoint.sh`

- [ ] **Step 1: Delete the files**

```bash
git rm Dockerfile entrypoint.sh
```

- [ ] **Step 2: Commit**

```bash
git commit -m "chore: remove ollama Dockerfile and entrypoint.sh"
```

---

### Task 8: Smoke test the full stack

- [ ] **Step 1: Run all unit tests**

```bash
pytest tests/ -v
```

Expected: all tests PASS (no import errors referencing `OllamaClient` or `ollama_*`).

- [ ] **Step 2: Verify no Ollama references remain in source**

```bash
grep -r "ollama" app/ .env docker-compose.yml requirements.txt --include="*.py" --include="*.yml" --include="*.txt" --include=".env" -i
```

Expected: zero matches.

- [ ] **Step 3: Build and start the stack (requires GPU + nvidia-container-toolkit)**

```bash
docker compose up --build
```

Wait for vLLM healthcheck to pass (can take 2–5 minutes while model downloads from HF).

- [ ] **Step 4: Hit the API**

```bash
curl -s -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is 2 + 2?"}' | python -m json.tool
```

Expected response shape:
```json
{
  "answer": "4",
  "explanation": "...",
  "fol": null,
  "cot": null,
  "premises": null,
  "confidence": null
}
```

- [ ] **Step 5: Check health endpoint**

```bash
curl -s http://localhost:8000/health | python -m json.tool
```

Expected:
```json
{
  "status": "ok",
  "vllm": "up",
  "redis": "up"
}
```

- [ ] **Step 6: Final commit**

```bash
git add .
git commit -m "chore: vllm migration complete - all ollama references removed"
```
