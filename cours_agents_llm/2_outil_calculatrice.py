# ============================================================
# 2_outil_calculatrice.py — Un outil pour ce que le LLM RATE
# ============================================================
# Les LLM "devinent" les maths, ils ne calculent pas → ils se trompent
# sur les gros nombres. La parade : leur donner une CALCULATRICE.
# On compare la réponse SANS outil et AVEC outil sur le même calcul.
#
# Lancement :   python 2_outil_calculatrice.py
# ============================================================

import json
from config import obtenir_client
from outils import calculer

client, modele = obtenir_client()

QUESTION = "Combien font 4321 multiplié par 8765, puis le tout plus 1234 ?"

# ------------------------------------------------------------
# 1. SANS outil : le LLM tente de calculer "de tête" (souvent faux)
# ------------------------------------------------------------
print("=== SANS outil (le LLM devine) ===")
sans = client.chat.completions.create(
    model=modele,
    messages=[{"role": "user", "content": QUESTION + " Donne juste le nombre."}],
)
print("🤖", sans.choices[0].message.content)
print("   (vraie réponse :", calculer("4321 * 8765 + 1234"), ")")
print("=" * 60)

# ------------------------------------------------------------
# 2. AVEC une calculatrice comme outil
# ------------------------------------------------------------
outils = [
    {
        "type": "function",
        "function": {
            "name": "calculer",
            "description": "Évalue une expression arithmétique (ex: '12 * 34 + 5'). "
                           "À utiliser pour TOUT calcul, même simple.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string", "description": "L'expression à calculer"},
                },
                "required": ["expression"],
            },
        },
    }
]

print("=== AVEC l'outil calculatrice ===")
messages = [{"role": "user", "content": QUESTION}]
reponse = client.chat.completions.create(model=modele, messages=messages, tools=outils)
message = reponse.choices[0].message

if message.tool_calls:
    messages.append(message)
    for appel in message.tool_calls:
        args = json.loads(appel.function.arguments)
        resultat = calculer(args["expression"])
        print(f"🛠️  calculer({args['expression']!r}) → {resultat}")
        messages.append({"role": "tool", "tool_call_id": appel.id, "content": resultat})

    finale = client.chat.completions.create(model=modele, messages=messages, tools=outils)
    print("🤖 Réponse finale :", finale.choices[0].message.content)
else:
    print("🤖 (le modèle n'a pas utilisé l'outil) :", message.content)

# ------------------------------------------------------------
# 🔧 À TOI DE JOUER
# ------------------------------------------------------------
# 1. Compare : la réponse SANS outil est-elle exacte ? Et AVEC ?
# 2. Essaie un calcul à plusieurs étapes : le LLM enchaîne-t-il les appels ?
# 3. Sécurité : dans outils.py, calculer('__import__("os")') est BLOQUÉ. Vérifie-le.
#    (on n'utilise jamais eval() brut sur une entrée venue du LLM !)
