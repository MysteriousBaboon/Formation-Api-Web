# ============================================================
# common/tools.py — La « boîte à outils » des agents
# ============================================================
# Reprise de cours_agents_llm/outils.py : un outil = une fonction
# Python. C'est TOUJOURS notre code qui exécute (jamais le LLM).
# ============================================================

import ast
import operator
from datetime import datetime

# --- Calculatrice SÉCURISÉE (jamais eval() sur une entrée du LLM) ---
_OPERATEURS = {
    ast.Add: operator.add, ast.Sub: operator.sub,
    ast.Mult: operator.mul, ast.Div: operator.truediv,
    ast.Pow: operator.pow, ast.Mod: operator.mod,
    ast.USub: operator.neg, ast.UAdd: operator.pos,
}


def _evaluer(noeud):
    if isinstance(noeud, ast.Constant) and isinstance(noeud.value, (int, float)):
        return noeud.value
    if isinstance(noeud, ast.BinOp) and type(noeud.op) in _OPERATEURS:
        return _OPERATEURS[type(noeud.op)](_evaluer(noeud.left), _evaluer(noeud.right))
    if isinstance(noeud, ast.UnaryOp) and type(noeud.op) in _OPERATEURS:
        return _OPERATEURS[type(noeud.op)](_evaluer(noeud.operand))
    raise ValueError("Expression non autorisée")


def calculer(expression):
    """Évalue une expression arithmétique en toute sécurité. Ex : '3 * 19.99'."""
    try:
        return str(_evaluer(ast.parse(str(expression), mode="eval").body))
    except Exception:
        return f"Erreur : '{expression}' n'est pas une expression valide."


def obtenir_meteo(ville):
    """Renvoie une météo simulée mais déterministe (démo sans vraie API)."""
    fausse_temp = 15 + (len(ville) % 10)
    return f"À {ville}, il fait {fausse_temp}°C et le ciel est dégagé."


def heure_actuelle():
    """Renvoie la date et l'heure courantes (jj/mm/aaaa)."""
    return datetime.now().strftime("%d/%m/%Y, %H:%M")


# --- Descriptions des outils pour le tool calling natif ---
SPECS_OUTILS = [
    {"type": "function", "function": {
        "name": "calculer",
        "description": "Évalue une expression arithmétique. À utiliser pour tout calcul.",
        "parameters": {"type": "object",
                       "properties": {"expression": {"type": "string"}},
                       "required": ["expression"]}}},
    {"type": "function", "function": {
        "name": "obtenir_meteo",
        "description": "Donne la météo actuelle d'une ville.",
        "parameters": {"type": "object",
                       "properties": {"ville": {"type": "string"}},
                       "required": ["ville"]}}},
    {"type": "function", "function": {
        "name": "heure_actuelle",
        "description": "Donne la date et l'heure actuelles.",
        "parameters": {"type": "object", "properties": {}}}},
]

# Registre nom -> fonction (appelée avec **arguments JSON du LLM).
REGISTRE = {
    "calculer": lambda expression: calculer(expression),
    "obtenir_meteo": lambda ville: obtenir_meteo(ville),
    "heure_actuelle": lambda: heure_actuelle(),
}
