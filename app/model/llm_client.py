import httpx
from app.core.config import settings


class OllamaClient:
    def __init__(self):
        self._base_url = settings.ollama_base_url
        self._model = settings.ollama_model

    async def generate(self, prompt: str, temperature: float = 0.1, num_predict: int = 1024) -> str:
        # TODO: wrap with asyncio.wait_for + friendly timeout error instead of raw httpx.TimeoutException
        async with httpx.AsyncClient(timeout=120.0) as client:
            resp = await client.post(
                f"{self._base_url}/api/generate",
                json={
                    "model": self._model,
                    "prompt": prompt,
                    "stream": False,
                    "format": "json",
                    "options": {
                        "temperature": temperature,
                        "num_predict": num_predict,
                    },
                },
            )
            resp.raise_for_status()
            return resp.json()["response"]

    async def is_alive(self) -> bool:
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                resp = await client.get(f"{self._base_url}/api/tags")
                return resp.status_code == 200
        except Exception:
            return False


llm = OllamaClient()
