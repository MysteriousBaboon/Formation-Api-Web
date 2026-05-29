# Corrigé exo 1 — Premier graphe propre
import matplotlib.pyplot as plt

mois = ["Jan", "Fev", "Mar", "Avr", "Mai", "Juin"]
visiteurs = [1200, 1500, 1100, 1800, 2100, 2500]

plt.figure(figsize=(9, 5))
plt.plot(mois, visiteurs, marker="o", color="#2563eb", linewidth=2)
plt.title("Visiteurs par mois", fontsize=14, fontweight="bold")
plt.xlabel("Mois")
plt.ylabel("Visiteurs")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("visiteurs.png", dpi=150, bbox_inches="tight")
plt.close()

print("visiteurs.png généré.")