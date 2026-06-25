# ============================================================
# starter.py — Bureau de recrutement de héros (à compléter)
# ============================================================
# Lancement :  cp .env.example .env  puis  python starter.py
# Page web  :  http://localhost:5004
# ============================================================

import os
from pathlib import Path
from functools import wraps

from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

# Charge le .env situé à côté de ce script (et pas un autre plus haut)
load_dotenv(Path(__file__).with_name(".env"))

API_TOKEN = os.getenv("API_TOKEN", "ligue-des-heros-2026")

app = Flask(__name__)

RANGS = [
    (30, "Recrue", "🐣"),
    (60, "Confirmé", "🦸"),
    (90, "Élite", "⭐"),
    (100, "Légende", "👑"),
]


# ------------------------------------------------------------
# Décorateur d'authentification (À COMPLÉTER)
# ------------------------------------------------------------
def require_token(view):
    @wraps(view)
    def wrapper(*args, **kwargs):
        # TODO : lire le header Authorization, vérifier "Bearer <token>"
        #        -> 401 si absent ou faux ; sinon laisser passer
        return view(*args, **kwargs)
    return wrapper


def rang_pour(niveau):
    """Renvoie (rang, emoji) selon le niveau."""
    for seuil, nom, emoji in RANGS:
        if niveau <= seuil:
            return nom, emoji
    return "Légende", "👑"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


# ------------------------------------------------------------
# POST /recrue (À COMPLÉTER)
# ------------------------------------------------------------
@app.route("/recrue", methods=["POST"])
@require_token
def recrue():
    data = request.get_json(silent=True) or {}
    # TODO : valider nom (str non vide), pouvoir (str non vide),
    #        niveau (int entre 1 et 100) -> 400 sinon
    # TODO : calculer rang + matricule, renvoyer le badge (200)
    return jsonify({"error": "pas encore implémenté"}), 501


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004, debug=True)
