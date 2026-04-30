from app.core.config import settings


class PineconeRetriever:
    def __init__(self):
        self._enabled = bool(settings.pinecone_api_key and settings.pinecone_index)
        if self._enabled:
            try:
                from pinecone import Pinecone
                self._pc = Pinecone(api_key=settings.pinecone_api_key)
                self._index = self._pc.Index(settings.pinecone_index)
            except ImportError:
                self._enabled = False

    async def retrieve(self, query: str, top_k: int = 3) -> str:
        """Return relevant context as plain text, or empty string if disabled."""
        if not self._enabled:
            return ""
        # TODO: embed query with EMBED_MODEL, search index, join top-k texts
        return ""


retriever = PineconeRetriever()
