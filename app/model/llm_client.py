import httpx
from openai import AsyncOpenAI

from app.core.config import settings


class VLLMClient:
    """Async OpenAI-compatible client bound to ONE vLLM endpoint + model."""

    def __init__(self, base_url: str, model: str, api_key: str | None = None):
        self._base_url = base_url
        self._model = model
        self._api_key = api_key or settings.vllm_api_key
        self._client: AsyncOpenAI | None = None
        # server root (no /v1) for the sleep/wake_up/is_sleeping dev endpoints
        self._server_root = base_url.rsplit("/v1", 1)[0].rstrip("/")

    @property
    def server_root(self) -> str:
        return self._server_root

    def _get_client(self) -> AsyncOpenAI:
        if self._client is None:
            self._client = AsyncOpenAI(base_url=self._base_url, api_key=self._api_key)
        return self._client

    @property
    def model(self) -> str:
        return self._model

    async def chat(
        self,
        messages: list[dict],
        temperature: float = 0.0,
        max_tokens: int = 2000,
    ) -> str:
        """Send a structured message list to vLLM, return completion text."""
        response = await self._get_client().chat.completions.create(
            model=self._model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            extra_body={
                "chat_template_kwargs": {"enable_thinking": False},
            },
        )
        return response.choices[0].message.content or ""

    async def generate(
        self,
        prompt: str,
        temperature: float = 0.0,
        max_tokens: int = 2000,
    ) -> str:
        """Convenience wrapper: single user message."""
        return await self.chat(
            [{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
        )

    async def is_alive(self) -> bool:
        try:
            await self._get_client().models.list()
            return True
        except Exception:
            return False

    # ---- vLLM sleep-mode dev endpoints (need VLLM_SERVER_DEV_MODE=1) ----
    async def sleep(self, level: int = 1) -> None:
        """Offload this server's weights GPU->CPU RAM (level 1), freeing VRAM."""
        async with httpx.AsyncClient() as c:
            await c.post(f"{self._server_root}/sleep", params={"level": level}, timeout=120)

    async def wake_up(self) -> None:
        """Re-load weights CPU RAM->GPU."""
        async with httpx.AsyncClient() as c:
            await c.post(f"{self._server_root}/wake_up", timeout=180)

    async def is_sleeping(self) -> bool:
        try:
            async with httpx.AsyncClient() as c:
                r = await c.get(f"{self._server_root}/is_sleeping", timeout=10)
                return bool(r.json().get("is_sleeping", False))
        except Exception:
            return False


# Physics (Task Type 2). `llm` is the canonical name used by the v05 pipeline.
llm = VLLMClient(settings.vllm_base_url, settings.vllm_model)
physics_llm = llm

# Logic (Task Type 1) — two-stage FOL -> QA, each on its own vLLM server.
fol_llm = VLLMClient(settings.fol_base_url, settings.fol_model)
qa_llm = VLLMClient(settings.qa_base_url, settings.qa_model)
