# ============================================================
# 1_schedule_simple.py — Planifier avec la lib 'schedule'
# ============================================================
# 'schedule' est la façon la plus LISIBLE de planifier en Python.
# On décrit la tâche en quasi-anglais, puis une boucle la fait vivre.
#
# Lancement :   python 1_schedule_simple.py
# Arrêt :       Ctrl+C
# ============================================================

import schedule
import time
from datetime import datetime


def saluer():
    print(f"[{datetime.now():%H:%M:%S}] Bonjour ! La tâche tourne.")


def rapport():
    print(f"[{datetime.now():%H:%M:%S}] (rapport quotidien simulé)")


# ------------------------------------------------------------
# 1. Déclarer les planifications (en quasi-anglais)
# ------------------------------------------------------------
schedule.every(5).seconds.do(saluer)            # toutes les 5 secondes
schedule.every().day.at("07:00").do(rapport)    # tous les jours à 7h00
# schedule.every().monday.do(rapport)           # tous les lundis
# schedule.every().hour.do(saluer)              # toutes les heures
# schedule.every(10).minutes.do(saluer)         # toutes les 10 minutes

print("Planificateur démarré. La tâche 'saluer' s'exécute toutes les 5s.")
print("Ctrl+C pour arrêter.\n")

# ------------------------------------------------------------
# 2. La boucle qui fait vivre le planificateur (OBLIGATOIRE)
# ------------------------------------------------------------
# schedule ne tourne pas en arrière-plan : il faut appeler
# run_pending() régulièrement pour qu'il lance les tâches dues.
while True:
    schedule.run_pending()   # exécute ce qui est dû maintenant
    time.sleep(1)           # on respire 1 seconde entre 2 vérifications