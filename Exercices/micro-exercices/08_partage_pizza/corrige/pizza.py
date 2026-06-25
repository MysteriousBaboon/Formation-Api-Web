# ============================================================
# pizza.py — Partage de pizza (corrigé)
# ============================================================
# Le bug : l'ancienne version renvoyait [base] * personnes et
# OUBLIAIT le reste (parts % personnes) -> des parts disparaissaient.
# Correction : les `reste` premiers convives reçoivent une part de plus.
# ============================================================


def partager_pizza(parts, personnes):
    """Répartit `parts` parts entre `personnes` convives, équitablement.

    Renvoie une liste de longueur `personnes` dont la somme vaut exactement `parts`.
    """
    if personnes <= 0:
        raise ValueError("il faut au moins une personne")

    base = parts // personnes
    reste = parts % personnes
    # Les `reste` premiers convives reçoivent une part en plus.
    return [base + 1 if i < reste else base for i in range(personnes)]


if __name__ == "__main__":
    parts, personnes = 10, 3
    repartition = partager_pizza(parts, personnes)
    print(f"🍕 {parts} parts pour {personnes} convives -> {repartition}")
    print(f"   parts distribuées : {sum(repartition)} / {parts}")
