"""LangChain wrapper around our batched HF generator.

We don't use `langchain-huggingface`'s `ChatHuggingFace` because:
- It re-implements chat-template rendering in ways that fight ours.
- It hides the batching path; we want explicit control so 8-question
  batches go through the GPU as one `model.generate(...)` call.

Instead this file exposes:

- `HFBatchedLLM`: a `Runnable[str, str]` whose `batch()` is overridden
  to call our `generate_batch`. Drop it at the end of any LCEL chain.
- `render_messages_to_prompt`: a small `Runnable` that takes LangChain
  `ChatPromptValue`s and emits the tokenizer-rendered string.

LangSmith tracing is automatic when the env vars are set — every chain
invocation appears in the project dashboard.
"""

from __future__ import annotations

from typing import Any, Sequence

from langchain_core.prompt_values import ChatPromptValue
from langchain_core.runnables import Runnable
from langchain_core.runnables.config import RunnableConfig

from app.physics_solution.shared.model_loader import (
    LoadedModel,
    generate_batch,
    generate_text,
)


def _lc_messages_to_dicts(messages) -> list[dict]:
    """Convert LangChain message objects to the dict form HF expects."""
    out: list[dict] = []
    for m in messages:
        role = getattr(m, "type", None)
        if role == "human":
            role = "user"
        elif role == "ai":
            role = "assistant"
        elif role == "system":
            role = "system"
        else:
            role = role or "user"
        out.append({"role": role, "content": m.content})
    return out


def _apply_chat_template_no_think(tokenizer, msgs: list[dict]) -> str:
    """`apply_chat_template` with thinking mode forcibly OFF.

    Qwen3.5 has thinking mode ON by default — the chat template wraps
    generation with a `<think>...</think>` block which on our problems
    blows ~700 tokens of "Thinking Process: Analyze the Request: ..."
    before reaching the actual reasoning. The Jinja2 template checks
    the `enable_thinking` kwarg.

    We try the kwarg first and fall back to a plain call if the
    tokenizer's template doesn't accept it (non-Qwen models).
    """
    try:
        return tokenizer.apply_chat_template(
            msgs,
            tokenize=False,
            add_generation_prompt=True,
            enable_thinking=False,
        )
    except TypeError:
        return tokenizer.apply_chat_template(
            msgs, tokenize=False, add_generation_prompt=True
        )


class RenderPrompt(Runnable):
    """Turn a `ChatPromptValue` (or str) into a tokenizer-rendered prompt string.

    Appends `assistant_prefix` after the assistant marker so the model is
    forced to continue from there. Leave it empty for natural behaviour.
    """

    def __init__(self, loaded: LoadedModel, assistant_prefix: str = "") -> None:
        super().__init__()
        self._loaded = loaded
        self._prefix = assistant_prefix

    def _render_one(self, value) -> str:
        if isinstance(value, str):
            text = value
        else:
            if isinstance(value, ChatPromptValue):
                msgs = _lc_messages_to_dicts(value.to_messages())
            else:
                msgs = _lc_messages_to_dicts(list(value))
            text = _apply_chat_template_no_think(self._loaded.tokenizer, msgs)
        if self._prefix:
            text += self._prefix
        return text

    def invoke(self, input: Any, config: RunnableConfig | None = None, **kwargs) -> str:
        return self._render_one(input)


class HFBatchedLLM(Runnable):
    """Runnable[str, str] that batches through `generate_batch` under the hood."""

    def __init__(
        self,
        loaded: LoadedModel,
        *,
        max_new_tokens: int = 1536,
        temperature: float = 0.0,
        top_p: float = 1.0,
        assistant_prefix: str = "",
    ) -> None:
        super().__init__()
        self._loaded = loaded
        self._max_new_tokens = max_new_tokens
        self._temperature = temperature
        self._top_p = top_p
        # If a prefix was prepended at render time, we mirror it on the
        # output so the recorded completion contains the full assistant turn.
        self._prefix = assistant_prefix

    @property
    def last_elapsed_s(self) -> float:
        return getattr(self, "_last_elapsed", 0.0)

    def invoke(self, input: str, config: RunnableConfig | None = None, **kwargs) -> str:
        completion, elapsed = generate_text(
            self._loaded,
            input,
            max_new_tokens=self._max_new_tokens,
            temperature=self._temperature,
            top_p=self._top_p,
        )
        self._last_elapsed = elapsed
        return (self._prefix + completion) if self._prefix else completion

    def batch(
        self,
        inputs: Sequence[str],
        config: RunnableConfig | None = None,
        *,
        return_exceptions: bool = False,
        **kwargs,
    ) -> list[str]:
        if len(inputs) == 1:
            return [self.invoke(inputs[0], config)]
        # Verify batching is actually engaged — useful when chain wiring is
        # accidentally serial. Visible once per batch on stdout.
        print(
            f"  [HFBatchedLLM] generating batch of {len(inputs)} prompts "
            f"(max_new_tokens={self._max_new_tokens})",
            flush=True,
        )
        completions, elapsed = generate_batch(
            self._loaded,
            list(inputs),
            max_new_tokens=self._max_new_tokens,
            temperature=self._temperature,
            top_p=self._top_p,
        )
        self._last_elapsed = elapsed
        if self._prefix:
            completions = [self._prefix + c for c in completions]
        return completions
