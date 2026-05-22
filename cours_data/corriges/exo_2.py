# ============================================================
# Exo 2 — Nettoyer un dataset crade
# ============================================================
# Objectifs : transformer data/clients_crade.csv (doublons,
# espaces, casses incoherentes, dates au format americain et
# francais melanges...) en un data/clients_propre.csv utilisable.
# ============================================================

import pandas as pd
from pathlib import Path


# ============================================================
# 1. Chargement
# ============================================================
df = pd.read_csv("data/clients_crade.csv")
nb_original = len(df)
print(f"Lignes au depart : {nb_original}")

# ============================================================
# 2. Strip + lower sur les colonnes texte
# ============================================================
# .str.strip() retire les espaces avant/apres
# .str.lower() met tout en minuscules

for col in ["Nom", "Email", "Ville"]:
    df[col] = df[col].astype(str).str.strip()
df["Email"] = df["Email"].str.lower()

# ============================================================
# 3. Age en nombre
# ============================================================
# errors="coerce" = au lieu de planter sur "vingt-cinq", pandas
# met NaN. Beaucoup plus pratique que de gerer les exceptions.
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")


# ============================================================
# 4. Dates au format unifie
# ============================================================
# Le CSV melange "2024-01-15", "15/02/2024", "15-02-2024"...
# format="mixed" = pandas detecte le format ligne par ligne.
# dayfirst=True force l'interpretation europeenne ("15/02" = 15 fev).
df["Date_inscription"] = pd.to_datetime(df["Date_inscription"], errors="coerce", dayfirst=True, format="%e/%f/%Y")

# ============================================================
# 5. Supprimer les lignes sans nom ou sans email valide
# ============================================================
# Un email valide contient au minimum un "@" et un "."
mask_email_ok = df["Email"].str.contains(r"@.+\.", regex=True, na=False)
df['is_mail'] = mask_email_ok
mask_nom_ok = df["Nom"].str.len() > 0

df = df[mask_email_ok & mask_nom_ok]


# ============================================================
# 6. Dedoublonner
# ============================================================
# Probleme : "alice DUPONT" et "alice dupont" sont le meme client
# mais avec des casses differentes. On normalise le nom dans une
# colonne temporaire juste pour la dedup, puis on la jette.
df["_nom_norm"] = df["Nom"].str.lower()
df = df.drop_duplicates(subset=["Email", "_nom_norm"], keep="first")
df = df.drop(columns=["_nom_norm",'is_mail'])

# ============================================================
# 7. Export
# ============================================================
sortie = Path("data/clients_propre.csv")
df.to_csv(sortie, index=False)

nb_final = len(df)
nb_supprimees = nb_original - nb_final

print(f"Lignes supprimees : {nb_supprimees}")
print(f"Lignes restantes  : {nb_final}")
print(f"Export OK : {sortie}")