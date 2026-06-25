# 🚀 Mini-projet — En ligne sans tout casser (~½ journée) · Niveau 🟠 intermédiaire

> **Type d'IA : 🧮 aucune** — c'est un projet **DevOps** : tu prends une API **déjà écrite** et tu la
> **mets en production proprement**. Ici on ne code (presque) pas de métier : on prouve qu'on sait
> **déployer** (C10) et **automatiser la livraison** (C11) — les deux compétences absentes des autres projets.
>
> **Prérequis :**
> - Un compte **GitHub** et un compte **Render** (gratuits).
> - `pip install -r app/requirements.txt` (Flask, gunicorn, python-dotenv, pytest).
> - L'app à déployer est fournie dans **`app/`** (reprise du micro-exercice 04/09 : le Bureau de recrutement de héros).
>
> 🎒 C'est une **mini-presta freelance** : « tu m'as codé l'API, maintenant **mets-la en ligne** et fais que je puisse la mettre à jour sans rien casser. »
> 🟨 **C'est LE projet du bloc BC03** : tests → documentation de déploiement → CI/CD.

---

## 🧑‍💼 Le client / le contexte

La **Ligue des Héros** a déjà ton API de recrutement qui tourne sur ton portable. Problème : elle
n'est accessible **que** chez toi, et à chaque correction tu redéploies à la main en croisant les doigts.
La cliente veut **une URL publique** qui marche, et surtout la **garantie** qu'une modif buggée
n'arrive **jamais** en ligne sans avoir été testée.

## 🎯 Le besoin

> « Mets mon API en ligne avec une vraie adresse, écris-moi la notice pour que n'importe qui puisse
> la redéployer, et fais en sorte qu'un `git push` qui casse les tests **n'atteigne pas** la production. »

## 📦 Ce que tu livres

- Une **doc de déploiement** (`DEPLOIEMENT.md`) qu'un inconnu peut suivre seul → **C10**.
- Un **`render.yaml`** (Infrastructure as Code) + le service Render qui tourne → **C11 (CD)**.
- Un **workflow GitHub Actions** (`.github/workflows/tests.yml`) qui lance `pytest` à chaque push → **C11 (CI)**.
- Un **tableau de plan de tests** (`PLAN_DE_TESTS.md`) en plus du `pytest` → **C9**.
- Un **README** qui pointe l'URL publique + la procédure.

> 📁 Un corrigé de référence de **tous** ces livrables est dans **`corrige/`** — à n'ouvrir
> **qu'après** avoir tenté (sinon tu ne sauras pas le défendre au jury).

---

## 🧱 Contraintes métier réelles

> Ce sont les réflexes qui séparent un « ça marche sur mon PC » d'une mise en prod défendable.

1. **Secret hors du code** : `API_TOKEN` vit dans une **variable d'environnement** (local : `.env` ignoré par Git ; prod : dashboard Render). Jamais dans le repo.
2. **Pas de serveur de dev en prod** : on lance avec **`gunicorn`**, pas `flask run`. Le port vient de `$PORT`.
3. **Debug coupé en prod** : `FLASK_DEBUG=false` (sinon une erreur expose la stack au public).
4. **CI avant CD** : les tests tournent dans un **pipeline** (GitHub Actions) ; Render ne déploie que du code parti depuis `main`.
5. **Réversible** : tu sais faire un **rollback** (Render *Deploys* ou `git revert`).

---

## 🪜 Étapes guidées

> Commit après chaque étape : le jury veut voir ta progression.

### 1. Faire tourner l'app en local (~20 min)
```bash
cd app
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
pytest -v          # 10 tests, tout vert
python app.py      # http://localhost:5004/health -> {"status":"ok"}
```

### 2. Le plan de tests 🟥 (~30 min) — *C9*
Rédige `PLAN_DE_TESTS.md` : un **tableau** (cas / données / attendu / obtenu / statut) qui décrit
les 7 cas automatisés (santé, token OK/KO, 400, bornes des rangs) **+** les cas manuels à vérifier une
fois en ligne. C'est ce tableau, et pas « j'ai cliqué », que le jury attend.

### 3. La notice de déploiement (~1h) — *C10*
Écris `DEPLOIEMENT.md` **pour un inconnu** : prérequis, push GitHub, création du service Render
(build `pip install -r requirements.txt`, start `gunicorn app:app --bind 0.0.0.0:$PORT`, health check
`/health`), variables d'environnement, test en ligne, **rollback**, **checklist pré-prod**.
> 💡 Inspire-toi de `cours_microservice/deploiement_render.md`, mais adapte à CETTE app (endpoints, token).

### 4. L'Infrastructure as Code (~30 min) — *C11 (CD)*
Crée `render.yaml` à la racine : il décrit le service (runtime, build, start, health check, variables).
Versionné, il rend le déploiement **reproductible** au lieu de cliquer dans l'UI.

### 5. La CI GitHub Actions 🟥 (~45 min) — *C11 (CI)*
Crée `.github/workflows/tests.yml` : à chaque `push`/`pull_request`, GitHub installe les dépendances et
lance `pytest`. **C'est le maillon qui fait la démarche DevOps.**
> ⚠️ **Le piège du jury** : « Render qui redéploie tout seul, c'est du DevOps ? » → **NON**, c'est du **CD** seulement.
> Tant qu'aucun **pipeline ne teste** avant de livrer, le maillon **qualité (CI)** manque. Sache l'expliquer.

### 6. Déployer pour de vrai + finitions (~45 min)
Pousse sur GitHub, crée le service Render, vérifie l'URL publique, déroule la **checklist pré-prod**.
Note l'URL dans le `README`. Fais **un** rollback pour prouver que tu sais revenir en arrière.

---

## ✅ Critères de réussite (grille façon jury CDA)

- [ ] Mon API répond sur une **URL publique** (`/health` = `200` en ligne).
- [ ] `POST /recrue` **sans token** répond `401` **en ligne** (la sécurité tient en prod).
- [ ] Mon `API_TOKEN` est **introuvable** dans le repo GitHub (uniquement dans Render).
- [ ] `FLASK_DEBUG=false` en production, lancement via **`gunicorn`**.
- [ ] Ma **CI** GitHub Actions passe au **vert** et **bloque** un push qui casse les tests.
- [ ] Je sais expliquer **CI vs CD** et pourquoi « Render seul ≠ DevOps ».
- [ ] Ma `DEPLOIEMENT.md` est suivie **par un inconnu** sans question (teste-la sur un·e camarade).
- [ ] J'ai un **plan de tests** (tableau) **et** des tests `pytest`.
- [ ] Je sais faire un **rollback**.

---

## 🚀 Bonus (si tu finis en avance)

- Ajoute un **badge** de statut CI dans le `README` (`![tests](.../tests.yml/badge.svg)`).
- Ajoute un **environnement de staging** : 2ᵉ service Render branché sur une branche `staging`.
- Ajoute `pytest --cov=app` dans la CI et **échoue** sous un seuil de couverture (ex. 80 %).
- Ajoute une étape **lint** (`ruff` ou `flake8`) au workflow avant les tests.
- Ajoute un **`/metrics`** simple (nombre de recrues) pour parler **monitoring**.

---

## 🗺️ Compétences CDA mobilisées

| Compétence | Mobilisée ? | Où, concrètement, dans CE projet |
|---|:--:|---|
| C1 — Environnement (.venv/.env/Git) | ✓ | `.env.example`, `.gitignore` (exclut `.env`), secrets en variables d'env |
| C2 — Interfaces (responsive/RGAA) | ~ | Page d'accueil (labels reliés, `aria-live`) — accessoire ici |
| C3 — Composants métier 🟥 | ~ | L'app (token, validation, codes HTTP) est **fournie** ; tu la déploies |
| C4 — Gestion de projet | ✓ | Commits par étape, README, branches (staging en bonus) |
| C5 — Analyse & maquettage | — | Hors périmètre |
| C6 — Architecture multicouche | ~ | Schéma du flux `push → CI → CD → prod` |
| C7 — Base relationnelle | — | Hors périmètre |
| C8 — Accès SQL + NoSQL 🟥 | — | Hors périmètre |
| **C9 — Plans de tests** | ✓ | `PLAN_DE_TESTS.md` (tableau) + `pytest` rejoué par la CI |
| **C10 — Doc de déploiement** | ✓ | `DEPLOIEMENT.md` pas-à-pas + checklist pré-prod + rollback |
| **C11 — Mise en prod DevOps** | ✓ | `render.yaml` (CD) **+** GitHub Actions (CI) ; CI **avant** CD |
| 🔒 Transversal (ANSSI/RGPD/RGAA/B1) | ✓ | Secret hors du code, `FLASK_DEBUG=false`, `401` en ligne, doc Render/Actions lue en anglais |
