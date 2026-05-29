
# ============================================================
# 3_validation.py — Valider les donnees entrantes
# ============================================================
# Ne JAMAIS faire confiance aux donnees recues.
# Toujours verifier :
#   - le JSON est valide
#   - les champs requis sont la
#   - les types sont les bons
#   - les valeurs sont coherentes (ex: prix >= 0)
#
# Test :
#   # Manquant - erreur 400
#   curl -X POST http://127.0.0.1:5003/lead \
#        -H "Content-Type: application/json" -d '{}'
#
#   # OK
#   curl -X POST http://127.0.0.1:5003/lead \
#        -H "Content-Type: application/json" \
#        -d '{"nom": "Alice", "email": "alice@acme.com", "budget": 50000}'
# ============================================================

from flask import Flask, request, jsonify

app = Flask(__name__)


def valider_lead(data):
    """Verifie les donnees d'un lead. Retourne (data_nettoyee, erreur_str)."""

    if not isinstance(data, dict):
        return None, "le body doit etre un objet JSON"

    # Champs requis
    for champ in ["nom", "email"]:
        if not data.get(champ):
            return None, f"champ '{champ}' manquant"

    if not isinstance(data["nom"], str):
        return None, "'nom' doit etre une chaine"

    if "@" not in data["email"]:
        return None, "'email' invalide"

    # budget : optionnel mais doit etre un nombre positif si fourni
    budget = data.get("budget", 0)
    if not isinstance(budget, (int, float)):
        return None, "'budget' doit etre un nombre"
    if budget < 0:
        return None, "'budget' doit etre positif"

    return {
        "nom": data["nom"].strip(),
        "email": data["email"].strip().lower(),
        "budget": float(budget),
    }, None


def calculer_score(lead):
    """Logique metier : on score un lead sur 100."""
    score = 0

    # Email pro = +30
    if not any(domaine in lead["email"] for domaine in ["@gmail", "@yahoo", "@hotmail"]):
        score += 30

    # Budget > 10k = +50
    if lead["budget"] >= 10000:
        score += 50
    elif lead["budget"] >= 1000:
        score += 20

    # Nom complet (prenom + nom) = +20
    if len(lead["nom"].split()) >= 2:
        score += 20

    return min(score, 100)


@app.route("/lead", methods=["POST"])
def lead():
    raw = request.get_json(silent=True)

    lead_clean, erreur = valider_lead(raw)
    if erreur:
        return jsonify({"error": erreur}), 400

    score = calculer_score(lead_clean)

    return jsonify({
        "lead": lead_clean,
        "score": score,
        "qualifie": score >= 50,
    })


if __name__ == "__main__":
    app.run(port=5003, debug=True)
