# ============================================================
# 5_chart_endpoint.py — Un endpoint Flask qui renvoie un PNG
# ============================================================
# LE pont avec le cours micro-service : ton API ne renvoie plus
# du JSON mais une vraie IMAGE de graphique. n8n peut appeler
# cet endpoint et poster le résultat dans Slack chaque matin.
#
# Lancement :   python 5_chart_endpoint.py
# Test image :  ouvre http://127.0.0.1:5001/api/chart dans le navigateur
# Test POST  :  voir la commande curl en bas du fichier
# ============================================================

import io
import os

# /!\ ORDRE IMPORTANT : on choisit le backend "Agg" (sans écran)
# AVANT d'importer pyplot, sinon ça plante sur un serveur.
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from flask import Flask, request, jsonify, send_file

app = Flask(__name__)
API_TOKEN = os.getenv("API_TOKEN", "dev-token-change-me")


def require_token(view):
    # Même décorateur que dans le cours micro-service.
    from functools import wraps

    @wraps(view)
    def wrapper(*args, **kwargs):
        header = request.headers.get("Authorization", "")
        if header.removeprefix("Bearer ").strip() != API_TOKEN:
            return jsonify({"error": "token invalide"}), 401
        return view(*args, **kwargs)
    return wrapper


def fig_to_png(fig):
    """Transforme une figure matplotlib en buffer PNG en mémoire (pas de fichier)."""
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=150, bbox_inches="tight")
    plt.close(fig)       # libère la mémoire — crucial sur un serveur
    buf.seek(0)          # on se replace au début du buffer
    return buf


# ------------------------------------------------------------
# 1. Endpoint démo : un graphe fixe (test rapide au navigateur)
# ------------------------------------------------------------
@app.route("/api/chart")
def chart_demo():
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(["A", "B", "C", "D"], [10, 25, 15, 30], color="#2563eb")
    ax.set_title("Graphe de démo")
    return send_file(fig_to_png(fig), mimetype="image/png")


# ------------------------------------------------------------
# 2. Endpoint réel : on envoie les données en POST, on reçoit l'image
# ------------------------------------------------------------
# Body attendu :
# {
#   "titre": "Ventes Q1",
#   "labels": ["Jan", "Fev", "Mar"],
#   "valeurs": [100, 130, 90],
#   "type": "bar"          // "bar", "line" ou "pie"
# }
@app.route("/api/chart/build", methods=["POST"])
@require_token
def chart_build():
    data = request.get_json(silent=True) or {}

    labels = data.get("labels")
    valeurs = data.get("valeurs")
    titre = data.get("titre", "Graphique")
    type_graphe = data.get("type", "bar")

    # Validation (réflexe du cours micro-service)
    if not isinstance(labels, list) or not isinstance(valeurs, list):
        return jsonify({"error": "'labels' et 'valeurs' doivent être des listes"}), 400
    if len(labels) != len(valeurs):
        return jsonify({"error": "labels et valeurs doivent avoir la même longueur"}), 400
    if not valeurs:
        return jsonify({"error": "listes vides"}), 400

    fig, ax = plt.subplots(figsize=(9, 5))

    if type_graphe == "line":
        ax.plot(labels, valeurs, marker="o", color="#2563eb", linewidth=2)
    elif type_graphe == "pie":
        ax.pie(valeurs, labels=labels, autopct="%1.0f%%")
    else:  # bar par défaut
        ax.bar(labels, valeurs, color="#2563eb")

    ax.set_title(titre, fontsize=14, fontweight="bold")
    if type_graphe != "pie":
        ax.grid(axis="y", alpha=0.3)

    return send_file(fig_to_png(fig), mimetype="image/png")


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)


# ============================================================
# TESTER L'ENDPOINT POST (récupère l'image dans graphe.png) :
#
#   curl -X POST http://127.0.0.1:5001/api/chart/build \
#     -H "Authorization: Bearer dev-token-change-me" \
#     -H "Content-Type: application/json" \
#     -d '{"titre":"Ventes Q1","labels":["Jan","Fev","Mar"],"valeurs":[100,130,90],"type":"bar"}' \
#     --output graphe.png
#
# Dans n8n : nœud HTTP Request → POST cette URL → le binaire image
# peut être branché direct sur un nœud Slack / Email en pièce jointe.
# ============================================================