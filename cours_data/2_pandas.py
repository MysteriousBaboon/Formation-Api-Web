# ============================================================
# 2_pandas.py — Le couteau suisse de la data en Python
# ============================================================
# Pandas est UNE des librairies les plus utilisees au monde.
# Elle te permet de manipuler des tableaux comme dans Excel,
# mais avec la puissance de Python.
# ============================================================

import pandas as pd


# ============================================================
# 1. Charger un fichier
# ============================================================
df = pd.read_csv("data/ventes.csv")
# df = DataFrame = tableau pandas. C'est l'objet central.

print("Apercu :")
print(df.head())        # 5 premieres lignes
print()
print("Dimensions :", df.shape)        # (lignes, colonnes)
print("Colonnes :", list(df.columns))
print()


# ============================================================
# 2. Stats automatiques
# ============================================================
print("Statistiques sur les colonnes numeriques :")
print(df.describe())
print()


# ============================================================
# 3. Selection de colonnes
# ============================================================
prix = df["prix"]                     # une seule colonne (Series)
sous_tableau = df[["produit", "prix"]] # plusieurs colonnes (DataFrame)


# ============================================================
# 4. Filtrer des lignes
# ============================================================
chers = df[df["prix"] > 50]
print(f"Produits a plus de 50 EUR : {len(chers)} lignes")

# Combiner plusieurs conditions avec & (et) et | (ou)
# Bien mettre des parentheses autour de chaque condition !
vetements_chers = df[(df["categorie"] == "vetements") & (df["prix"] > 30)]
print(f"Vetements > 30 EUR : {len(vetements_chers)} lignes")
print()


# ============================================================
# 5. Creer une colonne calculee
# ============================================================
df["total"] = df["prix"] * df["quantite"]
print("Apres ajout colonne total :")
print(df.head())
print()


# ============================================================
# 6. Trier
# ============================================================
top_ventes = df.sort_values("total", ascending=False).head(10)
print("Top 10 des ventes par total :")
print(top_ventes)
print()


# ============================================================
# 7. GROUPBY — LE pattern le plus utile
# ============================================================
# "Pour chaque categorie, calcule la somme du total"
ca_par_categorie = df.groupby("categorie")["total"].sum()
print("CA par categorie :")
print(ca_par_categorie)
print()

# "Pour chaque vendeur, combien de ventes et combien de CA ?"
perf_vendeurs = df.groupby("vendeur").agg(
    nb_ventes=("total", "size"),
    ca_total=("total", "sum"),
    ca_moyen=("total", "mean"),
)
print("Performance vendeurs :")
print(perf_vendeurs)
print()


# ============================================================
# 8. Exporter
# ============================================================
ca_par_categorie.to_csv("data/rapport_ca.csv")
perf_vendeurs.to_excel("data/perf_vendeurs.xlsx")
print("Rapports exportes dans data/")
