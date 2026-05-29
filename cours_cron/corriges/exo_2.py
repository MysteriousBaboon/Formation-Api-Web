# Corrigé exo 2 — Traduire des expressions cron

# --- Traductions ---
# 0 8 * * *        → tous les jours à 8h00
# */30 * * * *     → toutes les 30 minutes
# 0 12 * * 6       → tous les samedis à 12h00  (6 = samedi)
# 0 0 1 1 *        → le 1er janvier à minuit (une fois par an)
# 15 14 * * 1-5    → à 14h15 du lundi au vendredi

# --- Phrases → expressions ---
# 1. "Toutes les 5 minutes"               → */5 * * * *
# 2. "Tous les jours à 22h30"             → 30 22 * * *
# 3. "Tous les dimanches à 8h"            → 0 8 * * 0   (0 = dimanche)
# 4. "Le premier de chaque mois à midi"   → 0 12 1 * *

print("Voir les commentaires de ce fichier pour les réponses.")
print("Vérification : https://crontab.guru")