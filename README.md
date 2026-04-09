# 🐍 Mon Premier Projet Flask

Bienvenue ! Ce projet est conçu pour t'apprendre les bases de Flask,
un micro-framework Python pour créer des sites web et des API.

## 📁 Structure du projet

```
flask_projet_debutant/
├── app.py              ← Le fichier principal (c'est ici que tout se passe)
├── requirements.txt    ← Les dépendances (librairies nécessaires)
├── README.md           ← Ce fichier d'aide
├── templates/          ← Les pages HTML (ce que l'utilisateur voit)
│   ├── base.html       ← Le template de base (layout commun)
│   ├── accueil.html    ← La page d'accueil
│   └── salut.html      ← La page de salutation
└── static/             ← Les fichiers statiques (CSS, images, JS)
    └── style.css       ← Le style du site
```

## 🚀 Comment lancer le projet

### 1. Installer Python
Vérifie que Python 3 est installé :
```bash
python3 --version
```

### 2. Créer un environnement virtuel (recommandé)
```bash
python3 -m venv venv
source venv/bin/activate        # Sur Mac/Linux
# ou
venv\Scripts\activate           # Sur Windows
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Lancer l'application
```bash
python app.py
```

### 5. Ouvrir dans le navigateur
Va sur : **http://127.0.0.1:5000**

## 📚 Concepts abordés

- **Les routes** : comment associer une URL à une fonction
- **Les templates** : comment afficher du HTML dynamique
- **Les formulaires** : comment récupérer les données de l'utilisateur
- **Les fichiers statiques** : comment ajouter du CSS
- **Une mini API** : comment renvoyer du JSON

## 💡 Exercices pour aller plus loin

1. Ajoute une page `/about` qui affiche une description de toi
2. Modifie le formulaire pour demander aussi l'âge
3. Crée une route `/api/heure` qui renvoie l'heure actuelle en JSON
4. Ajoute une image dans le dossier `static/` et affiche-la sur la page d'accueil
