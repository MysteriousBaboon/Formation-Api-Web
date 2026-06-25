# 🐉 Scoring de dangerosité de monstre (~1h) — *Flask, logique métier*

> 🎓 **Compétence CDA visée : C3 — Composants métier (code visible)**
> Le cœur du métier : **transformer des données en une décision** (un score, un niveau)
> avec une **logique pondérée** que tu sais justifier. C'est *exactement* le type de calcul
> que le jury fait expliquer (le projet fil rouge « LeadScore » est un scoring, lui aussi).

---

## Le contexte

Tu codes le *Monsterdex*, l'encyclopédie d'un jeu où chaque créature reçoit un **indice
de dangerosité** calculé à partir de ses stats. L'API reçoit les caractéristiques d'un
monstre et renvoie un **score sur 100** + un **niveau de menace** coloré (🟢/🟠/🔴).

La **page web est fournie** (fiche de monstre qui change de couleur selon le danger).
Tu écris le moteur de scoring.

---

## Ce que tu dois construire

Un serveur Flask `app.py` (à partir de `starter.py`) avec :

### `POST /danger`
Reçoit :
```json
{ "nom": "Gnarrok", "force": 8, "vitesse": 7, "taille": 7, "regime": "carnivore" }
```

Valide :
- `force`, `vitesse`, `taille` : entiers **entre 1 et 10** → sinon **400**
- `regime` : l'un de `"herbivore"`, `"carnivore"`, `"omnivore"` → sinon **400**
- `nom` : optionnel (chaîne, `"Inconnu"` par défaut)

Calcule le **score** (formule imposée) :
```
score = force × 4  +  vitesse × 3  +  taille × 2  +  bonus_régime
bonus_régime : carnivore +10 · omnivore +5 · herbivore +0
score plafonné à 100
```

Détermine le **niveau de menace** :
| Score | Niveau | Couleur | Emoji |
|-------|--------|---------|-------|
| < 35 | Inoffensif | vert | 🟢 |
| 35–65 | Prudence | orange | 🟠 |
| > 65 | DANGER | rouge | 🔴 |

Et renvoie (**200**) :
```json
{
  "nom": "Gnarrok",
  "score": 79,
  "niveau": "DANGER",
  "couleur": "rouge",
  "emoji": "🔴",
  "detail": { "force": 32, "vitesse": 21, "taille": 14, "regime": 10 }
}
```

### `GET /` → sert la page fournie (`render_template("index.html")`)

---

## 💡 Conseils

- Mets les régimes et leurs bonus dans un **dict** : `BONUS = {"herbivore": 0, "omnivore": 5, "carnivore": 10}`.
  Tu valides le régime **et** tu lis le bonus avec la même structure (`if regime not in BONUS: ...`).
- Valide **chaque** stat de la même façon → écris une petite fonction
  `stat_valide(v)` qui renvoie `True` si c'est un `int` entre 1 et 10.
- `min(score, 100)` pour le plafond.
- Renvoie le `detail` (points par stat) : ça rend le score **explicable** — précieux à l'oral du jury.

---

## Pour tester

```bash
python app.py     # http://localhost:5005
```

```bash
# carnivore costaud -> DANGER
curl -X POST http://localhost:5005/danger -H "Content-Type: application/json" \
     -d '{"nom":"Gnarrok","force":8,"vitesse":7,"taille":7,"regime":"carnivore"}'
# petit herbivore -> Inoffensif
curl -X POST http://localhost:5005/danger -H "Content-Type: application/json" \
     -d '{"nom":"Mouton","force":2,"vitesse":2,"taille":2,"regime":"herbivore"}'
# stat hors bornes -> 400
curl -X POST http://localhost:5005/danger -H "Content-Type: application/json" \
     -d '{"force":99,"vitesse":7,"taille":7,"regime":"carnivore"}'
```

---

## ✅ Critères de réussite

- [ ] Un gros carnivore tombe en **DANGER 🔴**, un petit herbivore en **Inoffensif 🟢**.
- [ ] Une stat à 0, 11 ou `"huit"` → **400** (et pas un score faux).
- [ ] Un régime inconnu (`"fantôme"`) → **400**.
- [ ] Le `detail` permet de **reconstituer** le score à la main.
- [ ] Tu sais expliquer pourquoi la `force` pèse plus que la `taille` (les coefficients).

---

## ⭐ Bonus

1. **Faiblesse** : ajoute un champ `element` (`"feu"`, `"eau"`, `"plante"`) et renvoie
   l'élément qui le bat (table des faiblesses dans un dict).
2. **Comparateur** : `POST /duel` reçoit deux monstres et renvoie qui gagne (plus haut score).
3. **Classement** : garde les monstres notés en mémoire et expose `GET /top` (les 5 plus dangereux).
