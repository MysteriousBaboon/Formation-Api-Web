# ============================================================
# 1_premier_appel.py — Ton premier appel à un LLM
# ============================================================
# Le "Hello World" des LLM : on envoie un message, on lit la réponse.
#
# Prérequis : avoir configuré ton .env (voir README + config.py).
# Lancement :   python 1_premier_appel.py
# ============================================================

from config import obtenir_client, demander

# Récupère le client (ou affiche l'aide si .env absent)
client, modele = obtenir_client()
print(f"Modèle utilisé : {modele}\n")

# ------------------------------------------------------------
# 1. Un appel minimal : juste un message "user"
# ------------------------------------------------------------
messages = [
    {"role": "user", "content": "Explique ce qu'est un token, en une phrase simple."},
]

reponse = demander(client, modele, messages)
print("🤖", reponse)

# ------------------------------------------------------------
# 🔧 À TOI DE JOUER
# ------------------------------------------------------------
# 1. Change la question et relance.
# 2. Pose deux fois EXACTEMENT la même question : la réponse est-elle identique ?
#    (la température par défaut introduit de la variabilité — voir démo 2)
# 3. Demande une réponse "en 3 points" : le modèle respecte-t-il la consigne de format ?
