# ============================================================
# blueprints/ml.py — Cours « Machine Learning »
# ============================================================
# k-NN sur Iris : prédiction, évaluation, frontière de décision.
# ============================================================

from flask import Blueprint, request, jsonify, send_file

from common.charts import fig_to_png
from common import models

bp = Blueprint("ml", __name__)


@bp.route("/api/ml/iris", methods=["POST"])
def predire_iris():
    """Prédit l'espèce d'un iris à partir de ses 4 mesures."""
    data = request.get_json(silent=True) or {}
    features = data.get("features")
    if not isinstance(features, list) or len(features) != 4 \
            or not all(isinstance(x, (int, float)) for x in features):
        return jsonify({"error": "'features' doit être une liste de 4 nombres"}), 400

    bundle = models.iris_knn()
    classe = int(bundle["modele"].predict([features])[0])
    return jsonify({
        "features": features,
        "feature_names": bundle["feature_names"],
        "espece": bundle["target_names"][classe],
        "classe": classe,
    })


@bp.route("/api/ml/evaluate")
def evaluer():
    """Renvoie accuracy, matrice de confusion et rapport de classification."""
    return jsonify(models.iris_evaluate())


@bp.route("/api/ml/boundary.png")
def boundary():
    """Image PNG de la frontière de décision (2 features)."""
    return send_file(fig_to_png(models.iris_boundary_figure()), mimetype="image/png")
