# ♿ Rends ce formulaire accessible (~1h) — *RGAA, pour de vrai*

> 🎓 **Compétence CDA visée : C2 — Développer des interfaces utilisateur (accessibilité RGAA)**
> Le jury demande : *« en quoi ton interface est-elle accessible ? »*. Répondre « j'ai mis des
> couleurs sympa » = rouge. Ici on part d'un formulaire **volontairement inaccessible** et on le
> **corrige**, point par point, avec une **checklist d'audit** à la clé.

---

## Le contexte

Toujours **Troc'Quartier**. On te livre le formulaire **« Proposer un objet »** (`starter/`).
Il *fonctionne*… mais il est **inutilisable** pour une personne malvoyante, ou qui navigue au
clavier, ou avec un lecteur d'écran. Et justement, la présidente de l'asso a 78 ans.

Lance-le et essaie de le remplir **sans la souris** (touche `Tab` uniquement) : tu vas vite voir
le problème.

```bash
cd starter
pip install flask
python app.py        # http://localhost:5013
```

---

## ⚠️ Les 6 péchés d'accessibilité à corriger

Le formulaire de `starter/` les cumule **exprès** :

| # | Problème | Pourquoi c'est bloquant |
|---|---|---|
| 1 | **Pas de `<label>`** (juste des `placeholder`) | Le lecteur d'écran ne sait pas à quoi sert le champ ; le placeholder disparaît à la saisie |
| 2 | **Champs non reliés** (`id`/`for` absents) | Cliquer le texte ne focalise pas le champ ; aide technique perdue |
| 3 | **Contraste insuffisant** (gris clair sur blanc) | Illisible pour une vue basse (RGAA exige un ratio ≥ 4.5:1) |
| 4 | **`<div onclick>` au lieu de `<button>`** | **Inatteignable au clavier** : pas de `Tab`, pas d'`Entrée` |
| 5 | **Image sans `alt`** | Le lecteur d'écran lit « image » ou le nom de fichier, sans le sens |
| 6 | **Erreurs signalées par la couleur seule** | Un daltonien ne « voit » pas l'erreur ; pas de message lisible |

(+ détails : pas de `lang`, champs requis non indiqués, pas de regroupement.)

---

## Ce que tu dois construire

Repars de `starter/templates/index.html` et **corrige les 6 points** :

1. Un **`<label for="...">`** relié à chaque champ (`id` correspondant).
2. Des **contrastes suffisants** (texte foncé sur fond clair).
3. Un vrai **`<button type="submit">`** (atteignable au clavier).
4. Un **`alt`** descriptif sur l'image (ou `alt=""` si purement décorative).
5. Les **erreurs en texte** explicite, annoncées (`role="alert"` / `aria-live`), pas juste en rouge.
6. `lang="fr"`, champs requis avec `required` + `aria-required`, regroupement `<fieldset>/<legend>`.

Puis remplis **`corrige/AUDIT_RGAA.md`** (une checklist d'audit) — c'est ce document que tu montres au jury.

> 💡 `corrige/` contient une version accessible complète — à ouvrir **après** avoir tenté.

---

## 💡 Conseils

- Le duo gagnant :
  ```html
  <label for="nom">Nom de l'objet</label>
  <input id="nom" name="nom" required aria-required="true">
  ```
- **Teste au clavier** : `Tab` doit atteindre **tous** les champs **et** le bouton, dans l'ordre logique.
- Contraste : évite `color:#bbb`. Vérifie avec l'outil « contrast » des DevTools ou WebAIM.
- Message d'erreur accessible :
  ```html
  <p role="alert">⚠️ L'email n'est pas valide.</p>
  ```
- Un `<button>` natif est **toujours** mieux qu'un `<div onclick>` : focusable, activable à l'`Entrée`/`Espace`.

---

## ✅ Critères de réussite

- [ ] **Chaque** champ a un `<label for>` relié (cliquer le libellé focalise le champ).
- [ ] Je peux **tout remplir et valider au clavier seul** (`Tab` + `Entrée`), sans souris.
- [ ] Les **contrastes** sont suffisants (plus de gris clair illisible).
- [ ] L'image a un **`alt`** pertinent.
- [ ] Les **erreurs** sont en **texte** + annoncées (`role="alert"`), pas seulement en couleur.
- [ ] `lang="fr"`, champs requis indiqués, regroupement `<fieldset>`.
- [ ] J'ai rempli **`AUDIT_RGAA.md`** et je sais expliquer **chaque** correction.

---

## ⭐ Bonus

1. **Focus visible** : un `:focus-visible` net (contour) pour suivre la navigation clavier.
2. **Skip link** « Aller au contenu » en haut de page.
3. **Validation côté serveur** *et* client : ne fais jamais confiance au seul navigateur (rejoint l'ANSSI).
4. Teste avec un **lecteur d'écran** (NVDA, VoiceOver, ou Orca sous Linux) et note ce que tu entends.
