# ============================================================
# 5_cron_vers_n8n.py — Le cron qui pousse vers n8n
# ============================================================
# LE pont avec le cours micro-service / n8n : ton script Python
# s'auto-déclenche (cron) puis ENVOIE son résultat à un webhook
# n8n, qui se charge du reste (Slack, Notion, email...).
#
# C'est le "flux inversé" vu dans integration_n8n.md :
#   Python déclenche  →  n8n distribue
#
# Lancement :   python 5_cron_vers_n8n.py
# ============================================================

import os
import time
import logging
from datetime import datetime

import requests
import schedule

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
log = logging.getLogger(__name__)

# L'URL du Webhook Trigger côté n8n (à créer dans ton workflow n8n).
# Pour tester sans n8n : crée une URL gratuite sur https://webhook.site
N8N_WEBHOOK = os.getenv(
    "N8N_WEBHOOK_URL",
    "https://webhook.site/remplace-moi",
)


def collecter_donnees():
    """Étape métier : scraping, calcul, agrégation... (simulé ici)."""
    import random
    return {
        "date": datetime.now().isoformat(timespec="seconds"),
        "nb_nouveaux_leads": random.randint(0, 15),
        "ca_jour": random.randint(500, 3000),
    }


def pousser_vers_n8n():
    """Collecte puis envoie le résultat au webhook n8n."""
    try:
        payload = collecter_donnees()
        log.info("Envoi vers n8n : %s", payload)
        r = requests.post(N8N_WEBHOOK, json=payload, timeout=10)
        log.info("Réponse n8n : %s", r.status_code)
    except requests.RequestException as e:
        log.error("Échec de l'envoi à n8n : %s", e)


# ------------------------------------------------------------
# Planification : tous les jours à 7h en prod.
# Ici toutes les 15s pour voir le résultat tout de suite.
# ------------------------------------------------------------
# schedule.every().day.at("07:00").do(pousser_vers_n8n)
schedule.every(15).seconds.do(pousser_vers_n8n)

if __name__ == "__main__":
    log.info("Démarré. Configure N8N_WEBHOOK_URL puis regarde arriver les données.")
    pousser_vers_n8n()   # un envoi immédiat pour tester
    while True:
        schedule.run_pending()
        time.sleep(1)


# ============================================================
# CÔTÉ n8n :
#   1. Crée un workflow démarrant par un nœud "Webhook" (méthode POST)
#   2. Copie l'URL générée dans la variable N8N_WEBHOOK_URL (.env)
#   3. Branche derrière : un nœud IF (ca_jour > X ?) → Slack / Email
#   4. Lance ce script : n8n reçoit les données et fait le reste
#
# Combine avec le cron système (cours.md §6) pour que ça tourne
# même quand tu n'es pas là.
# ============================================================