# ============================================================
# config.py — Charge le .env et fabrique le client LLM (agnostique)
# ============================================================
# Ce fichier est partagé par toutes les démos. Tu n'as PAS à le modifier.
# Il lit ton .env (LLM_BASE_URL, LLM_API_KEY, LLM_MODEL) et te renvoie
# un client prêt à l'emploi — peu importe le fournisseur.
#
# Si le .env n'est pas configuré, il affiche un message clair et s'arrête
# proprement (au lieu d'un plantage incompréhensible).
# ============================================================

import os
import sys
from pathlib import Path

from dotenv import load_dotenv

# Charger le .env qui se trouve à côté de ce fichier
load_dotenv(Path(__file__).resolve().parent / ".env")

LLM_BASE_URL = os.getenv("LLM_BASE_URL")
LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL")


_MESSAGE_AIDE = """
❌ Le LLM n'est pas configuré.

1) Copie le modèle de configuration :
       cp .env.example .env
2) Ouvre .env et remplis-le (choisis une option) :

   Option A — service en ligne :
       LLM_BASE_URL=https://api.openai.com/v1
       LLM_API_KEY=sk-ta-cle
       LLM_MODEL=gpt-4o-mini

   Option B — Ollama en local (gratuit) :
       LLM_BASE_URL=http://localhost:11434/v1
       LLM_API_KEY=ollama
       LLM_MODEL=llama3.2

3) Relance le script.
"""


def config_ok():
    """Vrai si le minimum vital est renseigné."""
    # On exige un modèle + (une clé OU une URL locale).
    return bool(LLM_MODEL and (LLM_API_KEY or LLM_BASE_URL))


def obtenir_client():
    """Renvoie (client, nom_du_modele) ou affiche l'aide et quitte."""
    if not config_ok():
        print(_MESSAGE_AIDE)
        sys.exit(1)

    from openai import OpenAI

    client = OpenAI(
        base_url=LLM_BASE_URL or None,
        api_key=LLM_API_KEY or "non-utilise",
    )
    return client, LLM_MODEL


def demander(client, modele, messages, temperature=0.7):
    """Petit raccourci : envoie des messages, renvoie le texte de la réponse."""
    reponse = client.chat.completions.create(
        model=modele,
        messages=messages,
        temperature=temperature,
    )
    return reponse.choices[0].message.content
