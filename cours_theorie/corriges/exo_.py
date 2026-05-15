def creer_personne():
    nom = str(input("Entrez votre nom : "))
    age = int(input("Entrez votre âge : "))
    dangerosite = float(input("Entrez votre dangerosité : "))

    personne = {
        "Nom": nom,
        "Age": age,
        "Dangerosité": dangerosite
    }

    return personne


def afficher_nom(personne):
    nom = personne["Nom"]
    print("La personne concernée s'appelle "+nom)

def peut_boire(personne):
    age = personne["Age"]
    if (age>=18):
        print("ui tu peux boire :)")
    else:
        print("tu peux pas boire dsl, mais tu pourras bientôt :)")

personnes = []
for i in range(3):
    personne = creer_personne()
    afficher_nom(personne['name'])
    personnes.append(personne)
    
print(personnes)

# afficher_nom(personne)
# peut_boire(personne)