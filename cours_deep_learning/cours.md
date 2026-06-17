# 📚 Cours — Deep Learning & Computer Vision

> Le deep learning, c'est du machine learning avec des **réseaux de neurones**. Ce cours ouvre la boîte noire : un neurone, des couches, et comment tout ça « apprend ». On garde l'intuition, on laisse les maths lourdes de côté.

---

## 1. Le neurone artificiel : l'unité de base

Tout part d'une idée minuscule inspirée du cerveau. Un **neurone artificiel** :

1. reçoit des **entrées** (des nombres : `x1, x2, x3…`)
2. les multiplie par des **poids** (`w1, w2, w3…`) et ajoute un **biais** (`b`)
3. fait la somme, puis passe le résultat dans une **fonction d'activation**

```
   x1 ──(w1)──┐
   x2 ──(w2)──┼──▶ somme = w1·x1 + w2·x2 + w3·x3 + b ──▶ [activation] ──▶ sortie
   x3 ──(w3)──┘
```

- Les **poids** disent « quelle entrée compte le plus ».
- Le **biais** décale le seuil de déclenchement.
- L'**activation** introduit de la **non-linéarité** (sinon le réseau ne saurait tracer que des droites).

> 💡 Apprendre, pour un réseau, c'est **trouver les bons poids et biais**. Rien d'autre.
> Un LLM comme GPT, c'est *des milliards* de ces poids.

---

## 2. La fonction d'activation

Sans elle, empiler des neurones ne servirait à rien (la somme de droites reste une droite).
Les plus courantes :

| Activation | Allure | Usage |
|---|---|---|
| **Marche (step)** | 0 ou 1 | Le perceptron historique |
| **Sigmoïde** | S entre 0 et 1 | Probabilités |
| **ReLU** | `max(0, x)` | Le standard du deep learning moderne |

> 💡 ReLU est imbattable par sa simplicité : « si négatif → 0, sinon garde la valeur ». C'est
> elle qui équipe la majorité des réseaux profonds aujourd'hui.

---

## 3. Des neurones aux couches : pourquoi « profond »

Un seul neurone est limité. On les organise en **couches** :

```
 entrées        couche cachée 1     couche cachée 2     sortie
  (x1) ──┐      ┌─(o)─┐             ┌─(o)─┐
  (x2) ──┼──────┼─(o)─┼─────────────┼─(o)─┼──────────▶  (chat / chien)
  (x3) ──┘      └─(o)─┘             └─(o)─┘
              \_______________ profond = plusieurs couches ______________/
```

- **Chaque couche** apprend des motifs de plus en plus abstraits.
- En vision : la 1re couche détecte des **bords**, la suivante des **formes**, puis des **objets**.
- **« Deep »** = beaucoup de couches. Plus de couches = capacité d'abstraction plus grande
  (mais plus de données et de calcul nécessaires).

> 👉 La démo `1_perceptron_numpy.py` montre qu'**un seul neurone** ne peut pas apprendre le
> problème « XOR ». Il faut **plusieurs couches** : c'est *littéralement* la raison d'être du deep learning.

---

## 4. Comment un réseau apprend : l'aller-retour

L'apprentissage est une boucle répétée des milliers de fois :

```
        ┌──────────────── PROPAGATION AVANT ───────────────┐
        │  les entrées traversent le réseau → une prédiction │
        ▼                                                    │
   [On compare la prédiction à la bonne réponse → ERREUR]    │
        │                                                    │
        └──────────── RÉTROPROPAGATION ──────────────────────┘
           on remonte l'erreur et on ajuste chaque poids
```

1. **Propagation avant (forward)** : les données traversent le réseau, on obtient une prédiction.
2. **Erreur** : on mesure l'écart avec la vraie réponse (la « fonction de perte »).
3. **Rétropropagation (backprop)** : on calcule *qui* est responsable de l'erreur et on **ajuste
   chaque poids** dans le bon sens.
4. On recommence. À force, l'erreur diminue.

### L'analogie de la descente dans le brouillard 🌫️
Tu es sur une montagne dans le brouillard, tu veux descendre. Tu ne vois pas la vallée, mais tu
sens la **pente sous tes pieds** et tu fais un pas vers le bas. Tu répètes. C'est la **descente de
gradient** : à chaque étape, on bouge les poids dans la direction qui **réduit l'erreur**.

> 💡 La taille du pas s'appelle le **taux d'apprentissage** (learning rate). Trop grand : on
> saute par-dessus la vallée. Trop petit : on met une éternité.

---

## 5. Les grandes familles d'architectures

Selon la forme des données, on utilise des réseaux spécialisés :

| Architecture | Spécialité | Idée clé |
|---|---|---|
| **MLP** (dense) | Données tabulaires | Neurones tous connectés (la démo 2) |
| **CNN** (convolutif) | **Images** | Détecte des motifs locaux (bords, textures) |
| **RNN / LSTM** | Séquences (texte, audio) | Garde une « mémoire » du passé |
| **Transformer** | Texte (et +) | **L'attention** : relie chaque mot à tous les autres |

> 🔜 Le **Transformer** (2017) est l'architecture des LLM. On y arrive au **cours 11**.
> Les RNN ont été largement remplacés par les Transformers pour le langage.

---

## 6. Computer Vision : apprendre à voir

La vision par ordinateur, c'est faire comprendre des **images** à une machine. Une image, pour un
ordinateur, c'est juste un **tableau de nombres** (l'intensité de chaque pixel).

Les trois grandes tâches :

| Tâche | Question | Exemple |
|---|---|---|
| **Classification** | « C'est quoi ? » | Cette photo = un chat |
| **Détection d'objets** | « C'est quoi **et où** ? » | Une boîte autour de chaque voiture |
| **Segmentation** | « Quel pixel appartient à quoi ? » | Découper précisément la route, le ciel… |

C'est le **CNN** qui a fait décoller la vision en 2012 (AlexNet). Le principe : au lieu de tout
connecter, on fait **glisser de petits filtres** sur l'image pour repérer des motifs locaux,
couche après couche.

> 👉 La démo `2_mlp_sklearn_digits.py` fait de la **classification d'images** : reconnaître des
> chiffres manuscrits (8×8 pixels). Petit, mais c'est de la vraie vision par réseau de neurones.

---

## 7. Deep learning vs ML classique : quand l'un, quand l'autre ?

| | ML classique (cours 9) | Deep Learning |
|---|---|---|
| Données | Tabulaires, modérées | Images, son, texte, **beaucoup** de données |
| Features | Choisies à la main | **Apprises** par le réseau |
| Besoin de calcul | Faible | Élevé (souvent GPU) |
| Interprétabilité | Bonne (arbre lisible) | Faible (boîte noire) |

> ✅ Règle pratique : **peu de données tabulaires → ML classique** (souvent une forêt aléatoire
> suffit). **Images / texte / son en grande quantité → deep learning.**

---

## 8. Aller plus loin (en autonomie)

- **Transfer learning** : réutiliser un gros réseau déjà entraîné et l'adapter à ton problème
  avec peu de données. C'est ainsi qu'on fait de la vision « sérieuse » sans tout réentraîner.
- **Pré-entraîné = la norme** : on part presque toujours d'un modèle existant (ImageNet, etc.).
- **Démos en ligne** (rien à installer) :
  - *TensorFlow Playground* — entraîner un réseau à la souris : https://playground.tensorflow.org
  - *Teachable Machine* — un CNN en 3 minutes : https://teachablemachine.withgoogle.com
  - *CNN Explainer* — visualiser un CNN couche par couche : https://poloclub.github.io/cnn-explainer/

Le **Cours 11** prend ces réseaux et les pousse à l'extrême : les **LLM**.
