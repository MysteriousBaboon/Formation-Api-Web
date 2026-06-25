# ============================================================
# pizza.py — à débugger (le code du collègue précédent)
# ============================================================
# Lancement :  python pizza.py
# ============================================================


def partager_pizza(parts, personnes):
    """Répartit `parts` parts de pizza entre `personnes` convives,
    le plus équitablement possible.

    Renvoie une liste de longueur `personnes` : le nombre de parts de chacun.
    """
    if personnes <= 0:
        raise ValueError("il faut au moins une personne")

    base = parts // personnes
    return [base] * personnes   # ← est-ce vraiment équitable... et complet ?


if __name__ == "__main__":
    parts, personnes = 10, 3
    repartition = partager_pizza(parts, personnes)
    print(f"🍕 {parts} parts pour {personnes} convives -> {repartition}")
    print(f"   parts distribuées : {sum(repartition)} / {parts}")
