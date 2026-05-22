# ============================================================
# 2_beautifulsoup.py — Premier scraping sur un vrai site
# ============================================================
# Cible : https://books.toscrape.com/
# C'est un site officiellement concu pour s'entrainer au scraping.
# Pas d'API, pas de protection, donnees stables.
# ============================================================

import requests
from bs4 import BeautifulSoup


URL = "https://books.toscrape.com/"

# ============================================================
# 1. Telecharger la pagettps://books.toscrape.com/
# ============================================================
response = requests.get(URL, timeout=10)
response.encoding = 'utf-8'
response.raise_for_status()        # plante si code != 200

print(f"Status : {response.status_code}")
print(f"Taille du HTML : {len(response.text)} caracteres")

# ============================================================
# 2. Parser avec BeautifulSoup
# ============================================================
soup = BeautifulSoup(response.text, "html.parser", from_encoding='utf-8')

# Inspecte la page dans Chrome (clic droit -> Inspecter) :
# Chaque livre est dans une balise <article class="product_pod">
articles = soup.select("article.product_pod")

print(f"Trouve {len(articles)} livres sur la page d'accueil\n")


# ============================================================
# 3. Extraire les infos pour chaque livre
# ============================================================
livres = []
for article in articles:
    # Le titre est dans : <h3><a title="..."></a></h3>
    titre = article.h3.a["title"]

    # Le prix : <p class="price_color">£51.77</p>
    prix_texte = article.select_one(".price_color").text
    # On nettoie pour avoir un float : "£51.77" -> 51.77
    price = float(prix_texte.replace("£", "").strip()) if prix_texte else 0
    # prix = float(prix_texte.replace("£", "").strip())

    # Disponibilite : <p class="instock availability">In stock</p>
    dispo = article.select_one(".availability").text.strip()

    # Note (rating) : la classe est par exemple "star-rating Three"
    classes = article.select_one(".star-rating")["class"]
    note = classes[1]   # "Three", "Five", etc.

    livres.append({
        "titre": titre,
        "prix": price,
        "dispo": dispo,
        "note": note,
    })


# ============================================================
# 4. Afficher le resultat
# ============================================================
for livre in livres[:5]:
    print(livre)

print(f"\nPrix moyen : {sum(l['prix'] for l in livres) / len(livres):.2f} GBP")


# ============================================================
# 5. Sauvegarder en CSV
# ============================================================
import pandas as pd

df = pd.DataFrame(livres)
df.to_csv("livres.csv", index=False)
print("\nResultat sauvegarde dans livres.csv")
