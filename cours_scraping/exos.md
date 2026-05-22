# 🧪 Exercices — Web Scraping (3h)

> Tous les sites cibles de ces exos sont **conçus pour le scraping** : aucun souci éthique.
> Pour chaque exo, mets toujours un `timeout=10` et un `time.sleep(0.3)` minimum entre les requêtes.

---

## Exercice 1 — Échauffement HTML (20 min)

Pas de réseau pour celui-ci. Crée `exo_1.py` :

1. Copie ce HTML dans une variable Python :

```html
<div class="catalogue">
  <div class="article" data-id="42">
    <h2>Casque audio</h2>
    <span class="prix">129.99</span>
    <span class="stock">7 en stock</span>
  </div>
  <div class="article" data-id="43">
    <h2>Clavier mécanique</h2>
    <span class="prix">89.00</span>
    <span class="stock">0 en stock</span>
  </div>
  <div class="article" data-id="44">
    <h2>Souris gamer</h2>
    <span class="prix">45.50</span>
    <span class="stock">12 en stock</span>
  </div>
</div>
```

2. Avec BeautifulSoup, affiche :
   - Tous les noms d'articles
   - Le prix moyen
   - Les articles **en rupture de stock** (stock = 0)
   - L'`id` du data-attribute pour chaque article (`article["data-id"]`)

---

## Exercice 2 — Citations de quotes.toscrape.com (30 min)

Site cible : `https://quotes.toscrape.com/`

1. Récupère la page d'accueil
2. Pour chaque citation, extrais :
   - Le texte
   - L'auteur
   - La liste des tags
3. Sauvegarde dans `citations.json` (avec `json.dump`, `indent=2`, `ensure_ascii=False`)
4. **Bonus** : trouve l'auteur qui apparaît le plus de fois sur la première page

> 💡 Inspecte la page : chaque citation est dans `<div class="quote">`. Les tags sont dans `<a class="tag">`.

---

## Exercice 3 — Top Hacker News (45 min)

Site cible : `https://news.ycombinator.com/`

1. Avec un User-Agent réaliste, récupère la page d'accueil
2. Pour les **30 premiers posts**, extrais :
   - Rang (1, 2, 3...)
   - Titre
   - Lien externe (href)
   - Nombre de points (la ligne d'après dans le HTML, classe `.score`)
   - Auteur (`.hnuser`)
3. Sauvegarde dans `hn_top30.csv` avec pandas
4. Affiche dans la console le post avec le plus de points

> ⚠️ Le HTML de HN est vieux et un peu bizarre : les infos d'un post sont sur **2 lignes `<tr>` consécutives**. Inspecte bien la structure.

---

## Exercice 4 — Catalogue complet books.toscrape (45 min)

Site cible : `https://books.toscrape.com/`

1. Récupère **les 10 premières pages** du catalogue
2. Pour chaque livre : titre, prix (en float), note (en mot : "One", "Two", etc.), dispo
3. Sauvegarde dans `livres_complet.csv`
4. Avec pandas, sors un mini rapport :
   - Nombre total de livres scrapés
   - Prix moyen
   - Combien de livres pour chaque niveau de note
   - Top 5 des livres les plus chers (titre + prix)

> 💡 Pattern d'URL : `https://books.toscrape.com/catalogue/page-{n}.html`

---

## Exercice 5 — Détail produit (40 min)

Toujours `books.toscrape.com`.

1. Reprends le CSV de l'exo 4
2. Pour les **5 livres les plus chers**, récupère le **lien vers leur fiche détail** (attribut `href` du `<a>` dans le `<h3>`)
3. Pour chaque fiche détail :
   - Charge la page
   - Récupère la **description** (paragraphe sous `#product_description`)
   - Récupère le **nombre d'exemplaires en stock** (extrait du texte "In stock (22 available)")
4. Sauvegarde tout dans `fiches_detail.json`

> ⚠️ Les `href` du catalogue sont relatifs. Utilise `urllib.parse.urljoin(url_page, href)` pour reconstruire l'URL absolue.

---

## Bonus — Brancher sur n8n (si tu finis tout)

Imagine que ton manager veut **être alerté chaque matin** quand un livre passe sous les 10£.

1. Adapte ton scraper pour ne garder que les livres avec `prix < 10`
2. Au lieu de sauvegarder en CSV, envoie le résultat à un webhook (utilise `https://webhook.site` pour tester) :

```python
import requests

requests.post(
    "https://webhook.site/TON-URL-UNIQUE",
    json={
        "date": "2025-05-14",
        "nb_livres_pas_chers": len(livres_filtres),
        "livres": livres_filtres,
    },
    timeout=10,
)
```

3. Va voir sur `webhook.site` que ton POST est bien arrivé.

C'est exactement le format qu'attendrait un **nœud Webhook n8n**. La suite (envoyer en Slack/Notion/email) se fait dans n8n, plus dans Python.

---

## Récap des compétences acquises

| Compétence | Exo où tu l'as vue |
|---|---|
| Parser du HTML | 1 |
| Boucler sur des éléments | 1, 2, 4 |
| Extraire des attributs (`href`, `data-id`) | 1, 5 |
| Sauvegarder en JSON / CSV | 2, 3, 4 |
| Pagination | 4 |
| URLs relatives → absolues | 5 |
| User-Agent | 3 |
| Branchement webhook (n8n) | Bonus |
