# 🗺️ Couverture du titre CDA par le dossier Exercices

> **But de ce document** : prouver que réaliser **tout** le dossier `Exercices/` permet de
> défendre **les 11 compétences** du titre **Concepteur Développeur d'Applications**
> (RNCP37873, niveau 6) **+ le transversal** (ANSSI, RGPD, RGAA, anglais B1, veille) — preuves à l'appui.
>
> 🧠 **La règle d'or du jury** : « c'est l'IA qui l'a fait » est interdit. Pour chaque ligne de code,
> tu dois savoir dire **quoi**, **pourquoi**, et **ce qui se passe si on l'enlève**.
> 🟥 **Deux compétences exigent du vrai code visible et maîtrisé** : **C3** (composants métier) et **C8** (accès aux données).

Référentiel détaillé : [`../VALIDATION_COMPETENCES_CDA.md`](../VALIDATION_COMPETENCES_CDA.md) ·
plan de révision : [`../PROGRAMME_REVISION_CDA.md`](../PROGRAMME_REVISION_CDA.md).

---

## Légende

| Symbole | Sens |
|---|---|
| ✅ | Couverture **solide** : exercice/projet dédié, défendable seul |
| ~ | Couverture **amorcée** : présent mais en appui d'autre chose |
| 🟥 | Compétence **« code visible »** (le jury déroule ton code ligne à ligne) |
| 🆕 | Artefact **ajouté** pour combler un trou de couverture |

---

## 📊 Matrice principale — les 11 compétences

### 🟦 BC01 — Développer une application sécurisée

| Comp. | Intitulé | Couvert par | Preuve à montrer au jury |
|---|---|---|---|
| **C1** | Installer et configurer son environnement | `KIT_DOSSIER_JURY.md` 🆕 · **tous** les projets (`.env.example`, `.gitignore`, `requirements.txt`) | `.gitignore` qui exclut `.env` + `.env.example` versionné → « mes secrets ne sont pas dans Git » |
| **C2** | Développer des interfaces utilisateur | micro **13 — formulaire accessible** 🆕 · micro 03/04/05 · projets `quiz-coach`, `affiche-moi-ca`, `carte-bons-coins` | Avant/après accessibilité (labels, contrastes, clavier) + checklist RGAA |
| **C3** 🟥 | Développer des composants métier | micro **03** (dés), **04** (token héros), **05** (scoring monstre) · projets `quiz-coach`, `terrasse-o-metre`, `factures-en-clair`, `assistant-devis` | Dérouler `app.py` sans notes : validation, scoring, token Bearer, codes HTTP 200/400/401/500 |
| **C4** | Contribuer à la gestion de projet | `KIT_DOSSIER_JURY.md` 🆕 · historique Git de **chaque** projet | Backlog + user stories + `git log` avec commits petits et réguliers |

### 🟩 BC02 — Concevoir et développer une application en couches

| Comp. | Intitulé | Couvert par | Preuve à montrer au jury |
|---|---|---|---|
| **C5** | Analyser les besoins et maquetter | micro **10 — du brief au wireframe** 🆕 · en-tête « user stories » de chaque projet | Besoin fonctionnel/non-fonctionnel + diagramme de cas d'usage + wireframe |
| **C6** | Définir l'architecture logicielle | micro **11 — dessine l'architecture** 🆕 · projets `terrasse-o-metre`, `carte-bons-coins`, `assistant-devis` | Schéma multicouche + diagramme de séquence + tableau des choix justifiés (ANSSI) |
| **C7** | Concevoir une base de données relationnelle | micro **12 — modélise avant de coder** 🆕 · projet `factures-en-clair` (clients 1-N factures) | MCD/MLD Merise : clés primaire/étrangère, relation 1-N, normalisation |
| **C8** 🟥 | Accès aux données SQL **et** NoSQL | micro **06** (leaderboard SQL), **07** (CRUD + JSON) · projets `factures-en-clair` (SQL+JSON), `thermometre-avis` (JSON), `assistant-devis` (SQL) | Requête **paramétrée** (`?`) + anti-injection expliquée + un stockage NoSQL (JSON) |

### 🟨 BC03 — Préparer le déploiement d'une application sécurisée

| Comp. | Intitulé | Couvert par | Preuve à montrer au jury |
|---|---|---|---|
| **C9** | Préparer et exécuter les plans de tests | micro **08** (TDD pizza), **09** (tests API) · projet **`en-ligne-sans-casse`** 🆕 (tableau de plan de tests) · `factures-en-clair` | `pytest` au vert **+ tableau de plan de tests** (cas/données/attendu/obtenu/statut) |
| **C10** | Préparer et documenter le déploiement | projet **`en-ligne-sans-casse`** 🆕 (`DEPLOIEMENT.md`) · source `../cours_microservice/deploiement_render.md` | Procédure pas-à-pas qu'un inconnu peut suivre + checklist pré-prod + rollback |
| **C11** | Mise en production (DevOps) | projet **`en-ligne-sans-casse`** 🆕 (`.github/workflows/tests.yml` + `render.yaml`) | Flux `push → CI (pytest) → CD (Render)` : **CI + CD**, pas seulement Render |

---

## 🔒 Compétences transversales (le jury les cherche PARTOUT)

| Transversal | Couvert par | Preuve |
|---|---|---|
| **Sécurité ANSSI** | micro 04/06 · projets `factures`, `assistant-devis` · `en-ligne-sans-casse` 🆕 | Secrets hors du code, validation des entrées, **anti-injection** (requêtes paramétrées), token, `FLASK_DEBUG=false` en prod |
| **RGPD** | projet `quiz-coach` · `KIT_DOSSIER_JURY.md` 🆕 | Consentement explicite + données minimisées (ou savoir dire « aucune donnée perso ici ») |
| **RGAA (accessibilité)** | micro **13** 🆕 · `KIT_DOSSIER_JURY.md` 🆕 | Labels reliés, contrastes, navigation clavier, alternatives textuelles + checklist d'audit |
| **Anglais B1** | `KIT_DOSSIER_JURY.md` 🆕 (fiche « doc lue ») | Une doc de bibliothèque lue en anglais + résumé court |
| **Veille** | `KIT_DOSSIER_JURY.md` 🆕 (fiche veille) | 2-3 sources suivies (sécurité, outils IA) |

---

## ✅ Verdict de couverture

| Bloc | Compétences | État |
|---|---|---|
| BC01 | C1, C2, C3 🟥, C4 | ✅ couvert |
| BC02 | C5, C6, C7, C8 🟥 | ✅ couvert |
| BC03 | C9, C10, C11 | ✅ couvert |
| Transversal | ANSSI, RGPD, RGAA, anglais B1, veille | ✅ couvert |

**Aucune compétence n'est laissée sans exercice/projet ni sans preuve.** Réaliser l'intégralité
du dossier `Exercices/` = être capable de défendre le titre **haut la main**.

---

## 🚦 Parcours conseillé

1. **Fondamentaux** : micro 01-02.
2. **C3 (code visible)** : micro 03 → 04 → 05.
3. **C7 puis C8** : micro **12** 🆕 (modéliser) → micro 06 → 07.
4. **C9** : micro 08 → 09.
5. **C2 / RGAA** : micro **13** 🆕.
6. **C5 puis C6** : micro **10** 🆕 → **11** 🆕.
7. **Mini-projets** : dans l'ordre du [`mini-projets/README.md`](mini-projets/README.md).
8. **C10 + C11** : projet **`mini-projets/en-ligne-sans-casse`** 🆕 (mise en ligne d'une API déjà écrite).
9. **Dossier jury** : remplir [`KIT_DOSSIER_JURY.md`](KIT_DOSSIER_JURY.md) 🆕 au fil de l'eau.

---

## 📦 État de production des artefacts 🆕

| Artefact | Comble | Statut |
|---|---|---|
| `COUVERTURE_CDA.md` (ce fichier) | colonne vertébrale | ✅ livré |
| `mini-projets/en-ligne-sans-casse/` | C10 + C11 (+ C9 tableau) | ✅ livré |
| `micro-exercices/10_du-brief-au-wireframe/` | C5 | ✅ livré |
| `micro-exercices/11_dessine-architecture/` | C6 | ✅ livré |
| `micro-exercices/12_modelise-avant-de-coder/` | C7 | ✅ livré |
| `micro-exercices/13_formulaire-accessible/` | C2 / RGAA | ✅ livré |
| `KIT_DOSSIER_JURY.md` | C1, C4, C9-tableau, transversal | ✅ livré |

> Tous les artefacts de couverture sont en place : les 11 compétences + le transversal sont
> chacune rattachées à au moins un exercice/projet du dossier, avec une preuve défendable au jury.
