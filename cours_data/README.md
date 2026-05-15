# Python = ton couteau suisse anti-Excel

Manipuler des fichiers et des données avec Python : CSV, Excel, JSON, PDF, et automatisation de tâches sur des dossiers.

## 🎯 Objectifs

À la fin de ce module, tu seras capable de :

- Lire / écrire des fichiers **CSV** et **Excel** sans souffrir
- Nettoyer un dataset crade avec **pandas**
- Manipuler des fichiers et dossiers en masse avec **pathlib**
- Extraire du texte de **PDF**
- Automatiser des tâches répétitives que ferait un stagiaire pendant 3 jours

## 📁 Structure

```
cours_data/
├── README.md            ← Ce fichier
├── cours.md             ← Cours complet et concepts
├── requirements.txt     ← Librairies à installer
├── 0_setup.py           ← Génère les fichiers d'exemple
├── 1_csv.py             ← Lire/écrire un CSV
├── 2_pandas.py          ← Pandas pour nettoyer
├── 3_excel.py           ← Lire/écrire un Excel
├── 4_pathlib.py         ← Manipuler fichiers & dossiers
├── 5_pdf.py             ← Extraire du texte d'un PDF
├── exos.md              ← Exercices (3h)
└── data/                ← Fichiers générés par 0_setup.py
```

## 🚀 Setup

```bash
python3 -m venv .venv
source .venv/bin/activate          # Linux/Mac
# .venv\Scripts\activate            # Windows

pip install -r requirements.txt
python 0_setup.py                  # Génère les fichiers d'exemple
```

Puis lis `cours.md`, parcours les fichiers numérotés dans l'ordre, et attaque `exos.md`.
