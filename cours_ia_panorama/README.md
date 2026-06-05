# 🧭 Cours 8 — Panorama de l'IA (la carte du territoire)

Première journée du parcours IA. On ne code (presque) pas : on **prend de la hauteur**.
L'objectif est de te donner une **vision 360°** de ce qu'est l'intelligence artificielle,
pour que les 4 cours suivants tombent dans des cases claires.

## 🎯 Objectifs

À la fin de cette journée, tu seras capable de :

- Expliquer la différence entre **IA, Machine Learning, Deep Learning et IA générative**
- Citer les **grandes familles** de l'IA (vision, langage, audio, génératif, reco…)
- Distinguer les **3 types d'apprentissage** (supervisé, non-supervisé, renforcement)
- Parler le **vocabulaire de base** (modèle, dataset, features, entraînement, inférence…)
- Avoir un **regard critique** (biais, hallucinations, limites)

## 📁 Structure

```
cours_ia_panorama/
├── README.md            ← ce fichier
├── cours.md             ← le cours complet (à lire en premier)
├── glossaire.md         ← le lexique de survie, à garder ouvert
├── slides/
│   ├── contenu.py       ← le contenu des slides (modifiable)
│   └── panorama.pptx    ← le diaporama prêt à projeter
├── exos.md              ← exercices de réflexion (pas de code lourd)
└── corriges/            ← éléments de réponse
```

## 🗓️ Déroulé de journée conseillé

> 🦿 **Format adapté** : je présente la théorie au tableau le matin, puis vous bossez
> en autonomie l'après-midi. Tout est écrit pour être suivi **même sans moi**.

| Moment | Quoi | Support |
|---|---|---|
| Matin (~1h) | Mini-cours au tableau | `slides/panorama.pptx` + `cours.md` |
| Matin | Lecture tranquille | `cours.md` en entier + `glossaire.md` |
| Après-midi | Exercices de réflexion en autonomie | `exos.md` |
| Fin de journée | Mise en commun rapide | `corriges/` |

## 🚀 Pour démarrer

Ce cours est surtout de la lecture. Pour (re)générer le diaporama :

```bash
cd cours_ia_panorama
source ../.venv/bin/activate
pip install python-pptx          # déjà installé si tu as suivi le setup
python slides/contenu.py         # régénère slides/panorama.pptx
```

## 🔗 Le lien avec le reste

C'est la **porte d'entrée** du parcours IA. Tu viens de finir Python
(données, scraping, API, automatisation). À partir d'ici, on apprend à des machines
à **décider et à créer**, pas seulement à exécuter.

```
[Cours 8: Panorama]  →  9: Machine Learning  →  10: Deep Learning
                                              →  11: LLM  →  12: Agents
```

Garde la **carte** en tête : chaque cours suivant est une case de ce panorama.
