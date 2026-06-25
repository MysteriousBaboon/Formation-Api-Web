# ============================================================
# barometre.py — Baromètre d'humeur (corrigé)
# ============================================================
# Compétence : compter avec un dict + fabriquer un affichage visuel.
# Lancement :  python barometre.py
# ============================================================

votes = [
    "au top", "ça va", "bof", "au top", "fatigué",
    "au top", "ras-le-bol", "ça va", "au top", "bof",
    "ça va", "au top", "fatigué", "ras-le-bol", "ça va",
    "bof", "au top", "ça va", "ras-le-bol", "fatigué",
    "au top", "bof", "ras-le-bol", "ça va", "au top",
]

EMOJIS = {
    "au top": "🤩", "ça va": "🙂", "bof": "😐",
    "fatigué": "😴", "ras-le-bol": "😡",
}
COULEURS = {
    "au top": "\033[92m",
    "ça va": "\033[96m",
    "bof": "\033[93m",
    "fatigué": "\033[94m",
    "ras-le-bol": "\033[91m",
}
RESET = "\033[0m"
ORDRE = ["au top", "ça va", "bof", "fatigué", "ras-le-bol"]
LARGEUR_MAX = 30  # longueur (en blocs) de la barre la plus haute


# ------------------------------------------------------------
# 1. Compter les votes : {humeur: nombre}
# ------------------------------------------------------------
# dict.get(v, 0) renvoie 0 si l'humeur n'a pas encore été vue
# -> évite un KeyError au tout premier vote de chaque type.
compte = {}
for v in votes:
    compte[v] = compte.get(v, 0) + 1

total = len(votes)
maximum = max(compte.values())


# ------------------------------------------------------------
# 2. Dessiner l'histogramme
# ------------------------------------------------------------
print(f"🌡️  Baromètre d'humeur — {total} votes\n")

for humeur in ORDRE:
    nombre = compte.get(humeur, 0)
    longueur = round(nombre / maximum * LARGEUR_MAX)
    barre = COULEURS[humeur] + "█" * longueur + RESET
    pourcentage = round(nombre / total * 100)
    etiquette = f"{EMOJIS[humeur]} {humeur}".ljust(16)
    print(f"{etiquette} | {barre} {nombre} ({pourcentage}%)")


# ------------------------------------------------------------
# 3. L'humeur dominante = la clé associée au plus grand nombre
# ------------------------------------------------------------
dominante = max(compte, key=compte.get)
print(f"\n👉 Humeur dominante : {EMOJIS[dominante]} {dominante}")
