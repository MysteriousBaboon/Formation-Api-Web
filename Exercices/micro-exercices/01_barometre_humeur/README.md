# 🌡️ Baromètre d'humeur (~30 min) — *dictionnaires & affichage terminal*

> 🎓 **Compétence : Fondamentaux Python**
> Compter des occurrences avec un `dict`, parcourir des données et **fabriquer un
> affichage visuel** — la brique de base de tout tableau de bord.

---

## Le contexte

Chaque matin, ton équipe poste son humeur du jour dans un salon Slack. Tu récupères
la liste brute des votes et tu veux en faire un **baromètre visuel** directement dans
le terminal : un histogramme en barres colorées, comme un mini-dashboard.

```
🌡️  Baromètre d'humeur — 25 votes

🤩 au top      | ███████████ 8 (32%)
🙂 ça va       | ████████ 6 (24%)
😐 bof         | █████ 4 (16%)
😴 fatigué     | ████ 3 (12%)
😡 ras-le-bol  | █████ 4 (16%)

👉 Humeur dominante : 🤩 au top
```

---

## Ce que tu dois construire

À partir de `starter.py` (qui contient déjà la liste `votes`), écris un script qui :

1. **Compte** combien de fois chaque humeur apparaît, dans un dictionnaire `{humeur: nombre}`.
2. Calcule le **total** de votes et le **maximum** (l'humeur la plus votée).
3. Pour chaque humeur, affiche une **barre** dont la longueur est proportionnelle :
   `longueur = round(nombre / maximum * 30)` caractères `█`.
4. **Colore** chaque barre (codes ANSI fournis dans le starter).
5. Affiche à côté le **nombre** et le **pourcentage** du total.
6. Termine par l'**humeur dominante**.

---

## 💡 Conseils

- Compter sans rien importer :
  ```python
  compte = {}
  for v in votes:
      compte[v] = compte.get(v, 0) + 1
  ```
  *(ou découvre `collections.Counter` en bonus)*

- Une barre colorée = `COULEURS[humeur] + "█" * longueur + RESET`.
  Le `RESET` (`\033[0m`) est **obligatoire** sinon toute la suite reste colorée.

- Pour aligner les étiquettes : `f"{emoji} {humeur}".ljust(16)`.

- Trouver la clé au plus grand nombre : `max(compte, key=compte.get)`.

---

## ✅ Critères de réussite

- [ ] Le comptage est correct (la somme des nombres = nombre de votes).
- [ ] Les barres sont **proportionnelles** (la plus haute fait ~30 blocs).
- [ ] Les couleurs s'affichent **et** se coupent bien (pas de terminal tout rouge ensuite).
- [ ] Les pourcentages tombent juste.
- [ ] Tu sais expliquer pourquoi `dict.get(v, 0)` évite un plantage au premier vote.

---

## ⭐ Bonus

1. **Tri** : affiche les humeurs de la plus votée à la moins votée.
2. **Counter** : refais le comptage en une ligne avec `collections.Counter(votes)`.
3. **Saisie live** : demande les votes à l'utilisateur un par un (`input`) jusqu'à `"fin"`,
   puis dessine le baromètre.
