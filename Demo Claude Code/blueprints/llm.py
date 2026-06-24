# ============================================================
# blueprints/llm.py — Cours « LLM : comprendre & utiliser »
# ============================================================
# Chat, sortie JSON structurée, mini-RAG (TF-IDF) et embeddings.
# Appels LLM RÉELS via common.llm_client (token requis).
# ============================================================

import json
import logging

from flask import Blueprint, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from common.auth import require_token
from common import llm_client

log = logging.getLogger(__name__)

bp = Blueprint("llm", __name__)


def _gerer_erreurs_llm(fn):
    """Transforme les erreurs LLM en réponses HTTP propres."""
    try:
        return fn()
    except (llm_client.LLMIndisponible, llm_client.EmbeddingsIndisponibles) as exc:
        return jsonify({"error": str(exc)}), 503
    except Exception as exc:  # noqa: BLE001
        log.error("Erreur LLM : %s", exc)
        return jsonify({"error": f"échec de l'appel LLM : {exc}"}), 502


# ------------------------------------------------------------
# Mini-RAG : base de connaissances + recherche TF-IDF
# ------------------------------------------------------------
DOCUMENTS = [
    "La société DingueCorp a été fondée en 2019 à Lyon par Camille Roche.",
    "Le forfait Premium coûte 49 euros par mois et inclut le support prioritaire.",
    "Le service client est joignable du lundi au vendredi, de 9h à 18h.",
    "Le remboursement est possible sous 30 jours après l'achat, sans justificatif.",
    "Nos bureaux sont fermés les jours fériés français.",
]
_vectoriseur = TfidfVectorizer()
_matrice = _vectoriseur.fit_transform(DOCUMENTS)


def _chercher_passage(question):
    vecteur = _vectoriseur.transform([question])
    similarites = cosine_similarity(vecteur, _matrice)[0]
    i = int(similarites.argmax())
    return DOCUMENTS[i], float(similarites[i])


@bp.route("/api/llm/chat", methods=["POST"])
@require_token
def chat():
    """Un message → une réponse du modèle."""
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()
    system = (data.get("system") or "").strip()
    if not message:
        return jsonify({"error": "champ 'message' requis"}), 400

    def appel():
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": message})
        texte = llm_client.chat_text(messages, max_tokens=400, temperature=0.7)
        return jsonify({"reponse": texte, "modele": llm_client.config.LLM_MODEL})

    return _gerer_erreurs_llm(appel)


@bp.route("/api/llm/json", methods=["POST"])
@require_token
def sortie_json():
    """Analyse d'un avis client, forcée en JSON structuré."""
    data = request.get_json(silent=True) or {}
    avis = (data.get("avis") or "").strip()
    if not avis:
        return jsonify({"error": "champ 'avis' requis"}), 400

    def appel():
        messages = [
            {"role": "system", "content": (
                "Tu analyses des avis clients. Réponds UNIQUEMENT avec un objet JSON "
                "valide, sans texte autour, avec exactement ces clés :\n"
                '  "sentiment" : "positif" | "neutre" | "negatif"\n'
                '  "note"      : un entier de 1 à 5\n'
                '  "themes"    : une liste de mots-clés\n'
                '  "resume"    : une phrase courte')},
            {"role": "user", "content": avis},
        ]
        texte = llm_client.chat_text(messages, max_tokens=300, temperature=0)
        propre = (texte.strip().removeprefix("```json").removeprefix("```")
                  .removesuffix("```").strip())
        try:
            analyse = json.loads(propre)
            return jsonify({"analyse": analyse, "brut": texte})
        except json.JSONDecodeError:
            return jsonify({"error": "le modèle n'a pas renvoyé de JSON valide",
                            "brut": texte}), 502

    return _gerer_erreurs_llm(appel)


@bp.route("/api/llm/rag", methods=["POST"])
@require_token
def rag():
    """Retrouve le passage pertinent (TF-IDF) puis fait répondre le modèle."""
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip()
    if not question:
        return jsonify({"error": "champ 'question' requis"}), 400

    def appel():
        passage, score = _chercher_passage(question)
        messages = [
            {"role": "system", "content": (
                "Réponds à la question en t'appuyant UNIQUEMENT sur le CONTEXTE "
                "fourni. Si la réponse n'y est pas, dis-le honnêtement.")},
            {"role": "user", "content": f"CONTEXTE : {passage}\n\nQUESTION : {question}"},
        ]
        texte = llm_client.chat_text(messages, max_tokens=300, temperature=0)
        return jsonify({
            "question": question,
            "passage_retrouve": passage,
            "score": round(score, 3),
            "reponse": texte,
        })

    return _gerer_erreurs_llm(appel)


@bp.route("/api/llm/embeddings", methods=["POST"])
@require_token
def embeddings():
    """Transforme des textes en vecteurs + matrice de similarité de sens."""
    data = request.get_json(silent=True) or {}
    textes = data.get("textes")
    if not isinstance(textes, list) or not all(isinstance(t, str) for t in textes) \
            or not textes:
        return jsonify({"error": "'textes' doit être une liste non vide de chaînes"}), 400

    def appel():
        vecteurs = llm_client.embeddings(textes)
        sim = cosine_similarity(vecteurs).tolist()
        return jsonify({
            "textes": textes,
            "dimension": len(vecteurs[0]) if vecteurs else 0,
            "apercu_premier_vecteur": [round(float(x), 4) for x in vecteurs[0][:5]],
            "similarites": [[round(float(v), 3) for v in ligne] for ligne in sim],
        })

    return _gerer_erreurs_llm(appel)
