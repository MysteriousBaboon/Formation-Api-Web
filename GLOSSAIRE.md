# 📖 Glossaire cumulé — La Dinguerie

Les **notions et concepts** de la formation (Python → IA) réunis à un seul endroit. On y met le
vocabulaire à comprendre — pas la liste des fonctions/méthodes (ça, c'est dans la doc des
librairies). Chaque entrée donne une définition courte et un ou plusieurs **tags** indiquant le(s)
cours où la notion est abordée. Termes triés alphabétiquement dans chaque catégorie.

> Ce fichier est le surensemble global de `cours_ia_panorama/glossaire.md` (le lexique de la journée 8).

## Légende des tags

| Tag | Cours | Sujet |
|-----|-------|-------|
| `Python` | `cours_theorie` | Fondamentaux Python |
| `API` | `cours_api` | HTTP & APIs |
| `Scraping` | `cours_scraping` | Web scraping |
| `Données` | `cours_data` | CSV, pandas, Excel, PDF, regex |
| `Dataviz` | `cours_dataviz` | matplotlib, plotly |
| `Cron` | `cours_cron` | Planification & automatisation |
| `Microservice` | `cours_microservice` | Flask, webhooks, déploiement |
| `IA` | `cours_ia_panorama` | Panorama de l'IA |
| `ML` | `cours_machine_learning` | Machine learning classique |
| `DL` | `cours_deep_learning` | Réseaux de neurones |
| `LLM` | `cours_llm` | Modèles de langage & prompting |
| `Agents` | `cours_agents_llm` | Agents IA |

## Sommaire

**Bloc 1 — Python & outils de dev**
- [Python fondamentaux](#python-fondamentaux)
- [HTTP, API et Web](#http-api-et-web)
- [Web scraping](#web-scraping)
- [Données et fichiers](#données-et-fichiers)
- [Visualisation](#visualisation)
- [Automatisation et planification](#automatisation-et-planification)
- [Micro-services et déploiement](#micro-services-et-déploiement)

**Bloc 2 — Intelligence artificielle**
- [IA, panorama et vocabulaire](#ia-panorama-et-vocabulaire)
- [Machine Learning](#machine-learning)
- [Deep Learning](#deep-learning)
- [LLM, modèles de langage](#llm-modèles-de-langage)
- [Agents IA](#agents-ia)

---

# Bloc 1 — Python & outils de dev

## Python fondamentaux

- **Alias** — Nom raccourci donné à un module lors de l'import (ex. numpy → np). _(Python)_
- **Argument** — Une valeur passée à une fonction au moment de l'appel. _(Python)_
- **Argument obligatoire (positionnel)** — Argument qui doit toujours être fourni. _(Python)_
- **Argument optionnel** — Argument muni d'une valeur par défaut, donc facultatif. _(Python)_
- **Booléen** — Type à deux valeurs possibles : vrai ou faux. _(Python)_
- **Boucle `for`** — Parcourir une collection et exécuter du code pour chaque élément. _(Python)_
- **Boucle `while`** — Répéter du code tant qu'une condition reste vraie. _(Python)_
- **`break`** — Sortir immédiatement d'une boucle. _(Python)_
- **Chaînage de méthodes** — Enchaîner plusieurs méthodes sur le même objet. _(Python)_
- **Condition (`if` / `elif` / `else`)** — Exécuter du code différent selon qu'une condition est vraie ou fausse. _(Python)_
- **`continue`** — Passer directement à l'itération suivante d'une boucle. _(Python)_
- **Conversion de type (casting)** — Transformer une valeur d'un type vers un autre (texte ↔ nombre…). _(Python)_
- **Dictionnaire (dict)** — Collection de paires clé → valeur, accès par la clé. _(Python)_
- **Docstring** — Texte de documentation décrivant ce que fait une fonction. _(Python)_
- **Exception** — Une erreur survenant à l'exécution. _(Python)_
- **F-string** — Chaîne de texte dans laquelle on insère directement des variables. _(Python)_
- **Fonction** — Bloc de code réutilisable qui prend des entrées et renvoie un résultat. _(Python)_
- **Gestion d'erreurs (`try` / `except`)** — Capturer une erreur pour réagir au lieu de planter. _(Python)_
- **Import** — Charger un module ou une fonction pour s'en servir. _(Python)_
- **Liste (list)** — Collection ordonnée et modifiable d'éléments. _(Python)_
- **`match` / `case`** — Choisir un bloc à exécuter selon une valeur (sélection). _(Python)_
- **Méthode** — Une fonction attachée à un objet, appelée « sur » lui (notation point). _(Python)_
- **Module** — Un fichier de code Python réutilisable que l'on importe. _(Python)_
- **`None`** — Valeur spéciale représentant l'absence de valeur. _(Python)_
- **Nombre (`int` / `float`)** — Entier (`int`) ou nombre à virgule (`float`). _(Python)_
- **Opérateurs arithmétiques** — Symboles de calcul (addition, multiplication, modulo…). _(Python)_
- **Opérateurs d'affectation** — Assigner ou mettre à jour une variable. _(Python)_
- **Opérateurs de comparaison** — Comparer deux valeurs (résultat vrai/faux). _(Python)_
- **Opérateurs logiques** — Combiner des conditions (`et`, `ou`, `non`). _(Python)_
- **Package** — Un dossier regroupant plusieurs modules. _(Python)_
- **`pass`** — Mot-clé « ne rien faire », utile comme emplacement temporaire. _(Python)_
- **`raise`** — Déclencher volontairement une exception. _(Python)_
- **`return`** — Renvoyer un résultat depuis une fonction. _(Python)_
- **Set (ensemble)** — Collection d'éléments uniques, sans doublon. _(Python)_
- **Slicing (découpage)** — Extraire une portion d'une liste ou d'un texte. _(Python)_
- **Texte (str)** — Type représentant une chaîne de caractères. _(Python)_
- **Tuple** — Collection ordonnée mais immuable. _(Python)_
- **Type de données** — La nature d'une valeur (nombre, texte, booléen, liste…). _(Python)_
- **Variable** — Un nom qui désigne une valeur stockée en mémoire. _(Python)_

## HTTP, API et Web

- **API** — Interface permettant à deux programmes de communiquer. _(API)_
- **API REST** — Style d'API utilisant HTTP de façon standard (verbes, URLs, codes). _(API)_
- **Body (corps)** — Le contenu principal d'une requête ou d'une réponse. _(API)_
- **Endpoint** — Une URL précise d'une API, correspondant à une action. _(API, Microservice)_
- **En-tête (header)** — Métadonnée accompagnant une requête/réponse (type de contenu, auth…). _(API, Scraping)_
- **Flask** — Micro-framework Python pour créer des applis web et des APIs. _(API, Microservice)_
- **GET** — Verbe HTTP pour lire des données. _(API)_
- **HTTP** — Le protocole de communication entre client et serveur web. _(API)_
- **JSON** — Format texte standard pour échanger des données structurées. _(API, Données, LLM)_
- **Mode debug (Flask)** — Mode de développement : rechargement auto et erreurs détaillées. _(API)_
- **Paramètre d'URL** — Variable insérée dans le chemin d'une URL. _(API)_
- **POST** — Verbe HTTP pour envoyer des données. _(API)_
- **PUT** — Verbe HTTP pour remplacer une ressource. _(API)_
- **DELETE** — Verbe HTTP pour supprimer une ressource. _(API)_
- **Query string** — Données ajoutées à une URL après le `?`. _(API)_
- **requests** — La librairie Python de référence pour les requêtes HTTP. _(API, Scraping)_
- **Requête HTTP** — Message envoyé par le client pour demander une action. _(API)_
- **Réponse HTTP** — Message renvoyé par le serveur. _(API)_
- **Route** — L'association d'une URL à une fonction du serveur. _(API)_
- **Code de statut HTTP** — Nombre résumant le résultat d'une requête. _(API)_
- **Statut 200 (OK)** — La requête a réussi. _(API)_
- **Statut 404 (Not Found)** — Ressource introuvable. _(API)_
- **Statut 500 (Server Error)** — Erreur côté serveur. _(API)_
- **Timeout** — Délai maximum d'attente d'une réponse. _(API)_

## Web scraping

- **Anti-bot** — Mesures d'un site pour détecter et bloquer les robots. _(Scraping)_
- **Attribut HTML** — Information portée par une balise (`href`, `class`, `id`…). _(Scraping)_
- **Balise HTML** — Élément délimité par `< >` qui structure une page. _(Scraping)_
- **BeautifulSoup** — Librairie Python pour analyser du HTML et en extraire des données. _(Scraping)_
- **Browser headless** — Navigateur sans interface, piloté par du code. _(Scraping)_
- **CAPTCHA** — Test destiné à distinguer un humain d'un robot. _(Scraping)_
- **Classe (HTML)** — Attribut servant à regrouper/cibler des éléments. _(Scraping)_
- **Cookie** — Donnée stockée côté client pour garder un état entre requêtes. _(Scraping)_
- **DOM** — La page HTML vue comme un arbre d'éléments. _(Scraping)_
- **HTML** — Le langage de balisage qui structure une page web. _(Scraping)_
- **ID (HTML)** — Attribut identifiant de façon unique un élément. _(Scraping)_
- **JavaScript côté client** — Code exécuté dans le navigateur, modifiant la page après chargement. _(Scraping)_
- **Pagination** — Parcourir automatiquement plusieurs pages de résultats. _(Scraping)_
- **Parsing (analyse)** — Transformer du texte brut (HTML…) en données exploitables. _(Scraping)_
- **Playwright** — Outil pilotant un vrai navigateur, utile pour les sites en JavaScript. _(Scraping)_
- **robots.txt** — Fichier où un site indique ce que les robots peuvent visiter. _(Scraping)_
- **Sélecteur CSS** — Syntaxe pour cibler des éléments précis d'une page. _(Scraping)_
- **Session** — Connexion réutilisée qui conserve cookies et en-têtes. _(Scraping)_
- **SPA (Single Page Application)** — Site chargeant son contenu dynamiquement, sans rechargement. _(Scraping)_
- **Statut 403 (Forbidden)** — Le site refuse la requête. _(Scraping)_
- **Statut 429 (Too Many Requests)** — Trop de requêtes : il faut ralentir. _(Scraping)_
- **User-Agent** — En-tête identifiant le navigateur/client qui fait la requête. _(Scraping)_
- **Web scraping** — Extraction automatique de données depuis des pages web. _(Scraping)_

## Données et fichiers

- **CSV** — Format de tableau en texte simple, valeurs séparées par un délimiteur. _(Données, Scraping)_
- **DataFrame** — Structure en tableau (lignes × colonnes), brique de base de l'analyse de données. _(Données, Scraping, Dataviz)_
- **Délimiteur** — Le caractère qui sépare les colonnes d'un fichier. _(Données)_
- **Encodage** — La façon dont le texte est représenté en octets (UTF-8…). _(Données)_
- **Excel** — Format de feuille de calcul tabulaire (`.xlsx`). _(Données)_
- **Expression régulière (regex)** — Un motif pour rechercher/extraire du texte selon une forme. _(Données)_
- **Filtrage** — Sélectionner les lignes d'un tableau qui respectent une condition. _(Données)_
- **Groupe de capture** — Partie d'une regex que l'on isole pour récupérer sa valeur. _(Données)_
- **Groupe nommé** — Un groupe de capture auquel on donne un nom, pour la lisibilité. _(Données)_
- **openpyxl** — Librairie Python pour lire et écrire des fichiers Excel. _(Données)_
- **pandas** — La librairie Python de référence pour manipuler et analyser des données. _(Données)_
- **pathlib** — Librairie pour manipuler proprement les chemins de fichiers. _(Données)_
- **PDF** — Format de document portable, dont on peut extraire le texte. _(Données)_
- **pypdf** — Librairie Python pour lire du texte dans des PDF. _(Données)_
- **Series** — Une colonne unique de données (une dimension d'un DataFrame). _(Données)_

## Visualisation

- **Camembert** — Montrer la répartition d'un tout en parts. _(Dataviz)_
- **Courbe (ligne)** — Montrer une évolution, souvent dans le temps. _(Dataviz)_
- **Diagramme en barres** — Comparer des quantités par catégorie. _(Dataviz)_
- **Graphe interactif** — Visualisation explorable (zoom, survol), typiquement en HTML. _(Dataviz)_
- **Histogramme** — Montrer la distribution d'une variable (fréquence des valeurs). _(Dataviz)_
- **matplotlib** — La librairie Python de base pour tracer des graphiques. _(Dataviz)_
- **Nuage de points** — Montrer la relation entre deux variables. _(Dataviz)_
- **plotly** — Librairie pour des graphiques interactifs. _(Dataviz)_
- **Visualisation de données** — Représenter des données sous forme graphique pour les comprendre. _(Dataviz)_

## Automatisation et planification

- **Automatisation** — Faire exécuter une tâche par la machine, sans intervention humaine. _(Cron)_
- **cron** — Standard Unix/Linux pour planifier l'exécution de tâches. _(Cron)_
- **crontab** — La table où sont déclarées les tâches cron d'un système. _(Cron)_
- **Expression cron** — Notation à 5 champs (minute, heure, jour, mois, jour de semaine) décrivant une fréquence. _(Cron)_
- **Planification** — Programmer une tâche pour qu'elle s'exécute à des moments précis. _(Cron)_
- **schedule** — Librairie Python simple pour planifier des tâches. _(Cron)_
- **Scheduler (planificateur)** — Le composant qui déclenche les tâches au bon moment. _(Cron)_

## Micro-services et déploiement

- **Bearer token** — Jeton d'authentification envoyé dans l'en-tête `Authorization`. _(Microservice)_
- **Décorateur** — Une fonction qui en enveloppe une autre pour lui ajouter un comportement. _(Microservice)_
- **Déploiement continu** — Remettre l'application en ligne automatiquement à chaque mise à jour du code. _(Microservice)_
- **Domaine** — L'adresse publique d'un service déployé. _(Microservice)_
- **dotenv** — Mécanisme/librairie chargeant les variables d'un fichier `.env`. _(Microservice)_
- **gunicorn** — Serveur qui fait tourner une appli Python (Flask) en production. _(Microservice)_
- **Health check** — Endpoint servant à vérifier que le service est en ligne. _(Microservice)_
- **Logging** — Enregistrer les événements du programme pour suivre et déboguer. _(Microservice, Cron)_
- **Micro-service** — Petite application serveur dédiée à une seule tâche. _(Microservice)_
- **n8n** — Outil no-code d'automatisation reliant de nombreux services. _(Microservice, Cron, Agents)_
- **Orchestration** — Coordonner plusieurs services pour accomplir une tâche globale. _(Microservice)_
- **Port** — Numéro par lequel on joint un service sur une machine. _(Microservice)_
- **Render (PaaS)** — Plateforme qui héberge et fait tourner une application. _(Microservice)_
- **Statut 201 (Created)** — Une ressource a été créée. _(Microservice)_
- **Statut 400 (Bad Request)** — Les données envoyées sont invalides. _(Microservice)_
- **Statut 401 (Unauthorized)** — Authentification requise ou échouée. _(Microservice)_
- **Token d'authentification** — Clé secrète identifiant un appelant autorisé. _(Microservice)_
- **Validation** — Vérifier que les données reçues sont correctes et sûres. _(Microservice)_
- **Variables d'environnement (.env)** — Réglages et secrets stockés hors du code, jamais partagés. _(Microservice)_
- **`.gitignore`** — Fichier listant ce que Git doit ignorer (dont les secrets). _(Microservice)_
- **Webhook** — URL appelée par un système externe pour déclencher une action. _(Microservice, Cron)_

---

# Bloc 2 — Intelligence artificielle

## IA, panorama et vocabulaire

- **AlexNet** — Réseau gagnant d'ImageNet (2012), point de relance du deep learning. _(IA)_
- **Algorithme** — La recette/méthode d'apprentissage (arbre de décision, k-NN…). _(IA)_
- **AlphaGo** — Système IA ayant battu le champion du monde de Go. _(IA)_
- **Apprentissage non-supervisé** — Trouver des structures sans étiquettes (groupes, anomalies). _(IA)_
- **Apprentissage par renforcement** — Apprendre par essais/erreurs, guidé par une récompense. _(IA)_
- **Apprentissage supervisé** — Apprendre à partir d'exemples étiquetés (entrée + bonne réponse). _(IA)_
- **« Attention is all you need »** — Article fondateur des Transformers (2017). _(IA, LLM)_
- **Audio / voix** — Famille d'IA traitant les sons et la parole. _(IA)_
- **Biais** — Préjugés présents dans les données, reproduits voire amplifiés par le modèle. _(IA)_
- **Classification** — Prédire une catégorie (spam / pas spam). _(IA, ML)_
- **Compression (réduction de dimension)** — Représenter des données avec moins de variables. _(IA)_
- **Computer vision (vision)** — Famille d'IA traitant images et vidéos. _(IA, DL)_
- **Dataset** — L'ensemble des données d'exemple servant à entraîner/tester. _(IA)_
- **Décision / robotique** — Famille d'IA choisissant des actions dans un environnement. _(IA)_
- **Deep Learning** — Du ML fondé sur des réseaux de neurones à plusieurs couches. _(IA, DL)_
- **Détection d'anomalies** — Identifier des cas inhabituels dans les données. _(IA)_
- **Échantillon / instance** — Une ligne du dataset (un exemple). _(IA)_
- **Entraînement** — La phase, lente, où le modèle apprend. _(IA)_
- **Feature (caractéristique)** — Une variable d'entrée du modèle (surface, âge…). _(IA, ML)_
- **Garbage in, garbage out** — De mauvaises données produisent un mauvais modèle. _(IA)_
- **GenAI / IA générative** — IA qui crée du contenu (texte, image, son). _(IA, LLM)_
- **Hivers de l'IA** — Périodes (1970-1990) de coupes de financement de la recherche. _(IA)_
- **IA (Intelligence Artificielle)** — Programme réalisant des tâches « intelligentes » ; le grand ensemble. _(IA)_
- **ImageNet** — Célèbre compétition de classification d'images. _(IA)_
- **Inférence** — La phase, rapide, où l'on utilise le modèle pour prédire. _(IA)_
- **Label (étiquette)** — La bonne réponse à prédire (le prix réel, la classe « chat »). _(IA, ML)_
- **Machine Learning (ML)** — Sous-ensemble de l'IA où la machine apprend depuis les données. _(IA, ML)_
- **Maths + données + puissance de calcul** — Les trois ingrédients d'une IA. _(IA)_
- **Modèle** — Le résultat de l'entraînement : ce qui fait les prédictions. _(IA)_
- **NLP (traitement du langage naturel)** — Famille d'IA traitant le texte et le langage. _(IA, LLM)_
- **Recommandation** — Famille d'IA prédisant préférences et comportements. _(IA)_
- **Régression** — Prédire un nombre (un prix, une température). _(IA, ML)_
- **Règle par règle** — Approche classique (non-ML) où l'on code explicitement les règles. _(IA)_
- **Segmentation / clustering** — Trouver des groupes naturels dans des données non étiquetées. _(IA)_
- **Sur-apprentissage (overfitting)** — Le modèle apprend « par cœur » et rate les nouveaux cas. _(IA, ML)_
- **Train / Test** — On entraîne sur une partie des données, on teste sur une autre jamais vue. _(IA, ML)_

## Machine Learning

- **Accuracy** — Proportion de prédictions correctes. _(ML)_
- **Arbre de décision** — Suite de questions oui/non aboutissant à une décision lisible. _(ML)_
- **Boosting** — Combiner des modèles faibles pour en former un fort. _(ML)_
- **Bruit** — Erreurs et irrégularités présentes dans les données. _(ML)_
- **Complexité du modèle** — À quel point un modèle est « riche » ; influe sur le sur/sous-apprentissage. _(ML)_
- **Déséquilibre de classes** — Quand une catégorie est bien plus représentée que les autres. _(ML)_
- **Forêts aléatoires (Random Forest)** — Combinaison de nombreux arbres pour un modèle plus robuste. _(ML)_
- **Interface unifiée (scikit-learn)** — Tous les modèles s'utilisent pareil : entraîner, prédire, évaluer. _(ML)_
- **k plus proches voisins (k-NN)** — Classer un point selon la majorité de ses voisins les plus proches. _(ML)_
- **MAE (erreur absolue moyenne)** — Erreur moyenne d'une prédiction de nombre, en valeur absolue. _(ML)_
- **Matrice de confusion** — Tableau croisant prédictions et réalité, pour voir les types d'erreurs. _(ML)_
- **Normalisation (standardisation)** — Mettre les variables à une échelle comparable. _(ML)_
- **Pipeline ML** — L'enchaînement type : données → features → train/test → entraînement → évaluation → prédiction. _(ML)_
- **Précision** — Parmi les cas prédits « positifs », la part réellement positifs. _(ML)_
- **Rappel** — Parmi les vrais positifs, la part effectivement retrouvée. _(ML)_
- **Régression linéaire** — Prédire un nombre en ajustant une droite (ou un plan). _(ML)_
- **Régression logistique** — Un modèle de classification (malgré son nom). _(ML)_
- **RMSE (erreur quadratique moyenne)** — Mesure d'erreur qui pénalise davantage les grosses erreurs. _(ML)_
- **scikit-learn** — La librairie Python de référence pour le machine learning classique. _(ML)_
- **Sous-apprentissage (underfitting)** — Modèle trop simple, qui rate même les données d'entraînement. _(ML)_
- **SVM (Support Vector Machine)** — Modèle cherchant la meilleure frontière entre les classes. _(ML)_
- **Validation croisée** — Évaluer un modèle sur plusieurs découpages train/test pour un résultat plus fiable. _(ML)_

## Deep Learning

- **Abstraction** — La capacité des couches profondes à reconnaître des concepts de plus en plus complexes. _(DL)_
- **Biais (bias)** — Terme constant ajouté à un neurone, décalant son seuil de déclenchement. _(DL)_
- **Boîte noire** — Un modèle dont on explique difficilement les décisions. _(DL)_
- **CNN (réseau convolutif)** — Réseau de neurones spécialisé pour les images. _(DL, IA)_
- **Convolution** — Faire glisser des filtres sur une image pour y détecter des motifs. _(DL)_
- **Couche (layer)** — Un étage de neurones ; « profond » = beaucoup de couches. _(DL)_
- **Couches cachées** — Les couches situées entre l'entrée et la sortie. _(DL)_
- **Descente de gradient** — Méthode d'ajustement des poids dans le sens qui réduit l'erreur. _(DL)_
- **Fonction d'activation** — La décision non-linéaire d'un neurone (ReLU, sigmoïde…). _(DL)_
- **Fonction de perte** — Mesure de l'écart entre la prédiction et la vraie réponse. _(DL)_
- **GPU** — Puce qui accélère massivement l'entraînement des réseaux. _(DL, IA)_
- **Interprétabilité** — La capacité à comprendre les décisions d'un modèle. _(DL)_
- **Learning rate (taux d'apprentissage)** — La taille du pas lors de l'ajustement des poids. _(DL)_
- **LSTM** — Type de RNN gardant une mémoire plus longue. _(DL)_
- **MLP (perceptron multicouche)** — Réseau dense, tous les neurones connectés. _(DL)_
- **Motifs (bords, formes, objets)** — Ce que les couches successives d'un CNN apprennent à reconnaître. _(DL)_
- **Neurone / perceptron** — L'unité de base : combine des entrées pondérées et produit une sortie. _(DL, IA)_
- **Non-linéarité** — Propriété donnant au réseau sa capacité à modéliser des phénomènes complexes. _(DL)_
- **Pixel** — Unité d'une image (sa valeur = l'intensité). _(DL)_
- **Poids / paramètres** — Les réglages internes ajustés pendant l'entraînement. _(DL, IA)_
- **Profondeur** — Le nombre de couches d'un réseau. _(DL)_
- **Propagation avant (forward pass)** — Le passage des données à travers le réseau jusqu'à la sortie. _(DL)_
- **ReLU** — Fonction d'activation standard du deep learning moderne. _(DL)_
- **Réseau de neurones** — Modèle composé de neurones organisés en couches. _(DL, IA)_
- **Rétropropagation (backprop)** — Calculer la part d'erreur de chaque poids pour le corriger. _(DL, IA)_
- **RNN (réseau récurrent)** — Réseau spécialisé pour les séquences (texte, séries temporelles). _(DL)_
- **Sigmoïde** — Fonction d'activation lisse, en S, entre 0 et 1. _(DL)_
- **Transfer learning** — Réutiliser un modèle déjà entraîné pour un nouveau problème. _(DL, IA)_

## LLM, modèles de langage

- **API compatible OpenAI** — Interface standard que proposent la plupart des fournisseurs de LLM. _(LLM)_
- **Attention** — Mécanisme clé du Transformer reliant chaque mot à tous les autres. _(LLM)_
- **Cutoff** — Date au-delà de laquelle le modèle ne connaît rien (pas d'actualité). _(LLM)_
- **Embeddings** — Vecteurs de nombres représentant le *sens* d'un texte. _(LLM)_
- **Fenêtre de contexte** — La quantité de texte que le modèle peut « voir » d'un coup. _(LLM, IA)_
- **Few-shot** — Donner quelques exemples dans le prompt pour guider le modèle. _(LLM)_
- **Fine-tuning** — Ré-entraîner un modèle existant sur des données spécifiques. _(LLM, IA)_
- **Hallucination** — Quand le modèle invente une réponse fausse avec aplomb. _(LLM, IA)_
- **LLM (Large Language Model)** — Grand modèle de langage entraîné sur d'immenses quantités de texte. _(LLM, IA)_
- **LLM local (Ollama)** — Faire tourner un modèle sur sa propre machine, gratuitement. _(LLM)_
- **Mixture of Experts (MoE)** — Architecture activant seulement quelques sous-réseaux experts par requête. _(LLM)_
- **Modèle dense** — Modèle activant tous ses paramètres à chaque token (opposé de MoE). _(LLM)_
- **Paramètres activés vs stockés** — La capacité totale du modèle vs le calcul réellement fait par token. _(LLM)_
- **Pré-entraînement** — La phase où le modèle apprend à prédire le mot suivant sur une masse de texte. _(LLM)_
- **Prompt** — L'instruction ou la question donnée au modèle. _(LLM, IA)_
- **RAG (Retrieval-Augmented Generation)** — Donner au modèle des documents à consulter pour répondre. _(LLM, IA)_
- **RLHF** — Affiner le modèle d'après des réponses classées par des humains. _(LLM)_
- **Rôle (system / user / assistant)** — Le type d'un message : cadre/règles, demande, réponse du modèle. _(LLM)_
- **Similarité sémantique** — Proximité de *sens* entre deux textes, mesurée via leurs embeddings. _(LLM)_
- **Sortie structurée (JSON)** — Forcer le modèle à répondre dans un format exploitable par un programme. _(LLM)_
- **Streaming** — Afficher la réponse au fur et à mesure de sa génération. _(LLM)_
- **Température** — Réglage de la créativité : 0 = stable/déterministe, élevé = créatif/aléatoire. _(LLM)_
- **TF-IDF** — Mesure de similarité fondée sur les mots (recherche « simple », sans embeddings). _(LLM)_
- **Token** — Un morceau de mot ; l'unité que lit et écrit un LLM. _(LLM, IA)_
- **Tokenizer** — L'outil qui découpe le texte en tokens. _(LLM)_
- **Transformer** — L'architecture (2017) derrière tous les LLM modernes. _(LLM, IA)_
- **Zero-shot** — Demander une tâche au modèle sans lui donner d'exemple. _(LLM)_

## Agents IA

- **Agent** — Un LLM qui *agit* : il utilise des outils et enchaîne des étapes. _(Agents, IA)_
- **Boucle agentique** — Le cycle raisonner → agir → observer → recommencer jusqu'au résultat. _(Agents)_
- **Description d'outil** — Le texte qui explique au modèle à quoi sert un outil ; à soigner comme un prompt. _(Agents)_
- **Exécution de code arbitraire (danger)** — Laisser un LLM exécuter du code librement : risque de sécurité majeur. _(Agents)_
- **Function calling (tool calling)** — La capacité du modèle à *demander* l'appel d'une fonction. _(Agents, IA)_
- **Garde-fous** — Limites protégeant un agent : plafond d'étapes, validation humaine, contrôle des coûts. _(Agents)_
- **LangChain** — Framework populaire pour construire des agents et des chaînes LLM. _(Agents)_
- **LlamaIndex** — Framework spécialisé dans le RAG. _(Agents)_
- **Mémoire courte** — L'historique de la conversation en cours. _(Agents)_
- **Mémoire longue** — Des faits stockés durablement et retrouvés via un outil de recherche. _(Agents)_
- **Multi-agents** — Plusieurs agents spécialisés se répartissant le travail. _(Agents)_
- **Observabilité** — Journaliser chaque étape de l'agent (outil, arguments, résultat) pour déboguer. _(Agents)_
- **Outil (tool)** — Une fonction (calculatrice, recherche, appel d'API…) que l'agent peut utiliser. _(Agents)_
- **ReAct (Reasoning + Acting)** — Schéma d'agent alternant raisonnement et actions. _(Agents)_
- **Validation humaine** — Demander confirmation avant une action sensible. _(Agents)_