def print_name(name_):
    print(name_)

def can_drink(age_, age_level_=18):
    if age_ > age_level_:
        return True
    else:
        return False

def calculate_estimated_threat(threat_):
    return threat_ * 9000

list_users = []
for i in range(3):
    print(f"Utilisateur {i}")
    name = input("Quel est ton nom ?")
    age = input ("Quel est ton age ?")
    threat = input("A quel point est tu dangereux sur 0/1")
    is_usa = input("Etes vous aux USA ? Oui/Non").lower()


    if is_usa == 'oui':
        age_level = 21
    elif is_usa == 'non':
        age_level = 18
    else:
        print("USA n'est pas dans le bon format")
        break 

    my_dict = {"Nom":name, "Age": int(age), "Dangerosite":float(threat)}

    print_name(my_dict['Nom'])

    if can_drink(my_dict['Age'], age_level):
        print('Peut boire')
    else:
        print("ne peut pas boire")

    print(calculate_estimated_threat(my_dict["Dangerosite"]))

