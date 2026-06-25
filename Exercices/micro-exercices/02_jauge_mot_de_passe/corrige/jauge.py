# ============================================================
# jauge.py — Jauge de mot de passe (corrigé)
# ============================================================
# Compétence : une fonction pure qui NOTE une donnée + rendu visuel.
# Lancement :  python jauge.py
# ============================================================

import string

RESET = "\033[0m"
ROUGE, JAUNE, VERT = "\033[91m", "\033[93m", "\033[92m"
SYMBOLES = set(string.punctuation)  # {'!', '@', '#', '&', ...}

A_TESTER = ["123", "motdepasse", "Soleil2026", "Tr0ub4dour&Co"]


# ------------------------------------------------------------
# evaluer : fonction PURE -> renvoie un score + ce qui manque
# (pas de print ici : on pourra la tester avec pytest plus tard)
# ------------------------------------------------------------
def evaluer(mdp):
    score = 0
    manques = []

    # Longueur (deux paliers cumulables)
    if len(mdp) >= 8:
        score += 20
    else:
        manques.append("au moins 8 caractères")
    if len(mdp) >= 12:
        score += 15

    # Types de caractères présents
    if any(c.islower() for c in mdp):
        score += 15
    else:
        manques.append("une minuscule")

    if any(c.isupper() for c in mdp):
        score += 15
    else:
        manques.append("une majuscule")

    if any(c.isdigit() for c in mdp):
        score += 15
    else:
        manques.append("un chiffre")

    if any(c in SYMBOLES for c in mdp):
        score += 20
    else:
        manques.append("un symbole (!?@#...)")

    return {"score": score, "manques": manques}


# ------------------------------------------------------------
# verdict : traduit un score en libellé + couleur
# ------------------------------------------------------------
def verdict(score):
    if score < 40:
        return ("Faible", ROUGE, "🔴")
    if score < 70:
        return ("Moyen", JAUNE, "🟠")
    if score < 90:
        return ("Bon", VERT, "🟢")
    return ("Costaud", VERT, "💪")


# ------------------------------------------------------------
# afficher_jauge : la partie visuelle
# ------------------------------------------------------------
def afficher_jauge(mdp):
    resultat = evaluer(mdp)
    score = resultat["score"]
    libelle, couleur, emoji = verdict(score)

    rempli = round(score / 100 * 20)
    barre = couleur + "█" * rempli + RESET + "░" * (20 - rempli)

    print(f"{mdp!r}")
    print(f"  [{barre}] {score}/100  {emoji} {libelle}")
    if resultat["manques"]:
        print(f"  💡 Ajoute : {', '.join(resultat['manques'])}")
    print()


if __name__ == "__main__":
    for mdp in A_TESTER:
        afficher_jauge(mdp)
