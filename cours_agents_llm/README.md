# 🦾 Cours 12 — Agents LLM (le gros morceau)

Dernière journée — le **bouquet final**. Jusqu'ici, le LLM *répondait*. Maintenant, il va **agir** :
utiliser une calculatrice, appeler une API, enchaîner plusieurs étapes pour atteindre un but.
C'est ça, un **agent**.

## 🎯 Objectifs

À la fin de cette journée, tu seras capable de :

- Expliquer ce qu'est un **agent** (la boucle *perception → raisonnement → action*)
- Comprendre le **function / tool calling** : donner des outils au LLM
- Coder la **boucle agentique** (style *ReAct*) à la main pour la démystifier
- Construire un **agent multi-outils** qui choisit le bon outil
- Brancher un agent sur le **monde réel** (ton micro-service / n8n des cours précédents)
- Connaître les **garde-fous** (boucles infinies, coûts, sécurité)

## 📁 Structure

```
cours_agents_llm/
├── README.md
├── cours.md                  ← le cours complet (à lire en premier)
├── slides/
│   ├── contenu.py
│   └── agents_llm.pptx
├── requirements.txt
├── .env.example              ← copie en .env (mêmes infos qu'au cours 11)
├── config.py                 ← charge le .env et construit le client
├── 1_function_calling.py     ← le LLM décide d'appeler une fonction
├── 2_outil_calculatrice.py   ← un outil pour ce que le LLM rate (les maths)
├── 3_agent_boucle_react.py   ← la boucle d'agent codée À LA MAIN (ReAct)
├── 4_agent_multi_outils.py   ← un agent qui choisit entre plusieurs outils
├── 5_agent_vers_n8n.py       ← l'agent agit sur le monde réel (webhook / API)
├── exos.md                   ← projet fil rouge : ton propre agent
└── corriges/
```

## ⚙️ Configuration

Même principe qu'au cours 11 (code **agnostique** via `.env`).

```bash
cd cours_agents_llm
source ../.venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # puis remplis-le
python 1_function_calling.py
```

> ⚠️ **Tool calling natif** : les démos `1`, `2`, `4` utilisent la capacité « tools » du modèle.
> Elle marche avec OpenAI, Mistral, Groq… et les modèles Ollama récents (ex. `llama3.1`/`llama3.2`).
> La démo `3` (ReAct à la main) fonctionne avec **n'importe quel** modèle — c'est aussi la plus
> pédagogique pour comprendre ce qui se passe « sous le capot ».

## 🔗 Le lien avec le reste — la boucle se referme

Un agent, c'est la **synthèse de tout le parcours** :

```
        LLM (cours 11) ───┐
                          ├──▶  AGENT  ──▶ outils
   ton micro-service ─────┘                 │
     (cours 3)                              ├─ calculatrice
                                            ├─ ton API Python (cours 3)
   n8n / cron (cours 7) ◀───────────────────┘  déclenche / reçoit
```

- Un **outil** d'agent peut être **ton micro-service du cours 3**.
- Un agent peut être **déclenché par n8n / cron** (cours 7) et lui **renvoyer** un résultat.
- Tu boucles ainsi tout ce que tu as appris : Python → API → automatisation → IA qui agit.

> 🎓 C'est la dernière séance : `exos.md` propose un **projet fil rouge** pour assembler tout ça.
