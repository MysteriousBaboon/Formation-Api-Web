# Methods

# Les methodes sont des fonctions rattaches a la variable appelable en utilisant '.'
name = "Mark"
print(name.upper())              # "MARK"
print(name.lower())              # "mark"
print(name.capitalize())         # "Mark"
print(name.casefold())           # "mark" (comme lower mais plus agressif, gère les accents)
print(name.replace('M', 'W'))    # "Wark"
print(name.startswith('Ma'))     # True
print(name.endswith('rk'))       # True
print(name.find('ar'))           # 1 (index où ça commence, -1 si pas trouvé)
print(name.count('a'))           # 1

# Chainage de méthodes
print(name.replace('M', 'W').casefold().capitalize())  # "Wark"

# strip : enlever les espaces
texte = "   hello   "
print(texte.strip())             # "hello"
print(texte.lstrip())            # "hello   "
print(texte.rstrip())            # "   hello"

# split / join
long_string = "Bonjour, j' ai comme employe. Mark/Jeremy/Robert/Patrique"
print(long_string.split('.'))                  # coupe sur le '.'
print(long_string.split('.')[1].split('/'))    # ['Mark', 'Jeremy', 'Robert', 'Patrique']

noms = ['Mark', 'Jeremy', 'Robert']
print(' - '.join(noms))          # "Mark - Jeremy - Robert"
print(','.join(noms))            # "Mark,Jeremy,Robert"

# vérifications
print("123".isdigit())           # True
print("abc".isalpha())           # True
print("abc123".isalnum())        # True

# Attention au piege tuple vs string
new_text = "chose"
pas_string = "Ceci est:", new_text     # C'est un TUPLE pas un string
vrai_string = f"Ceci est: {new_text}"  # Ça c'est un string
print(type(pas_string))                # <class 'tuple'>
print(type(vrai_string))              # <class 'str'>


# Méthodes de LIST
list_letter = ['b', 'c', 'd', 'e']

# Ajouter
list_letter.append('Z')               # ajoute à la fin
list_letter.insert(0, 'a')            # insère à l'index 0
list_letter.extend(['X', 'Y'])        # ajoute plusieurs éléments

# Supprimer
list_letter.remove('Z')               # supprime par valeur (le premier trouvé)
dernier = list_letter.pop()            # retire et renvoie le dernier
premier = list_letter.pop(0)           # retire et renvoie l'index 0
list_letter.clear()                    # vide la liste

# Trier
list_letter = ['b', 'c', 'a', 'd']
list_letter.sort()                     # tri croissant en place
list_letter.sort(reverse=True)         # tri décroissant en place
list_letter.reverse()                  # inverse l'ordre

# Chercher
nombres = [1, 2, 3, 2, 4, 2]
print(nombres.index(3))               # 2 (index de la première occurrence)
print(nombres.count(2))               # 3 (combien de fois 2 apparaît)

# Copier
copie = nombres.copy()                # copie indépendante


# Méthodes de DICT
boulangeries = {
    "Paul": 1.20,
    "Marie": 0.90,
    "Jean": 1.00
}

# Accéder
print(boulangeries["Paul"])            # 1.20 (erreur si clé absente)
print(boulangeries.get("Luc", "Personne"))      # Personne (valeur par défaut si absent)

# Ajouter / modifier
boulangeries["Luc"] = 1.10            # ajoute une nouvelle clé
boulangeries.update({"Paul": 1.30, "Nadia": 0.95})  # met à jour plusieurs

# Supprimer
boulangeries.pop("Jean")              # retire et renvoie la valeur
del boulangeries["Luc"]               # supprime directement

# Parcourir
print(boulangeries.keys())            # les clés
print(boulangeries.values())          # les valeurs
print(boulangeries.items())           # les paires (clé, valeur)

for nom, prix in boulangeries.items():
    print(f"{nom} : {prix}€")

# Autres
print(len(boulangeries))              # nombre de clés
copie_dict = boulangeries.copy()


# Méthodes de SET
fruits = {'pomme', 'banane', 'cerise'}

fruits.add('kiwi')                     # ajouter un élément
fruits.discard('banane')               # supprimer (pas d'erreur si absent)
fruits.remove('cerise')                # supprimer (erreur si absent)

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a.union(set_b))             # {1, 2, 3, 4, 5, 6}
print(set_a.intersection(set_b))      # {3, 4}
print(set_a.difference(set_b))        # {1, 2}


# Méthodes de TUPLE
# Les tuples sont immuables (La variable ne peut pas etre modifie directement), donc très peu de méthodes
mon_tuple = (1, 2, 3, 2, 4, 2)
print(mon_tuple.count(2))             # 3
print(mon_tuple.index(3))             # 2
# C'est tout. On ne peut pas modifier un tuple