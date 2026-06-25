# ============================================================
# starter.py — Jauge de mot de passe (à compléter)
# ============================================================
# Lancement :  python starter.py
# ============================================================

import string

RESET = "\033[0m"
A_TESTER = ["123", "motdepasse", "Soleil2026", "Tr0ub4dour&Co"]


def evaluer(mdp):
    """Renvoie {'score': int, 'manques': list[str]} pour un mot de passe."""
    score = 0
    manques = []

    # TODO : longueur (>= 8 : +20 ; >= 12 : +15 de plus)
    # TODO : minuscule (+15), majuscule (+15), chiffre (+15)
    # TODO : symbole via set(string.punctuation) (+20)
    # TODO : remplir `manques` avec ce qui fait défaut

    return {"score": score, "manques": manques}


def verdict(score):
    """Renvoie (libellé, code_couleur_ansi, emoji) selon le score."""
    # TODO : < 40 Faible rouge 🔴 | 40-69 Moyen jaune 🟠 | 70-89 Bon vert 🟢 | >=90 Costaud 💪
    return ("?", RESET, "❓")


def afficher_jauge(mdp):
    """Affiche le mot de passe, sa jauge colorée et ce qui manque."""
    # TODO : appeler evaluer + verdict, construire la barre de 20 caractères, afficher
    pass


if __name__ == "__main__":
    for mdp in A_TESTER:
        afficher_jauge(mdp)
