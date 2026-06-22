# ============================================================
# corriges/exo_3_avis.py - Analyseur d'avis automatique (exo 3.3)
# ============================================================
# On boucle sur une liste d'avis, on demande un JSON pour chacun,
# on le parse, et on affiche un mini-rapport.
# ============================================================

import json
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

# Lit la config écrite dans le .env du dossier parent (cours_llm/.env)
load_dotenv(Path(__file__).resolve().parents[1] / ".env")

# Le client qui parle au LLM, via l'interface compatible OpenAI.
# Par défaut on cible Anthropic (Claude) ; le .env peut pointer ailleurs
# (OpenAI, Mistral, Ollama en local…) sans toucher au code.
client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL"),
    api_key=os.getenv("LLM_API_KEY"),
)
modele = os.getenv("LLM_MODEL")

AVIS = [
    "Livraison rapide mais le produit est arrivé cassé, très déçu.",
    "Parfait ! Exactement ce que je cherchais, je recommande les yeux fermés.",
    "Correct sans plus. Le prix est un peu élevé pour la qualité.",
]

CONSIGNE = (
    "Tu analyses des avis clients. Réponds UNIQUEMENT avec un objet JSON valide, "
    "sans texte autour, avec ces clés : "
    '"sentiment" ("positif"|"neutre"|"negatif"), "note" (entier 1-5).'
)


def analyser(avis):
    reponse = client.chat.completions.create(
        model=modele,
        messages=[
            {"role": "system", "content": CONSIGNE},
            {"role": "user", "content": avis},
        ],
        temperature=0,
    )
    texte = reponse.choices[0].message.content
    propre = texte.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    return json.loads(propre)


print(f"{'sentiment':>10} | {'note':>4} | avis")
print("-" * 70)
for avis in AVIS:
    try:
        d = analyser(avis)
        print(f"{d.get('sentiment',''):>10} | {str(d.get('note','')):>4} | {avis[:45]}...")
    except json.JSONDecodeError:
        print(f"{'(JSON KO)':>10} |      | {avis[:45]}...")
