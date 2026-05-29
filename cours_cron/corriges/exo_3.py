# Corrigé exo 3 — APScheduler avec cron
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

compteur = {"n": 0}   # dict mutable pour modifier depuis la fonction


@sched.scheduled_job("interval", seconds=4)
def incrementer():
    compteur["n"] += 1
    print(f"Compteur : {compteur['n']}")


@sched.scheduled_job("cron", second=0)
def chaque_minute():
    print(f"[{datetime.now():%H:%M:%S}] Top minute (cron, seconde 0)")


if __name__ == "__main__":
    print("APScheduler démarré. Ctrl+C pour arrêter.")
    try:
        sched.start()
    except (KeyboardInterrupt, SystemExit):
        print("\nArrêté.")