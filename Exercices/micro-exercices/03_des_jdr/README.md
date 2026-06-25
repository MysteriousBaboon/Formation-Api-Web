# 🎲 Lanceur de dés JDR (~1h) — *Flask, validation, codes HTTP*

> 🎓 **Compétence CDA visée : C3 — Développer des composants métier (code visible)**
> Recevoir une requête, **parser et valider** l'entrée, renvoyer le **bon code HTTP**.
> C'est exactement ce que le jury te fera dérouler ligne à ligne.

---

## Le contexte

Tu construis le moteur de dés d'une table de jeu de rôle en ligne. Les joueurs
tapent une notation classique de JDR — `2d6+3` veut dire *« lance 2 dés à 6 faces
et ajoute 3 »* — et ton service doit renvoyer le détail des lancers et le total.

La **page web est déjà fournie** (jolis dés animés 🎲). À toi d'écrire le **cerveau** :
l'endpoint Python qui reçoit la notation, la valide, lance les dés et renvoie le résultat.

---

## Ce que tu dois construire

Un petit serveur Flask `app.py` (à partir de `starter.py`) avec **deux routes** :

### 1. `GET /` — la page
Sert la page `templates/index.html` (déjà écrite, n'y touche pas). Une ligne suffit.

### 2. `POST /lancer` — le moteur de dés *(le cœur de l'exo)*

Reçoit un JSON :
```json
{ "notation": "2d6+3" }
```

Et renvoie (code **200**) :
```json
{
  "notation": "2d6+3",
  "des": 2,
  "faces": 6,
  "modificateur": 3,
  "lances": [4, 6],
  "total": 13,
  "detail": "4 + 6 + 3"
}
```

### Le format de notation à parser

`XdY+Z` où :
- `X` = nombre de dés (optionnel, **1 par défaut** → `d20` = `1d20`)
- `Y` = nombre de faces (obligatoire)
- `+Z` ou `-Z` = modificateur (optionnel)

Exemples valides : `1d6`, `d20`, `3d8+5`, `2d10-2`, `4D6` (insensible à la casse).

---

## Les règles de validation (⚠️ c'est ça que le jury regarde)

| Cas | Code HTTP | Message |
|-----|-----------|---------|
| `notation` absente ou pas une chaîne | **400** | `notation requise` |
| Format invalide (`abc`, `2x6`, `dd6`…) | **400** | `notation invalide` |
| Plus de **100 dés** ou plus de **1000 faces** | **400** | `valeurs trop grandes` |
| Dé à **moins de 2 faces** | **400** | `un dé a au moins 2 faces` |
| Tout va bien | **200** | le résultat |

> 💡 **Regex conseillée** pour parser la notation :
> ```python
> import re
> motif = re.compile(r"^(\d*)d(\d+)([+-]\d+)?$", re.IGNORECASE)
> m = motif.match(notation.strip())
> ```
> `m.group(1)` = les dés (chaîne vide si `d20`), `m.group(2)` = les faces,
> `m.group(3)` = le modificateur (`None` s'il n'y en a pas).

> 💡 Pour lancer un dé : `import random` puis `random.randint(1, faces)`.

---

## Pour tester

Lance le serveur :
```bash
python app.py
```

Puis ouvre **http://localhost:5003** dans ton navigateur et lance des dés 🎲.

Teste aussi l'API « à la main » (c'est ce que fait le jury) :
```bash
# cas normal → 200
curl -X POST http://localhost:5003/lancer -H "Content-Type: application/json" -d '{"notation": "2d6+3"}'

# notation pourrie → 400
curl -X POST http://localhost:5003/lancer -H "Content-Type: application/json" -d '{"notation": "patate"}'

# notation manquante → 400
curl -X POST http://localhost:5003/lancer -H "Content-Type: application/json" -d '{}'
```

---

## ✅ Critères de réussite

- [ ] La page s'ouvre et les dés s'affichent quand on lance.
- [ ] `2d6+3` renvoie bien 2 lancers + le modificateur dans le total.
- [ ] `d20` est accepté (1 dé par défaut).
- [ ] Une notation invalide renvoie un **400** (et **pas** un 500 / une page d'erreur).
- [ ] Aucune valeur n'est concaténée « à la main » : tu **parses** proprement avec la regex.
- [ ] Tu sais expliquer **à voix haute** ce que fait chaque ligne de ton endpoint.

---

## ⭐ Bonus (si tu as fini avant l'heure)

1. **Lancer avantage/désavantage** : accepte `{"notation": "2d20", "garder": "max"}`
   qui ne garde que le meilleur (ou le pire) dé — la mécanique de D&D 5e.
2. **Plusieurs jets d'un coup** : accepte `"2d6+3, 1d20, 4d4"` et renvoie une liste de résultats.
3. **Historique** : garde en mémoire les 10 derniers jets et expose-les sur `GET /historique`.
