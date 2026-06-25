# ============================================================
# modele.py — Modèle de données Troc'Quartier (corrigé)
# ============================================================
# Lancement :  python modele.py
# Démontre : 3 tables normalisées, clés primaire/étrangère,
# contraintes d'intégrité, requêtes paramétrées, jointure 3 tables.
# ============================================================

import sqlite3
from pathlib import Path

DB = Path(__file__).with_name("troc.db")

SCHEMA = """
CREATE TABLE membres (
    id      INTEGER PRIMARY KEY,
    prenom  TEXT NOT NULL,
    contact TEXT NOT NULL UNIQUE          -- un contact identifie un membre
);

CREATE TABLE objets (
    id              INTEGER PRIMARY KEY,
    nom             TEXT NOT NULL,
    description     TEXT,
    -- relation 1-N : un membre possède plusieurs objets, un objet a UN propriétaire
    proprietaire_id INTEGER NOT NULL REFERENCES membres(id)
);

CREATE TABLE reservations (
    id            INTEGER PRIMARY KEY,
    -- table d'association membre <-> objet, portant les dates
    objet_id      INTEGER NOT NULL REFERENCES objets(id),
    emprunteur_id INTEGER NOT NULL REFERENCES membres(id),
    date_debut    TEXT NOT NULL,
    date_fin      TEXT NOT NULL,
    statut        TEXT NOT NULL DEFAULT 'en attente',
    CHECK (date_fin >= date_debut)        -- intégrité métier
);
"""


def init_db(con):
    con.execute("PRAGMA foreign_keys = ON")   # SQLite : OFF par défaut !
    con.executescript(SCHEMA)
    con.commit()


def ajouter_membre(con, prenom, contact):
    cur = con.execute(
        "INSERT INTO membres (prenom, contact) VALUES (?, ?)", (prenom, contact)
    )
    return cur.lastrowid


def ajouter_objet(con, nom, description, proprietaire_id):
    cur = con.execute(
        "INSERT INTO objets (nom, description, proprietaire_id) VALUES (?, ?, ?)",
        (nom, description, proprietaire_id),
    )
    return cur.lastrowid


def reserver(con, objet_id, emprunteur_id, date_debut, date_fin):
    con.execute(
        "INSERT INTO reservations (objet_id, emprunteur_id, date_debut, date_fin) "
        "VALUES (?, ?, ?, ?)",
        (objet_id, emprunteur_id, date_debut, date_fin),
    )


def inserer_jeu_de_donnees(con):
    alice = ajouter_membre(con, "Alice", "alice@quartier.fr")
    bob = ajouter_membre(con, "Bob", "bob@quartier.fr")
    chloe = ajouter_membre(con, "Chloé", "chloe@quartier.fr")

    perceuse = ajouter_objet(con, "Perceuse", "Visseuse 18V + embouts", alice)
    ajouter_objet(con, "Tente 4 places", "Montage rapide", alice)
    raclette = ajouter_objet(con, "Appareil à raclette", "8 coupelles", bob)

    reserver(con, perceuse, bob, "2026-07-01", "2026-07-03")
    reserver(con, raclette, chloe, "2026-07-05", "2026-07-06")
    con.commit()


def lister_reservations(con):
    # Jointure à 3 tables : la preuve que le modèle relie bien les entités.
    sql = """
    SELECT o.nom            AS objet,
           prop.prenom      AS proprietaire,
           emp.prenom       AS emprunteur,
           r.date_debut, r.date_fin, r.statut
    FROM reservations r
    JOIN objets  o    ON o.id = r.objet_id
    JOIN membres prop ON prop.id = o.proprietaire_id
    JOIN membres emp  ON emp.id  = r.emprunteur_id
    ORDER BY r.date_debut;
    """
    return con.execute(sql).fetchall()


def demo_integrite(con):
    # Bonus : une réservation sur un objet inexistant doit être REFUSÉE
    # par la clé étrangère (grâce au PRAGMA foreign_keys = ON).
    try:
        con.execute(
            "INSERT INTO reservations (objet_id, emprunteur_id, date_debut, date_fin) "
            "VALUES (?, ?, ?, ?)",
            (999, 1, "2026-07-10", "2026-07-11"),
        )
        return "❌ accepté (le PRAGMA n'est pas actif)"
    except sqlite3.IntegrityError:
        return "✅ refusé (clé étrangère respectée)"


if __name__ == "__main__":
    if DB.exists():
        DB.unlink()
    with sqlite3.connect(DB) as con:
        init_db(con)
        inserer_jeu_de_donnees(con)

        print("📋 Réservations (objet · propriétaire · emprunteur · dates · statut) :")
        for objet, prop, emp, d1, d2, statut in lister_reservations(con):
            print(f"  {objet:<22} {prop:<8} -> {emp:<8} {d1}→{d2}  [{statut}]")

        print("\n🔒 Test d'intégrité (objet inexistant) :", demo_integrite(con))
