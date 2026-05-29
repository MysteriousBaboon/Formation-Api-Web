# 🧪 Exercices — Planification & automatisation (≈ 2h)

> Avant de commencer : `pip install -r requirements.txt`.
> Chaque exo a son corrigé dans `corriges/`.
> 💡 Pour les exos, mets des intervalles courts (secondes) pour voir le résultat tout de suite.

---

## Exercice 1 — Première tâche planifiée (20 min)

Crée `exo_1.py` avec la lib `schedule`.

1. Une fonction `heure_actuelle()` qui affiche l'heure courante (`datetime.now()`)
2. Planifie-la **toutes les 3 secondes**
3. Ajoute une deuxième fonction `bip()` qui affiche `"bip"` **toutes les 5 secondes**
4. Lance la boucle et observe les deux s'alterner

> 💡 N'oublie pas le `while True: schedule.run_pending(); time.sleep(1)`.

---

## Exercice 2 — Traduire des expressions cron (20 min)

Crée `exo_2.py`. Sans regarder le corrigé tout de suite, écris en commentaire ce que
signifie chacune de ces expressions cron, puis vérifie sur https://crontab.guru :

```
0 8 * * *
*/30 * * * *
0 12 * * 6
0 0 1 1 *
15 14 * * 1-5
```

Ensuite, écris l'expression cron correspondant à ces phrases :
1. "Toutes les 5 minutes"
2. "Tous les jours à 22h30"
3. "Tous les dimanches à 8h"
4. "Le premier de chaque mois à midi"

---

## Exercice 3 — APScheduler avec cron (35 min)

Crée `exo_3.py` avec **APScheduler**.

1. Une tâche `interval` qui s'exécute toutes les 4 secondes et affiche un compteur
   qui s'incrémente (1, 2, 3...)
2. Une tâche `cron` configurée pour s'exécuter chaque minute à la seconde 0
   (`second=0` dans un job cron)
3. Lance le scheduler, vérifie que le compteur monte bien

> 💡 Pour le compteur, utilise une variable globale ou une liste mutable
> (souviens-toi des fermetures du cours théorie).

---

## Exercice 4 — Le job complet (45 min)

Le projet fil rouge. Crée `exo_4.py` : un job qui surveille et alerte.

1. Une fonction `verifier_stock()` qui simule un stock (`random.randint(0, 20)`)
2. Si le stock est **< 5**, considère que c'est une rupture imminente → log un `warning`
3. Sinon, log un `info` normal
4. Le job doit avoir un **`try/except`** : s'il plante, il log l'erreur mais ne tue pas
   le scheduler
5. Planifie-le toutes les 8 secondes avec `schedule`
6. Configure le `logging` proprement (niveau INFO, format avec horodatage)

Bonus : au lieu de juste logger, envoie l'alerte vers une URL https://webhook.site
avec `requests.post(...)` (simule l'envoi vers n8n).

---

## Récap

| Compétence | Exo |
|---|---|
| Planifier avec `schedule` | 1, 4 |
| Lire/écrire des expressions cron | 2 |
| APScheduler (interval + cron) | 3 |
| Job robuste (logging + try/except) | 4 |
| Pousser vers un webhook (n8n) | 4 (bonus) |