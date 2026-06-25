# ============================================================
# starter.py — Lanceur de dés JDR (à compléter)
# ============================================================
# Lancement :  python starter.py   (ou renomme-le en app.py)
# Page web  :  http://localhost:5003
#
# Ton boulot : compléter l'endpoint POST /lancer.
# La page web (templates/index.html) appelle déjà cet endpoint.
# ============================================================

import re
import random

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Notation type "2d6+3" :  (nb de dés)d(nb de faces)(+/- modificateur)
MOTIF = re.compile(r"^(\d*)d(\d+)([+-]\d+)?$", re.IGNORECASE)


# ------------------------------------------------------------
# Route 1 — la page (déjà faite, ne touche pas)
# ------------------------------------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# ------------------------------------------------------------
# Route 2 — le moteur de dés (À TOI DE JOUER)
# ------------------------------------------------------------
@app.route("/lancer", methods=["POST"])
def lancer():
    data = request.get_json(silent=True) or {}
    notation = data.get("notation")

    # TODO 1 : si "notation" est absente ou n'est pas une chaîne -> 400 "notation requise"

    # TODO 2 : parser la notation avec MOTIF.match(...)
    #          si ça ne matche pas -> 400 "notation invalide"

    # TODO 3 : récupérer nb de dés (1 par défaut), faces, modificateur (0 par défaut)
    #          /!\ pense à convertir en int

    # TODO 4 : valider les bornes
    #          - dés > 100 ou faces > 1000 -> 400 "valeurs trop grandes"
    #          - faces < 2 -> 400 "un dé a au moins 2 faces"

    # TODO 5 : lancer les dés avec random.randint(1, faces), calculer le total

    # TODO 6 : renvoyer le JSON résultat (code 200)
    return jsonify({"error": "pas encore implémenté"}), 501


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)
