# 📚 Cours — Web Scraping

> Le scraping, c'est aller lire une page web "comme un humain" mais via du code, pour en extraire des données.

---

## 1. Quand scraper ?

Tu veux des données qui sont sur un site web, et :

- ❌ Pas d'API publique
- ❌ Le copier-coller manuel prendrait des heures
- ✅ Les données sont publiques (pas derrière un login privé)
- ✅ Tu respectes les conditions du site

Si l'API existe, **utilise l'API**. Toujours plus rapide, stable et autorisé.

---

## 2. Comment ça marche (concept en 30 secondes)

Quand ton navigateur affiche une page :

1. Il envoie une **requête HTTP GET** à l'URL
2. Le serveur renvoie du **HTML** (du texte structuré)
3. Le navigateur le **transforme en visuel**

Scraper = court-circuiter l'étape 3. On télécharge le HTML avec `requests`, puis on parse avec `BeautifulSoup` pour en extraire ce qui nous intéresse.

```python
import requests
from bs4 import BeautifulSoup

html = requests.get("https://example.com").text
soup = BeautifulSoup(html, "html.parser")

print(soup.title.text)
```

---

## 3. Le HTML en 5 minutes

Une page HTML c'est un arbre de **balises** :

```html
<html>
  <body>
    <h1 class="titre">Mon site</h1>
    <ul id="produits">
      <li class="produit">
        <span class="nom">Livre A</span>
        <span class="prix">19.99 €</span>
      </li>
      <li class="produit">
        <span class="nom">Livre B</span>
        <span class="prix">29.99 €</span>
      </li>
    </ul>
  </body>
</html>
```

Chaque balise peut avoir :

- Un **id** (unique sur la page) : `<div id="header">`
- Une ou plusieurs **classes** : `<span class="prix promo">`
- Des **attributs** : `<a href="/produit/42">`

Pour scraper, tu vas dire à BeautifulSoup :
> "Trouve toutes les balises `<span>` avec la classe `prix`"

---

## 4. Inspecter une page (étape la plus importante)

**Avant de coder une seule ligne**, ouvre la page dans Chrome/Firefox :

1. Clic droit sur l'élément qui t'intéresse → **Inspecter**
2. Tu vois le HTML correspondant en surbrillance
3. Note la balise et ses attributs (classe, id)

C'est ça qui te dit quoi chercher dans le code.

---

## 5. BeautifulSoup — Les méthodes qu'on utilise 90% du temps

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")

# Trouver UN element (le premier match)
soup.find("h1")                          # premier <h1>
soup.find("div", class_="prix")          # premier <div class="prix">
soup.find("a", id="contact")             # un id specifique

# Trouver TOUS les elements
soup.find_all("li")                      # toutes les <li>
soup.find_all("span", class_="prix")     # toutes les <span class="prix">

# Recuperer le texte
element = soup.find("h1")
element.text                             # tout le texte
element.text.strip()                     # sans espaces autour

# Recuperer un attribut
lien = soup.find("a")
lien["href"]                             # valeur de href
lien.get("href")                         # idem mais ne plante pas si absent

# Selecteurs CSS (puissants !)
soup.select(".prix")                     # toutes les classes prix
soup.select("ul#produits > li")          # tous les li direct dans #produits
soup.select("a[href^='/produit']")       # tous les a dont href commence par /produit
```

> 💡 `class_="..."` avec un underscore car `class` est un mot-clé Python réservé.

---

## 6. Le pattern type d'un scraper

```python
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url, timeout=10)
response.raise_for_status()             # plante si code != 200

soup = BeautifulSoup(response.text, "html.parser")

livres = []
for article in soup.select("article.product_pod"):
    titre = article.h3.a["title"]
    prix = article.select_one(".price_color").text
    livres.append({"titre": titre, "prix": prix})

print(f"{len(livres)} livres trouves")
```

---

## 7. Pagination — Parcourir plusieurs pages

Deux patterns courants :

### A. URL avec numéro de page

```
https://books.toscrape.com/catalogue/page-1.html
https://books.toscrape.com/catalogue/page-2.html
...
```

→ Boucle `for page in range(1, 51):`

### B. Bouton "page suivante"

→ Récupère le `href` du lien "Next" et boucle tant qu'il existe.

```python
url = "https://example.com/page-1"
while url:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # ... extraire les donnees ...

    bouton = soup.find("a", class_="next")
    url = bouton["href"] if bouton else None
```

---

## 8. Anti-bot basique

Beaucoup de sites bloquent les requêtes "non navigateur". Trois parades :

### A. Un User-Agent réaliste

```python
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
requests.get(url, headers=headers)
```

### B. Sleep entre les requêtes

```python
import time
time.sleep(1)         # 1 seconde entre chaque requete
```

> Si le site est lent, c'est un signe que tu charges trop. Ralentis.

### C. Session (réutilise les cookies)

```python
session = requests.Session()
session.headers.update({"User-Agent": "..."})

session.get(url1)
session.get(url2)     # reutilise la connexion
```

---

## 9. Quand `requests` ne suffit plus

Certains sites **chargent leur contenu en JavaScript** après l'arrivée de la page. `requests` ne voit que le HTML initial, vide.

Comment reconnaître :

- Tu vois le contenu dans Chrome ✅
- Mais `response.text` est presque vide ❌
- Ou tu vois `{{variable}}` dans le HTML brut

**Solution :** un vrai navigateur piloté en code → **Playwright** ou Selenium.

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://exemple-js.com")
    page.wait_for_selector(".produit")
    html = page.content()
    browser.close()
```

> Playwright est plus lent et plus lourd. À n'utiliser **que** quand `requests` échoue.

---

## 10. Sauvegarder ce qu'on a scrapé

Le scraping ne sert à rien sans persistance. Trois choix selon le besoin :

```python
# CSV (le plus universel)
import pandas as pd
pd.DataFrame(livres).to_csv("livres.csv", index=False)

# JSON (si structure imbriquee)
import json
with open("livres.json", "w") as f:
    json.dump(livres, f, indent=2)

# Excel (si tu vas l'envoyer a un humain)
pd.DataFrame(livres).to_excel("livres.xlsx", index=False)
```

---

## 11. Le branchement avec n8n

C'est là que ça devient intéressant pour un nocodeur :

1. Tu écris ton scraper en Python (1 fichier)
2. Tu le déploies (Render, Railway, ou en local + cron)
3. Tu fais que ton script **POST** le résultat à un webhook n8n
4. n8n s'occupe du reste : envoyer en Slack, ajouter à Notion, alerter par mail...

```python
import requests
import pandas as pd

# ... scraping ...

requests.post(
    "https://n8n.tonsite.com/webhook/livres",
    json={"livres": livres, "date": "2025-05-14"},
)
```

Ton Python fait UNE chose (scraper), n8n fait tout le reste.
