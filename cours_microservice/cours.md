# 📚 Cours — Micro-service Python pour étendre n8n

> Tu vas construire un petit serveur Python que n8n peut appeler pour faire ce qu'il ne sait pas faire en natif.

---

## 1. Pourquoi un micro-service ?

n8n est génial pour orchestrer, mais limité quand il faut :

- Faire du **calcul métier complexe** (scoring de leads, dédoublonnage intelligent)
- **Manipuler des données** (pandas, traitement de CSV/Excel)
- Appeler **du code Python existant** (un modèle, une lib spécifique)
- **Scraper** un site qui demande Playwright
- Faire un **traitement long** que tu ne veux pas dans le workflow n8n

Solution : tu fais une **mini-API Flask** qui expose ces fonctions, et n8n l'appelle via un nœud HTTP.

```
[Trigger n8n]  →  [HTTP node]  →  [Ton API Python]
                                      ↓
                                  (traitement)
                                      ↓
                  [Suite du workflow n8n]  ←  réponse JSON
```

---

## 2. Anatomie d'un endpoint webhook

Un endpoint = une URL qui répond à du POST avec du JSON.

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/score-lead", methods=["POST"])
def score_lead():
    data = request.get_json()
    # data = {"nom": "Alice", "entreprise": "Acme", "budget": 50000}

    score = 0
    if data.get("budget", 0) > 10000:
        score += 50
    if "@gmail" not in data.get("email", ""):  # email pro
        score += 30

    return jsonify({"score": score, "qualifie": score > 50})

if __name__ == "__main__":
    app.run(port=5000)
```

**C'est tout.** Tu as une API.

---

## 3. Tester un endpoint

### Avec curl

```bash
curl -X POST http://127.0.0.1:5000/score-lead \
  -H "Content-Type: application/json" \
  -d '{"nom": "Alice", "email": "alice@acme.com", "budget": 50000}'
```

### Avec Python

```python
import requests

r = requests.post(
    "http://127.0.0.1:5000/score-lead",
    json={"nom": "Alice", "email": "alice@acme.com", "budget": 50000},
    timeout=10,
)
print(r.json())
```

### Avec un outil graphique

- **Postman** ou **Insomnia** : interface complète
- **HTTPie** en CLI : `http POST :5000/score-lead nom=Alice budget:=50000`

---

## 4. Sécuriser avec un token

**Le problème** : si ton API est en ligne sans auth, n'importe qui peut l'appeler. Quelqu'un peut spammer ton service, voler des données, ou te coûter de l'argent (calcul, appels OpenAI...).

**La solution la plus simple** : un token partagé dans le header.

```python
import os
from functools import wraps
from flask import request, jsonify

API_TOKEN = os.getenv("API_TOKEN")

def require_token(view):
    @wraps(view)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization", "").replace("Bearer ", "")
        if token != API_TOKEN:
            return jsonify({"error": "unauthorized"}), 401
        return view(*args, **kwargs)
    return wrapper


@app.route("/score-lead", methods=["POST"])
@require_token
def score_lead():
    ...
```

Côté n8n, tu mets `Authorization: Bearer ton-token` dans les headers de la requête.

---

## 5. Valider les données entrantes

Ne JAMAIS faire confiance à ce que t'envoie un client. Toujours vérifier :

```python
@app.route("/score-lead", methods=["POST"])
def score_lead():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "JSON invalide"}), 400

    nom = data.get("nom")
    if not nom or not isinstance(nom, str):
        return jsonify({"error": "champ 'nom' manquant ou invalide"}), 400

    budget = data.get("budget", 0)
    if not isinstance(budget, (int, float)) or budget < 0:
        return jsonify({"error": "budget doit etre un nombre positif"}), 400

    # ... logique ...
```

Pour aller plus loin, des libs comme **pydantic** font ça plus proprement, mais cette validation manuelle suffit largement pour un micro-service.

---

## 6. Variables d'environnement (.env)

Tu as déjà vu ça avec TMDB. Même principe :

```python
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
```

Et un `.env` à la racine :

```
API_TOKEN=ma-cle-super-longue-et-aleatoire
```

**Toujours dans .gitignore.** Toujours.

---

## 7. Structurer un vrai projet

```
mon_service/
├── app.py              ← Routes, c'est l'entree
├── logique.py          ← Tes fonctions metier (scoring, etc.)
├── requirements.txt
├── .env                ← /!\ jamais commit
├── .env.example
└── .gitignore
```

Quand `app.py` devient gros (>200 lignes), tu sors la logique dans un autre fichier :

```python
# logique.py
def calculer_score(lead):
    score = 0
    if lead.get("budget", 0) > 10000:
        score += 50
    return score
```

```python
# app.py
from logique import calculer_score

@app.route("/score", methods=["POST"])
def score():
    data = request.get_json()
    return jsonify({"score": calculer_score(data)})
```

---

## 8. Renvoyer les bons codes HTTP

| Code | Sens | Quand l'utiliser |
|---|---|---|
| 200 | OK | Tout s'est bien passé |
| 201 | Created | Création d'une ressource |
| 400 | Bad Request | Le client a envoyé des données invalides |
| 401 | Unauthorized | Token manquant ou faux |
| 404 | Not Found | La ressource demandée n'existe pas |
| 500 | Server Error | Bug côté serveur |

```python
return jsonify({"error": "champ manquant"}), 400
return jsonify({"score": 75}), 200       # 200 par defaut
```

---

## 9. Logger pour débugger

`print()` c'est bien pour démarrer, mais ça part dans le vide en prod.

Pour suivre ce que reçoit ton API :

```python
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

@app.route("/score", methods=["POST"])
def score():
    data = request.get_json()
    log.info("Score demande pour %s", data.get("nom"))
    # ...
```

Sur Render, ces logs apparaissent dans le dashboard. Tu peux relire l'historique de tous les appels.

---

## 10. Aller plus loin

- **CORS** : si tu appelles ton API depuis un navigateur (front), il faudra `flask-cors`
- **Rate limiting** : empêcher quelqu'un d'appeler 1000 fois par seconde — `flask-limiter`
- **Tests** : `pytest` + `app.test_client()` pour tester sans lancer le serveur
- **Base de données** : SQLAlchemy ou plus simple : Supabase (déjà au programme)

Pour ce cours on reste sur l'essentiel : un endpoint + token + déploiement.
