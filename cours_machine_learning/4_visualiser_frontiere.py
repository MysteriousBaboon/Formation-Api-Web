# ============================================================
# 4_visualiser_frontiere.py — Voir la "frontière de décision"
# ============================================================
# Un modèle de classification découpe l'espace en zones : "ici c'est
# l'espèce A, là c'est la B...". Cette ligne entre les zones s'appelle
# la FRONTIÈRE DE DÉCISION. On va la dessiner.
#
# Pour pouvoir la voir en 2D, on n'utilise que 2 des 4 features.
# Le script génère une image : frontiere.png
#
# Lancement :   python 4_visualiser_frontiere.py
# ============================================================

import numpy as np
import matplotlib
matplotlib.use("Agg")            # backend "fichier" : pas besoin d'écran
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
# On garde seulement 2 features (longueur & largeur du pétale) pour dessiner en 2D
X = iris.data[:, 2:4]
y = iris.target

# ------------------------------------------------------------
# 1. Entraîner le modèle sur ces 2 features
# ------------------------------------------------------------
modele = KNeighborsClassifier(n_neighbors=5)
modele.fit(X, y)

# ------------------------------------------------------------
# 2. Construire une grille de points couvrant tout le plan
# ------------------------------------------------------------
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
xx, yy = np.meshgrid(
    np.arange(x_min, x_max, 0.02),
    np.arange(y_min, y_max, 0.02),
)

# 3. Demander au modèle de prédire la classe de CHAQUE point de la grille
Z = modele.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# ------------------------------------------------------------
# 4. Dessiner les zones (frontière) + les vraies fleurs par-dessus
# ------------------------------------------------------------
plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, Z, alpha=0.3, cmap="viridis")   # les zones colorées
scatter = plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor="k", cmap="viridis")
plt.xlabel(iris.feature_names[2])
plt.ylabel(iris.feature_names[3])
plt.title("Frontière de décision d'un k-NN (k=5) sur 2 features")
plt.legend(handles=scatter.legend_elements()[0], labels=list(iris.target_names))

plt.savefig("frontiere.png", dpi=110, bbox_inches="tight")
print("✅ Image générée : frontiere.png")
print("Ouvre-la : chaque couleur de fond = la zone où le modèle prédit cette espèce.")

# ------------------------------------------------------------
# 🔧 À TOI DE JOUER
# ------------------------------------------------------------
# 1. Mets n_neighbors=1 : la frontière devient "déchiquetée" (sur-apprentissage visuel !).
# 2. Mets n_neighbors=30 : la frontière devient très lisse (modèle plus "prudent").
# 3. Change les 2 features utilisées (ligne X = iris.data[:, 0:2] pour les sépales).
