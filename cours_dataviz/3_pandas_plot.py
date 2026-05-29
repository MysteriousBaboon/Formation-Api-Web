# ============================================================
# 3_pandas_plot.py — Graphes directement depuis un DataFrame
# ============================================================
# pandas sait appeler matplotlib tout seul avec .plot().
# C'est LE combo du quotidien : tu charges un CSV, tu groupes,
# tu traces. Un mini-dashboard en quelques lignes.
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# 1. Charger les données (le CSV est dans exemples/)
# ------------------------------------------------------------
df = pd.read_csv("exemples/ventes.csv")
print(df.head())

# ------------------------------------------------------------
# 2. Courbe : ventes totales par mois
# ------------------------------------------------------------
# On groupe par mois et on somme. .plot() trace direct.
ventes_par_mois = df.groupby("mois", sort=False)["ventes"].sum()
ventes_par_mois.plot(kind="line", marker="o", title="Ventes totales par mois")
plt.ylabel("Ventes")
plt.tight_layout()
plt.savefig("01_ventes_mois.png", dpi=150)
plt.close()

# ------------------------------------------------------------
# 3. Barres : ventes par région
# ------------------------------------------------------------
ventes_par_region = df.groupby("region")["ventes"].sum()
ventes_par_region.plot(kind="bar", color="#2563eb", title="Ventes par région")
plt.ylabel("Ventes")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("02_ventes_region.png", dpi=150)
plt.close()

# ------------------------------------------------------------
# 4. Camembert : répartition par catégorie
# ------------------------------------------------------------
# value_counts() compte les occurrences de chaque catégorie.
df["categorie"].value_counts().plot(
    kind="pie", autopct="%1.0f%%", title="Répartition des ventes par catégorie"
)
plt.ylabel("")  # enlève le label "categorie" sur le côté
plt.tight_layout()
plt.savefig("03_categories.png", dpi=150)
plt.close()

# ------------------------------------------------------------
# 5. Barres groupées : ventes par mois ET par région
# ------------------------------------------------------------
# pivot_table = tableau croisé (lignes = mois, colonnes = régions)
pivot = df.pivot_table(index="mois", columns="region", values="ventes", sort=False)
pivot.plot(kind="bar", title="Ventes par mois et région")
plt.ylabel("Ventes")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("04_mois_region.png", dpi=150)
plt.close()

print("4 graphiques générés (01 à 04).")
print("\nLe combo gagnant : groupby/pivot_table  +  .plot(kind=...)")