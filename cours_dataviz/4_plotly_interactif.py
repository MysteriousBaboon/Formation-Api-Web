# ============================================================
# 4_plotly_interactif.py — Graphes interactifs avec plotly
# ============================================================
# matplotlib = image statique. plotly = HTML interactif :
# on survole un point pour voir sa valeur, on zoome, on masque
# des séries en cliquant la légende. Parfait pour un rapport
# qu'on envoie par mail (fichier .html autonome).
# ============================================================

import pandas as pd
import plotly.express as px

df = pd.read_csv("exemples/ventes.csv")

# ------------------------------------------------------------
# 1. Barres : on passe le DataFrame + les noms de colonnes
# ------------------------------------------------------------
fig = px.bar(
    df,
    x="region",
    y="ventes",
    color="categorie",      # couleur par catégorie (barres empilées)
    title="Ventes par région et catégorie",
)
fig.write_html("plotly_barres.html")   # fichier autonome, ouvrable au navigateur
# fig.show()                            # décommente pour ouvrir directement

# ------------------------------------------------------------
# 2. Courbe : évolution des ventes par mois
# ------------------------------------------------------------
ventes_mois = df.groupby("mois", sort=False, as_index=False)["ventes"].sum()
fig2 = px.line(
    ventes_mois,
    x="mois",
    y="ventes",
    markers=True,
    title="Évolution des ventes",
)
fig2.write_html("plotly_courbe.html")

# ------------------------------------------------------------
# 3. Camembert
# ------------------------------------------------------------
fig3 = px.pie(df, names="categorie", values="ventes", title="Part des catégories")
fig3.write_html("plotly_camembert.html")

# ------------------------------------------------------------
# 4. Nuage de points (avec survol enrichi)
# ------------------------------------------------------------
fig4 = px.scatter(
    df,
    x="ventes",
    y="region",
    color="categorie",
    size="ventes",
    hover_data=["mois"],    # infos en plus au survol
    title="Ventes par région",
)
fig4.write_html("plotly_scatter.html")

# ------------------------------------------------------------
# 5. Exporter en IMAGE statique (PNG) — nécessite 'kaleido'
# ------------------------------------------------------------
# Utile pour Slack/email où l'on veut une image, pas du HTML.
fig.write_image("plotly_barres.png", width=900, height=500)

print("4 fichiers .html interactifs + 1 .png générés.")
print("Ouvre les .html dans ton navigateur et survole les graphes.")