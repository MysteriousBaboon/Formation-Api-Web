# ============================================================
# 4_conversation_memoire.py — Un mini-chat qui se SOUVIENT
# ============================================================
# Un LLM n'a AUCUNE mémoire entre deux appels. La "mémoire" d'un chat,
# c'est juste l'historique des messages qu'on lui RENVOIE à chaque fois.
# On le démontre en construisant une vraie conversation au terminal.
#
# Lancement :   python 4_conversation_memoire.py
# (tape 'quit' pour sortir)
# ============================================================

from config import obtenir_client

client, modele = obtenir_client()

# ------------------------------------------------------------
# L'historique : LA mémoire de la conversation
# ------------------------------------------------------------
# On commence par poser le cadre avec un message "system".
historique = [
    {"role": "system", "content": "Tu es un assistant amical et concis. Réponds en français."},
]

print("💬 Mini-chat (tape 'quit' pour sortir)")
print("Astuce : présente-toi, puis demande plus tard 'comment je m'appelle ?'")
print("=" * 60)

while True:
    question = input("\nToi > ").strip()
    if question.lower() in {"quit", "exit", "q"}:
        print("À bientôt !")
        break
    if not question:
        continue

    # 1. On AJOUTE le message de l'utilisateur à l'historique
    historique.append({"role": "user", "content": question})

    # 2. On envoie TOUT l'historique (c'est ça, la mémoire)
    reponse = client.chat.completions.create(
        model=modele,
        messages=historique,
        temperature=0.7,
    )
    texte = reponse.choices[0].message.content

    # 3. On AJOUTE aussi la réponse du modèle, pour le prochain tour
    historique.append({"role": "assistant", "content": texte})

    print("🤖 >", texte)
    print(f"   (l'historique contient maintenant {len(historique)} messages)")

# ------------------------------------------------------------
# 🔧 À TOI DE JOUER
# ------------------------------------------------------------
# 1. Présente-toi (ton prénom), discute, puis demande "comment je m'appelle ?".
#    Il s'en souvient grâce à l'historique.
# 2. Commente la ligne "historique.append(...assistant...)" : que se passe-t-il ?
#    (il perd le fil — il ne voit plus ses propres réponses)
# 3. Compte les messages : à long terme, l'historique grossit → ça coûte plus de tokens.
#    (les vrais chats "résument" les vieux messages pour économiser)
