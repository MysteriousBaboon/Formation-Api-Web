# 🕸️ Cours 2 — Web Scraping

Récupérer la donnée d'un site web même quand il n'y a pas d'API.

## 🎯 Objectifs

À la fin de ce module, tu seras capable de :

- Lire et comprendre une page HTML basique
- Extraire n'importe quel contenu d'une page avec **BeautifulSoup**
- Gérer la **pagination** (parcourir plusieurs pages automatiquement)
- Contourner les protections basiques (User-Agent, `time.sleep`)
- Reconnaître quand un site est trop compliqué (JS dynamique) et savoir quoi faire

## 📁 Structure

```
cours_scraping/
├── README.md
├── cours.md                ← Cours complet
├── requirements.txt
├── 1_html_basics.py        ← Parser du HTML "à la main"
├── 2_beautifulsoup.py      ← Extraire un titre et une liste
├── 3_pagination.py         ← Scraper plusieurs pages
├── 4_anti_bot.py           ← Headers, User-Agent, sleep
├── 5_playwright_demo.py    ← Demo pour les sites en JavaScript
├── exos.md                 ← Exercices (3h)
└── exemples/               ← HTML statique pour s'entraîner offline
```

## 🚀 Setup

```bash
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

Pour `playwright`, après l'install pip :
```bash
playwright install chromium
```
(Optionnel — uniquement si tu veux faire la démo du fichier 5.)

## ⚖️ Mini avertissement éthique

Avant de scraper un site :

1. Regarde si une **API officielle** existe (toujours mieux)
2. Lis les **conditions d'utilisation** du site
3. Respecte le fichier `/robots.txt` (ex: `https://site.com/robots.txt`)
4. Ajoute toujours un `time.sleep` entre les requêtes pour ne pas matraquer leur serveur
5. Ne scrape **jamais** de données personnelles, médicales, ou protégées

Les sites utilisés dans ce cours (`books.toscrape.com`, `quotes.toscrape.com`) sont **conçus pour être scrapés** : aucun problème éthique.
