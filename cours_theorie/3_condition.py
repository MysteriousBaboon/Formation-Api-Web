# if / elif / else
age = 20
majorite = 18

if age >= majorite: # Si
    print("Majeur")
else: # Sinon
    print("Mineur")

# Plusieurs conditions avec elif
note = 15
if note >= 16:
    print("Très bien")
elif note >= 14:
    print("Bien")
elif note >= 10:
    print("Passable")
else: # Si aucun des conditions si dessus vrai, on rentre dans celle la
    print("Insuffisant")

# Conditions combinées avec and / or / not
age = 25
a_permis = True
if age >= 18 and a_permis:
    print("Peut conduire")

if age < 12 or age > 65:
    print("Tarif réduit")

if not a_permis:
    print("Pas de permis")

# Vérifier l'appartenance avec in
liste_ages = [4, 10, 18, 20]
if 24 in liste_ages:
    print("Dedans")
else:
    print("Pas dedans")

# Syntaxe "one liner"
statut = "Majeur" if age >= 18 else "Mineur"

# match / case (Python 3.10)
is_majeur = "Oui"
match is_majeur:
    case "Oui":
        print("Oui")
    case "Non":
        print("Non")
    case _:          # _ = cas par défaut (comme else)
        print("Valeur inconnue")
