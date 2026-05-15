# ============================================================
# Exo 2 — Meteo a Reims (Open-Meteo)
# ============================================================
# Objectifs :
#   1. Recuperer la meteo actuelle a Reims
#   2. Bonus : fonction meteo(ville) avec geocodage
# ============================================================

import requests


METEO_URL = "https://api.open-meteo.com/v1/forecast"
GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"


# ============================================================
# 1. Meteo a Reims (coordonnees connues)
# ============================================================
params = {
    "latitude": 49.26,
    "longitude": 4.03,
    "current_weather": True,
}

try:
    response = requests.get(METEO_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
except requests.RequestException as e:
    print(f"Erreur API meteo : {e}")
    raise SystemExit(1)

courant = data["current_weather"]
print("=== Meteo a Reims ===")
print(f"Temperature   : {courant['temperature']} °C")
print(f"Vent          : {courant['windspeed']} km/h")
print(f"Code meteo    : {courant['weathercode']}")
print(f"Heure releve  : {courant['time']}")


# ============================================================
# 2. Bonus : fonction qui prend un nom de ville
# ============================================================
def meteo(ville):
    """Retourne un dict avec temperature/vent pour la ville donnee."""

    # Etape 1 : geocodage (ville -> lat/lon)
    geo = requests.get(GEO_URL, params={"name": ville, "count": 1}, timeout=10)
    geo.raise_for_status()
    resultats = geo.json().get("results", [])

    if not resultats:
        raise ValueError(f"Ville inconnue : {ville}")

    lat = resultats[0]["latitude"]
    lon = resultats[0]["longitude"]
    pays = resultats[0].get("country", "?")

    # Etape 2 : meteo
    response = requests.get(
        METEO_URL,
        params={"latitude": lat, "longitude": lon, "current_weather": True},
        timeout=10,
    )
    response.raise_for_status()
    courant = response.json()["current_weather"]

    return {
        "ville": ville,
        "pays": pays,
        "lat": lat,
        "lon": lon,
        "temperature": courant["temperature"],
        "vent": courant["windspeed"],
    }


# Test sur plusieurs villes
print("\n=== Test fonction meteo() ===")
for ville in ["Paris", "Tokyo", "Reykjavik", "Sydney"]:
    try:
        m = meteo(ville)
        print(f"{m['ville']:<12} ({m['pays']}) %s : {m['temperature']} °C, vent {m['vent']} km/h")
    except ValueError as e:
        print(f"  {e}")
    except requests.RequestException as e:
        print(f"  Erreur reseau pour {ville} : {e}")
