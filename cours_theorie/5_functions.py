# Definition de fonctions
def add(number_1, number_2): # Argument obligatoire / Positionnel
    """
    This is a function Docstring, it is used to give documentation about the function
    Takes number_1 and add it to number_2
    """
    return number_1 + number_2 # Le return permet de passer ce resultat au = de la fonction

def substract_by(number_1, number_2=1): # Argument optionnel
    """
    This is a function Docstring
    Takes number_1 and substract it to number_2. If number_2 is not given, it will instead substract by 1.
    """
    return number_1 - number_2

value_returned = add(3,4) 
print(value_returned)
value_returned = substract_by(4,3) 
print(value_returned)
value_returned = substract_by(4)  # Le second argument n'est pas obligatoire
print(value_returned)
value_returned = substract_by(4, number_2=5)
print(value_returned)


# Exemples de fonctions integrees a python
list_number = [3, 4, 5, 6]
print(len(list_number))          # Donne la taille de la liste. 4
print(type(list_number))         # Donne le type de la variabl.e <class 'list'>
print(sum(list_number))          # 18
print(min(list_number))          # 3
print(max(list_number))          # 6
print(sorted(list_number, reverse=True))  # [6, 5, 4, 3]
print(abs(-42))                  # Donne la valeur absolue de la variable. 42
print(round(3.14159, 2))        # 3.14
print(isinstance(42, int))      # Verifie que c'est le bon type de varaible. True