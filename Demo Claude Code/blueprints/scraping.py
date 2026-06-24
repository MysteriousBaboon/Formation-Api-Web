# ============================================================
# blueprints/scraping.py — Cours « Web scraping »
# ============================================================
# Reprend la logique de cours_scraping/2_beautifulsoup.py et
# 3_pagination.py : requests + BeautifulSoup sur books.toscrape.com.
# ============================================================

import logging
import re

import requests
from bs4 import BeautifulSoup
from flask import Blueprint, request, jsonify

log = logging.getLogger(__name__)

bp = Blueprint("scraping", __name__)

BASE = "https://books.toscrape.com/catalogue/"
MAX_PAGES = 5  # garde-fou : on ne matraque pas le site


def scraper_page(numero):
    """Scrape une page et retourne la liste des livres (None si 404)."""
    url = f"{BASE}page-{numero}.html"
    reponse = requests.get(url, timeout=10)
    if reponse.status_code == 404:
        return None
    reponse.raise_for_status()
    reponse.encoding = "utf-8"  # évite le « Â£ » sur le symbole livre
    soup = BeautifulSoup(reponse.text, "html.parser")

    livres = []
    for article in soup.select("article.product_pod"):
        prix_texte = article.select_one(".price_color").text
        # On extrait le nombre, peu importe le symbole monétaire parasite.
        match = re.search(r"\d+\.\d+", prix_texte)
        livres.append({
            "titre": article.h3.a["title"],
            "prix": float(match.group()) if match else 0.0,
            "dispo": article.select_one(".availability").text.strip(),
            "note": article.select_one(".star-rating")["class"][1],
        })
    return livres


@bp.route("/api/scrape/books")
def scrape_books():
    """Scrape N pages de books.toscrape.com et renvoie les livres en JSON."""
    try:
        pages = int(request.args.get("pages", 1))
    except (TypeError, ValueError):
        return jsonify({"error": "'pages' doit être un entier"}), 400

    pages = max(1, min(pages, MAX_PAGES))

    tous = []
    for page in range(1, pages + 1):
        try:
            livres = scraper_page(page)
        except requests.RequestException as exc:
            log.error("Erreur de scraping page %s : %s", page, exc)
            return jsonify({"error": f"échec réseau page {page}: {exc}"}), 502
        if livres is None:
            break
        tous.extend(livres)

    prix_moyen = round(sum(l["prix"] for l in tous) / len(tous), 2) if tous else 0
    return jsonify({
        "source": "https://books.toscrape.com/",
        "pages_scrapees": pages,
        "nb_livres": len(tous),
        "prix_moyen": prix_moyen,
        "livres": tous,
    })
