# Cours - Les LLM : comprendre et utiliser

> Un LLM (Large Language Model) est un gigantesque réseau de neurones entraîné à prédire le mot suivant. De cette idée simple sort tout le reste : conversation, traduction, code, raisonnement. Ce cours explique le « comment », puis te met aux commandes.

---

## 1. C'est quoi un LLM, en une phrase

> Un LLM est un modèle qui, à partir d'un texte, prédit le morceau de texte le plus probable
> ensuite, et qui, en répétant l'opération, écrit des phrases entières.

C'est tout. Il n'y a pas de base de données de réponses, pas de « compréhension » au sens humain.
Juste un réseau de neurones géant (un Transformer, cf. cours 10) avec des milliards de poids,
entraîné sur une énorme quantité de texte.

---

## 2. Les tokens : l'unité que lit le modèle

Un LLM ne voit pas des lettres ni vraiment des mots, mais des **tokens** : des morceaux de mots.

```
"L'intelligence artificielle"  →  ["L'", "intel", "ligence", " artificielle"]
```

- En moyenne, 1 token ≈ 4 caractères (≈ ¾ d'un mot en anglais, un peu plus en français).
- On paie au token (entrée + sortie), et la fenêtre de contexte se mesure en tokens.
- Découper en tokens permet de gérer des mots inconnus, des fautes, du code…

> Teste sur https://platform.openai.com/tokenizer : colle un texte, vois ses tokens.

---

## 3. Comment il génère : un mot à la fois

Le modèle ne « pond » pas une réponse d'un coup. Il génère token par token, en boucle :

```
"Le chat est sur le"  →  modèle  →  "toit" (87%) / "canapé" (8%) / "lit" (3%) ...
   on ajoute "toit", puis on recommence avec "Le chat est sur le toit" → ...
```

À chaque étape, il calcule une probabilité pour chaque token possible, en choisit un, l'ajoute,
et recommence. C'est de l'autocomplétion très, très sophistiquée.

> C'est pour ça qu'un LLM peut « halluciner » : il choisit ce qui est probable, pas ce qui
> est vrai. Les deux coïncident souvent, mais pas toujours.

---

## 4. Le Transformer et l'attention (intuition)

L'architecture qui a tout changé (2017) s'appelle le **Transformer**. Son ingrédient clé :
le mécanisme d'**attention**.

> L'attention permet à chaque mot de « regarder » tous les autres mots de la phrase pour se
> situer. Dans « la souris mange le fromage parce qu'elle a faim », le modèle relie « elle »
> à « la souris », pas au « fromage ».

C'est ce qui donne au modèle le contexte : il ne traite pas les mots isolément, mais en
relation les uns avec les autres. (Pas besoin des maths ici : retiens l'idée de « tout relier à tout ».)

---

## 5. Plus gros sans exploser le coût : le Mixture of Experts (MoE)

Comment fait-on des modèles toujours plus « savants » sans que chaque réponse coûte une
fortune en calcul ? L'astuce des plus grands modèles récents (Mixtral, GPT-4, DeepSeek…)
s'appelle le **Mixture of Experts** (MoE), littéralement « mélange d'experts ».

> Au lieu d'un seul gros réseau qui traite chaque token, le modèle contient plusieurs
> sous-réseaux spécialisés, les **experts**. Pour chaque token, un petit aiguilleur (le
> *router*) choisit les 2 ou 3 experts les plus pertinents - et ignore tous les autres.

Image : plutôt qu'un seul généraliste qui répond à tout, un cabinet de spécialistes où une
secrétaire oriente chaque question vers les bons médecins. On ne dérange que ceux qu'il faut.

Le gain est dans cette distinction :

| | Modèle « dense » classique | Modèle MoE |
|---|---|---|
| Paramètres stockés | N | Beaucoup plus que N |
| Paramètres activés par token | Tous | Une petite fraction |
| Coût de calcul | Élevé | Réduit, à qualité égale |

Le modèle a donc énormément de paramètres au total (il « sait » beaucoup de choses), mais
n'en allume qu'une petite partie à chaque token (il calcule peu).

> Concrètement, un MoE peut avoir la « culture » d'un modèle de 100 milliards de paramètres
> pour un coût de calcul proche d'un modèle de 15 milliards. C'est pour ça que la plupart des
> modèles de pointe récents sont des MoE.

À retenir : **beaucoup de connaissances stockées, peu de calcul dépensé par token**, grâce à
un aiguillage vers quelques experts.

---

## 6. Comment on l'entraîne (survol)

Trois grandes phases :

| Phase | Ce qui se passe | Résultat |
|---|---|---|
| Pré-entraînement | Lire une montagne de texte, prédire le mot suivant | Un modèle « brut » qui sait écrire |
| Fine-tuning (instruct) | Réentraîner sur des paires question/réponse | Un modèle qui suit des instructions |
| RLHF | Des humains classent les réponses, le modèle apprend leurs préférences | Un modèle plus utile et plus sûr |

> Le pré-entraînement coûte des millions (c'est rare). Le fine-tuning, lui, est
> accessible : on part d'un modèle existant et on l'adapte. (RLHF = *Reinforcement Learning from
> Human Feedback* : tu reconnais le « renforcement » du cours 8 !)

---

## 7. La fenêtre de contexte

C'est la quantité de texte que le modèle peut « voir » d'un coup (prompt + réponse), mesurée
en tokens.

- Petite fenêtre (4k tokens) : quelques pages.
- Grande fenêtre (128k, 1M…) : un livre entier.
- Au-delà, le modèle « oublie » le début. Il n'a aucune mémoire entre deux appels :
  si tu veux qu'il se souvienne, tu dois lui renvoyer l'historique (cf. démo 4).

> Un LLM est sans mémoire par défaut. Chaque appel est indépendant. La « mémoire » d'un
> chat, c'est juste l'historique qu'on rejoue à chaque fois.

---

## 8. Le prompting : bien parler au modèle

La qualité de la réponse dépend énormément de la question. Quelques principes.

### Les rôles
Un appel LLM se compose de messages, chacun avec un rôle :
- system : le cadre, la personnalité, les règles (« Tu es un prof de Python concis »)
- user : la demande de l'utilisateur
- assistant : les réponses précédentes du modèle (pour la mémoire)

### Les bonnes pratiques
1. Être précis : dis le format, la longueur, le ton attendus.
2. Donner des exemples (*few-shot*) : montrer 2-3 cas guide énormément le modèle.
3. Découper : pour une tâche complexe, demande des étapes.
4. Cadrer le rôle : le message *system* oriente tout le reste.

> *Zero-shot* = on demande sans exemple. *Few-shot* = on fournit quelques exemples dans le
> prompt. Le few-shot améliore souvent nettement la régularité des réponses.

---

## 9. Les paramètres : la température

Quand le modèle choisit le token suivant, la **température** règle son audace :

| Température | Comportement | Pour quoi |
|---|---|---|
| 0 | Toujours le plus probable, déterministe | Code, extraction, classification |
| 0.7 | Équilibré | Conversation générale |
| 1.2+ | Créatif, surprenant (et plus risqué) | Brainstorming, écriture créative |

> Pour une tâche où tu veux des résultats fiables et reproductibles (extraire un JSON,
> classer un avis), mets `temperature=0`.
>
> La température maximale dépend du fournisseur : **1.0 chez Anthropic (Claude)**,
> jusqu'à 2 chez OpenAI. Les démos restent à 1.0 pour fonctionner partout.

---

## 10. Les limites (à ne jamais oublier)

- Hallucinations : invente avec aplomb. Toujours vérifier les faits, chiffres, citations.
- Cutoff : ses connaissances s'arrêtent à une date. Il ignore l'actualité récente.
- Pas de calcul fiable : un LLM « devine » les maths, il ne calcule pas (→ donne-lui un outil, cours 12).
- Coût et latence : chaque appel prend du temps et de l'argent (au token).
- Biais et confidentialité : il reflète ses données ; n'y colle pas de secrets sans précaution.

> La parade à plusieurs de ces limites : lui donner des outils et des documents.
> C'est le RAG (§12) et les agents (cours 12).

---

## 11. Appeler un LLM par code (agnostique)

Tous les fournisseurs majeurs exposent la même interface (compatible OpenAI), Anthropic
compris. D'où un code unique qui marche partout, piloté par le `.env` :

```python
from openai import OpenAI
client = OpenAI(base_url=LLM_BASE_URL, api_key=LLM_API_KEY)

reponse = client.chat.completions.create(
    model=LLM_MODEL,
    messages=[
        {"role": "system", "content": "Tu es un assistant concis."},
        {"role": "user", "content": "Explique un token en une phrase."},
    ],
    temperature=0.7,
)
print(reponse.choices[0].message.content)
```

Change le `.env` (Anthropic ↔ OpenAI ↔ Ollama local) : le code ne bouge pas. C'est exactement
l'esprit de l'API unifiée de scikit-learn, mais pour les LLM.

> Chaque démo (1 à 6) lit elle-même le `.env` et crée son client en quelques lignes, tout
> en haut du fichier — rien n'est caché dans un fichier annexe : tu vois l'appel au LLM en entier.

---

## 12. Le RAG : donner des documents au modèle

Un LLM ne connaît pas tes documents (ton wiki interne, tes PDF…). Le **RAG**
(*Retrieval-Augmented Generation*) résout ça :

```
Question  →  [1. Chercher les passages pertinents dans TES docs]
          →  [2. Les coller dans le prompt]
          →  [3. Le LLM répond EN S'APPUYANT sur ces passages]
```

Avantages : réponses à jour, sourcées, et moins d'hallucinations (le modèle s'appuie
sur du concret). C'est la technique la plus utilisée en entreprise.

> La démo `5_mini_rag.py` en fait une version minimale : on retrouve le bon passage (par
> similarité de *mots*, avec TF-IDF), puis on le donne au LLM. La démo `6_embeddings.py` montre
> l'étage du dessus : la similarité de *sens* avec de vrais *embeddings*.

---

## 13. Aller plus loin

- Embeddings : transformer un texte en vecteur de nombres pour mesurer la similarité de
  sens (le cœur d'un vrai RAG). → tu en fais l'expérience dans la démo `6_embeddings.py`.
- Sortie structurée : forcer du JSON pour brancher le LLM dans un programme (démo 3).
- Streaming : afficher la réponse au fur et à mesure (meilleure UX).
- Coûts : surveille tes tokens ; préfère un petit modèle quand il suffit.

Au Cours 12, on donne au LLM des outils (calculatrice, recherche, ton API du cours 3) :
il ne se contente plus de répondre, il agit.
