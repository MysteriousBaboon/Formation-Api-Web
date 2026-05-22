# ============================================================
# Exo 1 — Le CSV des ventes
# ============================================================
# Objectifs :
#   1. Charger data/ventes.csv avec pandas
#   2. Afficher nb de ventes, CA total, panier moyen
#   3. Top 3 produits en quantite
#   4. Top 3 produits en CA
#   5. Exporter le top 3 CA dans data/top3_ca.xlsx
# ============================================================

import pandas as pd
from pathlib import Path


# ============================================================
# 1. Chargement
# ============================================================
df = pd.read_csv("data/ventes.csv")
# Colonne calculee : montant de chaque ligne (prix * quantite)
df["total"] = df["prix"] * df["quantite"]


# ============================================================
# 2. Indicateurs globaux
# ============================================================
nb_ventes = len(df)
ca_total = df["total"].sum()
panier_moyen = df["total"].sum() / len(df)

print("=" * 50)
print("Indicateurs globaux")
print("=" * 50)
print(f"Nombre de ventes : {nb_ventes}")
print(f"CA total         : {ca_total:.2f} EUR")
print(f"Panier moyen     : {panier_moyen:.2f} EUR")


# ============================================================
# 3. Top 3 produits par QUANTITE vendue
# ============================================================
# groupby("produit") = "regroupe par produit"
# ["quantite"].sum() = "somme les quantites de chaque groupe"
top_quantite = (
    df.groupby("produit")["quantite"]
    .sum()
    .sort_values(ascending=True)
    .head(3)
)

print("\nTop 3 produits par quantite :")
print(top_quantite)


# ============================================================
# 4. Top 3 produits par CA
# ============================================================
top_ca = (
    df.groupby("produit")["total"]
    .sum()
    .sort_values(ascending=False)
    .head(3)
)

print("\nTop 3 produits par CA :")
print(top_ca)


# ============================================================
# 5. Export Excel
# ============================================================
# .to_frame() transforme la Series en DataFrame, plus propre a l'export.
# On renomme la colonne "total" en "ca_eur" pour que ce soit clair.
sortie = Path("data/top3_ca.xlsx")

top_ca.to_frame(name="ca_eur").to_html(sortie)

print(f"\nExport OK : {sortie}")