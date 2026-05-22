# ============================================================
# 6_regex.py — Les expressions regulieres en Python
# ============================================================
# Une regex = un mini-langage pour decrire un motif de texte.
# Utile pour : extraire, valider, remplacer, nettoyer.
#
# Tu utilises la lib `re` du standard (rien a installer).
#
# Cheat-sheet minimale :
#   \d  un chiffre              \D  pas un chiffre
#   \w  une lettre/chiffre/_    \W  l'inverse
#   \s  un espace               \S  pas un espace
#   .   n'importe quel char     +   1 ou plus
#   *   0 ou plus               ?   0 ou 1 (optionnel)
#   ^   debut de chaine         $   fin de chaine
#   [abc] un char parmi a/b/c   [^abc] tout sauf a/b/c
#   ( )  groupe de capture      |   ou
# ============================================================

import re


# ============================================================
# 1. Les 3 fonctions de base : search, match, findall
# ============================================================
texte = "Mon numero de commande est 2025-042 et coute 1500 EUR"

# search = cherche LE PREMIER match n'importe ou dans la chaine
m = re.search(r"\d+", texte)
print(f"search       : {m.group()}")      # "2025"

# match = ne marche QUE si le motif est au DEBUT de la chaine
print(f"match au debut : {re.match(r'\d+', texte)}")   # None
print(f"match 'Mon'    : {re.match(r'Mon', texte)}")   # objet match

# findall = renvoie TOUS les matchs, sous forme de liste
print(f"findall      : {re.findall(r'\d+', texte)}")   # ['2025', '042', '1500']


# ============================================================
# 2. Groupes de capture — extraire des bouts precis
# ============================================================
# Les parentheses () disent : "memorise ce bout-la".
# .group(0) = tout le match, .group(1) = 1er groupe, etc.
print("\n--- Groupes ---")

ligne = "Facture #2025-042 du 14/05/2026"
m = re.search(r"Facture\s*#?([\w-]+)\s*du\s*(\d{2}/\d{2}/\d{4})", ligne)
if m:
    print(f"Match complet : {m.group(0)}")
    print(f"Numero        : {m.group(1)}")
    print(f"Date          : {m.group(2)}")


# ============================================================
# 3. Groupes nommes — plus lisible quand il y en a plusieurs
# ============================================================
# Syntaxe : (?P<nom>...) au lieu de juste (...)
print("\n--- Groupes nommes ---")

m = re.search(
    r"(?P<num>\d{4}-\d{3})\s*du\s*(?P<date>\d{2}/\d{2}/\d{4})",
    ligne,
)
if m:
    print(m.groupdict())   # {'num': '2025-042', 'date': '14/05/2026'}


# ============================================================
# 4. Validation — email, telephone, code postal
# ============================================================
# Les regex "parfaites" pour email font 1000 caracteres.
# Pour 95% des cas, cette version simple suffit largement.
print("\n--- Validation ---")

REGEX_EMAIL = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"
REGEX_TEL_FR = r"^0[1-9](?:[\s.-]?\d{2}){4}$"   # 06 11 22 33 44, 06.11..., 0611...
REGEX_CP = r"^\d{5}$"

emails = ["alice@mail.com", "pas-un-email", "bob.dupont+test@ma-boite.fr"]
for e in emails:
    ok = bool(re.match(REGEX_EMAIL, e))
    print(f"  {e:35s} -> {'OK' if ok else 'KO'}")

tels = ["06 11 22 33 44", "0611223344", "06.11.22.33.44", "123"]
for t in tels:
    ok = bool(re.match(REGEX_TEL_FR, t))
    print(f"  {t:20s} -> {'OK' if ok else 'KO'}")


# ============================================================
# 5. Extraction structuree — parser une facture en texte
# ============================================================
# Cas typique : tu as un texte (PDF, mail, log) et tu veux en
# sortir un dict propre.
print("\n--- Parsing facture ---")

facture = """
Facture#2025-042
Date : 14 mai 2026
Client : Acme Corp

TOTAL HT : 1250.00 EUR
TVA 20% : 250.00 EUR
TOTAL TTC : 1500.00 EUR
"""

infos = {
    "numero": re.search(r"Facture\s*#?([\w-]+)", facture).group(1),
    "date":   re.search(r"Date\s*:\s*(.+)", facture).group(1).strip(),
    "ht":     float(re.search(r"TOTAL HT\s*:\s*([\d.]+)", facture).group(1)),
    "tva":    float(re.search(r"TVA[^:]*:\s*([\d.]+)", facture).group(1)),
    "ttc":    float(re.search(r"TOTAL TTC\s*:\s*([\d.]+)", facture).group(1)),
}
print(infos)


# ============================================================
# 6. Substitution — re.sub pour remplacer / nettoyer
# ============================================================
# Cas tres frequent : retirer du HTML, masquer des donnees, etc.
print("\n--- Substitution ---")

# Retirer toutes les balises HTML
html = "<p>Bonjour <b>Alice</b>, ton solde est de <span>1500</span> EUR.</p>"
sans_html = re.sub(r"<[^>]+>", "", html)
print(f"Sans HTML : {sans_html}")

# Masquer un numero de carte (12 premiers chiffres -> X)
texte_cb = "Ma carte est 4532 1234 5678 9876"
masque = re.sub(r"\d{4}\s\d{4}\s\d{4}\s(\d{4})", r"XXXX XXXX XXXX \1", texte_cb)
print(f"Masquee   : {masque}")

# Normaliser les espaces multiples en un seul
sale = "trop     d'espaces       partout"
propre = re.sub(r"\s+", " ", sale)
print(f"Propre    : '{propre}'")


# ============================================================
# 7. Flags utiles — IGNORECASE, MULTILINE
# ============================================================
print("\n--- Flags ---")

# re.IGNORECASE : insensible a la casse
print(re.findall(r"python", "Python python PYTHON pYtHoN", flags=re.IGNORECASE))

# re.MULTILINE : ^ et $ matchent chaque debut/fin de ligne
log = """ERROR connexion refusee
INFO traitement ok
ERROR timeout
INFO fin"""
erreurs = re.findall(r"^ERROR.*$", log, flags=re.MULTILINE)
print(f"Erreurs trouvees : {erreurs}")


# ============================================================
# 8. Regex compilee — quand tu vas la reutiliser souvent
# ============================================================
# Si tu utilises la meme regex dans une boucle sur 10 000 lignes,
# compile-la une fois. Plus rapide et plus lisible.
print("\n--- Regex compilee ---")

PATTERN_PRIX = re.compile(r"(\d+(?:[.,]\d{2})?)\s*EUR")

annonces = [
    "PC portable a 999.99 EUR",
    "Souris : 25 EUR",
    "Casque audio (149,90 EUR) — promo",
    "Rien a vendre ici",
]

for a in annonces:
    m = PATTERN_PRIX.search(a)
    print(f"  {a:40s} -> {m.group(1) if m else '(pas de prix)'}")


# ============================================================
# 9. PIEGE classique : greedy vs non-greedy
# ============================================================
# Par defaut, + et * sont GLOUTONS : ils prennent le plus possible.
# Ajoute un ? pour les rendre paresseux (non-greedy).
print("\n--- Greedy ---")

html = "<b>gras</b> et <i>italique</i>"

# Glouton : prend tout entre le PREMIER < et le DERNIER >
print("Glouton    :", re.findall(r"<.+>", html))
# Paresseux : prend le moins possible (= une seule balise a la fois)
print("Paresseux  :", re.findall(r"<.+?>", html))


# ============================================================
# 10. Bonus — re.finditer pour iterer avec contexte
# ============================================================
# findall renvoie juste les strings. finditer renvoie les objets
# match complets : tu as la position, le texte autour, etc.
print("\n--- finditer ---")

texte = "Cmd 2025-001 a 150 EUR, Cmd 2025-002 a 250 EUR, Cmd 2025-003 a 75 EUR"

for m in re.finditer(r"Cmd (\d{4}-\d{3}) a (\d+) EUR", texte):
    num, montant = m.group(1), m.group(2)
    print(f"  Position {m.start():3d} : commande {num} = {montant} EUR")


# ============================================================
# Conseils generaux
# ============================================================
# 1. Teste tes regex sur https://regex101.com (mode Python) avant
#    de les coller dans ton code. Ca explique chaque token.
#
# 2. Si tu te retrouves a ecrire une regex de 200 caracteres,
#    c'est probablement le mauvais outil. Pour parser du HTML
#    serieusement, utilise BeautifulSoup. Pour du JSON, json.loads.
#
# 3. Toujours mettre tes regex dans des CONSTANTES en haut du
#    fichier (REGEX_EMAIL, PATTERN_PRIX...). Plus lisible, plus
#    facile a tester.
#
# 4. Utilise des raw strings (r"...") pour eviter de doubler les
#    backslashes. r"\d+" est equivalent a "\\d+" mais bien plus lisible.
# ============================================================