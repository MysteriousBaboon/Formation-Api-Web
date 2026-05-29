# 🧪 Exercices — Datavisualisation (≈ 2h30)

> Avant de commencer : `pip install -r requirements.txt`.
> Le CSV de travail est dans `exemples/ventes.csv`.
> Chaque exo a son corrigé dans `corriges/`.

---

## Exercice 1 — Premier graphe propre (20 min)

Crée `exo_1.py`.

À partir de ces données :

```python
mois = ["Jan", "Fev", "Mar", "Avr", "Mai", "Juin"]
visiteurs = [1200, 1500, 1100, 1800, 2100, 2500]
```

1. Trace une **courbe** des visiteurs par mois
2. Ajoute un titre, des labels d'axes
3. Mets une grille légère sur l'axe Y
4. **Sauvegarde** en `visiteurs.png` (dpi=150) — pas de `plt.show()`

> 💡 N'oublie pas `plt.close()` après le `savefig`.

---

## Exercice 2 — Le bon graphe pour la bonne donnée (25 min)

Crée `exo_2.py`. Tu reçois la répartition d'un budget :

```python
postes = ["Salaires", "Marketing", "Loyer", "Logiciels", "Autres"]
montants = [45000, 12000, 8000, 5000, 3000]
```

1. Choisis le **bon type de graphe** pour une répartition (indice : parts d'un tout)
2. Affiche les **pourcentages** sur chaque part
3. Donne-lui un titre
4. Sauvegarde en `budget.png`

Puis, dans le même fichier, compare 2 années de CA en **barres groupées** :

```python
annees = ["2024", "2025", "2026"]
ca_france = [120, 150, 180]
ca_export = [40, 55, 90]
```

> 💡 Pour 2 séries de barres côte à côte, le plus simple : passe par un DataFrame pandas
> `pd.DataFrame({"France": ca_france, "Export": ca_export}, index=annees).plot(kind="bar")`.

---

## Exercice 3 — Dashboard depuis le CSV (30 min)

Crée `exo_3.py`. Charge `exemples/ventes.csv` avec pandas et génère **3 images** :

1. `dash_region.png` : barres des ventes totales **par région**
2. `dash_categorie.png` : camembert de la répartition des ventes **par catégorie**
3. `dash_mois.png` : courbe des ventes totales **par mois**

Contraintes :
- Utilise `groupby` (et/ou `pivot_table`)
- Chaque graphe a un titre clair
- Les 3 fichiers sont sauvegardés, aucun `plt.show()`

> 💡 C'est exactement ce qu'un workflow n8n peut générer chaque matin sur tes vraies données.

---

## Exercice 4 — Rapport interactif plotly (25 min)

Crée `exo_4.py`. À partir de `exemples/ventes.csv` :

1. Fais un graphe **interactif** (plotly) des ventes par région, coloré par catégorie
2. Sauvegarde-le en `rapport.html`
3. Ouvre le fichier dans ton navigateur : survole les barres, clique la légende
4. Bonus : exporte aussi une version PNG avec `fig.write_image()`

> 💡 `import plotly.express as px` puis `px.bar(df, x=..., y=..., color=...)`.

---

## Exercice 5 — Endpoint graphique (40 min)

Le projet fil rouge : un micro-service qui renvoie un graphe. Crée `exo_5.py` (port 6005).

Endpoint : **`POST /api/graphique`** (protégé par token)

Reçoit :

```json
{
  "titre": "Top produits",
  "labels": ["iPhone", "Galaxy", "Pixel"],
  "valeurs": [999, 899, 799],
  "type": "bar"
}
```

Doit **renvoyer une image PNG** du graphe.

Contraintes :
1. Backend `matplotlib.use("Agg")` AVANT d'importer pyplot
2. Décorateur `@require_token` (token depuis `.env`)
3. Valider : `labels` et `valeurs` sont des listes de même longueur, non vides → sinon 400
4. Gérer au moins `type` = `bar` et `line`
5. Renvoyer l'image via `send_file(buf, mimetype="image/png")`, image générée en mémoire (`io.BytesIO`)

Teste avec :

```bash
curl -X POST http://127.0.0.1:6005/api/graphique \
  -H "Authorization: Bearer TON_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"titre":"Top","labels":["A","B","C"],"valeurs":[10,20,15],"type":"bar"}' \
  --output sortie.png
```

Ouvre `sortie.png` : tu as un endpoint qui produit des graphiques à la demande. 🎉

---

## Récap

| Compétence | Exo |
|---|---|
| Créer et sauvegarder un graphe | 1 |
| Choisir le bon type de graphe | 2 |
| Graphes depuis un DataFrame (groupby/pivot) | 3 |
| Graphes interactifs (plotly) | 4 |
| Servir une image via une API (lien micro-service) | 5 |