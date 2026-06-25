# 🧪 Mini-projet — Affiche-moi ça (~6h) · Niveau 🟢 accessible

> **Type d'IA : 🤖 LLM** (pour rédiger l'accroche et le slogan de l'affiche).
>
> **Prérequis :**
> - Copie `.env.example` → `.env` (la clé LLM de la formation est dans `cours_llm/.env`).
> - `pip install flask python-dotenv openai matplotlib`
> - Tu sais lancer `python app.py` en local sans erreur.
> - Exemples d'événements + palettes de couleurs fournis dans `data/evenements_exemple.json`.
>
> 🎒 C'est une **mini-presta freelance** : tu livres un truc qui tourne ET que tu sais expliquer au jury, ligne par ligne.

---

## 🧑‍💼 Le client / le contexte

Tu viens d'être contacté·e par **la MJC des Tilleuls**. Ils organisent des tas d'événements (concerts, ateliers, vide-greniers) mais leurs affiches sont bricolées dans Word, moches et chronophages. La bénévole qui s'en occupe en a marre. Elle veut un petit outil web où elle saisit *titre, date, lieu, ambiance*, choisit une couleur, et **récupère une affiche prête à imprimer** en 30 secondes. Elle te paie une journée pour lui livrer ça.

## 🎯 Le besoin

> « Je veux taper les infos de mon événement, choisir une ambiance, et **télécharger une jolie affiche** sans ouvrir un logiciel de graphisme. »

## 📦 Ce que tu livres

- Une appli **Flask** avec un formulaire de saisie d'événement.
- Une **accroche + un texte court** rédigés par l'IA à partir des infos.
- Une **affiche PNG** générée (titre, accroche, date, lieu) avec une **palette de couleurs** au choix.
- Un bouton **« Télécharger l'affiche »**.
- Un **README** d'installation + un `.env.example`.

---

## 🧱 Contraintes métier réelles

> Ce ne sont pas des caprices : c'est ce qui sépare un script de hackathon d'une presta livrable.

1. **Budget / temps** : ça tient en une journée ; **1 seul appel LLM** par affiche générée.
2. **Sécurité** : aucune clé dans le code → tout dans `.env` ; l'endpoint qui appelle l'IA est **protégé par token Bearer** ; les champs du formulaire sont **validés** (titre non vide, longueurs max) → **400** sinon.
3. **Données / RGPD** : pas de données personnelles ici (juste des infos d'événement public) — note-le, ça compte aussi de savoir le dire au jury.
4. **Robustesse** : si l'IA ne répond pas (timeout 10 s) ou renvoie un JSON cassé, l'affiche se génère quand même avec un texte de secours, sans planter.
5. **Lisible et imprimable** : l'affiche tient en **A4 portrait**, le titre ne déborde jamais (retour à la ligne automatique), contraste texte/fond suffisant.

---

## 🪜 Étapes guidées

> Commit après chaque étape (le jury veut un historique Git qui raconte ta progression).

### 1. Le squelette Flask (~30 min)
Crée `app.py` (port **6011**), charge `.env` et `data/evenements_exemple.json` (palettes + exemples), sers une page d'accueil avec le formulaire.
> 💡 Charge les palettes une fois au démarrage :
> ```python
> import json
> from pathlib import Path
> CONFIG = json.loads((Path(__file__).parent / "data" / "evenements_exemple.json").read_text(encoding="utf-8"))
> PALETTES = {p["nom"]: p for p in CONFIG["palettes"]}
> ```

### 2. Le formulaire (~45 min)
Champs : *titre, date, lieu, ambiance* (menu déroulant), *palette* (menu déroulant). Pense **accessibilité** : un `<label>` relié à chaque champ, navigation clavier, contrastes. Ajoute un bouton « Remplir avec un exemple » qui pioche dans `CONFIG["exemples"]`.
> ⚠️ Mets `required` et un `maxlength` sur les champs texte : un titre de 300 caractères casse la mise en page de l'affiche.

### 3. La couche intelligente : l'IA rédige les textes (~1h)
Crée `textes.py` : une fonction qui envoie les infos au LLM et récupère une **accroche** (1 phrase punchy) + un **slogan** court, en JSON.
> 💡 Client `openai` pointé sur le `.env`, **`temperature=0.7`** ici (on veut un peu de créativité, mais format JSON imposé) :
> ```python
> from openai import OpenAI
> client = OpenAI(base_url=os.getenv("LLM_BASE_URL"), api_key=os.getenv("LLM_API_KEY"))
> prompt = (f"Événement: {titre}, le {date}, à {lieu}, ambiance {ambiance}. "
>           'Donne une accroche courte et un slogan, en JSON: {"accroche": "...", "slogan": "..."}')
> resp = client.chat.completions.create(model=os.getenv("LLM_MODEL"),
>          messages=[{"role": "user", "content": prompt}], temperature=0.7, timeout=10)
> ```
> ⚠️ `try/except` autour du `json.loads` : si le JSON est cassé, mets une accroche de secours (ex. le titre lui-même).

### 4. Le composant métier : composer l'affiche (~1h30) — *le cœur, à savoir réexpliquer*
Crée `affiche.py` : une fonction `generer_affiche(infos, palette) -> bytes` qui dessine l'affiche avec matplotlib (format A4, fond de la palette, titre en gros, accroche, date + lieu en bas, slogan).
> 💡 Backend `Agg`, figure au ratio A4, texte centré, et **retour à la ligne automatique** du titre :
> ```python
> import matplotlib; matplotlib.use("Agg")
> import matplotlib.pyplot as plt, textwrap, io
> fig = plt.figure(figsize=(8.27, 11.69))            # A4 en pouces
> fig.patch.set_facecolor(palette["fond"])
> titre_wrap = "\n".join(textwrap.wrap(infos["titre"], width=18))
> fig.text(0.5, 0.7, titre_wrap, ha="center", color=palette["texte"], fontsize=42, weight="bold")
> # ... accroche, date, lieu, slogan ; puis :
> buf = io.BytesIO(); plt.savefig(buf, format="png", dpi=150); buf.seek(0); plt.close(fig)
> return buf.getvalue()
> ```

### 5. L'affichage + le téléchargement (~45 min)
Affiche un aperçu de l'affiche dans la page de résultat et propose un bouton de téléchargement.
> 💡 Sers l'image via `send_file(io.BytesIO(png_bytes), mimetype="image/png", as_attachment=True, download_name="affiche.png")`.

### 6. Sécuriser + valider (~45 min)
Protège l'endpoint qui appelle l'IA par un **décorateur `@require_token`** (token dans `.env`). Valide les champs reçus côté serveur → **400** si titre vide ou palette inconnue.
> 💡 Décorateur Bearer repris de `cours_microservice` (voir `2_auth_token.py`).

### 7. Finitions : README, `.env.example`, commits (~30 min)
README avec 2-3 **user stories** ("En tant que bénévole, je veux générer une affiche afin de gagner du temps"), procédure d'install, mot sur les choix RGAA. `.env.example` : `LLM_BASE_URL`, `LLM_API_KEY`, `LLM_MODEL`, `API_TOKEN`. `.gitignore` excluant `.env`.

---

## ✅ Critères de réussite (grille façon jury CDA)

- [ ] Je sais **expliquer `affiche.py`** ligne à ligne (mise en page, retour à la ligne, palette).
- [ ] Les champs sont **validés** ; une saisie invalide renvoie un **code 400** clair.
- [ ] **Aucun secret dans le code** : tout en `.env`, et `.env.example` est commité (pas `.env`).
- [ ] L'endpoint qui appelle l'IA est **protégé par token Bearer** (401 sans / mauvais token).
- [ ] **Historique Git** = commits petits et réguliers.
- [ ] Un **README** permet à un inconnu d'installer et lancer.
- [ ] L'interface est **responsive** et respecte les bases **RGAA** (labels reliés, contrastes, clavier).
- [ ] Je sais dire pourquoi il n'y a **pas d'enjeu RGPD** ici (aucune donnée personnelle).

---

## 🚀 Bonus (si tu finis en avance)

- Propose **2-3 mises en page** différentes (titre en haut / au centre / image de fond).
- Ajoute un **QR code** vers la billetterie (lib `qrcode`).
- Génère aussi une **version carrée** pour Instagram.
- Déploie sur **Render** (suis `cours_microservice/deploiement_render.md`).

---

## 🗺️ Compétences CDA mobilisées

| Compétence | Mobilisée ? | Où, concrètement, dans CE projet |
|---|:--:|---|
| C1 — Environnement (.venv/.env/Git) | ✓ | `.env.example`, `.gitignore`, commits par étape |
| C2 — Interfaces (responsive/RGAA) | ✓ | Formulaire accessible + page d'aperçu de l'affiche |
| C3 — Composants métier 🟥 | ~ | `affiche.py` (composition/mise en page) + validation des entrées + Bearer |
| C4 — Gestion de projet | ✓ | User stories en tête du README + historique Git |
| C5 — Analyse & maquettage | ✓ | Besoin de la MJC → maquette de l'affiche (croquis A4) avant de coder |
| C6 — Architecture multicouche | ~ | Séparation `app.py` / `textes.py` (IA) / `affiche.py` (rendu) |
| C7 — Base relationnelle (MCD/MLD) | — | Pas de base de données ici |
| C8 — Accès SQL + NoSQL 🟥 | — | Pas d'accès données ici (voir `factures-en-clair`) |
| C9 — Plans de tests | — | En bonus seulement |
| C10 — Doc de déploiement | — | En bonus seulement (Render) |
| C11 — Mise en prod DevOps | — | En bonus seulement |
| 🔒 Transversal (ANSSI/RGPD/RGAA/B1) | ✓ | Secrets en `.env`, validation, RGAA dès la maquette, savoir dire « pas de données perso », doc matplotlib lue en anglais |
