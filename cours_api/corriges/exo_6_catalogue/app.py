# ============================================================
# Exo 6 — Projet fil rouge : catalogue e-commerce
# ============================================================
# Flask + API dummyjson, 2 pages (form + resultats)
#
# Lancement :
#   pip install -r requirements.txt
#   python app.py
#   -> http://127.0.0.1:5000
# ============================================================

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_BASE = "https://dummyjson.com"


# ============================================================
# Page d'accueil — le formulaire de recherche
# ============================================================
@app.route("/")
def accueil():
    return render_template("index.html")


# ============================================================
# Page de resultats
# ============================================================
@app.route("/resultats")
def resultats():
    # 1. Recuperer le terme de recherche dans l'URL : ?q=phone
    q = request.args.get("q", "").strip()
    tri = request.args.get("tri", "")        # bonus niveau 1

    if not q:
        # Si la requete est vide, on renvoie un message clair
        return render_template(
            "resultats.html",
            produits=[],
            q="",
            erreur="Tape un mot-cle pour chercher.",
        )

    # 2. Appeler l'API dummyjson
    try:
        response = requests.get(
            f"{API_BASE}/products/search",
            params={"q": q, "limit": 12},
            timeout=10,
        )
        response.raise_for_status()
        produits = response.json()["products"]
    except requests.Timeout:
        return render_template(
            "resultats.html",
            produits=[],
            q=q,
            erreur="L'API met trop de temps a repondre. Reessaie dans un instant.",
        )
    except requests.RequestException as e:
        return render_template(
            "resultats.html",
            produits=[],
            q=q,
            erreur=f"Probleme avec l'API : {e}",
        )

    # 3. Tri optionnel (bonus niveau 1)
    if tri == "prix":
        produits = sorted(produits, key=lambda p: p["price"])
    elif tri == "note":
        produits = sorted(produits, key=lambda p: p["rating"], reverse=True)

    return render_template("resultats.html", produits=produits, q=q, erreur=None)


# ============================================================
# Bonus niveau 3 — Fiche detail produit
# ============================================================
@app.route("/produit/<int:id>")
def produit(id):
    try:
        response = requests.get(f"{API_BASE}/products/{id}", timeout=10)
        if response.status_code == 404:
            return render_template("produit.html", produit=None, erreur="Produit introuvable")
        response.raise_for_status()
        produit = response.json()
    except requests.RequestException as e:
        return render_template("produit.html", produit=None, erreur=str(e))

    return render_template("produit.html", produit=produit, erreur=None)


if __name__ == "__main__":
    app.run(debug=True)
