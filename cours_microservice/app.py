# ============================================================
# app.py — Le micro-service complet
# ============================================================
# Combine tout ce qu'on a vu : auth, validation, plusieurs
# endpoints metier, logs, healthcheck, page d'accueil.
#
# Lancement local :   python app.py
# Lancement prod :    gunicorn app:app
# ============================================================

import os
import logging
from functools import wraps
from datetime import datetime

from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN", "dev-token-change-me")
DEBUG = os.getenv("FLASK_DEBUG", "false").lower() == "true"

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger(__name__)

app = Flask(__name__)

# Compteur en memoire (juste pour la demo). En vrai : Redis ou DB.
COMPTEUR = {"appels": 0, "last_call": None}


# ============================================================
# Decorateur d'authentification
# ============================================================
def require_token(view):
    @wraps(view)
    def wrapper(*args, **kwargs):
        header = request.headers.get("Authorization", "")
        if not header.startswith("Bearer "):
            return jsonify({"error": "Bearer token requis"}), 401
        if header.removeprefix("Bearer ").strip() != API_TOKEN:
            log.warning("Tentative d'acces avec un token invalide")
            return jsonify({"error": "token invalide"}), 401
        return view(*args, **kwargs)
    return wrapper


# ============================================================
# Page d'accueil — petite UI de monitoring
# ============================================================
@app.route("/")
def home():
    return render_template("home.html", compteur=COMPTEUR)


@app.route("/health")
def health():
    log.debug("Ceci est un debug")
    log.info("Ceci est une info")
    log.warning("Ceci est un warning")
    log.error("Ceci est une erreur")
    return jsonify({"status": "ok", "timestamp": datetime.now().isoformat()})


# ============================================================
# ENDPOINT 1 — Scorer un lead
# ============================================================
@app.route("/api/lead/score", methods=["POST"])
@require_token
def score_lead():
    data = request.get_json(silent=True) or {}

    nom = data.get("nom", "").strip()
    email = data.get("email", "").strip().lower()
    budget = data.get("budget", 0)

    if not nom or "@" not in email:
        return jsonify({"error": "nom et email valides requis"}), 400
    if not isinstance(budget, (int, float)) or budget < 0:
        return jsonify({"error": "budget invalide"}), 400

    score = 0
    if not any(d in email for d in ["@gmail", "@yahoo", "@hotmail"]):
        score += 30
    if budget >= 10000:
        score += 50
    elif budget >= 1000:
        score += 20
    if len(nom.split()) >= 2:
        score += 20

    score = min(score, 100)
    log.info("Lead score : %s (%s) -> %s", nom, email, score)

    _bump()
    return jsonify({"score": score, "qualifie": score >= 50})


# ============================================================
# ENDPOINT 2 — Nettoyer / normaliser des emails en masse
# ============================================================
@app.route("/api/emails/clean", methods=["POST"])
@require_token
def clean_emails():
    data = request.get_json(silent=True) or {}
    emails = data.get("emails", [])

    if not isinstance(emails, list):
        return jsonify({"error": "'emails' doit etre une liste"}), 400

    valides, invalides = [], []
    pour_dedup = set()

    for raw in emails:
        if not isinstance(raw, str):
            invalides.append(raw)
            continue
        clean = raw.strip().lower()
        if "@" not in clean or "." not in clean:
            invalides.append(raw)
            continue
        if clean in pour_dedup:
            continue
        pour_dedup.add(clean)
        valides.append(clean)

    _bump()
    return jsonify({
        "valides": valides,
        "invalides": invalides,
        "nb_traite": len(emails),
        "nb_valides": len(valides),
        "nb_doublons_supprimes": len(emails) - len(valides) - len(invalides),
    })


# ============================================================
# ENDPOINT 3 — Calculer une statistique a la volee
# ============================================================
@app.route("/api/stats", methods=["POST"])
@require_token
def stats():
    data = request.get_json(silent=True) or {}
    nombres = data.get("nombres", [])

    if not isinstance(nombres, list) or not all(isinstance(n, (int, float)) for n in nombres):
        return jsonify({"error": "'nombres' doit etre une liste de nombres"}), 400

    if not nombres:
        return jsonify({"error": "liste vide"}), 400

    nombres_tries = sorted(nombres)
    n = len(nombres_tries)
    mediane = (
        nombres_tries[n // 2] if n % 2 else
        (nombres_tries[n // 2 - 1] + nombres_tries[n // 2]) / 2
    )

    _bump()
    return jsonify({
        "count": n,
        "min": min(nombres),
        "max": max(nombres),
        "moyenne": sum(nombres) / n,
        "mediane": mediane,
    })


# ============================================================
# Helpers
# ============================================================
def _bump():
    COMPTEUR["appels"] += 1
    COMPTEUR["last_call"] = datetime.now().isoformat(timespec="seconds")


# ============================================================
# Lancement
# ============================================================
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=DEBUG)
