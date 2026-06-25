# 🧪 Plan de tests — API Bureau de recrutement de héros

> **Compétence C9.** Le jury ne se contente pas de « j'ai cliqué, ça marche ».
> Il attend ce **tableau** (tests pensés à l'avance) **+** des tests automatisés (`pytest`).
> Colonne « Obtenu/Statut » à remplir quand tu exécutes — ici remplie après un run vert.

## 1. Tests automatisés (exécutés par `pytest` ET par la CI)

| # | Cas testé | Données d'entrée | Résultat attendu | Obtenu | Statut |
|---|---|---|---|---|---|
| T1 | Santé du service | `GET /health` | `200` + `{"status":"ok"}` | idem | ✅ |
| T2 | Recrutement nominal | `POST /recrue` + bon token, niveau 88 | `200`, rang `Élite`, matricule `COM-088` | idem | ✅ |
| T3 | Accès sans token | `POST /recrue` sans header `Authorization` | `401` | idem | ✅ |
| T4 | Accès mauvais token | `POST /recrue`, `Bearer faux` | `401` | idem | ✅ |
| T5 | Niveau hors bornes | `POST /recrue` + bon token, niveau `999` | `400` | idem | ✅ |
| T6 | Champ obligatoire manquant | `POST /recrue` + bon token, sans `nom` | `400` | idem | ✅ |
| T7 | Bornes des rangs | niveaux 25 / 50 / 75 / 95 | `Recrue` / `Confirmé` / `Élite` / `Légende` | idem | ✅ |

> Ces 7 cas correspondent 1:1 aux tests de `app/test_app.py`. La CI rejoue
> **exactement ce tableau** à chaque push : c'est ta preuve de **non-régression**.

## 2. Tests manuels (à faire une fois en ligne, après déploiement)

| # | Cas testé | Comment | Résultat attendu | Statut |
|---|---|---|---|---|
| M1 | Service réveillé | Ouvrir l'URL Render dans le navigateur | La page du bureau s'affiche | ☐ |
| M2 | Santé en prod | `curl https://<service>.onrender.com/health` | `{"status":"ok"}` | ☐ |
| M3 | Endpoint protégé en prod | `curl -X POST .../recrue` **sans** token | `401` | ☐ |
| M4 | Recrutement en prod | `curl -X POST .../recrue` avec le **vrai** token | `200` + badge | ☐ |
| M5 | Secret absent du repo | Chercher `API_TOKEN=` dans GitHub | Introuvable (uniquement dans Render) | ☐ |

## 3. Types de tests couverts (vocabulaire jury)

- **Unitaire / intégration** : T1–T7 testent l'app via le client de test Flask.
- **Fonctionnel / bout-en-bout** : M1–M4 testent le service réellement déployé.
- **Non-régression** : la CI relance T1–T7 à chaque modification.
