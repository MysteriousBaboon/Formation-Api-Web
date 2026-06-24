# ============================================================
# 5_agent_vers_n8n.py — L'agent AGIT sur le monde réel
# ============================================================
# Le saut final : un outil qui ne se contente pas de lire, mais qui
# DÉCLENCHE quelque chose à l'extérieur — ici un webhook (n8n, ou
# https://webhook.site pour tester). L'agent rédige une alerte et l'envoie.
#
# C'est le pont avec tes cours précédents :
#   - l'outil pourrait être TON micro-service Python (cours 3)
#   - n8n (cours 7) peut recevoir ça et le distribuer (Slack, email...)
#
# Configure N8N_WEBHOOK_URL dans .env (ou laisse vide → envoi simulé).
# Lancement :   python 5_agent_vers_n8n.py
# ============================================================

import os
import json
from pathlib import Path

import requests
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
WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL", "").strip()


# ------------------------------------------------------------
# L'outil qui AGIT : envoyer un message vers un webhook
# ------------------------------------------------------------
def envoyer_alerte(titre, message):
    """Envoie une alerte vers le webhook n8n (ou simule si non configuré)."""
    charge = {"titre": titre, "message": message}

    if not WEBHOOK_URL:
        print(f"   📭 (simulé — pas de N8N_WEBHOOK_URL) : {charge}")
        return "Alerte envoyée (simulation)."

    try:
        r = requests.post(WEBHOOK_URL, json=charge, timeout=10)
        return f"Alerte envoyée, statut HTTP {r.status_code}."
    except requests.RequestException as e:
        return f"Échec de l'envoi : {e}"


OUTILS = [
    {"type": "function", "function": {
        "name": "envoyer_alerte",
        "description": "Envoie une alerte/notification vers le système externe (n8n). "
                       "À utiliser quand l'utilisateur veut notifier ou alerter quelqu'un.",
        "parameters": {"type": "object", "properties": {
            "titre": {"type": "string", "description": "Titre court de l'alerte"},
            "message": {"type": "string", "description": "Le corps du message"},
        }, "required": ["titre", "message"]}}},
]


def agent(demande, max_tours=4):
    print(f"❓ {demande}\n" + "=" * 60)
    messages = [
        {"role": "system", "content": "Tu es un assistant qui peut envoyer des alertes. "
                                       "Rédige un message clair avant d'envoyer."},
        {"role": "user", "content": demande},
    ]

    for tour in range(1, max_tours + 1):
        reponse = client.chat.completions.create(
            model=modele, messages=messages, tools=OUTILS, temperature=0.3,
        )
        message = reponse.choices[0].message

        if not message.tool_calls:
            print("✅ Réponse finale :", message.content)
            return

        messages.append(message)
        for appel in message.tool_calls:
            args = json.loads(appel.function.arguments or "{}")
            print(f"[tour {tour}] 🛠️  envoyer_alerte(titre={args.get('titre')!r})")
            resultat = envoyer_alerte(**args)
            print(f"   → {resultat}")
            messages.append({"role": "tool", "tool_call_id": appel.id, "content": resultat})

    print("⏹️  Garde-fou : trop de tours.")


agent("Le stock du produit 'Café Premium' est tombé à 2 unités. "
      "Préviens l'équipe avec une alerte.")

# ------------------------------------------------------------
# 🔧 À TOI DE JOUER
# ------------------------------------------------------------
# 1. Crée un webhook gratuit sur https://webhook.site, colle l'URL dans .env
#    (N8N_WEBHOOK_URL=...), relance : tu VOIS l'alerte arriver dans le navigateur.
# 2. Dans n8n : un "Webhook Trigger" qui reçoit ça → un nœud Slack/Email. L'agent
#    déclenche un vrai workflow !
# 3. Remplace envoyer_alerte par un appel à TON micro-service du cours 3
#    (requests.post vers ton endpoint). L'agent pilote ton propre code.
