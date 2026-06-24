# ============================================================
# config.py — Configuration centralisée (lue depuis .env)
# ============================================================
# On charge plusieurs .env, sans écraser ce qui est déjà défini :
#   1. le .env de cette démo (prioritaire)
#   2. le .env de cours_llm/ (clés LLM réelles de la formation)
#   3. le .env de cours_agents_llm/ (config agents)
#   4. le .env racine du repo (API_TOKEN, FLASK_DEBUG)
# Ainsi la démo fonctionne « out of the box » avec la config
# déjà en place pour les cours, sans rien dupliquer.
# ============================================================

import os
from pathlib import Path

from dotenv import load_dotenv

ICI = Path(__file__).resolve().parent          # .../Demo Claude Code
REPO = ICI.parent                               # .../La Dinguerie

# Ordre = priorité décroissante (override=False : on ne remplace pas).
for chemin in (
    ICI / ".env",
    REPO / "cours_llm" / ".env",
    REPO / "cours_agents_llm" / ".env",
    REPO / ".env",
):
    if chemin.exists():
        load_dotenv(chemin, override=False)


class Config:
    """Regroupe toutes les variables d'environnement utiles."""

    # --- Serveur ---
    DEBUG = os.getenv("FLASK_DEBUG", "true").lower() == "true"
    PORT = int(os.getenv("PORT", "5000"))

    # --- Authentification (Bearer) ---
    API_TOKEN = os.getenv("API_TOKEN", "dev-token-change-me")

    # --- LLM (interface compatible OpenAI ; cible Anthropic par défaut) ---
    LLM_BASE_URL = os.getenv("LLM_BASE_URL", "https://api.anthropic.com/v1/")
    LLM_API_KEY = os.getenv("LLM_API_KEY", "")
    LLM_MODEL = os.getenv("LLM_MODEL", "claude-sonnet-4-6")

    # --- Embeddings (Anthropic n'en fournit pas : Voyage / OpenAI / Ollama) ---
    # Le cours utilise LLM_EMBED_MODEL ; on accepte aussi EMBED_MODEL en repli.
    EMBED_BASE_URL = os.getenv("EMBED_BASE_URL", "") or os.getenv("LLM_BASE_URL", "")
    EMBED_API_KEY = os.getenv("EMBED_API_KEY", "") or os.getenv("LLM_API_KEY", "")
    EMBED_MODEL = os.getenv("LLM_EMBED_MODEL", "") or os.getenv("EMBED_MODEL", "")

    # --- Agents : webhook n8n optionnel ---
    N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL", "")

    @classmethod
    def llm_pret(cls):
        """True si une clé LLM est configurée."""
        return bool(cls.LLM_API_KEY)

    @classmethod
    def embeddings_prets(cls):
        """True si les embeddings sont configurables."""
        return bool(cls.EMBED_BASE_URL and cls.EMBED_MODEL and cls.EMBED_API_KEY)


config = Config()
