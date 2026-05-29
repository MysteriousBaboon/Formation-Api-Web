# ============================================================
# 2_personnalisation.py — Rendre un graphe lisible et pro
# ============================================================
# Un graphe par défaut est moche. Avec 5-6 réglages il devient
# présentable à un client. On voit aussi comment SAUVEGARDER
# une image au lieu de l'afficher.
# ============================================================

import matplotlib.pyplot as plt

mois = ["Jan", "Fev", "Mar", "Avr", "Mai"]
ventes_2025 = [80, 100, 95, 120, 140]
ventes_2026 = [100, 130, 90, 160, 200]

# ------------------------------------------------------------
# 1. La taille de la figure (largeur, hauteur en pouces)
# ------------------------------------------------------------
plt.figure(figsize=(10, 5))

# ------------------------------------------------------------
# 2. Plusieurs séries + couleurs + légende
# ------------------------------------------------------------
plt.plot(mois, ventes_2025, label="2025", color="#a4b894", marker="|")
plt.plot(mois, ventes_2026, label="2026", color="#2563eb", marker="8", linewidth=2)

# ------------------------------------------------------------
# 3. Titres et axes soignés
# ------------------------------------------------------------
plt.title("Évolution des ventes", fontsize=14, fontweight="bold")
plt.xlabel("Mois")
plt.ylabel("Ventes (k€)")

# ------------------------------------------------------------
# 4. Grille légère + légende
# ------------------------------------------------------------
plt.grid(axis="y", alpha=0.1)   # alpha = transparence (0 = invisible, 1 = plein)
plt.legend()

# ------------------------------------------------------------
# 5. Éviter que ça déborde
# ------------------------------------------------------------
plt.tight_layout()

# ------------------------------------------------------------
# 6. SAUVEGARDER au lieu d'afficher
# ------------------------------------------------------------
# Sur un serveur, on ne peut pas faire plt.show() : on sauve un fichier.
plt.savefig("ventes_2026.png", dpi=150, bbox_inches="tight")
plt.close()   # TOUJOURS fermer après un savefig (libère la mémoire)

print("Graphique sauvegardé dans ventes_2026.png")

# ------------------------------------------------------------
# 7. Bonus : labels inclinés (utile pour des noms longs)
# ------------------------------------------------------------
produits = ["iPhone 15 Pro Max", "Galaxy S24 Ultra", "Pixel 8 Pro", "Xperia 1"]
stock = [12, 8, 5, 3]

plt.figure(figsize=(8, 5))
plt.bar(produits, stock, color="#16a34a")
plt.title("Stock par produit")
plt.xticks(rotation=45, ha="left")  # incliner pour que ça rentre
plt.tight_layout()
plt.savefig("stock.png", dpi=150)
plt.close()
print("Graphique sauvegardé dans stock.png")