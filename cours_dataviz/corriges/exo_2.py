# Corrigé exo 2 — Le bon graphe pour la bonne donnée
import matplotlib.pyplot as plt
import pandas as pd

# --- Répartition d'un budget → camembert ---
postes = ["Salaires", "Marketing", "Loyer", "Logiciels", "Autres"]
montants = [45000, 12000, 8000, 5000, 3000]

plt.figure(figsize=(7, 7))
plt.pie(montants, labels=postes, autopct="%1.1f%%")
plt.title("Répartition du budget", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("budget.png", dpi=150)
plt.close()

# --- Comparaison de 2 séries → barres groupées (via pandas) ---
annees = ["2024", "2025", "2026"]
ca_france = [120, 150, 180]
ca_export = [40, 55, 90]

df = pd.DataFrame({"France": ca_france, "Export": ca_export}, index=annees)
df.plot(kind="bar", figsize=(8, 5), title="CA France vs Export")
plt.ylabel("CA (k€)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("ca_compare.png", dpi=150)
plt.close()

print("budget.png et ca_compare.png générés.")