# ============================================================
# cours_machine_learning/slides/contenu.py
# Contenu des slides du Cours 9 — Machine Learning
# ============================================================
# Modifier les slides : édite les listes ci-dessous, puis relance :
#     python slides/contenu.py
# ============================================================

import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RACINE))

from _slides.theme import (
    nouveau_deck, slide_titre, slide_section, slide_puces, sauver,
)


def construire():
    prs = nouveau_deck()

    slide_titre(
        prs,
        "Machine Learning",
        "Cours 9 — Quand la machine apprend à partir de données",
    )

    # 1
    slide_section(prs, "1. L'idée : ne plus écrire la règle")
    slide_puces(prs, "Le renversement", [
        "Avant : on écrit les règles à la main (des if/else sans fin)",
        "ML : on montre des EXEMPLES, la machine trouve la règle",
        "Bon réflexe : « pourrais-je écrire toutes les règles à la main ? »",
        ("Si non (trop complexe, trop changeant) → machine learning", 1),
    ])

    # 2
    slide_section(prs, "2. Le workflow ML")
    slide_puces(prs, "Toujours les mêmes étapes", [
        "Données brutes : rassembler des exemples",
        "Features & labels : les entrées et la bonne réponse",
        "Train / Test : cacher une partie pour évaluer honnêtement",
        "Entraînement (.fit) : le modèle apprend",
        "Évaluation : est-il bon sur du JAMAIS VU ?",
        "Prédiction (.predict) : l'utiliser sur du nouveau",
    ])

    # 3
    slide_section(prs, "3. Deux grandes questions")
    slide_puces(prs, "Classification vs Régression", [
        "Classification : prédire une CATÉGORIE",
        ("spam / pas spam, chat / chien", 1),
        "Régression : prédire un NOMBRE",
        ("prix d'une maison, température de demain", 1),
        "Même workflow ; seuls le label et les métriques changent",
    ])

    # 4
    slide_section(prs, "4. Quelques modèles, par l'intuition")
    slide_puces(prs, "Trois façons d'apprendre", [
        "k-NN : « dis-moi qui sont tes voisins… » (classe majoritaire)",
        "Arbre de décision : une suite de questions oui/non (Akinator)",
        "Régression linéaire : la droite qui colle le mieux aux points",
        "Dans scikit-learn, ils s'utilisent TOUS de la même façon",
    ])

    # 5
    slide_section(prs, "5. Le piège n°1 : le sur-apprentissage")
    slide_puces(prs, "Apprendre vs apprendre par cœur", [
        "Sous-apprentissage : modèle trop simple, rate même le train",
        "Sur-apprentissage : apprend par cœur, se plante sur le nouveau",
        ("= l'élève qui récite mais ne sait rien appliquer", 1),
        "La parade : séparer TRAIN et TEST",
        "Bon sur train + nul sur test = sur-apprentissage",
    ])

    # 6
    slide_section(prs, "6. Mesurer la qualité")
    slide_puces(prs, "Les métriques clés", [
        "Accuracy : % de bonnes réponses (trompeur si classes déséquilibrées)",
        "Précision : quand je dis X, ai-je raison ?",
        "Rappel : tous les vrais X, les ai-je retrouvés ?",
        "Matrice de confusion : qui est confondu avec qui (la + utile)",
        "Régression : MAE / RMSE (erreur moyenne)",
    ])

    # 7
    slide_section(prs, "7. scikit-learn en 4 lignes")
    slide_puces(prs, "L'API unifiée", [
        "modele = KNeighborsClassifier()   → choisir",
        "modele.fit(X_train, y_train)      → entraîner",
        "modele.predict(X_test)            → prédire",
        "modele.score(X_test, y_test)      → évaluer",
        "Changer de modèle = changer 1 ligne, le reste ne bouge pas",
    ])

    slide_titre(prs, "À toi de jouer 🚀", "Lance les démos 1 → 4, puis exos.md")

    chemin = Path(__file__).resolve().parent / "machine_learning.pptx"
    sauver(prs, str(chemin))


if __name__ == "__main__":
    construire()
