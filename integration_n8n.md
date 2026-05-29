# 🔗 Brancher ton micro-service Python dans n8n

> Ton API tourne (en local ou sur Render). Maintenant on l'appelle depuis n8n.

---

## 1. Créer un workflow simple

Dans n8n, crée un nouveau workflow avec 3 nœuds :

```
[Manual Trigger] → [HTTP Request] → [Set / Slack / Notion]
```

---

## 2. Configurer le nœud HTTP Request

Clique sur le nœud **HTTP Request** et remplis :

| Champ | Valeur |
|---|---|
| **Method** | POST |
| **URL** | `https://mon-service.onrender.com/api/lead/score` |
| **Authentication** | None *(on gère via Header)* |
| **Send Headers** | ✅ activé |
| **Send Body** | ✅ activé |
| **Body Content Type** | JSON |

### Headers à ajouter

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{ $credentials.token }}` ou directement `Bearer ton-token` |
| `Content-Type` | `application/json` |

### Body (JSON)

```json
{
  "nom": "{{ $json.nom }}",
  "email": "{{ $json.email }}",
  "budget": {{ $json.budget }}
}
```

> 💡 Les `{{ ... }}` sont la syntaxe d'expression n8n. Elles permettent d'injecter des données d'un nœud précédent.

---

## 3. Utiliser la réponse

Le nœud HTTP Request renvoie un objet comme :

```json
{
  "score": 80,
  "qualifie": true
}
```

Tu peux ensuite ajouter un nœud **IF** :

- Condition : `{{ $json.qualifie }} === true`
- **True** : envoyer en Slack / créer un deal HubSpot / ajouter à Notion
- **False** : ignorer ou ajouter à une liste "à recontacter plus tard"

---

## 4. Stocker le token proprement dans n8n

❌ **Mauvais** : mettre `Bearer mon-token-secret` en dur dans chaque workflow.

✅ **Bon** : créer une **Credential** HTTP Header Auth dans n8n :

1. Dans n8n, va dans **Credentials** → **New**
2. Choisis **Header Auth**
3. Name : `Mon API Python`
4. Header Name : `Authorization`
5. Header Value : `Bearer ton-token-secret`
6. Save

Puis dans ton nœud HTTP Request :

- **Authentication** : Generic Credential Type
- **Generic Auth Type** : Header Auth
- **Credential** : `Mon API Python`

Tu peux maintenant retirer le header manuel. Si tu changes le token, tu le modifies en un seul endroit.

---

## 5. Cas d'usage type "Pipeline lead"

```
[Form Trigger]
  → reçoit nom, email, budget depuis un Typeform/Tally

[HTTP Request] → POST /api/lead/score
  → reçoit { score: 80, qualifie: true }

[IF] → qualifie ?
  ├─ true  → [HubSpot: Create Deal]
  └─ false → [Notion: Add to "Nurture list"]
```

Tu as **délégué la logique métier complexe** à ton Python, et n8n s'occupe de l'orchestration. C'est le bon découpage.

---

## 6. Inverser le flux : Python qui appelle n8n

Parfois c'est l'inverse : ton script Python s'exécute (cron, scraping...) et veut **envoyer le résultat à n8n** pour qu'il fasse le reste.

Côté n8n : crée un workflow démarrant par un **Webhook** trigger. Note l'URL générée (ex: `https://n8n.tonsite.com/webhook/lead-recu`).

Côté Python :

```python
import requests

requests.post(
    "https://n8n.tonsite.com/webhook/lead-recu",
    json={"nom": "Alice", "score": 80},
    timeout=10,
)
```

Et hop, le workflow n8n se déclenche.

---

## 7. Debug : voir ce qui passe entre les deux

- **Logs Render** : tu vois ce que ton API reçoit
- **Executions n8n** : tu vois ce que ton workflow a fait, avec le détail de chaque nœud
- **webhook.site** : ultra utile pour tester un POST AVANT de coder le récepteur

Le combo fonctionne dans les deux sens. Maîtriser ça = devenir un nocodeur **augmenté**.
