# ============================================================
# 5_mini_rag.py — Répondre à partir de TES documents (mini-RAG)
# ============================================================
# Un LLM ne connaît pas tes documents internes. Le RAG résout ça :
#   1. CHERCHER le passage le plus pertinent dans tes docs
#   2. Le COLLER dans le prompt
#   3. Laisser le LLM répondre EN S'APPUYANT dessus
#
# Ici, la recherche se fait avec TF-IDF (similarité de mots) pour rester
# simple et hors-ligne. Un vrai RAG utilise des "embeddings" (similarité
# de SENS), mais le principe — retrouver puis donner au modèle — est identique.
#
# Lancement :   python 5_mini_rag.py
# ============================================================

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from config import obtenir_client, demander

client, modele = obtenir_client()

# ------------------------------------------------------------
# 1. Notre "base de connaissances" (imagine un wiki interne)
# ------------------------------------------------------------
DOCUMENTS = [
    "La société DingueCorp a été fondée en 2019 à Lyon par Camille Roche.",
    "Le forfait Premium coûte 49 euros par mois et inclut le support prioritaire.",
    "Le service client est joignable du lundi au vendredi, de 9h à 18h.",
    "Le remboursement est possible sous 30 jours après l'achat, sans justificatif.",
    "Nos bureaux sont fermés les jours fériés français.",
]

# ------------------------------------------------------------
# 2. La RECHERCHE : trouver le document le plus proche de la question
# ------------------------------------------------------------
vectoriseur = TfidfVectorizer()
matrice_docs = vectoriseur.fit_transform(DOCUMENTS)


def chercher_passage(question):
    vecteur_question = vectoriseur.transform([question])
    similarites = cosine_similarity(vecteur_question, matrice_docs)[0]
    meilleur = similarites.argmax()
    return DOCUMENTS[meilleur], similarites[meilleur]


# ------------------------------------------------------------
# 3. RÉPONDRE en donnant le passage trouvé au LLM
# ------------------------------------------------------------
def repondre(question):
    passage, score = chercher_passage(question)
    print(f"❓ {question}")
    print(f"   📄 passage retrouvé (score {score:.2f}) : {passage}")

    messages = [
        {
            "role": "system",
            "content": (
                "Réponds à la question en t'appuyant UNIQUEMENT sur le CONTEXTE fourni. "
                "Si la réponse n'y est pas, dis-le honnêtement."
            ),
        },
        {"role": "user", "content": f"CONTEXTE : {passage}\n\nQUESTION : {question}"},
    ]
    print("   🤖", demander(client, modele, messages, temperature=0))
    print("-" * 60)


# Quelques questions de test
repondre("Combien coûte le forfait Premium ?")
repondre("Qui a fondé l'entreprise ?")
repondre("Puis-je être remboursé ?")
repondre("Quelle est la couleur préférée du PDG ?")   # absente des docs → il doit le dire

# ------------------------------------------------------------
# 🔧 À TOI DE JOUER
# ------------------------------------------------------------
# 1. Ajoute tes propres documents dans DOCUMENTS et pose des questions dessus.
# 2. Pose une question dont la réponse n'est PAS dans les docs : le modèle l'admet-il ?
# 3. Affiche les 2 meilleurs passages au lieu d'un seul (argsort) et donne-les au LLM.
