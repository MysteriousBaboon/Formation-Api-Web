# ============================================================
# 0_setup.py — Génère des factures PDF fictives pour le projet
# ============================================================
# Lance ce script UNE FOIS pour créer data/factures_pdf/ avec
# 7 factures de démo (plusieurs clients, certains reviennent →
# c'est ta relation 1-N client → factures).
#
#   pip install reportlab
#   python 0_setup.py
#
# Les montants sont volontairement "propres" pour que ton extraction
# regex soit vérifiable. Le format est régulier d'une facture à l'autre.
# ============================================================

from pathlib import Path
from reportlab.pdfgen import canvas

DOSSIER = Path(__file__).parent / "factures_pdf"
DOSSIER.mkdir(exist_ok=True)

# numero, date (AAAA-MM-JJ), client, [(designation, total_ht), ...]
FACTURES = [
    ("2026-001", "2026-01-08", "Brasserie Le Phare", [("Création logo", 600.0), ("Charte graphique", 900.0)]),
    ("2026-002", "2026-01-22", "Studio Yoga Zen", [("Affiche événement", 250.0)]),
    ("2026-003", "2026-02-05", "Brasserie Le Phare", [("Menu illustré", 480.0)]),
    ("2026-004", "2026-02-19", "Boutique Pampa", [("Identité visuelle", 1200.0), ("Cartes de visite", 150.0)]),
    ("2026-005", "2026-03-03", "Studio Yoga Zen", [("Refonte site vitrine", 1800.0)]),
    ("2026-006", "2026-03-27", "Cabinet Dr. Lemoine", [("Plaquette de présentation", 540.0)]),
    ("2026-007", "2026-04-14", "Boutique Pampa", [("Bannières réseaux sociaux", 380.0), ("Retouches photos", 220.0)]),
]

TVA = 0.20

for numero, date, client, lignes in FACTURES:
    total_ht = round(sum(montant for _, montant in lignes), 2)
    tva = round(total_ht * TVA, 2)
    total_ttc = round(total_ht + tva, 2)

    chemin = DOSSIER / f"facture_{numero}.pdf"
    c = canvas.Canvas(str(chemin))

    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 800, f"Facture N° {numero}")

    c.setFont("Helvetica", 12)
    c.drawString(100, 770, f"Date : {date}")
    c.drawString(100, 752, f"Client : {client}")
    c.drawString(100, 730, "Emise par : Nadia Cherif - Graphiste freelance")

    c.setFont("Helvetica-Bold", 11)
    c.drawString(100, 700, "Designation")
    c.drawString(400, 700, "Montant HT")

    c.setFont("Helvetica", 11)
    y = 680
    for designation, montant in lignes:
        c.drawString(100, y, designation)
        c.drawString(400, y, f"{montant:.2f} EUR")
        y -= 20

    y -= 10
    c.setFont("Helvetica", 12)
    c.drawString(100, y, f"Total HT : {total_ht:.2f} EUR")
    c.drawString(100, y - 20, f"TVA 20% : {tva:.2f} EUR")
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, y - 42, f"Total TTC : {total_ttc:.2f} EUR")

    c.save()
    print(f"  ✅ {chemin.name}  ({client}, {total_ttc:.2f} EUR TTC)")

print(f"\n{len(FACTURES)} factures générées dans {DOSSIER.resolve()}")
print("Astuce : 'Brasserie Le Phare', 'Studio Yoga Zen' et 'Boutique Pampa' ont")
print("plusieurs factures → c'est ta relation 1-N (un client → plusieurs factures).")
