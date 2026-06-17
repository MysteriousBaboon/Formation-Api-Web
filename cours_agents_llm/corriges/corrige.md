# ✅ Corrigés — Agents LLM

> Le comportement exact dépend du modèle. On corrige le **raisonnement** et la **mécanique**.
> Un agent complet d'exemple est dans `corriges/mon_agent.py`.

---

## Exercice 1 — Comprendre le tool calling

1. Oui, le LLM appelle `obtenir_meteo` avec `ville="Lyon"` : la question s'y prête.
2. Pour « raconte une blague », il **n'appelle pas** l'outil : il répond directement. Le modèle
   n'utilise un outil que quand c'est **pertinent** — c'est lui qui décide.
3. Pour deux villes, il demande généralement **deux appels** (un par ville).
4. **C'est TON code** qui exécute `obtenir_meteo`. Le LLM ne fait que **demander** l'appel ; il
   ne lance jamais lui-même de code.

---

## Exercice 2 — L'outil qui sauve les maths

1. Sans outil, le LLM se **trompe** souvent sur un grand produit (il devine). Avec l'outil
   calculatrice, la réponse est **exacte** (c'est Python qui calcule).
2. Sur un calcul en plusieurs étapes, l'agent peut **enchaîner** plusieurs appels.
3. `calculer('__import__("os")')` est bloqué car notre évaluateur n'autorise **que** des nombres
   et des opérations arithmétiques (via `ast`). Un `eval()` brut, lui, exécuterait n'importe quel
   code envoyé par le LLM → faille de sécurité majeure.

---

## Exercice 3 — La boucle d'agent à la main

1. Le cycle visible : `Pensée → Action → Observation`, répété.
2. Le calcul TTC demande **2 étapes** (3 × 19,99, puis × 1,20) → donc au moins 2 tours d'outil.
3. Avec `max_etapes=1`, l'agent n'a pas le temps de finir → le **garde-fou** s'active.
4. Ajout de `heure` : importer `heure_actuelle`, l'ajouter à `OUTILS` **et** au prompt `SYSTEME`
   (sinon le modèle ne sait pas qu'il existe).

---

## Exercice 4 — Agent multi-outils

1. L'agent appelle les outils dans l'ordre qui lui semble logique (souvent heure, météo, puis
   calcul) — parfois plusieurs dans le même tour.
2. Ajout de `convertir_euros_dollars` : il faut le mettre dans `REGISTRE` (la fonction) **et**
   `OUTILS` (la description), sinon il est invisible ou inexécutable.
3. **Natif** (`tools`) : robuste, propre, mais demande un modèle compatible. **À la main** (ReAct) :
   marche partout, très pédagogique, mais plus fragile (parsing du texte).

---

## Exercice 5 — L'agent qui agit

1. Sans webhook, l'envoi est simulé : l'agent a tout de même **rédigé** un titre et un message
   d'alerte cohérents (ex. « Stock critique : Café Premium »).
2. Avec une URL webhook.site, on **voit** la requête POST arriver en temps réel.
3. Garde-fous avant un vrai email : **validation humaine** obligatoire, liste blanche de
   destinataires, limite de fréquence, journalisation, et un mode « brouillon » avant envoi.

---

## Projet fil rouge

Voir `corriges/mon_agent.py` (assistant de budget). Les points évalués :
- **≥ 2 outils** réellement utilisés selon la demande,
- une **boucle** d'agent avec **garde-fou** (`max_tours`),
- le LLM **choisit** les outils (il n'appelle pas tout systématiquement),
- bonus : un outil qui touche le monde réel (API, fichier, webhook).
