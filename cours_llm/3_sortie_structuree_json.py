# ============================================================
# 3_sortie_structuree_json.py — Forcer une réponse en JSON
# ============================================================
# Pour brancher un LLM dans un PROGRAMME, on ne veut pas un paragraphe :
# on veut des données structurées. On demande donc du JSON, et on le
# transforme en dictionnaire Python exploitable.
#
# Lancement :   python 3_sortie_structuree_json.py
# ============================================================

import json
from config import obtenir_client, demander

client, modele = obtenir_client()

# ------------------------------------------------------------
# 1. Demander explicitement du JSON, avec le schéma voulu
# ------------------------------------------------------------
# Clé du succès : décrire PRÉCISÉMENT les champs attendus, et exiger
# "uniquement du JSON" (sans texte autour). Température 0 = fiable.
avis_client = "Livraison rapide mais le produit est arrivé cassé, très déçu."

messages = [
    {
        "role": "system",
        "content": (
            "Tu analyses des avis clients. Réponds UNIQUEMENT avec un objet JSON valide, "
            "sans texte autour, avec exactement ces clés :\n"
            '  "sentiment"  : "positif" | "neutre" | "negatif"\n'
            '  "note"       : un entier de 1 à 5\n'
            '  "themes"     : une liste de mots-clés\n'
            '  "resume"     : une phrase courte'
        ),
    },
    {"role": "user", "content": avis_client},
]

texte = demander(client, modele, messages, temperature=0)
print("Réponse brute du modèle :")
print(texte)
print("-" * 60)

# ------------------------------------------------------------
# 2. Transformer le texte JSON en vrai dictionnaire Python
# ------------------------------------------------------------
# Petit nettoyage : certains modèles entourent le JSON de ```json ... ```
texte_propre = texte.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()

try:
    donnees = json.loads(texte_propre)
    print("✅ JSON décodé en dictionnaire Python :")
    print("   sentiment :", donnees.get("sentiment"))
    print("   note      :", donnees.get("note"), "/ 5")
    print("   thèmes    :", donnees.get("themes"))
    print("   résumé    :", donnees.get("resume"))
    # ...et maintenant on pourrait l'enregistrer en base, déclencher une alerte, etc.
except json.JSONDecodeError:
    print("⚠️  Le modèle n'a pas renvoyé du JSON valide.")
    print("    Astuce : renforce la consigne, baisse la température, ou change de modèle.")

# ------------------------------------------------------------
# 🔧 À TOI DE JOUER
# ------------------------------------------------------------
# 1. Change l'avis client (un avis positif). Les champs s'adaptent-ils ?
# 2. Ajoute un champ "urgence" (true/false) dans la consigne système.
# 3. Boucle sur une LISTE d'avis et affiche un mini-rapport pour chacun.
