# ============================================================
# app.py — Le fichier principal de ton application Flask
# ============================================================
# C'est ici que tu définis :
#   - les ROUTES   (quelle URL → quelle fonction)
#   - la LOGIQUE   (ce que fait chaque page)
# ============================================================

# --- ÉTAPE 1 : Importer Flask ---
# On importe les outils dont on a besoin depuis la librairie Flask
from flask import Flask, render_template, request, jsonify

# --- ÉTAPE 2 : Créer l'application ---
# __name__ dit à Flask où trouver les fichiers du projet
app = Flask(__name__)


# ============================================================
# ROUTE 1 : La page d'accueil
# ============================================================
# @app.route("/") signifie : "quand quelqu'un va sur http://127.0.0.1:5000/"
# Flask appelle la fonction juste en-dessous.

@app.route("/")
def accueil():
    """Affiche la page d'accueil."""
    # render_template() va chercher le fichier HTML dans le dossier templates/
    return render_template("accueil.html")

@app.route("/bonjour")
def bonjour():
    """Affiche la page d'accueil."""
    # render_template() va chercher le fichier HTML dans le dossier templates/
    return render_template("bonjour.html")

# ============================================================
# ROUTE 2 : Une page avec un paramètre dans l'URL
# ============================================================
# <prenom> est une variable : Flask capture ce qui est dans l'URL
# Exemple : /salut/Marie  →  prenom = "Marie"

@app.route("/salut/<prenom>")
def salut(prenom):
    """Affiche un message personnalisé avec le prénom."""
    # On passe la variable 'prenom' au template HTML
    return render_template("salut.html", prenom=prenom)


# ============================================================
# ROUTE 3 : Recevoir les données d'un formulaire
# ============================================================
# methods=["POST"] signifie que cette route accepte l'envoi de formulaire
# (par défaut, une route n'accepte que GET = afficher une page)

@app.route("/formulaire", methods=["POST"])
def traiter_formulaire():
    """Récupère le prénom envoyé par le formulaire de la page d'accueil."""
    # request.form["prenom"] récupère la valeur tapée dans le champ "prenom"
    prenom = request.form["prenom"]

    # On redirige vers la page /salut/Prénom
    return render_template("salut.html", prenom=prenom)


# ============================================================
# ROUTE 4 : Une mini API qui renvoie du JSON
# ============================================================
# Une API ne renvoie pas du HTML, mais des données (souvent en JSON).
# C'est utile pour les applis mobiles ou le JavaScript côté client.

@app.route("/api/bonjour/<prenom>")
def api_bonjour(prenom):
    """Renvoie un message de bienvenue au format JSON."""
    # jsonify() transforme un dictionnaire Python en réponse JSON
    return jsonify({
        "message": f"Bonjour {prenom} !",
        "status": "ok"
    })


# ============================================================
# LANCER LE SERVEUR
# ============================================================
# Ce bloc ne s'exécute QUE si tu lances directement ce fichier :
#   python app.py
# Il ne s'exécute PAS si le fichier est importé par un autre module.

if __name__ == "__main__":
    # debug=True → le serveur redémarre automatiquement quand tu modifies le code
    #              et affiche les erreurs en détail dans le navigateur
    # ⚠️  Ne JAMAIS laisser debug=True en production (site public) !
    app.run(debug=True)
