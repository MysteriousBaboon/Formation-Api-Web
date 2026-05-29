# ⏰ Cours 7 — Planification & automatisation (cron)

Faire tourner ton code Python **tout seul**, à intervalles réguliers, sans cliquer sur "Run".

## 🎯 Objectifs

À la fin de ce module, tu seras capable de :

- Planifier une tâche Python avec **schedule** (simple) et **APScheduler** (robuste)
- Comprendre la syntaxe **cron** (le standard système, présent partout)
- Mettre une vraie tâche en boucle (scraping + envoi)
- Comprendre **quand utiliser cron vs n8n** (et comment les combiner)

## 📁 Structure

```
cours_cron/
├── README.md
├── cours.md                ← Cours complet (à lire en premier)
├── requirements.txt
├── 1_schedule_simple.py    ← La lib 'schedule' : lisible, parfait pour démarrer
├── 2_apscheduler.py        ← APScheduler : cron, persistance, robuste
├── 3_syntaxe_cron.py       ← Décoder la syntaxe cron (* * * * *)
├── 4_tache_reelle.py       ← Une vraie tâche : récupérer + alerter
├── 5_cron_vers_n8n.py      ← Le cron qui pousse vers un webhook n8n
└── exos.md                 ← 4 exercices progressifs
```

## 🚀 Pour démarrer

```bash
cd cours_cron
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python 1_schedule_simple.py   # Ctrl+C pour arrêter
```

## 🔗 Le lien avec le reste

C'est l'étape **"déclencher tout seul"**. Jusqu'ici tu lançais tes scripts à la main.
Avec un planificateur :

```
[Toutes les nuits à 6h]  →  [Scraping]  →  [pandas]  →  [dataviz]  →  [n8n: envoie le rapport]
```

Le fichier `5_cron_vers_n8n.py` boucle avec le **cours micro-service / n8n** : ton Python
s'auto-déclenche et pousse le résultat dans un workflow. C'est le flux inversé du cours n8n.