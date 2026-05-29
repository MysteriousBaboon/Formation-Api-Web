# 📚 Cours — Datavisualisation avec Python

> Une donnée que personne ne comprend ne sert à rien. La datavis, c'est l'étape qui transforme un tableau de chiffres en quelque chose qu'un humain lit en 2 secondes.

---

## 1. Pourquoi visualiser ?

Tu sais déjà **récupérer** (scraping, API) et **nettoyer** (pandas) la donnée. Mais un client,
un boss, un workflow n8n n'ont que faire d'un DataFrame de 5000 lignes. Ce qu'ils veulent :

- Une **courbe** qui monte ou qui descend
- Un **camembert** qui dit où part le budget
- Un **graphe à barres** qui compare des catégories

La datavis, c'est le dernier kilomètre : rendre la donnée **décidable**.

---

## 2. Les outils Python

| Outil | Pour quoi | Niveau |
|---|---|---|
| **matplotlib** | Le standard, tout faire | Facile à Moyen |
| **pandas .plot()** | Graphe direct depuis un DataFrame | Facile |
| **seaborn** | matplotlib en plus joli, stats | Moyen |
| **plotly** | Graphes interactifs (zoom, survol) | Moyen |

Dans ce cours on se concentre sur **matplotlib** (incontournable) et **plotly** (le "waouh"
interactif). seaborn est mentionné en bonus.

---

## 3. Anatomie d'un graphique matplotlib

```python
import matplotlib.pyplot as plt

x = ["Jan", "Fev", "Mar", "Avr"]
y = [100, 130, 90, 160]

plt.plot(x, y)          # une courbe
plt.title("Ventes 2026")
plt.xlabel("Mois")
plt.ylabel("Ventes (k€)")
plt.show()              # affiche la fenêtre
```

Le trio à retenir : **données → `plt.qqchose()` → `plt.show()`**.

---

## 4. Les types de graphes essentiels

```python
plt.plot(x, y)      # courbe        → évolution dans le temps
plt.bar(x, y)       # barres        → comparer des catégories
plt.barh(x, y)      # barres horiz. → idem, noms longs
plt.scatter(x, y)   # nuage         → corrélation entre 2 variables
plt.pie(valeurs, labels=noms)  # camembert → répartition (parts d'un tout)
plt.hist(donnees)   # histogramme   → distribution d'une variable
```

**Règle de choix rapide :**
- Évolution → courbe
- Comparaison → barres
- Répartition → camembert (max 5-6 parts, sinon illisible)
- Relation → nuage de points

---

## 5. Sauvegarder au lieu d'afficher

`plt.show()` ouvre une fenêtre — inutile sur un serveur. Pour générer un fichier :

```python
plt.savefig("graphique.png", dpi=150, bbox_inches="tight")
plt.close()   # IMPORTANT : libère la mémoire, sinon les graphes s'empilent
```

- `dpi=150` : qualité (150 = bien pour le web, 300 = impression)
- `bbox_inches="tight"` : enlève les marges blanches inutiles
- `plt.close()` : à TOUJOURS appeler après un savefig dans une boucle ou un serveur

---

## 6. Personnaliser (le minimum pour faire pro)

```python
plt.figure(figsize=(10, 5))           # taille en pouces (largeur, hauteur)
plt.bar(x, y, color="#2563eb")        # couleur en hex
plt.title("Ventes par région", fontsize=14, fontweight="bold")
plt.grid(axis="y", alpha=0.3)         # grille légère sur l'axe Y
plt.xticks(rotation=45)               # incliner les labels (noms longs)
plt.tight_layout()                    # évite que ça déborde
```

Une légende quand tu as plusieurs séries :

```python
plt.plot(x, ventes_2025, label="2025")
plt.plot(x, ventes_2026, label="2026")
plt.legend()
```

---

## 7. Graphes directement depuis pandas

C'est là que ça devient puissant : pandas branche matplotlib tout seul.

```python
import pandas as pd

df = pd.read_csv("ventes.csv")

df.plot(x="mois", y="ventes", kind="line")     # courbe
df.plot(x="region", y="ca", kind="bar")        # barres
df["categorie"].value_counts().plot(kind="pie")  # camembert des fréquences

import matplotlib.pyplot as plt
plt.savefig("rapport.png")
```

`kind=` accepte : `line`, `bar`, `barh`, `hist`, `box`, `pie`, `scatter`, `area`.

Un `groupby` + `.plot()` = un mini-dashboard en 2 lignes :

```python
df.groupby("region")["ca"].sum().plot(kind="barh", title="CA par région")
```

---

## 8. Graphes interactifs avec plotly

matplotlib c'est statique (une image). plotly génère du **HTML interactif** : on survole,
on zoome, on masque des séries. Parfait pour un rapport qu'on envoie par mail.

```python
import plotly.express as px

fig = px.bar(df, x="region", y="ca", title="CA par région", color="region")
fig.show()                      # ouvre dans le navigateur
fig.write_html("rapport.html")  # sauvegarde un fichier autonome
fig.write_image("rapport.png")  # image statique (nécessite 'kaleido')
```

`plotly.express` (importé `px`) couvre 90% des besoins : `px.line`, `px.bar`, `px.pie`,
`px.scatter`, `px.histogram`. Tu passes un DataFrame et les noms de colonnes, c'est tout.

---

## 9. Renvoyer un graphique depuis une API

C'est le pont avec le **cours micro-service**. Au lieu de sauver un fichier, tu renvoies
l'image directement dans la réponse HTTP, en mémoire :

```python
import io
import matplotlib
matplotlib.use("Agg")   # backend SANS interface (obligatoire sur un serveur)
import matplotlib.pyplot as plt
from flask import Flask, send_file

app = Flask(__name__)

@app.route("/api/chart")
def chart():
    plt.figure()
    plt.bar(["A", "B", "C"], [10, 25, 15])

    buf = io.BytesIO()              # un "fichier" en mémoire
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)                     # on se replace au début du buffer

    return send_file(buf, mimetype="image/png")
```

Deux points cruciaux côté serveur :
1. **`matplotlib.use("Agg")`** AVANT d'importer pyplot — sinon ça plante (pas d'écran).
2. **`io.BytesIO`** : on évite d'écrire sur le disque, l'image vit en mémoire le temps de la réponse.

Voir `5_chart_endpoint.py` pour la version complète avec données en POST.

---

## 10. Aller plus loin

- **seaborn** : `import seaborn as sns` — graphes statistiques magnifiques en une ligne
  (`sns.heatmap`, `sns.boxplot`). Construit sur matplotlib.
- **Sous-graphes** : `fig, axes = plt.subplots(2, 2)` pour plusieurs graphes dans une image.
- **Thèmes** : `plt.style.use("seaborn-v0_8")` ou `"ggplot"` pour changer le look d'un coup.
- **Dashboards** : Streamlit ou Dash pour une vraie app web de visualisation.

Pour ce cours on reste sur l'essentiel : créer un graphe propre, le sauver, et le servir via une API.