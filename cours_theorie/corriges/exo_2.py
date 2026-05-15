from exo_2_module import convert_to_second

user_input = input("donne moi un nombre de minutes")
secondes = convert_to_second(user_input)
secondes = convert_to_second(user_input, is_hour=False)
print(secondes)

user_input = input("donne moi un nombre d'heures")
secondes = convert_to_second(user_input, is_hour=True)
print(secondes)
