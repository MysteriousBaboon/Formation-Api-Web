# ============================================================
# 2_mlp_sklearn_digits.py — Un mini-réseau qui RECONNAÎT des chiffres
# ============================================================
# De la vraie computer vision, en version légère : on entraîne un petit
# réseau de neurones (MLP = Multi-Layer Perceptron, plusieurs couches)
# à reconnaître des chiffres manuscrits 8×8 pixels.
#
# Contrairement à la démo 1 (un seul neurone), ici on a PLUSIEURS COUCHES
# → le réseau peut apprendre des motifs complexes (les formes des chiffres).
#
# Le script génère une image : predictions.png
#
# Lancement :   python 2_mlp_sklearn_digits.py
# ============================================================

import matplotlib
matplotlib.use("Agg")            # backend "fichier" : pas besoin d'écran
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# ------------------------------------------------------------
# 1. Les données : 1797 images 8×8 de chiffres écrits à la main
# ------------------------------------------------------------
digits = load_digits()
X = digits.data       # chaque image "aplatie" en 64 nombres (8×8 pixels)
y = digits.target     # le vrai chiffre (0 à 9)
print(f"{len(X)} images de {X.shape[1]} pixels (8×8), chiffres de 0 à 9")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# ------------------------------------------------------------
# 2. Le réseau : 2 couches cachées (64 puis 32 neurones)
# ------------------------------------------------------------
# hidden_layer_sizes=(64, 32) = "profond" : l'info traverse 2 couches cachées.
reseau = MLPClassifier(
    hidden_layer_sizes=(64, 32),
    max_iter=600,
    random_state=42,
)
print("Entraînement du réseau... (quelques secondes)")
reseau.fit(X_train, y_train)

# ------------------------------------------------------------
# 3. Évaluer sur les images jamais vues
# ------------------------------------------------------------
y_pred = reseau.predict(X_test)
print(f"Précision sur le test : {accuracy_score(y_test, y_pred):.2%}")
print(f"Le réseau a {reseau.n_layers_} couches au total (entrée + cachées + sortie).")

# ------------------------------------------------------------
# 4. Visualiser 10 prédictions (vert = juste, rouge = faux)
# ------------------------------------------------------------
fig, axes = plt.subplots(2, 5, figsize=(10, 4.5))
for ax, image, vrai, predit in zip(
    axes.ravel(), X_test, y_test, y_pred
):
    ax.imshow(image.reshape(8, 8), cmap="gray_r")
    couleur = "green" if vrai == predit else "red"
    ax.set_title(f"prédit : {predit}", color=couleur, fontsize=11)
    ax.axis("off")

fig.suptitle("Un réseau de neurones lit des chiffres manuscrits", fontsize=13)
plt.tight_layout()
plt.savefig("predictions.png", dpi=110, bbox_inches="tight")
print("✅ Image générée : predictions.png (ouvre-la pour voir le réseau en action)")

# ------------------------------------------------------------
# 🔧 À TOI DE JOUER
# ------------------------------------------------------------
# 1. Mets hidden_layer_sizes=(4,) (un tout petit réseau). La précision chute-t-elle ?
# 2. Mets hidden_layer_sizes=(128, 64, 32) (plus profond). Gagne-t-on beaucoup ?
# 3. Repère sur l'image un chiffre mal prédit : avec quel autre chiffre est-il confondu ?
