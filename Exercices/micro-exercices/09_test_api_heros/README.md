# 🧪 Tester l'API des héros (~45 min) — *pytest sur un endpoint Flask*

> 🎓 **Compétence CDA visée : C9 — Plans de tests**
> Tester une **API** (pas juste une fonction) avec le **client de test Flask**. Tu vas couvrir
> **exactement** la check-list que le jury attend sur un micro-service : token OK/KO, validation, `/health`.

---

## Le contexte

On te livre `app.py` : c'est l'API du **Bureau de recrutement de héros** (la même qu'à l'exo 04).
Au lieu de la tester à la main avec `curl`, tu vas écrire une **suite de tests automatisés**
qui rejoue tous les cas en une commande — et qui te prévient si une modif casse quelque chose
(la fameuse **non-régression**).

> Pas besoin de lancer le serveur ! Flask fournit un **client de test** qui appelle l'app
> en mémoire : `app.test_client()`. Rapide, déterministe, parfait pour `pytest`.

---

## Ce que tu dois construire

Crée `test_app.py` à côté de `app.py`, avec une **fixture** qui fournit le client de test,
puis des tests qui couvrent la check-list du jury :

| Test | Requête | Code attendu |
|------|---------|--------------|
| `test_health` | `GET /health` | **200** + `{"status": "ok"}` |
| `test_recrue_ok` | `POST /recrue` **avec bon token** | **200** (+ vérifie le rang/matricule) |
| `test_sans_token` | `POST /recrue` **sans header** | **401** |
| `test_mauvais_token` | `POST /recrue` **token bidon** | **401** |
| `test_niveau_invalide` | `POST /recrue` `niveau: 999` | **400** |
| `test_nom_manquant` | `POST /recrue` sans `nom` | **400** |

Lance :
```bash
pytest -v
```
Objectif : **tout vert** ✅.

---

## 💡 Conseils

- La fixture qui donne le client de test :
  ```python
  import pytest
  from app import app, API_TOKEN

  @pytest.fixture
  def client():
      app.config["TESTING"] = True
      return app.test_client()
  ```
- Un appel authentifié :
  ```python
  EN_TETE = {"Authorization": f"Bearer {API_TOKEN}", "Content-Type": "application/json"}

  def test_recrue_ok(client):
      r = client.post("/recrue", headers=EN_TETE,
                      json={"nom": "Comète", "pouvoir": "Vol", "niveau": 88})
      assert r.status_code == 200
      assert r.get_json()["rang"] == "Élite"
  ```
- Importer `API_TOKEN` depuis `app` t'évite d'écrire le token en dur dans les tests.
- `r.get_json()` te donne le corps de la réponse sous forme de `dict`.

---

## ✅ Critères de réussite

- [ ] Une **fixture** `client` factorise `app.test_client()`.
- [ ] Les **6 cas** du tableau sont testés et **verts**.
- [ ] Les deux cas **401** (sans token / mauvais token) sont bien distingués.
- [ ] Au moins un test vérifie le **contenu** de la réponse (rang ou matricule), pas que le code HTTP.
- [ ] Tu sais expliquer pourquoi `app.test_client()` est mieux que `curl` pour une suite de tests.

---

## ⭐ Bonus

1. **Paramétrage des rangs** : avec `@pytest.mark.parametrize`, vérifie que niveau 25→Recrue,
   50→Confirmé, 75→Élite, 95→Légende.
2. **Cas limites** : teste `niveau: 1` et `niveau: 100` (les bornes doivent passer en 200).
3. **Couverture** : installe `pytest-cov` et lance `pytest --cov=app` pour voir le % de code testé.
