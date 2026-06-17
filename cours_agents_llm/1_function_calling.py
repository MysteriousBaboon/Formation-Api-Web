# ============================================================
# 1_function_calling.py — Le LLM décide d'appeler une fonction
# ============================================================
# Le concept de base d'un agent : on DÉCRIT un outil au LLM, et il répond
# (au lieu d'un texte) par une DEMANDE d'appel structurée. Notre code
# exécute la fonction, renvoie le résultat, et le LLM formule la réponse.
#
# Le flux complet en 4 temps :
#   1. on envoie la question + la description de l'outil
#   2. le LLM répond "appelle obtenir_meteo(ville='Lyon')"
#   3. NOTRE code exécute la vraie fonction Python
#   4. on renvoie le résultat → le LLM rédige la réponse finale
#
# Lancement :   python 1_function_calling.py
# ============================================================

import json
from config import obtenir_client
from outils import obtenir_meteo

client, modele = obtenir_client()

# ------------------------------------------------------------
# 1. Décrire l'outil au LLM (son nom, ce qu'il fait, ses paramètres)
# ------------------------------------------------------------
# La 'description' est CRUCIALE : c'est elle qui aide le LLM à savoir
# quand utiliser l'outil.
outils = [
    {
        "type": "function",
        "function": {
            "name": "obtenir_meteo",
            "description": "Donne la météo actuelle pour une ville donnée.",
            "parameters": {
                "type": "object",
                "properties": {
                    "ville": {"type": "string", "description": "Le nom de la ville"},
                },
                "required": ["ville"],
            },
        },
    }
]

messages = [{"role": "user", "content": "Quel temps fait-il à Lyon aujourd'hui ?"}]

# ------------------------------------------------------------
# 2. Premier appel : le LLM va-t-il demander l'outil ?
# ------------------------------------------------------------
reponse = client.chat.completions.create(model=modele, messages=messages, tools=outils)
message = reponse.choices[0].message

if not message.tool_calls:
    # Le modèle a répondu directement (sans outil)
    print("🤖 (sans outil) :", message.content)
else:
    # 3. Le LLM demande un appel d'outil → on l'exécute NOUS-MÊMES
    messages.append(message)   # on garde la demande dans l'historique
    for appel in message.tool_calls:
        arguments = json.loads(appel.function.arguments)
        print(f"🛠️  Le LLM demande : {appel.function.name}({arguments})")

        resultat = obtenir_meteo(**arguments)   # NOTRE code exécute la fonction
        print(f"   → résultat : {resultat}")

        # On renvoie le résultat au LLM, rattaché à sa demande
        messages.append({
            "role": "tool",
            "tool_call_id": appel.id,
            "content": resultat,
        })

    # 4. Deuxième appel : le LLM rédige la réponse finale avec le résultat
    reponse_finale = client.chat.completions.create(model=modele, messages=messages)
    print("\n🤖 Réponse finale :", reponse_finale.choices[0].message.content)

# ------------------------------------------------------------
# 🔧 À TOI DE JOUER
# ------------------------------------------------------------
# 1. Pose une question SANS rapport (ex. "raconte une blague"). Le LLM appelle-t-il l'outil ?
#    (non : il ne l'utilise que quand c'est pertinent — c'est lui qui décide)
# 2. Demande la météo de DEUX villes d'un coup. Combien d'appels d'outil demande-t-il ?
# 3. Améliore la description de l'outil et observe si le choix devient plus fiable.
