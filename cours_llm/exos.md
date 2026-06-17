# Exercices — Les LLM (≈ 3h, en autonomie)

> Format adapté : aujourd'hui on pratique. Configure d'abord ton `.env` (voir README),
> puis déroule les démos `1` à `5` et les exercices ci-dessous. Corrigés dans `corriges/`.
>
> Prérequis : `pip install -r requirements.txt` + un `.env` configuré (`cp .env.example .env`).

---

## Exercice 0 — Configuration (15 min)

1. `cp .env.example .env`, puis remplis-le (service en ligne ou Ollama local).
2. Lance `python 1_premier_appel.py`. Tu obtiens une réponse ?
   Sinon, lis le message d'aide : il te dit quoi corriger.

> Pas de clé / pas de budget ? Installe Ollama (gratuit) et utilise l'option B du `.env`.

---

## Exercice 1 — Sentir la génération (20 min)

À partir de `1_premier_appel.py` :

1. Pose deux fois la même question. Les réponses sont-elles identiques mot pour mot ? Pourquoi ?
2. Va sur https://platform.openai.com/tokenizer, colle une phrase française : combien de tokens ?
   Essaie un mot rare ou avec une faute : il est découpé en plus de morceaux ?
3. Demande explicitement « réponds en exactement 3 puces ». La consigne de format est-elle suivie ?

---

## Exercice 2 — Le pouvoir du prompt (30 min)

À partir de `2_prompting.py` :

1. Ajoute une 3e personnalité dans la partie 1 (ex. « Tu es un pirate du 18e siècle »). Net ?
2. Dans le few-shot (partie 2), retire les 2 exemples : le modèle répond-il encore en émojis ?
   Qu'est-ce que ça prouve sur l'utilité des exemples ?
3. Lance plusieurs fois la partie 3. La réponse à `temperature=0` change-t-elle ? Et à `1.2` ?

---

## Exercice 3 — JSON exploitable (35 min)

À partir de `3_sortie_structuree_json.py` :

1. Change l'avis client par un avis positif. Les champs s'adaptent-ils correctement ?
2. Ajoute un champ `"urgence"` (true/false) dans la consigne système. Le modèle le remplit-il ?
3. Mini-projet : crée une liste de 3 avis, boucle dessus, et affiche un tableau récap
   (sentiment + note) pour chaque. Tu viens de construire un analyseur d'avis automatique.

> `temperature=0` est ton ami pour tout ce qui doit être régulier et parsable.

---

## Exercice 4 — La mémoire d'un chat (25 min)

À partir de `4_conversation_memoire.py` :

1. Lance-le, présente ton prénom, discute 2-3 tours, puis demande « comment je m'appelle ? ».
   Il s'en souvient. Pourquoi (qu'est-ce qui est renvoyé à chaque appel) ?
2. Commente la ligne qui ajoute la réponse de l'assistant à l'historique. Relance : que se passe-t-il ?
3. Observe le compteur de messages monter. En quoi est-ce un problème de coût sur une longue
   conversation ? Quelle stratégie pour l'atténuer (indice dans les commentaires) ?

---

## Exercice 5 — Ton premier RAG (40 min)

À partir de `5_mini_rag.py` :

1. Lance-le. Pour la question « couleur préférée du PDG », que répond le modèle ? Pourquoi est-ce
   le bon comportement ?
2. Remplace `DOCUMENTS` par 5 phrases sur un sujet que tu connais (ton asso, ton jeu préféré…).
   Pose-lui des questions : répond-il juste ?
3. Pose une question dont la réponse n'est pas dans tes docs. L'admet-il, ou invente-t-il ?
4. Bonus : modifie `chercher_passage` pour renvoyer les 2 meilleurs passages
   (`similarites.argsort()[-2:]`) et donne-les au LLM. Les réponses s'améliorent-elles ?

---

## Checklist d'auto-évaluation

- [ ] J'ai configuré un LLM et obtenu une réponse par code (exo 0-1)
- [ ] Je sais ce qu'est un token et la génération token-par-token (§2-3)
- [ ] Je sais utiliser le rôle `system`, le few-shot et la température (exo 2)
- [ ] Je sais forcer une sortie JSON et la parser (exo 3)
- [ ] Je comprends qu'un LLM n'a pas de mémoire (on rejoue l'historique) (exo 4)
- [ ] J'ai construit un mini-RAG sur mes propres documents (exo 5)

> Si tout est coché, place au bouquet final : Cours 12 — Agents LLM.
