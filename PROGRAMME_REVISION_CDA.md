# 🎯 Programme de révision inratable — Titre CDA (RNCP37873, option IA & NoCode)

> Objectif : arriver au jury en sachant **dérouler chaque fichier sans tes notes**, **justifier chaque choix**, et **répondre aux questions-pièges**. Le jury ne note pas l'outil, il note **ta compréhension**.
> Compagnon de [VALIDATION_COMPETENCES_CDA.md](VALIDATION_COMPETENCES_CDA.md) (le « quoi prouver ») — ce fichier est le « comment réviser ».

---

## 0. Les 3 règles qui font passer (à relire chaque matin de révision)

1. **« L'IA l'a fait » ne suffit pas.** Sur chaque ligne tu dois savoir dire *quoi*, *pourquoi cette ligne*, *que se passe-t-il si je l'enlève*.
2. **Deux compétences exigent du code visible** (🟥 n°3 *composants métier* et n°8 *accès aux données*). Zéro impasse possible.
3. **Ordre que le jury adore : besoin → maquette → architecture → code → tests → déploiement.** Raconte toujours dans cet ordre.

**Modalités examen :** dossier de projet + diaporama → présentation → **entretien technique** (le jury creuse ton dossier) → questionnaire pro (dont **anglais B1**) → entretien final.

---

## 1. Calendrier sur 4 semaines (adapte les dates à ton jury)

Méthode = **active recall** (se tester) + **spaced repetition** (revoir J+1, J+3, J+7) + **1 oral blanc / semaine**.

| Semaine | Focus | Bloc | Livrable de fin de semaine |
|---|---|---|---|
| **S-4** | Fondations + BC01 (sécurité, environnement, métier, projet) | BC01 | Je déroule `cours_microservice/app.py` à l'oral, sans notes |
| **S-3** | BC02 (analyse, archi, BDD, accès données) | BC02 | MCD/MLD propre + requêtes SQL paramétrées + 1 accès NoSQL expliqués |
| **S-2** | BC03 (tests, doc déploiement, CI/CD DevOps) | BC03 | `pytest` au vert + doc de déploiement + schéma pipeline CI/CD |
| **S-1** | Transversal (ANSSI, RGPD, RGAA, anglais B1, veille) + **2 orals blancs** + dossier figé | Tous | Diaporama final + check-list cochée |

**Rituel quotidien (≈ 2 h) :**
- 15 min — relire les 3 règles + le glossaire du jour ([GLOSSAIRE.md](GLOSSAIRE.md))
- 60 min — réviser 1 compétence à fond (cours du repo + faire tourner le code)
- 30 min — **me tester à voix haute** sur les questions-pièges ci-dessous
- 15 min — noter ce que je n'ai pas su → c'est ça que je revois J+1

---

## 2. Révision par compétence (cours repo + à maîtriser + question-piège jury)

> Format : **[cours]** ce qu'il faut savoir refaire → ⚠️ question que le jury va poser (entraîne la réponse à voix haute).

### 🟦 BC01 — Développer une application sécurisée

**C1 — Environnement de travail**
`cours_theorie`, racine du repo (`.env`, `.gitignore`, `.venv`, `requirements.txt`).
À refaire : créer un `.venv`, geler `requirements.txt`, écrire un `.gitignore` qui exclut `.env`, fournir un `.env.example`.
⚠️ *« Montre-moi que tes secrets ne sont pas dans Git. »* → ouvrir `.gitignore` + `.env.example`, expliquer variable d'environnement vs valeur en dur.

**C2 — Interfaces utilisateur**
`cours_dataviz`, `cours_api` (`templates/`, `static/`).
À refaire : expliquer que le no-code **génère du HTML/CSS/JS**, prouver l'accessibilité **RGAA** (navigation clavier, alternatives textuelles, contrastes), validation côté client.
⚠️ *« En quoi ton interface est-elle accessible, concrètement ? »* → ne pas répondre « c'est joli » : citer contraste, libellés, focus clavier, responsive.

**C3 — Composants métier 🟥 CODE VISIBLE**
`cours_microservice/app.py`, `2_auth_token.py`, `3_validation.py` + `cours_llm` (appel LLM) + `cours_agents_llm`.
À refaire **par cœur** : dérouler `app.py` ligne à ligne — réception du lead, **validation des entrées**, **scoring**, appel **LLM**, **auth token Bearer**, **codes HTTP** (200/400/401/500).
⚠️ *« Pourquoi cette ligne ? Que se passe-t-il si je l'enlève ? »* → réponse pour chaque bloc. *« Comment empêches-tu une injection ? »* → validation + pas de concaténation.

**C4 — Gestion de projet**
Historique Git du repo, board (Trello/Notion).
À refaire : montrer **commits petits et réguliers**, branches par fonctionnalité, user stories, sprints.
⚠️ *« Montre ton `git log`. »* → un seul commit final = rouge. Raconte la progression.

### 🟩 BC02 — Concevoir et développer une application en couches

**C5 — Analyse des besoins & maquettage**
Référentiel (besoin LeadScore) + maquettes Figma/Lovable.
À refaire : besoin fonctionnel/non-fonctionnel, **diagramme de cas d'utilisation**, user stories, enchaînement des écrans.
⚠️ *« Quel besoin client résous-tu ? »* → « qualifier 200 leads/mois sans embaucher ». Toujours **besoin → maquette → solution**.

**C6 — Architecture logicielle**
`cours_microservice` (isolement de la logique métier), `cours_api`, `cours_cron`.
À refaire : schéma **multicouche / 3-tiers** `Front → n8n → Flask → Supabase` + **diagramme de séquence** d'un lead. Justifier l'isolement du métier dans le micro-service.
⚠️ *« n8n, c'est quelle couche ? »* → orchestration, pas métier. Ne pas confondre **outil** et **couche**.

**C7 — Base de données relationnelle**
`cours_data`, `cours_api` (Supabase/PostgreSQL).
À refaire : **MCD/MLD** (Merise), clés primaires/étrangères, relation **1-N** (un commercial → plusieurs leads), **normalisation**, intégrité référentielle.
⚠️ *« C'est juste des colonnes Airtable ? »* → non : montrer une vraie modélisation relationnelle.

**C8 — Accès aux données SQL & NoSQL 🟥 CODE VISIBLE**
`cours_data`, `cours_api`, `cours_llm/3_sortie_structuree_json.py`, `cours_llm/5_mini_rag.py` (stockage JSON).
À refaire : **CRUD** SQL avec **requêtes paramétrées** (anti-injection) + un usage **NoSQL** (réponse LLM en JSON/JSONB, cache).
⚠️ *« Montre une requête SQL et explique comment tu évites l'injection. »* → requête paramétrée, jamais de concaténation de chaînes. **Ne pas oublier le NoSQL** (exigé).

### 🟨 BC03 — Préparer le déploiement d'une application sécurisée

**C9 — Plans de tests**
`cours_microservice` (+ écrire `test_app.py` avec `pytest`).
À refaire : **tableau de plan de tests** (cas / données / attendu / obtenu / statut) + `pytest` (token OK/KO, validation 400, `/health`), non-régression.
⚠️ *« Comment testes-tu ? »* → pas « j'ai cliqué » : tableau de cas + tests automatisés.

**C10 — Documenter le déploiement**
`cours_microservice/deploiement_render.md`.
À refaire : procédure pas-à-pas (prérequis, variables d'env, build, lancement) **réutilisable par un inconnu** + checklist avant prod.
⚠️ *« Un collègue pourrait-il redéployer avec ta doc seule ? »* → oui, c'est le critère. Environnements dev/staging/prod.

**C11 — Mise en production DevOps**
`cours_microservice/integration_n8n.md`, `deploiement_render.md`, `cours_cron` (automatisation) + GitHub Actions.
À refaire : `git push` → **CI** (`pytest` dans GitHub Actions) → **CD** (Render redéploie si vert) → logs/monitoring.
⚠️ *« Render seul, c'est du DevOps ? »* → non, Render seul = **CD uniquement**. Ajouter la brique **CI** (tests dans un pipeline) sinon le maillon qualité manque. **C'est LE piège du module.**

---

## 3. Transversal (le jury l'attend PARTOUT)

- **Sécurité ANSSI** : secrets hors du code, auth, validation des entrées, anti-injection, HTTPS. → relier à `cours_microservice/2_auth_token.py` et `3_validation.py`.
- **RGPD** : mentions légales, consentement sur le formulaire, données personnelles minimisées.
- **RGAA** : accessibilité pensée **dès les maquettes** (pas après).
- **Anglais B1** : savoir **lire une doc technique en anglais** + répondre court à l'écrit. → S-1, lire 1 doc/jour en anglais (Flask, PostgreSQL, GitHub Actions) et reformuler en 3 phrases.
- **Veille** : préparer **2-3 sources** que tu suis (sécurité + outils IA) à citer.

---

## 4. Préparation de l'oral (la moitié de la note)

**Déroulé de présentation à répéter (chrono) :**
1. Contexte client + besoin (C5) — 2 min
2. Maquettes + parcours (C2, C5) — 2 min
3. Architecture multicouche + séquence (C6) — 2 min
4. Démo : un lead arrive → scoré → stocké → affiché — 3 min
5. Code expliqué (C3 `app.py`, C8 requêtes) — 4 min
6. Tests + déploiement + CI/CD (C9, C10, C11) — 3 min
7. Sécurité / RGPD / RGAA transversal — 2 min

**Banque de questions-pièges (s'entraîner à voix haute) :**
- « Pourquoi cette ligne dans `app.py` ? »
- « Que renvoie ton API si le token est faux ? » → **401**.
- « Différence intégration continue vs déploiement continu ? »
- « SQL vs NoSQL, pourquoi les deux ? »
- « C'est quoi une relation 1-N dans ton modèle ? »
- « Comment éviter une injection SQL ? »
- « n8n joue quel rôle dans l'architecture ? »
- « Si je supprime ta validation des entrées, que se passe-t-il ? »

**Technique anti-blocage :** si tu ne sais pas → reformuler la question, expliquer ta démarche, dire ce que tu vérifierais. Ne jamais dire « c'est l'IA qui a fait ».

---

## 5. Check-list jour J (à cocher avant de partir)

- [ ] Projet fil rouge traverse **les 3 blocs** (LeadScore)
- [ ] Je déroule **`app.py` (C3)** et **les requêtes (C8)** sans notes
- [ ] **MCD/MLD** + un usage **NoSQL** prêts à montrer
- [ ] **Plan de tests** + `pytest` au vert
- [ ] **Doc de déploiement** réutilisable par un inconnu
- [ ] **Pipeline CI/CD** (pas juste « git push → Render »)
- [ ] **Sécurité, RGPD, RGAA** visibles dans le dossier
- [ ] Je peux **lire une doc technique en anglais**
- [ ] **`git log`** raconte la progression (commits réguliers)
- [ ] Diaporama répété en temps réel ≤ 20 min
- [ ] 2-3 **sources de veille** prêtes à citer

---

## 6. Fiches d'auto-test (cache la réponse, récite)

| Question | Réponse attendue |
|---|---|
| Codes HTTP de l'API ? | 200 OK / 400 entrée invalide / 401 token faux / 500 erreur serveur |
| Anti-injection SQL ? | Requête paramétrée, jamais de concaténation |
| Architecture LeadScore ? | Front no-code → n8n → Flask → Supabase (3-tiers) |
| Relation 1-N ? | Un commercial → plusieurs leads (clé étrangère côté `leads`) |
| CI vs CD ? | CI = tests auto à chaque push ; CD = déploiement auto si vert |
| Render seul = ? | CD uniquement — il manque la CI pour parler DevOps |
| Où sont les secrets ? | Dans `.env`, exclu par `.gitignore`, exemple via `.env.example` |
| 2 compétences à code visible ? | C3 composants métier + C8 accès aux données |

---

*Programme adossé au repo de formation : chaque compétence pointe vers un `cours_*` réel. Réviser = faire tourner le code, pas seulement le lire.*