# 🦸 Bureau de recrutement de héros (~1h) — *Flask, auth par token, validation*

> 🎓 **Compétence CDA visée : C3 — Composants métier sécurisés (code visible)**
> Protéger un endpoint par **Bearer token** (→ **401**), valider les données reçues
> (→ **400**), et renvoyer un résultat propre (→ **200**). Le trio que le jury adore creuser.

---

## Le contexte

La *Ligue des Héros* recrute. Tu codes l'API du **bureau des recrues** : on lui envoie
un candidat (nom, super-pouvoir, niveau de puissance) et elle renvoie un **badge officiel**
avec son **rang** et son **matricule**. Mais attention : seuls les agents autorisés
(munis du bon **token**) peuvent enregistrer une recrue.

La **page web est fournie** (formulaire + carte de badge animée). Tu écris l'API derrière.

---

## Ce que tu dois construire

Un serveur Flask `app.py` (à partir de `starter.py`) avec :

### 1. Un décorateur `@require_token`
- Lit le token attendu depuis une **variable d'environnement** (`.env` + `python-dotenv`).
- Header attendu : `Authorization: Bearer <token>`.
- Pas de header ou mauvais token → **401** `{"error": "..."}`.

### 2. `POST /recrue` *(protégé par le token)*
Reçoit :
```json
{ "nom": "Comète", "pouvoir": "Vitesse", "niveau": 88 }
```
Valide :
- `nom` : chaîne non vide → sinon **400**
- `pouvoir` : chaîne non vide → sinon **400**
- `niveau` : entier **entre 1 et 100** → sinon **400**

Et renvoie le badge (**200**) :
```json
{
  "matricule": "COM-088",
  "nom": "Comète",
  "pouvoir": "Vitesse",
  "niveau": 88,
  "rang": "Élite",
  "emoji": "⭐"
}
```

**Calcul du rang** selon le niveau :
| Niveau | Rang | Emoji |
|--------|------|-------|
| 1–30 | Recrue | 🐣 |
| 31–60 | Confirmé | 🦸 |
| 61–90 | Élite | ⭐ |
| 91–100 | Légende | 👑 |

**Matricule** : 3 premières lettres du nom (majuscules) + niveau sur 3 chiffres.
Ex : `Comète` niveau 88 → `COM-088`.

### 3. `GET /health` → `{"status": "ok"}` (utile pour les tests de l'exo 09)
### 4. `GET /` → sert la page fournie (`render_template("index.html")`)

---

## 💡 Conseils

- Reprends le motif du décorateur vu en cours (`functools.wraps`, `request.headers.get("Authorization", "")`,
  `header.startswith("Bearer ")`, `header.removeprefix("Bearer ").strip()`).
- `isinstance(niveau, int)` **avant** de comparer (sinon `"88"` en string passerait).
  ⚠️ Astuce piège : `True` est un `int` en Python — pas grave ici, mais bon à savoir.
- Matricule : `nom.strip()[:3].upper()` et `f"{niveau:03d}"`.

---

## Pour tester

```bash
cp .env.example .env      # contient le token de démo
python app.py
```
Ouvre **http://localhost:5004**, remplis le formulaire (le token est pré-rempli),
puis joue avec un mauvais token pour voir le **401**.

En ligne de commande :
```bash
TOKEN="ligue-des-heros-2026"
# bon token -> 200
curl -X POST http://localhost:5004/recrue -H "Authorization: Bearer $TOKEN" \
     -H "Content-Type: application/json" -d '{"nom":"Comète","pouvoir":"Vitesse","niveau":88}'
# sans token -> 401
curl -X POST http://localhost:5004/recrue -H "Content-Type: application/json" \
     -d '{"nom":"Comète","pouvoir":"Vitesse","niveau":88}'
# niveau invalide -> 400
curl -X POST http://localhost:5004/recrue -H "Authorization: Bearer $TOKEN" \
     -H "Content-Type: application/json" -d '{"nom":"X","pouvoir":"Vol","niveau":999}'
```

---

## ✅ Critères de réussite

- [ ] Sans header `Authorization` → **401** (et pas un 500).
- [ ] Mauvais token → **401**. Bon token → **200**.
- [ ] `niveau` à 0, 101, `"abc"` ou manquant → **400**.
- [ ] Le rang et le matricule sont corrects.
- [ ] Le badge s'affiche dans la page web.
- [ ] Tu sais expliquer **pourquoi** le token est lu depuis `.env` et **jamais** écrit en dur dans le code.

---

## ⭐ Bonus

1. **Logging** : journalise chaque tentative avec un mauvais token (`logging.warning`).
2. **Anti-doublon** : refuse (409) un nom déjà recruté (garde un `set` en mémoire).
3. **Liste** : ajoute `GET /recrues` (protégé) qui renvoie tous les héros enregistrés.
