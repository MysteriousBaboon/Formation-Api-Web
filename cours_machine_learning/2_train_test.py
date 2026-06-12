# ============================================================
# 2_train_test.py — Séparer train/test & voir le sur-apprentissage
# ============================================================
# LE concept clé du ML : on n'évalue JAMAIS un modèle sur les données
# qu'il a apprises (ce serait tricher). On cache une partie des données
# pour le tester honnêtement.
#
# Pour bien VOIR le sur-apprentissage, on utilise ici un jeu de points
# 2D un peu BRUITÉ ("make_moons") : deux lunes qui s'entremêlent.
# Plus on laisse l'arbre devenir profond, plus il apprend le bruit
# "par cœur" → excellent sur le train, moins bon sur le test.
#
# Lancement :   python 2_train_test.py
# ============================================================

from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# ------------------------------------------------------------
# 1. Des données synthétiques, volontairement bruitées
# ------------------------------------------------------------
# noise=0.35 ajoute du "désordre" : c'est ce désordre qu'un modèle
# trop complexe va apprendre par cœur au lieu de l'ignorer.
X, y = make_moons(n_samples=300, noise=0.35, random_state=42)

# 2. Couper : 70 % pour apprendre, 30 % pour tester
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)
print(f"Entraînement : {len(X_train)} points   |   Test : {len(X_test)} points")
print("=" * 60)

# ------------------------------------------------------------
# 3. Comparer plusieurs profondeurs d'arbre
# ------------------------------------------------------------
# On regarde le score sur le TRAIN et sur le TEST.
# Symptôme du sur-apprentissage : train qui grimpe vers 100 %
# pendant que le test stagne, puis REDESCEND.
print(f"{'profondeur':>11} | {'score train':>11} | {'score test':>10}")
print("-" * 40)

for profondeur in [1, 2, 3, 5, 8, 15, None]:   # None = profondeur illimitée
    modele = DecisionTreeClassifier(max_depth=profondeur, random_state=42)
    modele.fit(X_train, y_train)

    score_train = modele.score(X_train, y_train)   # bon sur ce qu'il connaît
    score_test = modele.score(X_test, y_test)      # bon sur du nouveau ?

    etiquette = "illimitée" if profondeur is None else str(profondeur)
    print(f"{etiquette:>11} | {score_train:>11.2%} | {score_test:>10.2%}")

print("=" * 60)
print("Observe : le score TRAIN grimpe jusqu'à ~100 % (il apprend le bruit par cœur)")
print("alors que le score TEST plafonne puis REDESCEND. C'est le sur-apprentissage.")
print("Le 'bon' réglage est la profondeur qui maximise le score TEST (souvent 2 à 3 ici).")

# ------------------------------------------------------------
# 🔧 À TOI DE JOUER
# ------------------------------------------------------------
# 1. À quelle profondeur le score TEST est-il le meilleur ?
#    (c'est le bon compromis, ni trop simple ni trop complexe)
# 2. Baisse le bruit : noise=0.15. L'écart train/test se réduit-il ?
# 3. Augmente le bruit : noise=0.5. Le sur-apprentissage est-il plus marqué ?
