# 🧪 Exercices — Micro-service pour n8n (3h)

> Avant de commencer : `python app.py` doit tourner en local sans erreur.
> Tu peux tester tes endpoints avec `curl` ou directement depuis un script Python avec `requests`.

---

## Exercice 1 — Premier endpoint qui calcule (30 min)

Crée un nouveau fichier `exo_1.py` (port 6001).

Endpoint : **`POST /api/tva`**

- Reçoit un JSON `{"prix_ht": 1000, "taux": 0.20}`
- Renvoie `{"prix_ht": 1000, "tva": 200, "prix_ttc": 1200}`

Contraintes :
1. Vérifier que `prix_ht` est un nombre positif
2. `taux` est optionnel (par défaut 0.20)
3. Si erreur, renvoyer code 400 avec `{"error": "..."}`
4. Tester avec curl ou un script Python

> 💡 Si tu peux le tester dans n8n avec un nœud HTTP, encore mieux.

---

## Exercice 2 — Endpoint protégé par token (30 min)

Crée `exo_2.py` (port 6002).

1. Reprends ton endpoint TVA mais ajoute un décorateur `@require_token`
2. Lis le token depuis une variable d'environnement (utilise `python-dotenv` et un `.env`)
3. Vérifie :
   - Sans header `Authorization` → 401
   - Avec mauvais token → 401
   - Avec bon token → 200 et calcul OK
4. Bonus : log chaque tentative invalide avec `logging.warning(...)`

---

## Exercice 3 — Nettoyer une liste de leads (45 min)

Endpoint : **`POST /api/leads/clean`** (token requis)

Reçoit :

```json
{
  "leads": [
    {"nom": "Alice DUPONT", "email": " ALICE@MAIL.COM ", "tel": "06 11 22 33 44"},
    {"nom": "bob martin", "email": "bob@mail.com", "tel": "0611223345"},
    {"nom": "Alice Dupont", "email": "alice@mail.com", "tel": "0611223344"}
  ]
}
```

Doit renvoyer :

```json
{
  "leads": [
    {"nom": "Alice Dupont", "email": "alice@mail.com", "tel": "0611223344"},
    {"nom": "Bob Martin", "email": "bob@mail.com", "tel": "0611223345"}
  ],
  "nb_original": 3,
  "nb_apres_nettoyage": 2
}
```

Règles :
- Nom : trim + Title Case (`alice dupont` → `Alice Dupont`)
- Email : trim + lower
- Téléphone : supprimer espaces, tirets, points (`06 11 22 33 44` → `0611223344`)
- Dédoublonner sur l'email (un même email = un seul lead, on garde le premier vu)

> 💡 `"alice dupont".title()` → `"Alice Dupont"`. Pour les téléphones : `"".join(c for c in tel if c.isdigit())`.

---

## Exercice 4 — Conversion CSV → JSON (45 min)

Endpoint : **`POST /api/csv-to-json`** (token requis)

Reçoit un CSV envoyé sous forme de **chaîne de caractères** :

```json
{
  "csv": "nom,age,ville\nAlice,30,Paris\nBob,25,Lyon"
}
```

Doit renvoyer :

```json
{
  "lignes": [
    {"nom": "Alice", "age": "30", "ville": "Paris"},
    {"nom": "Bob", "age": "25", "ville": "Lyon"}
  ],
  "nb_lignes": 2
}
```

> 💡 Tu peux utiliser `io.StringIO` pour transformer la chaîne en quelque chose que `csv.DictReader` peut lire :
> ```python
> import csv
> from io import StringIO
> reader = csv.DictReader(StringIO(data["csv"]))
> lignes = list(reader)
> ```

Bonus : ajouter un paramètre optionnel `"separateur": ";"` pour gérer les CSV à la française.

**Pourquoi cet endpoint est utile en pratique :** n8n ne sait pas parser élégamment un CSV mal foutu. Tu lui exposes cette fonction et il peut s'en servir partout.

---

## Exercice 5 — Le projet fil rouge (40 min)

Endpoint : **`POST /api/produits/analyse`** (token requis)

Reçoit une liste de produits :

```json
{
  "produits": [
    {"nom": "iPhone", "prix": 999, "stock": 12, "categorie": "phone"},
    {"nom": "Galaxy", "prix": 899, "stock": 0, "categorie": "phone"},
    {"nom": "Pixel", "prix": 799, "stock": 5, "categorie": "phone"},
    {"nom": "MacBook", "prix": 1499, "stock": 3, "categorie": "laptop"},
    {"nom": "ThinkPad", "prix": 1299, "stock": 0, "categorie": "laptop"}
  ]
}
```

Doit renvoyer :

```json
{
  "nb_produits": 5,
  "nb_en_rupture": 2,
  "prix_moyen": 1099.0,
  "produits_par_categorie": {
    "phone": 3,
    "laptop": 2
  },
  "top_3_chers": [
    {"nom": "MacBook", "prix": 1499},
    {"nom": "ThinkPad", "prix": 1299},
    {"nom": "iPhone", "prix": 999}
  ],
  "alertes": [
    "Galaxy en rupture",
    "ThinkPad en rupture"
  ]
}
```

Contraintes :
- Tu **peux** (et c'est recommandé) utiliser `pandas` pour les calculs
- Renvoyer 400 si `produits` n'est pas une liste ou est vide

C'est exactement le genre d'endpoint qu'un workflow n8n peut appeler chaque matin sur le catalogue, pour ensuite envoyer les alertes en Slack.

---

## Bonus — Mettre ton service en ligne et le tester depuis n8n

Si tu as déjà un compte n8n (sinon utilise [https://webhook.site](https://webhook.site) pour simuler) :

1. Suis `deploiement_render.md` pour déployer ton `app.py` sur Render
2. Suis `integration_n8n.md` pour appeler ton endpoint depuis n8n
3. Branche le résultat sur un nœud Slack / Discord / Email
4. Démo : tu envoies un lead dans le workflow → ton API le score → n8n alerte si qualifié

C'est le pattern qui transforme Python en super-pouvoir d'un nocodeur.

---

## Récap

| Compétence | Exo |
|---|---|
| Recevoir et valider du JSON | 1, 5 |
| Codes HTTP corrects | 1 → 5 |
| Auth par token | 2 → 5 |
| `.env` et variables d'environnement | 2 |
| Logging | 2 |
| Manipuler des listes / dédoublonner | 3 |
| Parser un CSV reçu en string | 4 |
| Pandas dans un endpoint | 5 |
| Déploiement + appel depuis n8n | Bonus |
