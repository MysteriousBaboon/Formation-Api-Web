# ============================================================
# app.py — Scoring de dangerosité de monstre (corrigé)
# ============================================================
# Compétence CDA C3 : logique métier explicable + validation.
# Lancement :  python app.py    (http://localhost:5005)
# ============================================================

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Régime -> bonus. Ce dict sert à la fois à VALIDER (regime in BONUS)
# et à LIRE le bonus -> une seule source de vérité.
BONUS = {"herbivore": 0, "omnivore": 5, "carnivore": 10}

# Coefficients de pondération (la force compte plus que la taille)
COEF = {"force": 4, "vitesse": 3, "taille": 2}


def stat_valide(v):
    # bool est une sous-classe de int -> on refuse True/False
    return isinstance(v, int) and not isinstance(v, bool) and 1 <= v <= 10


def niveau_pour(score):
    if score < 35:
        return "Inoffensif", "vert", "🟢"
    if score <= 65:
        return "Prudence", "orange", "🟠"
    return "DANGER", "rouge", "🔴"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/danger", methods=["POST"])
def danger():
    data = request.get_json(silent=True) or {}

    force = data.get("force")
    vitesse = data.get("vitesse")
    taille = data.get("taille")
    regime = data.get("regime")
    nom = data.get("nom") or "Inconnu"

    # --- Validation ---------------------------------------------------
    for nom_stat, valeur in [("force", force), ("vitesse", vitesse), ("taille", taille)]:
        if not stat_valide(valeur):
            return jsonify({"error": f"{nom_stat} doit être un entier de 1 à 10"}), 400
    if regime not in BONUS:
        return jsonify({"error": "regime invalide (herbivore, carnivore ou omnivore)"}), 400

    # --- Score pondéré, détaillé puis plafonné ------------------------
    detail = {
        "force": force * COEF["force"],
        "vitesse": vitesse * COEF["vitesse"],
        "taille": taille * COEF["taille"],
        "regime": BONUS[regime],
    }
    score = min(sum(detail.values()), 100)

    niveau, couleur, emoji = niveau_pour(score)

    return jsonify({
        "nom": str(nom).strip(),
        "score": score,
        "niveau": niveau,
        "couleur": couleur,
        "emoji": emoji,
        "detail": detail,
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)
