# ============================================================
# starter.py — Modèle de données Troc'Quartier (à compléter)
# ============================================================
# Lancement :  python starter.py
# Crée un fichier troc.db à côté du script.
# ============================================================

import sqlite3
from pathlib import Path

DB = Path(__file__).with_name("troc.db")


def init_db(con):
    con.execute("PRAGMA foreign_keys = ON")
    # TODO : CREATE TABLE membres (id, prenom, contact)
    # TODO : CREATE TABLE objets (id, nom, description, proprietaire_id -> membres.id)
    # TODO : CREATE TABLE reservations (id, objet_id, emprunteur_id, date_debut, date_fin, statut)
    con.commit()


def inserer_jeu_de_donnees(con):
    # TODO : insère 2-3 membres, quelques objets, 1-2 réservations
    #        TOUJOURS en requêtes paramétrées (?, ?)  -- jamais de f-string
    con.commit()


def lister_reservations(con):
    # TODO : SELECT avec JOIN sur les 3 tables ->
    #        objet, propriétaire, emprunteur, statut
    return []


if __name__ == "__main__":
    if DB.exists():
        DB.unlink()  # repart propre à chaque lancement
    with sqlite3.connect(DB) as con:
        init_db(con)
        inserer_jeu_de_donnees(con)
        print("Réservations :")
        for ligne in lister_reservations(con):
            print(" ", ligne)
