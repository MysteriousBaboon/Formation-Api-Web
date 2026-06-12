# ✅ Corrigés — Machine Learning

> Les valeurs chiffrées exactes peuvent varier légèrement selon ta version de scikit-learn.
> Ce qui compte, c'est l'**interprétation**.

---

## Exercice 1 — Premier modèle

1. La fleur d'exemple `[5.1, 3.5, 1.4, 0.2]` est prédite **setosa** (petits pétales = signature de setosa).
2. Une fleur « extrême » (gros pétales) bascule vers **virginica** : logique, k-NN regarde les voisins.
3. `n_neighbors=1` : le modèle colle au voisin le plus proche (sensible au bruit).
   `n_neighbors=15` : il « moyenne » plus, plus prudent et lisse.
4. Oui, ça marche en changeant juste le modèle : c'est **l'API unifiée** de scikit-learn
   (`fit` / `predict` sont identiques pour tous les modèles).

---

## Exercice 2 — Sur-apprentissage

1. Le score *train* atteint **100 %** dès que la profondeur est suffisante (souvent ≥ 5, ou illimitée).
2. Le score *test* **ne suit pas** : c'est le **sur-apprentissage** (overfitting).
3. Avec `test_size=0.50`, on entraîne sur moins de données → le modèle apprend moins, le test
   devient un peu plus dur. Les scores baissent en général légèrement.
4. Évaluer sur les données d'entraînement, c'est tricher : le modèle les a **mémorisées**.
   La seule question honnête est : *« est-il bon sur des données jamais vues ? »*

---

## Exercice 3 — Matrice de confusion

1. Accuracy globale ≈ **100 %** (parfois une erreur, ~97-98 %), selon le split.
2. Quand il y a une erreur, c'est entre **versicolor** et **virginica** (espèces qui se ressemblent).
   *setosa* n'est jamais confondue (bien séparée).
3. *setosa* a un rappel parfait ; versicolor/virginica sont un cran en dessous selon le split.
4. `n_neighbors=1` : peut introduire 1-2 erreurs de plus (plus sensible au bruit).

---

## Exercice 4 — Frontière de décision

1. Les 3 zones colorées = les régions où le modèle prédit chaque espèce. La fleur tombe dans
   la zone de sa couleur → c'est sa prédiction.
2. `n_neighbors=1` → frontière **déchiquetée** : le modèle épouse chaque point, y compris le bruit.
   C'est le **sur-apprentissage**, vu à l'œil nu.
3. `n_neighbors=30` → frontière **très lisse** : modèle plus prudent, il généralise davantage.
4. Avec les sépales (`[:, 0:2]`), les espèces se **chevauchent** plus → plus difficile à séparer.
   Le choix des features compte autant que le choix du modèle !

---

## Exercice 5 — Comparer trois modèles

Voir `corriges/exo_5.py`. Sur Iris (jeu petit et « facile »), les trois modèles dépassent ~95 %.
Le point pédagogique : **le même code** (`fit` / `score`) entraîne trois modèles très différents.
Sur des données réelles plus complexes, la **forêt aléatoire** est souvent le meilleur premier choix.
