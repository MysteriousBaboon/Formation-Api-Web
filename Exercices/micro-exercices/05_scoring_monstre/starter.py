# ============================================================
# starter.py — Scoring de dangerosité de monstre (à compléter)
# ============================================================
# Lancement :  python starter.py
# Page web  :  http://localhost:5005
# ============================================================

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Régime -> bonus de dangerosité (sert AUSSI à valider le régime)
BONUS = {"herbivore": 0, "omnivore": 5, "carnivore": 10}


def stat_valide(v):
    """True si v est un entier entre 1 et 10."""
    # TODO : attention, True/False sont des int en Python -> les exclure
    return False


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/danger", methods=["POST"])
def danger():
    data = request.get_json(silent=True) or {}

    # TODO 1 : récupérer force, vitesse, taille, regime, nom (optionnel)
    # TODO 2 : valider les 3 stats (stat_valide) et le régime (dans BONUS) -> 400
    # TODO 3 : score = force*4 + vitesse*3 + taille*2 + BONUS[regime], plafonné à 100
    # TODO 4 : niveau/couleur/emoji selon les seuils (<35, 35-65, >65)
    # TODO 5 : renvoyer le JSON avec le detail des points

    return jsonify({"error": "pas encore implémenté"}), 501


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)
