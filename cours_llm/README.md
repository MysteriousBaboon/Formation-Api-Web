# Cours 11 — Les LLM : comprendre et utiliser

Quatrième journée — on entre dans le gros morceau du parcours. Un LLM (Large Language Model),
c'est le moteur derrière ChatGPT, Claude, Mistral… D'abord comment ça marche (théorie),
puis comment en piloter un par code (pratique).

## Objectifs

À la fin de cette journée, tu seras capable de :

- Expliquer tokens, prédiction du token suivant, fenêtre de contexte
- Donner l'intuition du Transformer et de l'attention
- Distinguer pré-entraînement / fine-tuning / RLHF
- Écrire de bons prompts (rôle système, few-shot, consignes claires)
- Appeler un LLM en Python de façon agnostique (le tien, ou un modèle local)
- Obtenir une sortie structurée (JSON) et gérer une conversation avec mémoire
- Comprendre le principe du RAG (donner des documents au modèle)

## Structure

```
cours_llm/
├── README.md
├── cours.md                    ← le cours complet (à lire en premier)
├── slides/
│   ├── contenu.py
│   └── llm.pptx
├── requirements.txt
├── .env.example                ← copie-le en .env et remplis tes infos
├── config.py                   ← charge le .env et construit le client (à ne pas modifier)
├── 1_premier_appel.py          ← ton premier appel à un LLM
├── 2_prompting.py              ← rôle système, few-shot, température
├── 3_sortie_structuree_json.py ← forcer une réponse en JSON exploitable
├── 4_conversation_memoire.py   ← un mini-chat qui se souvient
├── 5_mini_rag.py               ← répondre à partir de TES documents
├── exos.md
└── corriges/
```

## Configuration (à faire une fois)

Le code est agnostique : il marche avec n'importe quel fournisseur compatible OpenAI
(OpenAI, Mistral, Groq, Together… ou un modèle local via Ollama, gratuit).

```bash
cd cours_llm
source ../.venv/bin/activate
pip install -r requirements.txt

cp .env.example .env       # puis ouvre .env et remplis-le
```

Deux exemples de `.env` (choisis-en un) :

Option A — un service en ligne (clé API requise)
```
LLM_BASE_URL=https://api.openai.com/v1
LLM_API_KEY=sk-ta-cle-ici
LLM_MODEL=gpt-4o-mini
```

Option B — Ollama en local (gratuit, sans clé)
```
LLM_BASE_URL=http://localhost:11434/v1
LLM_API_KEY=ollama
LLM_MODEL=llama3.2
```
> Pour l'option B : installe Ollama (https://ollama.com), puis `ollama pull llama3.2`.

## Pour démarrer

```bash
python 1_premier_appel.py
```
> Si le `.env` n'est pas configuré, le script te l'explique clairement (pas de plantage cryptique).

## Le lien avec le reste

Un LLM est un gros réseau de neurones (un Transformer, cours 10). Appeler une API, tu sais
déjà faire (cours_api). Ici on combine les deux. Et c'est le socle du Cours 12 : un *agent*,
c'est un LLM à qui on donne des outils pour agir.

```
[Cours 10: réseaux de neurones]  →  [Cours 11: LLM]  →  [Cours 12: agents]
```
