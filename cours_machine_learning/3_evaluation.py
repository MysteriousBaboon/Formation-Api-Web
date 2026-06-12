# ============================================================
# 3_evaluation.py — Évaluer un modèle : au-delà de l'accuracy
# ============================================================
# "Bon" ou "mauvais", ça se mesure. L'accuracy (% de bonnes réponses)
# ne suffit pas : on veut savoir QUI est confondu avec QUI.
# → la matrice de confusion + le rapport précision/rappel.
#
# Lancement :   python 3_evaluation.py
# ============================================================

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
)

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)

# ------------------------------------------------------------
# 1. Entraîner puis prédire sur le jeu de TEST
# ------------------------------------------------------------
modele = KNeighborsClassifier(n_neighbors=3)
modele.fit(X_train, y_train)
y_pred = modele.predict(X_test)

# ------------------------------------------------------------
# 2. Accuracy : le % global de bonnes réponses
# ------------------------------------------------------------
print(f"Accuracy globale : {accuracy_score(y_test, y_pred):.2%}")
print("=" * 55)

# ------------------------------------------------------------
# 3. Matrice de confusion : qui est confondu avec qui ?
# ------------------------------------------------------------
# Ligne = vraie espèce, Colonne = espèce prédite.
# La diagonale = les bonnes réponses. Hors diagonale = les erreurs.
print("Matrice de confusion (lignes = réel, colonnes = prédit) :")
print("Classes :", list(map(str, iris.target_names)))
print(confusion_matrix(y_test, y_pred))
print("=" * 55)

# ------------------------------------------------------------
# 4. Précision & rappel, classe par classe
# ------------------------------------------------------------
print("Rapport détaillé :")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

print("Rappel : précision = 'quand je dis X, ai-je raison ?'")
print("         rappel    = 'tous les vrais X, les ai-je retrouvés ?'")

# ------------------------------------------------------------
# 🔧 À TOI DE JOUER
# ------------------------------------------------------------
# 1. Mets n_neighbors=1 : la matrice de confusion change-t-elle ?
# 2. Repère dans la matrice quelle paire d'espèces est la plus confondue.
#    (Indice : versicolor et virginica se ressemblent.)
