# ============================================================
# common/auth.py — Décorateur d'authentification par token
# ============================================================
# Repris du cours « microservice » : protège une route par un
# header  Authorization: Bearer <API_TOKEN>.
# ============================================================

import logging
from functools import wraps

from flask import request, jsonify

from config import config

log = logging.getLogger(__name__)


def require_token(view):
    """Refuse l'accès si le Bearer token ne correspond pas à API_TOKEN."""
    @wraps(view)
    def wrapper(*args, **kwargs):
        header = request.headers.get("Authorization", "")
        if not header.startswith("Bearer "):
            return jsonify({"error": "Bearer token requis (header Authorization)"}), 401
        if header.removeprefix("Bearer ").strip() != config.API_TOKEN:
            log.warning("Tentative d'accès avec un token invalide")
            return jsonify({"error": "token invalide"}), 401
        return view(*args, **kwargs)
    return wrapper
