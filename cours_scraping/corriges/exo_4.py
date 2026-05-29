# ============================================================
# Corrigé exo 4 — Catalogue complet books.toscrape (10 pages)
# ============================================================
# titre, prix (float), note (mot), dispo -> livres_complet.csv
# puis mini-rapport avec pandas.
# ============================================================

import time

import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE = "https://books.toscrape.com/catalogue/"


def scraper_page(numero):
    url = f"{BASE}page-{numero}.html"
    response = requests.get(url, timeout=10)
    if response.status_code == 404:
        return None
    response.raise_for_status()
    # /!\ ENCODAGE : sans ça, le symbole £ devient "Â£".
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    livres = []
    for article in soup.select("article.product_pod"):
        titre = article.h3.a["title"]
        prix_txt = article.select_one(".price_color").text.strip()   # "£51.77"
        prix = float(prix_txt.replace("£", ""))
        note = article.select_one("p.star-rating")["class"][1]        # "Three"
        dispo = article.select_one(".availability").text.strip()
        livres.append({"titre": titre, "prix": prix, "note": note, "dispo": dispo})
    return livres


tous = []
for page in range(1, 11):   # 10 premières pages
    print(f"Page {page}...")
    livres = scraper_page(page)
    if livres is None:
        break
    tous.extend(livres)
    time.sleep(0.3)

df = pd.DataFrame(tous)
df.to_csv("livres_complet.csv", index=False, encoding="utf-8")

# ------------------------------------------------------------
# Mini rapport
# ------------------------------------------------------------
print(f"\n{'=' * 45}")
print(f"Total livres   : {len(df)}")
print(f"Prix moyen     : £{df['prix'].mean():.2f}")
print("\nNombre de livres par note :")
print(df["note"].value_counts())
print("\nTop 5 des livres les plus chers :")
print(df.sort_values("prix", ascending=False).head(5)[["titre", "prix"]].to_string(index=False))