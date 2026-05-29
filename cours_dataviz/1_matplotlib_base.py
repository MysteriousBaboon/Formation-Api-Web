# ============================================================
# 1_matplotlib_base.py — Les bases de matplotlib
# ============================================================
# matplotlib = LA librairie de graphiques en Python.
# Le schéma est toujours le même :
#     données  →  plt.qqchose(...)  →  plt.show()
# ============================================================

import matplotlib.pyplot as plt

# ------------------------------------------------------------
# 1. Une courbe (line plot) → évolution dans le temps
# ------------------------------------------------------------
mois = ["Jan", "Fev", "Mar", "Avr", "Mai"]
ventes = [100, 130, 90, 160, 200]

plt.plot(mois, ventes)
plt.title("Ventes 2026", loc="left")
plt.xlabel("Mois")
plt.ylabel("Ventes (k€)")
plt.show()   # ouvre une fenêtre — ferme-la pour passer à la suite

# ------------------------------------------------------------
# 2. Des barres → comparer des catégories
# ------------------------------------------------------------
regions = ["Nord", "Sud", "Est", "Ouest"]
ca = [1200, 1700, 900, 1400]

plt.bar(regions, ca)
plt.title("Chiffre d'affaires par région")
plt.show()

# ------------------------------------------------------------
# 3. Barres horizontales → pratique quand les noms sont longs
# ------------------------------------------------------------
plt.barh(regions, ca)
plt.title("CA par région (horizontal)")
plt.show()

# ------------------------------------------------------------
# 4. Un camembert → répartition (parts d'un tout)
# ------------------------------------------------------------
# Garde max 5-6 parts, sinon c'est illisible.
plt.pie(ca, labels=regions, autopct="%1.1f%%")  # autopct = afficher les %
plt.title("Répartition du CA")
plt.show()

# ------------------------------------------------------------
# 5. Un nuage de points → relation entre 2 variables
# ------------------------------------------------------------
budget_pub = [10, 20, 30, 40, 50]
ventes_pub = [100, 180, 250, 280, 360]

plt.scatter(budget_pub, ventes_pub)
plt.title("Ventes vs Budget pub")
plt.xlabel("Budget pub (k€)")
plt.ylabel("Ventes (k€)")
plt.show()

# ------------------------------------------------------------
# 6. Un histogramme → distribution d'une variable
# ------------------------------------------------------------
ages = [22, 25, 25, 30, 31, 31, 31, 35, 40, 41, 42, 50]
plt.hist(ages, bins=5)
plt.title("Distribution des âges")
plt.show()

# ------------------------------------------------------------
# RÈGLE DE CHOIX
# ------------------------------------------------------------
# Évolution dans le temps  → plt.plot   (courbe)
# Comparer des catégories  → plt.bar    (barres)
# Répartition d'un tout    → plt.pie    (camembert)
# Relation entre 2 mesures → plt.scatter(nuage)
# Distribution            → plt.hist   (histogramme)