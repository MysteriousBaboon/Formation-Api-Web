class GreaterThanTen(Exception):
    def __init__(self, message="Supérieur à 10"):
        super().__init__(message)


user_input = input("Valeur entre 0/10")

try:
    input_converted = int(user_input)
    if input_converted > 10:
        raise GreaterThanTen
        # ou
        raise Exception("Ceci est aussi une erreur custom")
except ValueError:
    print("Erreur : Le type de la variable doit etre un chiffre")
except Exception as e:
    print(f"Erreur: Nouvelle erreur non repertorie : {e}")
    
print('Fin de script')