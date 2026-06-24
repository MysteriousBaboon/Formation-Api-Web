# ============================================================
# blueprints/theorie.py — Cours « Théorie Python »
# ============================================================
# Illustre fonctions + gestion d'erreurs avec une mini-calculatrice.
# ============================================================

from flask import Blueprint, request, jsonify

bp = Blueprint("theorie", __name__)

_OPS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}


@bp.route("/api/theorie/calc", methods=["POST"])
def calc():
    """Évalue 'a op b' — démonstration de fonctions et de try/except."""
    data = request.get_json(silent=True) or {}
    a = data.get("a")
    b = data.get("b")
    op = (data.get("op") or "").strip()

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return jsonify({"error": "a et b doivent être des nombres"}), 400
    if op not in _OPS:
        return jsonify({"error": f"opérateur invalide (choisir parmi {list(_OPS)})"}), 400

    try:
        resultat = _OPS[op](a, b)
    except ZeroDivisionError:
        return jsonify({"error": "division par zéro impossible"}), 400

    return jsonify({"expression": f"{a} {op} {b}", "resultat": resultat})
