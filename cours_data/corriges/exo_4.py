# ============================================================
# Exo 4 — Renommage et tri en masse
# ============================================================
# Objectifs :
#   1. Lister tous les fichiers de data/fichiers_a_renommer/
#   2. Mettre l'extension en minuscules + prefixer par la date
#   3. Creer data/tries/<extension>/ et y deplacer chaque fichier
#   4. Mini-rapport : combien traites, combien par extension
#
# /!\ Si tu relances ce script, les fichiers ont deja ete deplaces.
#     Pour rejouer proprement : python 0_setup.py
# ============================================================

from pathlib import Path
from datetime import date, datetime
from collections import Counter


# ============================================================
# 1. Setup des chemins
# ============================================================
source = Path("data/fichiers_a_renommer")
destination = Path("data/tries")
destination.mkdir(exist_ok=True)

print(date.today())
aujourdhui = date.today().isoformat()   # "2025-05-21"
aujourdhui = datetime.strptime(aujourdhui,"%Y-%m-%d").strftime("%A-%b-%Y")

# ============================================================
# 2. Boucle de traitement
# ============================================================
# Counter = dict specialise pour compter. Counter()["jpg"] += 1
# marche meme si la cle n'existe pas encore.
compteur = Counter()

fichiers = []
for f in source.iterdir():
    if f.is_file():
        fichiers.append(f)

fichiers = [f for f in source.iterdir() if f.is_file()]

for f in fichiers:
    # Extension en minuscules. f.suffix vaut ".JPG", on enleve le point.
    ext = f.suffix.lower().lstrip(".")

    # Nouveau nom : "2025-05-21_IMG_1234.jpg"
    # f.stem = nom sans extension, on rajoute l'extension lower derriere.
    nouveau_nom = f"{aujourdhui}_{f.stem}.{ext}"

    # Sous-dossier par extension. mkdir(parents=True) cree aussi
    # les parents si besoin ; exist_ok=True evite l'erreur s'il existe.
    sous_dossier = destination / ext
    sous_dossier.mkdir(parents=True, exist_ok=True)

    cible = sous_dossier / nouveau_nom

    # f.rename(cible) deplace ET renomme en une seule operation.
    f.rename(cible)

    compteur[ext] += 1


# ============================================================
# 3. Mini-rapport
# ============================================================
print("=" * 50)
print("Rapport")
print("=" * 50)
print(f"Fichiers traites : {sum(compteur.values())}")
for ext, n in compteur.most_common():
    print(f"  .{ext} : {n}")

source.rmdir() 