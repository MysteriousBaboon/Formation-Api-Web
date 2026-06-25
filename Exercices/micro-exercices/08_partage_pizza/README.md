# 🍕 Partage de pizza — chasse au bug (~45 min) — *pytest*

> 🎓 **Compétence CDA visée : C9 — Plans de tests**
> Écrire des **tests automatisés** (`pytest`) qui **prouvent** un bug, puis le corriger.
> Le jury distingue « j'ai cliqué et ça avait l'air bon » de « j'ai une suite de tests verte ».

---

## Le contexte

Le développeur d'avant a écrit une fonction `partager_pizza(parts, personnes)` censée
répartir les parts d'une pizza **le plus équitablement possible** entre les convives.
Elle a l'air de marcher… mais il y a un **bug sournois**. Ton job : ne **pas** le corriger
au pif, mais écrire des **tests** qui le mettent en évidence, **puis** réparer.

Lance le module pour voir le problème de tes yeux :
```bash
python pizza.py
```
```
🍕 10 parts pour 3 convives -> [3, 3, 3]
   parts distribuées : 9 / 10      ← une part s'est volatilisée 👻
```

---

## Ce que tu dois faire

### 1. Écrire les tests — `test_pizza.py`
Crée un fichier `test_pizza.py` avec plusieurs fonctions `test_...` qui vérifient le
**comportement attendu** de `partager_pizza` :

- **Aucune part perdue** : `sum(partager_pizza(10, 3))` doit valoir **10**.
- **Répartition équitable** : l'écart entre celui qui a le plus et celui qui a le moins
  de parts est **au plus 1**.
- **Cas exact** : `partager_pizza(12, 4)` doit donner `[3, 3, 3, 3]`.
- **Bon nombre de convives** : la liste a une longueur égale à `personnes`.
- **Garde-fou** : `partager_pizza(8, 0)` doit lever une `ValueError`.

Lance :
```bash
pytest -v
```
👉 Au moins un test doit passer au **ROUGE** (c'est lui qui révèle le bug).

### 2. Corriger `pizza.py`
Modifie `partager_pizza` pour **distribuer le reste** (`parts % personnes`) : les premiers
convives reçoivent une part de plus. Relance `pytest` → **tout doit être au VERT**.

---

## 💡 Conseils

- Squelette d'un test :
  ```python
  from pizza import partager_pizza

  def test_aucune_part_perdue():
      assert sum(partager_pizza(10, 3)) == 10
  ```
- Tester qu'une erreur est levée :
  ```python
  import pytest
  def test_zero_personne():
      with pytest.raises(ValueError):
          partager_pizza(8, 0)
  ```
- Idée de correction : `base = parts // personnes`, `reste = parts % personnes`,
  puis donne `base + 1` aux `reste` premiers, `base` aux autres.

---

## ✅ Critères de réussite

- [ ] `test_pizza.py` contient **au moins 4** tests.
- [ ] Avant correction : `pytest` montre du **rouge** sur le bon test.
- [ ] Après correction : **tous les tests sont verts**.
- [ ] `sum(partager_pizza(p, n)) == p` pour **n'importe quels** `p`, `n` (> 0).
- [ ] Tu sais expliquer pourquoi un test qui passe au rouge **avant** la correction, c'est exactement ce qu'on veut.

---

## ⭐ Bonus

1. **Paramétrage** : avec `@pytest.mark.parametrize`, teste d'un coup `(10,3)`, `(7,2)`, `(100,7)`…
   en vérifiant à chaque fois que la somme est conservée.
2. **Équité stricte** : ajoute un test qui vérifie que les parts sont triées (les premiers
   servis ont autant ou plus que les suivants).
3. **Prix** : ajoute `prix_par_personne(total_euros, personnes)` (arrondi au centime) et teste-la.
