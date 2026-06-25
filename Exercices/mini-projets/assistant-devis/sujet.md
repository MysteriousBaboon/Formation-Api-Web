# 🧪 Mini-projet — Assistant devis (~1 jour) · Niveau 🔴 costaud

> **Type d'IA : 🤖 LLM + agent (function calling / ReAct)** — l'IA orchestre des outils ; les chiffres viennent de ton code, pas du modèle.
>
> **Prérequis :**
> - Copie `.env.example` → `.env` (la clé LLM de la formation est dans `cours_llm/.env`).
> - `pip install flask python-dotenv openai matplotlib requests`
> - Tu as fait `cours_agents_llm` (function calling / boucle ReAct) : ce projet en est l'aboutissement.
> - Une base de prix de départ est fournie dans `data/tarifs.csv`.
>
> 🎒 C'est une **mini-presta freelance** : tu livres un truc qui tourne ET que tu sais expliquer au jury, ligne par ligne.

---

## 🧑‍💼 Le client / le contexte

Tu viens d'être contacté·e par **Marco, artisan peintre**. Il perd ses soirées à faire des devis : mesurer, convertir en litres de peinture et en heures, retrouver ses prix, taper le tout proprement. Il veut un **assistant** où il **décrit le chantier en langage normal** (« repeindre un salon de 25 m², deux couches, plus les boiseries ») et qui lui sort un **devis chiffré**. Il te paie une journée.

## 🎯 Le besoin

> « Je décris le chantier avec mes mots, et l'outil me calcule un devis propre que je peux envoyer au client. »

## 📦 Ce que tu livres

- Un **agent** (boucle d'outils, comme dans `cours_agents_llm`) qui transforme une description en devis.
- Des **outils métier** : calcul des quantités, recherche des prix en base, estimation du délai.
- Un endpoint **Flask sécurisé** `POST /api/devis`.
- Un **devis structuré** affiché + un **PDF** téléchargeable.
- Un **README** d'installation + un `.env.example`.

---

## 🧱 Contraintes métier réelles

> Ce ne sont pas des caprices : c'est ce qui sépare un script de hackathon d'une presta livrable.

1. **Budget / temps** : ça tient en une journée ; un **garde-fou `max_etapes=5`** sur la boucle de l'agent (sinon il tourne et coûte cher).
2. **Sécurité** : aucune clé dans le code → tout dans `.env` ; `/api/devis` est **protégé par token Bearer** ; la description reçue est **validée** (non vide, longueur max) → **400** sinon.
3. **Les chiffres sont fiables** : les prix et les quantités sont calculés par **tes outils** (code + base), **pas inventés par l'IA**. L'IA orchestre et rédige, elle ne chiffre pas de tête.
4. **Anti-injection** : la recherche de prix en base se fait en **requête paramétrée**.
5. **Robustesse** : si l'agent n'aboutit pas en 5 étapes, on renvoie une réponse claire (« je n'ai pas pu chiffrer, précise le chantier ») au lieu de planter.

---

## 🪜 Étapes guidées

> Commit après chaque étape (le jury veut un historique Git qui raconte ta progression).

### 1. La base de prix (~45 min)
Crée `app.py` (port **6017**), charge `.env`, et importe `data/tarifs.csv` dans une **base SQLite** `tarifs.db` (table `tarifs`).
> 💡 `import csv, sqlite3` ; crée la table puis insère chaque ligne en **paramétré** (`INSERT ... VALUES (?, ?, ?)`).

### 2. Les outils métier 🟥 (~1h30) — *le cœur, à savoir réexpliquer*
Crée `outils.py` avec des fonctions pures et testables :
- `surface_vers_peinture(m2, couches, rendement)` → litres + arrondi au pot ;
- `prix_poste(nom_poste)` → va chercher le prix en base (**requête paramétrée**) ;
- `estimer_heures(m2, postes)` → temps de main d'œuvre ;
- `delai_meteo(exterieur: bool)` → si chantier extérieur, interroge Open-Meteo pour signaler des jours de pluie (réutilise l'idée de `terrasse-o-metre`).
> 💡 Recherche de prix, **jamais** en f-string :
> ```python
> cur.execute("SELECT prix_unitaire_eur, unite FROM tarifs WHERE poste = ?", (nom_poste,))
> ```

### 3. La boucle de l'agent (~1h30)
Crée `agent.py` : une boucle **function calling / ReAct** (reprends le pattern de `cours_agents_llm`) qui expose tes outils au LLM. Le modèle lit la description, **appelle les bons outils**, récupère les résultats, et propose un devis.
> 💡 Le squelette de boucle, avec garde-fou :
> ```python
> for etape in range(5):                 # max_etapes = 5
>     reponse = client.chat.completions.create(model=..., messages=messages, tools=OUTILS)
>     msg = reponse.choices[0].message
>     if not msg.tool_calls:             # le modèle a fini → il rend le devis
>         break
>     for appel in msg.tool_calls:
>         resultat = EXECUTEURS[appel.function.name](**json.loads(appel.function.arguments))
>         messages.append({"role": "tool", "tool_call_id": appel.id, "content": json.dumps(resultat)})
> ```
> ⚠️ Sans le `range(5)`, un agent qui boucle peut enchaîner les appels (et les coûts). Le garde-fou, c'est la contrainte n°1.

### 4. Assembler le devis structuré (~1h)
À partir des résultats des outils, construis un **devis structuré** (lignes : poste, quantité, prix unitaire, total ; total HT, TVA, TTC). Affiche-le dans une page lisible.

### 5. Le PDF téléchargeable (~45 min)
Génère le devis en **PDF** (matplotlib `savefig(format="pdf")` suffit : un tableau propre avec en-tête).
> 💡 `send_file(buf, mimetype="application/pdf", as_attachment=True, download_name="devis.pdf")`.

### 6. Sécuriser l'endpoint (~45 min)
Expose `POST /api/devis` (Bearer) qui prend `{"description": "..."}`, valide l'entrée → **400** sinon, lance l'agent, renvoie le devis.
> 💡 Décorateur `@require_token` repris de `cours_microservice`.

### 7. Finitions : README, `.env.example`, commits (~30 min)
README avec user stories + install + explication de l'architecture (agent + outils + base). `.env.example` : `LLM_BASE_URL`, `LLM_API_KEY`, `LLM_MODEL`, `API_TOKEN`. `.gitignore` excluant `.env`, `*.db`.

---

## ✅ Critères de réussite (grille façon jury CDA)

- [ ] Je sais **expliquer la boucle de l'agent** et **pourquoi le `max_etapes`** existe.
- [ ] Les chiffres viennent de **mes outils** (base + calcul), **pas** de l'IA.
- [ ] La recherche de prix est une **requête paramétrée** (anti-injection).
- [ ] `/api/devis` est **protégé par token Bearer** ; description invalide → **400**.
- [ ] Si l'agent n'aboutit pas, l'appli **répond proprement** sans planter.
- [ ] **Aucun secret dans le code** + **README** réutilisable + **historique Git** régulier.
- [ ] Je peux montrer le **PDF** généré.

---

## 🚀 Bonus (si tu finis en avance)

- Écris `test_outils.py` (`pytest`) : `surface_vers_peinture(25, 2, 12)` donne le bon nombre de litres — compétence C9.
- Ajoute un outil **`enregistrer_devis`** qui sauve le devis en base (historique des devis).
- Gère **plusieurs corps de métier** (une base de prix par métier).
- Déploie sur **Render** + appel depuis **n8n** (Marco reçoit le devis par email) — compétence C11.

---

## 🗺️ Compétences CDA mobilisées

| Compétence | Mobilisée ? | Où, concrètement, dans CE projet |
|---|:--:|---|
| C1 — Environnement (.venv/.env/Git) | ✓ | `.env.example`, `.gitignore`, commits par étape |
| C2 — Interfaces (responsive/RGAA) | ~ | Page de saisie + devis affiché lisiblement |
| C3 — Composants métier 🟥 | ✓ | `outils.py` (calculs + prix) + endpoint validé + Bearer + codes HTTP |
| C4 — Gestion de projet | ✓ | User stories + historique Git |
| C5 — Analyse & maquettage | ~ | Besoin de Marco → maquette du devis avant de coder |
| C6 — Architecture multicouche | ✓ | Agent (orchestration) → outils (métier) → base SQLite (données) ; endpoint en façade |
| C7 — Base relationnelle (MCD/MLD) | ~ | Table `tarifs` (en bonus : historique des devis) |
| C8 — Accès SQL + NoSQL 🟥 | ✓ | **SQL** : lecture des prix en requête **paramétrée** (NoSQL/JSON possible en bonus) |
| C9 — Plans de tests | ~ | En bonus : `test_outils.py` (les outils sont purs → testables) |
| C10 — Doc de déploiement | — | En bonus (Render) |
| C11 — Mise en prod DevOps | ~ | En bonus : Render + appel n8n |
| 🔒 Transversal (ANSSI/RGPD/RGAA/B1) | ✓ | Secrets en `.env`, validation, anti-injection, garde-fou de coût, doc OpenAI tool-calling lue en anglais |
