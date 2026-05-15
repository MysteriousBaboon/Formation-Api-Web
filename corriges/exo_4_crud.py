# ============================================================
# Exo 4 — POST / PUT / DELETE (JSONPlaceholder)
# ============================================================
# Objectifs :
#   1. Creer un post (POST)
#   2. Verifier code 201
#   3. Le modifier (PUT)
#   4. Le supprimer (DELETE) et verifier 200
# ============================================================

import requests

BASE = "https://jsonplaceholder.typicode.com"


# ============================================================
# 1. CREATE — POST /posts
# ============================================================
nouveau = {
    "title": "Mon premier post",
    "body": "Ceci est le contenu de mon post.",
    "userId": 1,
}

print("[1] Creation du post...")
response = requests.post(f"{BASE}/posts", json=nouveau, timeout=10)

# /!\ Pour une creation, on attend le code 201 (Created), pas 200
assert response.status_code == 201, f"Echec creation, code {response.status_code}"
print(f"    OK (code {response.status_code})")

post = response.json()
post_id = post["id"]
print(f"    Post cree avec id={post_id}")
print(f"    Reponse complete : {post}")


# ============================================================
# 2. UPDATE — PUT /posts/{id}
# ============================================================
modif = {
    "id": post_id,
    "title": "Titre modifie",
    "body": "Contenu mis a jour.",
    "userId": 1,
}

print(f"\n[2] Modification du post {post_id}...")
response = requests.put(f"{BASE}/posts/{post_id}", json=modif, timeout=10)

assert response.status_code == 200, f"Echec modif, code {response.status_code}"
print(f"    OK (code {response.status_code})")
print(f"    Apres modif : {response.json()}")


# ============================================================
# 3. DELETE — DELETE /posts/{id}
# ============================================================
print(f"\n[3] Suppression du post {post_id}...")
response = requests.delete(f"{BASE}/posts/{post_id}", timeout=10)

assert response.status_code == 200, f"Echec delete, code {response.status_code}"
print(f"    OK (code {response.status_code})")


# ============================================================
# Note importante : JSONPlaceholder est un faux serveur.
# Il accepte tout et fait semblant, mais ne stocke RIEN.
# Si tu fais GET /posts/101 apres ton POST, tu auras une 404.
# C'est normal, c'est juste pour s'entrainer aux verbes HTTP.
# ============================================================
