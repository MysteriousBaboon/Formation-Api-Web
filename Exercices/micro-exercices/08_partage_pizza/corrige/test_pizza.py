# ============================================================
# test_pizza.py — Tests de partager_pizza (corrigé)
# ============================================================
# Lancement :  pytest -v
# ============================================================

import pytest

from pizza import partager_pizza


def test_aucune_part_perdue():
    # La somme des parts distribuées doit valoir le total : c'est CE test
    # qui passait au rouge avec le code bugué (il renvoyait [3, 3, 3] = 9).
    assert sum(partager_pizza(10, 3)) == 10


def test_repartition_equitable():
    repartition = partager_pizza(10, 3)
    assert max(repartition) - min(repartition) <= 1


def test_cas_exact():
    assert partager_pizza(12, 4) == [3, 3, 3, 3]


def test_bon_nombre_de_convives():
    assert len(partager_pizza(7, 5)) == 5


def test_zero_personne_leve_erreur():
    with pytest.raises(ValueError):
        partager_pizza(8, 0)


@pytest.mark.parametrize("parts, personnes", [(10, 3), (7, 2), (100, 7), (1, 4), (50, 50)])
def test_somme_toujours_conservee(parts, personnes):
    assert sum(partager_pizza(parts, personnes)) == parts
