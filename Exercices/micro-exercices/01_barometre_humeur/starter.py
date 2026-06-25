# ============================================================
# starter.py — Baromètre d'humeur (à compléter)
# ============================================================
# Lancement :  python starter.py
# ============================================================

# Les votes du jour (humeurs récoltées dans le salon d'équipe)
votes = [
    "au top", "ça va", "bof", "au top", "fatigué",
    "au top", "ras-le-bol", "ça va", "au top", "bof",
    "ça va", "au top", "fatigué", "ras-le-bol", "ça va",
    "bof", "au top", "ça va", "ras-le-bol", "fatigué",
    "au top", "bof", "ras-le-bol", "ça va", "au top",
]

# Pour le rendu visuel
EMOJIS = {
    "au top": "🤩", "ça va": "🙂", "bof": "😐",
    "fatigué": "😴", "ras-le-bol": "😡",
}
COULEURS = {
    "au top": "\033[92m",      # vert vif
    "ça va": "\033[96m",       # cyan
    "bof": "\033[93m",         # jaune
    "fatigué": "\033[94m",     # bleu
    "ras-le-bol": "\033[91m",  # rouge
}
RESET = "\033[0m"
ORDRE = ["au top", "ça va", "bof", "fatigué", "ras-le-bol"]

# TODO 1 : compter chaque humeur dans un dict `compte`

# TODO 2 : calculer le total et le maximum

# TODO 3 à 5 : pour chaque humeur de ORDRE, afficher une barre colorée
#              proportionnelle + le nombre + le pourcentage

# TODO 6 : afficher l'humeur dominante
