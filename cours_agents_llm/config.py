# ============================================================
# config.py — Charge le .env et fabrique le client LLM (agnostique)
# ============================================================
# Identique au cours 11 : tu n'as PAS à le modifier. Il lit ton .env
# et renvoie un client prêt, ou affiche une aide claire si rien n'est configuré.
# ============================================================

import os
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")

LLM_BASE_URL = os.getenv("LLM_BASE_URL")
LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL")


_MESSAGE_AIDE = """
❌ Le LLM n'est pas configuré.

1) cp .env.example .env
2) Remplis .env (service en ligne OU Ollama local) :
       LLM_BASE_URL=http://localhost:11434/v1
       LLM_API_KEY=ollama
       LLM_MODEL=llama3.2
3) Relance le script.

⚠️ Pour les démos 1, 2, 4 (tool calling), choisis un modèle qui supporte
   les "tools" (gpt-4o-mini, mistral, llama3.1/llama3.2 récents...).
"""


def config_ok():
    return bool(LLM_MODEL and (LLM_API_KEY or LLM_BASE_URL))


def obtenir_client():
    if not config_ok():
        print(_MESSAGE_AIDE)
        sys.exit(1)

    from openai import OpenAI

    client = OpenAI(
        base_url=LLM_BASE_URL or None,
        api_key=LLM_API_KEY or "non-utilise",
    )
    return client, LLM_MODEL
