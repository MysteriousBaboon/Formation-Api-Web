# ============================================================
# app.py — Troc'Quartier : "Proposer un objet" (corrigé)
# ============================================================
# Logique identique au starter : c'est le TEMPLATE qui change
# (templates/index.html accessible). La validation reste AUSSI
# côté serveur (on ne fait jamais confiance au seul navigateur).
#
# Lancement :  python app.py   ->  http://localhost:5013
# ============================================================

import re
from flask import Flask, request, render_template

app = Flask(__name__)

CATEGORIES = ["Bricolage", "Cuisine", "Camping", "Jardin", "Autre"]
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def valider(form):
    erreurs = {}
    if not form.get("nom", "").strip():
        erreurs["nom"] = "Le nom de l'objet est obligatoire."
    if form.get("categorie") not in CATEGORIES:
        erreurs["categorie"] = "Choisis une catégorie dans la liste."
    email = form.get("email", "").strip()
    if not EMAIL_RE.match(email):
        erreurs["email"] = "L'email de contact n'est pas valide (ex. prenom@domaine.fr)."
    if not form.get("consentement"):
        erreurs["consentement"] = "Tu dois accepter d'être contacté pour publier (RGPD)."
    return erreurs


@app.route("/", methods=["GET", "POST"])
def proposer():
    erreurs, valeurs, succes = {}, {}, False
    if request.method == "POST":
        valeurs = request.form
        erreurs = valider(request.form)
        succes = not erreurs
    return render_template(
        "index.html",
        categories=CATEGORIES,
        erreurs=erreurs,
        valeurs=valeurs,
        succes=succes,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5013, debug=True)
