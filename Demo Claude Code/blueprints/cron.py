# ============================================================
# blueprints/cron.py — Cours « Tâches planifiées »
# ============================================================
# Antisèche cron + déclenchement manuel d'un job (au lieu de
# laisser tourner un scheduler bloquant dans le serveur web).
# Logique reprise de 3_syntaxe_cron.py et 4_tache_reelle.py.
# ============================================================

import logging
import random
from datetime import datetime

from flask import Blueprint, request, jsonify

log = logging.getLogger(__name__)

bp = Blueprint("cron", __name__)

EXPRESSIONS = {
    "* * * * *":      "Toutes les minutes",
    "0 7 * * *":      "Tous les jours à 7h00",
    "30 6 * * *":     "Tous les jours à 6h30",
    "*/15 * * * *":   "Toutes les 15 minutes",
    "0 * * * *":      "Au début de chaque heure",
    "0 9 * * 1":      "Tous les lundis à 9h00",
    "0 9 * * 1-5":    "Du lundi au vendredi à 9h00",
    "0 8-18 * * 1-5": "Chaque heure de 8h à 18h, en semaine",
    "0 0 1 * *":      "Le 1er de chaque mois à minuit",
    "0 0 * * 0":      "Tous les dimanches à minuit",
}

SEUIL_ALERTE = 100


@bp.route("/api/cron/expressions")
def expressions():
    """Renvoie l'antisèche des expressions cron."""
    return jsonify({
        "format": "minute heure jour_du_mois mois jour_semaine",
        "aide": "https://crontab.guru",
        "exemples": [{"expression": e, "signification": s}
                     for e, s in EXPRESSIONS.items()],
    })


def _job_surveillance():
    """Tâche de prod simulée : vérifie un prix et alerte s'il baisse."""
    prix = random.randint(80, 130)
    alerte = prix < SEUIL_ALERTE
    if alerte:
        log.warning("ALERTE : prix bas détecté à %s € (seuil %s)", prix, SEUIL_ALERTE)
    else:
        log.info("Prix actuel : %s € — rien à signaler.", prix)
    return {
        "job": "surveillance",
        "execute_a": datetime.now().isoformat(timespec="seconds"),
        "prix": prix,
        "seuil": SEUIL_ALERTE,
        "alerte": alerte,
        "message": (f"Prix bas ({prix} €) sous le seuil de {SEUIL_ALERTE} €"
                    if alerte else f"Prix normal ({prix} €)"),
    }


JOBS = {"surveillance": _job_surveillance}


@bp.route("/api/cron/trigger", methods=["POST"])
def trigger():
    """Exécute immédiatement un job planifié (déclenchement manuel)."""
    data = request.get_json(silent=True) or {}
    nom = (data.get("job") or "surveillance").strip()
    if nom not in JOBS:
        return jsonify({"error": f"job inconnu (disponibles : {list(JOBS)})"}), 400
    try:
        resultat = JOBS[nom]()
    except Exception as exc:  # un job qui plante ne doit pas tuer le service
        log.error("Le job '%s' a échoué : %s", nom, exc)
        return jsonify({"error": f"le job a échoué : {exc}"}), 500
    return jsonify(resultat)
