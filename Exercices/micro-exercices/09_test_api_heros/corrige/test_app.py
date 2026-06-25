# ============================================================
# test_app.py — Tests de l'API des héros (corrigé)
# ============================================================
# Lancement :  pytest -v
# Pas besoin de lancer le serveur : on utilise le client de test Flask.
# ============================================================

import pytest

from app import app, API_TOKEN

EN_TETE = {"Authorization": f"Bearer {API_TOKEN}", "Content-Type": "application/json"}


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"


def test_recrue_ok(client):
    r = client.post("/recrue", headers=EN_TETE,
                    json={"nom": "Comète", "pouvoir": "Vol", "niveau": 88})
    assert r.status_code == 200
    corps = r.get_json()
    assert corps["rang"] == "Élite"
    assert corps["matricule"] == "COM-088"


def test_sans_token(client):
    # Aucun header Authorization -> on doit être bloqué.
    r = client.post("/recrue", json={"nom": "X", "pouvoir": "Vol", "niveau": 50})
    assert r.status_code == 401


def test_mauvais_token(client):
    r = client.post("/recrue",
                    headers={"Authorization": "Bearer faux", "Content-Type": "application/json"},
                    json={"nom": "X", "pouvoir": "Vol", "niveau": 50})
    assert r.status_code == 401


def test_niveau_invalide(client):
    r = client.post("/recrue", headers=EN_TETE,
                    json={"nom": "X", "pouvoir": "Vol", "niveau": 999})
    assert r.status_code == 400


def test_nom_manquant(client):
    r = client.post("/recrue", headers=EN_TETE,
                    json={"pouvoir": "Vol", "niveau": 50})
    assert r.status_code == 400


@pytest.mark.parametrize("niveau, rang", [(25, "Recrue"), (50, "Confirmé"), (75, "Élite"), (95, "Légende")])
def test_rangs(client, niveau, rang):
    r = client.post("/recrue", headers=EN_TETE,
                    json={"nom": "Test", "pouvoir": "Vol", "niveau": niveau})
    assert r.status_code == 200
    assert r.get_json()["rang"] == rang
