from __future__ import annotations
import logging
import os
from typing import Any, Dict, List

from dotenv import load_dotenv
from openai import (
    OpenAI,
)

load_dotenv()

logger = logging.getLogger(__name__)

_client: OpenAI | None = None

LLM_URL = "https://api.x.ai/v1"


def get_client(client=None) -> OpenAI:
    global _client
    if client is None:
        api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("Missing OpenAI API key. Set the OPENAI_API_KEY environment variable.")

    client = OpenAI(api_key=api_key, base_url=LLM_URL)
    return client


def build_message(prompt: str, model_name: str = "text-davinci-003") -> Dict[str, Any]:
    system_prompt = f"You tell the time and date of the US East Coast."
    return {
        "prompt": f"{system_prompt}\n\n{prompt}",
        "model": model_name,
    }


def analyze_with_grok(prompt: str) -> Dict[str, Any]:
    client = get_client()
    message = build_message("What is the current date and time in New York City?")
    
    kwargs = {
        "model": "grok-4-1-fast-reasoning",
        "message": message,
        "temperature": 0.7,
        "seed": 42
    }
    
    return client.completion.create(**kwargs)