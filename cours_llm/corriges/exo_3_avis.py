# ============================================================
# corriges/exo_3_avis.py — Analyseur d'avis automatique (exo 3.3)
# ============================================================
# On boucle sur une liste d'avis, on demande un JSON pour chacun,
# on le parse, et on affiche un mini-rapport.
# ============================================================

import json
import sys
from pathlib import Path

# Rendre config.py (dossier parent) importable depuis corriges/
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from config import obtenir_client, demander

client, modele = obtenir_client()

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
    texte = demander(
        client, modele,
        [
            {"role": "system", "content": CONSIGNE},
            {"role": "user", "content": avis},
        ],
        temperature=0,
    )
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
