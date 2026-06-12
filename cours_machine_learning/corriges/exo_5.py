# ============================================================
# corriges/exo_5.py — Comparer trois modèles sur Iris
# ============================================================
# Montre la force de l'API unifiée : on entraîne 3 modèles très
# différents avec EXACTEMENT le même code.
# ============================================================

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)

# Un dictionnaire {nom: modèle} — on boucle dessus avec le même code
modeles = {
    "k-NN (k=3)": KNeighborsClassifier(n_neighbors=3),
    "Arbre de décision": DecisionTreeClassifier(random_state=42),
    "Forêt aléatoire": RandomForestClassifier(random_state=42),
}

print(f"{'Modèle':>20} | score test")
print("-" * 35)
for nom, modele in modeles.items():
    modele.fit(X_train, y_train)             # même code pour tous
    score = modele.score(X_test, y_test)     # même code pour tous
    print(f"{nom:>20} | {score:.2%}")

print("-" * 35)
print("Sur Iris (petit et simple), les trois sont excellents.")
print("Sur des données réelles, la forêt aléatoire est souvent la plus robuste.")
