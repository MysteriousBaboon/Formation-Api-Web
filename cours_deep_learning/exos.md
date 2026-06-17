# 🧪 Exercices — Deep Learning & Computer Vision (≈ 2h, en autonomie)

> 🦿 **Format adapté.** Cours surtout conceptuel : ici on mélange **réflexion** et
> **manipulation légère** de deux démos déjà écrites. Pas de GPU, pas d'attente.
> Corrigés dans `corriges/`.
>
> Avant de commencer : `pip install -r requirements.txt`.

---

## Exercice 1 — Le neurone à la main (30 min)

À partir de `1_perceptron_numpy.py` :

1. Lance-le. Pour le **OU** et le **ET**, en combien d'epochs le neurone converge-t-il (0 erreur) ?
2. Pour le **XOR**, que se passe-t-il ? Le nombre d'erreurs tombe-t-il à 0 ?
3. Augmente `epochs=100` pour le XOR (modifie l'appel `evaluer(...)`). Finit-il par y arriver ?
   **Pourquoi** ? (relie ça au §3 du cours : un seul neurone = une seule droite)
4. Change `taux=0.1` en `0.5` puis `0.01`. L'effet sur la vitesse de convergence ?

---

## Exercice 2 — Décrire un neurone (15 min, sans code)

Réponds avec tes mots :

1. À quoi servent les **poids** ? Et le **biais** ?
2. Pourquoi la **fonction d'activation** est-elle indispensable (que se passe-t-il sans elle) ?
3. Reformule l'analogie de la **descente dans le brouillard**. Qu'est-ce que le « pas » ?
4. Vrai ou faux : « Apprendre, pour un réseau, c'est trouver les bons poids. » Justifie.

---

## Exercice 3 — Le réseau qui lit des chiffres (30 min) 🖼️

À partir de `2_mlp_sklearn_digits.py` :

1. Lance-le, ouvre `predictions.png`. Quelle est la précision sur le test ?
2. Repère un chiffre **mal prédit** (titre rouge). Avec quel autre chiffre est-il confondu ?
   Est-ce compréhensible visuellement (8 vs 3, 9 vs 4…) ?
3. Mets `hidden_layer_sizes=(4,)` (un réseau minuscule). La précision chute-t-elle ? Pourquoi ?
4. Mets `hidden_layer_sizes=(128, 64, 32)` (plus profond). Gagne-t-on **beaucoup** par rapport
   au réseau de base ? Qu'est-ce que ça t'apprend sur « plus profond = forcément mieux » ?

---

## Exercice 4 — Ranger les architectures (20 min, sans code)

Pour chaque cas, indique l'architecture la plus adaptée (**MLP**, **CNN**, **RNN/LSTM**,
**Transformer**) et justifie en une phrase :

1. Reconnaître un panneau de signalisation sur une photo
2. Prédire le mot suivant dans une phrase
3. Classer des clients à partir d'un tableau (âge, revenu, ancienneté)
4. Traduire un texte de l'anglais vers le français
5. Détecter une anomalie dans un signal audio au fil du temps

---

## Exercice 5 — Manipulation en ligne (25 min) 🌐

Va sur **TensorFlow Playground** : https://playground.tensorflow.org

1. Choisis le dataset « deux spirales » (en bas à gauche). Avec **0 couche cachée**, le réseau
   y arrive-t-il ? Pourquoi (pense au XOR de la démo 1) ?
2. Ajoute des couches/neurones jusqu'à séparer les spirales. Combien t'a-t-il fallu ?
3. Observe la zone de couleur évoluer pendant l'entraînement : tu **vois** la frontière de
   décision se former, exactement comme au cours 9.

> **Bonus** : sur https://poloclub.github.io/cnn-explainer/, suis une image qui traverse un CNN,
> couche par couche. Repère où les **bords** sont détectés.

---

## ✅ Checklist d'auto-évaluation

- [ ] Je sais expliquer un neurone (poids, biais, activation) (§1-2)
- [ ] Je comprends pourquoi il faut **plusieurs couches** (le XOR de la démo 1) (§3)
- [ ] Je peux raconter l'aller-retour avant/arrière (forward/backprop) (§4)
- [ ] J'associe CNN→images, Transformer→texte (§5)
- [ ] Je connais les 3 tâches de computer vision (§6)
- [ ] J'ai fait tourner un vrai réseau qui lit des chiffres (exo 3)
- [ ] J'ai joué avec TensorFlow Playground (exo 5)

> 🎯 Si tout est coché, place au **gros morceau** : **Cours 11 — Les LLM**.
