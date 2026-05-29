# 🚀 Déployer son micro-service sur Render (gratuit, 10 min)

Render héberge gratuitement des petits services Python. Ton API sera accessible publiquement avec une URL `https://ton-service.onrender.com`.

> ℹ️ Le plan gratuit "endort" ton service après 15 min sans activité. Le premier appel après une période d'inactivité prend ~30 secondes (réveil). Pour un usage perso ou démo c'est OK ; pour de la prod, prends le plan payant (~7$/mois) ou Railway.

---

## 1. Préparer le projet

À la racine de `cours_microservice/`, vérifie que tu as :

- ✅ `app.py` (avec `if __name__ == "__main__": ...` qui lit `PORT` depuis env)
- ✅ `requirements.txt` (avec `flask`, `gunicorn`, `python-dotenv`)
- ✅ `.gitignore` qui exclut `.env`, `.venv`, `__pycache__`

Si pas de `.gitignore`, crée-le :

```
.env
.venv/
__pycache__/
*.pyc
```

---

## 2. Pousser sur GitHub

```bash
git init
git add .
git commit -m "Initial commit"

# Cree un repo sur github.com puis :
git remote add origin https://github.com/TON-USER/mon-service.git
git branch -M main
git push -u origin main
```

---

## 3. Créer le service sur Render

1. Va sur [https://render.com](https://render.com), inscris-toi avec ton GitHub
2. Clique **New** → **Web Service**
3. Connecte ton repo GitHub
4. Configure :

| Champ | Valeur |
|---|---|
| **Name** | `mon-service` (ce sera dans l'URL) |
| **Region** | Frankfurt (proche de la France) |
| **Branch** | `main` |
| **Runtime** | Python 3 |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app` |
| **Instance Type** | Free |

5. **Environment Variables** : clique "Add Environment Variable"
   - `API_TOKEN` = `un-token-long-et-aleatoire-ici`
   - `FLASK_DEBUG` = `false`

6. Clique **Create Web Service**

Attends 2-3 minutes. Tu verras dans les logs :

```
==> Build successful
==> Starting service with 'gunicorn app:app'
==> Your service is live at https://mon-service.onrender.com
```

---

## 4. Tester en ligne

```bash
# Healthcheck (pas d'auth)
curl https://mon-service.onrender.com/health

# Endpoint protege
curl -X POST https://mon-service.onrender.com/api/lead/score \
  -H "Authorization: Bearer TON_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"nom": "Test", "email": "test@example.com", "budget": 5000}'
```

---

## 5. Mettre à jour le service

Chaque fois que tu fais `git push`, Render redéploie automatiquement. Tu peux suivre le déploiement dans l'onglet **Logs**.

---

## 6. Alternatives à Render

| Service | Avantage | Limite gratuite |
|---|---|---|
| **Render** | UI simple, Python natif | 750h/mois, s'endort |
| **Railway** | Plus moderne, plus rapide | 5$ de crédit / mois |
| **Fly.io** | Plus puissant, edge | 3 VMs gratuites |
| **PythonAnywhere** | Spécialisé Python | 1 app web gratuite |

Pour un premier projet, **Render** est le plus simple.

---

## 7. Checklist sécurité avant prod

- [ ] `FLASK_DEBUG=false` en prod
- [ ] `API_TOKEN` jamais dans le code, uniquement en variable d'env
- [ ] `.env` dans `.gitignore` (NE JAMAIS COMMITER)
- [ ] Si tu retires un token, redéploie immédiatement
- [ ] Logger les tentatives d'auth échouées (déjà fait dans `app.py`)
