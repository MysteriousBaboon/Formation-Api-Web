# ============================================================
# corriges/mon_agent.py — Projet fil rouge : assistant de budget
# ============================================================
# Un agent qui aide à gérer un petit budget : il calcule (calculatrice)
# et garde une "note" de dépenses (un outil qui écrit dans une liste).
# Il choisit l'outil selon la demande, avec un garde-fou anti-boucle.
# ============================================================

import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

# Rend le dossier parent importable (pour outils.py) et lit son .env
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from outils import calculer

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

# Le client qui parle au LLM, via l'interface compatible OpenAI.
# Par défaut on cible Anthropic (Claude) ; le .env peut pointer ailleurs
# (OpenAI, Mistral, Ollama en local…) sans toucher au code.
client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL"),
    api_key=os.getenv("LLM_API_KEY"),
)
modele = os.getenv("LLM_MODEL")

# Une "mémoire" toute simple : la liste des dépenses enregistrées
DEPENSES = []


def enregistrer_depense(libelle, montant):
    DEPENSES.append({"libelle": libelle, "montant": float(montant)})
    total = sum(d["montant"] for d in DEPENSES)
    return f"Dépense enregistrée. Total actuel : {total:.2f} €."


REGISTRE = {
    "calculer": lambda expression: calculer(expression),
    "enregistrer_depense": lambda libelle, montant: enregistrer_depense(libelle, montant),
}

OUTILS = [
    {"type": "function", "function": {
        "name": "calculer",
        "description": "Évalue un calcul arithmétique.",
        "parameters": {"type": "object", "properties": {
            "expression": {"type": "string"}}, "required": ["expression"]}}},
    {"type": "function", "function": {
        "name": "enregistrer_depense",
        "description": "Enregistre une dépense et renvoie le total cumulé.",
        "parameters": {"type": "object", "properties": {
            "libelle": {"type": "string"},
            "montant": {"type": "number"}},
            "required": ["libelle", "montant"]}}},
]


def agent(demande, max_tours=6):
    print(f"❓ {demande}\n" + "=" * 60)
    messages = [
        {"role": "system", "content": "Tu es un assistant de budget. Utilise les outils pour "
                                       "calculer et enregistrer les dépenses. Réponds en français."},
        {"role": "user", "content": demande},
    ]
    for tour in range(1, max_tours + 1):
        rep = client.chat.completions.create(
            model=modele, messages=messages, tools=OUTILS, temperature=0)
        msg = rep.choices[0].message
        if not msg.tool_calls:
            print("✅", msg.content)
            return
        messages.append(msg)
        for appel in msg.tool_calls:
            args = json.loads(appel.function.arguments or "{}")
            res = REGISTRE[appel.function.name](**args)
            print(f"[tour {tour}] 🛠️  {appel.function.name}({args}) → {res}")
            messages.append({"role": "tool", "tool_call_id": appel.id, "content": str(res)})
    print("⏹️  Garde-fou atteint.")


if __name__ == "__main__":
    agent("J'ai dépensé 12,50 € au resto et 4 € de café. "
          "Enregistre-les, puis dis-moi combien il me reste sur un budget de 50 €.")
