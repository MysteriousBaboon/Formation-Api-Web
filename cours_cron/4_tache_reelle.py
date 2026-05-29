# ============================================================
# 4_tache_reelle.py — Une vraie tâche planifiée, robuste
# ============================================================
# Le pattern complet d'un job de prod :
#   - une fonction métier
#   - du logging (pour savoir ce qui s'est passé)
#   - un try/except (une tâche qui plante ne doit PAS tuer le scheduler)
#
# Ici on simule : "récupérer un prix et alerter s'il baisse".
#
# Lancement :   python 4_tache_reelle.py
# ============================================================

import schedule
import time
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger(__name__)

SEUIL_ALERTE = 100   # on alerte si le prix passe sous ce seuil


def recuperer_prix():
    """Simule un scraping/appel API qui renvoie un prix."""
    # En vrai : requests.get(...) + BeautifulSoup, comme au cours scraping.
    import random
    return random.randint(80, 130)


def envoyer_alerte(prix):
    """Simule l'envoi (Slack, email, webhook n8n...)."""
    log.warning("ALERTE : prix bas détecté à %s € (seuil %s)", prix, SEUIL_ALERTE)


def job_surveillance():
    """La tâche planifiée. Elle gère ses propres erreurs."""
    try:
        log.info("Vérification du prix...")
        prix = recuperer_prix()
        log.info("Prix actuel : %s €", prix)
        if prix < SEUIL_ALERTE:
            envoyer_alerte(prix)
        else:
            log.info("Rien à signaler.")
    except Exception as e:
        # On log l'erreur mais on NE laisse PAS planter le scheduler.
        log.error("Le job a échoué : %s", e)


# ------------------------------------------------------------
# Planification : toutes les 10s pour la démo.
# En vrai tu mettrais : schedule.every().day.at("07:00")
# ------------------------------------------------------------
schedule.every(10).seconds.do(job_surveillance)

if __name__ == "__main__":
    log.info("Surveillance démarrée (vérif toutes les 10s). Ctrl+C pour arrêter.")
    job_surveillance()   # un premier passage immédiat
    while True:
        schedule.run_pending()
        time.sleep(1)