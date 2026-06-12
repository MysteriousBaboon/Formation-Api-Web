# 📚 Cours — Machine Learning (apprentissage supervisé)

> Le machine learning, c'est apprendre une règle **à partir d'exemples** au lieu de l'écrire à la main. Ce cours te montre comment, avec l'intuition d'abord et le code ensuite.

---

## 1. Le problème : et si on n'écrivait pas la règle ?

Imagine que tu veuilles détecter les e-mails de spam. En Python « classique », tu écrirais des règles :

```python
if "gagné" in mail or "viagra" in mail or mail.count("!") > 5:
    spam = True
```

Problème : les spams évoluent, tu n'en finis jamais d'ajouter des `if`. Le **machine learning**
renverse l'approche : tu **montres des milliers d'exemples** (spam / pas spam) à un algorithme,
et c'est **lui** qui trouve les règles tout seul.

> 💡 Règle simple pour savoir si c'est un cas de ML : *« Est-ce que je pourrais écrire toutes les
> règles à la main ? »* Si c'est trop complexe ou trop changeant → machine learning.

---

## 2. Le workflow du Machine Learning

Presque tous les projets ML suivent **le même pipeline** :

```
   ┌──────────┐   ┌──────────┐   ┌───────────┐   ┌──────────────┐   ┌────────────┐
   │ 1.Données│──▶│2.Features│──▶│3.Train/   │──▶│4.Entraînement│──▶│5.Évaluation│
   │  brutes  │   │ + labels │   │   Test    │   │   (fit)      │   │ (métriques)│
   └──────────┘   └──────────┘   └───────────┘   └──────────────┘   └────────────┘
                                                                          │
                                                                          ▼
                                                                  ┌──────────────┐
                                                                  │ 6.Prédiction │
                                                                  │  (predict)   │
                                                                  └──────────────┘
```

| Étape | En clair |
|---|---|
| **1. Données** | On rassemble des exemples (le dataset). |
| **2. Features / labels** | On choisit les **entrées** (features) et la **bonne réponse** (label). |
| **3. Train / Test** | On **cache** une partie des données pour tester honnêtement. |
| **4. Entraînement** | Le modèle apprend la correspondance features → label (`.fit()`). |
| **5. Évaluation** | On mesure s'il est bon sur les données **jamais vues** (`.score()`). |
| **6. Prédiction** | On l'utilise sur de **nouvelles** données (`.predict()`). |

> ✅ Tu retrouveras **exactement** ces étapes dans les démos `1` à `4`.

---

## 3. Supervisé : classification vs régression

Le ML supervisé répond à deux grandes questions :

| | **Classification** | **Régression** |
|---|---|---|
| On prédit… | une **catégorie** | un **nombre** |
| Exemple | spam / pas spam, chat / chien | prix d'une maison, température |
| Sortie | « classe B » | « 247 500 € » |

C'est le **même workflow** dans les deux cas. Seuls le type de label et les métriques changent.

---

## 4. Quelques modèles, expliqués sans maths

Un « modèle » = une **famille de méthodes** pour trouver la règle. En voici trois, par l'intuition :

### 4.1 k plus proches voisins (k-NN)
> « Dis-moi qui sont tes voisins, je te dirai qui tu es. »

Pour classer un nouveau point, on regarde les **k exemples les plus proches** et on prend la
classe **majoritaire**. Simple, intuitif, sans vrai « entraînement ».

### 4.2 Arbre de décision
> Une suite de questions oui/non, comme un « Akinator ».

```
La fleur a-t-elle un pétale > 2.5 cm ?
├── Oui → Largeur > 1.8 cm ?  ├── Oui → Virginica
│                              └── Non → Versicolor
└── Non → Setosa
```

Lisible, mais attention : un arbre trop profond apprend **par cœur** (voir §5).

### 4.3 Régression linéaire
> Tracer la **droite** (ou le plan) qui colle le mieux aux points.

Pour prédire un nombre : `prix ≈ a × surface + b`. Le modèle cherche les meilleurs `a` et `b`.

> 💡 Il en existe des dizaines (forêts aléatoires, SVM, boosting…). Pas besoin de les connaître
> tous : retiens **l'idée** et le fait qu'ils s'utilisent tous **de la même façon** dans scikit-learn.

---

## 5. Le piège n°1 : le sur-apprentissage

C'est **le** concept à comprendre aujourd'hui.

- **Sous-apprentissage (underfitting)** : le modèle est trop simple, il rate même les exemples
  d'entraînement. (L'élève qui n'a pas révisé.)
- **Sur-apprentissage (overfitting)** : le modèle apprend les exemples **par cœur**, y compris le
  bruit, et se plante sur les nouveaux cas. (L'élève qui récite le cours mais ne sait rien appliquer.)

```
Erreur
  │ \                                   ╱  ← sur-apprentissage (test)
  │  \                               ╱
  │   \___________________________╱
  │    ───────────────────────────  ← entraînement (toujours bon)
  │                  ▲
  │            le bon endroit
  └───────────────────────────────▶ complexité du modèle
```

**La parade : séparer train et test.** On entraîne sur une partie (souvent 70-80 %) et on évalue
sur l'autre, **jamais vue**. Si le modèle est bon sur le train mais nul sur le test → sur-apprentissage.

> ⚠️ Évaluer un modèle sur ses propres données d'entraînement, c'est **tricher** : bien sûr qu'il
> les connaît, il les a apprises ! La vraie question est : *« est-il bon sur du nouveau ? »*

---

## 6. Évaluer : les métriques qui comptent

« Bon » ou « mauvais », ça se **mesure**. Selon le type de problème :

### Classification
| Métrique | Question | Piège |
|---|---|---|
| **Accuracy** | % de bonnes réponses | Trompeuse si les classes sont déséquilibrées |
| **Précision** | Parmi les « positifs » prédits, combien sont justes ? | — |
| **Rappel** | Parmi les vrais positifs, combien ai-je retrouvés ? | — |
| **Matrice de confusion** | Qui est confondu avec qui ? | La vue la plus utile |

> 💡 Exemple du déséquilibre : un test qui dit toujours « pas de maladie » a 99 % d'accuracy si
> 99 % des gens sont sains… mais rate **tous** les malades. D'où précision/rappel.

### Régression
| Métrique | En clair |
|---|---|
| **MAE** | Erreur moyenne en valeur absolue (€, °C…) |
| **RMSE** | Pareil, mais pénalise plus les grosses erreurs |

---

## 7. scikit-learn : tout ça en 4 lignes

La magie de scikit-learn : **tous** les modèles s'utilisent pareil.

```python
from sklearn.neighbors import KNeighborsClassifier

modele = KNeighborsClassifier()      # 1. choisir un modèle
modele.fit(X_train, y_train)         # 2. entraîner (apprendre)
predictions = modele.predict(X_test) # 3. prédire
score = modele.score(X_test, y_test) # 4. évaluer
```

Change `KNeighborsClassifier` en `DecisionTreeClassifier` ou `LogisticRegression` :
**le reste du code ne bouge pas.** C'est ça, la force de l'API unifiée.

- `X` = les **features** (un tableau : une ligne par exemple, une colonne par caractéristique)
- `y` = les **labels** (la bonne réponse de chaque exemple)

> 👉 Les démos `1_premier_modele.py` à `4_visualiser_frontiere.py` déroulent exactement ça.
> Lis-les dans l'ordre, lance-les, **modifie une valeur**, relance, observe.

---

## 8. Aller plus loin (en autonomie)

- **Normalisation** : certains modèles (k-NN) marchent mieux si les features sont à la même échelle
  (`StandardScaler`).
- **Validation croisée** (`cross_val_score`) : évaluer plus robustement qu'avec un seul split.
- **Forêts aléatoires** (`RandomForestClassifier`) : souvent un excellent premier choix.
- **Le vrai métier** n'est pas le modèle, mais les **données** : les nettoyer, choisir les bonnes
  features. C'est 80 % du travail (et ça réutilise ton cours pandas !).

Le **Cours 10** garde ce workflow mais remplace ces modèles par des **réseaux de neurones**.
