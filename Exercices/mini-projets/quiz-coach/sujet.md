# 🧪 Mini-projet — Quiz-coach (~6h) · Niveau 🟢 accessible

> **Type d'IA : 🤖 LLM** (juste pour *rédiger* les conseils ; le profil, lui, est calculé par ton code).
>
> **Prérequis :**
> - Copie `.env.example` → `.env` (la clé LLM de la formation est dans `cours_llm/.env`).
> - `pip install flask python-dotenv openai matplotlib`
> - Tu sais lancer `python app.py` en local sans erreur.
> - Les questions de départ sont fournies dans `data/questions.json`.
>
> 🎒 C'est une **mini-presta freelance** : tu livres un truc qui tourne ET que tu sais expliquer au jury, ligne par ligne.

---

## 🧑‍💼 Le client / le contexte

Tu viens d'être contacté·e par **Léa, coach en organisation et gestion du temps**. Elle a un site vitrine mais personne ne la contacte : les visiteurs lisent et repartent. Elle a vu passer des « quiz de personnalité » qui cartonnent et elle veut le sien : un **quiz-diagnostic** rigolo qui dit au visiteur *quel·le organisateur·rice il/elle est*, lui donne **3 conseils sur mesure**, et au passage lui propose de **laisser son email** pour recevoir un guide. Elle te paie une journée pour lui livrer un truc qui tourne et qu'elle pourra mettre sur son site.

## 🎯 Le besoin

> « Je veux un quiz de 8 questions qui sort un **profil visuel** et des **conseils personnalisés** à la fin, et qui me ramène des contacts qualifiés sans que j'aie à lever le petit doigt. »

## 📦 Ce que tu livres

- Une appli **Flask** avec un quiz web (1 page de questions → 1 page de résultat).
- Un **profil sur 4 axes** affiché en **radar chart** (Organisation, Concentration, Énergie, Motivation).
- **3 conseils personnalisés** rédigés par l'IA à partir du profil.
- Une **capture d'email optionnelle** (avec consentement) en fin de quiz.
- Un **README** d'installation + un `.env.example`.

---

## 🧱 Contraintes métier réelles

> Ce ne sont pas des caprices : c'est ce qui sépare un script de hackathon d'une presta livrable.

1. **Budget / temps** : ça tient en une journée ; **1 seul appel LLM** par résultat de quiz (Léa paie l'API, pas question de la cramer).
2. **Sécurité** : aucune clé dans le code → tout dans `.env` ; l'endpoint qui appelle l'IA est **protégé par token Bearer** ; les réponses reçues sont **validées** (sinon code 400).
3. **RGPD** : l'email est **optionnel**, avec une **case de consentement** cochée explicitement, et tu ne stockes **que l'email + la date** (rien d'autre). Une ligne de mention « tes données ne servent qu'à t'envoyer le guide ».
4. **Robustesse** : si l'IA renvoie un JSON cassé ou ne répond pas (timeout 10 s), l'appli affiche quand même le profil + un conseil de secours, sans planter.
5. **Le profil ne ment pas** : le calcul du profil est fait par **ton code à toi** (pas par l'IA). L'IA ne fait que *rédiger* les conseils à partir du profil que TU as calculé.

---

## 🪜 Étapes guidées

> Commit après chaque étape (le jury veut un historique Git qui raconte ta progression).

### 1. Le squelette Flask (~30 min)
Crée `app.py` (port **6010**), charge `.env`, sers une page d'accueil qui lit `data/questions.json` et affiche les 8 questions dans un `<form>`.
> 💡 Charge les questions une fois au démarrage :
> ```python
> import json
> from pathlib import Path
> QUESTIONS = json.loads((Path(__file__).parent / "data" / "questions.json").read_text(encoding="utf-8"))
> ```

### 2. Le formulaire du quiz (~45 min)
Pour chaque question, propose ses options en boutons radio. Pense **accessibilité** dès maintenant : un `<label>` relié à chaque `input`, navigation possible au clavier, contrastes lisibles.
> 💡 Un groupe de réponses par question : `name="q1"`, `value="a"`. Au submit, tu récupères tout d'un coup avec `request.form`.
> ⚠️ Mets un `required` sur chaque groupe : un quiz à moitié rempli fausse le profil.

### 3. Le composant métier : calculer le profil (~1h) — *le cœur, à savoir réexpliquer*
Crée un module séparé `scoring.py` avec une fonction `calculer_profil(reponses: dict) -> dict`. Elle :
1. additionne les `points` de chaque option choisie, axe par axe ;
2. ramène chaque axe sur **100** (sur la base du `max_par_axe` du barème) ;
3. trouve l'**axe dominant** → renvoie le **profil** correspondant (`bareme.profils`), ou `equilibre` en cas d'égalité.
> 💡 Le squelette à compléter :
> ```python
> def calculer_profil(reponses, questions):
>     scores = {axe: 0 for axe in questions["axes"]}
>     for q in questions["questions"]:
>         choix = reponses.get(q["id"])          # ex: "a"
>         option = next((o for o in q["options"] if o["id"] == choix), None)
>         if option is None:
>             continue
>         for axe, pts in option["points"].items():
>             scores[axe] += pts
>     # ... normaliser sur 100, trouver l'axe dominant, renvoyer le profil
>     return {"scores": scores_sur_100, "axe_dominant": axe, "profil": profil}
> ```
> ⚠️ C'est CETTE fonction que le jury te demandera de dérouler ligne à ligne. Pas d'IA ici : du code clair que tu maîtrises. Bonus malin : un `test_scoring.py` qui vérifie qu'un jeu de réponses « tout organisation » sort bien *L'Architecte*.

### 4. La couche intelligente : les conseils par l'IA (~1h)
Crée `conseils.py` : une fonction qui reçoit le profil + les scores et demande au LLM **3 conseils personnalisés** au format JSON.
> 💡 Client `openai` pointé sur le `.env`, **`temperature=0`** pour du JSON stable :
> ```python
> from openai import OpenAI
> client = OpenAI(base_url=os.getenv("LLM_BASE_URL"), api_key=os.getenv("LLM_API_KEY"))
> prompt = f"Profil: {profil['nom']} ({profil['punchline']}). Scores: {scores}. " \
>          "Donne 3 conseils concrets et bienveillants pour cette personne, en JSON: " \
>          '{"conseils": ["...", "...", "..."]}'
> resp = client.chat.completions.create(model=os.getenv("LLM_MODEL"),
>          messages=[{"role": "user", "content": prompt}], temperature=0, timeout=10)
> ```
> ⚠️ Entoure le `json.loads(...)` d'un `try/except` : si l'IA bave un JSON cassé, renvoie un conseil de secours au lieu de planter (contrainte n°4).

### 5. La page de résultat + le radar (~1h)
Génère le **radar chart** des 4 axes en PNG (matplotlib projection polaire, backend `Agg`) et affiche-le avec le profil et les 3 conseils.
> 💡 Sers l'image via un endpoint, comme dans `cours_dataviz` (exo 5) :
> ```python
> import matplotlib
> matplotlib.use("Agg")           # AVANT d'importer pyplot
> import matplotlib.pyplot as plt
> import io
> from flask import send_file
> # radar : axes = angles régulièrement répartis sur 2*pi, on referme la boucle,
> # ax = plt.subplot(polar=True); ax.plot(angles, valeurs); ax.fill(...)
> buf = io.BytesIO(); plt.savefig(buf, format="png", dpi=150); buf.seek(0); plt.close()
> return send_file(buf, mimetype="image/png")
> ```

### 6. Sécuriser + valider + RGPD (~45 min)
Protège l'endpoint qui parle à l'IA par un **décorateur `@require_token`** (token dans `.env`). Valide les réponses reçues (les 8 questions présentes, des `id` d'option connus) → **400** sinon. Ajoute la **case de consentement** + le stockage minimal de l'email.
> 💡 Décorateur Bearer (repris de `cours_microservice`) :
> ```python
> from functools import wraps
> def require_token(view):
>     @wraps(view)
>     def wrapper(*a, **k):
>         h = request.headers.get("Authorization", "")
>         if h.removeprefix("Bearer ").strip() != os.getenv("API_TOKEN"):
>             return jsonify({"error": "invalid token"}), 401
>         return view(*a, **k)
>     return wrapper
> ```
> 💡 Email : `if request.form.get("consent") == "on": ...` puis append `{"email": ..., "date": ...}` dans un fichier `leads.json`. **Pas de consentement = on ne stocke rien.**

### 7. Finitions : README, `.env.example`, commits (~30 min)
README avec 2-3 **user stories** ("En tant que visiteur, je veux connaître mon profil afin de…"), la procédure d'install, et un mot sur les choix RGAA/RGPD. `.env.example` listant `LLM_BASE_URL`, `LLM_API_KEY`, `LLM_MODEL`, `API_TOKEN`. `.gitignore` excluant `.env` et `leads.json`.

---

## ✅ Critères de réussite (grille façon jury CDA)

- [ ] Je sais **expliquer `scoring.py`** ligne à ligne (c'est moi qui calcule le profil, pas l'IA).
- [ ] Les réponses sont **validées** ; un envoi incomplet ou trafiqué renvoie un **code 400** clair.
- [ ] **Aucun secret dans le code** : tout en `.env`, et `.env.example` est commité (pas `.env`).
- [ ] L'endpoint qui appelle l'IA est **protégé par token Bearer** (401 sans / mauvais token).
- [ ] **Historique Git** = commits petits et réguliers qui suivent les 7 étapes.
- [ ] Un **README** permet à un inconnu d'installer et lancer le quiz.
- [ ] L'interface est **responsive** et respecte les bases **RGAA** (labels reliés, contrastes, navigation clavier).
- [ ] **RGPD** : email optionnel + consentement explicite + données minimisées (email + date seulement).
- [ ] Je peux citer **où chaque compétence CDA** est mobilisée (tableau ci-dessous).

---

## 🚀 Bonus (si tu finis en avance)

- Écris `test_scoring.py` (`pytest`) : un jeu de réponses « tout organisation » doit sortir *L'Architecte* (compétence C9).
- Ajoute un **2e visuel** : une jauge ou des barres en complément du radar.
- Déploie sur **Render** (suis `cours_microservice/deploiement_render.md`).
- Branche la capture d'email sur un **webhook n8n** pour ajouter le contact dans le CRM de Léa.

---

## 🗺️ Compétences CDA mobilisées

| Compétence | Mobilisée ? | Où, concrètement, dans CE projet |
|---|:--:|---|
| C1 — Environnement (.venv/.env/Git) | ✓ | `.env.example`, `.gitignore` (exclut `.env`/`leads.json`), commits par étape |
| C2 — Interfaces (responsive/RGAA) | ✓ | Formulaire quiz : labels reliés, contrastes, clavier, page résultat lisible mobile |
| C3 — Composants métier 🟥 | ✓ | `scoring.py` (calcul des axes + profil), endpoint validé + Bearer + codes 200/400/401 |
| C4 — Gestion de projet | ✓ | 2-3 user stories en tête du README + historique Git régulier |
| C5 — Analyse & maquettage | ✓ | Besoin de Léa traduit en parcours quiz → résultat ; croquis des 2 écrans avant de coder |
| C6 — Architecture multicouche | ~ | Séparation `app.py` (orchestration) / `scoring.py` (métier) / `data/` (données) |
| C7 — Base relationnelle (MCD/MLD) | — | Pas de base relationnelle ici (voir `factures-en-clair`) |
| C8 — Accès SQL + NoSQL 🟥 | ~ | Volet NoSQL léger : stockage des leads en JSON (`leads.json`) |
| C9 — Plans de tests | ~ | En bonus : `test_scoring.py` (pytest sur le composant métier) |
| C10 — Doc de déploiement | — | En bonus seulement (Render) |
| C11 — Mise en prod DevOps | — | En bonus seulement (webhook n8n / CI) |
| 🔒 Transversal (ANSSI/RGPD/RGAA/B1) | ✓ | Secrets en `.env`, validation des entrées, consentement RGPD, RGAA dès la maquette, doc matplotlib lue en anglais |
