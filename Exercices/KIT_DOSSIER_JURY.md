# 🎒 Kit dossier jury — les preuves « non-code » du CDA

> Certaines compétences ne se prouvent pas par un script, mais par des **artefacts de démarche** :
> gestion de projet (C4), plan de tests (C9), environnement (C1), et le **transversal** (ANSSI, RGPD,
> RGAA, anglais B1, veille). Ce kit fournit les **gabarits à remplir** pour ton dossier — un par section.
>
> 👉 À utiliser sur **chaque** mini-projet et sur ton projet final. Copie les blocs, remplis-les.
> Voir la couverture globale : [`COUVERTURE_CDA.md`](COUVERTURE_CDA.md).

---

## C4 — Gestion de projet (agile + versionnement)

### Backlog & user stories
| ID | User story (En tant que… je veux… afin de…) | Priorité | Sprint | Statut |
|---|---|---|---|---|
| US1 | En tant que…, je veux…, afin de… | Haute | 1 | ✅ Fait |
| US2 | … | Moyenne | 1 | 🔧 En cours |
| US3 | … | Basse | 2 | ⏳ À faire |

### Convention Git (à respecter et à montrer)
- **Commits petits et réguliers**, un par étape, message à l'impératif : `Ajoute la validation du niveau`.
- **Une branche par fonctionnalité** : `feat/scoring`, `fix/token-401`.
- **Pull request** pour fusionner dans `main` (même en solo : ça trace la démarche).

> ⚠️ **Piège jury** : un seul commit final « projet fini » = rouge. Le jury veut un `git log` qui **raconte**.

```bash
git log --oneline --graph        # capture ça pour le dossier
```

---

## C9 — Gabarit de plan de tests

> À remplir AVANT de coder les tests (on pense les cas), puis on exécute et on remplit « Obtenu / Statut ».

| # | Cas testé | Données d'entrée | Résultat attendu | Obtenu | Statut |
|---|---|---|---|---|---|
| T1 | … | … | … | … | ☐ |
| T2 | Accès sans token | aucun header `Authorization` | `401` | | ☐ |
| T3 | Entrée invalide | champ obligatoire manquant | `400` | | ☐ |
| T4 | Cas nominal | données valides | `200` + contenu attendu | | ☐ |

- **Types à citer** : unitaire · intégration · fonctionnel · **non-régression** (rejoués à chaque modif).
- **Automatisé** : ces cas vivent aussi dans `test_*.py` et tournent en CI (cf. `mini-projets/en-ligne-sans-casse/`).

---

## C1 — Checklist environnement de travail

- [ ] **`.venv`** créé et activé (`python -m venv .venv`).
- [ ] **`requirements.txt`** à jour (`pip freeze > requirements.txt`).
- [ ] **`.env`** pour les secrets — **et** **`.env.example`** versionné (modèle sans valeurs).
- [ ] **`.gitignore`** exclut `.env`, `.venv/`, `__pycache__/`, `*.db`, sorties générées.
- [ ] **README** avec la procédure d'installation (clonable par un inconnu).
- [ ] Preuve : `git status` propre + `git ls-files | grep -c .env$` → **0** (le `.env` n'est pas suivi).

> ⚠️ **Piège jury** : un secret committé. Montre `.gitignore` + `.env.example` = réflexe pro.

---

## 🔒 Transversal — à cocher sur chaque projet

### Sécurité (ANSSI)
- [ ] Secrets **hors du code** (variables d'environnement).
- [ ] **Validation des entrées** côté serveur (jamais confiance au client).
- [ ] **Anti-injection** : requêtes SQL **paramétrées** (`?`), jamais de f-string dans une requête.
- [ ] **Authentification** des endpoints sensibles (token Bearer → `401`).
- [ ] **HTTPS** en production, `FLASK_DEBUG=false`.

### RGPD
- [ ] Je collecte une donnée perso ? → **consentement explicite** + données **minimisées**.
- [ ] Aucune donnée perso ? → je sais **le dire** (et le justifier).
- [ ] Pas de revente, stockage local/maîtrisé, durée de conservation pensée.

### Accessibilité (RGAA)
- [ ] `<label>` reliés, **contrastes** suffisants, navigation **clavier**, **alt** sur les images.
- [ ] Erreurs en **texte** (pas seulement la couleur). *(Exercice dédié : `micro-exercices/13_formulaire-accessible/`.)*

### Anglais B1 — fiche « doc lue »
| Bibliothèque / outil | Page lue (URL) | Ce que j'en ai retenu (2 lignes, en français) |
|---|---|---|
| ex. Flask | flask.palletsprojects.com/quickstart | … |
| … | … | … |

### Veille — 2 à 3 sources que je suis
| Source | Thème | Pourquoi je la suis |
|---|---|---|
| ex. bulletins CERT-FR | sécurité | alertes vulnérabilités |
| … | outils IA | … |
| … | … | … |

---

## ✅ Check-list « dossier prêt »

- [ ] Backlog + `git log` qui raconte (C4).
- [ ] Plan de tests (tableau) + `pytest` au vert (C9).
- [ ] Environnement propre, secrets hors Git (C1).
- [ ] Transversal coché : ANSSI, RGPD, RGAA, anglais B1, veille.
- [ ] Je peux dérouler dans l'ordre : **besoin → maquette → architecture → code → tests → déploiement**.
