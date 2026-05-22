# ============================================================
# Bonus — pipeline.py : le rapport hebdo automatise
# ============================================================
# Squelette type d'un script "lance-le chaque lundi" :
#   1. Lit le CSV de ventes
#   2. Nettoie + dedoublonne
#   3. Genere un Excel formate (en-tetes colores, colonnes ajustees)
#      - Onglet "Synthese" : CA total, panier moyen, top 5 vendeurs
#      - Onglet "Detail"   : toutes les ventes triees par date
#   4. Sauvegarde avec la date du jour dans le nom
#
# C'est exactement ce qu'un nocodeur peut declencher depuis n8n
# chaque lundi a 9h pour recevoir le rapport dans sa boite mail.
# ============================================================

from pathlib import Path
from datetime import date

import pandas as pd
from openpyxl.styles import Font, PatternFill, Alignment


DATA = Path("data")


# ============================================================
# 1. Lecture + nettoyage
# ============================================================
df = pd.read_csv(DATA / "ventes.csv")

# Dedoublonnage : si le CSV brut contient deux fois exactement
# la meme ligne, on la garde qu'une fois. drop_duplicates() sans
# argument compare toutes les colonnes.
avant = len(df)
df = df.drop_duplicates()
print(f"Dedoublonnage : {avant} -> {len(df)} lignes")

# Colonne calculee + tri par date pour l'onglet detail
df["total"] = df["prix"] * df["quantite"]
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.sort_values("date")


# ============================================================
# 2. Calculs de synthese
# ============================================================
ca_total = df["total"].sum()
panier_moyen = df["total"].mean()

top_vendeurs = (
    df.groupby("vendeur")["total"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
    .rename(columns={"total": "ca_eur"})
)

# DataFrame "Synthese" : 2 colonnes (indicateur, valeur).
# Plus simple a lire dans Excel qu'un gros dict.
synthese = pd.DataFrame(
    [
        ("CA total (EUR)", round(ca_total, 2)),
        ("Panier moyen (EUR)", round(panier_moyen, 2)),
        ("Nombre de ventes", len(df)),
    ],
    columns=["Indicateur", "Valeur"],
)


# ============================================================
# 3. Export Excel avec mise en forme
# ============================================================
# On nomme le fichier avec la date du jour pour avoir un historique
# automatique : rapport_2025-05-21.xlsx, rapport_2025-05-28.xlsx, etc.
nom_fichier = f"rapport_{date.today().isoformat()}.xlsx"
sortie = DATA / nom_fichier

with pd.ExcelWriter(sortie, engine="openpyxl") as writer:
    synthese.to_excel(writer, sheet_name="Synthese", index=False, startrow=2)
    top_vendeurs.to_excel(writer, sheet_name="Synthese", index=False, startrow=len(synthese) + 6)
    df.to_excel(writer, sheet_name="Detail", index=False)

    # On recupere le workbook pour styliser apres ecriture des donnees.
    wb = writer.book

    # --- Styles communs ---
    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill("solid", fgColor="2E5984")
    titre_font = Font(bold=True, size=14, color="2E5984")
    centre = Alignment(horizontal="center")

    # --- Onglet Synthese : titres de section + en-tetes ---
    ws_synth = wb["Synthese"]
    ws_synth["A1"] = "Indicateurs cles"
    ws_synth["A1"].font = titre_font
    ws_synth[f"A{len(synthese) + 5}"] = "Top 5 vendeurs"
    ws_synth[f"A{len(synthese) + 5}"].font = titre_font

    # Stylise les deux lignes d'en-tete (synthese + top vendeurs)
    for row_idx in (3, len(synthese) + 7):
        for cell in ws_synth[row_idx]:
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = centre

    # --- Onglet Detail : en-tete colore ---
    ws_detail = wb["Detail"]
    for cell in ws_detail[1]:
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = centre

    # --- Ajustement automatique de la largeur des colonnes ---
    # Pour chaque onglet, on regarde la valeur la plus longue de
    # chaque colonne et on ajuste +2 pour la marge.
    for ws in (ws_synth, ws_detail):
        for col_cells in ws.columns:
            longueur = max(len(str(c.value)) if c.value is not None else 0 for c in col_cells)
            lettre = col_cells[0].column_letter
            ws.column_dimensions[lettre].width = longueur + 2

print(f"Rapport genere : {sortie}")