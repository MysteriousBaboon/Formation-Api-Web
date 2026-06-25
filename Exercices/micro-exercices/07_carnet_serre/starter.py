# ============================================================
# starter.py — Carnet de la serre (à compléter)
# ============================================================
# Lancement :  python starter.py
# Crée un fichier serre.db à côté du script.
# ============================================================

import json
import sqlite3
from pathlib import Path
from datetime import date, timedelta

DB = Path(__file__).with_name("serre.db")


def init_db():
    # TODO : table plantes (id, nom, espece, frequence, dernier_arrosage, notes)
    pass


def ajouter(nom, espece, frequence, dernier_arrosage, notes):
    # TODO : INSERT paramétré ; notes (dict) -> json.dumps(notes)
    pass


def lister():
    # TODO : SELECT * ORDER BY id ; renvoie la liste
    return []


def arroser(plante_id):
    # TODO : UPDATE dernier_arrosage = <aujourd'hui> WHERE id = ?
    pass


def supprimer(plante_id):
    # TODO : DELETE WHERE id = ?
    pass


def afficher(plantes):
    print("🪴 CARNET DE LA SERRE\n")
    # TODO : pour chaque plante, 💧 si jours_écoulés >= frequence sinon ✅
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

    afficher(lister())
