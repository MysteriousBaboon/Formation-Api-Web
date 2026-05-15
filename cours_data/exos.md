# 🧪 Exercices — Data & Fichiers (3h)

> **Prérequis :** avoir lancé `python 0_setup.py` au moins une fois.
> Chaque exercice doit être un fichier Python séparé : `exo_1.py`, `exo_2.py`, etc.

---

## Exercice 1 — Le CSV des ventes (30 min)

Fichier source : `data/ventes.csv`

1. Charge le CSV avec pandas
2. Affiche :
   - Le nombre total de ventes (lignes)
   - Le **CA total** (somme de `prix * quantite`)
   - Le **panier moyen** (CA total / nb de ventes)
3. Trouve les **3 produits les plus vendus en quantité**
4. Trouve les **3 produits qui rapportent le plus de CA**
5. Exporte le top 3 par CA dans `data/top3_ca.xlsx`

> 💡 `df["nouvelle_col"] = df["a"] * df["b"]` et `df.groupby("col")["autre"].sum().sort_values(ascending=False).head(3)`

---

## Exercice 2 — Nettoyer un dataset crade (45 min)

Fichier source : `data/clients_crade.csv`

Le manager t'a refilé un export bordélique. Tu dois en sortir un fichier propre `clients_propre.csv`.

À faire :

1. Charger le fichier
2. **Doublons** : supprimer les lignes en double (un même client peut apparaître avec des casses différentes — penser à normaliser le nom en minuscules avant de dédupliquer)
3. **Espaces parasites** : `.str.strip()` sur les colonnes texte
4. **Casse email** : tous les emails en minuscules
5. **Âge** : transformer la colonne `Age` en nombre. Les valeurs non-numériques deviennent vides (utilise `pd.to_numeric(..., errors="coerce")`)
6. **Dates** : uniformiser le format en `YYYY-MM-DD` (utilise `pd.to_datetime(..., errors="coerce")`)
7. Lignes sans email valide ou sans nom → à supprimer
8. Exporter dans `data/clients_propre.csv`
9. À la fin, afficher combien de lignes ont été supprimées et combien il en reste

---

## Exercice 3 — Consolider plusieurs fichiers (30 min)

Dossier source : `data/ventes_mensuelles/` (3 fichiers : `janvier.csv`, `fevrier.csv`, `mars.csv`)

1. Liste les fichiers du dossier avec `pathlib`
2. Charge-les tous, **ajoute une colonne `mois`** dérivée du nom de fichier
3. Concatène les 3 DataFrames en un seul (`pd.concat`)
4. Sors un Excel `data/rapport_trimestriel.xlsx` avec **3 onglets** :
   - `Brut` : toutes les lignes concaténées
   - `Par mois` : somme du montant pour chaque mois
   - `Par catégorie` : somme du montant pour chaque catégorie

> 💡 `pd.ExcelWriter("fichier.xlsx") as writer:` puis `df.to_excel(writer, sheet_name="...")`

---

## Exercice 4 — Renommage et tri en masse (30 min)

Dossier source : `data/fichiers_a_renommer/`

1. Lister tous les fichiers du dossier
2. Pour chaque fichier :
   - Mettre l'extension en minuscules
   - Préfixer le nom avec la date du jour : `2025-05-14_<nom_original>`
3. Créer un dossier `data/tries/` puis dedans un sous-dossier par extension (`jpg/`, `txt/`)
4. **Déplacer** chaque fichier renommé dans le bon sous-dossier (`f.rename(destination)`)
5. À la fin, afficher un mini rapport :
   - Nombre de fichiers traités
   - Nombre par extension

> ⚠️ Si tu re-lances le script, les fichiers seront déjà renommés. Pour rejouer proprement : relance `python 0_setup.py`.

---

## Exercice 5 — Mini-rapport PDF (45 min)

Tu reçois la facture `data/facture.pdf`. Imagine que demain tu en reçois 50.

1. Lis le PDF avec `pypdf`, récupère le texte complet
2. Extrais avec des regex :
   - Numéro de facture
   - Date
   - Montant HT
   - Montant TVA
   - Montant TTC
3. Stocke ça dans un dictionnaire
4. **Bonus** : modifie `0_setup.py` (ou fais un nouveau script) pour générer 5 factures différentes, puis ton script doit pondre un Excel `data/recap_factures.xlsx` avec une ligne par facture et les 5 colonnes ci-dessus.

> 💡 Regex de base :
> - `r"Facture\s*#?([\w-]+)"` capture le numéro
> - `r"TOTAL TTC\s*:\s*([\d.]+)"` capture un montant

---

## Bonus — Le projet fil rouge (si tu finis tout)

Construis un script `pipeline.py` qui en **un seul lancement** fait :

1. Lit le CSV de ventes
2. Nettoie + dédoublonne
3. Génère un Excel formaté (avec en-têtes colorés, colonnes ajustées) contenant :
   - Onglet "Synthèse" : CA total, panier moyen, top 5 vendeurs
   - Onglet "Détail" : toutes les ventes triées par date
4. Sauvegarde le fichier avec la date du jour dans le nom : `rapport_2025-05-14.xlsx`

C'est le squelette type d'un **rapport hebdomadaire automatisé**. Tu peux ensuite le déclencher chaque lundi via n8n.
