# 🧠 Cours 10 — Deep Learning & Computer Vision

Troisième journée du parcours IA. On ouvre la boîte noire des **réseaux de neurones** :
d'où vient la « magie » du deep learning, et comment une machine en arrive à *voir*.
Cours **surtout conceptuel** : l'intuition d'abord, deux petites démos ensuite.

## 🎯 Objectifs

À la fin de cette journée, tu seras capable de :

- Expliquer ce qu'est un **neurone artificiel** (poids, biais, activation)
- Décrire l'idée de la **propagation avant** et de la **rétropropagation** (sans les maths)
- Comprendre pourquoi on parle de **« profond »** et ce que ça apporte
- Citer les grandes architectures : **CNN** (vision), RNN, **Transformers** (→ cours 11)
- Situer les tâches de **computer vision** : classification, détection, segmentation

## 📁 Structure

```
cours_deep_learning/
├── README.md
├── cours.md                  ← le cours complet (à lire en premier)
├── slides/
│   ├── contenu.py
│   └── deep_learning.pptx    ← diaporama prêt à projeter
├── requirements.txt
├── 1_perceptron_numpy.py     ← un neurone CODÉ À LA MAIN (numpy), qui apprend
├── 2_mlp_sklearn_digits.py   ← un petit réseau qui reconnaît des chiffres (vision)
├── exos.md                   ← exercices (intuition + manipulation légère)
└── corriges/
```

## 🗓️ Déroulé de journée conseillé

> 🦿 **Format adapté.** Beaucoup de schémas et d'intuition le matin. L'après-midi, deux
> démos **légères** (pas de PyTorch, pas de GPU) : un neurone à la main, puis un mini-réseau.

| Moment | Quoi | Support |
|---|---|---|
| Matin (~1h15) | Mini-cours (le neurone, l'apprentissage, la vision) | `slides/deep_learning.pptx` + `cours.md` |
| Après-midi | Démos `1` (perceptron) puis `2` (chiffres) | les `.py` |
| Après-midi | Exercices + démos en ligne | `exos.md` |

## 🚀 Pour démarrer

```bash
cd cours_deep_learning
source ../.venv/bin/activate
pip install -r requirements.txt

python 1_perceptron_numpy.py    # un neurone qui apprend, codé à la main
```

> ⚠️ **Pas de PyTorch / TensorFlow ici.** Ils sont lourds et pas encore compatibles avec
> Python 3.14. L'objectif est l'**intuition** : on code un neurone avec `numpy`, et on
> utilise le mini-réseau de scikit-learn. Largement suffisant pour comprendre.

## 🔗 Le lien avec le reste

Le **Cours 9** t'a montré le *workflow* ML avec des modèles « classiques ». Ici, on remplace
ces modèles par des **réseaux de neurones** — même logique `fit` / `predict`, mais une mécanique
interne très différente. Et surtout, ce cours prépare le **Cours 11** : les LLM sont eux-mêmes
de **gros réseaux de neurones** (des Transformers).

```
[Cours 9: ML classique]  →  [Cours 10: réseaux de neurones]  →  [Cours 11: LLM]
```
