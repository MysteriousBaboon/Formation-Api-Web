# ============================================================
# serre.py — Carnet de la serre (corrigé)
# ============================================================
# Compétence CDA C8 : CRUD paramétré (SQL) + champ JSON (NoSQL).
# Lancement :  python serre.py   (crée serre.db à côté)
# ============================================================

import json
import sqlite3
from pathlib import Path
from datetime import date, timedelta

DB = Path(__file__).with_name("serre.db")


def connexion():
    return sqlite3.connect(DB)


# ------------------------------------------------------------
# C(reate) — la table
# ------------------------------------------------------------
def init_db():
    with connexion() as conn:
        conn.execute("DROP TABLE IF EXISTS plantes")
        conn.execute("""
            CREATE TABLE plantes (
                id               INTEGER PRIMARY KEY AUTOINCREMENT,
                nom              TEXT    NOT NULL,
                espece           TEXT    NOT NULL,
                frequence        INTEGER NOT NULL,   -- jours entre deux arrosages
                dernier_arrosage TEXT    NOT NULL,   -- AAAA-MM-JJ
                notes            TEXT                -- JSON libre (volet NoSQL)
            )
        """)


# ------------------------------------------------------------
# C(reate) — ajouter une plante
# ------------------------------------------------------------
def ajouter(nom, espece, frequence, dernier_arrosage, notes):
    with connexion() as conn:
        conn.execute(
            "INSERT INTO plantes (nom, espece, frequence, dernier_arrosage, notes) "
            "VALUES (?, ?, ?, ?, ?)",
            (nom, espece, frequence, dernier_arrosage, json.dumps(notes)),
        )


# ------------------------------------------------------------
# R(ead) — lister
# ------------------------------------------------------------
def lister():
    with connexion() as conn:
        curseur = conn.execute(
            "SELECT id, nom, espece, frequence, dernier_arrosage, notes "
            "FROM plantes ORDER BY id"
        )
        return curseur.fetchall()


# ------------------------------------------------------------
# U(pdate) — arroser (met la date du jour)
# ------------------------------------------------------------
def arroser(plante_id):
    with connexion() as conn:
        conn.execute(
            "UPDATE plantes SET dernier_arrosage = ? WHERE id = ?",
            (date.today().isoformat(), plante_id),
        )


# ------------------------------------------------------------
# D(elete) — supprimer
# ------------------------------------------------------------
def supprimer(plante_id):
    with connexion() as conn:
        conn.execute("DELETE FROM plantes WHERE id = ?", (plante_id,))


# ------------------------------------------------------------
# Affichage avec état d'arrosage
# ------------------------------------------------------------
def a_soif(frequence, dernier_arrosage):
    jours = (date.today() - date.fromisoformat(dernier_arrosage)).days
    return jours >= frequence, jours


def afficher(plantes):
    print("🪴 CARNET DE LA SERRE\n")
    for pid, nom, espece, frequence, dernier, notes_txt in plantes:
        soif, jours = a_soif(frequence, dernier)
        etat = "💧 à arroser" if soif else "✅ ok        "
        piece = json.loads(notes_txt).get("piece", "?")
        print(f"#{pid} {nom} ({espece}) — arrosée il y a {jours}j, tous les {frequence}j  "
              f"{etat}  [{piece}]")
    print()


if __name__ == "__main__":
    init_db()

    aujourdhui = date.today()
    def il_y_a(n):
        return (aujourdhui - timedelta(days=n)).isoformat()

    ajouter("Monstera", "Monstera deliciosa", 7, il_y_a(9),
            {"piece": "salon", "lumiere": "vive", "toxique_chat": True})
    ajouter("Cactus", "Echinocactus", 21, il_y_a(5),
            {"piece": "bureau", "lumiere": "plein soleil", "toxique_chat": False})
    ajouter("Basilic", "Ocimum basilicum", 2, il_y_a(3),
            {"piece": "cuisine", "lumiere": "vive", "toxique_chat": False})
    ajouter("Ficus", "Ficus elastica", 7, il_y_a(1),
            {"piece": "salon", "lumiere": "mi-ombre", "toxique_chat": True})

    print("== État initial ==")
    afficher(lister())

    print("== On arrose le Monstera (#1) -> il repasse en ✅ ==")
    arroser(1)
    afficher(lister())

    print("== On retire le Basilic (#3) ==")
    supprimer(3)
    afficher(lister())

    # --- Volet NoSQL : interroger un champ rangé dans le JSON ----------
    print("🐱 Plantes toxiques pour le chat :")
    for pid, nom, espece, frequence, dernier, notes_txt in lister():
        if json.loads(notes_txt).get("toxique_chat"):
            print(f"   ⚠️ {nom}")
