# 🧰 Mini-projets — des mini-prestas freelance pour valider le CDA

> Chaque mini-projet = **une commande client** que tu livres en **moins d'une journée**.
> Objectif double : (1) un truc qui **tourne et qu'on voit à l'écran**, (2) du code que tu sais
> **réexpliquer au jury**. Ici on ne fait pas « joli » : on fait **livrable + défendable**.

Tu prépares le titre **CDA (Concepteur Développeur d'Applications, option IA & NoCode)**. Le jury ne note pas l'outil, il note **ta compréhension**. Ces projets sont pensés pour que tu puisses dire, sur chaque ligne : *quoi, pourquoi, et ce qui se passe si je l'enlève*. Voir [`VALIDATION_COMPETENCES_CDA.md`](../../VALIDATION_COMPETENCES_CDA.md) et [`PROGRAMME_REVISION_CDA.md`](../../PROGRAMME_REVISION_CDA.md) à la racine du repo.

> 🧠 **Les types d'IA sont variés exprès** : 🤖 LLM, 📊 Machine Learning classique (scikit-learn), 🧮 sans IA du tout. Un bon développeur sait **choisir** son outil — et parfois, le meilleur choix est de *ne pas* mettre d'IA. C'est un argument apprécié au jury.

---

## 🚦 Dans quel ordre les faire

Difficulté croissante (commence par le haut) :

1. 🟢 🤖 [quiz-coach](quiz-coach/) — quiz qui profile et conseille
2. 🟢 🤖 [affiche-moi-ca](affiche-moi-ca/) — générateur d'affiches d'événement
3. 🟠 🧮 [terrasse-o-metre](terrasse-o-metre/) — météo → décision business
4. 🟠 📊 [thermometre-avis](thermometre-avis/) — avis clients classés par un modèle ML
5. 🟠 🧮 [revue-presse](revue-presse/) — veille automatisée du lundi
6. 🟠 🧮 [carte-bons-coins](carte-bons-coins/) — carte interactive de lieux
7. 🔴 🧮 [factures-en-clair](factures-en-clair/) — PDF → base SQLite + JSON
8. 🔴 🤖 [assistant-devis](assistant-devis/) — agent qui rédige un devis

---

## 📋 Le catalogue

| Projet | Type d'IA | Pitch client | Briques mélangées | Compétences CDA | Durée / Niv | Ce que tu vois à l'écran |
|---|---|---|---|---|---|---|
| [quiz-coach](quiz-coach/) | 🤖 LLM | « Un quiz qui profile mes prospects » | Flask · scoring métier · LLM · dataviz · RGPD | C2 **C3🟥** C5 +transv. | ~6h 🟢 | quiz → radar de profil + reco perso |
| [affiche-moi-ca](affiche-moi-ca/) | 🤖 LLM | « Des affiches pour mes événements d'asso » | Flask form · LLM · matplotlib | C1 C2 C3~ C5 +transv. | ~6h 🟢 | l'affiche PNG générée, à télécharger |
| [terrasse-o-metre](terrasse-o-metre/) | 🧮 Sans IA | « Dois-je sortir ma terrasse demain ? » | météo API · pandas · dataviz · Flask · cron | C1 **C3🟥** C6 C9~ +transv. | ~6h 🟠 | courbe météo + badge GO/NO-GO + message du jour |
| [thermometre-avis](thermometre-avis/) | 📊 ML (sklearn) | « Mes avis clients classés tout seuls » | data · scikit-learn · dataviz · Flask · stockage JSON | C3~ **C8 (NoSQL)** C6 C9~ +transv. | ~6h 🟠 | jauge satisfaction + barres thèmes + verbatims |
| [revue-presse](revue-presse/) | 🧮 Sans IA | « Un digest d'actu chaque lundi » | scraping (sandbox) · pandas · cron · templates HTML | C3~ C11~ +transv. | ~6h 🟠 | page digest en cartes + envoi auto |
| [carte-bons-coins](carte-bons-coins/) | 🧮 Sans IA | « Une carte de mes lieux partenaires » | data · géocodage · Plotly map · Flask | C2 C6 C7~ C8~ +transv. | ~6h 🟠 | carte interactive avec filtres + fiches |
| [factures-en-clair](factures-en-clair/) | 🧮 Sans IA | « Range mes PDF de factures en base » | pypdf/regex · **SQLite** · **JSON** · dataviz | **C3🟥 C7 C8🟥** C9 +transv. | ~1j 🔴 | upload PDF → tableau CA + alerte TVA |
| [assistant-devis](assistant-devis/) | 🤖 LLM + agent | « Décris un chantier, j'écris le devis » | agent ReAct · LLM · SQLite · microservice · PDF | **C3🟥** C6 C8 +transv. | ~1j 🔴 | langage naturel → devis structuré + PDF |

> 🟥 = compétence **« code visible »** exigée par le titre. **C3** (composants métier) est couverte par quiz-coach, terrasse, factures et assistant-devis ; **C8** (accès SQL **et** NoSQL) est couverte à fond par **factures-en-clair**, en NoSQL par thermometre-avis, en SQL par assistant-devis.
>
> ⚖️ **Répartition des types d'IA** : 3 projets 🤖 LLM · 1 projet 📊 ML classique · 4 projets 🧮 sans IA. (`thermometre-avis` propose en bonus un petit réseau de neurones `MLPClassifier` — pour goûter aussi au 🧠 deep learning.)

---

## ⚙️ Mode d'emploi commun (à lire UNE fois)

### 1. Configuration du LLM — **seulement pour les projets 🤖**
Les projets 🤖 (quiz-coach, affiche-moi-ca, assistant-devis) parlent au LLM via l'**interface compatible OpenAI** pointée par défaut sur **Anthropic** (même principe que `cours_llm`). Mets ça dans leur `.env` :
```
LLM_BASE_URL=https://api.anthropic.com/v1/
LLM_API_KEY=sk-ant-...        # la clé de la formation est dans cours_llm/.env
LLM_MODEL=claude-sonnet-4-6
API_TOKEN=mon-token-bearer    # protège tes endpoints d'action
```
- Pour du **JSON exploitable** : toujours `temperature=0`.
- Anthropic **n'a pas d'embeddings** : si un bonus en demande, vois `cours_llm` (Voyage / OpenAI / Ollama).
- Les projets 📊 et 🧮 **n'ont pas besoin de clé LLM** : leur `.env` se limite à `API_TOKEN` (et `WEBHOOK_URL` pour la revue de presse), voire rien.

### 2. Le cadre « presta freelance »
Traite chaque projet comme une **vraie commande** :
- Écris **2-3 user stories** en haut de ton README (« En tant que…, je veux…, afin de… »).
- Fais un **croquis d'écran** AVANT de coder (une photo d'un dessin papier suffit pour le jury).
- **Commits réguliers** : un par étape, message clair. Un seul commit final = rouge au jury.

### 3. Les exigences transversales (le jury les cherche PARTOUT)
- 🔒 **Sécurité ANSSI** : secrets hors du code (`.env`), validation des entrées, **anti-injection** (requêtes SQL **paramétrées**, jamais de f-string dans une requête), endpoints protégés par token.
- 🧾 **RGPD** : si tu collectes une donnée perso (email…), **consentement** explicite + données **minimisées**. Si aucune donnée perso, sache **le dire**.
- ♿ **RGAA** : dès le croquis — `<label>` reliés aux champs, contrastes, navigation clavier, alternatives textuelles.
- 🇬🇧 **Anglais B1** : tu liras au moins une doc de bibliothèque en anglais ; note la source.
- 🛰️ **Veille** : garde 2-3 sources que tu suis (sécurité, outils IA).

### 4. Structure attendue de ton rendu (par projet)
```
mon-projet/
├── README.md          ← user stories + install + "comment lancer" + (déploiement)
├── .env.example       ← variables attendues (JAMAIS le vrai .env)
├── .gitignore         ← exclut .env, __pycache__, *.db, sorties générées
├── requirements.txt
├── app.py / scripts   ← ton code (sépare orchestration / métier / données)
└── (data/, templates/, tests…)
```

### 5. Ce qui est volontairement laissé en **bonus**
Le **déploiement** (C10) et la **CI/CD DevOps** (C11) sont en bonus dans chaque projet : sur une mini-presta d'une journée, on les **amorce** (cron, webhook, note Render). Tu les prouveras à fond sur le **projet fil rouge** de ton dossier. Si tu veux les travailler ici, suis `cours_microservice/deploiement_render.md` et ajoute un workflow GitHub Actions qui lance `pytest`.

---

*Adossé au repo de formation : chaque brique pointe vers un `cours_*` réel. Réviser = faire tourner le code, pas seulement le lire.*
