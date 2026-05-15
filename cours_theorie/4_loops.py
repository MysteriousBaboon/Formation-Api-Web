# Boucle while
age = 0
limit = 18
while age < limit:
    print(age)
    age += 1

# while avec break
while True:
    reponse = input("Tape 'stop' pour quitter : ") # input permet de taper une commande dans le terminal
    if reponse == "stop":
        break

# Boucle for
list_human = ['Karen', 'Lucas', 'Carla', 'Billel', 'Lucas', 'Ulysse', 'Yanis']
for y in list_human: # y est une variable, on peut l'appeler comme on veut
    print(y)

# for avec range
for i in range(5):
    print(i)           # 0, 1, 2, 3, 4

# for avec enumerate
for index, nom in enumerate(list_human):
    print(f"{index} -> {nom}")

# for sur un dictionnaire
boulangeries = {"Paul": 1.20, "Marie": 0.90, "Jean": 1.00}
for nom, prix in boulangeries.items():
    print(f"{nom} : {prix}€")


# break / continue / pass
for i in range(10):
    if i == 3:
        continue    # saute le 3
    if i == 7:
        break       # arrête au 7
    print(i)        # 0, 1, 2, 4, 5, 6

# pass = ne rien faire (placeholder)
for i in range(5):
    if i == 3:
        pass        # TODO: gérer ce cas plus tard
    print(i)