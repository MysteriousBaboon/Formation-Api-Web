# ============================================================
# blueprints/web_api.py — Cours « API & requêtes HTTP »
# ============================================================
# Consommer des API externes avec requests (GitHub, dummyjson)
# + une mini-API JSON maison (l'heure).
# ============================================================

import logging
from datetime import datetime

import requests
from flask import Blueprint, request, jsonify

log = logging.getLogger(__name__)

bp = Blueprint("web_api", __name__)

GITHUB = "https://api.github.com"
DUMMYJSON = "https://dummyjson.com"


@bp.route("/api/web/heure")
def heure():
    """Le « hello world » d'une API : renvoie l'heure courante en JSON."""
    maintenant = datetime.now()
    return jsonify({
        "heure": maintenant.strftime("%H:%M:%S"),
        "date": maintenant.strftime("%d-%m-%Y"),
        "iso": maintenant.isoformat(timespec="seconds"),
    })


@bp.route("/api/web/github")
def github():
    """Renvoie le profil GitHub d'un utilisateur + son top 5 de dépôts."""
    user = (request.args.get("user") or "").strip()
    if not user:
        return jsonify({"error": "paramètre 'user' requis"}), 400

    try:
        r_user = requests.get(f"{GITHUB}/users/{user}", timeout=10)
        if r_user.status_code == 404:
            return jsonify({"error": f"utilisateur '{user}' introuvable"}), 404
        r_user.raise_for_status()
        infos = r_user.json()

        r_repos = requests.get(
            f"{GITHUB}/users/{user}/repos",
            params={"per_page": 100}, timeout=10,
        )
        r_repos.raise_for_status()
        repos = r_repos.json()
    except requests.RequestException as exc:
        log.error("Erreur API GitHub : %s", exc)
        return jsonify({"error": f"échec API GitHub : {exc}"}), 502

    top = sorted(repos, key=lambda r: r.get("stargazers_count", 0), reverse=True)[:5]
    return jsonify({
        "login": infos.get("login"),
        "nom": infos.get("name"),
        "bio": infos.get("bio"),
        "followers": infos.get("followers"),
        "depots_publics": infos.get("public_repos"),
        "top_depots": [
            {"nom": r["name"], "etoiles": r["stargazers_count"],
             "description": r.get("description")}
            for r in top
        ],
    })


@bp.route("/api/web/catalogue")
def catalogue():
    """Recherche de produits via l'API dummyjson — projet fil rouge."""
    q = (request.args.get("q") or "").strip()
    if not q:
        return jsonify({"error": "paramètre 'q' requis"}), 400

    try:
        r = requests.get(
            f"{DUMMYJSON}/products/search",
            params={"q": q, "limit": 12}, timeout=10,
        )
        r.raise_for_status()
        produits = r.json().get("products", [])
    except requests.RequestException as exc:
        log.error("Erreur API dummyjson : %s", exc)
        return jsonify({"error": f"échec API dummyjson : {exc}"}), 502

    return jsonify({
        "recherche": q,
        "nb_resultats": len(produits),
        "produits": [
            {"titre": p["title"], "prix": p["price"], "note": p.get("rating"),
             "categorie": p.get("category")}
            for p in produits
        ],
    })
