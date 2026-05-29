# Corrigé exo 1 — Première tâche planifiée
import schedule
import time
from datetime import datetime


def heure_actuelle():
    print(f"Il est {datetime.now():%H:%M:%S}")


def bip():
    print("bip")


schedule.every(3).seconds.do(heure_actuelle)
schedule.every(5).seconds.do(bip)

print("Démarré. Ctrl+C pour arrêter.")
while True:
    schedule.run_pending()
    time.sleep(1)