# ============================================================
# 3_syntaxe_cron.py — Décoder la syntaxe cron
# ============================================================
# cron est le standard universel de planification (Linux, Mac,
# serveurs, GitHub Actions, Render...). 5 champs séparés
# par des espaces. Ce fichier sert d'antisèche commentée.
# ============================================================

# ------------------------------------------------------------
# La structure : 5 champs
# ------------------------------------------------------------
#   ┌───── minute        (0-59)
#   │ ┌───── heure        (0-23)
#   │ │ ┌───── jour du mois (1-31)
#   │ │ │ ┌───── mois         (1-12)
#   │ │ │ │ ┌───── jour semaine (0-6, 0 = dimanche)
#   │ │ │ │ │
#   * * * * *
#
#   *  = toutes les valeurs
#   */N = tous les N (ex: */15 = toutes les 15)
#   A-B = de A à B (ex: 1-5 = lundi à vendredi)
#   A,B = A et B (ex: 0,30 = à 0 et 30 min)

# ------------------------------------------------------------
# Une "antisèche" sous forme de dictionnaire
# ------------------------------------------------------------
EXPRESSIONS = {
    "* * * * *":        "Toutes les minutes",
    "0 7 * * *":        "Tous les jours à 7h00",
    "30 6 * * *":       "Tous les jours à 6h30",
    "*/15 * * * *":     "Toutes les 15 minutes",
    "0 * * * *":        "Au début de chaque heure",
    "0 9 * * 1":        "Tous les lundis à 9h00",
    "0 9 * * 1-5":      "Du lundi au vendredi à 9h00",
    "0 8-18 * * 1-5":   "Chaque heure de 8h à 18h, en semaine",
    "0 0 1 * *":        "Le 1er de chaque mois à minuit",
    "0 0 * * 0":        "Tous les dimanches à minuit",
}

if __name__ == "__main__":
    print("ANTISÈCHE CRON\n" + "=" * 45)
    for expr, sens in EXPRESSIONS.items():
        print(f"  {expr:<16} → {sens}")
    print("\n💡 Pour traduire n'importe quelle expression : https://crontab.guru")
    print("\nExemple de ligne dans 'crontab -e' :")
    print("  0 7 * * * /chemin/.venv/bin/python /chemin/script.py >> log.txt 2>&1")