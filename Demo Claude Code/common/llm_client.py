# ============================================================
# common/llm_client.py — Accès LLM (interface compatible OpenAI)
# ============================================================
# On utilise le SDK `openai` piloté par le .env (LLM_BASE_URL,
# LLM_API_KEY, LLM_MODEL) — cible Anthropic par défaut, comme dans
# les cours. Garde-fous : si la clé manque, on lève une exception
# que les blueprints transforment en HTTP 503 explicite.
# ============================================================

from openai import OpenAI

from config import config

TIMEOUT = 30  # secondes


class LLMIndisponible(Exception):
    """Levée quand la configuration LLM est absente/incomplète."""


class EmbeddingsIndisponibles(Exception):
    """Levée quand aucun fournisseur d'embeddings n'est configuré."""


def _client_chat():
    if not config.llm_pret():
        raise LLMIndisponible(
            "Aucune clé LLM configurée. Renseigne LLM_API_KEY (et LLM_BASE_URL / "
            "LLM_MODEL) dans le .env. Voir .env.example."
        )
    return OpenAI(base_url=config.LLM_BASE_URL, api_key=config.LLM_API_KEY,
                  timeout=TIMEOUT)


def completion(messages, max_tokens=300, temperature=0.7, tools=None, stop=None):
    """Appelle le modèle de chat et renvoie l'objet réponse complet."""
    client = _client_chat()
    kwargs = {
        "model": config.LLM_MODEL,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
    }
    if tools is not None:
        kwargs["tools"] = tools
    if stop is not None:
        kwargs["stop"] = stop
    return client.chat.completions.create(**kwargs)


def chat_text(messages, **kwargs):
    """Raccourci : renvoie directement le texte de la réponse."""
    reponse = completion(messages, **kwargs)
    return reponse.choices[0].message.content


def embeddings(textes):
    """Calcule les embeddings d'une liste de textes (fournisseur EMBED_*)."""
    if not config.embeddings_prets():
        raise EmbeddingsIndisponibles(
            "Embeddings non disponibles : Anthropic n'en fournit pas. Configure "
            "EMBED_BASE_URL / EMBED_API_KEY / LLM_EMBED_MODEL (Voyage AI, OpenAI, "
            "ou Ollama) dans le .env."
        )
    client = OpenAI(base_url=config.EMBED_BASE_URL, api_key=config.EMBED_API_KEY,
                    timeout=TIMEOUT)
    reponse = client.embeddings.create(model=config.EMBED_MODEL, input=textes)
    return [donnee.embedding for donnee in reponse.data]
