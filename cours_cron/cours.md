# 📚 Cours — Planification & automatisation

> Un script que tu dois lancer à la main n'est pas automatisé. Ce module rend ton code autonome : il s'exécute tout seul, à l'heure que tu décides.

---

## 1. Le problème

Tu as un script qui scrape des prix, génère un graphe, ou nettoie une base. Super. Mais :

- Tu dois **penser** à le lancer
- Tu dois **avoir ton PC allumé** au bon moment
- Tu **oublies** un jour sur deux

L'automatisation, c'est dire une fois pour toutes : *"exécute ça tous les jours à 7h"*, et ne plus jamais y toucher.

---

## 2. Les approches

| Approche | Pour quoi | Niveau |
|---|---|---|
| **schedule** (lib Python) | Tâches simples, lisible | Facile |
| **APScheduler** (lib Python) | Cron, persistance, robuste | Moyen |
| **cron** (système Linux/Mac) | Standard, indépendant de Python | Moyen |
| **n8n / cloud** | No-code, tourne sans ton PC | Facile |

**Règle :** pour apprendre et pour un PC qui tourne, `schedule`/`APScheduler`. Pour de la prod
qui doit tourner même PC éteint → cron sur un serveur, ou un Schedule Trigger n8n.

---

## 3. La lib `schedule` — la plus lisible

```python
import schedule
import time

def ma_tache():
    print("Je m'exécute !")

schedule.every(10).seconds.do(ma_tache)      # toutes les 10 secondes
schedule.every().day.at("07:00").do(ma_tache)  # tous les jours à 7h
schedule.every().monday.do(ma_tache)         # tous les lundis

# La boucle qui fait vivre le planificateur :
while True:
    schedule.run_pending()   # lance les tâches dues
    time.sleep(1)            # respire 1 seconde
```

Le `while True` est **obligatoire** : `schedule` ne tourne pas en arrière-plan tout seul,
il faut un programme vivant qui appelle `run_pending()` régulièrement.

---

## 4. APScheduler — plus robuste

`schedule` est mignon mais limité. **APScheduler** gère le cron, les fuseaux horaires,
plusieurs tâches en parallèle, et peut reprendre après un crash.

```python
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job("interval", seconds=10)
def tache_intervalle():
    print("Toutes les 10s")

@sched.scheduled_job("cron", hour=7, minute=0)
def tache_quotidienne():
    print("Tous les jours à 7h00")

sched.start()   # bloque et fait tourner le planificateur
```

Deux types de déclencheurs :
- **`interval`** : toutes les X secondes/minutes/heures
- **`cron`** : "à telle heure tel jour" (comme le cron système)

---

## 5. La syntaxe cron (à connaître absolument)

cron est le standard d'Unix. 5 champs séparés par des espaces :

```
┌───── minute        (0-59)
│ ┌───── heure        (0-23)
│ │ ┌───── jour du mois (1-31)
│ │ │ ┌───── mois         (1-12)
│ │ │ │ ┌───── jour semaine (0-6, 0 = dimanche)
│ │ │ │ │
* * * * *
```

Le `*` veut dire "toutes les valeurs". Exemples :

| Expression | Sens |
|---|---|
| `* * * * *` | Toutes les minutes |
| `0 7 * * *` | Tous les jours à 7h00 |
| `*/15 * * * *` | Toutes les 15 minutes |
| `0 9 * * 1` | Tous les lundis à 9h00 |
| `0 0 1 * *` | Le 1er de chaque mois à minuit |
| `0 8-18 * * 1-5` | Toutes les heures de 8h à 18h, lun→ven |

> 💡 Le site [crontab.guru](https://crontab.guru) traduit n'importe quelle expression en français.

---

## 6. Le cron système (Linux / Mac)

Indépendant de Python : le système lance ton script même si rien ne tourne.

```bash
crontab -e          # éditer ses tâches cron
crontab -l          # lister ses tâches
```

Une ligne = une expression cron + la commande :

```
0 7 * * * /usr/bin/python3 /home/mark/mon_script.py >> /home/mark/log.txt 2>&1
```

- Chemins **absolus** obligatoires (cron ne connaît pas ton `cd`)
- `>> log.txt 2>&1` : redirige sortie + erreurs dans un fichier (sinon tu ne vois rien)

> ⚠️ cron utilise un environnement minimal : pas tes variables d'env habituelles, pas ton venv.
> Pointe vers le python de ton venv : `/home/mark/projet/.venv/bin/python`.

---

## 7. Une vraie tâche planifiée

Le pattern complet : une fonction métier + une planification + de la gestion d'erreur.

```python
import schedule, time, logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
log = logging.getLogger(__name__)

def job_quotidien():
    try:
        log.info("Début du job")
        # ... scraping / calcul / envoi ...
        log.info("Job terminé OK")
    except Exception as e:
        log.error("Le job a planté : %s", e)   # on log mais on ne crashe pas le scheduler

schedule.every().day.at("07:00").do(job_quotidien)

while True:
    schedule.run_pending()
    time.sleep(30)
```

**Règle d'or :** une tâche planifiée doit **attraper ses propres erreurs**. Si elle plante
sans `try/except`, elle peut tuer tout le planificateur — et plus rien ne tourne.

---

## 8. cron vs n8n : lequel choisir ?

| Critère | cron / APScheduler | n8n (Schedule Trigger) |
|---|---|---|
| Doit tourner PC éteint | Non (sauf serveur) | Oui (cloud) |
| Logique Python complexe | Idéal | Limité |
| Brancher Slack/Email/Notion | À coder | Natif, en 2 clics |
| Visibilité des exécutions | Logs à lire | Interface visuelle |

**Le bon combo :** n8n déclenche (Schedule Trigger) → appelle ton **micro-service Python**
(le cours précédent) pour la logique lourde → n8n distribue le résultat. Tu gardes le meilleur
des deux : la robustesse du planning cloud + la puissance de Python.

---

## 9. Aller plus loin

- **`time.sleep()` n'est PAS de la planification** : ça bloque, ça dérive, ça ne survit pas
  à un crash. Utilise un vrai scheduler.
- **Persistance** : APScheduler peut stocker ses jobs en base (SQLite) pour reprendre après reboot.
- **Sur un serveur** : `systemd timer` est l'alternative moderne à cron, avec de vrais logs.
- **Cloud** : Render Cron Jobs, GitHub Actions (`schedule:`), ou le Schedule Trigger n8n.

Pour ce cours on reste sur l'essentiel : planifier une tâche en Python et comprendre cron.