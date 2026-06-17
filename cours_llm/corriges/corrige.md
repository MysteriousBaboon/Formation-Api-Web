# Corrigés — Les LLM

> Les réponses d'un LLM varient d'un modèle et d'une exécution à l'autre. On corrige donc
> le raisonnement, pas le texte exact. Un corrigé de code est dans `corriges/exo_3_avis.py`.

---

## Exercice 1 — Sentir la génération

1. Les réponses diffèrent (souvent) : la température par défaut (> 0) introduit de l'aléatoire
   dans le choix du token suivant.
2. Le français consomme un peu plus de tokens que l'anglais ; un mot rare ou fautif est découpé
   en plusieurs tokens (le modèle ne l'a pas « en entier » dans son vocabulaire).
3. La plupart des modèles instruct respectent bien une consigne de format claire (« 3 puces »).

---

## Exercice 2 — Le pouvoir du prompt

1. La personnalité « pirate » change nettement le style : le message system cadre tout.
2. Sans les exemples, le modèle risque de répondre en texte normal au lieu d'émojis : le
   *few-shot* sert justement à montrer le format attendu plutôt qu'à le décrire.
3. À `temperature=0`, la réponse est stable (quasi identique à chaque fois) ; à `1.2`, elle
   varie beaucoup (créative mais imprévisible).

---

## Exercice 3 — JSON exploitable

1. Sur un avis positif, `sentiment` passe à `"positif"` et `note` monte (4-5).
2. Le champ `"urgence"` est rempli si la consigne est claire ; `temperature=0` fiabilise le format.
3. Voir `corriges/exo_3_avis.py` : on boucle sur une liste d'avis et on imprime un récap.
   Point clé : on parse le JSON (`json.loads`) pour exploiter les champs en Python.

---

## Exercice 4 — La mémoire d'un chat

1. Il se souvient car on lui renvoie tout l'historique à chaque appel — la mémoire n'est pas
   « dans » le modèle, elle est dans notre liste `historique`.
2. En retirant l'ajout des réponses de l'assistant, il perd le fil : il ne voit plus ce qu'il
   a déjà dit, les réponses deviennent incohérentes.
3. L'historique grossit, donc plus de tokens à chaque appel, donc plus cher et plus lent. Parade :
   résumer les vieux messages, ou ne garder que les N derniers.

---

## Exercice 5 — Ton premier RAG

1. Pour la « couleur préférée du PDG », le modèle doit répondre qu'il ne sait pas (l'info n'est
   pas dans le contexte). C'est le bon comportement : on lui a demandé de s'appuyer uniquement
   sur le contexte, donc moins d'hallucinations.
2-3. Sur tes propres documents, il répond juste quand l'info est présente, et devrait admettre
   son ignorance sinon (c'est tout l'intérêt de la consigne système du RAG).
4. Donner les 2 meilleurs passages aide quand la réponse est répartie sur plusieurs documents.
