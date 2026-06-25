# ============================================================
# leaderboard.py — Leaderboard d'arcade (corrigé)
# ============================================================
# Compétence CDA C8 : requêtes PARAMÉTRÉES (anti-injection SQL).
# Lancement :  python leaderboard.py   (crée arcade.db à côté)
# ============================================================

import sqlite3
from pathlib import Path

DB = Path(__file__).with_name("arcade.db")
MEDAILLES = ["🥇", "🥈", "🥉"]


def connexion():
    # Le `with sqlite3.connect(...)` committe automatiquement à la sortie du bloc.
    return sqlite3.connect(DB)


def init_db():
    with connexion() as conn:
        # On repart d'une table propre à chaque lancement de la démo
        conn.execute("DROP TABLE IF EXISTS scores")
        conn.execute("""
            CREATE TABLE scores (
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                joueur  TEXT    NOT NULL,
                points  INTEGER NOT NULL,
                cree_le TEXT    DEFAULT CURRENT_TIMESTAMP
            )
        """)


def ajouter_score(joueur, points):
    # ✅ Requête PARAMÉTRÉE : les valeurs passent dans le tuple, jamais collées au texte SQL.
    #    Même si `joueur` contient du SQL malveillant, il est traité comme une simple chaîne.
    with connexion() as conn:
        conn.execute(
            "INSERT INTO scores (joueur, points) VALUES (?, ?)",
            (joueur, points),
        )


def top_scores(n=10):
    with connexion() as conn:
        curseur = conn.execute(
            "SELECT joueur, points FROM scores ORDER BY points DESC LIMIT ?",
            (n,),
        )
        return curseur.fetchall()


def chercher(joueur):
    with connexion() as conn:
        curseur = conn.execute(
            "SELECT joueur, points FROM scores WHERE joueur = ? ORDER BY points DESC",
            (joueur,),
        )
        return curseur.fetchall()


def afficher(top):
    print("🏆 LEADERBOARD ARCADE\n")
    for i, (joueur, points) in enumerate(top):
        rang = MEDAILLES[i] if i < 3 else f"{i + 1:>2}."
        print(f"{rang}  {joueur:<28} {points:>7} pts")
    print()


if __name__ == "__main__":
    init_db()

    for joueur, points in [
        ("ZELDA", 9800), ("MARIO", 15200), ("LINK", 12300),
        ("SAMUS", 8700), ("KIRBY", 11000), ("YOSHI", 10250),
    ]:
        ajouter_score(joueur, points)

    # Tentative d'injection SQL via le pseudo
    pseudo_piege = "Bobby'); DROP TABLE scores;--"
    ajouter_score(pseudo_piege, 5000)

    afficher(top_scores(5))

    # --- Preuve que l'injection a été neutralisée ---------------------
    survivants = chercher(pseudo_piege)
    print("🛡️  Test anti-injection")
    print(f"    Table 'scores' toujours là ? {'oui ✅' if survivants is not None else 'non ❌'}")
    print(f"    Pseudo piégé stocké tel quel : {survivants}")
