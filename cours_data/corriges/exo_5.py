# ============================================================
# Exo 5 — Mini-rapport PDF (factures -> Excel)
# ============================================================
# Objectifs :
#   1. Lire le PDF avec pypdf, recuperer le texte
#   2. Extraire avec des regex : numero, date, HT, TVA, TTC
#   3. Stocker dans un dict
#   Bonus : generer 5 factures de demo, parser chacune,
#           pondre data/recap_factures.xlsx
#
#   pip install pypdf reportlab pandas openpyxl
# ============================================================

import re
from pathlib import Path

import pandas as pd
from pypdf import PdfReader
from reportlab.pdfgen import canvas


DATA = Path("data")


# ============================================================
# 1. Helper : extraire les infos d'UN PDF
# ============================================================
# On centralise dans une fonction pour la reutiliser en bonus
# sur les 5 factures generees.
def extraire_facture(chemin_pdf: Path) -> dict:
    reader = PdfReader(chemin_pdf)


    texte = "*********".join(page.extract_text() for page in reader.pages)
    # re.search renvoie None si aucun match. On encapsule pour
    # eviter de repeter "if match: ... else: None" 5 fois.
    def chercher(pattern: str) -> str | None:
        m = re.search(pattern, texte)
        return m.group(1) if m else None

    return {
        "fichier": chemin_pdf.name,
        "numero": chercher(r"Facture\s*#?([\w-]+)"),
        "date": chercher(r"Date\s*:\s*(.+)"),
        "ht": chercher(r"TOTAL HT\s*:\s*([\d.]+)"),
        "tva": chercher(r"TVA[^:]*:\s*([\d.]+)"),
        "ttc": chercher(r"TOTAL TTC\s*:\s*([\d.]+)"),
    }


# ============================================================
# 2. Cas simple : la facture deja generee par 0_setup.py
# ============================================================
print("=== Facture unique ===")
infos = extraire_facture(DATA / "facture.pdf")
for cle, valeur in infos.items():
    print(f"  {cle:8s} : {valeur}")


# ============================================================
# 3. BONUS — generer 5 factures puis les agreger en Excel
# ============================================================
# On fabrique 5 PDF avec des montants differents pour avoir
# de quoi remplir un Excel. En vrai, ces PDF viendraient d'un
# client, d'un scan, d'un dossier de mails...
print("\n=== Generation de 5 factures de demo ===")
factures_dir = DATA / "factures"
factures_dir.mkdir(exist_ok=True)

factures_demo = [
    ("2025-101", "12 mai 2025", 500.00, 100.00, 600.00),
    ("2025-102", "13 mai 2025", 1200.00, 240.00, 1440.00),
    ("2025-103", "14 mai 2025", 75.00, 15.00, 90.00),
    ("2025-104", "15 mai 2025", 3200.00, 640.00, 3840.00),
    ("2025-105", "16 mai 2025", 950.00, 190.00, 1140.00),
]

for numero, date_str, ht, tva, ttc in factures_demo:
    chemin = factures_dir / f"facture_{numero}.pdf"
    c = canvas.Canvas(str(chemin))
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 800, f"Facture #{numero}")
    c.setFont("Helvetica", 12)
    c.drawString(100, 770, "Client : Demo Corp")
    c.drawString(100, 750, f"Date : {date_str}")
    c.drawString(100, 700, f"TOTAL HT : {ht:.2f} EUR")
    c.drawString(100, 680, f"TVA 20% : {tva:.2f} EUR")
    c.drawString(100, 660, f"TOTAL TTC : {ttc:.2f} EUR")
    c.save()

print(f"  {len(factures_demo)} factures generees dans {factures_dir}/")


# ============================================================
# 4. Parser le dossier en boucle -> liste de dicts -> DataFrame
# ============================================================
lignes = [extraire_facture(pdf) for pdf in sorted(factures_dir.glob("*.pdf"))]
df = pd.DataFrame(lignes)

# Les montants sont parses en string par regex. On les convertit
# pour pouvoir trier / sommer dans Excel.
for col in ["ht", "tva", "ttc"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("\n=== Recap ===")
print(df)


# ============================================================
# 5. Export Excel
# ============================================================
sortie = DATA / "recap_factures.xlsx"
df.to_excel(sortie, index=False)
print(f"\nExport OK : {sortie}")