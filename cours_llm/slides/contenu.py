# ============================================================
# cours_llm/slides/contenu.py
# Contenu des slides du Cours 11 - Les LLM
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
        "Les LLM",
        "Cours 11 - Comprendre et piloter les grands modèles de langage",
    )

    # 1
    slide_section(prs, "1. C'est quoi un LLM ?")
    slide_puces(prs, "Une idée simple", [
        "Un réseau de neurones géant (un Transformer)",
        "Entraîné à PRÉDIRE LE MOT SUIVANT",
        "Des milliards de poids, énormément de texte",
        "Pas de base de réponses, pas de 'compréhension' humaine",
    ])

    # 2
    slide_section(prs, "2. Tokens & génération")
    slide_puces(prs, "Comment il lit et écrit", [
        "Token : un morceau de mot (≈ 4 caractères)",
        "On paie au token ; le contexte se mesure en tokens",
        "Il génère UN TOKEN À LA FOIS, en boucle",
        "À chaque étape : le token le plus probable (pas le plus vrai)",
        ("→ d'où les hallucinations", 1),
    ])

    # 3
    slide_section(prs, "3. Le Transformer et l'attention")
    slide_puces(prs, "Le secret de 2017", [
        "L'ATTENTION : chaque mot regarde tous les autres",
        "« la souris... elle a faim » → 'elle' = la souris",
        "C'est ce qui donne le CONTEXTE au modèle",
        "Idée à retenir : 'tout relier à tout'",
    ])

    # 4
    slide_section(prs, "4. Comment on l'entraîne")
    slide_puces(prs, "Trois phases", [
        "Pré-entraînement : lire une montagne de texte (coûteux)",
        "Fine-tuning : apprendre à suivre des instructions",
        "RLHF : des humains classent → le modèle apprend leurs préférences",
        ("RLHF = le 'renforcement' du cours 8 !", 1),
    ])

    # 5
    slide_section(prs, "5. Contexte et mémoire")
    slide_puces(prs, "À garder en tête", [
        "Fenêtre de contexte : ce qu'il voit d'un coup (en tokens)",
        "Au-delà, il 'oublie' le début",
        "AUCUNE mémoire entre deux appels",
        "La 'mémoire' d'un chat = on RENVOIE l'historique à chaque fois",
    ])

    # 6
    slide_section(prs, "6. Le prompting")
    slide_puces(prs, "Bien parler au modèle", [
        "Rôles : system (le cadre), user (la demande), assistant (ses réponses)",
        "Être précis : format, longueur, ton",
        "Few-shot : donner 2-3 exemples guide énormément",
        "Température : 0 = fiable/stable, 1.0 = créatif (max 1.0 chez Claude)",
    ])

    # 7
    slide_section(prs, "7. Limites à ne jamais oublier")
    slide_puces(prs, "Garder l'esprit critique", [
        "Hallucinations : invente avec aplomb → vérifier",
        "Cutoff : ne connaît pas l'actualité récente",
        "Calcul peu fiable : un LLM devine, il ne calcule pas",
        "Coût & latence : chaque appel prend temps et argent",
    ])

    # 8
    slide_section(prs, "8. L'appeler par code (agnostique)")
    slide_puces(prs, "Un seul code, tous les fournisseurs", [
        "Interface compatible OpenAI partout (Anthropic compris)",
        "client.chat.completions.create(model, messages, temperature)",
        "Le .env choisit : Anthropic (Claude), OpenAI, ou Ollama LOCAL",
        "Changer de fournisseur = changer le .env, pas le code",
    ])

    # 9
    slide_section(prs, "9. Le RAG")
    slide_puces(prs, "Donner TES documents au modèle", [
        "1. Chercher les passages pertinents dans tes docs",
        "2. Les coller dans le prompt",
        "3. Le LLM répond en s'appuyant dessus",
        "Réponses à jour, sourcées, moins d'hallucinations",
    ])

    slide_titre(prs, "À toi de jouer",
                "Configure ton .env, puis lance les démos 1 → 5")

    chemin = Path(__file__).resolve().parent / "llm.pptx"
    sauver(prs, str(chemin))


if __name__ == "__main__":
    construire()
