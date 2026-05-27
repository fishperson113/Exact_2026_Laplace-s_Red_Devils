import pytest
from unittest.mock import AsyncMock, MagicMock, patch

from app.model.llm_client import VLLMClient


@pytest.mark.asyncio
async def test_generate_returns_string():
    """VLLMClient.generate() should return the assistant message content."""
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = '{"answer": "42"}'

    mock_client = MagicMock()
    mock_client.chat.completions.create = AsyncMock(return_value=mock_response)

    client = VLLMClient()
    with patch.object(client, "_get_client", return_value=mock_client):
        result = await client.generate("What is 6x7?")

    assert result == '{"answer": "42"}'


@pytest.mark.asyncio
async def test_is_alive_returns_true_on_success():
    """is_alive() should return True when /v1/models responds 200."""
    mock_client = MagicMock()
    mock_client.models.list = AsyncMock(return_value=MagicMock())

    client = VLLMClient()
    with patch.object(client, "_get_client", return_value=mock_client):
        result = await client.is_alive()

    assert result is True


@pytest.mark.asyncio
async def test_is_alive_returns_false_on_exception():
    """is_alive() should return False when the server is unreachable."""
    mock_client = MagicMock()
    mock_client.models.list = AsyncMock(side_effect=Exception("connection refused"))

    client = VLLMClient()
    with patch.object(client, "_get_client", return_value=mock_client):
        result = await client.is_alive()

    assert result is False
