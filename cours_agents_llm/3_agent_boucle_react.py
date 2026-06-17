# ============================================================
# 3_agent_boucle_react.py — La boucle d'agent codée À LA MAIN
# ============================================================
# Ici, PAS de tool calling natif : on construit la boucle d'agent
# nous-mêmes, par du prompt + du parsing. C'est plus rustique, mais ça
# DÉMYSTIFIE complètement ce qu'est un agent — et ça marche avec
# n'importe quel modèle (même un petit Ollama).
#
# Le motif "ReAct" : le modèle alterne
#     Pensée  →  Action  →  Observation  →  ...  →  Réponse finale
#
# Lancement :   python 3_agent_boucle_react.py
# ============================================================

import re
from config import obtenir_client
from outils import calculer, obtenir_meteo

client, modele = obtenir_client()

# Les outils disponibles, par nom
OUTILS = {
    "calculer": calculer,         # calculer[3 * 19.99]
    "meteo": obtenir_meteo,       # meteo[Lyon]
}

# ------------------------------------------------------------
# Le prompt qui apprend au modèle à raisonner en boucle
# ------------------------------------------------------------
SYSTEME = """Tu es un agent qui résout des tâches étape par étape.
Tu disposes de ces outils :
- calculer[expression]  : évalue un calcul, ex. calculer[3 * 19.99]
- meteo[ville]          : donne la météo d'une ville, ex. meteo[Lyon]

À chaque tour, réponds DANS CE FORMAT, une seule action à la fois :
Pensée: <ton raisonnement>
Action: <nom_outil>[<argument>]

Quand tu as la réponse, écris à la place :
Pensée: <ton raisonnement>
Réponse finale: <la réponse pour l'utilisateur>
"""


def executer_action(texte):
    """Cherche 'Action: outil[arg]' dans le texte et exécute l'outil."""
    m = re.search(r"Action:\s*(\w+)\[(.*?)\]", texte)
    if not m:
        return None
    nom, argument = m.group(1), m.group(2)
    if nom not in OUTILS:
        return f"Outil inconnu : {nom}"
    return OUTILS[nom](argument)


def agent(question, max_etapes=5):
    print(f"❓ {question}\n" + "=" * 60)
    messages = [
        {"role": "system", "content": SYSTEME},
        {"role": "user", "content": question},
    ]

    for etape in range(1, max_etapes + 1):
        reponse = client.chat.completions.create(
            model=modele, messages=messages, temperature=0,
            stop=["Observation:"],   # on s'arrête avant que le modèle invente l'observation
        )
        texte = reponse.choices[0].message.content.strip()
        print(f"[étape {etape}]\n{texte}")

        # Cas 1 : le modèle a fini
        if "Réponse finale:" in texte:
            finale = texte.split("Réponse finale:", 1)[1].strip()
            print("=" * 60)
            print("✅ Réponse finale :", finale)
            return finale

        # Cas 2 : le modèle veut utiliser un outil → on l'exécute
        observation = executer_action(texte)
        if observation is None:
            print("⚠️  Pas d'action détectée, on arrête.")
            return None
        print(f"🛠️  Observation: {observation}\n")

        # On rejoue le tour + l'observation pour l'étape suivante
        messages.append({"role": "assistant", "content": texte})
        messages.append({"role": "user", "content": f"Observation: {observation}"})

    print("⏹️  Nombre d'étapes maximum atteint (garde-fou anti-boucle).")
    return None


# Une tâche qui demande PLUSIEURS étapes (calcul en 2 temps)
agent("Quel est le prix TTC de 3 articles à 19,99 € avec 20 % de TVA ?")

# ------------------------------------------------------------
# 🔧 À TOI DE JOUER
# ------------------------------------------------------------
# 1. Pose une question météo : "Dois-je prendre un parapluie à Lyon ?"
# 2. Baisse max_etapes à 1 : le garde-fou se déclenche-t-il sur une tâche en 2 temps ?
# 3. Ajoute un outil dans OUTILS et dans le prompt SYSTEME (ex. 'heure').
