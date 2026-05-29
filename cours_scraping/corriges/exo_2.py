# ============================================================
# Corrigé exo 2 — Citations de quotes.toscrape.com
# ============================================================
# texte + auteur + tags de chaque citation -> citations.json
# Bonus : l'auteur le plus présent sur la page.
# ============================================================

import json
from collections import Counter

import requests
from bs4 import BeautifulSoup

URL = "https://quotes.toscrape.com/"

response = requests.get(URL, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

citations = []
for bloc in soup.select("div.quote"):
    texte = bloc.select_one(".text").text.strip()
    auteur = bloc.select_one(".author").text.strip()
    tags = [t.text.strip() for t in bloc.select("a.tag")]
    citations.append({"texte": texte, "auteur": auteur, "tags": tags})

# ------------------------------------------------------------
# Sauvegarde JSON (ensure_ascii=False pour garder les accents/guillemets)
# ------------------------------------------------------------
with open("citations.json", "w", encoding="utf-8") as f:
    json.dump(citations, f, ensure_ascii=False, indent=2)

print(f"{len(citations)} citations -> citations.json")

# ------------------------------------------------------------
# Bonus : l'auteur qui revient le plus souvent
# ------------------------------------------------------------
auteurs = Counter(c["auteur"] for c in citations)
top_auteur, nb = auteurs.most_common(1)[0]
print(f"Auteur le plus présent : {top_auteur} ({nb} citations)")