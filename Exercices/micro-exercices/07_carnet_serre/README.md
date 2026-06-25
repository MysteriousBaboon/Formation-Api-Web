# 🪴 Carnet de la serre (~1h15) — *SQLite : le CRUD complet + JSON*

> 🎓 **Compétence CDA visée : C8 — Accès aux données (code visible)**
> Les **4 opérations** d'une base (Créer, Lire, Mettre à jour, Supprimer = CRUD) en
> requêtes **paramétrées**, **plus** un champ **JSON** : le jury exige du SQL **et** du NoSQL.

---

## Le contexte

Tu gères ta collection de plantes d'intérieur. Chaque plante a une fréquence d'arrosage,
et le carnet te dit lesquelles ont **soif** aujourd'hui (💧) ou vont bien (✅). Certaines
infos sont « libres » (pièce, exposition, toxique pour le chat…) : on les range dans un
champ **JSON** — la partie « NoSQL » dans une base SQL.

```
🪴 CARNET DE LA SERRE

#1 Monstera (Monstera deliciosa) — arrosée il y a 9j, tous les 7j   💧 à arroser   [salon]
#2 Cactus (Echinocactus) — arrosé il y a 5j, tous les 21j           ✅ ok          [bureau]
#3 Basilic (Ocimum) — arrosé il y a 3j, tous les 2j                 💧 à arroser   [cuisine]
```

> SQLite est inclus dans Python (`import sqlite3`). La base `serre.db` est créée toute seule.

---

## Ce que tu dois construire

À partir de `starter.py`, écris le **CRUD** (toutes les requêtes **paramétrées** avec `?`) :

1. **`init_db()`** — table `plantes` : `id`, `nom`, `espece`, `frequence` (jours entre arrosages),
   `dernier_arrosage` (date `AAAA-MM-JJ`), `notes` (**JSON** libre).
2. **`ajouter(nom, espece, frequence, dernier_arrosage, notes)`** — **C**reate (`INSERT`),
   `notes` est un **dict** → stocke-le avec `json.dumps(notes)`.
3. **`lister()`** — **R**ead (`SELECT`), renvoie toutes les plantes.
4. **`arroser(id)`** — **U**pdate (`UPDATE ... SET dernier_arrosage = ? WHERE id = ?`) avec la date du jour.
5. **`supprimer(id)`** — **D**elete (`DELETE ... WHERE id = ?`).
6. **`afficher(plantes)`** — montre 💧 si la plante a soif (jours écoulés ≥ fréquence), sinon ✅.
7. **Volet NoSQL** : relis le champ `notes` avec `json.loads(...)` et liste, par exemple,
   les plantes **toxiques pour le chat**.

---

## 💡 Conseils

- Stocker / relire le JSON :
  ```python
  import json
  notes_txt = json.dumps({"piece": "salon", "toxique_chat": True})  # dict -> texte (pour la BDD)
  notes = json.loads(notes_txt)                                      # texte -> dict (à la lecture)
  ```
- Date du jour : `from datetime import date` → `date.today().isoformat()` donne `"2026-06-25"`.
- Jours écoulés : `(date.today() - date.fromisoformat(dernier_arrosage)).days`.
- **Toujours** `WHERE id = ?` avec le paramètre à part — jamais `f"... id = {id}"`.

---

## Pour tester

```bash
python serre.py
```
Tu dois voir l'état initial, puis l'effet de `arroser(1)` (le Monstera repasse en ✅),
puis l'effet de `supprimer(...)`, et enfin la liste des plantes toxiques pour le chat.

---

## ✅ Critères de réussite

- [ ] Les **4 opérations** CRUD fonctionnent, toutes **paramétrées**.
- [ ] Après `arroser(1)`, la plante n'a plus soif (✅).
- [ ] Après `supprimer(id)`, la plante disparaît de la liste.
- [ ] Le champ `notes` est bien stocké en **JSON** et relu en **dict**.
- [ ] Tu sais expliquer la différence entre une colonne classique (`nom`) et le champ `notes`
      souple (quand préférer l'un ou l'autre).

---

## ⭐ Bonus

1. **Requête dans le JSON** : SQLite sait fouiller un champ JSON →
   `SELECT nom FROM plantes WHERE json_extract(notes, '$.toxique_chat') = 1`.
2. **À arroser aujourd'hui** : une fonction qui ne renvoie que les plantes assoiffées.
3. **Historique** : une 2ᵉ table `arrosages` (id_plante, date) reliée par une **clé étrangère**.
