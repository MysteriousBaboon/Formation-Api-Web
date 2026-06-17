# ============================================================
# 1_perceptron_numpy.py — Un neurone CODÉ À LA MAIN qui apprend
# ============================================================
# Pas de bibliothèque magique ici : on code un perceptron (le neurone
# historique de 1958) avec juste numpy, pour DÉMYSTIFIER l'apprentissage.
#
# Tu vas voir, en clair :
#   - les POIDS et le BIAIS s'ajuster tout seuls
#   - l'erreur diminuer à chaque passage (epoch)
#   - et la LIMITE célèbre : un seul neurone ne sait pas faire "XOR"
#     → c'est EXACTEMENT pourquoi le deep learning empile des couches.
#
# Lancement :   python 1_perceptron_numpy.py
# ============================================================

import numpy as np


class Perceptron:
    """Un seul neurone : sortie = step(poids · entrées + biais)."""

    def __init__(self, n_entrees, taux=0.1):
        self.poids = np.zeros(n_entrees)   # on démarre à zéro
        self.biais = 0.0
        self.taux = taux                   # le "pas" d'apprentissage

    def _activation(self, somme):
        # Fonction "marche" : 1 si la somme dépasse 0, sinon 0
        return 1 if somme >= 0 else 0

    def predire(self, x):
        return self._activation(np.dot(self.poids, x) + self.biais)

    def entrainer(self, X, y, epochs=10, bavard=True):
        for epoch in range(1, epochs + 1):
            erreurs = 0
            for xi, cible in zip(X, y):
                prediction = self.predire(xi)
                erreur = cible - prediction          # 0 si juste, +1 ou -1 sinon
                if erreur != 0:
                    # LA règle d'apprentissage : pousser les poids vers la bonne réponse
                    self.poids += self.taux * erreur * xi
                    self.biais += self.taux * erreur
                    erreurs += 1
            if bavard:
                print(f"  epoch {epoch:>2} | erreurs : {erreurs} | "
                      f"poids = {np.round(self.poids, 2)} | biais = {round(self.biais, 2)}")
            if erreurs == 0:
                if bavard:
                    print("  → 0 erreur : le neurone a CONVERGÉ. 🎉")
                break


def evaluer(nom, X, y, epochs=12):
    print(f"\n=== {nom} ===")
    p = Perceptron(n_entrees=X.shape[1], taux=0.1)
    p.entrainer(X, y, epochs=epochs)
    justes = sum(p.predire(xi) == cible for xi, cible in zip(X, y))
    print(f"  Résultat : {justes}/{len(y)} bonnes réponses")
    return justes == len(y)


# Entrées possibles de 2 bits : (0,0), (0,1), (1,0), (1,1)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# ------------------------------------------------------------
# 1. Le OU logique (OR) — linéairement séparable → le neurone y arrive
# ------------------------------------------------------------
y_or = np.array([0, 1, 1, 1])     # vrai dès qu'au moins une entrée est à 1
ok_or = evaluer("Apprendre le OU logique (OR)", X, y_or)

# ------------------------------------------------------------
# 2. Le ET logique (AND) — aussi séparable → ça marche aussi
# ------------------------------------------------------------
y_and = np.array([0, 0, 0, 1])    # vrai seulement si les deux sont à 1
ok_and = evaluer("Apprendre le ET logique (AND)", X, y_and)

# ------------------------------------------------------------
# 3. Le OU EXCLUSIF (XOR) — PAS séparable → un seul neurone ÉCHOUE
# ------------------------------------------------------------
y_xor = np.array([0, 1, 1, 0])    # vrai si UNE SEULE des deux est à 1
ok_xor = evaluer("Apprendre le OU EXCLUSIF (XOR)", X, y_xor)

# ------------------------------------------------------------
# La morale de l'histoire
# ------------------------------------------------------------
print("\n" + "=" * 60)
print(f"OR  appris ? {ok_or}   |   AND appris ? {ok_and}   |   XOR appris ? {ok_xor}")
print("Un SEUL neurone ne peut séparer que par une droite. XOR n'est pas")
print("séparable par une droite → il échoue. La solution : EMPILER des couches.")
print("C'est précisément l'idée du DEEP LEARNING (voir la démo 2).")

# ------------------------------------------------------------
# 🔧 À TOI DE JOUER
# ------------------------------------------------------------
# 1. Change le taux d'apprentissage (taux=0.5 puis 0.01). La vitesse de convergence change ?
# 2. Pour XOR, augmente epochs=100 : le neurone finit-il par y arriver ? (non, et c'est normal)
# 3. Invente ta propre table de vérité (y = ...) et regarde si elle est apprenable.
