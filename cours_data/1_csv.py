# ============================================================
# 1_csv.py — Lire et ecrire des CSV avec la lib native
# ============================================================
# Pas besoin de pandas ici : la lib `csv` du standard suffit
# pour 80% des cas simples. On verra pandas juste apres.
# ============================================================

import csv
from pathlib import Path


# ============================================================
# LIRE un CSV
# ============================================================
print("=" * 50)
print("Lecture de ventes.csv")
print("=" * 50)

chemin = Path("data/ventes.csv")

with open(chemin, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    # DictReader transforme chaque ligne en dictionnaire {colonne: valeur}
    # Plus pratique que csv.reader qui renvoie des listes.
    for i, ligne in enumerate(reader):
        if i >= 5:
            break
        print(ligne)


# ============================================================
# CALCULS basiques sans pandas
# ============================================================
print("\nTotal des ventes (somme prix * quantite) :")

total = 0
with open(chemin, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for ligne in reader:
        # /!\ Les valeurs sont TOUJOURS des strings, il faut convertir
        prix = float(ligne["prix"])
        quantite = int(ligne["quantite"])
        total += prix * quantite

print(f"{total:.2f} EUR")


# ============================================================
# ECRIRE un CSV
# ============================================================
print("\nEcriture d'un nouveau CSV...")

lignes = [
    {"nom": "Alice", "score": 95},
    {"nom": "Bob", "score": 78},
    {"nom": "Charlie", "score": 88},
]

with open("data/scores.csv", "w", encoding="utf-8", newline="") as f:
    # newline="" est OBLIGATOIRE sur Windows pour eviter les lignes vides
    writer = csv.DictWriter(f, fieldnames=["nom", "score"])
    writer.writeheader()
    writer.writerows(lignes)

print("data/scores.csv cree")


# ============================================================
# PIEGE classique : separateur en ;
# ============================================================
# En France, Excel exporte souvent avec des `;` au lieu de `,`
# car la virgule est deja utilisee comme separateur decimal.
#
# Solution : preciser delimiter=";"
#
# with open(chemin, encoding="utf-8") as f:
#     reader = csv.DictReader(f, delimiter=";")
