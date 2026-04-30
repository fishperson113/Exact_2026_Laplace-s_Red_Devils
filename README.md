# Chatbot QA — XAI System

A Retrieval-Augmented Generation (RAG) chatbot with explainable AI (xAI) output.  
Built on LlamaIndex + Pinecone + self-hosted Ollama.

---

## Architecture

```
[ API Layer ]          ← FastAPI — expose endpoints, handle request/response
      ↓
[ Core Engine ]        ← orchestration, pipeline control flow
      ↓
[ Retrieval Layer ]    ← LlamaIndex + Pinecone — chunking, search, context building
      ↓
[ Model Layer ]        ← Ollama (Mistral / Qwen / ...) — generate + reasoning
      ↓
[ Validation Layer ]   ← xAI — source attribution, confidence scoring, explanation
      ↓
[ Tool Layer ]         ← (optional) web search, calculator, external APIs
```

### Layer responsibilities

| Layer | Role | Mandatory |
|---|---|---|
| **API** | HTTP interface, auth, rate limit | ✅ |
| **Core Engine** | Orchestrate the QA pipeline end-to-end | ✅ |
| **Retrieval** | Deterministic context retrieval — always runs before LLM | ✅ |
| **Model** | LLM inference only — generate answer from given context | ✅ |
| **Validation** | Attach sources, explain reasoning, score confidence | ✅ |
| **Tools** | Supplemental actions when pipeline needs external data | ⚙️ optional |

### Why retrieval is NOT a tool

In agent systems: LLM decides when/whether to call retrieval → unstable, hard to debug.  
In this QA system: retrieval is a **mandatory pipeline step** — LLM only sees what we decide to give it.

```
Agent style:   LLM → decide → call retrieval tool → get context   ← ❌ not this
RAG style:     query → retrieval → context → LLM                  ← ✅ this
```

---

## Tech Stack

| Concern | Choice |
|---|---|
| API framework | FastAPI |
| Orchestration | LlamaIndex (pipeline) / LangGraph (future) |
| Vector store | Pinecone |
| LLM | Ollama (self-hosted) |
| Embedding | (TBD — e.g. nomic-embed-text via Ollama) |

---

## Project Structure

```
.
├── app/
│   ├── api/                  # API Layer
│   │   ├── routes/           # chat, health, ingest endpoints
│   │   └── middleware/       # auth, rate limit, logging
│   │
│   ├── core/                 # Core Engine
│   │   ├── pipeline.py       # main QA pipeline (entry point)
│   │   └── orchestrator.py   # step sequencing
│   │
│   ├── retrieval/            # Retrieval Layer
│   │   ├── indexer.py        # document ingestion, chunking → Pinecone
│   │   ├── retriever.py      # query → top-k chunks
│   │   └── context_builder.py# format retrieved chunks into LLM context
│   │
│   ├── model/                # Model Layer
│   │   ├── llm_client.py     # Ollama client wrapper
│   │   └── prompts/          # prompt templates
│   │
│   ├── validation/           # Validation Layer (xAI)
│   │   ├── explainer.py      # source attribution, reasoning explanation
│   │   └── scorer.py         # confidence scoring
│   │
│   └── tools/                # Tool Layer (optional)
│       └── web_search.py
│
├── data/
│   └── documents/            # raw source documents for ingestion
│
├── scripts/
│   ├── ingest.py             # one-off: chunk + embed + push to Pinecone
│   └── health_check.py       # smoke test pipeline end-to-end
│
├── tests/
│   ├── test_retrieval.py
│   ├── test_pipeline.py
│   └── test_validation.py
│
├── Dockerfile                # Ollama self-host
├── docker-compose.yml
├── entrypoint.sh
├── .env.example
└── README.md
```

---

## QA Pipeline Flow

```
User question
     │
     ▼
[Core Engine] ── trigger pipeline
     │
     ▼
[Retrieval Layer]
  ├─ embed query
  ├─ search Pinecone (top-k)
  └─ build context window
     │
     ▼
[Model Layer]
  ├─ inject context + question into prompt
  └─ generate answer via Ollama
     │
     ▼
[Validation Layer]
  ├─ attach source chunks used
  ├─ score answer confidence
  └─ produce explanation (xAI)
     │
     ▼
API response: { answer, sources, confidence, explanation }
```

---

## Getting Started

### 1. Start Ollama

```bash
cp .env.example .env
# Set OLLAMA_MODEL in .env (e.g. qwen2.5:7b)
docker compose up -d
```

### 2. Ingest documents

```bash
# (after BE is implemented)
python scripts/ingest.py --source data/documents/
```

### 3. Run API

```bash
# (after BE is implemented)
uvicorn app.api.main:app --reload
```

---

## Environment Variables

| Variable | Description |
|---|---|
| `OLLAMA_MODEL` | Model to pull and serve (e.g. `qwen2.5:7b`) |
| `OLLAMA_BASE_URL` | Ollama API URL (default: `http://localhost:11434`) |
| `PINECONE_API_KEY` | Pinecone API key |
| `PINECONE_INDEX` | Pinecone index name |
| `EMBED_MODEL` | Embedding model name |
