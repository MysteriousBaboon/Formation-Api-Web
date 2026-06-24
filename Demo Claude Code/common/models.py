# ============================================================
# common/models.py — Modèles ML/DL entraînés à la demande (cache)
# ============================================================
# Les modèles s'entraînent au PREMIER appel puis restent en mémoire.
# Datasets fournis par scikit-learn (rien à télécharger).
#   - Iris  : k-NN (cours machine learning)
#   - Digits: MLP  (cours deep learning)
#   - Perceptron numpy : OR / AND / XOR (cours deep learning)
# ============================================================

import numpy as np
from sklearn.datasets import load_iris, load_digits
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Cache mémoire des objets entraînés.
_cache = {}


# ------------------------------------------------------------
# IRIS — k-NN
# ------------------------------------------------------------
def iris_knn():
    """k-NN entraîné sur tout le jeu Iris (+ métadonnées)."""
    if "iris_knn" not in _cache:
        iris = load_iris()
        modele = KNeighborsClassifier(n_neighbors=3)
        modele.fit(iris.data, iris.target)
        _cache["iris_knn"] = {
            "modele": modele,
            "target_names": list(iris.target_names),
            "feature_names": list(iris.feature_names),
        }
    return _cache["iris_knn"]


def iris_evaluate():
    """Entraîne sur 75 % / évalue sur 25 % : accuracy, confusion, rapport."""
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.25, random_state=42
    )
    modele = KNeighborsClassifier(n_neighbors=3)
    modele.fit(X_train, y_train)
    y_pred = modele.predict(X_test)
    return {
        "accuracy": round(float(accuracy_score(y_test, y_pred)), 4),
        "matrice_confusion": confusion_matrix(y_test, y_pred).tolist(),
        "classes": list(iris.target_names),
        "rapport": classification_report(
            y_test, y_pred, target_names=iris.target_names, output_dict=True
        ),
        "n_test": int(len(y_test)),
    }


def iris_boundary_figure():
    """Construit la figure de la frontière de décision (2 features pétale)."""
    import matplotlib.pyplot as plt  # backend Agg déjà fixé par common.charts

    iris = load_iris()
    X = iris.data[:, 2:4]
    y = iris.target
    modele = KNeighborsClassifier(n_neighbors=5)
    modele.fit(X, y)

    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                         np.arange(y_min, y_max, 0.02))
    Z = modele.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.contourf(xx, yy, Z, alpha=0.3, cmap="viridis")
    scatter = ax.scatter(X[:, 0], X[:, 1], c=y, edgecolor="k", cmap="viridis")
    ax.set_xlabel(iris.feature_names[2])
    ax.set_ylabel(iris.feature_names[3])
    ax.set_title("Frontière de décision d'un k-NN (k=5)")
    ax.legend(handles=scatter.legend_elements()[0], labels=list(iris.target_names))
    return fig


# ------------------------------------------------------------
# DIGITS — MLP
# ------------------------------------------------------------
def digits_mlp():
    """MLP entraîné sur les chiffres 8×8 (+ jeu de test conservé)."""
    if "digits_mlp" not in _cache:
        digits = load_digits()
        X_train, X_test, y_train, y_test = train_test_split(
            digits.data, digits.target, test_size=0.25, random_state=42
        )
        modele = MLPClassifier(hidden_layer_sizes=(64, 32),
                               max_iter=2000, random_state=42)
        modele.fit(X_train, y_train)
        _cache["digits_mlp"] = {
            "modele": modele,
            "X_test": X_test,
            "y_test": y_test,
            "accuracy": round(float(accuracy_score(y_test, modele.predict(X_test))), 4),
        }
    return _cache["digits_mlp"]


# ------------------------------------------------------------
# PERCEPTRON — codé à la main (numpy)
# ------------------------------------------------------------
class Perceptron:
    """Un seul neurone : sortie = step(poids · entrées + biais)."""

    def __init__(self, n_entrees, taux=0.1):
        self.poids = np.zeros(n_entrees)
        self.biais = 0.0
        self.taux = taux

    def predire(self, x):
        return 1 if np.dot(self.poids, x) + self.biais >= 0 else 0

    def entrainer(self, X, y, epochs=12):
        trace = []
        for epoch in range(1, epochs + 1):
            erreurs = 0
            for xi, cible in zip(X, y):
                erreur = cible - self.predire(xi)
                if erreur != 0:
                    self.poids += self.taux * erreur * xi
                    self.biais += self.taux * erreur
                    erreurs += 1
            trace.append({"epoch": epoch, "erreurs": int(erreurs),
                          "poids": [round(float(p), 2) for p in self.poids],
                          "biais": round(float(self.biais), 2)})
            if erreurs == 0:
                break
        return trace


_TABLES = {
    "OR": [0, 1, 1, 1],
    "AND": [0, 0, 0, 1],
    "XOR": [0, 1, 1, 0],
}


def perceptron_logique(fonction):
    """Entraîne un perceptron sur une table de vérité (OR/AND/XOR)."""
    fonction = fonction.upper()
    if fonction not in _TABLES:
        raise ValueError(f"fonction inconnue (choisir parmi {list(_TABLES)})")
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array(_TABLES[fonction])
    p = Perceptron(n_entrees=2, taux=0.1)
    trace = p.entrainer(X, y)
    predictions = [{"entree": xi.tolist(), "attendu": int(c), "predit": p.predire(xi)}
                   for xi, c in zip(X, y)]
    justes = sum(1 for pr in predictions if pr["attendu"] == pr["predit"])
    return {
        "fonction": fonction,
        "epochs_utilisees": len(trace),
        "trace": trace,
        "predictions": predictions,
        "bonnes_reponses": f"{justes}/{len(y)}",
        "appris": justes == len(y),
        "note": ("XOR n'est pas séparable par une droite : un seul neurone échoue. "
                 "C'est pourquoi le deep learning empile des couches."
                 if fonction == "XOR" else
                 "Fonction linéairement séparable : le neurone converge."),
    }
