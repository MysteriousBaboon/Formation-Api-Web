# 🎓 Démo « tous les cours » — La Dinguerie

Une **application Flask unique** qui démontre les **12 cours** de la formation
(Python → IA), de la théorie aux agents LLM. Chaque cours a sa carte sur un hub et
ses démos testables en direct (formulaires générés automatiquement + API JSON).

## Lancer

```bash
cd "La Dinguerie/Demo Claude Code"
cp .env.example .env          # renseigne API_TOKEN et la config LLM (ou laisse l'app
                              # réutiliser les .env existants de cours_llm/ et de la racine)
python app.py                 # → http://localhost:5000
```

> Le `.venv` du repo contient déjà toutes les dépendances. Sinon : `pip install -r requirements.txt`.

## Architecture

```
app.py            Factory + hub (/) + page de cours (/cours/<slug>) + /health
config.py         Lecture des .env (LLM, embeddings, token)
registry.py       Catalogue des 12 cours et de leurs démos (SOURCE UNIQUE)
common/           auth.py · llm_client.py · charts.py · models.py · tools.py
blueprints/       1 fichier par cours (theorie, web_api, microservice, …)
templates/        base.html · hub.html · cours.html
static/           style.css · app.js (génère les formulaires, gère le token)
```

**Ajouter / modifier une démo** = éditer `registry.py` (aucun HTML/JS à toucher) et,
si besoin, ajouter la route dans le blueprint correspondant.

## Endpoints par cours

| Cours | Endpoints | Auth |
|---|---|---|
| Théorie | `POST /api/theorie/calc` | — |
| API & HTTP | `GET /api/web/heure` · `/api/web/github?user=` · `/api/web/catalogue?q=` | — |
| Microservice | `POST /api/lead/score` · `/api/emails/clean` · `/api/stats` | 🔒 |
| Cron | `GET /api/cron/expressions` · `POST /api/cron/trigger` | — |
| Données | `POST /api/data/stats` · `POST /api/data/report` (Excel) | — |
| Dataviz | `GET /api/chart` · `POST /api/chart/build` (PNG) | — |
| Scraping | `GET /api/scrape/books?pages=N` | — |
| Panorama IA | `GET /api/panorama/glossaire?q=` | — |
| Machine Learning | `POST /api/ml/iris` · `GET /api/ml/evaluate` · `/api/ml/boundary.png` | — |
| Deep Learning | `POST /api/dl/perceptron` · `/api/dl/digit` · `GET /api/dl/accuracy` | — |
| LLM | `POST /api/llm/chat` · `/api/llm/json` · `/api/llm/rag` · `/api/llm/embeddings` | 🔒 |
| Agents | `POST /api/agent/tool-calling` · `/api/agent/react` · `/api/agent/multi-tools` · `GET /api/agent/mcp-tools` | 🔒 |

🔒 = nécessite le header `Authorization: Bearer <API_TOKEN>`.

## Notes

- **Modèles ML/DL** : entraînés au premier appel puis mis en cache (datasets fournis
  par scikit-learn — Iris, Digits ; rien à télécharger).
- **LLM/Agents** : appels **réels** (interface compatible OpenAI pointée sur Anthropic).
  Garde-fous : `max_tokens` bas, timeout 30 s, et **503 explicite** si la clé manque.
- **Embeddings** : Anthropic n'en fournit pas → configure Voyage/OpenAI/Ollama, sinon 503.
- ⚠️ **Sécurité** : ne commite jamais ton `.env`. Si une clé a fuité, régénère-la.
