# Development Guide — Procedural Extension Pattern

Pipeline hiện tại là base tối giản: nhận câu hỏi → gọi Ollama → trả JSON.
Mọi tính năng mới đều được thêm vào theo **cùng một pattern**: thêm field vào State → viết node → nối edge vào graph.
Không phá vỡ node cũ, không breaking changes.

---

## Cấu trúc graph hiện tại

```
[load_history] → [generate] → [parse] → [save_memory] → END
```

`app/core/pipeline.py` là file duy nhất cần đụng khi mở rộng pipeline.

---

## Pattern: Thêm tính năng mới

### Bước 1 — Thêm field vào QAState

```python
class QAState(TypedDict):
    question: str
    history: list[dict]
    raw_response: str
    response: Optional[QAResponse]
    # --- thêm vào đây ---
    your_new_field: str
```

### Bước 2 — Viết node mới

Node nhận state, trả về **dict chỉ gồm key nó thay đổi**.
LangGraph merge phần còn lại tự động — không cần return toàn bộ state.

```python
async def node_your_feature(state: QAState) -> dict:
    result = do_something(state["question"])
    return {"your_new_field": result}
```

### Bước 3 — Nối vào graph

```python
g.add_node("your_feature", node_your_feature)

# Chèn vào giữa 2 node có sẵn — không đụng node khác
g.add_edge("load_history", "your_feature")   # thay vì load_history → generate
g.add_edge("your_feature", "generate")
```

---

## Thêm Tool nội bộ (Z3, SymPy, calculator...)

Tool là node thực hiện tác vụ ngoài LLM. Viết hàm async trong `app/tools/`, gọi trong node.

```python
# app/tools/z3_solver.py
from z3 import Solver, Real, sat

def solve_constraints(constraints: dict) -> dict:
    s = Solver()
    # ... thêm constraint vào solver
    return {"sat": s.check() == sat, "model": str(s.model())}
```

Z3 là blocking (không async native) — bọc bằng `run_in_executor`:

```python
# pipeline.py
import asyncio
from concurrent.futures import ThreadPoolExecutor
from app.tools.z3_solver import solve_constraints

_executor = ThreadPoolExecutor(max_workers=2)

async def node_z3(state: QAState) -> dict:
    loop = asyncio.get_event_loop()
    result = await asyncio.wait_for(
        loop.run_in_executor(_executor, solve_constraints, state["constraints"]),
        timeout=10.0,
    )
    return {"tool_result": result}
```

Dùng `add_conditional_edges` nếu tool chỉ chạy trong một số trường hợp:

```python
def route_after_parse(state: QAState) -> str:
    if state.get("needs_z3"):
        return "z3"
    return "save_memory"

g.add_conditional_edges("parse", route_after_parse, {"z3": "z3", "save_memory": "save_memory"})
g.add_edge("z3", "save_memory")
```

> **FastMCP**: chỉ cần khi tool là microservice độc lập cần reuse cross-service. Đa số case không cần.
> **`@tool` decorator (LangChain)**: chỉ dùng khi muốn LLM tự quyết gọi tool — không dùng trong pipeline này.

---

## MoE (Mixture of Experts)

MoE trong pipeline này chỉ là gọi `llm.generate()` nhiều lần với prompt khác nhau.
Không cần thay đổi gì về memory hay session.

### Graph sau khi thêm MoE

```
[load_history] → [route] → [physics_expert]  ↘
                        ↘ [rules_expert]   → [aggregate] → [parse] → [save_memory] → END
```

### Bước 1 — Thêm field vào State

```python
class QAState(TypedDict):
    ...
    expert: str                        # "physics" | "rules"
    expert_response: str               # raw output từ expert được chọn
```

### Bước 2 — Prompt files

```
app/model/prompts/
    qa_system.py       ← hiện tại
    router.py          ← build_router_prompt()
    expert_physics.py  ← build_physics_prompt()
    expert_rules.py    ← build_rules_prompt()
```

Mỗi file chỉ chứa text và build function, không có logic.

### Bước 3 — Viết nodes

```python
from app.model.prompts.router import build_router_prompt
from app.model.prompts.expert_physics import build_physics_prompt
from app.model.prompts.expert_rules import build_rules_prompt

async def node_route(state: QAState) -> dict:
    prompt = build_router_prompt(state["question"])
    expert = await llm.generate(prompt)   # trả về "physics" hoặc "rules"
    return {"expert": expert.strip()}

async def node_physics_expert(state: QAState) -> dict:
    prompt = build_physics_prompt(state["question"], history=state["history"])
    return {"expert_response": await llm.generate(prompt)}

async def node_rules_expert(state: QAState) -> dict:
    prompt = build_rules_prompt(state["question"], history=state["history"])
    return {"expert_response": await llm.generate(prompt)}
```

### Bước 4 — Nối vào graph

```python
def route_to_expert(state: QAState) -> str:
    return state["expert"]   # "physics" | "rules"

g.add_node("route", node_route)
g.add_node("physics", node_physics_expert)
g.add_node("rules", node_rules_expert)

g.add_edge("load_history", "route")
g.add_conditional_edges("route", route_to_expert, {"physics": "physics", "rules": "rules"})
g.add_edge("physics", "parse")
g.add_edge("rules", "parse")
```

---

## Retrieval với Pinecone

Retriever hiện tại là stub — trả `""` nếu `PINECONE_API_KEY` không set.
Khi cần retrieval, thêm field `context` vào State và thêm node:

```python
class QAState(TypedDict):
    ...
    context: str   # retrieved docs, mặc định ""
```

```python
async def node_retrieve(state: QAState) -> dict:
    context = await retriever.retrieve(state["question"])
    return {"context": context}
```

`build_prompt()` đã có sẵn param `context=""` — chỉ cần truyền vào:

```python
async def node_generate(state: QAState) -> dict:
    prompt = build_prompt(state["question"], context=state["context"], history=state["history"])
    return {"raw_response": await llm.generate(prompt)}
```

Fill logic embedding vào `app/retrieval/retriever.py` khi sẵn sàng:

```python
async def retrieve(self, query: str, top_k: int = 3) -> str:
    embedding = await embed(query)
    results = self._index.query(vector=embedding, top_k=top_k, include_metadata=True)
    chunks = [m["metadata"]["text"] for m in results["matches"]]
    return "\n\n".join(chunks)
```

---

## Short-term Memory

Redis lưu lịch sử hội thoại theo session. Dùng `SESSION_ID = "default"` — 1 Redis key, không cần quản lý gì thêm.

Khi thêm MoE hay tool, state vẫn chung 1 `QAState` → LangGraph merge tự động, không cần lo về memory hay lock.

Cấu hình trong `.env`:

```
SESSION_TTL=3600        # giây — session hết hạn sau 1 tiếng không hoạt động
MAX_HISTORY_TURNS=5     # giữ tối đa 5 lượt Q&A gần nhất
```

---

## Checklist khi thêm tính năng

- [ ] Thêm field vào `QAState` nếu cần truyền data qua nodes
- [ ] Viết `node_xxx()` — chỉ return dict của key nó thay đổi
- [ ] Thêm prompt file vào `app/model/prompts/` nếu cần prompt mới
- [ ] Thêm `add_node` + `add_edge` (hoặc `add_conditional_edges`) vào `_build_graph()`
- [ ] Không sửa node đang hoạt động — thêm node mới và chèn vào graph
- [ ] Dùng `run_in_executor` nếu tool là blocking (Z3, SymPy...)
- [ ] Test bằng `curl http://localhost:8000/ask` sau mỗi thay đổi
