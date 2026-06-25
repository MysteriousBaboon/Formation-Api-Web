# 🎯 Micro-exercices techniques — spécial titre CDA

Des **mini-exercices ciblés** (chacun **< 1h30**) pour muscler la *vraie technique*
derrière vos outils no-code. Chaque exo attaque **une fonctionnalité précise** que
le jury **Concepteur Développeur d'Applications** (RNCP37873) vous fera dérouler
**ligne à ligne** — donc on code, on comprend, et on sait expliquer.

> 🧠 **Le piège n°1 du jury** : répondre « c'est l'IA qui l'a fait ».
> Ici, l'objectif est l'inverse : être capable de **réexpliquer chaque ligne sans notes**.

---

## Comment ça marche

- **1 dossier = 1 exercice**, autonome.
- Dans chaque dossier :
  - `README.md` → l'énoncé (objectifs, conseils 💡, critères ✅, bonus ⭐)
  - parfois un `starter.py` ou un template fourni → ton point de départ
  - `corrige/` → la solution commentée (à n'ouvrir **qu'après** avoir tenté !)

### Installation (une fois)

```bash
python -m venv .venv
source .venv/bin/activate        # Windows : .venv\Scripts\activate
pip install -r requirements.txt
```

`sqlite3` est dans la bibliothèque standard de Python → rien à installer pour les exos base de données.

---

## Les exercices

| # | Thème | Compétence CDA | Ce que tu apprends à faire | Durée | Rendu |
|---|-------|----------------|----------------------------|-------|-------|
| 01 | 🌡️ Baromètre d'humeur | Fondamentaux | Compter avec un `dict` et dessiner un histogramme dans le terminal | ~30 min | Terminal couleur |
| 02 | 🔐 Jauge de mot de passe | Fondamentaux | Écrire une fonction qui **note** une chaîne (longueur, types de caractères) | ~40 min | Terminal (jauge) |
| 03 | 🎲 Lanceur de dés JDR | **C3 — Flask** | Recevoir, **parser et valider** une entrée, renvoyer le bon **code HTTP** | ~1h | Page web 🎲 |
| 04 | 🦸 Bureau de recrutement de héros | **C3 — Flask** | Protéger un endpoint par **token** (401) et valider les données | ~1h | Page web (badge) |
| 05 | 🐉 Scoring de dangerosité | **C3 — Flask** | Coder une **logique métier** de scoring et la rendre visuelle | ~1h | Carte web couleur |
| 06 | 🏆 Leaderboard d'arcade | **C8 — SQL** | Écrire des requêtes **paramétrées** (anti-injection) en SQLite | ~1h | Tableau terminal |
| 07 | 🪴 Carnet de la serre | **C8 — SQL** | Un **CRUD** complet + stocker du **JSON** (le volet NoSQL) | ~1h15 | Terminal (emojis) |
| 08 | 🍕 Partage de pizza | **C9 — Tests** | Écrire des tests `pytest` qui **attrapent un bug**, puis le corriger | ~45 min | pytest rouge→vert |
| 09 | 🧪 Tester l'API des héros | **C9 — Tests** | Tester un endpoint Flask : **token, 400, /health** | ~45 min | pytest |

> 🎓 **Compétences visées (référentiel CDA)**
> - **C3** (logique métier sécurisée) et **C8** (accès aux données) exigent du *code visible* à l'examen → exos 03 à 07.
> - **C9** (plans de tests) → exos 08 et 09.
> - Les fondamentaux (01-02) consolident la base Python indispensable au reste.

---

## Conseils de survie

- 🔁 **Teste au fur et à mesure**, ne code pas 50 lignes d'un coup.
- 🧪 Pour les exos Flask : garde un terminal pour le serveur, un autre pour `curl`.
- 🚫 **Jamais** de concaténation de chaînes dans une requête SQL ni dans un calcul de sécurité.
- 🙋 Bloqué·e plus de 15 min ? Regarde l'indice 💡, puis le `corrige/` en dernier recours.
