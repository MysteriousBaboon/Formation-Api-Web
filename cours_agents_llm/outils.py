# ============================================================
# outils.py — La "boîte à outils" de nos agents
# ============================================================
# Un outil d'agent = une simple fonction Python. On les regroupe ici
# pour que les démos restent lisibles. Chaque fonction est ce que le LLM
# pourra demander d'exécuter (mais c'est TOUJOURS notre code qui exécute).
# ============================================================

import ast
import operator
from datetime import datetime


# ------------------------------------------------------------
# 1. Calculatrice SÉCURISÉE
# ------------------------------------------------------------
# ⚠️ On n'utilise JAMAIS eval() sur une chaîne venue du LLM : ce serait
# une faille de sécurité béante. On évalue nous-mêmes, en n'autorisant
# QUE des nombres et des opérations arithmétiques.
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
        resultat = _evaluer(ast.parse(expression, mode="eval").body)
        return str(resultat)
    except Exception:
        return f"Erreur : '{expression}' n'est pas une expression valide."


# ------------------------------------------------------------
# 2. Météo (SIMULÉE pour la démo)
# ------------------------------------------------------------
def obtenir_meteo(ville):
    """Renvoie une météo bidon mais déterministe (démo sans vraie API)."""
    fausse_temp = 15 + (len(ville) % 10)   # juste pour varier selon la ville
    return f"À {ville}, il fait {fausse_temp}°C et le ciel est dégagé."


# ------------------------------------------------------------
# 3. Heure actuelle (le LLM n'a pas d'horloge)
# ------------------------------------------------------------
def heure_actuelle():
    """Renvoie la date et l'heure courantes (format neutre jj/mm/aaaa)."""
    return datetime.now().strftime("%d/%m/%Y, %H:%M")


# Petit test rapide si on lance ce fichier directement
if __name__ == "__main__":
    print("calculer('3 * 19.99 * 1.20') =", calculer("3 * 19.99 * 1.20"))
    print("calculer('__import__(\"os\")')  =", calculer('__import__("os")'))  # bloqué !
    print("obtenir_meteo('Lyon')         =", obtenir_meteo("Lyon"))
    print("heure_actuelle()              =", heure_actuelle())
