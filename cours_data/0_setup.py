# ============================================================
# 0_setup.py — Génère les fichiers d'exemple pour le cours
# ============================================================
# Lance ce script UNE FOIS au début pour créer le dossier data/
# avec des CSV, Excel et PDF de démo.
#
#   python 0_setup.py
#
# ============================================================

from pathlib import Path
import csv
import json
import random

import pandas as pd
from openpyxl import Workbook
from reportlab.pdfgen import canvas

DATA = Path("data")
DATA.mkdir(exist_ok=True)


# --- 1. Un CSV simple et propre ---------------------------------
with open(DATA / "ventes.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["date", "produit", "categorie", "prix", "quantite", "vendeur"])
    writer.writeheader()
    produits = [
        ("T-shirt", "vetements", 19.90),
        ("Jean", "vetements", 49.90),
        ("Sneakers", "chaussures", 89.00),
        ("Casquette", "accessoires", 14.50),
        ("Pull", "vetements", 39.00),
        ("Bottes", "chaussures", 120.00),
    ]
    vendeurs = ["Alice", "Bob", "Charlie", "Dimitri"]
    for i in range(200):
        produit, cat, prix = random.choice(produits)
        writer.writerow({
            "date": f"2025-{random.randint(1, 6):02d}-{random.randint(1, 28):02d}",
            "produit": produit,
            "categorie": cat,
            "prix": prix,
            "quantite": random.randint(1, 5),
            "vendeur": random.choice(vendeurs),
        })

# --- 2. Un CSV crade (doublons, valeurs manquantes, formats foireux) ---
with open(DATA / "clients_crade.csv", "w", encoding="utf-8", newline="") as f:
    f.write("Nom,Email,Age,Ville,Date_inscription\n")
    f.write("alice DUPONT,alice@mail.com,30,Paris,2024-01-15\n")
    f.write("Bob Martin, BOB@MAIL.COM ,,Lyon,15/02/2024\n")
    f.write("alice dupont,alice@mail.com,30,Paris,2024-01-15\n")  # doublon
    f.write("Charlie,charlie@mail.com,vingt-cinq,Marseille,2024-03-01\n")
    f.write("Dimitri Petrov,dimitri@mail.com,42,,2024-04-20\n")
    f.write(",no-email,99,Toulouse,2024-05-10\n")
    f.write("Eva Lopez,eva@mail.com,28,Bordeaux,2024/06/05\n")
    f.write("BOB MARTIN,bob@mail.com,35,Lyon,15-02-2024\n")  # doublon casse différente

# --- 3. Un fichier Excel ----------------------------------------
wb = Workbook()
ws = wb.active
ws.title = "Commandes"
ws.append(["id", "client", "produit", "montant"])
for i in range(1, 51):
    ws.append([i, f"Client {i}", random.choice(["A", "B", "C"]), round(random.uniform(20, 500), 2)])
wb.save(DATA / "commandes.xlsx")

# --- 4. Plusieurs fichiers à consolider -------------------------
mois_dir = DATA / "ventes_mensuelles"
mois_dir.mkdir(exist_ok=True)
for mois in ["janvier", "fevrier", "mars"]:
    rows = [
        {"date": f"2025-01-{random.randint(1, 28):02d}", "montant": round(random.uniform(50, 2000), 2),
         "categorie": random.choice(["A", "B", "C"])}
        for _ in range(30)
    ]
    pd.DataFrame(rows).to_csv(mois_dir / f"{mois}.csv", index=False)

# --- 5. Un JSON -------------------------------------------------
data = {
    "entreprise": "La Dinguerie",
    "employes": [
        {"nom": "Alice", "poste": "dev", "salaire": 45000},
        {"nom": "Bob", "poste": "designer", "salaire": 42000},
        {"nom": "Charlie", "poste": "manager", "salaire": 60000},
    ]
}
with open(DATA / "entreprise.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# --- 6. Un PDF (facture fictive) --------------------------------
pdf_path = DATA / "facture.pdf"
c = canvas.Canvas(str(pdf_path))
c.setFont("Helvetica-Bold", 16)
c.drawString(100, 800, "Facture #2025-042")
c.setFont("Helvetica", 12)
c.drawString(100, 770, "Client : Acme Corp")
c.drawString(100, 750, "Date : 14 mai 2025")
c.drawString(100, 720, "Description           Quantite     Prix Unitaire     Total")
c.drawString(100, 700, "Service A             3            150.00            450.00")
c.drawString(100, 680, "Service B             1            800.00            800.00")
c.drawString(100, 650, "TOTAL HT : 1250.00 EUR")
c.drawString(100, 630, "TVA 20% : 250.00 EUR")
c.drawString(100, 610, "TOTAL TTC : 1500.00 EUR")
c.save()

# --- 7. Un dossier de fichiers a renommer -----------------------
rename_dir = DATA / "fichiers_a_renommer"
rename_dir.mkdir(exist_ok=True)
for i in range(10):
    (rename_dir / f"IMG_{random.randint(1000, 9999)}.JPG").write_text("fake image content")
    (rename_dir / f"doc_{i}.TXT").write_text("contenu")

print(f"✅ Fichiers générés dans {DATA.resolve()}")
print("Contenu :")
for f in sorted(DATA.rglob("*")):
    if f.is_file():
        print(f"  {f.relative_to(DATA)}")
