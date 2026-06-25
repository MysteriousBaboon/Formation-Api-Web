# 🏛️ Dessine l'architecture (~1h) — *penser en couches avant de brancher des outils*

> 🎓 **Compétence CDA visée : C6 — Définir l'architecture logicielle**
> Le jury veut t'entendre **séparer les couches** et **justifier** tes choix (dont la sécurité ANSSI).
> Le piège classique : confondre **l'outil** (n8n, Render…) et **la couche** (orchestration, données…).
> Ici tu dessines l'architecture de **Troc'Quartier** — sans coder.

---

## Le contexte

Reprenons **Troc'Quartier** (l'asso de prêt d'objets entre voisins, cf. exo 10). On a validé le besoin,
il faut maintenant décider **comment c'est branché** avant d'écrire du code. Stack envisagée :

- une **interface** (formulaire + liste d'objets), no-code ou HTML/CSS ;
- un **micro-service Flask** qui porte la logique (réserver = vérifier que l'objet est libre, etc.) ;
- une **base de données** (membres, objets, réservations) ;
- une **automatisation** qui envoie un mail au propriétaire quand une demande arrive.

Ton job : poser tout ça **en couches** et expliquer **pourquoi** la logique de réservation vit dans
le micro-service, et pas dans le formulaire.

---

## ⚠️ Le piège que cet exo t'apprend à éviter

> — « n8n, c'est quelle couche ? » — « euh, c'est n8n. » ❌

L'**outil** n'est pas la **couche**. Une couche est un **rôle** (présentation / orchestration /
métier / données) ; un outil **remplit** un rôle. Tu dois savoir dire : *« la couche métier,
c'est mon micro-service Flask ; je l'isole pour que la règle de réservation soit au même endroit,
testable, et pas dupliquée dans l'interface. »*

---

## Ce que tu dois produire

Remplis **`starter/architecture.md`** avec **3 livrables** :

1. **Un diagramme d'architecture multicouche** (Mermaid) : Présentation → Orchestration →
   Métier → Données, avec l'outil qui remplit chaque couche.
2. **Un diagramme de séquence** (Mermaid) d'un scénario clé : *« un voisin réserve un objet »*,
   de l'interface jusqu'à la base.
3. **Un tableau des choix justifiés** : pour chaque couche, *l'outil choisi* + *pourquoi* +
   *le point de sécurité (ANSSI)* associé.

> 💡 Le `corrige/` montre une version complète — à ouvrir **après** avoir tenté.

---

## 💡 Conseils

- Les **4 couches** à nommer : **Présentation** (ce que voit l'utilisateur), **Orchestration**
  (qui déclenche quoi : webhooks, mails), **Métier** (les règles : objet libre ?), **Données** (le stockage).
- Diagramme multicouche en Mermaid (`flowchart TB`), une couche par `subgraph` :
  ```mermaid
  flowchart TB
    subgraph Presentation
      UI[Interface voisins]
    end
    subgraph Metier
      API[Micro-service Flask]
    end
    UI --> API
  ```
- Séquence : `sequenceDiagram`, acteurs en haut, flèches `->>` (appel) et `-->>` (réponse).
- **Justifie l'isolement du métier** : testable, réutilisable, une seule source de vérité,
  on ne fait pas confiance à l'interface pour la sécurité (validation **côté serveur**).
- ANSSI à glisser : secrets hors du code, validation **serveur**, accès base **paramétré**, HTTPS.

---

## ✅ Critères de réussite

- [ ] Mon diagramme distingue **4 couches** nommées (présentation / orchestration / métier / données).
- [ ] Pour **chaque** couche, je nomme **l'outil** qui la remplit (et je ne confonds pas les deux).
- [ ] Mon **diagramme de séquence** « réserver un objet » se rend et va de l'UI à la base.
- [ ] Mon **tableau** justifie chaque choix **et** cite un point de sécurité par couche.
- [ ] Je sais répondre à : *« pourquoi la règle de réservation est dans le service, pas dans le formulaire ? »*

---

## ⭐ Bonus

1. Ajoute une **couche Intelligence** (un LLM qui résume l'état d'un objet) et place-la proprement.
2. Montre le **couplage faible** : si je remplace la base SQLite par PostgreSQL, **quelle couche bouge** ? (réponse : seulement la couche données).
3. Dessine le **chemin d'une donnée sensible** (le contact d'un membre) et où elle est protégée.
