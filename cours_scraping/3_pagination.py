# ============================================================
# 3_pagination.py — Scraper plusieurs pages a la suite
# ============================================================
# Le site books.toscrape.com a 50 pages de livres.
# On va toutes les parcourir.
#
# Pattern URL : /catalogue/page-1.html, page-2.html, etc.
# ============================================================

import requests
from bs4 import BeautifulSoup
import time
import pandas as pd


BASE = "https://books.toscrape.com/catalogue/"


def scraper_page(numero):
    """Scrape une page et retourne la liste des livres trouves."""
    url = f"{BASE}page-{numero}.html"
    response = requests.get(url, timeout=10)
BeautifulSoup
    # 404 = on a depasse la derniere page, on s'arrete proprement
    if response.status_code == 404:
        return None

    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    livres = []
    for article in soup.select("article.product_pod"):
        livres.append({
            "titre": article.h3.a["title"],
            "prix": float(article.select_one(".price_color").text.replace("£", "")),
            "dispo": article.select_one(".availability").text.strip(),
            "note": article.select_one(".star-rating")["class"][1],
        })
    return livres


# ============================================================
# Boucle principale
# ============================================================
tous_les_livres = []
page = 1

# On limite a 5 pages pour la demo (et eviter de matraquer le site)
# Pour TOUT scraper, mets MAX_PAGES = 100 (il s'arretera tout seul au 404)
MAX_PAGES = 5

while page <= MAX_PAGES:
    print(f"Page {page}...")
    livres = scraper_page(page)

    if livres is None:
        print("Plus de pages, on s'arrete.")
        break

    tous_les_livres.extend(livres)
    page += 1

    # Toujours un sleep entre les requetes
    time.sleep(0.5)

print(f"\nTotal : {len(tous_les_livres)} livres scrapes")


# ============================================================
# Sauvegarder en CSV
# ============================================================
df = pd.DataFrame(tous_les_livres)
df.to_csv("livres_complet.csv", index=False)

# Petite analyse pour montrer la puissance du combo
print("\nPrix moyen par note :")
print(df.groupby("note")["prix"].mean())

print(f"\nLivre le plus cher : {df.loc[df['prix'].idxmax(), 'titre']} ({df['prix'].max()} GBP)")
print(f"Livre le moins cher : {df.loc[df['prix'].idxmin(), 'titre']} ({df['prix'].min()} GBP)")


# ============================================================
# Alternative : suivre le bouton "next"
# ============================================================
# Quand l'URL n'est pas previsible, on suit le lien "page suivante" :
#
# url = "https://example.com/page-1"
# while url:
#     response = requests.get(url, timeout=10)
#     soup = BeautifulSoup(response.text, "html.parser")
#     # ... extraire ...
#     next_btn = soup.select_one("li.next a")
#     url = urljoin(response.url, next_btn["href"]) if next_btn else None
#
# (`urljoin` de `urllib.parse` gere les liens relatifs)
# ============================================================
