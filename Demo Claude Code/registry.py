# ============================================================
# registry.py — Catalogue des 12 cours et de leurs démos
# ============================================================
# Source unique de vérité pour :
#   - les cartes du hub (page d'accueil)
#   - les formulaires générés automatiquement sur chaque page de cours
#
# Chaque démo est décrite en DONNÉES (pas de code) : le front
# (static/app.js) génère le formulaire et appelle l'endpoint.
#
# Schéma d'une démo :
#   id       : identifiant unique (slug)
#   titre    : titre affiché
#   desc     : courte explication
#   methode  : "GET" ou "POST"
#   url      : chemin de l'endpoint
#   auth     : True => envoie le header Authorization: Bearer <token>
#   rendu    : "json" (défaut), "image" (PNG) ou "download" (fichier)
#   champs   : liste de champs de saisie
#       { nom, label, type, defaut, placeholder }
#       type ∈ "text" | "number" | "textarea" | "json"
#       (GET => les champs deviennent des query params ;
#        POST => les champs deviennent le corps JSON)
# ============================================================


COURS = [
    # --------------------------------------------------------
    {
        "slug": "theorie",
        "numero": 1,
        "titre": "Théorie Python",
        "emoji": "🐍",
        "resume": "Les fondamentaux : variables, conditions, boucles, fonctions, erreurs.",
        "vitrine": [
            "Types de données : int, float, str, bool, list, dict, tuple, set",
            "Conditions (if/elif/else) et boucles (for/while)",
            "Fonctions, méthodes, modules et imports",
            "Gestion d'erreurs avec try/except",
        ],
        "demos": [
            {
                "id": "calc",
                "titre": "Calculatrice (fonctions + erreurs)",
                "desc": "Évalue une opération simple — illustre fonctions et gestion d'erreurs.",
                "methode": "POST",
                "url": "/api/theorie/calc",
                "rendu": "json",
                "champs": [
                    {"nom": "a", "label": "a", "type": "number", "defaut": 7},
                    {"nom": "op", "label": "opérateur", "type": "text", "defaut": "*",
                     "placeholder": "+  -  *  /"},
                    {"nom": "b", "label": "b", "type": "number", "defaut": 6},
                ],
            },
        ],
    },
    # --------------------------------------------------------
    {
        "slug": "api",
        "numero": 2,
        "titre": "API & requêtes HTTP",
        "emoji": "🔌",
        "resume": "Consommer des API externes (GitHub, catalogue) avec requests.",
        "demos": [
            {
                "id": "heure",
                "titre": "Heure serveur (mini-API JSON)",
                "desc": "Le « hello world » d'une API : renvoie l'heure en JSON.",
                "methode": "GET",
                "url": "/api/web/heure",
                "rendu": "json",
                "champs": [],
            },
            {
                "id": "github",
                "titre": "Dépôts GitHub d'un utilisateur",
                "desc": "Appelle l'API publique GitHub et renvoie les dépôts.",
                "methode": "GET",
                "url": "/api/web/github",
                "rendu": "json",
                "champs": [
                    {"nom": "user", "label": "Utilisateur", "type": "text",
                     "defaut": "torvalds"},
                ],
            },
            {
                "id": "catalogue",
                "titre": "Catalogue produits (dummyjson)",
                "desc": "Recherche de produits via une API externe — projet fil rouge.",
                "methode": "GET",
                "url": "/api/web/catalogue",
                "rendu": "json",
                "champs": [
                    {"nom": "q", "label": "Recherche", "type": "text", "defaut": "phone"},
                ],
            },
        ],
    },
    # --------------------------------------------------------
    {
        "slug": "microservice",
        "numero": 3,
        "titre": "Microservice Flask",
        "emoji": "⚙️",
        "resume": "API robuste : auth par token, validation, scoring métier, logs.",
        "demos": [
            {
                "id": "lead",
                "titre": "Scorer un lead (auth requise)",
                "desc": "Validation stricte + logique de scoring. Nécessite le token.",
                "methode": "POST",
                "url": "/api/lead/score",
                "auth": True,
                "rendu": "json",
                "champs": [
                    {"nom": "nom", "label": "Nom", "type": "text", "defaut": "Marie Curie"},
                    {"nom": "email", "label": "Email", "type": "text",
                     "defaut": "marie@entreprise.com"},
                    {"nom": "budget", "label": "Budget (€)", "type": "number", "defaut": 12000},
                ],
            },
            {
                "id": "emails",
                "titre": "Nettoyer une liste d'emails",
                "desc": "Normalise, valide et déduplique. Nécessite le token.",
                "methode": "POST",
                "url": "/api/emails/clean",
                "auth": True,
                "rendu": "json",
                "champs": [
                    {"nom": "emails", "label": "Emails (JSON)", "type": "json",
                     "defaut": '["A@Mail.com", "a@mail.com", "invalide", "b@mail.com"]'},
                ],
            },
            {
                "id": "stats",
                "titre": "Statistiques descriptives",
                "desc": "min, max, moyenne, médiane sur une liste. Nécessite le token.",
                "methode": "POST",
                "url": "/api/stats",
                "auth": True,
                "rendu": "json",
                "champs": [
                    {"nom": "nombres", "label": "Nombres (JSON)", "type": "json",
                     "defaut": "[12, 7, 22, 3, 18, 9]"},
                ],
            },
        ],
    },
    # --------------------------------------------------------
    {
        "slug": "cron",
        "numero": 4,
        "titre": "Tâches planifiées",
        "emoji": "⏰",
        "resume": "Planification de jobs : syntaxe cron et déclenchement manuel.",
        "demos": [
            {
                "id": "expressions",
                "titre": "Antisèche des expressions cron",
                "desc": "Renvoie des exemples d'expressions cron commentées.",
                "methode": "GET",
                "url": "/api/cron/expressions",
                "rendu": "json",
                "champs": [],
            },
            {
                "id": "trigger",
                "titre": "Déclencher un job maintenant",
                "desc": "Exécute immédiatement une tâche planifiée (surveillance de prix).",
                "methode": "POST",
                "url": "/api/cron/trigger",
                "rendu": "json",
                "champs": [
                    {"nom": "job", "label": "Job", "type": "text", "defaut": "surveillance"},
                ],
            },
        ],
    },
    # --------------------------------------------------------
    {
        "slug": "data",
        "numero": 5,
        "titre": "Manipulation de données",
        "emoji": "📊",
        "resume": "Lire et analyser des données (pandas), générer un rapport Excel.",
        "demos": [
            {
                "id": "stats",
                "titre": "Stats sur un CSV collé",
                "desc": "Colle un CSV : pandas calcule des statistiques par colonne.",
                "methode": "POST",
                "url": "/api/data/stats",
                "rendu": "json",
                "champs": [
                    {"nom": "csv", "label": "Contenu CSV", "type": "textarea",
                     "defaut": "produit,prix,quantite\nstylo,1.5,10\ncahier,3.2,5\ngomme,0.8,20"},
                ],
            },
            {
                "id": "report",
                "titre": "Rapport Excel automatisé",
                "desc": "Génère un classeur Excel multi-onglets téléchargeable.",
                "methode": "POST",
                "url": "/api/data/report",
                "rendu": "download",
                "champs": [
                    {"nom": "csv", "label": "Contenu CSV", "type": "textarea",
                     "defaut": "produit,prix,quantite\nstylo,1.5,10\ncahier,3.2,5\ngomme,0.8,20"},
                ],
            },
        ],
    },
    # --------------------------------------------------------
    {
        "slug": "dataviz",
        "numero": 6,
        "titre": "Visualisation",
        "emoji": "📈",
        "resume": "Générer des graphiques (matplotlib) servis en PNG par l'API.",
        "demos": [
            {
                "id": "chart",
                "titre": "Graphique de démonstration",
                "desc": "Renvoie un PNG d'exemple généré par matplotlib.",
                "methode": "GET",
                "url": "/api/chart",
                "rendu": "image",
                "champs": [],
            },
            {
                "id": "build",
                "titre": "Construire un graphique",
                "desc": "Choisis le type et les données : l'API renvoie un PNG.",
                "methode": "POST",
                "url": "/api/chart/build",
                "rendu": "image",
                "champs": [
                    {"nom": "titre", "label": "Titre", "type": "text", "defaut": "Ventes 2026"},
                    {"nom": "type", "label": "Type (bar/line/pie)", "type": "text",
                     "defaut": "bar"},
                    {"nom": "labels", "label": "Labels (JSON)", "type": "json",
                     "defaut": '["Jan", "Fév", "Mar", "Avr"]'},
                    {"nom": "valeurs", "label": "Valeurs (JSON)", "type": "json",
                     "defaut": "[12, 19, 7, 23]"},
                ],
            },
        ],
    },
    # --------------------------------------------------------
    {
        "slug": "scraping",
        "numero": 7,
        "titre": "Web scraping",
        "emoji": "🕷️",
        "resume": "Télécharger et parser du HTML avec requests + BeautifulSoup.",
        "demos": [
            {
                "id": "books",
                "titre": "Scraper books.toscrape.com",
                "desc": "Récupère titres, prix, notes et disponibilité sur N pages.",
                "methode": "GET",
                "url": "/api/scrape/books",
                "rendu": "json",
                "champs": [
                    {"nom": "pages", "label": "Nombre de pages", "type": "number",
                     "defaut": 1},
                ],
            },
        ],
    },
    # --------------------------------------------------------
    {
        "slug": "panorama",
        "numero": 8,
        "titre": "Panorama de l'IA",
        "emoji": "🗺️",
        "resume": "Vision 360° : IA ⊃ Machine Learning ⊃ Deep Learning ⊃ IA générative.",
        "vitrine": [
            "3 types d'apprentissage : supervisé, non-supervisé, par renforcement",
            "Grandes familles : vision, langage (NLP), audio, génératif",
            "Vocabulaire structurant du domaine",
        ],
        "demos": [
            {
                "id": "glossaire",
                "titre": "Glossaire de la formation (JSON)",
                "desc": "Renvoie le glossaire cumulé des 12 cours, structuré.",
                "methode": "GET",
                "url": "/api/panorama/glossaire",
                "rendu": "json",
                "champs": [
                    {"nom": "q", "label": "Filtre (optionnel)", "type": "text", "defaut": ""},
                ],
            },
        ],
    },
    # --------------------------------------------------------
    {
        "slug": "ml",
        "numero": 9,
        "titre": "Machine Learning",
        "emoji": "🤖",
        "resume": "Workflow supervisé complet : entraîner, évaluer, prédire (scikit-learn).",
        "demos": [
            {
                "id": "iris",
                "titre": "Prédire l'espèce d'un iris (k-NN)",
                "desc": "4 mesures de fleur → espèce prédite par un k-NN entraîné sur Iris.",
                "methode": "POST",
                "url": "/api/ml/iris",
                "rendu": "json",
                "champs": [
                    {"nom": "features", "label": "Mesures [sép.long, sép.larg, pét.long, pét.larg]",
                     "type": "json", "defaut": "[5.1, 3.5, 1.4, 0.2]"},
                ],
            },
            {
                "id": "evaluate",
                "titre": "Évaluer le modèle",
                "desc": "Accuracy, matrice de confusion et rapport de classification.",
                "methode": "GET",
                "url": "/api/ml/evaluate",
                "rendu": "json",
                "champs": [],
            },
            {
                "id": "boundary",
                "titre": "Frontière de décision (PNG)",
                "desc": "Visualise la frontière de décision sur 2 dimensions.",
                "methode": "GET",
                "url": "/api/ml/boundary.png",
                "rendu": "image",
                "champs": [],
            },
        ],
    },
    # --------------------------------------------------------
    {
        "slug": "deep_learning",
        "numero": 10,
        "titre": "Deep Learning",
        "emoji": "🧠",
        "resume": "Du perceptron (numpy) au réseau de neurones sur chiffres manuscrits.",
        "demos": [
            {
                "id": "perceptron",
                "titre": "Perceptron : OR / AND / XOR",
                "desc": "Entraîne un perceptron à la main et montre l'échec sur XOR.",
                "methode": "POST",
                "url": "/api/dl/perceptron",
                "rendu": "json",
                "champs": [
                    {"nom": "fonction", "label": "Fonction logique (OR/AND/XOR)",
                     "type": "text", "defaut": "XOR"},
                ],
            },
            {
                "id": "digit",
                "titre": "Reconnaître un chiffre (MLP)",
                "desc": "64 pixels (image 8×8) → chiffre prédit + probabilités.",
                "methode": "POST",
                "url": "/api/dl/digit",
                "rendu": "json",
                "champs": [
                    {"nom": "pixels", "label": "64 pixels (JSON, 0-16)", "type": "json",
                     "defaut": "[]", "placeholder": "Laisse vide => exemple aléatoire du jeu de test"},
                ],
            },
            {
                "id": "accuracy",
                "titre": "Précision du réseau",
                "desc": "Accuracy du MLP sur le jeu de test des chiffres.",
                "methode": "GET",
                "url": "/api/dl/accuracy",
                "rendu": "json",
                "champs": [],
            },
        ],
    },
    # --------------------------------------------------------
    {
        "slug": "llm",
        "numero": 11,
        "titre": "LLM : comprendre & utiliser",
        "emoji": "💬",
        "resume": "Prompting, sortie JSON, RAG, embeddings — via une API LLM réelle.",
        "demos": [
            {
                "id": "chat",
                "titre": "Chat simple",
                "desc": "Un message → une réponse du modèle. (Appel réel, token requis)",
                "methode": "POST",
                "url": "/api/llm/chat",
                "auth": True,
                "rendu": "json",
                "champs": [
                    {"nom": "message", "label": "Message", "type": "textarea",
                     "defaut": "Explique ce qu'est un token en une phrase."},
                    {"nom": "system", "label": "Rôle système (optionnel)", "type": "text",
                     "defaut": "Tu es un formateur concis."},
                ],
            },
            {
                "id": "json",
                "titre": "Sortie structurée JSON",
                "desc": "Force le modèle à répondre en JSON (analyse de sentiment).",
                "methode": "POST",
                "url": "/api/llm/json",
                "auth": True,
                "rendu": "json",
                "champs": [
                    {"nom": "avis", "label": "Avis client", "type": "textarea",
                     "defaut": "Produit génial mais livraison très lente."},
                ],
            },
            {
                "id": "rag",
                "titre": "Mini-RAG",
                "desc": "Recherche le passage pertinent (TF-IDF) puis répond.",
                "methode": "POST",
                "url": "/api/llm/rag",
                "auth": True,
                "rendu": "json",
                "champs": [
                    {"nom": "question", "label": "Question", "type": "text",
                     "defaut": "Quels sont les horaires d'ouverture ?"},
                ],
            },
            {
                "id": "embeddings",
                "titre": "Embeddings",
                "desc": "Transforme des textes en vecteurs. (Nécessite EMBED_* configuré)",
                "methode": "POST",
                "url": "/api/llm/embeddings",
                "auth": True,
                "rendu": "json",
                "champs": [
                    {"nom": "textes", "label": "Textes (JSON)", "type": "json",
                     "defaut": '["chat", "chien", "voiture"]'},
                ],
            },
        ],
    },
    # --------------------------------------------------------
    {
        "slug": "agents",
        "numero": 12,
        "titre": "Agents LLM",
        "emoji": "🛠️",
        "resume": "Boucle perception→raisonnement→action : tool calling, ReAct, multi-outils.",
        "demos": [
            {
                "id": "tool-calling",
                "titre": "Tool calling (météo)",
                "desc": "Le modèle décide d'appeler un outil pour répondre. (Appel réel)",
                "methode": "POST",
                "url": "/api/agent/tool-calling",
                "auth": True,
                "rendu": "json",
                "champs": [
                    {"nom": "question", "label": "Question", "type": "text",
                     "defaut": "Quel temps fait-il à Lyon ?"},
                ],
            },
            {
                "id": "react",
                "titre": "Boucle ReAct (trace)",
                "desc": "Pensée → Action → Observation, à la main, avec trace complète.",
                "methode": "POST",
                "url": "/api/agent/react",
                "auth": True,
                "rendu": "json",
                "champs": [
                    {"nom": "question", "label": "Question", "type": "text",
                     "defaut": "Combien font 3 * 19.99, et quelle heure est-il ?"},
                ],
            },
            {
                "id": "multi-tools",
                "titre": "Agent multi-outils",
                "desc": "Tool calling natif avec 3 outils (calcul, météo, heure).",
                "methode": "POST",
                "url": "/api/agent/multi-tools",
                "auth": True,
                "rendu": "json",
                "champs": [
                    {"nom": "question", "label": "Question", "type": "text",
                     "defaut": "Quelle heure est-il et quel temps à Paris ?"},
                ],
            },
            {
                "id": "mcp-tools",
                "titre": "Outils exposés (MCP)",
                "desc": "Liste les outils déclarés par le serveur MCP du cours.",
                "methode": "GET",
                "url": "/api/agent/mcp-tools",
                "rendu": "json",
                "champs": [],
            },
        ],
    },
]


# Index pratique slug -> cours
PAR_SLUG = {c["slug"]: c for c in COURS}


def get_cours(slug):
    """Retourne le dict d'un cours par son slug, ou None."""
    return PAR_SLUG.get(slug)
