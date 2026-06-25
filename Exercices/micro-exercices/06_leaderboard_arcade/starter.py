# ============================================================
# starter.py — Leaderboard d'arcade (à compléter)
# ============================================================
# Lancement :  python starter.py
# Crée un fichier arcade.db à côté du script.
# ============================================================

import sqlite3
from pathlib import Path

DB = Path(__file__).with_name("arcade.db")
MEDAILLES = ["🥇", "🥈", "🥉"]


def init_db():
    # TODO : créer la table `scores` (id, joueur, points, cree_le)
    pass


def ajouter_score(joueur, points):
    # TODO : INSERT PARAMÉTRÉ (?, ?) — surtout pas de f-string !
    pass


def top_scores(n=10):
    # TODO : SELECT joueur, points ... ORDER BY points DESC LIMIT ?
    return []


def afficher(top):
    print("🏆 LEADERBOARD ARCADE\n")
    # TODO : pour chaque (joueur, points), afficher médaille ou rang + aligné
    print()


if __name__ == "__main__":
    init_db()

    for joueur, points in [
        ("ZELDA", 9800), ("MARIO", 15200), ("LINK", 12300),
        ("SAMUS", 8700), ("KIRBY", 11000), ("YOSHI", 10250),
    ]:
        ajouter_score(joueur, points)

    # Le pseudo piégé : une tentative d'injection SQL classique
    ajouter_score("Bobby'); DROP TABLE scores;--", 5000)

    afficher(top_scores(5))
