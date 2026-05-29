# 📊 Cours 6 — Datavisualisation avec Python

Transformer des données brutes en graphiques lisibles, puis les exposer dans un micro-service.

## 🎯 Objectifs

À la fin de ce module, tu seras capable de :

- Créer des graphiques avec **matplotlib** (le standard)
- Faire des graphes interactifs avec **plotly**
- Construire des graphes directement depuis un **DataFrame pandas**
- Sauvegarder un graphique en image (PNG)
- Exposer un endpoint **`/api/chart`** qui renvoie une image, appelable depuis n8n

## 📁 Structure

```
cours_dataviz/
├── README.md
├── cours.md               ← Cours complet (à lire en premier)
├── requirements.txt
├── 1_matplotlib_base.py   ← Les bases : ligne, barres, camembert
├── 2_personnalisation.py  ← Titres, couleurs, légendes, axes
├── 3_pandas_plot.py       ← Graphes directement depuis un DataFrame
├── 4_plotly_interactif.py ← Graphes interactifs (HTML)
├── 5_chart_endpoint.py    ← Un endpoint Flask qui renvoie un PNG
├── exos.md                ← 5 exercices progressifs
└── exemples/
    └── ventes.csv
```

## 🚀 Pour démarrer

```bash
cd cours_dataviz
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python 1_matplotlib_base.py
```

## 🔗 Le lien avec le reste

C'est l'étape **"montrer"** de ton parcours :

```
[Scraping/API]  →  [pandas: nettoyer]  →  [DATAVIZ: montrer]  →  [n8n: envoyer en Slack]
```

Le fichier `5_chart_endpoint.py` rebranche tout sur le **cours micro-service** : ton API ne
renvoie plus juste du JSON, mais une vraie image de graphique qu'un workflow n8n peut poster
dans un canal Slack chaque matin.