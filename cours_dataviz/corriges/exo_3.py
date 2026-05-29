# Corrigé exo 3 — Dashboard depuis le CSV
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("exemples/ventes.csv")

# 1. Barres : ventes par région
df.groupby("region")["ventes"].sum().plot(
    kind="bar", color="#2563eb", title="Ventes par région", figsize=(8, 5)
)
plt.ylabel("Ventes")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("dash_region.png", dpi=150)
plt.close()

# 2. Camembert : répartition par catégorie
df.groupby("categorie")["ventes"].sum().plot(
    kind="pie", autopct="%1.0f%%", title="Ventes par catégorie", figsize=(7, 7)
)
plt.ylabel("")
plt.tight_layout()
plt.savefig("dash_categorie.png", dpi=150)
plt.close()

# 3. Courbe : ventes par mois
df.groupby("mois", sort=False)["ventes"].sum().plot(
    kind="line", marker="o", title="Ventes par mois", figsize=(8, 5)
)
plt.ylabel("Ventes")
plt.tight_layout()
plt.savefig("dash_mois.png", dpi=150)
plt.close()

print("dash_region.png, dash_categorie.png, dash_mois.png générés.")