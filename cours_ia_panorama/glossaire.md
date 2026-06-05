# 📖 Glossaire — le lexique de survie de l'IA

> Garde ce fichier ouvert pendant tout le parcours. Quand un mot te bloque, il est sûrement ici.
> Les termes marqués 🔜 seront approfondis dans un cours suivant.

---

## Les concepts de base

| Terme | Définition simple |
|---|---|
| **IA (Intelligence Artificielle)** | Programme qui réalise des tâches « intelligentes ». Le grand ensemble. |
| **Machine Learning (ML)** | Sous-ensemble de l'IA où la machine **apprend depuis des données** au lieu d'être codée règle par règle. |
| **Deep Learning** | Du ML utilisant des **réseaux de neurones** à plusieurs couches. 🔜 Cours 10 |
| **IA générative** | IA qui **crée** du contenu (texte, image, son). 🔜 Cours 11-12 |
| **Modèle** | Le résultat de l'entraînement : le « cerveau » qui fait des prédictions. |
| **Algorithme** | La recette/méthode d'apprentissage (ex. : arbre de décision, k-NN). |

## Les données

| Terme | Définition simple |
|---|---|
| **Dataset** | L'ensemble des données d'exemple utilisées pour entraîner/tester. |
| **Feature** (caractéristique) | Une variable d'entrée (surface, âge, couleur de pixel…). |
| **Label** (étiquette) | La bonne réponse à prédire (le prix réel, la classe « chat »). |
| **Échantillon / instance** | Une ligne du dataset (un exemple). |
| **Train / Test** | On entraîne sur une partie des données, on **teste** sur une autre jamais vue. 🔜 Cours 9 |

## L'apprentissage

| Terme | Définition simple |
|---|---|
| **Supervisé** | Apprendre depuis des exemples **étiquetés** (entrée + bonne réponse). |
| **Non-supervisé** | Trouver des structures **sans étiquettes** (groupes, anomalies). |
| **Renforcement** | Apprendre par **essai/erreur** guidé par une récompense. |
| **Classification** | Prédire une **catégorie** (spam / pas spam). 🔜 Cours 9 |
| **Régression** | Prédire un **nombre** (un prix, une température). 🔜 Cours 9 |
| **Entraînement** | La phase où le modèle apprend (lente). |
| **Inférence** | La phase où on utilise le modèle pour prédire (rapide). |
| **Sur-apprentissage (overfitting)** | Le modèle apprend « par cœur » et rate les nouveaux cas. 🔜 Cours 9 |

## Les réseaux de neurones

| Terme | Définition simple |
|---|---|
| **Neurone / perceptron** | L'unité de base : combine des entrées et produit une sortie. 🔜 Cours 10 |
| **Couche (layer)** | Un étage de neurones. « Profond » = beaucoup de couches. |
| **Poids / paramètres** | Les réglages internes ajustés pendant l'entraînement. |
| **Fonction d'activation** | La « décision » non-linéaire d'un neurone (ReLU, sigmoïde…). 🔜 Cours 10 |
| **Rétropropagation** | La méthode pour corriger les poids selon l'erreur. 🔜 Cours 10 |
| **CNN** | Réseau spécialisé pour les **images**. 🔜 Cours 10 |
| **GPU** | La puce qui accélère massivement l'entraînement. |

## Le monde des LLM

| Terme | Définition simple |
|---|---|
| **LLM (Large Language Model)** | Grand modèle de langage entraîné sur énormément de texte. 🔜 Cours 11 |
| **Transformer** | L'architecture (2017) derrière tous les LLM modernes. 🔜 Cours 11 |
| **Token** | Un morceau de mot ; l'unité que lit/écrit un LLM. 🔜 Cours 11 |
| **Prompt** | L'instruction/question qu'on donne au modèle. 🔜 Cours 11 |
| **Fenêtre de contexte** | La quantité de texte que le modèle peut « voir » d'un coup. 🔜 Cours 11 |
| **Hallucination** | Quand un LLM invente une réponse fausse avec aplomb. |
| **Fine-tuning** | Ré-entraîner un modèle existant sur des données spécifiques. 🔜 Cours 11 |
| **RAG** | Donner au LLM des documents à consulter pour répondre. 🔜 Cours 11 |
| **Agent** | Un LLM qui **agit** : utilise des outils, enchaîne des étapes. 🔜 Cours 12 |
| **Tool / function calling** | Donner au LLM la capacité d'appeler des fonctions/API. 🔜 Cours 12 |

---

> 💡 Tu n'as pas besoin de tout retenir aujourd'hui. Ce glossaire est une **référence** :
> reviens-y à chaque cours, et les 🔜 se rempliront tout seuls au fil du parcours.
