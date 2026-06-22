# ============================================================
# 1_premier_appel.py - Ton premier appel à un LLM
# ============================================================
# Le "Hello World" des LLM : on envoie un message, on lit la réponse.
#
# Prérequis : avoir configuré ton .env (voir README + .env.example).
# Lancement :   python 1_premier_appel.py
# ============================================================

import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

# Lit la config écrite dans le fichier .env (placé à côté de ce script)
load_dotenv(Path(__file__).resolve().parent / ".env")

# Le client qui parle au LLM, via l'interface compatible OpenAI.
# Par défaut on cible Anthropic (Claude) ; le .env peut pointer ailleurs
# (OpenAI, Mistral, Ollama en local…) sans toucher au code.
client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL"),
    api_key=os.getenv("LLM_API_KEY"),
)
modele = os.getenv("LLM_MODEL")

print(f"Modèle utilisé : {modele}\n")

# ------------------------------------------------------------
# 1. Un appel minimal : juste un message "user"
# ------------------------------------------------------------
messages = [
    {"role": "user", "content": "Explique ce qu'est un token, en une phrase simple."},
]

reponse = client.chat.completions.create(
    model=modele,
    messages=messages,
    temperature=0.7,
)
print("🤖", reponse.choices[0].message.content)

# ------------------------------------------------------------
# 🔧 À TOI DE JOUER
# ------------------------------------------------------------
# 1. Change la question et relance.
# 2. Pose deux fois EXACTEMENT la même question : la réponse est-elle identique ?
#    (la température par défaut introduit de la variabilité - voir démo 2)
# 3. Demande une réponse "en 3 points" : le modèle respecte-t-il la consigne de format ?
