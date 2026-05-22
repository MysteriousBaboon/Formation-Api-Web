# ============================================================
# 4_anti_bot.py — Quand le site bloque les bots
# ============================================================
# Beaucoup de sites refusent les requetes "non navigateur".
# Trois techniques pour ressembler a un vrai utilisateur :
#   1. User-Agent realiste
#   2. Pauses entre requetes
#   3. Session (cookies + connexion reutilisee)
# ============================================================

import requests
from bs4 import BeautifulSoup
import time


# ============================================================
# Test : Hacker News (assez tolerant mais respecte robots.txt)
# ============================================================
URL = "https://news.ycombinator.com/"


# ============================================================
# 1. SANS headers : ca peut marcher... ou pas
# ============================================================
response_brut = requests.get(URL, timeout=10)
print(f"Sans header : {response_brut.status_code}")


# ============================================================
# 2. AVEC un User-Agent realiste
# ============================================================
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 1.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "fr-FR,fr;q=0.9,en;q=0.8",
}

response = requests.get(URL, headers=headers, timeout=10)
print(f"Avec header : {response.status_code}")


# ============================================================
# 3. Parser et extraire les top news
# ============================================================
soup = BeautifulSoup(response.text, "html.parser")

# Chaque post sur HN est dans <tr class="athing">
posts = soup.select("tr.athing")

print(f"\n{len(posts)} posts trouves\n")
print("Top 10 Hacker News :\n")

for i, post in enumerate(posts[:10], 1):
    # Le titre est dans <span class="titleline"> > <a>
    a = post.select_one(".titleline a")
    titre = a.text
    lien = a["href"]
    print(f"{i:2}. {titre}")
    print(f"    {lien}\n")


# ============================================================
# 4. Session — utile si tu fais BEAUCOUP de requetes
# ============================================================
# Une Session reutilise la meme connexion TCP (plus rapide)
# et garde les cookies entre les appels (utile si tu te connectes).

session = requests.Session()
session.headers.update(headers)

for i in range(3):
    r = session.get(URL, timeout=10)
    print(f"Appel {i + 1} : {r.status_code}")
    time.sleep(1)        # JAMAIS sans sleep en boucle


# ============================================================
# 5. robots.txt — l'ethique du scraper
# ============================================================
# Avant de scraper massivement, lis le fichier robots.txt :
#   https://news.ycombinator.com/robots.txt
#
# Il liste ce que les bots ne devraient PAS scraper.
# Ce n'est pas legalement contraignant en France, mais c'est
# une bonne pratique. Et si le site liste un "Crawl-delay",
# respecte-le.

robots = requests.get("https://news.ycombinator.com/robots.txt").text
print("\n--- robots.txt de HN ---")
print(robots)


# ============================================================
# 6. Quand tu te fais bloquer quand meme...
# ============================================================
# - Code 403 ou 429 : trop de requetes, ralentis (sleep plus long)
# - Code 503 : le site detecte les bots, essaie Playwright
# - CAPTCHA : abandonne, c'est non. Negocie une API avec eux.
# ============================================================
