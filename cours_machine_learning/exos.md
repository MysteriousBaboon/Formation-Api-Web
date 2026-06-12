# 🧪 Exercices — Machine Learning (≈ 2h, en autonomie)

> 🦿 **Format adapté.** Les démos `1` à `4` sont déjà écrites : ici tu **les lis, les lances,
> et tu les modifies**. L'objectif est de comprendre, pas de tout coder de zéro.
> Corrigés dans `corriges/`.
>
> Avant de commencer : `pip install -r requirements.txt`.

---

## Exercice 1 — Explorer ton premier modèle (20 min)

À partir de `1_premier_modele.py` :

1. Lance-le tel quel. Quelle espèce est prédite pour la fleur d'exemple ?
2. Change les 4 mesures de `nouvelle_fleur` (essaie une fleur « moyenne », puis une « extrême »).
   La prédiction change-t-elle de façon logique ?
3. Mets `n_neighbors=1`, relance ; puis `n_neighbors=15`. Décris en une phrase l'effet attendu.
4. Remplace `KNeighborsClassifier` par `DecisionTreeClassifier`
   (`from sklearn.tree import DecisionTreeClassifier`) **sans rien changer d'autre**.
   Ça marche toujours ? Pourquoi ? (relie ça à « l'API unifiée » du cours)

---

## Exercice 2 — Diagnostiquer le sur-apprentissage (30 min)

À partir de `2_train_test.py` :

1. Lance-le et **lis le tableau**. À partir de quelle profondeur le score *train* atteint-il 100 % ?
2. À cette profondeur, le score *test* est-il aussi bon ? Comment s'appelle ce phénomène ?
3. Passe `test_size` de `0.30` à `0.50`. Les scores changent-ils ? Pourquoi le test devient-il
   « plus dur » ?
4. **Question de réflexion** : pourquoi est-ce malhonnête d'évaluer un modèle sur ses données
   d'entraînement ? Écris ta réponse en 2-3 phrases.

---

## Exercice 3 — Lire une matrice de confusion (25 min)

À partir de `3_evaluation.py` :

1. Lance-le. Quelle est l'accuracy globale ?
2. Dans la matrice de confusion, repère **les erreurs** (les cases hors diagonale). Quelles deux
   espèces sont confondues ?
3. Dans le rapport, trouve la classe avec le **meilleur rappel** et celle avec le **moins bon**.
4. Mets `n_neighbors=1`. L'accuracy et la matrice changent-elles ? Mieux ou moins bien ?

---

## Exercice 4 — Visualiser la frontière (25 min) 🖼️

À partir de `4_visualiser_frontiere.py` :

1. Lance-le, puis ouvre `frontiere.png`. Décris ce que représentent les **3 zones colorées**.
2. Mets `n_neighbors=1`, relance, regarde l'image : la frontière est-elle lisse ou « déchiquetée » ?
   Quel phénomène du cours ça illustre **visuellement** ?
3. Mets `n_neighbors=30` : la frontière devient comment ? Le modèle est-il plus « prudent » ?
4. **Bonus** : change les 2 features (`iris.data[:, 0:2]` pour les sépales). Les espèces sont-elles
   plus faciles ou plus difficiles à séparer avec ces features ?

---

## Exercice 5 — Mini-défi : un nouveau modèle (30 min) 🏗️

Crée `exo_5.py` (inspire-toi de `2_train_test.py`) :

1. Charge Iris, fais un `train_test_split` (test_size=0.30, random_state=42).
2. Entraîne une **forêt aléatoire** : `from sklearn.ensemble import RandomForestClassifier`.
3. Affiche le score sur le test.
4. Compare avec le k-NN et l'arbre de décision : lequel gagne sur ce jeu de données ?

> 💡 Tout le code que tu connais déjà fonctionne : c'est encore la même API `fit` / `score`.

---

## ✅ Checklist d'auto-évaluation

- [ ] Je sais nommer les étapes du workflow ML (§2 du cours)
- [ ] Je distingue classification et régression (§3)
- [ ] J'explique avec mes mots k-NN, arbre, régression linéaire (§4)
- [ ] J'ai vu le sur-apprentissage dans un tableau **et** sur une image (exos 2 & 4)
- [ ] Je sais lire une matrice de confusion (exo 3)
- [ ] J'ai entraîné un modèle que je n'avais pas vu en démo (exo 5)

> 🎯 Si tout est coché, direction le **Cours 10 — Deep Learning & Vision**.
