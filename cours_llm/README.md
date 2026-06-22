# Cours 11 - Les LLM : comprendre et utiliser

Quatrième journée - on entre dans le gros morceau du parcours. Un LLM (Large Language Model),
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
├── 1_premier_appel.py          ← ton premier appel à un LLM
├── 2_prompting.py              ← rôle système, few-shot, température
├── 3_sortie_structuree_json.py ← forcer une réponse en JSON exploitable
├── 4_conversation_memoire.py   ← un mini-chat qui se souvient
├── 5_mini_rag.py               ← répondre à partir de TES documents
├── 6_embeddings.py             ← similarité de SENS (le vrai moteur d'un RAG)
├── exos.md
└── corriges/
```

## Configuration (à faire une fois)

Le code passe par l'interface compatible OpenAI. Par défaut on cible **Anthropic
(Claude)**, qui l'expose aussi ; le même code marche avec OpenAI, Mistral, ou un
modèle local via Ollama (gratuit) — il suffit de changer le `.env`.

```bash
cd cours_llm
source ../.venv/bin/activate
pip install -r requirements.txt

cp .env.example .env       # puis ouvre .env et remplis-le
```

Deux exemples de `.env` (choisis-en un) :

Option A - Anthropic / Claude (clé API requise)
```
LLM_BASE_URL=https://api.anthropic.com/v1/
LLM_API_KEY=sk-ant-ta-cle-ici
LLM_MODEL=claude-sonnet-4-6
```

Option B - Ollama en local (gratuit, sans clé)
```
LLM_BASE_URL=http://localhost:11434/v1
LLM_API_KEY=ollama
LLM_MODEL=llama3.2
```
> Pour l'option B : installe Ollama (https://ollama.com), puis `ollama pull llama3.2`.

> ⚠️ **Démo 6 (embeddings)** : Anthropic ne fournit pas d'API d'embeddings. Pour cette
> démo uniquement, renseigne un fournisseur séparé dans le `.env` (variables `EMBED_*` :
> Voyage AI, OpenAI, ou Ollama). Exemples prêts à l'emploi dans `.env.example`.

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
