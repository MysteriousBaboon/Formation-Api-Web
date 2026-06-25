# 🧪 Mini-projet — Terrasse-o-mètre (~6h) · Niveau 🟠 intermédiaire

> **Type d'IA : 🧮 aucune** — c'est un choix assumé : une **règle métier claire** suffit, elle est gratuite et tu peux la justifier au jury. Savoir *ne pas* mettre d'IA est un argument de pro.
>
> **Prérequis :**
> - `pip install flask python-dotenv requests pandas matplotlib`
> - Tu sais lancer `python app.py` en local sans erreur.
> - La règle métier (seuils) est fournie dans `data/seuils_exemple.json` — pas en dur dans le code.
> - Aucune clé n'est nécessaire : **Open-Meteo** est gratuit et sans inscription.
>
> 🎒 C'est une **mini-presta freelance** : tu livres un truc qui tourne ET que tu sais expliquer au jury, ligne par ligne.

---

## 🧑‍💼 Le client / le contexte

Tu viens d'être contacté·e par **Karim, patron d'un café avec terrasse à Bordeaux**. Chaque matin, il joue à pile ou face : sortir les tables et les parasols (1h de boulot, plus appeler un extra), ou tout laisser en salle. S'il se trompe, il perd soit du chiffre, soit une matinée de manutention pour rien. Il veut un petit tableau de bord qui lui dit, chaque matin, **« terrasse ou pas ? »** avec une vraie raison derrière. Il te paie une journée.

## 🎯 Le besoin

> « Dis-moi chaque matin si je sors la terrasse demain, et si je dois prévoir un extra — avec un mot que je peux transférer à mon équipe. »

## 📦 Ce que tu livres

- Une appli **Flask** avec un tableau de bord : **courbe température + probabilité de pluie** sur la journée.
- Un **badge de décision GO / MITIGÉ / NO-GO** calculé par **ta** règle métier.
- Une recommandation **staff** (faut-il un extra ?).
- Un **message du jour** pour l'équipe (texte prêt-à-transférer).
- Un **job du matin** qui rafraîchit tout automatiquement.
- Un **README** d'installation + un `.env.example`.

---

## 🧱 Contraintes métier réelles

> Ce ne sont pas des caprices : c'est ce qui sépare un script de hackathon d'une presta livrable.

1. **Budget / temps** : ça tient en une journée ; l'API météo est gratuite mais on ne la spamme pas (1 appel / matin).
2. **Sécurité** : aucune clé dans le code → tout dans `.env` ; l'endpoint `/api/terrasse` est **protégé par token Bearer** ; les paramètres (ville/coordonnées) sont **validés** → **400** sinon.
3. **Données / RGPD** : pas de données personnelles (juste de la météo publique) — sache le dire.
4. **Robustesse** : si Open-Meteo ne répond pas (timeout 10 s), le dashboard affiche « météo indisponible » au lieu de planter.
5. **La décision est explicable** : le GO/NO-GO vient de **seuils lisibles** (`data/seuils_exemple.json`), pas d'une boîte noire. Tu dois pouvoir justifier chaque seuil.

---

## 🪜 Étapes guidées

> Commit après chaque étape (le jury veut un historique Git qui raconte ta progression).

### 1. Le squelette Flask (~30 min)
Crée `app.py` (port **6012**), charge `.env` et `data/seuils_exemple.json`, sers une page tableau de bord (vide pour l'instant).

### 2. Récupérer la météo (~1h)
Crée `meteo.py` : appelle **Open-Meteo** (géocodage puis prévisions horaires), range les heures du jour dans un DataFrame pandas.
> 💡 Deux appels `requests`, sans clé :
> ```python
> import requests
> # géocodage (si tu pars d'un nom de ville)
> g = requests.get("https://geocoding-api.open-meteo.com/v1/search",
>                  params={"name": "Bordeaux", "count": 1, "language": "fr"}, timeout=10).json()
> lat, lon = g["results"][0]["latitude"], g["results"][0]["longitude"]
> # prévisions horaires
> p = {"latitude": lat, "longitude": lon, "timezone": "auto", "forecast_days": 2,
>      "hourly": "temperature_2m,precipitation_probability,wind_speed_10m"}
> meteo = requests.get("https://api.open-meteo.com/v1/forecast", params=p, timeout=10).json()
> df = pd.DataFrame(meteo["hourly"])      # colonnes: time, temperature_2m, ...
> ```

### 3. Le composant métier : la règle GO/NO-GO (~1h30) — *le cœur, à savoir réexpliquer*
Crée `regles.py` avec `decider(df, seuils) -> dict`. Pour la **plage horaire** d'ouverture (`plage_horaire`), regarde la **température moyenne**, la **proba de pluie max** et le **vent max**, puis applique les seuils :
- tout dans le vert → **GO** ; un seul critère limite → **MITIGÉ** ; température < seuil ou pluie > seuil → **NO-GO**.
- staff : si la température dépasse `seuil_staff_extra_c`, recommande un extra.
> 💡 La règle vit dans le JSON, pas dans le code :
> ```python
> r = seuils["regles"]
> temp_ok  = temp_moy >= r["temperature_min_go_c"]
> pluie_ok = pluie_max <= r["proba_pluie_max_go_pct"]
> vent_ok  = vent_max  <= r["vent_max_go_kmh"]
> decision = "GO" if (temp_ok and pluie_ok and vent_ok) else ("NO-GO" if not (temp_ok and pluie_ok) else "MITIGÉ")
> ```
> ⚠️ C'est CETTE fonction que le jury fera dérouler. Garde-la pure (entrées → sortie), sans appel réseau dedans : c'est aussi ce qui la rend testable (voir bonus pytest).

### 4. Le message d'équipe — sans IA (~30 min)
Le mot à transférer à l'équipe vient des **messages préparés** dans `seuils_exemple.json` (`messages.go` / `mitige` / `nogo`), complété par les chiffres du jour (température, pluie).
> 💡 `msg = seuils["messages"][decision.lower().replace("-","")] + f" (max {temp_max}°C, pluie {pluie_max}%)"`.
> 💡 *Pourquoi pas d'IA ici ?* Parce qu'il n'y a que 3 cas : un dictionnaire de messages est plus fiable, gratuit et instantané. Savoir choisir l'outil le plus simple, c'est exactement ce que le jury valorise.

### 5. Le tableau de bord visuel (~1h)
Génère un graphe (matplotlib `Agg`) : **courbe de température** + **proba de pluie** sur la journée, et affiche le **badge** coloré (vert/orange/rouge) avec la raison.
> 💡 Sers l'image comme dans `cours_dataviz` (exo 5) : `io.BytesIO` + `send_file(buf, mimetype="image/png")`.

### 6. Sécuriser l'endpoint + le job du matin (~45 min)
Expose `POST /api/terrasse` (Bearer) qui renvoie la décision en JSON. Crée `job_matin.py` qui appelle tout chaque matin.
> 💡 Programme le job comme dans `cours_cron` :
> ```python
> import schedule, time
> schedule.every().day.at("07:30").do(rafraichir)
> while True: schedule.run_pending(); time.sleep(30)
> ```

### 7. Finitions : README, `.env.example`, commits (~30 min)
README avec user stories + install + explication des seuils. `.env.example` : `API_TOKEN`. `.gitignore` excluant `.env`.

---

## ✅ Critères de réussite (grille façon jury CDA)

- [ ] Je sais **expliquer `regles.py`** ligne à ligne et **justifier chaque seuil**.
- [ ] Je sais **justifier l'absence d'IA** (une règle suffit, c'est plus fiable et gratuit).
- [ ] Les paramètres sont **validés** ; une entrée invalide renvoie un **code 400**.
- [ ] **Aucun secret dans le code** : tout en `.env`, `.env.example` commité (pas `.env`).
- [ ] `/api/terrasse` est **protégé par token Bearer** (401 sans / mauvais token).
- [ ] L'appli **ne plante pas** si la météo est indisponible (gestion du timeout).
- [ ] **Historique Git** + **README** qui permet à un inconnu d'installer et lancer.

---

## 🚀 Bonus (si tu finis en avance)

- Écris `test_regles.py` (`pytest`) : une météo « 25°C, 0% pluie » sort **GO + extra** ; « 12°C » sort **NO-GO** (compétence C9).
- Pousse le résultat sur un **webhook n8n** chaque matin (alerte Slack pour l'équipe) — compétence C11.
- Gère **plusieurs établissements** (une ligne de seuils par lieu).
- Déploie sur **Render** + un vrai cron (suis `cours_microservice/deploiement_render.md`).

---

## 🗺️ Compétences CDA mobilisées

| Compétence | Mobilisée ? | Où, concrètement, dans CE projet |
|---|:--:|---|
| C1 — Environnement (.venv/.env/Git) | ✓ | `.env.example`, `.gitignore`, commits par étape |
| C2 — Interfaces (responsive/RGAA) | ~ | Tableau de bord lisible (graphe + badge), pensé mobile |
| C3 — Composants métier 🟥 | ✓ | `regles.py` (décision GO/NO-GO/staff), endpoint validé + Bearer + codes HTTP |
| C4 — Gestion de projet | ✓ | User stories + historique Git |
| C5 — Analyse & maquettage | ~ | Besoin de Karim → maquette du dashboard avant de coder |
| C6 — Architecture multicouche | ✓ | API météo → `meteo.py` → `regles.py` (métier) → dashboard ; `job_matin.py` orchestre |
| C7 — Base relationnelle (MCD/MLD) | — | Pas de base de données |
| C8 — Accès SQL + NoSQL 🟥 | — | Pas d'accès données ici (voir `factures-en-clair`) |
| C9 — Plans de tests | ~ | En bonus : `test_regles.py` (la règle est pure → facile à tester) |
| C10 — Doc de déploiement | — | En bonus (Render) |
| C11 — Mise en prod DevOps | ~ | En bonus : job cron + webhook n8n |
| 🔒 Transversal (ANSSI/RGPD/RGAA/B1) | ✓ | Secrets en `.env`, validation, robustesse réseau, doc Open-Meteo lue en anglais |
