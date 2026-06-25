# Audit d'accessibilité — formulaire « Proposer un objet »

> Checklist façon jury. Pour chaque critère : l'état **avant** (starter) → **après** (corrigé),
> et **comment** je le vérifie. C'est ce document que tu présentes pour répondre à
> *« en quoi ton interface est-elle accessible ? »*.

| # | Critère RGAA | Avant | Après | Comment je le vérifie |
|---|---|:--:|:--:|---|
| 1 | Chaque champ a un **`<label for>`** relié | ❌ | ✅ | Cliquer le libellé focalise le champ |
| 2 | Champs **identifiés** (`id` ↔ `for`) | ❌ | ✅ | Inspecteur : `for="nom"` ↔ `id="nom"` |
| 3 | **Contrastes** suffisants (≥ 4.5:1) | ❌ | ✅ | Outil contraste DevTools / WebAIM |
| 4 | Actions au **clavier** (vrai `<button>`) | ❌ | ✅ | `Tab` atteint le bouton, `Entrée` l'active |
| 5 | Images avec **`alt`** pertinent | ❌ | ✅ | Lecteur d'écran annonce « Logo Troc'Quartier » |
| 6 | **Erreurs** en texte + annoncées (`role="alert"`) | ❌ | ✅ | Message lisible, pas seulement une pastille rouge |
| 7 | **Langue** de page (`lang="fr"`) | ❌ | ✅ | `<html lang="fr">` |
| 8 | Champs **requis** indiqués (`required` + `aria-required`) | ❌ | ✅ | Mention « (obligatoire) » + attribut |
| 9 | **Regroupement** logique (`<fieldset>/<legend>`) | ❌ | ✅ | Le lecteur d'écran annonce le groupe |
| 10 | **Focus visible** (`:focus-visible`) | ❌ | ✅ (bonus) | Contour net en naviguant au `Tab` |

## Test clavier (le plus parlant à l'oral)

1. Je charge la page, je n'utilise **que** `Tab`.
2. L'ordre de focus suit l'ordre visuel : nom → catégorie → description → email → consentement → bouton.
3. Sur le bouton, `Entrée` envoie le formulaire.
4. En cas d'erreur, le message est **lu** (il a `role="alert"`) et le champ est marqué `aria-invalid`.

## Ce que je sais expliquer au jury

- **Pourquoi un `placeholder` ne remplace pas un `<label>`** : il disparaît à la saisie et n'est pas
  fiable pour les aides techniques.
- **Pourquoi un `<div onclick>` est exclu** : non focusable, non activable au clavier → l'utilisateur
  qui n'a pas de souris est bloqué.
- **Pourquoi je valide aussi côté serveur** (`app.py`) : l'accessibilité ne dispense pas de la sécurité ;
  on ne fait jamais confiance au seul navigateur (rejoint l'ANSSI et la C3).
