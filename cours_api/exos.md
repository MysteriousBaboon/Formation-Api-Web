# Exercices — APIs & Python `requests`

> **Prérequis :** `pip install requests python-dotenv`  
> Pour chaque exercice, gérer les erreurs avec `try/except` et toujours mettre un `timeout=10`.

---

## Exercice 1 — Échauffement · GitHub API (20 min)

**API :** [https://api.github.com](https://api.github.com) pas de clé requise

### Objectif

1. Récupérer les infos de l'utilisateur GitHub `torvalds`
2. Afficher son nombre de followers et sa bio
3. Récupérer la liste de ses repos publics et afficher les **5 plus populaires** (triés par `stargazers_count`)

### Endpoints utiles

| Action | Endpoint |
|---|---|
| Infos utilisateur | `GET /users/{username}` |
| Repos publics | `GET /users/{username}/repos` |

---

## Exercice 2 — Météo (30 min)

**API :** [https://open-meteo.com/](https://open-meteo.com/) gratuite, pas de clé

### Objectif

1. Récupérer la météo actuelle à **Reims** (lat `49.26`, lon `4.03`)
2. Afficher : température actuelle, vitesse du vent, code météo

### Bonus

Créer une fonction `meteo(ville)` qui :
- Convertit un nom de ville en coordonnées via l'API de géocodage Open-Meteo
- Puis récupère la météo, **deux appels chaînés**

### Endpoints utiles

| Action | Endpoint |
|---|---|
| Météo actuelle | `GET https://api.open-meteo.com/v1/forecast` |
| Géocodage | `GET https://geocoding-api.open-meteo.com/v1/search` |

---

## Exercice 3 — Authentification · TheMovieDB (30 min)

**API :** [https://www.themoviedb.org/](https://www.themoviedb.org/), inscription gratuite, clé API à générer

### Objectif

1. Créer un compte et récupérer une clé API
2. La stocker dans un fichier `.env` (ne jamais la mettre dans le code)
3. Rechercher le film **"Inception"** via l'API
4. Pour le premier résultat, afficher : titre, année, note, synopsis
5. Récupérer et afficher les **3 acteurs principaux**

### Endpoints utiles

| Action | Endpoint |
|---|---|
| Recherche film | `GET /search/movie?query=Inception` |
| Casting | `GET /movie/{id}/credits` |

### Rappel `.env`

```
TMDB_API_KEY=ta_cle_ici
```

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("TMDB_API_KEY")
```

---

## Exercice 4 — POST, PUT, DELETE · JSONPlaceholder (30 min)

**API :** [https://jsonplaceholder.typicode.com/](https://jsonplaceholder.typicode.com/) — bac à sable, pas de clé

### Objectif

Enchaîner les 4 opérations dans un seul script en loggant chaque étape :

1. **Créer** un post (`POST /posts`) avec un titre, un corps et un `userId`
2. **Vérifier** que le code de retour est `201`
3. **Modifier** ce post (`PUT /posts/{id}`)
4. **Supprimer** ce post (`DELETE /posts/{id}`) et vérifier le `200`

### Méthodes HTTP à utiliser

```python
requests.post(url, json=data)
requests.put(url, json=data)
requests.delete(url)
```

---

## Exercice 5 — Pagination & persistance · PokéAPI (45 min)

**API :** [https://pokeapi.co/](https://pokeapi.co/), pas de clé

### Objectif

1. Récupérer la liste des **150 premiers Pokémon** (attention à `limit` et `offset`)
2. Pour chacun, appeler l'endpoint détail pour obtenir : nom, taille, poids, types
3. Sauvegarder le tout dans un fichier `pokemons.json`

### Bonus

- Ajouter un `time.sleep(0.1)` entre chaque appel pour ne pas surcharger l'API
- Entourer chaque appel détail d'un `try/except` pour ne pas bloquer si un Pokémon échoue

### Endpoints utiles

| Action | Endpoint |
|---|---|
| Liste paginée | `GET /api/v2/pokemon?limit=50&offset=0` |
| Détail | `GET /api/v2/pokemon/{name}` |

---

# Exercice 6 — Projet fil rouge (1h30)

## Contexte métier

Tu viens d'être recruté comme développeur junior dans une petite agence e-commerce.
Ton manager te demande un outil interne simple : **un tableau de bord qui affiche les produits tendance du moment** pour aider l'équipe à alimenter leur catalogue.

Pas besoin de coder le scraping, pas besoin de base de données, tu vas brancher une API publique et afficher les résultats dans une mini app web Flask.

---

## Ce que tu vas construire

Une application Flask avec **deux pages** :

| Route | Ce qu'elle fait |
|---|---|
| `GET /` | Formulaire : l'utilisateur entre une catégorie (ex: `smartphones`, `running shoes`) |
| `GET /resultats?q=...` | Affiche les produits trouvés : nom, prix, note, nombre d'avis |

**API utilisée :** [https://dummyjson.com/](https://dummyjson.com/), gratuite, pas de clé, données e-commerce réalistes.

---

## Structure du projet

```
projet_catalogue/
├── app.py
├── .env
├── templates/
│   ├── index.html
│   └── resultats.html
└── requirements.txt
```

---

## Étapes guidées

### 1. Installer les dépendances

```bash
pip install flask requests python-dotenv
```

`requirements.txt` :
```
flask
requests
python-dotenv
```

### 2. Explorer l'API avant de coder

Ouvre ces URLs dans ton navigateur et observe le JSON retourné :

- Liste de produits : `https://dummyjson.com/products?limit=10`
- Recherche : `https://dummyjson.com/products/search?q=phone`
- Détail produit : `https://dummyjson.com/products/1`

> **Règle d'or :** toujours lire la réponse JSON à la main avant d'écrire une seule ligne de code.

### 3. Coder `app.py`

Ton fichier Flask doit :

1. Définir une route `/` qui affiche un formulaire HTML
2. Définir une route `/resultats` qui :
   - Récupère le paramètre `q` depuis l'URL (`request.args.get("q")`)
   - Appelle `https://dummyjson.com/products/search?q={q}&limit=12`
   - Passe les produits au template `resultats.html`
3. Gérer le cas où l'API ne répond pas (afficher un message d'erreur propre)

### 4. Créer les templates

**`index.html`** — un formulaire simple :
- Un champ texte pour la catégorie
- Un bouton "Rechercher"
- L'action du formulaire pointe vers `/resultats`

**`resultats.html`** — pour chaque produit, afficher :
- Le nom (`title`)
- La marque (`brand`)
- Le prix (`price`) en €
- La note (`rating`) sur 5
- Le nombre d'avis (`stock`) — bonus : afficher "Rupture" si `stock == 0`

---

## Exemple de réponse API

```json
{
  "products": [
    {
      "id": 1,
      "title": "iPhone 9",
      "brand": "Apple",
      "price": 549.99,
      "rating": 4.69,
      "stock": 94,
      "category": "smartphones"
    }
  ],
  "total": 1,
  "limit": 12
}
```

---

## Critères de réussite

- [ ] L'app se lance sans erreur
- [ ] Une recherche vide ou invalide n'affiche pas de crash, un message clair à la place
- [ ] Gestion des erreurs réseau (`try/except`, `timeout=10`)
- [ ] Les templates sont dans `templates/`, aucun HTML dans `app.py`

---

## Bonus (si tu as du temps)

**Niveau 1 — Trier les résultats**
Ajouter un paramètre `tri` dans l'URL (`?q=phone&tri=prix` ou `tri=note`) et trier la liste côté Python avant de l'envoyer au template.

**Niveau 2 — Catégories prêtes à l'emploi**
Appeler `https://dummyjson.com/products/categories` au démarrage de l'app et afficher les catégories disponibles sous forme de boutons cliquables sur la page d'accueil.

**Niveau 3 — Page détail**
Ajouter une route `/produit/<int:id>` qui appelle `https://dummyjson.com/products/{id}` et affiche la fiche complète d'un produit (description, images, remise si `discountPercentage > 0`).

---

## Ce que cet exercice t'a appris

| Compétence | Où tu l'as utilisée |
|---|---|
| Appel API avec `requests` | Route `/resultats` |
| Paramètres de query string | `?q=...&limit=12` |
| Gestion d'erreurs | `try/except`, `timeout` |
| Passer des données à un template | `render_template("resultats.html", produits=...)` |
| Lire une doc d'API | Explorer dummyjson avant de coder |