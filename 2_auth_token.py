# ============================================================
# 2_auth_token.py — Securiser un endpoint avec un token
# ============================================================
# On ajoute un decorateur @require_token qui verifie le header
# Authorization. Si le token est faux/manquant -> 401.
#
# Test :
#   # Sans token (echec attendu)
#   curl -X POST http://127.0.0.1:5002/prive -d '{}' \
#        -H "Content-Type: application/json"
#
#   # Avec token (OK)
#   curl -X POST http://127.0.0.1:5002/prive \
#        -H "Authorization: Bearer mon-token-secret" \
#        -H "Content-Type: application/json" -d '{"x": 1}'
# ============================================================

import os
from functools import wraps
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN", "mon-token-secret")
# Valeur de fallback pour le cours, en prod on n'aurait JAMAIS de fallback.
app = Flask(__name__)


# ============================================================
# Le decorateur d'authentification
# ============================================================
def require_token(view):
    """Decorateur qui exige un token valide dans le header Authorization."""

    @wraps(view)
    def wrapper(*args, **kwargs):
        header = request.headers.get("Authorization", "")

        # Format attendu : "Bearer <token>"
        if not header.startswith("Bearer "):
            return jsonify({"error": "header Authorization manquant ou mal forme"}), 401

        token = header.removeprefix("Bearer ").strip()

        if token != API_TOKEN:
            return jsonify({"error": "token invalide"}), 401

        return view(*args, **kwargs)

    return wrapper


# ============================================================
# Un endpoint protege
# ============================================================
@app.route("/prive")
@require_token
def prive():
    data = request.get_json()
    return jsonify({"message": "Bravo, tu es authentifie", "data": data})


# ============================================================
# Un endpoint public (pas de decorateur)
# ============================================================
@app.route("/public")
def public():
    return jsonify({"message": "Tout le monde peut me voir"})


if __name__ == "__main__":
    app.run(port=5002, debug=True)
