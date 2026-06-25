# ============================================================
# app.py — Bureau de recrutement de héros (corrigé)
# ============================================================
# Compétence CDA C3 : auth par token (401), validation (400),
# logique métier (rang + matricule), bon code HTTP.
#
# Lancement :  cp ../.env.example .env  puis  python app.py
# Page web  :  http://localhost:5004
# ============================================================

import os
import logging
from pathlib import Path
from functools import wraps

from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

# On charge le .env LOCAL (à côté de ce fichier), pas un .env qui traînerait
# plus haut dans l'arborescence -> l'exo reste auto-suffisant.
load_dotenv(Path(__file__).with_name(".env"))

API_TOKEN = os.getenv("API_TOKEN", "ligue-des-heros-2026")

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
# Décorateur d'authentification
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
    # 3 premières lettres (alpha) du nom + niveau sur 3 chiffres
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
    return jsonify({"status": "ok"})


@app.route("/recrue", methods=["POST"])
@require_token
def recrue():
    data = request.get_json(silent=True) or {}

    nom = data.get("nom")
    pouvoir = data.get("pouvoir")
    niveau = data.get("niveau")

    # --- Validation ---------------------------------------------------
    if not isinstance(nom, str) or not nom.strip():
        return jsonify({"error": "nom requis"}), 400
    if not isinstance(pouvoir, str) or not pouvoir.strip():
        return jsonify({"error": "pouvoir requis"}), 400
    # bool est une sous-classe de int -> on l'exclut explicitement
    if not isinstance(niveau, int) or isinstance(niveau, bool):
        return jsonify({"error": "niveau doit être un entier"}), 400
    if not (1 <= niveau <= 100):
        return jsonify({"error": "niveau hors bornes (1 à 100)"}), 400

    # --- Badge --------------------------------------------------------
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
    app.run(host="0.0.0.0", port=5004, debug=True)
