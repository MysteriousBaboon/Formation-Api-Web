# ============================================================
# app.py — Troc'Quartier : "Proposer un objet" (version À CORRIGER)
# ============================================================
# Le code Python est correct (validation côté serveur OK).
# Le problème est dans templates/index.html : il est INACCESSIBLE.
# Ton job : corriger le TEMPLATE (voir README), pas forcément ce fichier.
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
        erreurs["categorie"] = "Choisis une catégorie."
    email = form.get("email", "").strip()
    if not EMAIL_RE.match(email):
        erreurs["email"] = "L'email de contact n'est pas valide."
    if not form.get("consentement"):
        erreurs["consentement"] = "Le consentement est requis (RGPD)."
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
