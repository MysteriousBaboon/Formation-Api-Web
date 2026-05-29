# Corrigé exo 5 — Endpoint graphique (projet fil rouge)
import io
import os
from functools import wraps

import matplotlib
matplotlib.use("Agg")            # AVANT pyplot — backend sans écran
import matplotlib.pyplot as plt

from flask import Flask, request, jsonify, send_file
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
API_TOKEN = os.getenv("API_TOKEN", "dev-token-change-me")


def require_token(view):
    @wraps(view)
    def wrapper(*args, **kwargs):
        header = request.headers.get("Authorization", "")
        if header.removeprefix("Bearer ").strip() != API_TOKEN:
            return jsonify({"error": "token invalide"}), 401
        return view(*args, **kwargs)
    return wrapper


@app.route("/api/graphique", methods=["POST"])
@require_token
def graphique():
    data = request.get_json(silent=True) or {}
    labels = data.get("labels")
    valeurs = data.get("valeurs")
    titre = data.get("titre", "Graphique")
    type_graphe = data.get("type", "bar")

    if not isinstance(labels, list) or not isinstance(valeurs, list):
        return jsonify({"error": "labels et valeurs doivent être des listes"}), 400
    if not valeurs or len(labels) != len(valeurs):
        return jsonify({"error": "listes vides ou de longueurs différentes"}), 400

    fig, ax = plt.subplots(figsize=(9, 5))
    if type_graphe == "line":
        ax.plot(labels, valeurs, marker="o", color="#2563eb", linewidth=2)
        ax.grid(axis="y", alpha=0.3)
    else:  # bar par défaut
        ax.bar(labels, valeurs, color="#2563eb")
        ax.grid(axis="y", alpha=0.3)
    ax.set_title(titre, fontsize=14, fontweight="bold")

    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    buf.seek(0)
    return send_file(buf, mimetype="image/png")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6005, debug=True)