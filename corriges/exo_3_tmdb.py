# ============================================================
# Exo 3 — TheMovieDB (auth par cle API)
# ============================================================
# Objectifs :
#   1. Cle API stockee dans .env
#   2. Chercher "Inception"
#   3. Afficher titre, annee, note, synopsis
#   4. Afficher 3 acteurs principaux
# ============================================================

import os
import requests
from dotenv import load_dotenv


# ============================================================
# Charger la cle API depuis .env
# ============================================================
# A la racine du projet api/, le fichier .env contient :
#   TMDB_API_KEY=ta_cle_ici
#
# load_dotenv() cherche le .env automatiquement.
load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")

if not API_KEY:
    raise SystemExit("Pas de TMDB_API_KEY dans .env. Va sur themoviedb.org pour en generer une.")

BASE = "https://api.themoviedb.org/3"

movie = input("Quelle est ton film prefere ?")

# ============================================================
# 1. Rechercher "Inception"
# ============================================================
try:
    response = requests.get(
        f"{BASE}/search/movie",
        params={"api_key": API_KEY, "query": movie, "language": "fr-FR"},
        timeout=10,
    )
    response.raise_for_status()
    resultats = response.json()["results"]
except requests.RequestException as e:
    raise SystemExit(f"Erreur API recherche : {e}")

if not resultats:
    raise SystemExit("Aucun resultat trouve")

film = resultats[0]


# ============================================================
# 2. Afficher les infos du premier resultat
# ============================================================
# release_date est au format "2010-07-15", on extrait l'annee
annee = film["release_date"] if film.get("release_date") else "?"

print(f"=== {film['title']} ({annee}) ===")
print(f"Note     : {film['vote_average']} / 10 ({film['vote_count']} votes)")
print(f"Synopsis : {film.get('overview', '(pas de synopsis)')}")


# ============================================================
# 3. Casting — 3 acteurs principaux
# ============================================================
film_id = film["id"]

try:
    response = requests.get(
        f"{BASE}/movie/{film_id}/credits",
        params={"api_key": API_KEY, "language": "fr-FR"},
        timeout=10,
    )
    response.raise_for_status()
    casting = response.json()["cast"]
except requests.RequestException as e:
    raise SystemExit(f"Erreur API casting : {e}")

print("\nActeurs principaux :")
for acteur in casting[:3]:
    print(f"  - {acteur['name']:<25} dans le role de {acteur['character']}")
