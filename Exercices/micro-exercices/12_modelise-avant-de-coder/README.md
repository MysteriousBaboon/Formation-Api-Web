# 🗃️ Modélise avant de coder (~1h15) — *MCD/MLD et vraie base relationnelle*

> 🎓 **Compétence CDA visée : C7 — Concevoir une base de données relationnelle**
> Le jury veut une **vraie modélisation** (clés, relations, normalisation), pas « des colonnes
> dans un tableur ». Ici tu modélises la base de **Troc'Quartier**, puis tu la crées en SQLite —
> et tu prouves que tes relations tiennent avec une **jointure**.

---

## Le contexte

**Troc'Quartier** (prêt d'objets entre voisins, cf. exos 10-11) a besoin de stocker proprement :

- des **membres** (qui propose, qui emprunte) ;
- des **objets** (chacun appartient à **un** membre) ;
- des **réservations** (un membre emprunte un objet sur une période).

Avant la moindre ligne de code, tu **dessines le modèle** (MCD/MLD), puis tu le traduis en
**tables SQLite** avec clés primaires, clés étrangères et contraintes.

---

## ⚠️ Le piège que cet exo t'apprend à éviter

> — « C'est juste des colonnes dans un tableur ? » — ❌

Mettre `objet1`, `objet2`, `objet3` dans la ligne d'un membre, ou recopier le nom du propriétaire
dans chaque objet, c'est **non normalisé** : redondances, incohérences, données qui se contredisent.
La bonne approche : **une table par entité**, reliée par des **clés étrangères**. Un objet pointe
vers son propriétaire via `proprietaire_id`, jamais en recopiant son nom.

---

## Ce que tu dois construire

À partir de `starter.py` :

1. **Le MCD/MLD** (dans `starter/modele.md` ou en commentaire) : les 3 entités, leurs attributs,
   les relations **1-N** (un membre → plusieurs objets ; un membre → plusieurs réservations ;
   un objet → plusieurs réservations) et la **cardinalité**.
2. **Le schéma SQLite** : `CREATE TABLE` pour `membres`, `objets`, `reservations`, avec
   **clé primaire**, **clé étrangère** (`REFERENCES`), et au moins une **contrainte**
   (`NOT NULL`, `UNIQUE`, ou `CHECK`).
3. **Un jeu de données** : insère quelques membres, objets et réservations (en **requêtes paramétrées**).
4. **Une jointure** : liste les réservations avec *le nom de l'objet*, *le propriétaire* et *l'emprunteur*
   — la preuve que ton modèle relie bien les tables.

---

## 💡 Conseils

- Active les clés étrangères dans SQLite (désactivées par défaut !) :
  ```python
  con.execute("PRAGMA foreign_keys = ON")
  ```
- Une clé étrangère :
  ```sql
  CREATE TABLE objets (
    id INTEGER PRIMARY KEY,
    nom TEXT NOT NULL,
    proprietaire_id INTEGER NOT NULL REFERENCES membres(id)
  );
  ```
- **Normalisation** : aucune donnée recopiée. Le nom du propriétaire est dans `membres`, **une seule fois**.
- Une jointure à 3 tables :
  ```sql
  SELECT o.nom, prop.prenom AS proprietaire, emp.prenom AS emprunteur, r.statut
  FROM reservations r
  JOIN objets o   ON o.id = r.objet_id
  JOIN membres prop ON prop.id = o.proprietaire_id
  JOIN membres emp  ON emp.id = r.emprunteur_id;
  ```
- MCD en Mermaid (`erDiagram`) — pratique pour le dossier (voir `corrige/`).

---

## ✅ Critères de réussite

- [ ] J'ai **3 tables** (une par entité), pas de données recopiées (**normalisé**).
- [ ] Chaque table a une **clé primaire** ; les liens passent par des **clés étrangères** (`REFERENCES`).
- [ ] Au moins une **contrainte** d'intégrité (`NOT NULL` / `UNIQUE` / `CHECK`).
- [ ] `PRAGMA foreign_keys = ON` est activé.
- [ ] Ma **jointure** affiche objet + propriétaire + emprunteur (les relations tiennent).
- [ ] Je sais expliquer ma relation **1-N** et pourquoi je ne recopie pas le nom du propriétaire.

---

## ⭐ Bonus

1. **Intégrité** : tente d'insérer une réservation avec un `objet_id` inexistant → la clé étrangère
   doit **refuser** (grâce au `PRAGMA`).
2. **CHECK** : ajoute `CHECK (date_fin >= date_debut)` sur `reservations`.
3. **Index** : crée un index sur `reservations(objet_id)` et explique à quoi il sert.
4. **N-N assumé** : explique pourquoi `reservations` est en réalité la **table d'association**
   entre `membres` et `objets`.
