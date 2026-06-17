# 🧪 Exercices — Agents LLM (≈ 3h, en autonomie)

> 🦿 **Format adapté.** Dernière séance, on construit. Configure ton `.env` (comme au cours 11),
> déroule les démos `1` à `5`, puis attaque le **projet fil rouge**. Corrigés dans `corriges/`.
>
> Prérequis : `pip install -r requirements.txt` + `.env` configuré.
> ⚠️ Démos 1, 2, 4 : modèle qui supporte le *tool calling*. Démo 3 : n'importe quel modèle.

---

## Exercice 1 — Comprendre le tool calling (25 min)

À partir de `1_function_calling.py` :

1. Lance-le. Le LLM appelle-t-il `obtenir_meteo` ? Affiche-t-il la bonne ville en argument ?
2. Pose une question SANS rapport (« raconte une blague »). Appelle-t-il l'outil ? Pourquoi ?
3. Demande la météo de **deux villes**. Combien d'appels d'outil demande-t-il ?
4. **Question clé** : qui exécute réellement la fonction `obtenir_meteo` — le LLM ou ton code ?

---

## Exercice 2 — L'outil qui sauve les maths (25 min)

À partir de `2_outil_calculatrice.py` :

1. La réponse **sans** outil au gros calcul est-elle exacte ? Et **avec** ?
2. Pose un calcul en plusieurs étapes : l'agent enchaîne-t-il les appels à la calculatrice ?
3. **Sécurité** : lance `python outils.py` et observe que `calculer('__import__("os")')` est
   **bloqué**. Explique pourquoi un `eval()` brut serait dangereux ici.

---

## Exercice 3 — La boucle d'agent à la main (35 min) ⭐

À partir de `3_agent_boucle_react.py` (la démo la plus importante à comprendre) :

1. Lance-le et **lis chaque étape**. Repère le cycle *Pensée → Action → Observation*.
2. Combien d'étapes a-t-il fallu pour le calcul TTC ? Pourquoi plus d'une ?
3. Mets `max_etapes=1` : le garde-fou anti-boucle se déclenche-t-il ?
4. Ajoute l'outil `heure` : importe `heure_actuelle`, ajoute-le à `OUTILS` **et** décris-le dans
   le prompt `SYSTEME`. Pose une question qui l'utilise.

---

## Exercice 4 — Agent multi-outils (30 min)

À partir de `4_agent_multi_outils.py` :

1. Lance-le. Dans quel **ordre** l'agent appelle-t-il les outils pour la question à 3 volets ?
2. Ajoute un outil `convertir_euros_dollars(montant)` (taux fixe 1,08) dans `REGISTRE` **et**
   `OUTILS`. Pose une question qui le déclenche.
3. Compare avec la démo 3 : tool calling **natif** vs boucle **à la main** — avantages de chacun ?

---

## Exercice 5 — L'agent qui agit (25 min) 🌍

À partir de `5_agent_vers_n8n.py` :

1. Lance-le sans webhook : l'envoi est **simulé**. Quel titre/message l'agent a-t-il rédigé ?
2. Crée un webhook gratuit sur https://webhook.site, colle l'URL dans `N8N_WEBHOOK_URL` (`.env`),
   relance : tu **vois** l'alerte arriver. 🎉
3. **Réflexion** : quels garde-fous mettrais-tu avant qu'un agent envoie un **vrai** email ?

---

## 🏗️ Projet fil rouge — Ton assistant agent (60 min)

Crée `mon_agent.py` : un agent qui combine **au moins 2 outils** pour une tâche utile **à toi**.
Idées : assistant de courses (calcul + liste), veille météo + alerte, mini-CRM…

**Cahier des charges minimal :**
1. Au moins **2 outils** (réutilise `outils.py` ou crée les tiens).
2. Une **boucle** d'agent (style démo 4) avec un **garde-fou** (`max_tours`).
3. L'agent doit **choisir** ses outils selon la question (ne pas tout appeler bêtement).
4. **Bonus** : un outil qui appelle une vraie API (la tienne du cours 3, ou une API publique).

> 💡 Pars d'une copie de `4_agent_multi_outils.py` et adapte. Un corrigé d'exemple
> (assistant de budget) est dans `corriges/mon_agent.py`.

---

## ✅ Checklist d'auto-évaluation

- [ ] J'explique ce qu'est un agent (LLM + outils + boucle) (§1-2)
- [ ] Je comprends le tool calling, et que c'est MON code qui exécute (exo 1)
- [ ] Je sais pourquoi donner une calculatrice à un LLM (exo 2)
- [ ] J'ai suivi une boucle ReAct étape par étape (exo 3)
- [ ] J'ai construit un agent multi-outils avec garde-fou (exo 4 + projet)
- [ ] J'ai fait agir un agent sur l'extérieur (webhook) (exo 5)
- [ ] J'ai assemblé mon propre agent (projet fil rouge)

> 🎓 **Félicitations** — tu as bouclé le parcours, de la variable Python à l'agent autonome !
