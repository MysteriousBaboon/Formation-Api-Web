# ============================================================
# 4_agent_multi_outils.py — Un agent qui CHOISIT entre plusieurs outils
# ============================================================
# Un vrai mini-agent : on lui donne plusieurs outils, et une BOUCLE qui
# le laisse en appeler autant qu'il faut (un, puis un autre...) jusqu'à
# pouvoir répondre. Avec un garde-fou anti-boucle infinie.
#
# Lancement :   python 4_agent_multi_outils.py
# ============================================================

import json
from config import obtenir_client
from outils import calculer, obtenir_meteo, heure_actuelle

client, modele = obtenir_client()

# ------------------------------------------------------------
# 1. Le registre : nom d'outil → vraie fonction Python
# ------------------------------------------------------------
REGISTRE = {
    "calculer": lambda expression: calculer(expression),
    "obtenir_meteo": lambda ville: obtenir_meteo(ville),
    "heure_actuelle": lambda: heure_actuelle(),
}

# 2. La description de chaque outil pour le LLM
OUTILS = [
    {"type": "function", "function": {
        "name": "calculer",
        "description": "Évalue une expression arithmétique. À utiliser pour tout calcul.",
        "parameters": {"type": "object", "properties": {
            "expression": {"type": "string"}}, "required": ["expression"]}}},
    {"type": "function", "function": {
        "name": "obtenir_meteo",
        "description": "Donne la météo actuelle d'une ville.",
        "parameters": {"type": "object", "properties": {
            "ville": {"type": "string"}}, "required": ["ville"]}}},
    {"type": "function", "function": {
        "name": "heure_actuelle",
        "description": "Donne la date et l'heure actuelles.",
        "parameters": {"type": "object", "properties": {}}}},
]


def agent(question, max_tours=6):
    print(f"❓ {question}\n" + "=" * 60)
    messages = [
        {"role": "system", "content": "Tu es un assistant qui utilise des outils quand c'est utile. "
                                       "Réponds en français."},
        {"role": "user", "content": question},
    ]

    for tour in range(1, max_tours + 1):
        reponse = client.chat.completions.create(
            model=modele, messages=messages, tools=OUTILS, temperature=0,
        )
        message = reponse.choices[0].message

        # Pas d'outil demandé → c'est la réponse finale
        if not message.tool_calls:
            print("✅ Réponse finale :", message.content)
            return message.content

        # Sinon, on exécute TOUS les outils demandés ce tour-ci
        messages.append(message)
        for appel in message.tool_calls:
            nom = appel.function.name
            args = json.loads(appel.function.arguments or "{}")
            resultat = REGISTRE[nom](**args)
            print(f"[tour {tour}] 🛠️  {nom}({args}) → {resultat}")
            messages.append({"role": "tool", "tool_call_id": appel.id, "content": str(resultat)})

    print("⏹️  Nombre de tours maximum atteint (garde-fou).")
    return None


# Une question qui peut mobiliser PLUSIEURS outils
agent("Quelle heure est-il, et quel temps fait-il à Marseille ? "
      "Et combien font 15 % de 240 ?")

# ------------------------------------------------------------
# 🔧 À TOI DE JOUER
# ------------------------------------------------------------
# 1. Observe l'ordre dans lequel l'agent appelle les outils.
# 2. Ajoute ton propre outil (ex. une fonction 'convertir_euros_dollars(montant)')
#    dans REGISTRE *et* dans OUTILS, puis pose une question qui l'utilise.
# 3. Baisse max_tours et vois le garde-fou se déclencher.
