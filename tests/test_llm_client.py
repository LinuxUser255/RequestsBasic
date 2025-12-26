from openai import OpenAI

from src import llm_client


def test_get_client_returns_configured_openai_instance(monkeypatch):
    """Test that get_client returns a properly configured OpenAI client."""
    # Reset any cached client
    monkeypatch.setattr(llm_client, "_client", None)
    monkeypatch.setenv("OPENAI_API_KEY", "test-api-key-12345")

    client = llm_client.get_client()

    assert isinstance(client, OpenAI)
    assert client.base_url == llm_client.LLM_URL


