# Corrigé exo 4 — Le job complet (surveillance + alerte)
import random
import time
import logging

import schedule
import requests   # pour le bonus

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger(__name__)

SEUIL = 5
WEBHOOK = None   # mets une URL https://webhook.site pour activer le bonus


def verifier_stock():
    try:
        stock = random.randint(0, 20)
        if stock < SEUIL:
            log.warning("Rupture imminente : stock = %s", stock)
            if WEBHOOK:
                requests.post(WEBHOOK, json={"alerte": "stock_bas", "stock": stock}, timeout=10)
        else:
            log.info("Stock OK : %s", stock)
    except Exception as e:
        log.error("Le job a échoué : %s", e)


schedule.every(8).seconds.do(verifier_stock)

if __name__ == "__main__":
    log.info("Surveillance du stock démarrée (toutes les 8s). Ctrl+C pour arrêter.")
    verifier_stock()
    while True:
        schedule.run_pending()
        time.sleep(1)