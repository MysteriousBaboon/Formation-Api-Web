# 🧪 Mini-projet — Revue de presse du lundi (~6h) · Niveau 🟠 intermédiaire

> **Type d'IA : 🧮 aucune** — pur scraping + traitement de données + mise en forme. Pas besoin d'IA pour regrouper et présenter proprement.
>
> **Prérequis :**
> - `pip install requests beautifulsoup4 jinja2 python-dotenv schedule`
> - Tu sais lancer un script Python sans erreur.
> - Pas de données fournies : tu **scrapes un site bac à sable** prévu pour ça → `https://quotes.toscrape.com`.
>
> 🎒 C'est une **mini-presta freelance** : tu livres un truc qui tourne ET que tu sais expliquer au jury, ligne par ligne.

---

## 🧑‍💼 Le client / le contexte

Tu viens d'être contacté·e par **Inès, animatrice d'une communauté en ligne** (newsletter sur le développement personnel et le travail). Chaque lundi, elle publie une **« sélection de citations inspirantes »** regroupées par thème. Elle y passe une heure tous les lundis matin : chercher, copier-coller, mettre en forme. Elle veut **automatiser** ça : un digest prêt à publier, généré tout seul. Elle te paie une journée.

## 🎯 Le besoin

> « Chaque lundi, sors-moi une sélection de citations regroupées par thème, dans une page prête à copier dans ma newsletter. »

## 📦 Ce que tu livres

- Un **scraper** qui récupère des citations (texte, auteur, tags) depuis `quotes.toscrape.com`, en gérant la **pagination**.
- Une **sélection regroupée par thème** (à partir des tags).
- Une **page HTML « digest » en cartes**, propre et lisible.
- Un **job du lundi matin** qui régénère le digest et l'envoie sur un **webhook**.
- Un **README** d'installation + un `.env.example`.

---

## 🧱 Contraintes métier réelles

> Ce ne sont pas des caprices : c'est ce qui sépare un script de hackathon d'une presta livrable.

1. **Budget / temps** : ça tient en une journée ; aucun service payant.
2. **Scraping responsable** : tu vises **uniquement** le site bac à sable `quotes.toscrape.com` (conçu pour s'entraîner, aucun souci éthique). User-Agent réaliste, `timeout=10`, `time.sleep(0.3)` entre les pages.
3. **Sécurité** : aucune URL de webhook dans le code → tout dans `.env`.
4. **Robustesse** : si le site ne répond pas (timeout) ou si une page change de structure, le script log l'erreur et **continue** avec ce qu'il a, sans planter.
5. **Prêt à publier** : le digest est une page HTML autonome (styles inline), lisible sur mobile.

---

## 🪜 Étapes guidées

> Commit après chaque étape (le jury veut un historique Git qui raconte ta progression).

### 1. Le scraper (~1h15)
Crée `scraper.py` : récupère les citations sur **toutes les pages** (suis le bouton « Next »). Pour chaque citation : `texte`, `auteur`, `tags`.
> 💡 Sélecteurs BeautifulSoup (repris de `cours_scraping`) :
> ```python
> import requests, time
> from bs4 import BeautifulSoup
> HEADERS = {"User-Agent": "Mozilla/5.0 (revue-presse pédagogique)"}
> url = "https://quotes.toscrape.com/"
> citations = []
> while url:
>     soup = BeautifulSoup(requests.get(url, headers=HEADERS, timeout=10).text, "html.parser")
>     for q in soup.select(".quote"):
>         citations.append({
>             "texte": q.select_one(".text").get_text(strip=True),
>             "auteur": q.select_one(".author").get_text(strip=True),
>             "tags": [t.get_text(strip=True) for t in q.select(".tag")],
>         })
>     nxt = soup.select_one("li.next a")
>     url = "https://quotes.toscrape.com" + nxt["href"] if nxt else None
>     time.sleep(0.3)
> ```
> ⚠️ Ne pointe **jamais** ce scraper vers un vrai média : tu n'as pas le droit, et ce n'est pas le but. Le site bac à sable est là exprès.

### 2. Le composant métier : sélectionner & regrouper (~1h15) — *le cœur, à savoir réexpliquer*
Crée `selection.py` : repère les **thèmes dominants** (tags les plus fréquents), puis regroupe ~10 citations variées par thème (sans doublon).
> 💡 :
> ```python
> from collections import Counter
> tous_les_tags = [t for c in citations for t in c["tags"]]
> themes = [tag for tag, _ in Counter(tous_les_tags).most_common(5)]
> # pour chaque thème, garde quelques citations qui portent ce tag
> ```

### 3. Le digest HTML en cartes (~1h15)
Crée un template Jinja `digest.html.j2` : une **intro** (texte préparé, ex. « Voici la sélection de la semaine ✨ »), puis une carte par citation (texte, auteur, tags), regroupées par thème. Rends-le en `digest.html`.
> 💡 `from jinja2 import Template; Template(gabarit).render(intro=..., themes=...)` puis écris le fichier.

### 4. Le job du lundi + le webhook (~45 min)
Crée `job_lundi.py` : régénère le digest et **POST** un résumé sur l'URL de webhook (`WEBHOOK_URL` du `.env`).
> 💡 Programme-le comme dans `cours_cron` :
> ```python
> import schedule, time
> schedule.every().monday.at("08:00").do(generer_et_envoyer)
> while True: schedule.run_pending(); time.sleep(30)
> ```
> 💡 Pas de webhook sous la main ? Teste avec [https://webhook.site](https://webhook.site).

### 5. Robustesse + secrets (~45 min)
Entoure les appels réseau de `try/except`, log les erreurs (`logging`). Vérifie qu'**aucune URL** n'est en dur : tout vient du `.env`.

### 6. Finitions : README, `.env.example`, commits (~30 min)
README avec user stories + install + **explication de l'éthique du scraping** (pourquoi un site bac à sable). `.env.example` : `WEBHOOK_URL`. `.gitignore` excluant `.env` et `digest.html`.

---

## ✅ Critères de réussite (grille façon jury CDA)

- [ ] Je sais **expliquer mon scraper** (sélecteurs, pagination, anti-bot) et **pourquoi je vise un site bac à sable**.
- [ ] Le script **gère la pagination** (toutes les pages, pas juste la première).
- [ ] **Aucun secret/URL dans le code** : tout en `.env`, `.env.example` commité (pas `.env`).
- [ ] Le script **ne plante pas** si une page est indisponible (try/except + log).
- [ ] **Historique Git** = commits petits et réguliers.
- [ ] Un **README** permet à un inconnu d'installer et lancer.
- [ ] Le digest est **lisible sur mobile**.

---

## 🚀 Bonus (si tu finis en avance)

- Évite les **doublons** d'une semaine à l'autre (garde un historique des citations déjà publiées en JSON).
- Envoie le digest par **email** au lieu d'un webhook (lib `smtplib`).
- Ajoute une **image d'en-tête** générée (réutilise l'idée d'`affiche-moi-ca`).
- Déploie le job sur **Render** avec un vrai cron — compétence C11.

---

## 🗺️ Compétences CDA mobilisées

| Compétence | Mobilisée ? | Où, concrètement, dans CE projet |
|---|:--:|---|
| C1 — Environnement (.venv/.env/Git) | ✓ | `.env.example`, `.gitignore`, commits par étape |
| C2 — Interfaces (responsive/RGAA) | ~ | Page digest HTML lisible sur mobile |
| C3 — Composants métier 🟥 | ~ | `selection.py` (sélection/regroupement par thème), robustesse réseau |
| C4 — Gestion de projet | ✓ | User stories + historique Git |
| C5 — Analyse & maquettage | ~ | Besoin d'Inès → maquette du digest |
| C6 — Architecture multicouche | ~ | Scraping → sélection (métier) → rendu HTML ; `job_lundi.py` orchestre |
| C7 — Base relationnelle (MCD/MLD) | — | Pas de base de données |
| C8 — Accès SQL + NoSQL 🟥 | — | Pas d'accès données ici (historique JSON possible en bonus) |
| C9 — Plans de tests | — | En bonus seulement |
| C10 — Doc de déploiement | — | En bonus (Render) |
| C11 — Mise en prod DevOps | ~ | Job cron + envoi webhook (amorce d'automatisation/DevOps) |
| 🔒 Transversal (ANSSI/RGPD/RGAA/B1) | ✓ | Secrets en `.env`, **scraping éthique** (site bac à sable), robustesse, doc BeautifulSoup lue en anglais |
