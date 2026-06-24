# ============================================================
# app.py — Démo « tous les cours » de La Dinguerie
# ============================================================
# Une seule application Flask qui expose, cours par cours, une
# démo interactive (dashboard HTML) + des endpoints d'API.
#
# Lancement :  python app.py    →  http://localhost:5000
# ============================================================

import importlib
import logging

from flask import Flask, render_template, abort

from config import config
from registry import COURS, get_cours

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
log = logging.getLogger(__name__)

# Modules de blueprints à charger (un par cours). On les importe de
# façon tolérante : un blueprint pas encore écrit n'empêche pas l'app
# de démarrer (il apparaît juste comme « à venir » dans le hub).
BLUEPRINTS = [
    "theorie", "web_api", "microservice", "cron", "data", "dataviz",
    "scraping", "panorama", "ml", "deep_learning", "llm", "agents",
]


def enregistrer_blueprints(app):
    """Importe et enregistre chaque blueprint disponible."""
    charges = set()
    for nom in BLUEPRINTS:
        try:
            module = importlib.import_module(f"blueprints.{nom}")
            app.register_blueprint(module.bp)
            charges.add(nom)
        except ModuleNotFoundError:
            log.warning("Blueprint « %s » absent — démos marquées « à venir ».", nom)
        except Exception as exc:  # noqa: BLE001 — on veut un démarrage robuste
            log.error("Blueprint « %s » non chargé : %s", nom, exc)
    return charges


def create_app():
    app = Flask(__name__)
    app.config["JSON_AS_ASCII"] = False  # garder les accents dans le JSON

    charges = enregistrer_blueprints(app)

    # Quels cours ont au moins un blueprint chargé ?
    # (le nom de module web_api correspond au slug « api »)
    slug_vers_module = {c["slug"]: ("web_api" if c["slug"] == "api" else c["slug"])
                        for c in COURS}

    def cours_actif(slug):
        return slug_vers_module.get(slug) in charges

    # --- Hub : liste des 12 cours ---
    @app.route("/")
    def hub():
        cours = sorted(COURS, key=lambda c: c["numero"])
        return render_template("hub.html", cours=cours, actif=cours_actif)

    # --- Page d'un cours : démos générées depuis le registre ---
    @app.route("/cours/<slug>")
    def page_cours(slug):
        cours = get_cours(slug)
        if cours is None:
            abort(404)
        return render_template(
            "cours.html",
            cours=cours,
            actif=cours_actif(slug),
            llm_pret=config.llm_pret(),
        )

    # --- Healthcheck global ---
    @app.route("/health")
    def health():
        return {"status": "ok", "blueprints": sorted(charges)}

    return app


app = create_app()


if __name__ == "__main__":
    log.info("Démo La Dinguerie sur http://localhost:%s", config.PORT)
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG)
