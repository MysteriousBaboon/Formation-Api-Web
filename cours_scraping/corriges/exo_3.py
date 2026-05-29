# ============================================================
# Corrigé exo 3 — Top 30 Hacker News
# ============================================================
# Le HTML de HN est vieux : un post = 2 <tr> consécutives.
#   - <tr class="athing"> : rang + titre + lien
#   - le <tr> suivant      : points (.score) + auteur (.hnuser)
# ============================================================

import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://news.ycombinator.com/"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
}

response = requests.get(URL, headers=HEADERS, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

posts = []
for ligne in soup.select("tr.athing")[:30]:
    rang_txt = ligne.select_one(".rank")
    rang = int(rang_txt.text.replace(".", "")) if rang_txt else None

    a = ligne.select_one(".titleline a")
    titre = a.text.strip()
    lien = a["href"]

    # La ligne d'infos est le <tr> juste après (sibling)
    ligne_infos = ligne.find_next_sibling("tr")
    score_el = ligne_infos.select_one(".score") if ligne_infos else None
    user_el = ligne_infos.select_one(".hnuser") if ligne_infos else None

    # "120 points" -> 120 ; certains posts (annonces) n'ont pas de score
    points = int(score_el.text.split()[0]) if score_el else 0
    auteur = user_el.text.strip() if user_el else None

    posts.append({
        "rang": rang,
        "titre": titre,
        "lien": lien,
        "points": points,
        "auteur": auteur,
    })

# ------------------------------------------------------------
# Sauvegarde CSV avec pandas
# ------------------------------------------------------------
df = pd.DataFrame(posts)
df.to_csv("hn_top30.csv", index=False, encoding="utf-8")
print(f"{len(df)} posts -> hn_top30.csv")

# ------------------------------------------------------------
# Le post le plus voté
# ------------------------------------------------------------
top = df.loc[df["points"].idxmax()]
print(f"\nPlus de points : {top['titre']} ({top['points']} points, par {top['auteur']})")