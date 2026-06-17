# ============================================================
# 2_prompting.py — Rôle système, few-shot, température
# ============================================================
# La même question peut donner des réponses très différentes selon
# COMMENT on la pose. On illustre trois leviers :
#   - le message "system" (le cadre / la personnalité)
#   - le "few-shot" (donner des exemples)
#   - la "température" (créativité vs fiabilité)
#
# Lancement :   python 2_prompting.py
# ============================================================

from config import obtenir_client, demander

client, modele = obtenir_client()

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
    print("🤖", demander(client, modele, messages, temperature=0.7))
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
print("🤖", demander(client, modele, messages, temperature=0))

# ------------------------------------------------------------
# 3. La température : fiabilité (0) vs créativité (1.2)
# ------------------------------------------------------------
print("\n=== 3. Température : 0 (stable) vs 1.2 (créatif) ===\n")

messages = [
    {"role": "user", "content": "Invente un nom de start-up qui vend du café."},
]
for temp in [0, 1.2]:
    print(f"température = {temp}")
    print("🤖", demander(client, modele, messages, temperature=temp))
    print("-" * 60)

# ------------------------------------------------------------
# 🔧 À TOI DE JOUER
# ------------------------------------------------------------
# 1. Ajoute une 3e personnalité (ex. "Tu es un pirate"). L'effet est-il net ?
# 2. Dans le few-shot, retire les 2 exemples : le modèle répond-il encore en émojis ?
# 3. Lance plusieurs fois la partie 3 : la réponse à température=0 bouge-t-elle ? Et à 1.2 ?
