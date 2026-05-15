# 📚 Cours — Manipulation de données et fichiers en Python

> Tout ce que tu vas voir ici remplace une journée de manipulation manuelle sur Excel.

---

## 1. Pourquoi Python plutôt qu'Excel ?

Excel est **génial** pour explorer 100 lignes à la main.
Python est **imbattable** dès que :

- Tu as **plusieurs fichiers** à traiter en même temps
- Le format des données est **bordélique** (dates, doublons, encodages...)
- Tu dois **répéter** le même traitement chaque semaine
- Tu veux **automatiser** le pipeline complet (lecture → traitement → export → email)

---

## 2. Les formats que tu vas rencontrer

| Format | Pour quoi | Librairie Python |
|---|---|---|
| **CSV** | Le format universel d'échange | `csv` (natif), `pandas` |
| **Excel** (`.xlsx`) | Ce que t'envoient les humains | `openpyxl`, `pandas` |
| **JSON** | Réponses d'API, configs | `json` (natif) |
| **PDF** | Factures, contrats | `pypdf` |

---

## 3. CSV — Le format "tableau" universel

Un CSV c'est un tableau en texte brut, séparé par des virgules (ou des `;` en France).

```csv
nom,age,ville
Alice,30,Paris
Bob,25,Lyon
```

### Lire un CSV (méthode native)

```python
import csv

with open("data.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for ligne in reader:
        print(ligne["nom"], ligne["age"])
```

### Écrire un CSV

```python
import csv

lignes = [
    {"nom": "Alice", "age": 30},
    {"nom": "Bob", "age": 25},
]

with open("sortie.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["nom", "age"])
    writer.writeheader()
    writer.writerows(lignes)
```

> 💡 Toujours préciser `encoding="utf-8"` sinon les accents explosent sur Windows.

---

## 4. Pandas — La bibliothèque qui change la vie

Pandas, c'est Excel mais en Python : tu charges un fichier, il devient un **DataFrame** (un gros tableau intelligent).

### Charger un fichier

```python
import pandas as pd

df = pd.read_csv("ventes.csv")
df = pd.read_excel("ventes.xlsx")    # même API !
df = pd.read_json("ventes.json")
```

### Les opérations qu'on fait 80% du temps

```python
df.head(10)                        # 10 premières lignes
df.shape                           # (nombre_lignes, nombre_colonnes)
df.columns                         # liste des colonnes
df.describe()                      # stats automatiques

df["prix"].mean()                  # moyenne d'une colonne
df["prix"].sum()                   # somme

df[df["prix"] > 100]               # filtrer
df.sort_values("prix", ascending=False)   # trier
df.drop_duplicates()               # supprimer les doublons

df["total"] = df["prix"] * df["quantite"]    # créer une colonne
df = df.dropna()                   # supprimer lignes avec valeurs vides

df.to_excel("propre.xlsx", index=False)      # exporter
```

### Le pattern "groupby" (LE truc qui sert tout le temps)

```python
# CA par catégorie
df.groupby("categorie")["total"].sum()

# Nombre de ventes par vendeur
df.groupby("vendeur").size()
```

---

## 5. Excel avancé — openpyxl

Pandas suffit pour 90% des cas. Mais si tu veux **mettre en forme** (couleurs, polices, fusions de cellules), il faut `openpyxl`.

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

wb = Workbook()
ws = wb.active
ws.title = "Rapport"

ws["A1"] = "Nom"
ws["B1"] = "Total"

# Mettre en gras la ligne d'en-tête
for cell in ws[1]:
    cell.font = Font(bold=True)
    cell.fill = PatternFill("solid", fgColor="FFD700")

ws.append(["Alice", 1200])
ws.append(["Bob", 800])

wb.save("rapport.xlsx")
```

---

## 6. Pathlib — Manipuler fichiers et dossiers proprement

`pathlib` remplace `os.path` et tout son bordel.

```python
from pathlib import Path

dossier = Path("data")

# Lister tous les .csv
for fichier in dossier.glob("*.csv"):
    print(fichier.name)

# Récursif (sous-dossiers inclus)
for fichier in dossier.rglob("*.pdf"):
    print(fichier)

# Créer un dossier
Path("output").mkdir(exist_ok=True)

# Renommer
ancien = Path("vieux.csv")
ancien.rename("nouveau.csv")

# Vérifier
chemin = Path("data/fichier.csv")
if chemin.exists():
    print(chemin.stat().st_size, "octets")
```

---

## 7. PDF — Extraire du texte

```python
from pypdf import PdfReader

reader = PdfReader("facture.pdf")

for page in reader.pages:
    print(page.extract_text())
```

> ⚠️ L'extraction PDF est imparfaite : selon le PDF (scanné vs natif), tu auras du texte propre ou du charabia. Pour les PDF scannés, il faudrait de l'OCR (Tesseract) — hors scope de ce cours.

---

## 8. Le combo gagnant : Path + Pandas

Le scénario typique d'automatisation :

```python
from pathlib import Path
import pandas as pd

# 1. Lister tous les fichiers du dossier
fichiers = list(Path("ventes_mensuelles").glob("*.csv"))

# 2. Lire tous les CSV et les empiler
dfs = [pd.read_csv(f) for f in fichiers]
df_total = pd.concat(dfs, ignore_index=True)

# 3. Nettoyer
df_total = df_total.drop_duplicates()
df_total["date"] = pd.to_datetime(df_total["date"])

# 4. Agréger
rapport = df_total.groupby("categorie")["montant"].sum()

# 5. Exporter
rapport.to_excel("rapport_consolide.xlsx")
```

**Voilà.** Ce script en 10 lignes fait le travail d'un stagiaire pendant 2 jours.

---

## 9. Pièges classiques

| Piège | Solution |
|---|---|
| Accents qui explosent | Toujours `encoding="utf-8"` |
| Dates qui restent en texte | `pd.to_datetime(df["date"])` |
| Excel avec `;` au lieu de `,` | `pd.read_csv("...", sep=";")` |
| Cellules vides → erreurs | `df.dropna()` ou `df.fillna(0)` |
| `pip install` ne marche pas | Activer le venv d'abord ! |

---

## 10. Pour aller plus loin (hors cours)

- **Plotly / matplotlib** pour générer des graphiques
- **smtplib** pour envoyer le rapport par email
- **schedule** ou cron pour exécuter ton script chaque lundi matin
- Brancher la sortie sur **n8n** pour orchestrer le tout
