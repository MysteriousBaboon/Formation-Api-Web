# ============================================================
# common/charts.py — Helper de génération d'images matplotlib
# ============================================================
# /!\ ORDRE IMPORTANT : backend "Agg" (sans écran) AVANT pyplot,
# sinon ça plante sur un serveur. Repris de cours_dataviz.
# ============================================================

import io

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402


def fig_to_png(fig):
    """Transforme une figure matplotlib en buffer PNG en mémoire."""
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=150, bbox_inches="tight")
    plt.close(fig)       # libère la mémoire — crucial sur un serveur
    buf.seek(0)
    return buf
