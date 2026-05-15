# Exo 6 — Catalogue produits (corrigé)

Mini application Flask qui interroge l'API publique **dummyjson** et affiche les produits trouvés.

## Lancement

```bash
pip install -r requirements.txt
python app.py
```

→ Ouvrir `http://127.0.0.1:5000`

## Routes

| Route | Description |
|---|---|
| `GET /` | Formulaire de recherche |
| `GET /resultats?q=phone` | Liste des résultats |
| `GET /resultats?q=phone&tri=prix` | Tri par prix (bonus) |
| `GET /resultats?q=phone&tri=note` | Tri par note (bonus) |
| `GET /produit/1` | Fiche détail (bonus) |

## Ce que le corrigé montre

- `request.args.get("q")` pour lire un paramètre d'URL
- `try/except` autour de l'appel API avec `timeout=10`
- Gestion propre des 3 cas : timeout, erreur réseau, recherche vide
- Passage de variables au template avec `render_template("file.html", produits=...)`
- Template Jinja : `{% for %}`, `{% if %}`, filtres (`|length`, `|format`)
