# ============================================================
# blueprints/microservice.py — Cours « Microservice Flask »
# ============================================================
# Endpoints métier protégés par token, avec validation stricte.
# Logique reprise de cours_microservice/app.py.
# ============================================================

import logging

from flask import Blueprint, request, jsonify

from common.auth import require_token

log = logging.getLogger(__name__)

bp = Blueprint("microservice", __name__)


@bp.route("/api/lead/score", methods=["POST"])
@require_token
def score_lead():
    """Valide puis score un lead commercial."""
    data = request.get_json(silent=True) or {}
    nom = (data.get("nom") or "").strip()
    email = (data.get("email") or "").strip().lower()
    budget = data.get("budget", 0)

    if not nom or "@" not in email:
        return jsonify({"error": "nom et email valides requis"}), 400
    if not isinstance(budget, (int, float)) or budget < 0:
        return jsonify({"error": "budget invalide"}), 400

    score = 0
    if not any(d in email for d in ["@gmail", "@yahoo", "@hotmail"]):
        score += 30
    if budget >= 10000:
        score += 50
    elif budget >= 1000:
        score += 20
    if len(nom.split()) >= 2:
        score += 20

    score = min(score, 100)
    log.info("Lead scoré : %s (%s) -> %s", nom, email, score)
    return jsonify({"score": score, "qualifie": score >= 50})


@bp.route("/api/emails/clean", methods=["POST"])
@require_token
def clean_emails():
    """Normalise, valide et déduplique une liste d'emails."""
    data = request.get_json(silent=True) or {}
    emails = data.get("emails", [])
    if not isinstance(emails, list):
        return jsonify({"error": "'emails' doit être une liste"}), 400

    valides, invalides, vus = [], [], set()
    for raw in emails:
        if not isinstance(raw, str):
            invalides.append(raw)
            continue
        clean = raw.strip().lower()
        if "@" not in clean or "." not in clean:
            invalides.append(raw)
            continue
        if clean in vus:
            continue
        vus.add(clean)
        valides.append(clean)

    return jsonify({
        "valides": valides,
        "invalides": invalides,
        "nb_traite": len(emails),
        "nb_valides": len(valides),
        "nb_doublons_supprimes": len(emails) - len(valides) - len(invalides),
    })


@bp.route("/api/stats", methods=["POST"])
@require_token
def stats():
    """Statistiques descriptives sur une liste de nombres."""
    data = request.get_json(silent=True) or {}
    nombres = data.get("nombres", [])
    if not isinstance(nombres, list) or not all(isinstance(n, (int, float)) for n in nombres):
        return jsonify({"error": "'nombres' doit être une liste de nombres"}), 400
    if not nombres:
        return jsonify({"error": "liste vide"}), 400

    tries = sorted(nombres)
    n = len(tries)
    mediane = tries[n // 2] if n % 2 else (tries[n // 2 - 1] + tries[n // 2]) / 2
    return jsonify({
        "count": n,
        "min": min(nombres),
        "max": max(nombres),
        "moyenne": sum(nombres) / n,
        "mediane": mediane,
    })
