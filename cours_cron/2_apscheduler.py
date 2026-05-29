# ============================================================
# 2_apscheduler.py — Planifier avec APScheduler (robuste)
# ============================================================
# APScheduler gère le cron, les fuseaux horaires, plusieurs
# tâches en parallèle. C'est le choix "sérieux".
#
# Lancement :   python 2_apscheduler.py
# Arrêt :       Ctrl+C
# ============================================================

from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


# ------------------------------------------------------------
# 1. Déclencheur 'interval' : toutes les X secondes/minutes
# ------------------------------------------------------------
@sched.scheduled_job("interval", seconds=5)
def toutes_les_5s():
    print(f"[{datetime.now():%H:%M:%S}] interval : toutes les 5 secondes")


# ------------------------------------------------------------
# 2. Déclencheur 'cron' : à une heure précise
# ------------------------------------------------------------
@sched.scheduled_job("cron", hour=7, minute=0)
def chaque_matin():
    print(f"[{datetime.now():%H:%M:%S}] cron : tous les jours à 7h00")


# ------------------------------------------------------------
# 3. cron avec jour de la semaine (mon, tue, wed... ou 0-6)
# ------------------------------------------------------------
@sched.scheduled_job("cron", day_of_week="mon-fri", hour="9-18")
def heures_ouvrees():
    print(f"[{datetime.now():%H:%M:%S}] cron : chaque heure ouvrée (lun-ven, 9h-18h)")


# ------------------------------------------------------------
# 4. Lancer le planificateur (bloque le programme)
# ------------------------------------------------------------
if __name__ == "__main__":
    print("APScheduler démarré. Ctrl+C pour arrêter.\n")
    try:
        sched.start()
    except (KeyboardInterrupt, SystemExit):
        print("\nPlanificateur arrêté.")