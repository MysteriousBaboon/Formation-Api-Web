# Opérateurs arithmétiques
a = 5 + 2
b = 5 - 3
c = 5 * 2 # multiplication
d = 5 / 2 # divison
e = 5 // 2 # divison entiere 
f = 5 % 2 # modulo (reste)
g = 5 ** 2 # puissance


# Opérateurs d’affectation
x = 5
x += 2 # x = x+2
x -= 1 
x *= 3
x /= 2 # x = x / 2 
x //= 2
x %= 2
x **= 2 # etc

# Opérateurs de comparaison
# Renvoient toujours un booléen (True / False)
age = 16
majorite = 18
print(age == majorite)   # égal à 
print(age != majorite)   # différent de
print(age > majorite)    # supérieur
print(age < majorite)    # inférieur
print(age >= majorite)   # supérieur ou égal
print(age <= majorite)   # inférieur ou égal

# Opérateurs logiques
age = 20
a_permis = True

# and, les deux doivent etre vraies
peut_conduire = age >= 18 and a_permis

# or, au moins une doit etre vraie
doit_travailler = age < 15 or age > 65 

# not, inverse le booléen
est_mineur = not age >= 18

# Combinaison
peut_voter = age >= 18 and not est_mineur