from .eval.scorer import extract, numeric_close, Extraction, RowResult, summarise
from .prompts.system import PHYSICS_SYSTEM_EN, ZEROSHOT_USER_TEMPLATE, ASSISTANT_PREFIX
from .runtime.tracing import setup_tracing, traceable


def __getattr__(name):
    """Lazy re-exports for heavy (torch / langchain / huggingface) symbols."""
    _model_loader = {
        "load_model", "LoadedModel", "generate_text", "generate_batch",
    }
    _batched_llm = {"HFBatchedLLM", "RenderPrompt"}
    _runner = {"run_solver"}
    _hf = {
        "VersionMeta", "push", "build_model_card", "collect_env_info",
        "per_domain_breakdown", "now_utc", "load_token",
    }
    _prompts_helpers = {"fewshot_messages_from"}

    if name in _model_loader:
        from .model.loader import load_model, LoadedModel, generate_text, generate_batch
        return locals()[name]
    if name in _batched_llm:
        from .model.batched_llm import HFBatchedLLM, RenderPrompt
        return locals()[name]
    if name in _runner:
        from .runtime.runner import run_solver
        return run_solver
    if name in _hf:
        from .upload.hf import (
            VersionMeta, push, build_model_card, collect_env_info,
            per_domain_breakdown, now_utc, load_token,
        )
        return locals()[name]
    if name in _prompts_helpers:
        from .prompts.helpers import fewshot_messages_from
        return fewshot_messages_from
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
