# 📚 Cours — Panorama de l'IA

> Avant d'apprendre à *faire* de l'IA, il faut une carte du territoire. Ce cours te donne le vocabulaire et les repères pour que tout le reste du parcours ait du sens.

---

## 1. C'est quoi « l'IA », vraiment ?

L'**intelligence artificielle**, c'est faire réaliser à une machine des tâches qui demandent
normalement de *l'intelligence humaine* : reconnaître un visage, comprendre une phrase,
traduire, recommander un film, conduire une voiture.

Trois choses à retenir tout de suite :

1. **Ce n'est pas magique.** Une IA = des **maths** + des **données** + de la **puissance de calcul**. Rien de plus.
2. **Ce n'est pas conscient.** Un modèle ne « comprend » pas comme toi. Il calcule des probabilités.
3. **Ce n'est pas nouveau.** Le domaine a plus de 60 ans. Ce qui est nouveau, c'est l'échelle (données + GPU).

> 💡 La meilleure définition opérationnelle : *une IA, c'est un programme qui s'améliore à partir d'exemples au lieu d'être codé règle par règle.*

---

## 2. Les poupées russes : IA ⊃ ML ⊃ Deep Learning ⊃ Génératif

Le piège n°1 du débutant, c'est de mélanger ces mots. Ils s'**emboîtent** :

```
┌─────────────────────────────────────────────┐
│  INTELLIGENCE ARTIFICIELLE                    │  ← le grand ensemble
│  ┌─────────────────────────────────────────┐ │
│  │  MACHINE LEARNING                         │ │  ← apprend depuis des données
│  │  ┌─────────────────────────────────────┐ │ │
│  │  │  DEEP LEARNING                        │ │ │  ← réseaux de neurones profonds
│  │  │  ┌─────────────────────────────────┐ │ │ │
│  │  │  │  IA GÉNÉRATIVE (ChatGPT, etc.)  │ │ │ │  ← crée du contenu
│  │  │  └─────────────────────────────────┘ │ │ │
│  │  └─────────────────────────────────────┘ │ │
│  └─────────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
```

| Terme | Définition simple | Exemple |
|---|---|---|
| **IA** | Toute machine qui « fait intelligent » | Un thermostat malin, un filtre anti-spam |
| **Machine Learning** | La machine **apprend** depuis des exemples | Prédire un prix immobilier |
| **Deep Learning** | Du ML avec des **réseaux de neurones** profonds | Reconnaître un chat sur une photo |
| **IA générative** | Du deep learning qui **crée** du contenu | ChatGPT, Midjourney |

> ✅ Phrase à retenir : **« Tout le deep learning est du machine learning, mais tout le machine learning n'est pas du deep learning. »**

---

## 3. Les grandes familles de l'IA

L'IA n'est pas un bloc unique. Selon **ce qu'on lui donne à manger**, on parle de familles
différentes. C'est ta « vue 360° » :

| Famille | Ce qu'elle traite | Exemples concrets |
|---|---|---|
| 👁️ **Vision** (computer vision) | Images, vidéos | Reconnaissance faciale, voitures autonomes, contrôle qualité |
| 💬 **Langage** (NLP) | Texte | Traduction, résumé, analyse de sentiment, chatbots |
| 🔊 **Audio / voix** | Sons, parole | Siri, sous-titres automatiques, synthèse vocale |
| 🎨 **Génératif** | Crée du nouveau contenu | ChatGPT (texte), Midjourney (images), Suno (musique) |
| 🛒 **Recommandation** | Comportements, préférences | Netflix, Spotify, fil Instagram, Amazon |
| 🎮 **Décision / robotique** | Actions dans un environnement | AlphaGo, robots d'usine, trading |

> 💡 Beaucoup de produits **mélangent** plusieurs familles. Une voiture autonome = vision
> + décision. Un assistant vocal = audio + langage + génératif.

**Notre parcours se concentre sur le langage et le génératif** (cours 11-12, les LLM et les agents),
avec un solide passage par le ML (cours 9) et la vision (cours 10).

---

## 4. Comment une machine « apprend » : les 3 types d'apprentissage

C'est LE concept clé du machine learning. Il existe **trois grandes façons** d'apprendre :

### 4.1 Apprentissage supervisé (le plus courant)

On donne à la machine des **exemples étiquetés** : une entrée + la bonne réponse.

```
Photo de chat   → étiquette "chat"
Photo de chien  → étiquette "chien"
... (des milliers d'exemples) ...
```

La machine apprend la correspondance, puis sait étiqueter une **nouvelle** photo.
👉 C'est ce qu'on verra aux **cours 9 et 10**.

**Deux sous-cas :**
- **Classification** : prédire une *catégorie* (chat/chien, spam/pas spam)
- **Régression** : prédire un *nombre* (le prix d'une maison, la météo de demain)

### 4.2 Apprentissage non-supervisé

Pas d'étiquettes. La machine cherche **toute seule** des structures dans les données.

```
10 000 clients  →  la machine trouve 4 groupes qui se ressemblent
```

👉 Usage typique : **segmentation** de clients, **détection d'anomalies**, compression.

### 4.3 Apprentissage par renforcement

La machine apprend par **essai / erreur**, guidée par une **récompense**.

```
Action  →  Récompense (+1) ou punition (-1)  →  ajuste sa stratégie  →  recommence
```

👉 Usage typique : **jeux** (AlphaGo a battu le champion du monde de Go), **robotique**,
et même l'affinage des LLM (le fameux « RLHF »).

| Type | A besoin d'étiquettes ? | Question posée |
|---|---|---|
| Supervisé | ✅ Oui | « Quelle est la bonne réponse ? » |
| Non-supervisé | ❌ Non | « Quels groupes existent ? » |
| Renforcement | ⚠️ Récompenses | « Quelle action rapporte le plus ? » |

---

## 5. Le vocabulaire de survie

Tu vas croiser ces mots **partout**. Garde `glossaire.md` ouvert, mais voici l'essentiel :

| Mot | Ce que ça veut dire |
|---|---|
| **Modèle** | Le « cerveau » entraîné qui fait des prédictions |
| **Dataset** | L'ensemble des données d'exemple |
| **Feature** | Une caractéristique d'entrée (la surface d'une maison) |
| **Label** | La bonne réponse associée (le prix réel) |
| **Entraînement** | La phase où le modèle apprend (lente, coûteuse) |
| **Inférence** | La phase où on l'utilise pour prédire (rapide) |
| **Paramètres / poids** | Les milliers (ou milliards) de réglages internes ajustés à l'entraînement |
| **GPU** | La puce qui rend l'entraînement rapide (calcul massivement parallèle) |

> 💡 Analogie : entraîner un modèle, c'est comme **réviser** ; faire de l'inférence, c'est
> **passer l'examen**. On révise longtemps une fois, on répond vite plein de fois.

---

## 6. 60 ans d'IA en 5 dates

Comprendre l'histoire évite de croire que « l'IA est née avec ChatGPT ».

| Année | Événement | Pourquoi ça compte |
|---|---|---|
| **1958** | Le **perceptron** (premier neurone artificiel) | L'idée du réseau de neurones naît |
| **1970-1990** | Les « **hivers de l'IA** » | Trop de promesses, pas assez de résultats → financements coupés |
| **2012** | **AlexNet** gagne ImageNet | Le **deep learning** explose, la vision décolle |
| **2017** | Les **Transformers** (« Attention is all you need ») | L'architecture derrière TOUS les LLM modernes |
| **2022** | **ChatGPT** | L'IA générative devient grand public |

Deux ingrédients ont tout débloqué après 2012 : **assez de données** (Internet) et **assez de
puissance** (GPU). Les idées, elles, existaient depuis longtemps.

---

## 7. Limites & garde-fous (garder l'esprit critique)

Une IA impressionnante reste un outil faillible. À connaître **dès le premier jour** :

- **Biais** : un modèle reproduit (et amplifie) les biais de ses données d'entraînement.
  Données biaisées → décisions biaisées (recrutement, crédit, justice…).
- **Hallucinations** : un LLM peut **inventer** une réponse fausse avec un aplomb total.
  Il optimise « ce qui sonne juste », pas « ce qui est vrai ».
- **Dépendance aux données** : *garbage in, garbage out*. Pas de bonnes données, pas de bon modèle.
- **Coût & énergie** : entraîner les gros modèles coûte des millions et consomme beaucoup.
- **Vie privée & droit d'auteur** : d'où viennent les données ? Avait-on le droit ?

> ⚠️ Règle d'or pour la suite du parcours : **une IA propose, un humain dispose.**
> On vérifie toujours, surtout sur des décisions qui comptent.

---

## 8. La carte de nos 5 journées

Voilà où chaque cours suivant se range dans le panorama :

| Cours | Thème | Famille / concept | Ce que ça débloque |
|---|---|---|---|
| **8** | Panorama (ici) | Vue d'ensemble | Le vocabulaire et les repères |
| **9** | Machine Learning | Supervisé classique | Faire prédire un modèle depuis des données |
| **10** | Deep Learning & Vision | Réseaux de neurones | Comprendre l'intuition derrière le deep learning |
| **11** | LLM | Langage + génératif | Comprendre et piloter les grands modèles de langage |
| **12** | Agents LLM | Génératif + décision | L'IA qui **agit** : utilise des outils, enchaîne des actions |

> 🎯 Le gros morceau du parcours, ce sont les **cours 11 et 12** (LLM et agents).
> Les cours 9 et 10 te donnent les fondations pour comprendre *comment* ces modèles marchent.

---

## 9. Pour aller plus loin (en autonomie)

Rien ne vaut la manipulation directe. Ces démos tournent dans le navigateur, sans rien installer :

- **Teachable Machine** (Google) : entraîne un modèle de vision en 3 minutes avec ta webcam
  → https://teachablemachine.withgoogle.com
- **Quick, Draw!** (Google) : un réseau de neurones devine tes dessins
  → https://quickdraw.withgoogle.com
- **Can't Find My Way** / visualisations de réseaux : voir un réseau « réfléchir »
- Un **LLM** (ChatGPT, Claude, Le Chat de Mistral…) : pose-lui une question piège et
  cherche une **hallucination**. Tu en trouveras.

Note ce que tu observes : ça nourrira les exercices de `exos.md`.
