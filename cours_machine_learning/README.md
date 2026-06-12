# 🤖 Cours 9 — Machine Learning (apprentissage supervisé)

Deuxième journée du parcours IA. On passe de la théorie à la **première vraie machine qui apprend**.
L'objectif : comprendre, par l'intuition et quelques démos, **comment un modèle apprend à partir
de données** — sans maths lourdes.

## 🎯 Objectifs

À la fin de cette journée, tu seras capable de :

- Décrire le **workflow ML** : données → features → train/test → entraînement → évaluation → prédiction
- Distinguer **classification** (catégorie) et **régression** (nombre)
- Expliquer avec tes mots **k-NN**, **arbre de décision**, **régression linéaire**
- Comprendre le **sur-apprentissage** et pourquoi on sépare *train* et *test*
- Lire les **métriques** clés (accuracy, précision/rappel, matrice de confusion)
- Entraîner un modèle en **4 lignes** avec scikit-learn

## 📁 Structure

```
cours_machine_learning/
├── README.md
├── cours.md                  ← le cours complet (à lire en premier)
├── slides/
│   ├── contenu.py            ← contenu des slides (modifiable)
│   └── machine_learning.pptx ← diaporama prêt à projeter
├── requirements.txt
├── 1_premier_modele.py       ← entraîner un classifieur en 4 lignes (Iris)
├── 2_train_test.py           ← séparer train/test + voir le sur-apprentissage
├── 3_evaluation.py           ← métriques : accuracy, matrice de confusion
├── 4_visualiser_frontiere.py ← voir la "frontière de décision" (génère une image)
├── exos.md                   ← exercices (surtout interprétation + ajustements)
└── corriges/                 ← corrigés
```



## 🚀 Pour démarrer

```bash
cd cours_machine_learning
source ../.venv/bin/activate
pip install -r requirements.txt

python 1_premier_modele.py     # ton premier modèle, en 4 lignes
```

> 💡 Les jeux de données (Iris, digits) sont **fournis avec scikit-learn** : rien à télécharger.

## 🔗 Le lien avec le reste

C'est la **suite directe du Cours 8** : ici on entre dans le « Machine Learning » des poupées russes.
On réutilise **pandas** (cours_data) pour manipuler les données et **matplotlib** (cours_dataviz)
pour visualiser. Le **Cours 10** poussera l'idée plus loin avec les réseaux de neurones.

```
[Cours 8: panorama]  →  [Cours 9: ML classique]  →  [Cours 10: deep learning]
```
