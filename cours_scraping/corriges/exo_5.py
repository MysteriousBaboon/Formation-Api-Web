# ============================================================
# Corrigé exo 5 — Fiche détail des 5 livres les plus chers
# ============================================================
# On repart du CSV de l'exo 4, on prend les 5 plus chers, on
# va sur chaque fiche détail récupérer description + stock.
#
# /!\ Les href du catalogue sont relatifs -> urljoin.
# ============================================================

import json
import re
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE = "https://books.toscrape.com/catalogue/"


def url_fiche(titre):
    """Retrouve l'URL de la fiche d'un livre depuis la page 1 du catalogue.

    (Le CSV de l'exo 4 ne stocke pas l'URL : on la récupère en re-scrapant
    le catalogue et en associant chaque titre à son href.)
    """
    # Construit une fois la table {titre: url} en parcourant quelques pages.
    return TABLE_URLS.get(titre)


def construire_table_urls(nb_pages=10):
    table = {}
    for page in range(1, nb_pages + 1):
        url = f"{BASE}page-{page}.html"
        r = requests.get(url, timeout=10)
        if r.status_code == 404:
            break
        r.encoding = "utf-8"
        soup = BeautifulSoup(r.text, "html.parser")
        for article in soup.select("article.product_pod"):
            titre = article.h3.a["title"]
            table[titre] = urljoin(url, article.h3.a["href"])
        time.sleep(0.3)
    return table


def scraper_fiche(url):
    r = requests.get(url, timeout=10)
    r.encoding = "utf-8"
    soup = BeautifulSoup(r.text, "html.parser")

    # Description : le <p> qui suit la div #product_description
    bloc = soup.select_one("#product_description")
    description = ""
    if bloc:
        p = bloc.find_next_sibling("p")
        description = p.text.strip() if p else ""

    # Stock : texte du type "In stock (22 available)"
    dispo_txt = soup.select_one(".availability").text.strip()
    match = re.search(r"\((\d+) available\)", dispo_txt)
    stock = int(match.group(1)) if match else 0

    return {"description": description, "stock": stock}


# ------------------------------------------------------------
# 1. Charger le CSV de l'exo 4 et prendre les 5 plus chers
# ------------------------------------------------------------
df = pd.read_csv("livres_complet.csv")
top5 = df.sort_values("prix", ascending=False).head(5)

# 2. Table titre -> URL (les fiches ne sont pas dans le CSV)
TABLE_URLS = construire_table_urls()

# 3. Scraper chaque fiche
fiches = []
for _, row in top5.iterrows():
    titre = row["titre"]
    url = url_fiche(titre)
    if not url:
        print(f"URL introuvable pour : {titre}")
        continue
    detail = scraper_fiche(url)
    fiches.append({
        "titre": titre,
        "prix": float(row["prix"]),
        "url": url,
        **detail,
    })
    time.sleep(0.3)

# 4. Sauvegarde JSON
with open("fiches_detail.json", "w", encoding="utf-8") as f:
    json.dump(fiches, f, ensure_ascii=False, indent=2)

print(f"{len(fiches)} fiches -> fiches_detail.json")
for fiche in fiches:
    print(f"\n{fiche['titre']} (£{fiche['prix']}) — {fiche['stock']} en stock")
    print(f"  {fiche['description'][:100]}...")