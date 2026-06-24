# ============================================================
# blueprints/deep_learning.py — Cours « Deep Learning »
# ============================================================
# Perceptron à la main (OR/AND/XOR) + MLP sur chiffres manuscrits.
# ============================================================

import random

from flask import Blueprint, request, jsonify

from common import models

bp = Blueprint("deep_learning", __name__)


@bp.route("/api/dl/perceptron", methods=["POST"])
def perceptron():
    """Entraîne un perceptron sur une fonction logique et renvoie la trace."""
    data = request.get_json(silent=True) or {}
    fonction = (data.get("fonction") or "XOR").strip()
    try:
        return jsonify(models.perceptron_logique(fonction))
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400


@bp.route("/api/dl/digit", methods=["POST"])
def digit():
    """Prédit un chiffre à partir de 64 pixels (ou un exemple aléatoire du test)."""
    data = request.get_json(silent=True) or {}
    pixels = data.get("pixels")

    bundle = models.digits_mlp()
    modele, X_test, y_test = bundle["modele"], bundle["X_test"], bundle["y_test"]

    if pixels in (None, [], ""):
        # Pas d'entrée : on tire un exemple du jeu de test pour la démo.
        idx = random.randrange(len(X_test))
        vecteur = X_test[idx]
        vrai = int(y_test[idx])
    else:
        if not isinstance(pixels, list) or len(pixels) != 64 \
                or not all(isinstance(x, (int, float)) for x in pixels):
            return jsonify({"error": "'pixels' doit être une liste de 64 nombres (0-16)"}), 400
        vecteur = pixels
        vrai = None

    proba = modele.predict_proba([vecteur])[0]
    predit = int(proba.argmax())
    return jsonify({
        "predit": predit,
        "vrai": vrai,
        "correct": (vrai == predit) if vrai is not None else None,
        "probabilites": {str(i): round(float(p), 3) for i, p in enumerate(proba)},
        "image_8x8": [[int(v) for v in vecteur[r * 8:r * 8 + 8]] for r in range(8)],
    })


@bp.route("/api/dl/accuracy")
def accuracy():
    """Précision du MLP sur le jeu de test des chiffres."""
    bundle = models.digits_mlp()
    return jsonify({
        "accuracy": bundle["accuracy"],
        "n_test": int(len(bundle["y_test"])),
        "architecture": "MLP (couches cachées 64 puis 32) sur images 8×8",
    })
