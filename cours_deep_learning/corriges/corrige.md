# ✅ Corrigés — Deep Learning & Computer Vision

> Les chiffres exacts peuvent varier un peu. C'est l'**intuition** qui compte.

---

## Exercice 1 — Le neurone à la main

1. **OU** et **ET** convergent vite (généralement en 2 à 6 epochs) : ils sont *linéairement
   séparables*, un seul neurone suffit.
2. **XOR** : le nombre d'erreurs **ne tombe jamais à 0**. Le neurone tourne en rond.
3. Même avec `epochs=100`, le XOR **échoue toujours**. Raison : un seul neurone ne peut tracer
   qu'**une droite**, or aucune droite ne sépare les points du XOR. Il faut **plusieurs couches**
   → c'est la raison d'être du deep learning.
4. `taux` plus grand (0.5) : pas plus gros, convergence parfois plus rapide mais plus instable.
   `taux` plus petit (0.01) : plus lent, plus de petits pas.

---

## Exercice 2 — Décrire un neurone

1. Les **poids** disent quelle entrée compte le plus ; le **biais** décale le seuil de
   déclenchement (il permet d'activer même quand les entrées sont faibles).
2. Sans activation, empiler des neurones reste équivalent à **une seule droite** : le réseau
   ne pourrait apprendre que des relations linéaires. L'activation apporte la **non-linéarité**.
3. Descente dans le brouillard : on ne voit pas la vallée, mais on sent la **pente** et on fait
   un **pas** vers le bas, encore et encore. Le « pas » = le **taux d'apprentissage**.
4. **Vrai.** Tout l'apprentissage consiste à ajuster poids et biais pour réduire l'erreur.

---

## Exercice 3 — Le réseau qui lit des chiffres

1. Précision sur le test ≈ **96-98 %** avec le réseau `(64, 32)`.
2. Les confusions classiques : **8↔3**, **9↔4**, **1↔7** — des chiffres visuellement proches.
3. `(4,)` : précision en **forte baisse** : trop peu de neurones pour capturer 10 formes de
   chiffres → sous-apprentissage.
4. `(128, 64, 32)` : gain **faible** (souvent < 1 point) pour beaucoup plus de calcul. Morale :
   « plus profond » n'est **pas automatiquement** meilleur — il y a un point de rendement décroissant.

---

## Exercice 4 — Ranger les architectures

1. Panneau sur une photo → **CNN** (image).
2. Mot suivant dans une phrase → **Transformer** (langage ; un RNN marcherait, en moins bien).
3. Clients dans un tableau → **MLP** (données tabulaires ; un modèle ML classique irait aussi).
4. Traduction → **Transformer** (c'est sa tâche d'origine).
5. Anomalie dans un signal audio au fil du temps → **RNN/LSTM** (séquence temporelle).

---

## Exercice 5 — TensorFlow Playground

1. Avec **0 couche cachée**, les spirales (non linéairement séparables) sont **impossibles** à
   séparer — même limite que le XOR.
2. Il faut **plusieurs couches** et assez de neurones (souvent 2 couches de 6-8 neurones, +
   des features adaptées). L'important : tu constates qu'**ajouter de la profondeur débloque**
   des problèmes qu'un modèle simple ne sait pas résoudre.
3. La zone colorée qui se déforme = la **frontière de décision** en train de s'apprendre.
