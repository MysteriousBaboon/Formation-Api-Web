# 🏆 Leaderboard d'arcade (~1h) — *SQLite & requêtes paramétrées*

> 🎓 **Compétence CDA visée : C8 — Accès aux données (code visible)**
> Écrire des requêtes **paramétrées** (le `?`), jamais de concaténation de chaînes.
> C'est **LE** réflexe anti-injection SQL que le jury vérifie en priorité.

---

## Le contexte

Tu codes le tableau des scores d'une borne d'arcade rétro. Les joueurs entrent leur
pseudo (3 lettres, façon vieux flipper) et leur score. Ton programme stocke tout dans
une base **SQLite** et affiche le **Top 10** avec les médailles 🥇🥈🥉.

```
🏆 LEADERBOARD ARCADE

🥇  MARIO              15200 pts
🥈  LINK               12300 pts
🥉  KIRBY              11000 pts
 4. YOSHI              10250 pts
 5. ZELDA               9800 pts
```

> Pas d'installation : **SQLite est inclus dans Python** (`import sqlite3`). La base est
> un simple fichier `arcade.db` créé automatiquement à côté de ton script.

---

## ⚠️ Le piège que cet exo t'apprend à éviter

Pour insérer un score, on est tenté d'écrire :

```python
# ❌ NE FAIS JAMAIS ÇA — faille d'injection SQL
conn.execute(f"INSERT INTO scores (joueur, points) VALUES ('{joueur}', {points})")
```

Si un petit malin entre le pseudo `Bobby'); DROP TABLE scores;--`, **ta table est détruite**.
La bonne façon, c'est la requête **paramétrée** (les valeurs passent à part, jamais collées au texte) :

```python
# ✅ TOUJOURS comme ça
conn.execute("INSERT INTO scores (joueur, points) VALUES (?, ?)", (joueur, points))
```

---

## Ce que tu dois construire

À partir de `starter.py`, écris ces fonctions :

1. **`init_db()`** — crée la table `scores` :
   `id` (clé primaire auto), `joueur` (texte), `points` (entier), `cree_le` (date auto).
2. **`ajouter_score(joueur, points)`** — `INSERT` **paramétré** (`?`).
3. **`top_scores(n=10)`** — `SELECT ... ORDER BY points DESC LIMIT ?` → renvoie la liste.
4. **`afficher(top)`** — affiche le classement avec 🥇🥈🥉 pour les 3 premiers.
5. Dans le `main` : insère quelques scores **dont un pseudo piégé**, affiche le Top 5,
   puis **prouve** que la table a survécu (la requête paramétrée a neutralisé l'injection).

---

## 💡 Conseils

- Connexion : `conn = sqlite3.connect("arcade.db")`. Avec `with sqlite3.connect(...) as conn:`
  le `commit` est automatique.
- Créer la table sans planter si elle existe : `CREATE TABLE IF NOT EXISTS ...`
  (ou `DROP TABLE IF EXISTS scores` au début pour repartir propre à chaque lancement).
- Date automatique côté SQL : colonne `cree_le TEXT DEFAULT CURRENT_TIMESTAMP`.
- `LIMIT ?` : le paramètre se passe **aussi** par `?` → `execute("... LIMIT ?", (n,))`.
- Aligner l'affichage : `f"{joueur:<16} {points:>7} pts"`.

---

## ✅ Critères de réussite

- [ ] Le Top est trié du **plus haut** au plus bas score.
- [ ] **Toutes** les requêtes utilisent `?`, **aucune** f-string ni `+` dans le SQL.
- [ ] Le pseudo `Bobby'); DROP TABLE scores;--` est **stocké tel quel** et la table **existe toujours**.
- [ ] Tu sais expliquer **pourquoi** `?` protège (les données ne sont jamais interprétées comme du code SQL).

---

## ⭐ Bonus

1. **Meilleur score par joueur** : un même pseudo peut jouer plusieurs fois →
   `GROUP BY joueur` + `MAX(points)`.
2. **Anti-triche** : refuse un score négatif ou > 999999 avant l'insert.
3. **Recherche** : `chercher(pseudo)` qui renvoie tous les scores d'un joueur (`WHERE joueur = ?`).
