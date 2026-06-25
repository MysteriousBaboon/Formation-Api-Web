# ============================================================
# app.py — Bureau de recrutement de héros (à DÉPLOYER)
# ============================================================
# Ce code métier est DÉJÀ écrit (repris du micro-exercice 04/09).
# Ton job dans ce mini-projet n'est PAS de le réécrire, mais de le
# METTRE EN LIGNE proprement (C10) et d'AUTOMATISER sa livraison (C11).
#
# Local      :  cp .env.example .env  puis  python app.py
# Production :  gunicorn app:app --bind 0.0.0.0:$PORT
# ============================================================

import os
import logging
from pathlib import Path
from functools import wraps

from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

# .env LOCAL uniquement (jamais committé) -> les secrets viennent de
# variables d'environnement, en local comme en prod. C'est la base de C1/ANSSI.
load_dotenv(Path(__file__).with_name(".env"))

API_TOKEN = os.getenv("API_TOKEN", "ligue-des-heros-2026")
# En prod on coupe le mode debug (sinon une erreur expose la stack au public).
DEBUG = os.getenv("FLASK_DEBUG", "false").lower() == "true"
# Render (et la plupart des hébergeurs) imposent le port via la variable PORT.
PORT = int(os.getenv("PORT", "5004"))

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

app = Flask(__name__)

# Seuils de rang : (niveau_max, nom, emoji)
RANGS = [
    (30, "Recrue", "🐣"),
    (60, "Confirmé", "🦸"),
    (90, "Élite", "⭐"),
    (100, "Légende", "👑"),
]


# ------------------------------------------------------------
# Décorateur d'authentification (Bearer token -> 401 si KO)
# ------------------------------------------------------------
def require_token(view):
    @wraps(view)
    def wrapper(*args, **kwargs):
        header = request.headers.get("Authorization", "")
        if not header.startswith("Bearer "):
            return jsonify({"error": "Bearer token requis"}), 401
        if header.removeprefix("Bearer ").strip() != API_TOKEN:
            log.warning("Tentative de recrutement avec un token invalide")
            return jsonify({"error": "token invalide"}), 401
        return view(*args, **kwargs)
    return wrapper


# ------------------------------------------------------------
# Logique métier : rang + matricule
# ------------------------------------------------------------
def rang_pour(niveau):
    for seuil, nom, emoji in RANGS:
        if niveau <= seuil:
            return nom, emoji
    return "Légende", "👑"


def matricule_pour(nom, niveau):
    lettres = "".join(c for c in nom if c.isalpha())[:3].upper() or "HRO"
    return f"{lettres}-{niveau:03d}"


# ------------------------------------------------------------
# Routes
# ------------------------------------------------------------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    # Endpoint de santé : Render et la CI s'en servent pour vérifier que
    # le service répond. Pas d'auth, réponse minimale et rapide.
    return jsonify({"status": "ok"})


@app.route("/recrue", methods=["POST"])
@require_token
def recrue():
    data = request.get_json(silent=True) or {}

    nom = data.get("nom")
    pouvoir = data.get("pouvoir")
    niveau = data.get("niveau")

    # --- Validation des entrées (400 si invalide) ---------------------
    if not isinstance(nom, str) or not nom.strip():
        return jsonify({"error": "nom requis"}), 400
    if not isinstance(pouvoir, str) or not pouvoir.strip():
        return jsonify({"error": "pouvoir requis"}), 400
    if not isinstance(niveau, int) or isinstance(niveau, bool):
        return jsonify({"error": "niveau doit être un entier"}), 400
    if not (1 <= niveau <= 100):
        return jsonify({"error": "niveau hors bornes (1 à 100)"}), 400

    rang, emoji = rang_pour(niveau)
    badge = {
        "matricule": matricule_pour(nom, niveau),
        "nom": nom.strip(),
        "pouvoir": pouvoir.strip(),
        "niveau": niveau,
        "rang": rang,
        "emoji": emoji,
    }
    log.info("Recrue enregistrée : %s (%s)", badge["nom"], badge["matricule"])
    return jsonify(badge), 200


if __name__ == "__main__":
    # Sert UNIQUEMENT au lancement local (python app.py).
    # En production, c'est gunicorn qui lance l'app (voir render.yaml).
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
