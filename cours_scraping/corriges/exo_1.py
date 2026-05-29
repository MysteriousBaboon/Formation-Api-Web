# ============================================================
# Corrigé exo 1 — Échauffement HTML (pas de réseau)
# ============================================================
# On parse du HTML stocké dans une variable, sans requests.
# Objectifs : noms, prix moyen, articles en rupture, data-id.
# ============================================================

from bs4 import BeautifulSoup

HTML = """
<div class="catalogue">
  <div class="article" data-id="42">
    <h2>Casque audio</h2>
    <span class="prix">129.99</span>
    <span class="stock">7 en stock</span>
  </div>
  <div class="article" data-id="43">
    <h2>Clavier mécanique</h2>
    <span class="prix">89.00</span>
    <span class="stock">0 en stock</span>
  </div>
  <div class="article" data-id="44">
    <h2>Souris gamer</h2>
    <span class="prix">45.50</span>
    <span class="stock">12 en stock</span>
  </div>
</div>
"""

soup = BeautifulSoup(HTML, "html.parser")

# ------------------------------------------------------------
# 1. Tous les noms d'articles
# ------------------------------------------------------------
print("Articles :")
for article in soup.select("div.article"):
    print(" -", article.h2.text)

# ------------------------------------------------------------
# 2. Prix moyen
# ------------------------------------------------------------
prix = [float(a.select_one(".prix").text) for a in soup.select("div.article")]
print(f"\nPrix moyen : {sum(prix) / len(prix):.2f} €")

# ------------------------------------------------------------
# 3. Articles en rupture de stock (le texte commence par "0")
# ------------------------------------------------------------
print("\nEn rupture de stock :")
for article in soup.select("div.article"):
    stock_txt = article.select_one(".stock").text          # "0 en stock"
    nb = int(stock_txt.split()[0])                          # -> 0
    if nb == 0:
        print(" -", article.h2.text)

# ------------------------------------------------------------
# 4. Le data-id de chaque article
# ------------------------------------------------------------
print("\ndata-id de chaque article :")
for article in soup.select("div.article"):
    print(f" - {article.h2.text} : id={article['data-id']}")