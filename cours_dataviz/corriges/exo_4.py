# Corrigé exo 4 — Rapport interactif plotly
import pandas as pd
import plotly.express as px

df = pd.read_csv("exemples/ventes.csv")

fig = px.bar(
    df,
    x="region",
    y="ventes",
    color="categorie",
    title="Ventes par région et catégorie",
    barmode="group",
)
fig.write_html("rapport.html")

# Bonus : version image (nécessite kaleido)
fig.write_image("rapport.png", width=900, height=500)

print("rapport.html + rapport.png générés. Ouvre le .html dans ton navigateur.")