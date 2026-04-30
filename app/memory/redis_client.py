import json
import redis.asyncio as aioredis
from app.core.config import settings


class SessionMemory:
    def __init__(self):
        self._client: aioredis.Redis | None = None

    async def _get_client(self) -> aioredis.Redis:
        if self._client is None:
            self._client = aioredis.from_url(settings.redis_url, decode_responses=True)
        return self._client

    def _key(self, session_id: str) -> str:
        return f"session:{session_id}"

    async def get_history(self, session_id: str) -> list[dict]:
        client = await self._get_client()
        raw = await client.get(self._key(session_id))
        if raw is None:
            return []
        return json.loads(raw)

    async def append(self, session_id: str, question: str, answer: str) -> None:
        client = await self._get_client()
        history = await self.get_history(session_id)
        history.append({"q": question, "a": answer})
        history = history[-settings.max_history_turns:]
        await client.setex(
            self._key(session_id),
            settings.session_ttl,
            json.dumps(history, ensure_ascii=False),
        )

    async def clear(self, session_id: str) -> None:
        client = await self._get_client()
        await client.delete(self._key(session_id))

    async def is_alive(self) -> bool:
        try:
            client = await self._get_client()
            await client.ping()
            return True
        except Exception:
            return False


memory = SessionMemory()
