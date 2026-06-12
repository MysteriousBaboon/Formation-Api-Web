# ============================================================
# 1_premier_modele.py — Ton premier modèle de ML, en 4 lignes
# ============================================================
# Objectif : entraîner une IA qui reconnaît l'espèce d'une fleur
# (le célèbre jeu de données "Iris", fourni avec scikit-learn).
#
# Le workflow du cours, étape par étape :
#   1. Données → 2. Features/labels → 4. Entraînement → 6. Prédiction
#
# Lancement :   python 1_premier_modele.py
# ============================================================

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

# ------------------------------------------------------------
# 1. Les données (fournies avec scikit-learn, rien à télécharger)
# ------------------------------------------------------------
iris = load_iris()

X = iris.data       # les FEATURES : 4 mesures par fleur (longueur/largeur pétale & sépale)
y = iris.target     # les LABELS  : l'espèce (0, 1 ou 2)

print("Nombre d'exemples :", len(X))
print("Features (mesures) :", iris.feature_names)
print("Classes (espèces)  :", list(map(str, iris.target_names)))
print("Exemple — la 1re fleur :", X[0], "→ espèce", iris.target_names[y[0]])
print("-" * 55)

# ------------------------------------------------------------
# 2. Choisir + entraîner un modèle (les fameuses 4 lignes)
# ------------------------------------------------------------
modele = KNeighborsClassifier(n_neighbors=3)   # "regarde les 3 voisins les plus proches"
modele.fit(X, y)                                # APPRENTISSAGE : le modèle mémorise les exemples

# ------------------------------------------------------------
# 3. Prédire l'espèce d'une NOUVELLE fleur
# ------------------------------------------------------------
# Une fleur jamais vue : [longueur sépale, largeur sépale, longueur pétale, largeur pétale]
nouvelle_fleur = [[5.1, 3.5, 1.4, 0.2]]
prediction = modele.predict(nouvelle_fleur)

print("Nouvelle fleur :", nouvelle_fleur[0])
print("➡️  Espèce prédite :", iris.target_names[prediction[0]])
print("-" * 55)

# ------------------------------------------------------------
# 🔧 À TOI DE JOUER
# ------------------------------------------------------------
# 1. Change les mesures de `nouvelle_fleur` et relance. La prédiction change-t-elle ?
# 2. Change n_neighbors=3 en n_neighbors=1, puis 15. Une intuition de l'effet ?
# 3. Remplace KNeighborsClassifier par DecisionTreeClassifier
#    (from sklearn.tree import DecisionTreeClassifier) — le reste du code ne bouge pas !
