# 🎓 Valider le titre CDA quand on est « IA & NoCode »

**Titre visé :** Concepteur Développeur d'Applications — RNCP37873 (niveau 6, Bac+3/4)
**Public :** alternants **Option IA & NoCode** — profils non-dev qui produisent avec des outils no-code (Bubble, FlutterFlow, n8n, Airtable, Supabase…) et de l'IA générative (Claude, Cursor, Lovable…).

> Ce document traduit chacune des **11 compétences** du référentiel en **exemple concret de la vraie vie**, en précisant : ce que le jury veut vérifier, la **preuve** à mettre dans le dossier de projet, le **vocabulaire** à tenir à l'oral, et le **piège** spécifique au no-code/IA.

---

## ⚠️ À lire avant tout : la règle d'or du jury

Le titre CDA reste un titre de **développeur**. Le jury ne note pas l'outil, il note **ta compréhension** et **ta démarche**. Deux conséquences :

1. **« L'IA / le no-code l'a fait pour moi » ne suffit pas.** Tu dois pouvoir **expliquer ce que l'outil produit sous le capot** : ce que Bubble génère (HTML/CSS/JS), ce qu'une automatisation n8n appelle, ce que fait le code que Claude a écrit. Tu es le **chef d'orchestre**, pas un simple utilisateur.
2. **Deux compétences exigent du vrai code visible** (voir 🟥 plus bas) : *Développer des composants métier* et *Développer des composants d'accès aux données*. Le pur no-code y est **risqué**. C'est exactement pourquoi la formation inclut Python/Flask/micro-services : ils **sécurisent** ces deux compétences.

**Modalités d'examen** (rappel) : dossier de projet + diaporama, présentation, **entretien technique** (le jury creuse ton dossier), questionnaire pro (dont **anglais B1**), entretien final. Tout se joue sur ta capacité à **raconter et justifier** tes choix.

---

## 🧵 Le fil rouge : « LeadScore »

Pour rendre tout concret, on suit **un seul projet** du début à la fin — réaliste pour un alternant IA & NoCode :

> **LeadScore** — une PME reçoit des prospects (formulaire web, salons, imports). Elle veut les **capter, enrichir et noter automatiquement** pour appeler les plus chauds en priorité.

**Stack type (100 % au programme de la formation) :**

| Couche | Outil | Cours du repo |
|---|---|---|
| Interface (présentation) | Front no-code (Lovable / Bubble) + dashboard | `cours_dataviz`, `cours_api` |
| Orchestration | **n8n** (webhooks, automatisations) | `cours_microservice`, `cours_cron` |
| Logique métier | **Micro-service Flask** (scoring + enrichissement IA) | `cours_microservice`, `cours_data`, `cours_scraping` |
| Intelligence | **LLM** via API (qualification, résumé) | `cours_llm`, `cours_agents_llm` |
| Données | **Supabase** (PostgreSQL) + stockage JSON/NoSQL | `cours_api`, `cours_data` |
| Mise en prod | **GitHub + Render** (CI/CD), logs, tests | `cours_microservice` |

---

# 🟦 BC01 — Développer une application sécurisée

## 1. Installer et configurer son environnement de travail

🎯 **Le jury veut vérifier :** que tu sais monter un poste de travail projet, gérer dépendances et secrets, versionner.

🌍 **Exemple LeadScore :** tu installes **Cursor/VS Code** + Python, tu crées un **environnement virtuel** (`.venv`), tu remplis `requirements.txt`, tu clones le repo **Git**, tu connectes tes comptes **Supabase / Render / n8n** et tu ranges toutes les clés API dans un **`.env`** (jamais dans le code).

📎 **Preuve dans le dossier :** capture de l'IDE configuré, `requirements.txt`, `.gitignore` (qui exclut `.env`), `.env.example`, un README « Installation » pas-à-pas.

🗣️ **À l'oral :** IDE, environnement virtuel, gestionnaire de paquets (`pip`), dépendances, variable d'environnement, dépôt Git, clé API.

⚠️ **Piège :** committer un secret. Montre ton `.gitignore` et ton `.env.example` — c'est un réflexe de pro très bien vu.

---

## 2. Développer des interfaces utilisateur

🎯 **Le jury veut vérifier :** que tu construis une UI utilisable, responsive et **accessible (RGAA)**, avec validation des saisies.

🌍 **Exemple LeadScore :** le **formulaire de capture** de prospect et le **dashboard** de suivi. Réalisés en no-code (Lovable/Bubble) ou en HTML/CSS généré par IA. Champs obligatoires, messages d'erreur, responsive mobile, contrastes et libellés conformes RGAA.

📎 **Preuve :** maquette → interface réelle (avant/après), captures desktop + mobile, lien en ligne, note sur les choix d'accessibilité.

🗣️ **À l'oral :** responsive, composant UI, validation côté client, ergonomie, **RGAA** / accessibilité, parcours utilisateur.

⚠️ **Piège :** savoir **expliquer ce que le no-code génère** (du HTML/CSS/JS) et **prouver l'accessibilité réelle** (navigation clavier, alternatives textuelles), pas juste « c'est joli ».

---

## 3. Développer des composants métier 🟥 *(code visible attendu)*

🎯 **Le jury veut vérifier :** que tu développes la **logique métier sécurisée** — et que tu la **comprends ligne à ligne**.

🌍 **Exemple LeadScore :** le **micro-service Flask** qui reçoit un lead, le **score** (budget, email pro…), appelle un **LLM** pour l'enrichir/résumer, **valide les données entrantes**, protège l'endpoint par **token Bearer** et renvoie les bons **codes HTTP**. → c'est exactement `cours_microservice/app.py`.

📎 **Preuve :** extraits de code commentés, règle de scoring, validation des entrées, gestion des erreurs, sécurisation (auth, secrets).

🗣️ **À l'oral :** composant métier, séparation des responsabilités, validation des entrées, authentification, codes HTTP (200/400/401/500), injection.

⚠️ **Piège n°1 du parcours :** si Claude/Cursor a écrit le code, tu dois pouvoir **réexpliquer chaque bloc** et répondre à « pourquoi cette ligne ? ». Entraîne-toi à dérouler `app.py` sans tes notes.

---

## 4. Contribuer à la gestion d'un projet informatique

🎯 **Le jury veut vérifier :** que tu travailles en **méthode (agile)**, avec versionnement et suivi.

🌍 **Exemple LeadScore :** un **board** (Trello/Notion/Jira) avec **user stories** et sprints, des **commits Git** réguliers, des **branches** par fonctionnalité, des points d'avancement avec le « client » (ton tuteur/formateur).

📎 **Preuve :** captures du backlog, historique Git (`git log`), exemples de user stories, planning de sprint.

🗣️ **À l'oral :** agile/Scrum, sprint, backlog, user story, estimation, versionnement, branche, *pull request*, *daily*.

⚠️ **Piège :** un historique Git « 1 seul commit final ». Commits **petits et réguliers** = preuve de démarche.

---

# 🟩 BC02 — Concevoir et développer une application en couches

## 5. Analyser les besoins et maquetter une application

🎯 **Le jury veut vérifier :** que tu transformes un **besoin client** en spécifications + **maquettes**.

🌍 **Exemple LeadScore :** entretien fictif avec la PME → tu rédiges le **besoin** (« qualifier 200 leads/mois sans embaucher »), des **user stories**, un **diagramme de cas d'utilisation**, puis des **maquettes Figma** (ou générées par IA via Lovable) avec l'**enchaînement des écrans**.

📎 **Preuve :** mini cahier des charges, user stories, diagramme de cas d'usage, maquettes + arborescence des écrans.

🗣️ **À l'oral :** besoin fonctionnel / non-fonctionnel, cas d'utilisation, *wireframe* / maquette, parcours utilisateur, RGAA.

⚠️ **Piège :** sauter l'analyse pour aller direct à l'outil. Le jury adore voir **besoin → maquette → solution** dans cet ordre.

---

## 6. Définir l'architecture logicielle d'une application

🎯 **Le jury veut vérifier :** que tu sais penser **multicouche** (présentation / métier / données) et **justifier** tes choix, sécurité ANSSI comprise.

🌍 **Exemple LeadScore :** un **schéma d'architecture** : `Front no-code → n8n → micro-service Flask → Supabase`, avec un **diagramme de séquence** « un lead arrive → est scoré → est stocké → s'affiche ». Tu justifies pourquoi la logique métier est **isolée** dans le micro-service.

📎 **Preuve :** schéma d'architecture en couches, diagramme de séquence, tableau des choix techniques justifiés.

🗣️ **À l'oral :** architecture **multicouche / 3-tiers**, séparation des responsabilités, API, couplage faible, recommandations **ANSSI**.

⚠️ **Piège :** ne pas confondre l'**outil** (n8n) et la **couche** (orchestration/métier). Sache nommer ce qui joue chaque rôle.

---

## 7. Concevoir et mettre en place une base de données relationnelle

🎯 **Le jury veut vérifier :** que tu **modélises** des données relationnelles propres (clés, relations, normalisation).

🌍 **Exemple LeadScore :** tables **`leads`**, **`utilisateurs`**, **`scores`** dans **Supabase (PostgreSQL)**. Tu fais un **MCD/MLD** (Merise ou entité-association), tu poses **clés primaires/étrangères** et une **relation 1-N** (un commercial → plusieurs leads).

📎 **Preuve :** MCD/MLD, schéma des tables, captures Supabase, script de création SQL.

🗣️ **À l'oral :** modèle relationnel, MCD/MLD, clé primaire/étrangère, relation 1-N / N-N, **normalisation**, intégrité référentielle.

⚠️ **Piège :** « j'ai juste créé des colonnes dans Airtable ». Montre une **vraie modélisation relationnelle** réfléchie, pas un tableur.

---

## 8. Développer des composants d'accès aux données SQL et NoSQL 🟥 *(code visible attendu)*

🎯 **Le jury veut vérifier :** que tu écris des **accès aux données sécurisés**, en **SQL** *et* **NoSQL**.

🌍 **Exemple LeadScore :** depuis le micro-service, des **requêtes SQL** (CRUD) sur Supabase avec **requêtes paramétrées** (anti-injection) ; et un usage **NoSQL** pour l'enrichissement (réponses LLM stockées en **JSON/JSONB**, ou cache, ou Airtable).

📎 **Preuve :** extraits de requêtes SQL (SELECT/INSERT/UPDATE/DELETE), code d'accès (client Supabase / ORM), exemple de stockage NoSQL.

🗣️ **À l'oral :** **CRUD**, requête paramétrée, **injection SQL**, ORM, **SQL vs NoSQL**, transaction.

⚠️ **Piège :** oublier le **NoSQL** (la compétence l'exige explicitement) ou concaténer des chaînes dans une requête (= faille d'injection à bannir).

---

# 🟨 BC03 — Préparer le déploiement d'une application sécurisée

## 9. Préparer et exécuter les plans de tests d'une application

🎯 **Le jury veut vérifier :** que tu **planifies** des tests et que tu les **exécutes** (manuels + automatisés).

🌍 **Exemple LeadScore :** un **plan de tests** (tableau : cas / données / résultat attendu / obtenu / statut), des **tests manuels** du formulaire, et des **tests automatisés `pytest`** sur le micro-service (token OK/KO, validation 400, `/health`).

📎 **Preuve :** tableau de plan de tests, fichier `test_app.py`, captures des résultats (vert/rouge), cas de non-régression.

🗣️ **À l'oral :** test **unitaire / d'intégration / fonctionnel**, jeu d'essai, cas de test, **non-régression**, couverture.

⚠️ **Piège :** se contenter de « j'ai cliqué, ça marche ». Un **tableau de cas** + quelques `pytest` font toute la différence.

---

## 10. Préparer et documenter le déploiement d'une application

🎯 **Le jury veut vérifier :** que quelqu'un d'autre pourrait **redéployer** ton appli grâce à ta **doc**.

🌍 **Exemple LeadScore :** une **procédure de déploiement** pas-à-pas (prérequis, variables d'env, build, lancement) — c'est exactement ce que fait déjà `cours_microservice/deploiement_render.md` : préparer le projet, pousser sur GitHub, configurer Render, tester en ligne.

📎 **Preuve :** doc de déploiement, README, **checklist avant prod**, schéma de l'environnement de production.

🗣️ **À l'oral :** environnements **dev / staging / prod**, build, dépendances, documentation technique, *rollback*.

⚠️ **Piège :** une doc « pour toi seul ». Écris-la pour **un inconnu** : c'est le critère de réussite.

---

## 11. Contribuer à la mise en production dans une démarche DevOps

🎯 **Le jury veut vérifier :** que tu participes à une **chaîne automatisée** qualité → livraison, en **collaboration** avec la prod.

🌍 **Exemple LeadScore :** `git push` → **CI** (GitHub Actions lance les `pytest`) → **CD** (Render redéploie automatiquement si le vert passe) → suivi des **logs/monitoring** sur le dashboard Render → coordination avec « l'équipe de prod ».

📎 **Preuve :** workflow `.github/workflows/tests.yml`, `render.yaml` (infra as code), captures du pipeline et des logs, schéma du flux CI/CD.

🗣️ **À l'oral :** **CI/CD**, pipeline, **intégration continue** vs **déploiement continu**, **IaC**, monitoring, *rollback*, DevOps.

⚠️ **Piège (point clé de ce module) :** Render seul = **CD uniquement**. Pour défendre « démarche **DevOps** », ajoute la brique **CI (tests automatisés dans un pipeline)** — sinon le maillon qualité manque.

---

# 🔒 Compétences transversales (présentes dans tout le dossier)

Ces exigences ne sont pas des compétences isolées mais le jury les attend **partout** :

- **Sécurité (ANSSI)** : secrets hors du code, authentification, validation des entrées, anti-injection, HTTPS.
- **RGPD** : mentions légales, consentement sur le formulaire LeadScore, données personnelles minimisées et protégées.
- **Accessibilité (RGAA)** : pris en compte dès les maquettes.
- **Anglais B1** : sache **lire une doc technique en anglais** et répondre court à l'écrit (épreuve du questionnaire pro).
- **Veille** : cite 2-3 sources que tu suis (sécurité, outils IA) — montre que tu restes à jour.

---

# 🗺️ Synthèse — compétence → preuve no-code/IA

| # | Compétence | Outil(s) LeadScore | Preuve maîtresse | Code visible ? |
|---|---|---|---|---|
| 1 | Environnement de travail | Cursor, Git, `.venv` | README install + `.gitignore` | — |
| 2 | Interfaces utilisateur | Lovable / Bubble | Maquette → UI + RGAA | partiel |
| 3 | Composants métier | Flask + LLM | `app.py` expliqué | 🟥 oui |
| 4 | Gestion de projet | Trello, Git | Backlog + historique Git | — |
| 5 | Analyse & maquettage | Figma / Lovable | Besoins + cas d'usage + maquettes | — |
| 6 | Architecture logicielle | Schéma multicouche | Diagrammes archi + séquence | — |
| 7 | Base de données | Supabase | MCD/MLD + tables | partiel |
| 8 | Accès aux données | Supabase + JSON | Requêtes SQL + NoSQL | 🟥 oui |
| 9 | Plans de tests | pytest + tableau | Plan de tests + `test_app.py` | partiel |
| 10 | Documenter le déploiement | Render | `deploiement_render.md` | — |
| 11 | Mise en prod DevOps | GitHub + Render | Pipeline CI/CD + logs | partiel |

🟥 = **du vrai code est attendu** : ne pas tout déléguer au no-code sur ces deux compétences.

---

# ✅ Check-list « dossier prêt pour le jury »

- [ ] Un projet fil rouge qui traverse **les 3 blocs** (LeadScore ou équivalent).
- [ ] Du **code que je sais expliquer** pour les compétences 3 et 8.
- [ ] Une **base relationnelle modélisée** (MCD) + un usage **NoSQL**.
- [ ] Un **plan de tests** + quelques tests **automatisés**.
- [ ] Une **doc de déploiement** réutilisable par un inconnu.
- [ ] Un **pipeline CI/CD** (pas seulement « git push → Render »).
- [ ] **Sécurité, RGPD, accessibilité** visibles dans le dossier.
- [ ] Je sais **lire une doc technique en anglais**.
- [ ] Mon **historique Git** raconte la progression (commits réguliers).
- [ ] Je peux **dérouler chaque écran/fichier sans mes notes**.