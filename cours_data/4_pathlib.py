# ============================================================
# 4_pathlib.py — Manipuler fichiers et dossiers proprement
# ============================================================
# pathlib remplace l'ancien `os.path`. C'est la nouvelle facon
# recommandee de gerer des chemins de fichiers en Python.
# ============================================================

from pathlib import Path


# ============================================================
# 1. Creer un objet Path
# ============================================================
data = Path("data")

print("Le dossier existe ?", data.exists())
print("C'est un dossier ?", data.is_dir())
print("Chemin absolu :", data.resolve())


# ============================================================
# 2. Lister des fichiers
# ============================================================
print("\nTous les CSV de data/ :")
for f in data.glob("*.csv"):
    print(f" - {f.name}  ({f.stat().st_size} octets)")

print("\nTous les fichiers (recursif) :")
for f in data.rglob("*"):
    if f.is_file():
        print(f" - {f.relative_to(data)}")


# ============================================================
# 3. Renommer en masse — cas typique d'automatisation
# ============================================================
# Imagine : un dossier de 200 photos a renommer.
# A la main = 1h. En Python = 5 secondes.

dossier = data / "fichiers_a_renommer"
print(f"\nFichiers a renommer dans {dossier} :")
for f in dossier.iterdir():
    print(f"  {f.name}")

print("\nRenommage : extensions en minuscules + prefixe...")
for f in dossier.iterdir():
    # On veut : IMG_1234.JPG -> photo_img_1234.jpg
    nouveau_nom = "photo_" + f.stem.lower() + f.suffix.lower()
    nouveau_chemin = f.with_name(nouveau_nom)
    f.rename(nouveau_chemin)

print("Apres renommage :")
for f in dossier.iterdir():
    print(f"  {f.name}")


# ============================================================
# 4. Creer / supprimer des dossiers
# ============================================================
output = Path("data/output")
output.mkdir(exist_ok=True)
# exist_ok=True : ne plante pas si le dossier existe deja

# Ecrire un fichier dedans
(output / "hello.txt").write_text("Salut !")

# Lire un fichier
contenu = (output / "hello.txt").read_text()
print(f"\nContenu lu : {contenu}")


# ============================================================
# 5. Operations utiles
# ============================================================
chemin = Path("data/ventes.csv")
print(f"\nInfos sur {chemin} :")
print(f"  Nom complet      : {chemin.name}")
print(f"  Nom sans ext     : {chemin.stem}")
print(f"  Extension        : {chemin.suffix}")
print(f"  Dossier parent   : {chemin.parent}")
print(f"  Taille (octets)  : {chemin.stat().st_size}")


# ============================================================
# 6. Le pattern "trier les fichiers par type"
# ============================================================
# Cas reel : "j'ai un dossier Telechargements avec 500 fichiers
# en vrac, je veux les ranger par type"

print("\n--- Demo de tri par extension ---")
tri = data / "tri_par_type"
tri.mkdir(exist_ok=True)

for f in dossier.iterdir():
    if not f.is_file():
        continue
    ext = f.suffix.lower().lstrip(".") or "sans_extension"
    sous_dossier = tri / ext
    sous_dossier.mkdir(exist_ok=True)
    # NB : ici on COPIERAIT, mais comme c'est de la demo on
    # ne fait que l'afficher. Decommente pour vraiment deplacer :
    # f.rename(sous_dossier / f.name)
    print(f"  {f.name} -> irait dans {sous_dossier}/")
