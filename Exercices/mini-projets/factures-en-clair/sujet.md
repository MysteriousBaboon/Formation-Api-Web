# 🧪 Mini-projet — Factures en clair (~1 jour) · Niveau 🔴 costaud

> **Type d'IA : 🧮 aucune** — extraction de données, base SQL et dataviz. C'est volontaire : ce projet prouve que tu maîtrises l'**accès aux données**, sans IA pour masquer la technique. (Un commentaire généré par IA est proposé en bonus.)
>
> **Prérequis :**
> - `pip install flask matplotlib pypdf` (et `reportlab` pour générer les factures de démo).
> - Lance d'abord `python data/0_setup.py` : il crée 7 factures PDF fictives dans `data/factures_pdf/`.
> - `sqlite3` est déjà dans Python (rien à installer).
>
> 🎒 C'est une **mini-presta freelance** : tu livres un truc qui tourne ET que tu sais expliquer au jury, ligne par ligne.
> 🟥 **C'est LE projet « code visible » du lot** : il prouve les compétences exigées sur l'accès aux données (SQL **et** NoSQL).

---

## 🧑‍💼 Le client / le contexte

Tu viens d'être contacté·e par **Nadia, graphiste freelance**. Ses factures sont des PDF éparpillés dans un dossier. À chaque fin de trimestre, elle ressaisit tout dans un tableur pour suivre son chiffre d'affaires et surveiller le **seuil de franchise de TVA**. C'est long et source d'erreurs. Elle veut un outil qui **lit ses PDF**, **range tout dans une base** et lui sort un **tableau de bord de CA**. Elle te paie une journée.

## 🎯 Le besoin

> « Avale mes PDF de factures, range-les proprement, et montre-moi mon chiffre d'affaires par mois — et préviens-moi si j'approche du seuil de TVA. »

## 📦 Ce que tu livres

- Un module qui **extrait** les infos des PDF (numéro, date, client, montants).
- Une **base SQLite** modélisée (clients ↔ factures, relation 1-N) avec un **CRUD en requêtes paramétrées**.
- Un **export JSON** des factures groupées par client (volet NoSQL).
- Une appli **Flask** : tableau de bord **CA par mois** + **alerte seuil de TVA**.
- Un **README** d'installation + un `.env.example`.

---

## 🧱 Contraintes métier réelles

> Ce ne sont pas des caprices : c'est ce qui sépare un script de hackathon d'une presta livrable.

1. **Budget / temps** : ça tient en une journée ; tout tourne en local, aucun service externe.
2. **Sécurité = anti-injection** : toutes les requêtes SQL sont **paramétrées** (`?`), **jamais** de f-string ni de concaténation dans une requête. C'est le point que le jury vérifie en premier sur cette compétence.
3. **Données / RGPD** : un nom de client est une donnée pro → base locale, pas de partage externe, données minimisées.
4. **Robustesse** : un PDF illisible ou un champ manquant est **signalé** (loggé) et n'interrompt pas le traitement des autres.
5. **Idempotent** : relancer l'import **ne crée pas** de doublons (le numéro de facture est unique).

---

## 🪜 Étapes guidées

> Commit après chaque étape (le jury veut un historique Git qui raconte ta progression).

### 1. Générer les données + squelette (~30 min)
Lance `python data/0_setup.py` (crée les PDF). Crée `app.py` (port **6016**).

### 2. L'extraction : PDF → données (~1h15)
Crée `extraction.py` : lis chaque PDF avec `pypdf`, extrais avec des **regex** le numéro, la date, le client, le total HT et le total TTC.
> 💡 Repris de `cours_data` (pdf + regex) :
> ```python
> import re
> from pypdf import PdfReader
> txt = "\n".join(p.extract_text() for p in PdfReader(chemin).pages)
> numero = re.search(r"Facture N°?\s*([0-9-]+)", txt).group(1)
> client = re.search(r"Client\s*:\s*(.+)", txt).group(1).strip()
> ttc    = float(re.search(r"Total TTC\s*:\s*([0-9.]+)", txt).group(1))
> ```
> ⚠️ Entoure chaque extraction d'un garde-fou : si un champ manque, log et passe au PDF suivant.

### 3. La base relationnelle : modéliser (MCD) + créer (~1h)
Dessine d'abord ton **MCD/MLD** : une table `clients` et une table `factures`, reliées en **1-N** (un client → plusieurs factures) via une **clé étrangère** `client_id`. Crée le schéma SQLite.
> 💡 :
> ```python
> import sqlite3
> con = sqlite3.connect("factures.db"); cur = con.cursor()
> cur.executescript("""
> CREATE TABLE IF NOT EXISTS clients (
>   id INTEGER PRIMARY KEY, nom TEXT UNIQUE NOT NULL);
> CREATE TABLE IF NOT EXISTS factures (
>   id INTEGER PRIMARY KEY, numero TEXT UNIQUE NOT NULL, date TEXT,
>   total_ht REAL, total_ttc REAL,
>   client_id INTEGER REFERENCES clients(id));
> """); con.commit()
> ```

### 4. Le CRUD en requêtes paramétrées 🟥 (~1h15) — *le cœur, à savoir réexpliquer*
Crée `db.py` avec les fonctions d'accès : insérer un client (ou récupérer son id), insérer une facture, lister les factures, calculer le CA. **Tout en requêtes paramétrées.**
> 💡 La règle d'or anti-injection :
> ```python
> # ✅ paramétré : la valeur passe par le 2e argument
> cur.execute("INSERT INTO clients(nom) VALUES (?)", (nom,))
> cur.execute("SELECT id FROM clients WHERE nom = ?", (nom,))
> ```
> ⚠️ **JAMAIS** ça :
> ```python
> # ❌ faille d'injection SQL — interdit, le jury sanctionne
> cur.execute(f"SELECT id FROM clients WHERE nom = '{nom}'")
> ```

### 5. Le volet NoSQL : export JSON (~30 min)
Crée `export_json.py` : exporte toutes les factures **groupées par client** dans `factures_export.json`. C'est ton accès **NoSQL** (un document hiérarchique), pratique pour partager ou archiver.

### 6. Le composant métier + le dashboard (~1h15)
Crée `analyse.py` : **CA par mois** + détection du **seuil de TVA** (ex. franchise auto-entrepreneur). Trace le CA mensuel (matplotlib `Agg`) et affiche le tableau de bord dans `app.py`, avec une **alerte** si le CA cumulé approche du seuil.
> 💡 L'alerte est une simple règle : `if ca_cumule >= 0.9 * SEUIL: alerte = "Tu approches du seuil de TVA"`.

### 7. Tests + finitions (~45 min)
Écris `test_db.py` (`pytest`) : insère un client + 2 factures, vérifie que le CA est correct et qu'un **doublon de numéro** est rejeté. README + `.env.example` + `.gitignore` excluant `*.db`, `factures_export.json`, `data/factures_pdf/`.

---

## ✅ Critères de réussite (grille façon jury CDA)

- [ ] **Toutes** mes requêtes SQL sont **paramétrées** (je sais montrer le `?` et expliquer l'anti-injection).
- [ ] Mon **MCD/MLD** est clair : `clients` 1-N `factures`, clé primaire + clé étrangère.
- [ ] J'ai **les deux** accès : **SQL** (SQLite) **et** **NoSQL** (export JSON).
- [ ] Relancer l'import **ne duplique pas** les factures (numéro unique).
- [ ] Un PDF illisible **ne casse pas** tout l'import (log + on continue).
- [ ] `test_db.py` passe au **vert** (`pytest`).
- [ ] **README** réutilisable + **historique Git** régulier.

---

## 🚀 Bonus (si tu finis en avance)

- Ajoute un **commentaire généré par IA** sur le dashboard (« ton meilleur mois… ») via le client LLM de `cours_llm` — c'est ici que l'IA a du sens, en touche finale.
- Ajoute un **upload de PDF** dans l'appli (l'utilisateur dépose un fichier) avec validation du type.
- Ajoute une table `lignes_facture` (relation 1-N facture → lignes) pour le détail.
- Mets une **CI GitHub Actions** qui lance `pytest` à chaque push — compétence C11.

---

## 🗺️ Compétences CDA mobilisées

| Compétence | Mobilisée ? | Où, concrètement, dans CE projet |
|---|:--:|---|
| C1 — Environnement (.venv/.env/Git) | ✓ | `.env.example`, `.gitignore` (exclut `*.db`), commits par étape |
| C2 — Interfaces (responsive/RGAA) | ~ | Tableau de bord CA lisible |
| C3 — Composants métier 🟥 | ✓ | `extraction.py` + `analyse.py` (CA, seuil TVA), validation, gestion d'erreurs |
| C4 — Gestion de projet | ✓ | User stories + historique Git |
| C5 — Analyse & maquettage | ~ | Besoin de Nadia → MCD avant de coder |
| C6 — Architecture multicouche | ✓ | Extraction → `db.py` (données) → `analyse.py` (métier) → dashboard |
| C7 — Base relationnelle (MCD/MLD) | ✓ | `clients` 1-N `factures`, clé primaire/étrangère, contrainte d'unicité |
| C8 — Accès SQL + NoSQL 🟥 | ✓ | **SQL** : CRUD SQLite **paramétré** ; **NoSQL** : export JSON groupé par client |
| C9 — Plans de tests | ✓ | `test_db.py` (CRUD, calcul CA, rejet des doublons) |
| C10 — Doc de déploiement | — | En bonus (Render) |
| C11 — Mise en prod DevOps | ~ | En bonus : CI GitHub Actions (`pytest`) |
| 🔒 Transversal (ANSSI/RGPD/RGAA/B1) | ✓ | **Anti-injection** (requêtes paramétrées), données minimisées, doc pypdf/SQLite lue en anglais |
