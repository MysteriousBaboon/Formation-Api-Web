# 🔐 Jauge de mot de passe (~40 min) — *fonctions, chaînes & sets*

> 🎓 **Compétence : Fondamentaux Python** (+ réflexe sécurité utile pour le CDA)
> Écrire une **fonction qui note une donnée** selon des règles, et la rendre visuelle.
> C'est exactement la mécanique d'un *scoring* (qu'on retrouve dans les exos Flask 04 et 05).

---

## Le contexte

Tu ajoutes à un formulaire d'inscription un petit **vérificateur de robustesse** de mot
de passe, comme ceux qui affichent une barre rouge → verte quand tu tapes. Ici, version
terminal :

```
'123'
  [██░░░░░░░░░░░░░░░░░░] 20/100  🔴 Faible
  💡 Ajoute : au moins 8 caractères, une minuscule, une majuscule, un symbole (!?@#...)

'Tr0ub4dour&Co'
  [████████████████████] 100/100  💪 Costaud
```

---

## Ce que tu dois construire

À partir de `starter.py`, écris :

1. Une fonction **`evaluer(mdp)`** qui renvoie un **score sur 100** selon ces règles :

   | Règle | Points |
   |-------|--------|
   | longueur ≥ 8 | +20 |
   | longueur ≥ 12 | +15 (en plus) |
   | contient une minuscule | +15 |
   | contient une majuscule | +15 |
   | contient un chiffre | +15 |
   | contient un symbole (`!?@#...`) | +20 |

   Elle renvoie aussi la **liste de ce qui manque** (pour conseiller l'utilisateur).

2. Une fonction **`verdict(score)`** qui traduit le score en libellé + couleur :
   `< 40` 🔴 Faible · `40–69` 🟠 Moyen · `70–89` 🟢 Bon · `≥ 90` 💪 Costaud.

3. Un affichage **jauge** : une barre de 20 caractères, remplie proportionnellement
   au score (`█` colorés) et complétée par des `░`, suivie du score et du verdict.

---

## 💡 Conseils

- Détecter les types de caractères sans rien importer :
  ```python
  any(c.islower() for c in mdp)   # au moins une minuscule ?
  any(c.isdigit() for c in mdp)   # au moins un chiffre ?
  ```
- Pour les symboles, sers-toi d'un **set** (rapide à interroger) :
  ```python
  import string
  symboles = set(string.punctuation)   # {'!', '@', '#', ...}
  any(c in symboles for c in mdp)
  ```
- Remplissage de la jauge : `rempli = round(score / 100 * 20)` puis
  `"█" * rempli + "░" * (20 - rempli)`.
- N'oublie pas le `RESET` (`\033[0m`) après la partie colorée.

---

## ✅ Critères de réussite

- [ ] `evaluer("123")` donne un petit score ; `evaluer("Tr0ub4dour&Co")` donne 100.
- [ ] La jauge est **proportionnelle** et change de **couleur** selon le verdict.
- [ ] La liste « ce qui manque » est juste et utile.
- [ ] `evaluer` est une **fonction pure** (mêmes entrées → même sortie, pas de `print` dedans).
- [ ] Tu sais expliquer pourquoi on **ne stocke jamais** un mot de passe en clair (culture sécu).

---

## ⭐ Bonus

1. **Mot de passe interdit** : si le mot de passe est dans une mini-liste noire
   (`["123456", "password", "azerty"]`), force le score à 0.
2. **Interactif** : lis le mot de passe avec `input()` et affiche la jauge en direct.
3. **Suggestion** : si le score est faible, propose une version renforcée
   (ajoute un chiffre, une majuscule, un symbole).
