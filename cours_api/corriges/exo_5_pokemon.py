# ============================================================
# Exo 5 — Pagination + persistance (PokeAPI)
# ============================================================
# Objectifs :
#   1. Recuperer les 150 premiers Pokemon
#   2. Pour chacun : nom, taille, poids, types
#   3. Sauvegarder dans pokemons.json
#   4. Bonus : sleep + try/except par appel
# ============================================================

import requests
import json
import time

BASE = "https://pokeapi.co/api/v2"


# ============================================================
# 1. Recuperer la liste des 150 premiers Pokemon
# ============================================================
print("Recuperation de la liste...")
response = requests.get(
    f"{BASE}/pokemon",
    params={"limit": 150, "offset": 0},
    timeout=10,
)
response.raise_for_status()

liste = response.json()["results"]
print(f"  {len(liste)} pokemon dans la liste")


# ============================================================
# 2. Pour chaque pokemon, recuperer son detail
# ============================================================
pokemons = []
erreurs = []

for i, p in enumerate(liste, 1):
    nom = p["name"]

    try:
        response = requests.get(p["url"], timeout=10)
        response.raise_for_status()
        detail = response.json()

        pokemons.append({
            "id": detail["id"],
            "nom": detail["name"],
            "taille": detail["height"],          # en decimetres
            "poids": detail["weight"],           # en hectogrammes
            "types": [t["type"]["name"] for t in detail["types"]],
        })
        print("OK")

    except requests.RequestException as e:
        # Si UN pokemon plante, on continue avec les autres
        print(f"ECHEC ({e})")
        erreurs.append(nom)

    # On laisse respirer l'API
    time.sleep(0.1)


# ============================================================
# 3. Sauvegarder en JSON
# ============================================================
with open("pokemons.json", "w", encoding="utf-8") as f:
    json.dump(pokemons, f, ensure_ascii=False, indent=2)
    # ensure_ascii=False : garde les accents/caracteres speciaux lisibles
    # indent=2 : JSON lisible par un humain (joli)

print(f"\n{len(pokemons)} pokemon sauvegardes dans pokemons.json")
if erreurs:
    print(f"Echecs : {erreurs}")


# ============================================================
# Petite analyse pour le fun
# ============================================================
# Compter les types
from collections import Counter
types_count = Counter()
for p in pokemons:
    for t in p["types"]:
        types_count[t] += 1

print("\nTop 5 des types :")
for t, n in types_count.most_common(5):
    print(f"  {t:<10} {n}")

# Le plus gros / le plus lourd
plus_grand = max(pokemons, key=lambda p: p["taille"])
plus_lourd = max(pokemons, key=lambda p: p["poids"])
print(f"\nPlus grand : {plus_grand['nom']} ({plus_grand['taille'] / 10} m)")
print(f"Plus lourd : {plus_lourd['nom']} ({plus_lourd['poids'] / 10} kg)")
