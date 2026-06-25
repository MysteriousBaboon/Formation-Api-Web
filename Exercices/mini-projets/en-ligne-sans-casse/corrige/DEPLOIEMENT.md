# 🚀 Documentation de déploiement — API Bureau de recrutement de héros

> **Compétence C10.** Critère de réussite : **un·e collègue qui ne connaît pas le projet
> doit pouvoir le redéployer avec CE document seul**, sans rien te demander.
> Hébergeur : **Render** (plan gratuit). Source de référence : [`../../../../cours_microservice/deploiement_render.md`](../../../../cours_microservice/deploiement_render.md).

## 0. Prérequis

- Un compte **GitHub** et un compte **Render** (inscription gratuite via GitHub).
- Le code de l'app : `app.py`, `requirements.txt`, `templates/`, `test_app.py`.
- `requirements.txt` contient bien **`gunicorn`** (serveur de production).

## 1. Préparer le projet (local)

```bash
python -m venv .venv
source .venv/bin/activate        # Windows : .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # remplis API_TOKEN
pytest -v                        # tout doit être vert AVANT de déployer
python app.py                    # vérifie http://localhost:5004/health
```

Vérifie que `.gitignore` exclut bien `.env` (le secret ne doit **jamais** partir sur GitHub).

## 2. Pousser sur GitHub

```bash
git init
git add .
git commit -m "API héros prête à déployer"
git remote add origin https://github.com/<TON-USER>/bureau-heros.git
git branch -M main
git push -u origin main
```

## 3. Créer le service sur Render

| Champ | Valeur |
|---|---|
| Type | **Web Service** |
| Repository | ton repo GitHub `bureau-heros` |
| Region | **Frankfurt** |
| Branch | `main` |
| Runtime | **Python 3** |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn app:app --bind 0.0.0.0:$PORT` |
| Instance Type | **Free** |
| Health Check Path | `/health` |

> 💡 Tu peux aussi laisser Render lire le fichier **`render.yaml`** (Infrastructure as Code) :
> il décrit tout ce tableau automatiquement.

### Variables d'environnement (onglet *Environment*)

| Clé | Valeur | Note |
|---|---|---|
| `API_TOKEN` | une chaîne **longue et aléatoire** | le secret — **jamais** dans le code |
| `FLASK_DEBUG` | `false` | obligatoire en prod |

Render fournit `PORT` automatiquement : **ne pas** le définir à la main.

Clique **Create Web Service**, attends 2-3 min. Les logs affichent :
```
==> Build successful
==> Starting service with 'gunicorn app:app --bind 0.0.0.0:$PORT'
==> Your service is live at https://bureau-heros.onrender.com
```

## 4. Tester en ligne

```bash
# Santé (pas d'auth)
curl https://bureau-heros.onrender.com/health
# -> {"status":"ok"}

# Sans token -> doit refuser
curl -X POST https://bureau-heros.onrender.com/recrue
# -> 401

# Avec le vrai token
curl -X POST https://bureau-heros.onrender.com/recrue \
  -H "Authorization: Bearer <TON_API_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"nom":"Comète","pouvoir":"Vol","niveau":88}'
# -> 200 + badge
```

## 5. Mises à jour

Chaque `git push` sur `main` déclenche un **redéploiement automatique** (CD). Suis-le dans
l'onglet **Logs** de Render. Couplé à la CI (voir [`.github/workflows/tests.yml`](.github/workflows/tests.yml)),
un push qui casse les tests est **bloqué avant** d'atteindre la prod.

## 6. Rollback (revenir en arrière)

- **Via Render** : onglet *Deploys* → choisir un déploiement précédent → **Rollback**.
- **Via Git** : `git revert <commit>` puis `git push` → Render redéploie la version corrigée.

## ✅ Checklist avant prod (pré-prod)

- [ ] `pytest -v` est **vert** en local **et** dans la CI GitHub Actions.
- [ ] `FLASK_DEBUG=false` côté Render.
- [ ] `API_TOKEN` présent dans Render, **absent** du repo (`.env` dans `.gitignore`).
- [ ] `/health` répond `200` en ligne.
- [ ] `POST /recrue` **sans** token répond `401` en ligne.
- [ ] L'URL publique est notée dans le `README`.
- [ ] Je sais faire un **rollback** (testé au moins une fois).

## 🌍 Environnements

| Environnement | Où | Token | Debug |
|---|---|---|---|
| **dev** | `python app.py` en local | `.env` local | `true` possible |
| **prod** | Render (`gunicorn`) | variable Render | `false` |

> *(staging facultatif : un 2ᵉ service Render branché sur une branche `staging`.)*
