# ============================================================
# blueprints/agents.py — Cours « Agents LLM »
# ============================================================
# Tool calling, boucle ReAct (à la main) et agent multi-outils.
# Appels LLM RÉELS via common.llm_client (token requis).
# ============================================================

import json
import logging
import re

from flask import Blueprint, request, jsonify

from common.auth import require_token
from common import llm_client
from common import tools

log = logging.getLogger(__name__)

bp = Blueprint("agents", __name__)


def _gerer_erreurs_llm(fn):
    try:
        return fn()
    except llm_client.LLMIndisponible as exc:
        return jsonify({"error": str(exc)}), 503
    except Exception as exc:  # noqa: BLE001
        log.error("Erreur agent : %s", exc)
        return jsonify({"error": f"échec de l'appel LLM : {exc}"}), 502


# ------------------------------------------------------------
# 1. Tool calling simple (un outil : la météo)
# ------------------------------------------------------------
_SPEC_METEO = [tools.SPECS_OUTILS[1]]  # obtenir_meteo


@bp.route("/api/agent/tool-calling", methods=["POST"])
@require_token
def tool_calling():
    """Le modèle décide (ou non) d'appeler l'outil météo, puis répond."""
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip()
    if not question:
        return jsonify({"error": "champ 'question' requis"}), 400

    def appel():
        messages = [{"role": "user", "content": question}]
        reponse = llm_client.completion(messages, tools=_SPEC_METEO, max_tokens=400)
        message = reponse.choices[0].message

        if not message.tool_calls:
            return jsonify({"a_utilise_outil": False, "reponse": message.content})

        messages.append(message)
        appels = []
        for appel_outil in message.tool_calls:
            args = json.loads(appel_outil.function.arguments or "{}")
            resultat = tools.REGISTRE[appel_outil.function.name](**args)
            appels.append({"outil": appel_outil.function.name,
                           "arguments": args, "resultat": resultat})
            messages.append({"role": "tool", "tool_call_id": appel_outil.id,
                             "content": str(resultat)})

        finale = llm_client.chat_text(messages, max_tokens=400)
        return jsonify({"a_utilise_outil": True, "appels": appels, "reponse": finale})

    return _gerer_erreurs_llm(appel)


# ------------------------------------------------------------
# 2. Boucle ReAct codée à la main (Pensée / Action / Observation)
# ------------------------------------------------------------
_SYSTEME_REACT = """Tu es un agent qui résout des tâches étape par étape.
Tu disposes de ces outils :
- calculer[expression]  : évalue un calcul, ex. calculer[3 * 19.99]
- meteo[ville]          : donne la météo d'une ville, ex. meteo[Lyon]

À chaque tour, réponds DANS CE FORMAT, une seule action à la fois.

Soit :
Pensée: <ton raisonnement>
Action: <nom_outil>[<argument>]

Ou, quand tu as la réponse :
Pensée: <ton raisonnement>
Réponse finale: <la réponse pour l'utilisateur>

Tu appelles un outil OU tu donnes une réponse finale, jamais les deux.
Tu ne fais pas les calculs toi-même : c'est l'outil qui s'en charge.
"""

_OUTILS_REACT = {"calculer": tools.calculer, "meteo": tools.obtenir_meteo}


def _executer_action(texte):
    m = re.search(r"Action:\s*(\w+)\[(.*?)\]", texte)
    if not m:
        return None
    nom, argument = m.group(1), m.group(2)
    if nom not in _OUTILS_REACT:
        return f"Outil inconnu : {nom}"
    return _OUTILS_REACT[nom](argument)


@bp.route("/api/agent/react", methods=["POST"])
@require_token
def react():
    """Boucle ReAct à la main, renvoie la trace complète des étapes."""
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip()
    if not question:
        return jsonify({"error": "champ 'question' requis"}), 400
    max_etapes = 5

    def appel():
        messages = [
            {"role": "system", "content": _SYSTEME_REACT},
            {"role": "user", "content": question},
        ]
        trace = []
        for etape in range(1, max_etapes + 1):
            texte = llm_client.chat_text(messages, max_tokens=400, temperature=0,
                                         stop=["Observation:"]).strip()
            if "Réponse finale:" in texte:
                finale = texte.split("Réponse finale:", 1)[1].strip()
                trace.append({"etape": etape, "texte": texte})
                return jsonify({"question": question, "trace": trace,
                                "reponse_finale": finale, "etapes": etape})

            observation = _executer_action(texte)
            if observation is None:
                trace.append({"etape": etape, "texte": texte,
                              "note": "aucune action détectée, arrêt"})
                return jsonify({"question": question, "trace": trace,
                                "reponse_finale": None})

            trace.append({"etape": etape, "texte": texte,
                          "observation": str(observation)})
            messages.append({"role": "assistant", "content": texte})
            messages.append({"role": "user", "content": f"Observation: {observation}"})

        return jsonify({"question": question, "trace": trace,
                        "reponse_finale": None,
                        "note": "nombre d'étapes maximum atteint (garde-fou)"})

    return _gerer_erreurs_llm(appel)


# ------------------------------------------------------------
# 3. Agent multi-outils (tool calling natif, plusieurs tours)
# ------------------------------------------------------------
@bp.route("/api/agent/multi-tools", methods=["POST"])
@require_token
def multi_tools():
    """Agent avec 3 outils, boucle jusqu'à la réponse (garde-fou anti-boucle)."""
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip()
    if not question:
        return jsonify({"error": "champ 'question' requis"}), 400
    max_tours = 6

    def appel():
        messages = [
            {"role": "system", "content": "Tu es un assistant qui utilise des outils "
                                          "quand c'est utile. Réponds en français."},
            {"role": "user", "content": question},
        ]
        trace = []
        for tour in range(1, max_tours + 1):
            reponse = llm_client.completion(messages, tools=tools.SPECS_OUTILS,
                                            max_tokens=500, temperature=0)
            message = reponse.choices[0].message
            if not message.tool_calls:
                return jsonify({"question": question, "trace": trace,
                                "reponse_finale": message.content, "tours": tour})

            messages.append(message)
            for appel_outil in message.tool_calls:
                nom = appel_outil.function.name
                args = json.loads(appel_outil.function.arguments or "{}")
                resultat = tools.REGISTRE[nom](**args)
                trace.append({"tour": tour, "outil": nom, "arguments": args,
                              "resultat": str(resultat)})
                messages.append({"role": "tool", "tool_call_id": appel_outil.id,
                                 "content": str(resultat)})

        return jsonify({"question": question, "trace": trace,
                        "reponse_finale": None,
                        "note": "nombre de tours maximum atteint (garde-fou)"})

    return _gerer_erreurs_llm(appel)


# ------------------------------------------------------------
# 4. Outils exposés par le serveur MCP du cours
# ------------------------------------------------------------
@bp.route("/api/agent/mcp-tools")
def mcp_tools():
    """Liste les outils déclarés par cours_agents_llm/6_serveur_mcp.py."""
    return jsonify({
        "serveur": "mes-outils",
        "transport": "stdio",
        "source": "cours_agents_llm/6_serveur_mcp.py",
        "outils": [
            {"nom": "calculer", "parametres": ["expression"],
             "description": "Évalue une expression arithmétique. Ex : '3 * 19.99'."},
            {"nom": "obtenir_meteo", "parametres": ["ville"],
             "description": "Donne la météo actuelle d'une ville."},
        ],
        "note": ("MCP (Model Context Protocol) = prise standard entre les LLM et les "
                 "outils. Le serveur est piloté en stdio par un client (Claude Desktop, "
                 "Claude Code, ou le client de la démo 7)."),
    })
