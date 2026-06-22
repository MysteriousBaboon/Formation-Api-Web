# ============================================================
# 2_prompting.py - Rôle système, few-shot, température
# ============================================================
# La même question peut donner des réponses très différentes selon
# COMMENT on la pose. On illustre trois leviers :
#   - le message "system" (le cadre / la personnalité)
#   - le "few-shot" (donner des exemples)
#   - la "température" (créativité vs fiabilité)
#
# Lancement :   python 2_prompting.py
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

# ------------------------------------------------------------
# 1. Le rôle "system" change tout
# ------------------------------------------------------------
print("=== 1. Même question, deux rôles système différents ===\n")

question = "Parle-moi de la pluie."

for personnalite in [
    "Tu es un météorologue rigoureux et factuel.",
    "Tu es un poète romantique du 19e siècle.",
]:
    messages = [
        {"role": "system", "content": personnalite},
        {"role": "user", "content": question},
    ]
    print(f"[system] {personnalite}")
    reponse = client.chat.completions.create(
        model=modele,
        messages=messages,
        temperature=0.7,
    )
    print("🤖", reponse.choices[0].message.content)
    print("-" * 60)

# ------------------------------------------------------------
# 2. Le few-shot : guider par l'exemple
# ------------------------------------------------------------
print("\n=== 2. Few-shot : on montre le format attendu ===\n")

# On donne 2 exemples (sous forme d'échange user/assistant), puis la vraie question.
messages = [
    {"role": "system", "content": "Tu transformes un plat en émoji. Réponds UNIQUEMENT par des émojis."},
    {"role": "user", "content": "pizza"},
    {"role": "assistant", "content": "🍕"},
    {"role": "user", "content": "sushi"},
    {"role": "assistant", "content": "🍣"},
    {"role": "user", "content": "salade"},   # à lui de jouer
]
print("Plat : salade")
reponse = client.chat.completions.create(
    model=modele,
    messages=messages,
    temperature=0,
)
print("🤖", reponse.choices[0].message.content)

# ------------------------------------------------------------
# 3. La température : fiabilité (0) vs créativité (1.0)
# ------------------------------------------------------------
# Note : chez Anthropic (Claude), la température va de 0 à 1.0. D'autres
# fournisseurs (OpenAI…) montent jusqu'à 2. On reste à 1.0 pour rester portable.
print("\n=== 3. Température : 0 (stable) vs 1.0 (créatif) ===\n")

messages = [
    {"role": "user", "content": "Invente un nom de start-up qui vend du café."},
]
for temp in [0, 1.0]:
    print(f"température = {temp}")
    reponse = client.chat.completions.create(
        model=modele,
        messages=messages,
        temperature=temp,
    )
    print("🤖", reponse.choices[0].message.content)
    print("-" * 60)

# ------------------------------------------------------------
# 🔧 À TOI DE JOUER
# ------------------------------------------------------------
# 1. Ajoute une 3e personnalité (ex. "Tu es un pirate"). L'effet est-il net ?
# 2. Dans le few-shot, retire les 2 exemples : le modèle répond-il encore en émojis ?
# 3. Lance plusieurs fois la partie 3 : la réponse à température=0 bouge-t-elle ? Et à 1.0 ?
