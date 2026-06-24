# ============================================================
# blueprints/data.py — Cours « Manipulation de données »
# ============================================================
# Analyse de CSV avec pandas + génération d'un rapport Excel
# formaté (openpyxl). Inspiré de 2_pandas.py et corriges/pipeline.py.
# ============================================================

import io
import logging
from datetime import date

import pandas as pd
from openpyxl.styles import Font, PatternFill, Alignment
from flask import Blueprint, request, jsonify, send_file

log = logging.getLogger(__name__)

bp = Blueprint("data", __name__)


def _lire_csv(texte):
    """Parse un CSV collé (détecte ',' ou ';') en DataFrame."""
    if not texte or not texte.strip():
        raise ValueError("CSV vide")
    sep = ";" if texte.count(";") > texte.count(",") else ","
    return pd.read_csv(io.StringIO(texte), sep=sep)


@bp.route("/api/data/stats", methods=["POST"])
def stats():
    """Renvoie un aperçu + des statistiques par colonne numérique."""
    data = request.get_json(silent=True) or {}
    try:
        df = _lire_csv(data.get("csv", ""))
    except Exception as exc:
        return jsonify({"error": f"CSV invalide : {exc}"}), 400

    numeriques = df.select_dtypes(include="number")
    stats_cols = {
        col: {
            "min": float(numeriques[col].min()),
            "max": float(numeriques[col].max()),
            "moyenne": round(float(numeriques[col].mean()), 3),
            "somme": round(float(numeriques[col].sum()), 3),
        }
        for col in numeriques.columns
    }
    return jsonify({
        "lignes": int(df.shape[0]),
        "colonnes": list(df.columns),
        "apercu": df.head(5).to_dict(orient="records"),
        "stats_numeriques": stats_cols,
    })


@bp.route("/api/data/report", methods=["POST"])
def report():
    """Génère un classeur Excel formaté (Synthèse + Détail) et le renvoie."""
    data = request.get_json(silent=True) or {}
    try:
        df = _lire_csv(data.get("csv", ""))
    except Exception as exc:
        return jsonify({"error": f"CSV invalide : {exc}"}), 400

    df = df.drop_duplicates()

    # Synthèse : nb lignes + somme/moyenne de chaque colonne numérique.
    lignes_synth = [("Nombre de lignes", len(df))]
    for col in df.select_dtypes(include="number").columns:
        lignes_synth.append((f"{col} — somme", round(float(df[col].sum()), 2)))
        lignes_synth.append((f"{col} — moyenne", round(float(df[col].mean()), 2)))
    synthese = pd.DataFrame(lignes_synth, columns=["Indicateur", "Valeur"])

    buf = io.BytesIO()
    with pd.ExcelWriter(buf, engine="openpyxl") as writer:
        synthese.to_excel(writer, sheet_name="Synthese", index=False, startrow=2)
        df.to_excel(writer, sheet_name="Detail", index=False)

        wb = writer.book
        header_font = Font(bold=True, color="FFFFFF")
        header_fill = PatternFill("solid", fgColor="2E5984")
        titre_font = Font(bold=True, size=14, color="2E5984")
        centre = Alignment(horizontal="center")

        ws_synth = wb["Synthese"]
        ws_synth["A1"] = "Indicateurs clés"
        ws_synth["A1"].font = titre_font
        for cell in ws_synth[3]:
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = centre

        ws_detail = wb["Detail"]
        for cell in ws_detail[1]:
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = centre

        for ws in (ws_synth, ws_detail):
            for col_cells in ws.columns:
                longueur = max((len(str(c.value)) if c.value is not None else 0)
                               for c in col_cells)
                ws.column_dimensions[col_cells[0].column_letter].width = longueur + 2

    buf.seek(0)
    nom = f"rapport_{date.today().isoformat()}.xlsx"
    return send_file(
        buf,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        as_attachment=True,
        download_name=nom,
    )
