# ============================================================
# Exo 1 — GitHub API
# ============================================================
# Objectifs :
#   1. Recuperer les infos de l'utilisateur GitHub `torvalds`
#   2. Afficher followers + bio
#   3. Top 5 des repos par etoiles
# ============================================================

import requests

USERNAME = "torvalds"
BASE = "https://api.github.com"


# ============================================================
# 1. Infos utilisateur
# ============================================================
try:
    response = requests.get(f"{BASE}/users/{USERNAME}", timeout=10)
    response.raise_for_status()
    user = response.json()
except requests.RequestException as e:
    print(f"Erreur lors de la recuperation de l'utilisateur : {e}")
    raise SystemExit(1)

print(f"=== {user['login']} ===")
print(f"Nom        : {user.get('name', '(inconnu)')}")
print(f"Bio        : {user.get('bio') or '(pas de bio)'}")
print(f"Followers  : {user['followers']}")
print(f"Following  : {user['following']}")
print(f"Repos pub. : {user['public_repos']}")


# ============================================================
# 2. Top 5 repos par etoiles
# ============================================================
# /!\ Par defaut /repos renvoie 30 repos. Avec ?per_page=100
# on en recupere plus. Pour TOUS les repos il faudrait paginer.
try:
    response = requests.get(
        f"{BASE}/users/{USERNAME}/repos",
        params={"per_page": 100},
        timeout=10,
    )
    response.raise_for_status()
    repos = response.json()
except requests.RequestException as e:
    print(f"Erreur lors de la recuperation des repos : {e}")
    raise SystemExit(1)

# Tri decroissant par nombre d'etoiles
top = sorted(repos, key=lambda r: r["stargazers_count"], reverse=True)[:5]

print("\n=== Top 5 repos ===")
for i, repo in enumerate(top, 1):
    print(f"{i}. {repo['name']:<30} ⭐ {repo['stargazers_count']}")
    print(f"   {repo.get('description') or '(pas de description)'}")
