# 🧪 Mini-projet — Carte des bons coins (~6h) · Niveau 🟠 intermédiaire

> **Type d'IA : 🧮 aucune** — données + géocodage + cartographie interactive. Pas besoin d'IA pour afficher une belle carte filtrable.
>
> **Prérequis :**
> - `pip install flask python-dotenv pandas plotly requests`
> - Tu sais lancer `python app.py` en local sans erreur.
> - 12 lieux lyonnais (sans coordonnées) sont fournis dans `data/lieux.csv`.
> - Le géocodage utilise **Nominatim** (OpenStreetMap), gratuit et sans clé.
>
> 🎒 C'est une **mini-presta freelance** : tu livres un truc qui tourne ET que tu sais expliquer au jury, ligne par ligne.

---

## 🧑‍💼 Le client / le contexte

Tu viens d'être contacté·e par **une association de commerçants et de lieux culturels** d'un quartier de Lyon. Ils ont une liste de « bons coins » dans un tableur, mais rien de visuel à montrer aux visiteurs. Ils veulent une **carte interactive** à intégrer sur leur site : des points colorés par catégorie, des filtres, et une **fiche** par lieu. Ils te paient une journée.

## 🎯 Le besoin

> « Transforme ma liste d'adresses en une **carte qu'on peut explorer**, avec une fiche claire pour chaque lieu. »

## 📦 Ce que tu livres

- Une appli **Flask** qui affiche une **carte interactive** (Plotly) des lieux.
- Des **marqueurs colorés par catégorie** + un **filtre** par catégorie.
- Une **fiche par lieu** (nom, catégorie, description).
- Un **cache de géocodage** (on ne re-géocode pas à chaque lancement).
- Un **README** d'installation + un `.env.example`.

---

## 🧱 Contraintes métier réelles

> Ce ne sont pas des caprices : c'est ce qui sépare un script de hackathon d'une presta livrable.

1. **Budget / temps** : ça tient en une journée ; le géocodage est **mis en cache** (on ne re-géocode pas inutilement).
2. **Géocodage responsable** : Nominatim impose **1 requête/seconde max** et un **User-Agent** identifiable → tu respectes ça (`time.sleep(1)`), sinon tu te fais bloquer (c'est une vraie contrainte d'API).
3. **Sécurité** : aucune clé dans le code → tout dans `.env` ; les données reçues (CSV) sont **validées** (colonnes attendues) → **400** sinon.
4. **Données / RGPD** : adresses de lieux publics uniquement, pas de données personnelles.
5. **Robustesse** : une adresse non géocodable est **ignorée proprement** (log) et n'empêche pas la carte de s'afficher.

---

## 🪜 Étapes guidées

> Commit après chaque étape (le jury veut un historique Git qui raconte ta progression).

### 1. Le squelette + les données (~30 min)
Crée `app.py` (port **6015**), charge `.env`, lis `data/lieux.csv` avec pandas.

### 2. Le géocodage + son cache — le volet accès données (~1h30) — *le cœur, à savoir réexpliquer*
Crée `geocode.py` : pour chaque lieu, transforme l'adresse en `latitude/longitude` via **Nominatim**, et **mets le résultat en cache** dans `cache_geocode.json` (clé = adresse). Au lancement suivant, on relit le cache.
> 💡 Nominatim, dans les règles :
> ```python
> import requests, time, json
> from pathlib import Path
> CACHE = Path("cache_geocode.json")
> cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
> def geocoder(adresse):
>     if adresse in cache:
>         return cache[adresse]
>     r = requests.get("https://nominatim.openstreetmap.org/search",
>             params={"q": adresse, "format": "json", "limit": 1},
>             headers={"User-Agent": "carte-bons-coins-pedago/1.0"}, timeout=10).json()
>     time.sleep(1)                       # respecte la politique d'usage (1 req/s)
>     coords = {"lat": float(r[0]["lat"]), "lon": float(r[0]["lon"])} if r else None
>     cache[adresse] = coords; CACHE.write_text(json.dumps(cache, ensure_ascii=False))
>     return coords
> ```
> ⚠️ Le cache JSON, c'est aussi ton volet **NoSQL** (un document clé→valeur) ET ce qui rend l'appli rapide et économe.

### 3. Le composant métier : nettoyer & préparer (~45 min)
Crée `lieux.py` : valide chaque lieu (champs obligatoires), écarte ceux sans coordonnées, regroupe par catégorie. Construis la structure que la carte va consommer.

### 4. La carte interactive (~1h30)
Construis la carte avec **Plotly** (fond OpenStreetMap), un point par lieu, **couleur par catégorie**, le nom au survol. Affiche la **fiche** du lieu (description) au clic ou à côté de la carte. Sers la page HTML.
> 💡 :
> ```python
> import plotly.express as px
> fig = px.scatter_map(df, lat="lat", lon="lon", color="categorie",
>                      hover_name="nom", hover_data=["description"], zoom=12, height=600)
> fig.update_layout(map_style="open-street-map")
> carte_html = fig.to_html(full_html=False)     # à injecter dans ton template
> ```
> *(Selon ta version de Plotly : `scatter_mapbox` + `mapbox_style="open-street-map"`.)*

### 5. Sécuriser + valider (~45 min)
Si tu exposes un endpoint pour recharger des lieux (`POST /api/lieux`), protège-le par **Bearer** et valide les colonnes du CSV → **400** sinon.
> 💡 Décorateur `@require_token` repris de `cours_microservice`.

### 6. Finitions : README, `.env.example`, commits (~30 min)
README (user stories + install + note sur le cache et la politique Nominatim). `.env.example` : `API_TOKEN`. `.gitignore` excluant `.env`, `cache_geocode.json`.

---

## ✅ Critères de réussite (grille façon jury CDA)

- [ ] Je sais **expliquer le géocodage + le cache** et pourquoi je respecte 1 req/s.
- [ ] Une adresse non géocodable est **gérée proprement** (la carte s'affiche quand même).
- [ ] **Aucun secret dans le code** : tout en `.env`, `.env.example` commité (pas `.env`).
- [ ] {si endpoint} il est **protégé par token Bearer** et valide les entrées → 400.
- [ ] Le **cache** évite de rappeler le géocodeur inutilement.
- [ ] **Historique Git** + **README** réutilisable par un inconnu.
- [ ] La carte est **interactive** (zoom, survol, filtre par catégorie).

---

## 🚀 Bonus (si tu finis en avance)

- Ajoute une **barre de recherche** ou des **boutons de filtre** par catégorie.
- Calcule la **distance** entre deux lieux sélectionnés.
- Range les lieux dans **SQLite** (table `lieux`, catégorie en clé étrangère vers une table `categories`) → compétences C7 + C8 SQL.
- Déploie sur **Render** (suis `cours_microservice/deploiement_render.md`).

---

## 🗺️ Compétences CDA mobilisées

| Compétence | Mobilisée ? | Où, concrètement, dans CE projet |
|---|:--:|---|
| C1 — Environnement (.venv/.env/Git) | ✓ | `.env.example`, `.gitignore`, commits par étape |
| C2 — Interfaces (responsive/RGAA) | ✓ | Carte interactive + filtres, pensée mobile |
| C3 — Composants métier 🟥 | ~ | `lieux.py` (validation/préparation), gestion des erreurs de géocodage |
| C4 — Gestion de projet | ✓ | User stories + historique Git |
| C5 — Analyse & maquettage | ~ | Besoin de l'asso → maquette de la carte |
| C6 — Architecture multicouche | ✓ | CSV → géocodage → métier → carte ; cache séparé |
| C7 — Base relationnelle (MCD/MLD) | ~ | Modélisation des lieux (en bonus : tables SQLite + clé étrangère catégorie) |
| C8 — Accès SQL + NoSQL 🟥 | ~ | Volet **NoSQL** : cache JSON clé→valeur (géocodage) ; SQL en bonus |
| C9 — Plans de tests | — | En bonus seulement |
| C10 — Doc de déploiement | — | En bonus (Render) |
| C11 — Mise en prod DevOps | — | En bonus |
| 🔒 Transversal (ANSSI/RGPD/RGAA/B1) | ✓ | Secrets en `.env`, **respect de la politique d'API** Nominatim, robustesse, doc Plotly lue en anglais |
