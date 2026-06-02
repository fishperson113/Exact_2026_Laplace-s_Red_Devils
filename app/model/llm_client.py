from openai import AsyncOpenAI

from app.core.config import settings


class VLLMClient:
    def __init__(self):
        self._client: AsyncOpenAI | None = None
        self._model = settings.vllm_model

    def _get_client(self) -> AsyncOpenAI:
        if self._client is None:
            self._client = AsyncOpenAI(
                base_url=settings.vllm_base_url,
                api_key=settings.vllm_api_key,
            )
        return self._client

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


llm = VLLMClient()
