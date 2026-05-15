# Modules
# Import classique (tout le module)
import random
import math
import os

print(random.randint(0, 5000))
print(math.sqrt(16))
print(os.getcwd())

# Import avec alias
import math as mt
import datetime as dt

print(mt.pi)
print(dt.datetime.now())

# Import d'une ou plusieurs fonctions
from random import randint, choice
from math import sqrt, pi

print(randint(0, 100))     # pas besoin de random.randint()
print(sqrt(25))
print(pi)

# Import de tout (déconseillé)
from math import *
print(cos(0))              # marche mais on sait plus d'où ça vient


### Import de ses fichiers
# Structure du projet :
# mon_projet/
# ├── 7_modules.py
# ├── functions_mark.py
# └── module/
#     ├── __init__.py         <- fichier vide obligatoire
#     ├── functions_mark.py
#     └── function_2.py

# Import d'un fichier au même niveau
import functions_mark
functions_mark.add(5, 5)

# Import d'une fonction depuis un fichier
from functions_mark import add
add(5, 5)

# Import depuis un sous-dossier (package / module)
from module import functions_mark, function_2
functions_mark.add(5, 5)

# Import d'une fonction depuis un sous-dossier
from module.functions_mark import add
from module.function_2 import ma_fonction
add(5, 5)