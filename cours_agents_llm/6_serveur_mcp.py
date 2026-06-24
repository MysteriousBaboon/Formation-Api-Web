# ============================================================
# 6_serveur_mcp.py — Un SERVEUR MCP : nos outils derrière un protocole standard
# ============================================================
# Jusqu'ici, nos outils vivaient DANS le script de l'agent (REGISTRE + OUTILS).
# Ici, on les SORT dans un serveur MCP autonome. N'importe quel client MCP
# (Claude Desktop, Claude Code, Cursor… ou notre client de la démo 7) peut
# alors les utiliser — sans recopier une seule ligne de notre code.
#
# MCP (Model Context Protocol) = une "prise standard" entre les LLM et les outils.
#
# Lancement direct (pour tester) :   python 6_serveur_mcp.py
#   → le serveur attend des messages sur l'entrée standard (stdio). C'est NORMAL
#     qu'il semble "ne rien faire" : il est piloté par un CLIENT (démo 7 ou
#     Claude Desktop). Fais Ctrl+C pour quitter.
# ============================================================

from mcp.server.fastmcp import FastMCP

# On réutilise EXACTEMENT les mêmes fonctions que les démos précédentes :
# l'outil ne change pas, on change juste la façon de l'exposer.
from outils import calculer as _calculer, obtenir_meteo as _obtenir_meteo

# Le serveur, avec un nom lisible côté client.
mcp = FastMCP("mes-outils")


# Chaque @mcp.tool() expose une fonction comme outil MCP. La docstring et les
# annotations de type (expression: str) servent à DÉCRIRE l'outil au LLM —
# c'est le rôle qu'avaient les champs "description" et "parameters" des démos 1 à 5.
@mcp.tool()
def calculer(expression: str) -> str:
    """Évalue une expression arithmétique. À utiliser pour tout calcul. Ex : '3 * 19.99'."""
    return _calculer(expression)


@mcp.tool()
def obtenir_meteo(ville: str) -> str:
    """Donne la météo actuelle d'une ville."""
    return _obtenir_meteo(ville)


if __name__ == "__main__":
    # Transport "stdio" par défaut : le serveur parle au client via l'entrée /
    # sortie standard. C'est le mode utilisé par Claude Desktop & co. pour les
    # serveurs LOCAUX. (Un serveur distant utiliserait plutôt HTTP.)
    mcp.run()