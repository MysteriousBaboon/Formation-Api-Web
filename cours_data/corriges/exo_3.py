# ============================================================
# Exo 3 — Consolider plusieurs fichiers
# ============================================================
# Objectifs :
#   1. Lister les CSV de data/ventes_mensuelles/ avec pathlib
#   2. Charger chaque CSV, ajouter une colonne "mois" deduite
#      du nom de fichier
#   3. Concatener en un seul DataFrame
#   4. Exporter un Excel a 3 onglets : Brut, Par mois, Par categorie
# ============================================================

import pandas as pd
from pathlib import Path


# ============================================================
# 1. Lister les fichiers
# ============================================================
dossier = Path("data/ventes_mensuelles")
fichiers = sorted(dossier.glob("*.csv"))

print(f"{len(fichiers)} fichiers trouves :")
for f in fichiers:
    print(f"  {f.name}")


# ============================================================
# 2. Charger + ajouter la colonne "mois"
# ============================================================
# f.stem = nom du fichier sans extension ("janvier.csv" -> "janvier")
# C'est exactement ce qu'on veut comme valeur de mois.
dataframes = []
for f in fichiers:
    df_mois = pd.read_csv(f)
    df_mois["mois"] = f.stem
    dataframes.append(df_mois)

# ============================================================
# 3. Concatener
# ============================================================
# ignore_index=True = on refait des index propres de 0 a N
# (sinon chaque morceau garde ses anciens index et on a des doublons)
df = pd.concat(dataframes, ignore_index=True)
print(f"\nTotal apres concat : {len(df)} lignes")
print(df.head())


# ============================================================
# 4. Agregations
# ============================================================
par_mois = df.groupby("mois")["montant"].sum().sort_values(ascending=False)
par_categorie = df.groupby("categorie")["montant"].sum().sort_values(ascending=False)

print("\nMontant par mois :")
print(par_mois)
print("\nMontant par categorie :")
print(par_categorie)


# ============================================================
# 5. Export Excel multi-onglets
# ============================================================
# ExcelWriter en context manager = il sauvegarde a la sortie du with.
# Chaque to_excel ecrit dans un onglet different.
sortie = Path("data/rapport_trimestriel.xlsx")

with pd.ExcelWriter(sortie) as writer:
    df.to_excel(writer, sheet_name="Brut", index=False)
    par_mois.to_excel(writer, sheet_name="Par mois")
    par_categorie.to_excel(writer, sheet_name="Par categorie")

print(f"\nExport OK : {sortie}")