# 🗺️ Du brief au wireframe (~1h15) — *analyser un besoin avant de coder*

> 🎓 **Compétence CDA visée : C5 — Analyser les besoins et maquetter**
> Le jury adore l'ordre **besoin → maquette → solution**. Foncer sur l'outil sans avoir
> écrit le besoin, c'est rouge. Ici tu t'entraînes à **transformer une phrase de client
> en spécifications + maquette** — sans écrire une ligne de Python.

---

## Le contexte

**Troc'Quartier**, une petite asso de quartier, te contacte. La présidente t'explique en
deux phrases, autour d'un café :

> « Les voisins ont plein de trucs qui dorment dans leurs placards — une perceuse, une tente,
> un appareil à raclette… On voudrait un site où chacun **propose** ses objets à prêter, et où
> les autres peuvent **réserver** ce qui est libre. Faut que ce soit **simple**, même pour ma
> mère de 78 ans, et que ça marche **sur téléphone**. »

C'est tout ce que tu as. Ton job : en faire un **mini cahier des charges** + une **maquette**
que tu pourrais présenter au jury en disant « voilà ce que j'ai compris, voilà ce que je construis ».

---

## ⚠️ Le piège que cet exo t'apprend à éviter

Le réflexe débutant : ouvrir Lovable/Flask et coder direct. Au jury, ça donne :

> — « Quel besoin résous-tu ? » — « Ben… un site de prêt. » ❌

Un·e pro **cadre d'abord** : qui s'en sert, pour faire quoi, avec quelles contraintes, et à quoi
ça ressemble. **Le code vient après.** Cet exo, c'est l'étape d'avant.

---

## Ce que tu dois produire

Remplis le fichier **`starter/reponse.md`** (un gabarit t'attend) avec **5 livrables** :

1. **Le besoin reformulé** — 3-4 phrases : le problème, pour qui, le bénéfice attendu.
2. **Besoins fonctionnels / non-fonctionnels** — deux listes séparées
   (fonctionnel = *ce que ça fait* ; non-fonctionnel = *contraintes* : mobile, simple, sécurité…).
3. **3 user stories** au format `En tant que <rôle>, je veux <action>, afin de <bénéfice>`.
4. **Un diagramme de cas d'usage** en **Mermaid** (acteurs → actions).
5. **Un wireframe** de l'écran principal — un **croquis** (ASCII, ou photo d'un dessin papier),
   pas un design fini : on veut la **disposition**, pas les couleurs.

> 💡 Le `corrige/` contient une version complète — à ouvrir **après** avoir tenté.

---

## 💡 Conseils

- **Fonctionnel vs non-fonctionnel** : « réserver un objet » = fonctionnel ;
  « marche sur téléphone », « utilisable par une personne âgée » = non-fonctionnel.
- Le **non-fonctionnel** est là où tu glisses le transversal CDA : **RGAA** (accessible mamie 78 ans),
  responsive (mobile), **RGPD** (on stocke un nom/contact → consentement, données minimisées).
- Cas d'usage en Mermaid, squelette :
  ```mermaid
  flowchart LR
    Voisin((Voisin)) --> A[Proposer un objet]
    Voisin --> B[Réserver un objet]
  ```
- Wireframe ASCII : des `┌─┐`, `[ Bouton ]`, `[____]` pour les champs. Vite fait, lisible.
- Pense **parcours** : quel écran d'abord, on clique où, on arrive où.

---

## ✅ Critères de réussite

- [ ] Le **besoin** est reformulé avec mes mots (pas un copier-coller du client).
- [ ] J'ai **séparé** fonctionnel et non-fonctionnel (au moins 3 de chaque).
- [ ] Mes 3 **user stories** respectent le format *rôle / action / bénéfice*.
- [ ] Mon **diagramme de cas d'usage** Mermaid se **rend** (acteurs + actions visibles).
- [ ] J'ai **un wireframe** de l'écran principal avec ses zones (titre, liste, action).
- [ ] Je peux **présenter tout ça à l'oral** dans l'ordre besoin → maquette.

---

## ⭐ Bonus

1. **Diagramme de séquence** : « un voisin réserve un objet » (c'est l'amorce de la C6).
2. **Arborescence des écrans** : accueil → fiche objet → confirmation (un mini plan du site).
3. **Critères d'acceptation** sur une user story (« étant donné…, quand…, alors… »).
