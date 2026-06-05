# ============================================================
# cours_ia_panorama/slides/contenu.py
# Contenu des slides du Cours 8 — Panorama de l'IA
# ============================================================
# Pour MODIFIER les slides : édite les listes ci-dessous (titres + puces),
# puis relance :   python slides/contenu.py
# Ça régénère slides/panorama.pptx (prêt à projeter).
#
# Une puce = une chaîne "..."  ou  un tuple ("...", niveau) où
# niveau vaut 0, 1 ou 2 (pour indenter).
# ============================================================

import sys
from pathlib import Path

# On rend le dossier _slides/ (à la racine du repo) importable
RACINE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RACINE))

from _slides.theme import (
    nouveau_deck, slide_titre, slide_section, slide_puces, sauver,
)


def construire():
    prs = nouveau_deck()

    slide_titre(
        prs,
        "Panorama de l'IA",
        "Cours 8 — La carte du territoire avant de plonger",
    )

    # --- Partie 1 ---
    slide_section(prs, "1. C'est quoi « l'IA » ?")
    slide_puces(prs, "Une définition simple", [
        "IA = faire faire à une machine des tâches qui demandent",
        ("normalement de « l'intelligence » humaine", 1),
        "Reconnaître une image, comprendre une phrase, recommander un film…",
        "Ce n'est PAS magique : ce sont des maths + des données + du calcul",
    ])
    slide_puces(prs, "Les poupées russes", [
        "Intelligence Artificielle : le grand ensemble",
        ("Machine Learning : la machine apprend à partir d'exemples", 1),
        ("Deep Learning : du ML avec des réseaux de neurones profonds", 2),
        ("IA générative (ChatGPT…) : du deep learning qui crée du contenu", 2),
        "Retiens : IA ⊃ ML ⊃ Deep Learning ⊃ IA générative",
    ])

    # --- Partie 2 ---
    slide_section(prs, "2. Les grandes familles")
    slide_puces(prs, "Où l'IA travaille aujourd'hui", [
        "Vision (computer vision) : analyser images & vidéos",
        "Langage (NLP) : comprendre et générer du texte",
        "Audio / voix : reconnaissance et synthèse vocale",
        "Génératif : créer texte, images, son, code",
        "Recommandation : Netflix, Spotify, e-commerce",
        "Décision / robotique : jeux, robots, conduite",
    ])

    # --- Partie 3 ---
    slide_section(prs, "3. Comment une machine « apprend »")
    slide_puces(prs, "Les 3 grands types d'apprentissage", [
        "Supervisé : on montre des exemples étiquetés (photo → « chat »)",
        ("→ le cœur de ce qu'on verra (cours 9 & 10)", 1),
        "Non-supervisé : on cherche des groupes sans étiquettes",
        ("→ segmentation de clients, détection d'anomalies", 1),
        "Par renforcement : apprendre par essai/erreur et récompense",
        ("→ jeux (AlphaGo), robotique", 1),
    ])
    slide_puces(prs, "Le vocabulaire de survie", [
        "Modèle : le « cerveau » entraîné qui fait des prédictions",
        "Dataset : les données d'exemple",
        "Features / labels : les entrées / la bonne réponse",
        "Entraînement vs inférence : apprendre vs utiliser",
        "Paramètres (poids) : ce que le modèle ajuste en apprenant",
        "GPU : la puce qui rend l'entraînement rapide",
    ])

    # --- Partie 4 ---
    slide_section(prs, "4. Un peu d'histoire")
    slide_puces(prs, "60 ans en 5 dates", [
        "1958 : le perceptron, premier neurone artificiel",
        "1970-90 : « hivers de l'IA », trop de promesses, peu de résultats",
        "2012 : le deep learning explose (ImageNet, la vision décolle)",
        "2017 : les Transformers (« Attention is all you need »)",
        "2022 : ChatGPT — l'IA générative pour le grand public",
    ])

    # --- Partie 5 ---
    slide_section(prs, "5. Limites & garde-fous")
    slide_puces(prs, "Garder l'esprit critique", [
        "Biais : un modèle reproduit les biais de ses données",
        "Hallucinations : un LLM peut inventer avec aplomb",
        "Données : pas de bonnes données = pas de bon modèle",
        "Coût & énergie : entraîner de gros modèles coûte cher",
        "Vie privée & droit d'auteur : d'où viennent les données ?",
    ])

    # --- Carte du parcours ---
    slide_section(prs, "La carte de nos 5 journées")
    slide_puces(prs, "Où on va ensemble", [
        "Cours 8 — Panorama (aujourd'hui) : la vue d'ensemble",
        "Cours 9 — Machine Learning : la machine qui apprend des données",
        "Cours 10 — Deep Learning & Vision : les réseaux de neurones",
        "Cours 11 — LLM : comprendre et piloter les grands modèles de langage",
        "Cours 12 — Agents LLM : l'IA qui agit, pas seulement qui répond",
    ])
    slide_titre(prs, "À toi de jouer 🚀", "Ouvre exos.md et explore les démos en ligne")

    chemin = Path(__file__).resolve().parent / "panorama.pptx"
    sauver(prs, str(chemin))


if __name__ == "__main__":
    construire()
