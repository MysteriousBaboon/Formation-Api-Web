# 🧪 Mini-projet — Thermomètre des avis (~6h) · Niveau 🟠 intermédiaire

> **Type d'IA : 📊 Machine Learning classique (scikit-learn)** — pas de LLM ici, tu entraînes ton propre modèle.
>
> **Prérequis :**
> - `pip install flask python-dotenv pandas scikit-learn matplotlib`
> - Tu as fait `cours_machine_learning` (entraînement, train/test, accuracy, matrice de confusion).
> - Tu sais lancer `python app.py` en local sans erreur.
> - 35 avis clients fictifs (avec note) sont fournis dans `data/avis_exemple.csv`.
>
> 🎒 C'est une **mini-presta freelance** : tu livres un truc qui tourne ET que tu sais expliquer au jury, ligne par ligne.

---

## 🧑‍💼 Le client / le contexte

Tu viens d'être contacté·e par **le patron d'un food truck**, « Le Gras Double ». Il reçoit des avis avec une note (Google, son site) mais aussi des **retours sans note** : messages sur les réseaux, mots glissés dans la boîte à idées du camion. Il aimerait un outil qui **apprend** à reconnaître un avis content d'un avis fâché, pour pouvoir **classer même les retours sans note**, et savoir **sur quoi** les gens râlent ou kiffent. Il te paie une journée.

## 🎯 Le besoin

> « Apprends à mon outil à reconnaître un bon d'un mauvais retour, et dis-moi sur QUOI ça coince, sans que je lise tout. »

## 📦 Ce que tu livres

- Un **modèle de classification** (scikit-learn) entraîné sur les avis notés, avec son **score d'évaluation**.
- Un **tableau de bord** : jauge de satisfaction, **barres par thème** (accueil, qualité, prix, attente, hygiène…), top verbatims.
- La capacité de **classer un nouvel avis sans note**.
- Les analyses **stockées en JSON** (on ne réentraîne pas à chaque rechargement).
- Un **README** d'installation + un `.env.example`.

---

## 🧱 Contraintes métier réelles

> Ce ne sont pas des caprices : c'est ce qui sépare un script de hackathon d'une presta livrable.

1. **Budget / temps** : ça tient en une journée ; le modèle tourne **en local** (aucune API payante).
2. **Sécurité** : secrets éventuels dans `.env` ; l'endpoint d'analyse est **protégé par token Bearer** ; le CSV reçu est **validé** (colonnes attendues) → **400** sinon.
3. **Données / RGPD** : un avis peut contenir un prénom → tu **n'affiches pas** d'info personnelle, tu ne stockes que texte + note + sentiment + thème.
4. **Honnêteté du modèle** : tu **évalues** ton modèle (accuracy + matrice de confusion) et tu sais dire ce qu'il vaut. Sur 35 avis, c'est une démo — pas un modèle de prod, et tu l'assumes.
5. **Reproductible** : `random_state` fixé pour que ton train/test soit rejouable.

---

## 🪜 Étapes guidées

> Commit après chaque étape (le jury veut un historique Git qui raconte ta progression).

### 1. Le squelette + les données (~30 min)
Crée `app.py` (port **6013**), lis `data/avis_exemple.csv` avec pandas.
> 💡 `df = pd.read_csv("data/avis_exemple.csv")` — colonnes : `id, date, note, texte`.

### 2. Préparer les données : créer les étiquettes (~45 min)
À partir de la **note**, fabrique l'étiquette de sentiment, puis sépare train/test (repris de `cours_machine_learning`).
> 💡 :
> ```python
> from sklearn.model_selection import train_test_split
> df["sentiment"] = df["note"].apply(lambda n: "positif" if n >= 4 else ("négatif" if n <= 2 else "neutre"))
> X_train, X_test, y_train, y_test = train_test_split(
>     df["texte"], df["sentiment"], test_size=0.3, random_state=0)
> ```

### 3. Le composant métier : entraîner le modèle (~1h) — *le cœur, à savoir réexpliquer*
Crée `modele.py` : transforme le texte en chiffres (**TF-IDF**) et entraîne un classifieur. Encapsule le tout dans un `Pipeline`.
> 💡 :
> ```python
> from sklearn.feature_extraction.text import TfidfVectorizer
> from sklearn.linear_model import LogisticRegression
> from sklearn.pipeline import make_pipeline
> modele = make_pipeline(TfidfVectorizer(), LogisticRegression(max_iter=1000))
> modele.fit(X_train, y_train)
> ```
> ⚠️ Le jury va demander : *« TF-IDF, ça fait quoi ? »* → ça transforme un texte en vecteur de poids de mots (mots rares et fréquents pondérés). Sache l'expliquer avec tes mots.

### 4. Évaluer le modèle (~45 min)
Mesure l'**accuracy** sur le test et trace la **matrice de confusion** (matplotlib `Agg`). Garde ce chiffre : c'est ta preuve que tu sais ce que vaut ton modèle.
> 💡 :
> ```python
> from sklearn.metrics import accuracy_score, confusion_matrix
> pred = modele.predict(X_test)
> print("Accuracy :", accuracy_score(y_test, pred))
> ```

### 5. Classer + agréger : le tableau de bord (~1h15)
Crée `analyse.py` : utilise le modèle pour classer **tous** les avis (et un nouvel avis sans note), détecte le **thème** par mots-clés, puis calcule la **satisfaction** et le **comptage par thème**, et sélectionne 2-3 verbatims marquants.
> 💡 Le thème par mots-clés (simple et explicable, pas d'IA) :
> ```python
> THEMES = {"attente": ["attente", "file", "long", "minutes"],
>           "prix": ["cher", "prix", "euros", "tarif"],
>           "hygiène": ["sale", "hygiène", "cheveu", "propre"],
>           "accueil": ["accueil", "sympa", "sourire", "aimable"]}
> ```

### 6. Stocker (NoSQL) + servir + sécuriser (~1h)
Sauve les analyses dans `analyses.json` (volet **NoSQL**, sert de cache). Affiche la **jauge** + les **barres par thème** + verbatims. Expose `POST /api/analyser` (Bearer) qui (re)lance l'analyse ; valide les colonnes du CSV → **400** sinon.
> 💡 Décorateur `@require_token` repris de `cours_microservice`.

### 7. Finitions : README, `.env.example`, commits (~30 min)
README (user stories + install + **le score de ton modèle** + note RGPD). `.env.example` : `API_TOKEN`. `.gitignore` excluant `.env` et `analyses.json`.

---

## ✅ Critères de réussite (grille façon jury CDA)

- [ ] Je sais **expliquer mon pipeline ML** (TF-IDF → classifieur) et **donner l'accuracy** de mon modèle.
- [ ] J'ai une **matrice de confusion** et je sais la lire.
- [ ] Mon modèle classe un **nouvel avis sans note**.
- [ ] Le CSV reçu est **validé** ; des colonnes manquantes renvoient un **code 400**.
- [ ] `/api/analyser` est **protégé par token Bearer** (401 sans / mauvais token).
- [ ] **RGPD** : pas d'info personnelle affichée, données minimisées.
- [ ] **Historique Git** + **README** réutilisable par un inconnu.

---

## 🚀 Bonus (si tu finis en avance)

- Remplace le classifieur par un **petit réseau de neurones** (`MLPClassifier`, cf. `cours_deep_learning`) et compare l'accuracy.
- **Persiste** le modèle entraîné avec `joblib` (on ne réentraîne plus au démarrage).
- Fais **évoluer la satisfaction dans le temps** (courbe par semaine).
- Range les avis dans **SQLite** pour comparer SQL vs NoSQL (compétence C8 complète).

---

## 🗺️ Compétences CDA mobilisées

| Compétence | Mobilisée ? | Où, concrètement, dans CE projet |
|---|:--:|---|
| C1 — Environnement (.venv/.env/Git) | ✓ | `.env.example`, `.gitignore`, commits par étape |
| C2 — Interfaces (responsive/RGAA) | ~ | Tableau de bord lisible (jauge + barres + verbatims) |
| C3 — Composants métier 🟥 | ~ | `modele.py` (pipeline ML) + `analyse.py` (agrégation), endpoint validé + Bearer |
| C4 — Gestion de projet | ✓ | User stories + historique Git |
| C5 — Analyse & maquettage | ~ | Besoin du food truck → maquette du dashboard |
| C6 — Architecture multicouche | ✓ | Données → `modele.py` (ML) → `analyse.py` (métier) → dashboard, cache JSON |
| C7 — Base relationnelle (MCD/MLD) | — | Pas de base relationnelle (volet NoSQL ici) |
| C8 — Accès SQL + NoSQL 🟥 | ✓ | Volet **NoSQL** : stockage/relecture des analyses en JSON (`analyses.json`) |
| C9 — Plans de tests | ~ | L'**évaluation du modèle** (accuracy, matrice de confusion) est ta démarche de test |
| C10 — Doc de déploiement | — | En bonus seulement |
| C11 — Mise en prod DevOps | — | En bonus seulement |
| 🔒 Transversal (ANSSI/RGPD/RGAA/B1) | ✓ | Secrets en `.env`, validation, anonymisation RGPD, doc scikit-learn lue en anglais |
