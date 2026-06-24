# ============================================================
# blueprints/panorama.py — Cours « Panorama de l'IA »
# ============================================================
# Cours théorique : on l'expose en « vitrine » en servant le
# GLOSSAIRE.md de la formation, parsé en JSON structuré.
# ============================================================

import logging
import re
from pathlib import Path

from flask import Blueprint, request, jsonify

log = logging.getLogger(__name__)

bp = Blueprint("panorama", __name__)

GLOSSAIRE = Path(__file__).resolve().parent.parent.parent / "GLOSSAIRE.md"

# Entrée type :  - **Terme** — Définition. _(Tag1, Tag2)_
_ENTREE = re.compile(r"^-\s+\*\*(.+?)\*\*\s+[—-]\s+(.*?)\s*(?:_\((.+?)\)_)?\s*$")


def _charger_glossaire():
    """Parse le GLOSSAIRE.md en sections -> liste d'entrées."""
    if not GLOSSAIRE.exists():
        return {}
    sections = {}
    courante = None
    for ligne in GLOSSAIRE.read_text(encoding="utf-8").splitlines():
        if ligne.startswith("## "):
            courante = ligne[3:].strip()
            sections[courante] = []
        elif courante:
            m = _ENTREE.match(ligne.strip())
            if m:
                sections[courante].append({
                    "terme": m.group(1),
                    "definition": m.group(2),
                    "tags": [t.strip() for t in (m.group(3) or "").split(",") if t.strip()],
                })
    # On ne garde que les sections qui contiennent des entrées.
    return {k: v for k, v in sections.items() if v}


@bp.route("/api/panorama/glossaire")
def glossaire():
    """Renvoie le glossaire de la formation, avec filtre texte optionnel."""
    sections = _charger_glossaire()
    if not sections:
        return jsonify({"error": "GLOSSAIRE.md introuvable"}), 404

    q = (request.args.get("q") or "").strip().lower()
    if q:
        filtre = {}
        for section, entrees in sections.items():
            gardees = [e for e in entrees
                       if q in e["terme"].lower() or q in e["definition"].lower()]
            if gardees:
                filtre[section] = gardees
        sections = filtre

    total = sum(len(v) for v in sections.values())
    return jsonify({
        "filtre": q or None,
        "nb_sections": len(sections),
        "nb_termes": total,
        "sections": sections,
    })
