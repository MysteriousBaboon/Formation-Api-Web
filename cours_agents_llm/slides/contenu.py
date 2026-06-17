# ============================================================
# cours_agents_llm/slides/contenu.py
# Contenu des slides du Cours 12 — Agents LLM
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
        "Agents LLM",
        "Cours 12 — Quand l'IA ne répond plus seulement : elle agit",
    )

    # 1
    slide_section(prs, "1. D'un LLM à un agent")
    slide_puces(prs, "Combler les faiblesses du LLM", [
        "Le LLM seul : ne calcule pas bien, ignore tes données, n'agit pas",
        "Un agent = un LLM + des OUTILS + une boucle",
        "Le LLM est le cerveau, les outils sont les mains",
        "Il décide QUAND utiliser quel outil",
    ])

    # 2
    slide_section(prs, "2. La boucle agentique")
    slide_puces(prs, "Perception → raisonnement → action", [
        "Raisonner : que faire maintenant ?",
        "Agir : appeler un outil",
        "Observer : lire le résultat",
        "Recommencer jusqu'à pouvoir répondre",
        ("Ce motif s'appelle ReAct (Reasoning + Acting)", 1),
    ])

    # 3
    slide_section(prs, "3. Le function / tool calling")
    slide_puces(prs, "Comment le LLM 'appelle' une fonction", [
        "On DÉCRIT les outils au modèle (nom, rôle, paramètres)",
        "Le LLM répond par une DEMANDE d'appel structurée",
        "C'est TOUJOURS notre code qui exécute la fonction",
        "On renvoie le résultat → le LLM formule la réponse",
        ("La description de l'outil = un mini-prompt à soigner", 1),
    ])

    # 4
    slide_section(prs, "4. Les bons outils")
    slide_puces(prs, "Un outil = une fonction Python", [
        "Calculatrice : pour les calculs fiables",
        "Recherche / RAG : pour les infos à jour ou privées",
        "Appel d'API : pour agir sur d'autres systèmes",
        "Date/heure : le LLM n'a pas d'horloge",
        ("Ton micro-service du cours 3 EST un outil d'agent parfait", 1),
    ])

    # 5
    slide_section(prs, "5. Les garde-fous")
    slide_puces(prs, "Un agent qui agit, ça se sécurise", [
        "Limite d'itérations : sinon boucle infinie + budget brûlé",
        "Validation humaine pour les actions sensibles",
        "Jamais d'eval() brut sur une entrée du LLM",
        "Coût : chaque étape = un appel LLM",
        ("Une IA propose, un humain dispose", 1),
    ])

    # 6
    slide_section(prs, "6. Les frameworks")
    slide_puces(prs, "Coder à la main, puis outiller", [
        "LangChain : le plus connu (chaînes, agents, intégrations)",
        "LlamaIndex : spécialisé RAG / données",
        "SDK natifs (OpenAI, Anthropic) : tool calling intégré",
        "n8n (nœud AI Agent) : des agents en no-code",
        ("Comprendre sans framework d'abord = le meilleur apprentissage", 1),
    ])

    # 7
    slide_section(prs, "La boucle se referme")
    slide_puces(prs, "Tout le parcours dans un agent", [
        "LLM (cours 11) = le cerveau",
        "Ton API / micro-service (cours 3) = un outil",
        "n8n / cron (cours 7) = déclenche et distribue",
        "De la variable Python à l'IA autonome : bravo 🎓",
    ])

    slide_titre(prs, "À toi de jouer 🚀",
                "Démos 1 → 5, puis le projet fil rouge (exos.md)")

    chemin = Path(__file__).resolve().parent / "agents_llm.pptx"
    sauver(prs, str(chemin))


if __name__ == "__main__":
    construire()
