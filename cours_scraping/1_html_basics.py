# ============================================================
# 1_html_basics.py — Comprendre la structure d'une page HTML
# ============================================================
# Avant de scraper, il faut comprendre ce qu'on lit.
# Ici on prend un HTML EN DUR et on apprend a y naviguer.
# ============================================================

from bs4 import BeautifulSoup

# Un HTML simple, comme tu pourrais en avoir sur un vrai site
html = """
<html>
  <head>
    <title>Boutique de livres</title>
  </head>
  <body>
    <h1 id="titre-principal">Bienvenue !</h1>

    <ul class="liste-livres">
      <li class="livre">
        <span class="titre">Le Petit Prince</span>
        <span class="prix">12.50</span>
        <a href="/livre/1">Voir</a>
      </li>
      <li class="livre">
        <span class="titre">1984</span>
        <span class="prix">9.90</span>
        <a href="/livre/2">Voir</a>
      </li>
      <li class="livre indisponible">
        <span class="titre">Dune</span>
        <span class="prix">15.00</span>
       ("h1") <a href="/livre/3">Voir</a>
      </li>
    </ul>
  </body>
</html>
"""

# On donne le HTML a BeautifulSoup qui le transforme en arbre
soup = BeautifulSoup(html, "html.parser")

# ============================================================
# 1. Acceder a une seule balise
# ============================================================
print("Le titre de la page :", soup.title.text)
print("Le h1 :", soup.find("h1").text)
print("L'id du h1 :", soup.find("h1")["id"])


# ============================================================
# 2. Trouver TOUTES les balises d'un type
# ============================================================

print("\nTous les livres :")
for livre in soup.find_all("li"):
    titre = livre.find("span", class_="titre").text
    prix = livre.find("span", class_="prix").text
    print(f"  - {titre} : {prix} EUR")


# ============================================================
# 3. Selecteurs CSS — souvent plus puissants
# ============================================================
print("\nMemes infos via CSS selectors :")
for livre in soup.select("li.livre"):
    titre = livre.select_one(".titre").text
    print(titre)
    prix = livre.select_one(".prix").text
    print(prix)

    print(f"  - {titre} : {prix} EUR")


# ============================================================
# 4. Lire un attribut (un lien par exemple)
# ============================================================
print("\nLiens vers les fiches :")
for lien in soup.select("li.livre a"):
    print(f"  {lien.text} -> {lien['href']}")


# ============================================================
# 5. Filtres avances
# ============================================================
print("\nLivres INDISPONIBLES uniquement :")
for livre in soup.select("li.livre.indisponible"):
    print(f"  - {livre.select_one('.titre')}")


# ============================================================
# A retenir
# ============================================================
# - find() = le premier
# - find_all() = tous (renvoie une liste)
# - select() = selecteurs CSS, plus expressif
# - .text = recuperer le texte
# - ["attr"] = recuperer un attribut
# ============================================================
