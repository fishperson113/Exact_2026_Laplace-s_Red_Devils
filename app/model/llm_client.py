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
                api_key="dummy",  # vLLM does not require a real API key
            )
        return self._client

    async def generate(
        self,
        prompt: str,
        temperature: float = 0.1,
        max_tokens: int = 1024,
    ) -> str:
        response = await self._get_client().chat.completions.create(
            model=self._model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
            extra_body={"guided_json": True},  # vLLM structured output hint
        )
        return response.choices[0].message.content

    async def is_alive(self) -> bool:
        try:
            await self._get_client().models.list()
            return True
        except Exception:
            return False


llm = VLLMClient()
