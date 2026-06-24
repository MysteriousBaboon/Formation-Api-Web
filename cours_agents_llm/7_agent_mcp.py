# ============================================================
# 7_agent_mcp.py — Un agent qui branche les outils d'un SERVEUR MCP
# ============================================================
# La même boucle d'agent qu'à la démo 4… mais les outils ne sont plus codés en
# dur ici : ils viennent du serveur MCP (démo 6). Le client MCP :
#   1. lance le serveur et se connecte (transport stdio),
#   2. DÉCOUVRE ses outils tout seul (list_tools),
#   3. les traduit au format attendu par le LLM,
#   4. quand le LLM demande un outil, DÉLÈGUE l'exécution au serveur (call_tool).
#
# L'aha : démo 4 → l'agent exécutait l'outil (REGISTRE[nom](**args)).
#          démo 7 → il délègue au serveur MCP (session.call_tool(...)).
#          Le LLM, lui, ne voit aucune différence : c'est toujours du tool calling.
#
# Lancement :   python 7_agent_mcp.py     (pas besoin de lancer la démo 6 à part)
# ============================================================

import asyncio
import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Lit la config écrite dans le fichier .env (placé à côté de ce script)
load_dotenv(Path(__file__).resolve().parent / ".env")

# Le client qui parle au LLM, via l'interface compatible OpenAI.
# Par défaut on cible Anthropic (Claude) ; le .env peut pointer ailleurs
# (OpenAI, Mistral, Ollama en local…) sans toucher au code.
client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL"),
    api_key=os.getenv("LLM_API_KEY"),
)
modele = os.getenv("LLM_MODEL")

# Comment lancer le serveur MCP : ici en sous-processus local, via stdio.
# On utilise le MÊME Python que celui qui exécute ce client (sys.executable),
# pour être sûr que le paquet 'mcp' y est installé.
PARAMS_SERVEUR = StdioServerParameters(
    command=sys.executable,
    args=[str(Path(__file__).resolve().parent / "6_serveur_mcp.py")],
)


def mcp_vers_openai(outils_mcp):
    """Traduit les outils annoncés par le serveur MCP au format 'tools' du LLM."""
    return [
        {"type": "function", "function": {
            "name": o.name,
            "description": o.description,
            "parameters": o.inputSchema,   # déjà un JSON Schema, fourni par le serveur
        }}
        for o in outils_mcp
    ]


async def agent(question, session, outils_llm, max_tours=6):
    print(f"❓ {question}\n" + "=" * 60)
    messages = [
        {"role": "system", "content": "Tu es un assistant qui utilise des outils quand c'est utile. "
                                       "Réponds en français."},
        {"role": "user", "content": question},
    ]

    for tour in range(1, max_tours + 1):
        reponse = client.chat.completions.create(
            model=modele, messages=messages, tools=outils_llm, temperature=0,
        )
        message = reponse.choices[0].message

        # Pas d'outil demandé → c'est la réponse finale
        if not message.tool_calls:
            print("✅ Réponse finale :", message.content)
            return message.content

        messages.append(message)
        for appel in message.tool_calls:
            nom = appel.function.name
            args = json.loads(appel.function.arguments or "{}")

            # 👉 LA différence avec la démo 4 : on n'exécute PAS l'outil nous-mêmes.
            #    On délègue au SERVEUR MCP, via le protocole.
            resultat = await session.call_tool(nom, arguments=args)
            texte = resultat.content[0].text if resultat.content else ""

            print(f"[tour {tour}] 🛠️  (via MCP) {nom}({args}) → {texte}")
            messages.append({"role": "tool", "tool_call_id": appel.id, "content": texte})

    print("⏹️  Nombre de tours maximum atteint (garde-fou).")
    return None


async def main():
    # 1. On se connecte au serveur MCP (lancé en sous-processus, transport stdio).
    async with stdio_client(PARAMS_SERVEUR) as (lecture, ecriture):
        async with ClientSession(lecture, ecriture) as session:
            await session.initialize()

            # 2. On DÉCOUVRE les outils du serveur (au lieu de les coder en dur).
            annonce = await session.list_tools()
            outils_llm = mcp_vers_openai(annonce.tools)
            print("🔌 Outils découverts sur le serveur MCP :",
                  ", ".join(o.name for o in annonce.tools), "\n")

            # 3. Même boucle d'agent qu'à la démo 4 — mais branchée sur MCP.
            await agent(
                "Quel temps fait-il à Marseille, et combien font 15 % de 240 ?",
                session, outils_llm,
            )


if __name__ == "__main__":
    asyncio.run(main())

# ------------------------------------------------------------
# 🔧 À TOI DE JOUER
# ------------------------------------------------------------
# 1. Ajoute un outil au SERVEUR (démo 6) avec un @mcp.tool() — PAS ici. Relance
#    ce client : il le découvre tout seul (rien à changer dans l'agent). C'est ça,
#    le découplage offert par MCP.
# 2. Compare avec la démo 4 : qu'est-ce qui a changé dans la boucle, et qu'est-ce
#    qui est resté identique côté LLM ?
# 3. Branche plutôt ce même serveur dans Claude Desktop / Claude Code (voir cours.md,
#    section MCP) : tes outils deviennent disponibles dans un vrai client, sans code.