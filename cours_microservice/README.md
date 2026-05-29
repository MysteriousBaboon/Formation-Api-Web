# 🔌 Cours 3 — Construire ton micro-service Python pour n8n

Transformer Flask (déjà vu) en outil qui étend les capacités de n8n.

## 🎯 Objectifs

À la fin de ce module, tu seras capable de :

- Créer un **endpoint webhook** que n8n appelle
- Le sécuriser avec un **token d'authentification**
- Valider les données entrantes proprement
- Déployer ton service **en ligne** en 10 minutes (Render, gratuit)
- Connecter le tout depuis un workflow n8n

## 📁 Structure

```
cours_microservice/
├── README.md
├── cours.md               ← Cours complet
├── requirements.txt
├── .env.example
├── app.py                 ← Le serveur Flask complet
├── 1_endpoint_simple.py   ← Le webhook le plus basique
├── 2_auth_token.py        ← Avec authentification
├── 3_validation.py        ← Valider les données reçues
├── deploiement_render.md  ← Guide de déploiement
├── integration_n8n.md     ← Comment brancher dans n8n
├── exos.md                ← Exercices (3h)
└── templates/
    └── home.html          ← Petite UI de monitoring
```

## 🚀 Setup local

```bash
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

cp .env.example .env
# Edite le .env et mets un token long et aleatoire

python app.py
```

L'app tourne sur `http://127.0.0.1:5000`.

Test rapide :

```bash
curl http://127.0.0.1:5000/health
```

## 🌐 Mise en ligne

Voir `deploiement_render.md` pour mettre ton API en ligne en 10 minutes.

## 🔗 Connexion n8n

Voir `integration_n8n.md` pour le pas-à-pas côté n8n.
