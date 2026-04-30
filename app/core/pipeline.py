from __future__ import annotations

import uuid
from typing import Optional
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, END

from app.api.schemas import AskRequest, QAResponse
from app.memory.redis_client import memory
from app.model.llm_client import llm
from app.model.prompts.qa_system import build_prompt
from app.validation.parser import parse_response

SESSION_ID = "default"


# ---------------------------------------------------------------------------
# State
# ---------------------------------------------------------------------------
class QAState(TypedDict):
    question: str
    history: list[dict]
    raw_response: str
    response: Optional[QAResponse]


# ---------------------------------------------------------------------------
# Nodes
# ---------------------------------------------------------------------------

async def node_load_history(state: QAState) -> dict:
    return {"history": await memory.get_history(SESSION_ID)}


async def node_generate(state: QAState) -> dict:
    prompt = build_prompt(state["question"], history=state["history"])
    return {"raw_response": await llm.generate(prompt)}


async def node_parse(state: QAState) -> dict:
    return {"response": parse_response(state["raw_response"])}


async def node_save_memory(state: QAState) -> dict:
    r = state["response"]
    if r:
        await memory.append(SESSION_ID, state["question"], r.answer)
    return {}


# ---------------------------------------------------------------------------
# Graph
# ---------------------------------------------------------------------------

def _build_graph():
    g = StateGraph(QAState)

    g.add_node("load_history", node_load_history)
    g.add_node("generate", node_generate)
    g.add_node("parse", node_parse)
    g.add_node("save_memory", node_save_memory)

    g.set_entry_point("load_history")
    g.add_edge("load_history", "generate")
    g.add_edge("generate", "parse")
    g.add_edge("parse", "save_memory")
    g.add_edge("save_memory", END)

    return g.compile()


_graph = _build_graph()


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------

async def run_qa_pipeline(request: AskRequest) -> QAResponse:
    initial: QAState = {
        "question": request.question,
        "history": [],
        "raw_response": "",
        "response": None,
    }
    final = await _graph.ainvoke(initial)
    return final["response"]
