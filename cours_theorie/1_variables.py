# Integer # Int
prix_baguette_de_pain = 50000
# Float
prix_baguette_precise = 0.40 
# String
prix_baguette_text = "Ceci est un texte, 'ceci' est un texte"
# Boolean
is_my_baguette_cooked = False 
# None (valeur vide)
empty = None 

# List
prix_baguettes_de_mon_quartier = [0.90, 0.50, 0.30, 2]
# Acceder a un element
prix_baguettes_de_mon_quartier[0]
# Dict 
prix_baguettes_quartier_par_nom = {"boulangerie 1" : 0.90,
                                    "boulangerie 2" : 0.70, "is_boulangerie 1" : True}
# Acceder a un element
prix_baguettes_quartier_par_nom['boulangerie 1']

# List et Dict peuvent contenir des types de variables differents. Exemple, chiffre et texte
list_test = [0.90, '2']
dict_test = {"test 1" : 0.90, "test 2" : '2'}

# Tuples
binomes = ('binome 1', 'binome 2')
# Set (pas de doublon)
binomes_set = {'binome 1', 'binone 2', 'binome 3', 'binome 1'} 
print(binomes_set) 

# Conversion d'un type de variable vers un autre int, str, dict, list, bool, set, tuple
prix_baguette_de_pain = int(prix_baguette_precise)

# Slicing de listes
list_floors = [0, 1, 2, 3 ,4, 5, 6, 7, 8, 9, 10]

print(list_floors[:5]) # Jusqu'au cinquieme element
print(list_floors[0:10:2]) # A aprtir de l'element 0 jusqu'au 10 en passant de 2 par 2

# Les string en python peuvent etre considere comme des listes de lettres
intro = "Bonjour je m'appelle Mark"
print(intro[0::2])

# Inserer une variable dans une string
prenom = "Mark"
prix = 0.90
f_string = f"La baguette de {prenom} coûte {prix} euros"
print(f_string)