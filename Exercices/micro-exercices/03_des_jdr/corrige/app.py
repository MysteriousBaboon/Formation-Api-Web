# ============================================================
# app.py — Lanceur de dés JDR (corrigé)
# ============================================================
# Compétence CDA C3 : recevoir une requête, parser/valider
# l'entrée, renvoyer le bon code HTTP.
#
# Lancement :  python app.py
# Page web  :  http://localhost:5003
# ============================================================

import re
import random

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Notation type "2d6+3" :
#   group(1) = nb de dés  (chaîne vide si absent, ex "d20")
#   group(2) = nb de faces
#   group(3) = modificateur signé (None si absent)
MOTIF = re.compile(r"^(\d*)d(\d+)([+-]\d+)?$", re.IGNORECASE)

# Garde-fous : on refuse les valeurs délirantes (déni de service, page qui rame…)
MAX_DES = 100
MAX_FACES = 1000


# ------------------------------------------------------------
# Route 1 — la page d'accueil
# ------------------------------------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# ------------------------------------------------------------
# Route 2 — le moteur de dés
# ------------------------------------------------------------
@app.route("/lancer", methods=["POST"])
def lancer():
    data = request.get_json(silent=True) or {}
    notation = data.get("notation")

    # --- Validation 1 : présence + type -------------------------------
    if not isinstance(notation, str) or not notation.strip():
        return jsonify({"error": "notation requise"}), 400

    # --- Validation 2 : format (la regex fait le tri) -----------------
    m = MOTIF.match(notation.strip())
    if not m:
        return jsonify({"error": "notation invalide"}), 400

    # --- Extraction des morceaux --------------------------------------
    # "" -> 1 dé par défaut (cas "d20") ; le modificateur vaut 0 s'il manque.
    nb_des = int(m.group(1)) if m.group(1) else 1
    faces = int(m.group(2))
    modificateur = int(m.group(3)) if m.group(3) else 0

    # --- Validation 3 : bornes raisonnables ---------------------------
    if nb_des > MAX_DES or faces > MAX_FACES:
        return jsonify({"error": "valeurs trop grandes"}), 400
    if faces < 2:
        return jsonify({"error": "un dé a au moins 2 faces"}), 400
    if nb_des < 1:
        return jsonify({"error": "il faut au moins un dé"}), 400

    # --- Le lancer ----------------------------------------------------
    lances = [random.randint(1, faces) for _ in range(nb_des)]
    total = sum(lances) + modificateur

    # Détail lisible : "4 + 6 + 3" (ou "4 + 6 - 2" si modificateur négatif)
    detail = " + ".join(str(v) for v in lances)
    if modificateur > 0:
        detail += f" + {modificateur}"
    elif modificateur < 0:
        detail += f" - {abs(modificateur)}"

    return jsonify({
        "notation": notation.strip(),
        "des": nb_des,
        "faces": faces,
        "modificateur": modificateur,
        "lances": lances,
        "total": total,
        "detail": detail,
    })


# ------------------------------------------------------------
# Lancement
# ------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)
