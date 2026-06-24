# ============================================================
# blueprints/dataviz.py — Cours « Visualisation »
# ============================================================
# Renvoie de vraies images PNG générées par matplotlib.
# Repris de cours_dataviz/5_chart_endpoint.py.
# ============================================================

import matplotlib.pyplot as plt
from flask import Blueprint, request, jsonify, send_file

from common.charts import fig_to_png

bp = Blueprint("dataviz", __name__)


@bp.route("/api/chart")
def chart_demo():
    """Graphe fixe de démonstration (test rapide au navigateur)."""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(["A", "B", "C", "D"], [10, 25, 15, 30], color="#2563eb")
    ax.set_title("Graphe de démo")
    ax.grid(axis="y", alpha=0.3)
    return send_file(fig_to_png(fig), mimetype="image/png")


@bp.route("/api/chart/build", methods=["POST"])
def chart_build():
    """Construit un graphique (bar/line/pie) à partir de données JSON."""
    data = request.get_json(silent=True) or {}
    labels = data.get("labels")
    valeurs = data.get("valeurs")
    titre = data.get("titre", "Graphique")
    type_graphe = data.get("type", "bar")

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
