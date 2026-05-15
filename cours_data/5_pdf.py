# ============================================================
# 5_pdf.py — Extraire du texte d'un PDF
# ============================================================
# pypdf est la librairie de reference pour PDF en pur Python.
#   pip install pypdf
# ============================================================

from pypdf import PdfReader
from pathlib import Path
import re


# ============================================================
# 1. Lire un PDF page par page
# ============================================================
reader = PdfReader("data/facture.pdf")

print(f"Le PDF contient {len(reader.pages)} page(s)")
print()

texte_complet = ""
for i, page in enumerate(reader.pages):
    print(f"--- Page {i + 1} ---")
    texte = page.extract_text()
    print(texte)
    texte_complet += texte + "\n"


# ============================================================
# 2. Extraire des donnees structurees (regex)
# ============================================================
# Sur une facture, on veut souvent extraire :
# - Le numero
# - La date
# - Le montant total
#
# On utilise des expressions regulieres (regex) pour ca.

print("\n=== Extraction structuree ===")

# Cherche "Facture #2025-042"
match_num = re.search(r"Facture\s*#?([\w-]+)", texte_complet)
if match_num:
    print(f"Numero de facture : {match_num.group(1)}")

# Cherche "TOTAL TTC : 1500.00"
match_ttc = re.search(r"TOTAL TTC\s*:\s*([\d.]+)", texte_complet)
if match_ttc:
    print(f"Montant TTC      : {match_ttc.group(1)} EUR")

# Cherche une date type "14 mai 2025"
match_date = re.search(r"\d{1,2}\s+\w+\s+\d{4}", texte_complet)
if match_date:
    print(f"Date trouvee     : {match_date.group(0)}")


# ============================================================
# 3. Batch — extraire les totaux de TOUS les PDF d'un dossier
# ============================================================
# Cas reel : ton manager te file 50 factures PDF, tu dois lui
# faire un Excel avec le total de chacune.

print("\n=== Batch de PDF ---")
print("(Ici on n'a qu'un PDF mais le code marcherait pour 1000)")

resultats = []
for pdf_path in Path("data").glob("*.pdf"):
    reader = PdfReader(pdf_path)
    texte = "\n".join(page.extract_text() for page in reader.pages)

    total_match = re.search(r"TOTAL TTC\s*:\s*([\d.]+)", texte)
    total = float(total_match.group(1)) if total_match else None

    resultats.append({
        "fichier": pdf_path.name,
        "total_ttc": total,
    })

for r in resultats:
    print(r)


# ============================================================
# Limites
# ============================================================
# - PDF scannes (= une image) : pypdf ne peut RIEN extraire.
#   Il faut alors de l'OCR (ex: pytesseract).
# - PDF avec colonnes complexes : le texte peut sortir dans
#   le mauvais ordre. Pour des PDF tres structures (rapports
#   financiers), regarder pdfplumber qui gere les tableaux.
# ============================================================
