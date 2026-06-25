# 🤓 Développeur d'Application POUR LES NULS

> Tu codes avec l'IA et le no-code, et on te demande quand même de décrocher un **titre de développeur**. Panique pas. Voici la version sans prise de tête, où chaque compétence commence par une **devinette de la vie de tous les jours** avant qu'on lâche le mot savant que le jury veut entendre.
>
> Ce guide est le **petit frère rigolo** de deux gros documents sérieux :
> - [VALIDATION_COMPETENCES_CDA.md](VALIDATION_COMPETENCES_CDA.md) → la liste exacte de ce qu'il faut prouver
> - [PROGRAMME_REVISION_CDA.md](PROGRAMME_REVISION_CDA.md) → comment réviser sans paniquer
>
> Ici, on déjargonne. Là-bas, tu auras les détails. **Titre visé :** Concepteur Développeur d'Applications (CDA), RNCP37873, niveau Bac+3/4, option IA & NoCode.

---

## 🥇 La SEULE règle à graver dans ton crâne

Le jury s'en fiche **complètement** que tu aies cliqué dans Bubble ou demandé à Claude d'écrire ton code.

**Ce qu'il note, c'est TA tête.** Est-ce que tu comprends ce que ta machine a fabriqué ? Est-ce que tu peux l'expliquer ? Est-ce que tu sais *pourquoi* tu as fait ça comme ça ?

> 🤔 **Petite devinette :** imagine que tu fasses construire ta maison par des ouvriers, et qu'à la fin l'architecte te demande « pourquoi la cuisine est ici et pas là ? ». Si ta seule réponse c'est « bah, c'est les ouvriers qui ont fait »… tu as l'air de quoi ?
>
> 💡 **Réponse :** d'un touriste dans ta propre maison. Le jury ne veut pas un touriste. Il veut le **chef de chantier** qui sait expliquer chaque mur. Toi, tu es le chef d'orchestre de l'IA, pas un simple utilisateur.

**Conséquence n°1 :** « c'est l'IA qui l'a fait » = réponse interdite. Tu dois savoir dérouler ton projet ligne par ligne, écran par écran, **sans tes notes**.

**Conséquence n°2 :** deux compétences (la **n°3** et la **n°8**, on les marque 🟥) exigent du **vrai code que tu comprends**. Sur celles-là, le 100 % no-code est un piège mortel. C'est exactement pour ça que ta formation t'a fait toucher du Python/Flask : pour te **protéger** sur ces deux-là.

---

## 🧱 C'est quoi ces « 3 blocs » dont tout le monde parle ?

Le titre est découpé en 3 paquets de compétences. Traduction en humain :

| Bloc | Le nom officiel (qui fait peur) | Ce que ça veut VRAIMENT dire |
|---|---|---|
| 🟦 **BC01** | Développer une application sécurisée | « Installe ton atelier proprement et fabrique des briques solides » |
| 🟩 **BC02** | Concevoir et développer une application en couches | « Réfléchis AVANT de construire, et range tes données comme il faut » |
| 🟨 **BC03** | Préparer le déploiement d'une application sécurisée | « Mets en ligne sans tout faire péter » |

Et dedans, **11 compétences** en tout. Les voici en une phrase chacune, on les détaille juste après :

| # | En version « pour les nuls » | 🟥 Code obligatoire ? |
|---|---|---|
| C1 | Monter son atelier de travail | — |
| C2 | Fabriquer les écrans que les gens utilisent | un peu |
| C3 | Fabriquer le « cerveau » qui calcule | 🟥 **OUI** |
| C4 | Bosser en équipe sans bordel | — |
| C5 | Comprendre le besoin et dessiner avant de construire | — |
| C6 | Faire le plan de la maison | — |
| C7 | Ranger les données dans de bons tiroirs | un peu |
| C8 | Aller chercher / ranger les données sans se faire pirater | 🟥 **OUI** |
| C9 | Vérifier que ça marche vraiment | un peu |
| C10 | Écrire la notice pour mettre en ligne | — |
| C11 | Automatiser la mise en ligne (DevOps) | un peu |

> 🧵 **Le fil rouge de tout le guide : « LeadScore ».** Imagine une petite boîte qui reçoit plein de prospects (des gens potentiellement intéressés) et qui veut les **trier automatiquement** pour rappeler en priorité les plus chauds. On va illustrer **chaque** compétence avec ce projet. C'est ton exemple béton.

---

# 🟦 BC01 — « Monte ton atelier et fabrique des briques solides »

## C1 — Monter son atelier de travail

> 🤔 **La devinette :** un grand chef cuisinier débarque dans une cuisine inconnue. Avant même de toucher un œuf, qu'est-ce qu'il fait ?
>
> 💡 **Réponse :** il range ses couteaux, allume ses feux, vérifie qu'il a les bons ingrédients, et planque la recette secrète de mamie là où personne ne la trouve. **Bah un dev, c'est pareil** : avant de coder, il installe ses outils, isole son projet, et cache ses mots de passe.

🔁 **En vrai dans ton projet :** tu installes ton éditeur (Cursor/VS Code) + Python, tu crées une **bulle isolée** pour ton projet (le `.venv`, pour ne pas tout mélanger), tu notes la liste de tes ingrédients dans un fichier (`requirements.txt`), et tu ranges **toutes tes clés secrètes** (mots de passe, clés API) dans un fichier `.env` que tu **ne montres à personne**.

📎 **Pour valider, tu dois pouvoir montrer :**
- une capture de ton éditeur configuré ;
- ton fichier `requirements.txt` (la liste des ingrédients) ;
- ton fichier `.gitignore` qui dit « surtout ne publie JAMAIS le `.env` » ;
- un `.env.example` (la recette avec les cases vides, pour qu'un collègue sache quoi remplir sans voir tes vrais secrets) ;
- un petit mode d'emploi « Installation » dans le README.

🗣️ **Les mots magiques à lâcher au jury :** environnement virtuel (`.venv`), dépendances, gestionnaire de paquets (`pip`), variable d'environnement, clé API, dépôt Git.

⚠️ **Le piège où tout le monde tombe :** publier un mot de passe en ligne par accident. Si tu montres ton `.gitignore` et ton `.env.example`, tu prouves que tu as le **réflexe du pro**. Énorme bon point.

---

## C2 — Fabriquer les écrans que les gens utilisent

> 🤔 **La devinette :** tu construis un distributeur de billets. Il est super joli. Mais il n'a pas de braille, le bouton « valider » est invisible au soleil, et si tu tapes « patate » comme montant, il plante. C'est un bon distributeur ?
>
> 💡 **Réponse :** non. Un bon écran n'est pas juste *beau*, il est **utilisable par tout le monde** (même les personnes handicapées), il marche sur téléphone, et il **refuse poliment** les bêtises qu'on tape dedans.

🔁 **En vrai dans ton projet :** le **formulaire** où un prospect laisse ses infos, et le **tableau de bord** où la boîte suit ses leads. Que tu le fasses en no-code (Lovable/Bubble) ou en HTML généré par IA, il faut : des champs obligatoires, des messages d'erreur clairs, un affichage qui s'adapte au mobile, et des contrastes/libellés corrects pour l'accessibilité.

📎 **Pour valider, tu dois pouvoir montrer :**
- le « avant/après » : ton dessin (maquette) → l'écran réel ;
- des captures sur ordi **et** sur téléphone ;
- le lien vers la version en ligne ;
- une petite note sur tes choix d'accessibilité (ce que tu as fait pour les daltoniens, la navigation au clavier, etc.).

🗣️ **Les mots magiques à lâcher au jury :** responsive (= s'adapte à l'écran), composant d'interface, validation des saisies, ergonomie, **RGAA** (= les règles d'accessibilité), parcours utilisateur.

⚠️ **Le piège où tout le monde tombe :** dire « c'est joli » et s'arrêter là. Le jury veut que tu saches expliquer que le no-code **génère du HTML/CSS/JS** sous le capot, et que tu **prouves** l'accessibilité pour de vrai (navigation au clavier, textes alternatifs sur les images).

---

## C3 — Fabriquer le « cerveau » qui calcule 🟥 *(VRAI CODE OBLIGATOIRE)*

> 🤔 **La devinette :** dans un restaurant, qui décide si un client VIP passe devant tout le monde ? Ce n'est pas le menu (l'écran), ni le frigo (les données). C'est quelqu'un qui **réfléchit selon des règles**. Qui ?
>
> 💡 **Réponse :** le maître d'hôtel. C'est lui le **cerveau** : il applique la logique « ce client a réservé + il est fidèle → table en priorité ». Dans ton appli, ce cerveau, c'est ta **logique métier** — la partie qui calcule, décide, et trie.

🔁 **En vrai dans ton projet :** c'est le petit moteur (un **micro-service Flask**) qui reçoit un lead, lui **donne une note** (gros budget ? email pro ?), demande à une **IA (LLM)** de le résumer, **vérifie que les infos reçues sont valides**, **bloque les intrus** avec un mot de passe (token), et répond avec les bons **codes** (200 = ok, 400 = tu m'as envoyé n'importe quoi, 401 = t'as pas le droit, 500 = je me suis planté).

📎 **Pour valider, tu dois pouvoir montrer :**
- des extraits de **code commenté** que tu sais réexpliquer ;
- ta règle de notation (comment tu décides du score) ;
- la vérification des données entrantes ;
- la gestion des erreurs et la protection par mot de passe.

🗣️ **Les mots magiques à lâcher au jury :** composant métier, validation des entrées, authentification (token Bearer), codes HTTP, injection.

⚠️ **Le piège où tout le monde tombe (LE gros piège n°1) :** si c'est Claude/Cursor qui a écrit le code, tu dois pouvoir **réexpliquer chaque morceau** et répondre à « pourquoi cette ligne ? ». Entraîne-toi à dérouler ton fichier principal **sans tes notes**. Ici, le pur no-code te laisse à poil — d'où le code.

---

## C4 — Bosser en équipe sans bordel

> 🤔 **La devinette :** deux scénarios. (A) Tu écris ton roman d'un seul jet, tu le rends, et s'il y a un problème… tant pis. (B) Tu sauvegardes ton brouillon tous les soirs, avec une note « ajout du chapitre 3 ». Lequel rassure ton éditeur ?
>
> 💡 **Réponse :** le (B), évidemment. On voit ta **progression**, on peut **revenir en arrière**, on comprend ce que tu as fait et quand. C'est exactement ce qu'on attend d'un dev : travailler **par petites étapes traçables**.

🔁 **En vrai dans ton projet :** un **tableau de tâches** (Trello/Notion/Jira) avec des objectifs écrits du point de vue de l'utilisateur (user stories), des **sauvegardes régulières** de ton code (commits Git), des **branches** par fonctionnalité, et des points réguliers avec ton « client » (ton tuteur/formateur).

📎 **Pour valider, tu dois pouvoir montrer :**
- des captures de ton tableau de tâches ;
- ton historique de sauvegardes (`git log`) bien fourni ;
- quelques exemples de user stories ;
- ton planning de sprints.

🗣️ **Les mots magiques à lâcher au jury :** agile/Scrum, sprint, backlog, user story, versionnement, branche, *pull request*.

⚠️ **Le piège où tout le monde tombe :** un historique avec **un seul gros commit final** « voilà le projet ». Ça crie « j'ai tout fait la veille ». Des sauvegardes **petites et régulières** = preuve que tu as une vraie démarche.

---

# 🟩 BC02 — « Réfléchis avant de construire, et range bien tes données »

## C5 — Comprendre le besoin et dessiner avant de construire

> 🤔 **La devinette :** un client te dit « je veux un truc pour gérer mes clients ». Tu fonces acheter le matériel tout de suite, ou tu poses d'abord des questions et tu fais un croquis sur une nappe ?
>
> 💡 **Réponse :** tu poses des questions et tu **croques d'abord**. Sinon tu construis un truc magnifique… dont personne ne voulait. Comprendre le **besoin** puis le **dessiner** AVANT de coder, c'est la moitié du métier.

🔁 **En vrai dans ton projet :** tu fais un entretien (même fictif) avec la boîte → tu écris le besoin (« trier 200 leads/mois sans embaucher »), tu listes des user stories, tu fais un **schéma des cas d'usage** (qui fait quoi avec l'appli), puis des **maquettes** (Figma ou générées par IA) avec l'enchaînement des écrans.

📎 **Pour valider, tu dois pouvoir montrer :**
- un mini cahier des charges ;
- tes user stories ;
- un diagramme de cas d'usage ;
- tes maquettes + l'arborescence des écrans.

🗣️ **Les mots magiques à lâcher au jury :** besoin fonctionnel / non-fonctionnel, cas d'utilisation, *wireframe* (maquette fil de fer), parcours utilisateur.

⚠️ **Le piège où tout le monde tombe :** sauter cette étape pour foncer dans l'outil. Le jury **adore** l'ordre : **besoin → maquette → solution**. Montre-le dans cet ordre et tu marques des points gratuits.

---

## C6 — Faire le plan de la maison

> 🤔 **La devinette :** dans une maison, est-ce que tu mets la plomberie, l'électricité, la cuisine et le salon **dans la même pièce, tous mélangés** ? Ou est-ce que chaque chose a son rôle et sa place ?
>
> 💡 **Réponse :** chaque chose à sa place. En informatique pareil : on **sépare** ce qui s'affiche (la déco), ce qui calcule (le cerveau), et ce qui stocke (les placards). Ça s'appelle l'**architecture en couches**, et savoir faire ce plan, c'est cette compétence.

🔁 **En vrai dans ton projet :** un schéma clair `Écran no-code → n8n (le facteur qui transporte) → cerveau Flask → base de données Supabase`, plus un petit film en images d'« un lead qui arrive → est noté → est rangé → s'affiche ». Et tu justifies pourquoi le cerveau est **isolé** dans son coin.

📎 **Pour valider, tu dois pouvoir montrer :**
- un schéma d'architecture en couches ;
- un diagramme de séquence (le « film » étape par étape) ;
- un tableau de tes choix techniques, justifiés.

🗣️ **Les mots magiques à lâcher au jury :** architecture multicouche / 3-tiers, séparation des responsabilités, couplage faible, recommandations **ANSSI** (= les règles de sécurité officielles).

⚠️ **Le piège où tout le monde tombe :** confondre l'**outil** et le **rôle**. n8n est un outil ; son **rôle** c'est l'orchestration (transporter/déclencher), pas le calcul. Sache nommer **qui joue quel rôle**.

---

## C7 — Ranger les données dans de bons tiroirs

> 🤔 **La devinette :** tu gères une bibliothèque. Tu balances tous les bouquins en tas par terre, ou tu fais des étagères « Livres », « Auteurs », et un fil qui relie chaque livre à son auteur ?
>
> 💡 **Réponse :** des étagères bien reliées. Sinon, retrouver « tous les livres de cet auteur » devient un cauchemar. **Bien ranger ses données dans des tiroirs reliés entre eux**, c'est ça, concevoir une base de données.

🔁 **En vrai dans ton projet :** des tables `leads`, `utilisateurs`, `scores` dans Supabase. Tu fais un **plan des tiroirs** (un MCD/MLD), tu poses des **identifiants uniques** (clés), et tu crées un **lien** du genre « un commercial → plusieurs leads » (une relation 1-N).

📎 **Pour valider, tu dois pouvoir montrer :**
- ton plan des tables (MCD/MLD) ;
- le schéma de tes tables + captures Supabase ;
- le script qui crée les tables.

🗣️ **Les mots magiques à lâcher au jury :** modèle relationnel, MCD/MLD, clé primaire / clé étrangère, relation 1-N, normalisation, intégrité référentielle.

⚠️ **Le piège où tout le monde tombe :** « j'ai juste créé des colonnes dans Airtable ». Un tableur, ce n'est **pas** une base de données réfléchie. Montre une **vraie modélisation** avec des liens entre les tiroirs.

---

## C8 — Aller chercher / ranger les données sans se faire pirater 🟥 *(VRAI CODE OBLIGATOIRE)*

> 🤔 **La devinette :** tu es gardien d'un coffre-fort. Quelqu'un arrive et dit « donne-moi le contenu du coffre n°4… ET pendant que tu y es, ouvre tous les autres et vide-les ». Tu fais quoi ?
>
> 💡 **Réponse :** tu prends sa demande **au pied de la lettre, sans l'exécuter aveuglément**. Tu traites « n°4 » comme un *numéro*, pas comme un ordre. Sinon n'importe quel malin te vide la banque. En code, ça veut dire écrire des **requêtes paramétrées** pour ne **jamais** se faire avoir par une phrase piégée (une « injection »).

🔁 **En vrai dans ton projet :** depuis ton cerveau, tu écris les ordres pour **lire, ajouter, modifier, supprimer** (CRUD) des leads dans Supabase, **toujours en mode sécurisé**. Et tu montres aussi un usage **NoSQL** : par exemple ranger la réponse de l'IA en **JSON** (un format souple, comme une fiche libre plutôt qu'un tableau rigide).

📎 **Pour valider, tu dois pouvoir montrer :**
- des extraits de requêtes (lire/ajouter/modifier/supprimer) ;
- ton code d'accès aux données ;
- **un exemple de stockage NoSQL** (du JSON), parce que la compétence l'exige **explicitement**.

🗣️ **Les mots magiques à lâcher au jury :** CRUD, requête paramétrée, injection SQL, ORM, SQL **vs** NoSQL, transaction.

⚠️ **Le piège où tout le monde tombe (LE gros piège n°2) :** (1) **oublier le NoSQL** — il est obligatoire, pas optionnel ; (2) **coller bout à bout** du texte dans une requête (= la porte grande ouverte aux pirates). Requête paramétrée **toujours**, jamais de collage de chaînes.

---

# 🟨 BC03 — « Mets en ligne sans tout faire péter »

## C9 — Vérifier que ça marche vraiment

> 🤔 **La devinette :** tu fabriques des parachutes. Tu les vends en disant « je l'ai plié, ça a l'air bien » ? Ou tu as une **liste de tests** que chaque parachute doit passer avant de partir ?
>
> 💡 **Réponse :** une liste de tests, par pitié. « Ça a l'air bien » ne suffit pas quand ça compte. Tester, c'est **prévoir les cas** (même les foireux) et **vérifier** que l'appli réagit comme prévu — idéalement avec des tests qui se lancent tout seuls.

🔁 **En vrai dans ton projet :** un **tableau de tests** (cas testé / ce que j'envoie / résultat attendu / résultat obtenu / OK ou pas), des tests manuels du formulaire, **et** des tests automatiques (`pytest`) sur ton cerveau : mot de passe bon/mauvais, données invalides (erreur 400), page de santé `/health`.

📎 **Pour valider, tu dois pouvoir montrer :**
- ton tableau de plan de tests ;
- ton fichier de tests automatiques ;
- des captures des résultats (vert = ça passe, rouge = ça casse) ;
- des cas de **non-régression** (vérifier qu'une nouveauté n'a rien cassé d'ancien).

🗣️ **Les mots magiques à lâcher au jury :** test unitaire / d'intégration / fonctionnel, jeu d'essai, cas de test, non-régression, couverture.

⚠️ **Le piège où tout le monde tombe :** « j'ai cliqué partout, ça marche ». Un **tableau de cas** + quelques tests automatiques font **toute** la différence aux yeux du jury.

---

## C10 — Écrire la notice pour mettre en ligne

> 🤔 **La devinette :** tu montes un meuble IKEA génial. Tu es super fier. Mais ta notice, c'est trois gribouillis que toi seul comprends. Un inconnu peut-il remonter le meuble ?
>
> 💡 **Réponse :** non. Et c'est ça le test. Une **bonne doc de déploiement**, c'est une notice tellement claire qu'**un parfait inconnu** pourrait remettre ton appli en ligne sans t'appeler.

🔁 **En vrai dans ton projet :** une procédure **pas à pas** pour mettre LeadScore en ligne : les prérequis, les variables secrètes à mettre, comment construire et lancer. (C'est exactement ce que fait déjà `cours_microservice/deploiement_render.md`.)

📎 **Pour valider, tu dois pouvoir montrer :**
- ta doc de déploiement complète ;
- un README clair ;
- une **checklist avant la mise en ligne** ;
- un schéma de ton environnement de production.

🗣️ **Les mots magiques à lâcher au jury :** environnements dev / staging / prod, build, documentation technique, *rollback* (= revenir à la version d'avant).

⚠️ **Le piège où tout le monde tombe :** une doc écrite « pour toi tout seul », avec des étapes dans ta tête mais pas sur le papier. Écris-la **pour un inconnu** : c'est littéralement le critère de réussite.

---

## C11 — Automatiser la mise en ligne (la fameuse « démarche DevOps »)

> 🤔 **La devinette :** imagine que tu veuilles te mettre **au chômage** en faisant le **moins de choses possible** à chaque mise à jour de ton appli. Tu mettrais quoi en place ?
>
> 💡 **Réponse :** (1) des **tests qui se lancent tout seuls** pour être sûr que ta nouveauté ne casse rien, et (2) une **mise en ligne automatique** pour ne plus jamais le refaire à la main. Les deux ensemble = **CI/CD**, le cœur de la « démarche DevOps ». Tu pousses ton code, et la machine fait le reste : elle teste, et si c'est vert, elle déploie.

🔁 **En vrai dans ton projet :** `git push` → les tests se lancent automatiquement (GitHub Actions = la **CI**) → si tout est vert, Render redéploie tout seul (= la **CD**) → tu surveilles les **logs** sur le tableau de bord.

📎 **Pour valider, tu dois pouvoir montrer :**
- ton fichier de pipeline (`.github/workflows/tests.yml`) ;
- ta config d'infra (ex. `render.yaml`) ;
- des captures du pipeline qui tourne et des logs ;
- un schéma du flux CI/CD.

🗣️ **Les mots magiques à lâcher au jury :** CI/CD, pipeline, **intégration continue** (les tests auto) **vs déploiement continu** (la mise en ligne auto), IaC (infra décrite dans un fichier), monitoring, DevOps.

⚠️ **Le piège où tout le monde tombe (LE piège du module) :** Render tout seul ne fait que **la moitié** du boulot — la mise en ligne. Sans la brique **tests automatiques (CI)**, ce n'est **pas** du DevOps, c'est juste du déploiement. Le maillon « qualité » manque. Ajoute la CI, sinon le jury te le sort.

---

# 🔒 Les trucs que le jury attend PARTOUT (pas dans une seule case)

Ces exigences ne sont pas une compétence isolée : elles doivent **se voir un peu partout** dans ton dossier.

> 🤔 **Sécurité (ANSSI)** — *Tu laisserais les clés de ta maison sous le paillasson avec ton nom dessus ?* Non. Donc : secrets cachés (jamais dans le code), porte fermée à clé (authentification), videur à l'entrée (validation des saisies), et adresse sécurisée (HTTPS).

> 🤔 **RGPD** — *Si quelqu'un te donne son numéro, tu as le droit de le revendre à la terre entière ?* Non. Donc : mentions légales, **consentement** sur le formulaire, et tu ne collectes que le strict nécessaire.

> 🤔 **Accessibilité (RGAA)** — *On construit une mairie sans rampe pour les fauteuils roulants ?* Plus maintenant. Pareil pour un site : l'accessibilité se pense **dès les maquettes**, pas après coup.

> 🤔 **Anglais B1** — *La notice de ton outil est en anglais et tu la fermes en panique ?* Non, tu dois savoir **lire une doc technique en anglais** et répondre court à l'écrit. (Astuce : lis une doc en anglais par jour et résume-la en 3 phrases.)

> 🤔 **Veille** — *Tu utilises un GPS dont la carte date de 1995 ?* Non. Montre que tu restes à jour : prépare **2-3 sources** que tu suis (sécurité + outils IA) à citer au jury.

---

# 🟥 Les 2 pièges MORTELS à ne jamais oublier

Sur **9 compétences sur 11**, le no-code et l'IA peuvent te porter. Mais sur **2 d'entre elles, il faut du vrai code que TU comprends** :

- **C3 — le cerveau qui calcule** : tu dois dérouler ton fichier principal ligne à ligne.
- **C8 — l'accès aux données** : tu dois montrer des requêtes sécurisées (et du NoSQL).

> 💡 Si tu ne devais réviser que **deux** choses à fond, ce serait celles-là. Le jury **sait** que c'est là que les profils IA/no-code se cassent les dents, donc il va creuser. Pas d'impasse possible.

---

# ✅ Check-list « mon dossier est prêt » (à cocher la veille)

- [ ] Un seul projet fil rouge qui traverse **les 3 blocs** (genre LeadScore).
- [ ] Du **code que je sais réexpliquer** pour C3 et C8.
- [ ] Une **base de données vraiment modélisée** (un plan, pas un tableur) + un usage **NoSQL**.
- [ ] Un **plan de tests** + quelques tests **automatiques** au vert.
- [ ] Une **notice de déploiement** qu'un inconnu pourrait suivre.
- [ ] Un **pipeline CI/CD** (pas juste « git push → Render »).
- [ ] **Sécurité, RGPD, accessibilité** visibles dans le dossier.
- [ ] Je sais **lire une doc technique en anglais**.
- [ ] Mon **historique de sauvegardes** raconte ma progression (commits réguliers).
- [ ] Je peux **dérouler chaque écran et chaque fichier SANS mes notes**.

---

# 🗣️ Le top des questions-pièges (et la réponse courte qui sauve)

| Le jury demande… | Tu réponds (court et net) |
|---|---|
| « Pourquoi cette ligne dans ton code ? » | Tu expliques ce qu'elle fait **et** ce qui casse si on l'enlève. |
| « Que renvoie ton appli si le mot de passe est faux ? » | **401** (pas le droit d'entrer). |
| « C'est quoi la différence intégration continue / déploiement continu ? » | CI = les tests se lancent auto à chaque envoi ; CD = la mise en ligne se fait auto si c'est vert. |
| « Pourquoi du SQL **et** du NoSQL ? » | SQL pour les données bien rangées et reliées ; NoSQL pour le souple (les fiches libres, le JSON de l'IA). |
| « C'est quoi une relation 1-N chez toi ? » | Un commercial → plusieurs leads (le lien est posé côté `leads`). |
| « Comment tu évites une injection ? » | Requête paramétrée, **jamais** de texte collé bout à bout. |
| « n8n, il joue quel rôle ? » | L'orchestration (le facteur qui transporte/déclenche), **pas** le calcul. |
| « Si je supprime ta validation des saisies, il se passe quoi ? » | N'importe quelle saisie pourrie entre → bugs et failles. C'est mon videur à l'entrée. |
| « Render tout seul, c'est du DevOps ? » | Non, juste la mise en ligne (CD). Il manque les tests auto (CI) pour parler DevOps. |
| « Où sont tes secrets ? » | Dans le `.env`, exclu par `.gitignore`, avec un `.env.example` pour les collègues. |

> 🧯 **Technique anti-panique :** tu ne sais pas répondre ? **Ne dis jamais « c'est l'IA qui a fait »**. Reformule la question, explique ta démarche, dis ce que tu irais vérifier. Le jury préfère un candidat qui réfléchit à voix haute qu'un candidat qui se cache derrière son outil.

---

## 📚 Pour aller plus loin (la version « adulte » sans les blagues)

- **[VALIDATION_COMPETENCES_CDA.md](VALIDATION_COMPETENCES_CDA.md)** — chaque compétence, ses preuves exactes et son vocabulaire jury.
- **[PROGRAMME_REVISION_CDA.md](PROGRAMME_REVISION_CDA.md)** — le planning de révision sur 4 semaines, l'oral chronométré et toutes les questions-pièges.
- **[GLOSSAIRE.md](GLOSSAIRE.md)** — tous les mots savants, traduits.

*Rappel final : le jury ne note pas l'outil, il note **ta tête**. Réviser = faire tourner ton projet et savoir le raconter, pas juste le relire. 🚀*
