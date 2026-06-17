# ============================================================
# cours_deep_learning/slides/contenu.py
# Contenu des slides du Cours 10 — Deep Learning & Computer Vision
# ============================================================
# Modifier : édite les listes, puis relance :  python slides/contenu.py
# ============================================================

import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RACINE))

from _slides.theme import (
    nouveau_deck, slide_titre, slide_section, slide_puces, sauver,
)


def construire():
    prs = nouveau_deck()

    slide_titre(
        prs,
        "Deep Learning & Computer Vision",
        "Cours 10 — Dans la boîte noire des réseaux de neurones",
    )

    # 1
    slide_section(prs, "1. Le neurone artificiel")
    slide_puces(prs, "L'unité de base", [
        "Reçoit des entrées (des nombres)",
        "Les multiplie par des POIDS, ajoute un BIAIS, fait la somme",
        "Passe le tout dans une fonction d'ACTIVATION",
        "Apprendre = trouver les bons poids et biais",
        ("Un LLM = des MILLIARDS de ces poids", 1),
    ])

    # 2
    slide_section(prs, "2. La fonction d'activation")
    slide_puces(prs, "La non-linéarité, le secret", [
        "Sans elle : empiler des neurones = une simple droite",
        "Marche (step) : 0 ou 1 (le perceptron historique)",
        "Sigmoïde : un S entre 0 et 1 (probabilités)",
        "ReLU : max(0, x) — le standard moderne, simple et efficace",
    ])

    # 3
    slide_section(prs, "3. Pourquoi « profond » ?")
    slide_puces(prs, "Des neurones aux couches", [
        "On organise les neurones en COUCHES successives",
        "Chaque couche apprend des motifs plus abstraits",
        ("Vision : bords → formes → objets", 1),
        "« Deep » = beaucoup de couches",
        "Un seul neurone ne sait pas faire XOR → il FAUT des couches",
    ])

    # 4
    slide_section(prs, "4. Comment ça apprend")
    slide_puces(prs, "L'aller-retour", [
        "Propagation avant : les entrées traversent → une prédiction",
        "Erreur : écart entre prédiction et vraie réponse",
        "Rétropropagation : on remonte l'erreur, on ajuste chaque poids",
        "On répète des milliers de fois → l'erreur diminue",
        "Analogie : descendre une montagne dans le brouillard (gradient)",
    ])

    # 5
    slide_section(prs, "5. Les grandes architectures")
    slide_puces(prs, "À chaque donnée son réseau", [
        "MLP (dense) : données tabulaires",
        "CNN : IMAGES (détecte des motifs locaux) — la vision",
        "RNN / LSTM : séquences (texte, audio)",
        "Transformer : texte — l'ATTENTION (→ cours 11, les LLM)",
    ])

    # 6
    slide_section(prs, "6. Computer Vision")
    slide_puces(prs, "Apprendre à voir", [
        "Une image = un tableau de nombres (les pixels)",
        "Classification : « c'est quoi ? »",
        "Détection : « c'est quoi ET où ? » (des boîtes)",
        "Segmentation : « quel pixel appartient à quoi ? »",
        "Le CNN a fait décoller la vision en 2012 (AlexNet)",
    ])

    # 7
    slide_section(prs, "7. Deep learning ou ML classique ?")
    slide_puces(prs, "Quand utiliser quoi", [
        "Peu de données tabulaires → ML classique (cours 9)",
        "Images / son / texte en masse → deep learning",
        "DL : features apprises toutes seules, mais boîte noire",
        "ML classique : interprétable, léger, souvent suffisant",
    ])

    slide_titre(prs, "À toi de jouer 🚀",
                "Démo 1 (un neurone à la main) puis 2 (lire des chiffres)")

    chemin = Path(__file__).resolve().parent / "deep_learning.pptx"
    sauver(prs, str(chemin))


if __name__ == "__main__":
    construire()
