# ============================================================
# 6_embeddings.py — Du texte vers des nombres : la similarité de SENS
# ============================================================
# La démo 5 (RAG) retrouvait un passage par similarité de MOTS (TF-IDF) :
# elle marche tant que la question partage des mots avec le document.
# Mais "voiture" et "automobile" n'ont AUCUN mot commun... alors qu'ils
# veulent dire la même chose.
#
# Les EMBEDDINGS résolvent ça : chaque texte devient un vecteur de nombres
# tel que deux textes de SENS proche donnent deux vecteurs proches — même
# sans aucun mot en commun. C'est le vrai moteur d'un RAG.
#
# Pré-requis : un fournisseur d'embeddings dans ton .env (EMBED_* + LLM_EMBED_MODEL).
#              ⚠️ Anthropic n'en propose pas : voir .env.example (Voyage AI, OpenAI,
#              ou Ollama). Pas configuré ? Le script te l'explique proprement.
# Lancement :   python 6_embeddings.py
# ============================================================

import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from sklearn.metrics.pairwise import cosine_similarity

# Lit la config écrite dans le fichier .env (placé à côté de ce script)
load_dotenv(Path(__file__).resolve().parent / ".env")

# Anthropic ne fournit PAS d'embeddings : cette démo utilise donc un client
# DÉDIÉ, configuré via EMBED_* dans le .env (Voyage AI, OpenAI, Ollama…).
# À défaut d'EMBED_*, on réutilise le bloc chat (LLM_*) — pratique avec Ollama.
client_embeddings = OpenAI(
    base_url=os.getenv("EMBED_BASE_URL") or os.getenv("LLM_BASE_URL"),
    api_key=os.getenv("EMBED_API_KEY") or os.getenv("LLM_API_KEY"),
)
MODELE_EMBED = os.getenv("LLM_EMBED_MODEL")


def calculer_embeddings(textes):
    """Transforme une liste de textes en vecteurs (embeddings) via l'API.

    Renvoie un vecteur de nombres par texte. Le fournisseur et le modèle sont
    lus dans le .env (EMBED_* + LLM_EMBED_MODEL). Même interface compatible
    OpenAI que le chat, mais un endpoint différent.
    """
    reponse = client_embeddings.embeddings.create(model=MODELE_EMBED, input=textes)
    return [donnee.embedding for donnee in reponse.data]

# ------------------------------------------------------------
# 1. Un texte devient un VECTEUR de nombres
# ------------------------------------------------------------
try:
    vecteur = calculer_embeddings(["Bonjour le monde"])[0]
except Exception as erreur:
    print("⚠️  Impossible d'obtenir des embeddings.")
    print("    Anthropic ne propose pas d'API d'embeddings : configure un autre")
    print("    fournisseur dans ton .env via EMBED_BASE_URL / EMBED_API_KEY /")
    print("    LLM_EMBED_MODEL (Voyage AI, OpenAI, ou Ollama en local).")
    print("    Voir .env.example pour des exemples prêts à l'emploi.")
    print(f"    Détail technique : {erreur}")
    raise SystemExit(1)

print("1) Un texte → un vecteur de nombres")
print(f"   dimension du vecteur : {len(vecteur)}")
print(f"   5 premières valeurs  : {[round(x, 3) for x in vecteur[:5]]}")
print("-" * 60)

# ------------------------------------------------------------
# 2. La similarité de SENS (et non de mots)
# ------------------------------------------------------------
phrases = [
    "J'adore conduire ma voiture",
    "Mon automobile est très confortable",   # 0 mot commun avec la 1re...
    "Le chat dort sur le canapé",            # ... sujet totalement différent
]
vecteurs = calculer_embeddings(phrases)
sim = cosine_similarity(vecteurs)

print("2) Similarité de sens (1.0 = identique, 0 = sans rapport)")
for i, phrase_a in enumerate(phrases):
    for j in range(i + 1, len(phrases)):
        print(f"   {sim[i][j]:.2f}  | « {phrase_a} »  ~  « {phrases[j]} »")
print("   → voiture / automobile ressortent proches SANS partager de mot.")
print("-" * 60)

# ------------------------------------------------------------
# 3. Le RAG version "sens" : retrouver le bon passage même reformulé
# ------------------------------------------------------------
DOCUMENTS = [
    "La société DingueCorp a été fondée en 2019 à Lyon par Camille Roche.",
    "Le forfait Premium coûte 49 euros par mois et inclut le support prioritaire.",
    "Le service client est joignable du lundi au vendredi, de 9h à 18h.",
    "Le remboursement est possible sous 30 jours après l'achat, sans justificatif.",
]
vecteurs_docs = calculer_embeddings(DOCUMENTS)


def meilleur_passage(question):
    vecteur_question = calculer_embeddings([question])
    scores = cosine_similarity(vecteur_question, vecteurs_docs)[0]
    meilleur = scores.argmax()
    return DOCUMENTS[meilleur], scores[meilleur]


# Question SANS aucun mot des documents (ni "remboursement", ni "30 jours") :
question = "Puis-je récupérer mon argent si je change d'avis ?"
passage, score = meilleur_passage(question)
print("3) RAG par le sens — question reformulée, 0 mot en commun :")
print(f"   ❓ {question}")
print(f"   📄 passage trouvé (score {score:.2f}) : {passage}")
print("   → TF-IDF (démo 5) aurait calé : aucun mot partagé. Le sens, lui, relie.")
print("-" * 60)

# ------------------------------------------------------------
# 🔧 À TOI DE JOUER
# ------------------------------------------------------------
# 1. Ajoute tes propres phrases en partie 2 : quelles paires sont les plus proches ?
# 2. Reprends le mini-RAG (démo 5) et remplace sa recherche TF-IDF par ces embeddings.
# 3. Sur une même question reformulée, compare le passage trouvé par les deux méthodes.
