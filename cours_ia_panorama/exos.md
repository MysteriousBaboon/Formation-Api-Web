# 🧪 Exercices — Panorama de l'IA (≈ 2h, en autonomie)

> 🦿 **Cours sans code.** Ces exercices se font avec un papier/un fichier texte et un navigateur.
> L'objectif n'est pas d'avoir « la » bonne réponse, mais de **t'approprier le vocabulaire**.
> Les éléments de réponse sont dans `corriges/`.

---

## Exercice 1 — Ranger les cas d'usage dans les bonnes familles (25 min)

Pour chacun de ces produits/usages, indique **la (ou les) famille(s)** de l'IA concernée(s)
parmi : Vision · Langage (NLP) · Audio/voix · Génératif · Recommandation · Décision/robotique.

1. Le fil d'actualité de TikTok qui te propose des vidéos
2. Une app qui transforme une photo de plante en nom d'espèce
3. La transcription automatique d'un mémo vocal en texte
4. Midjourney qui crée une image à partir d'une phrase
5. Un filtre anti-spam dans ta boîte mail
6. Une voiture qui se gare toute seule
7. La traduction instantanée d'un menu de restaurant
8. AlphaGo qui joue au Go

> 💡 Certains cas combinent **plusieurs** familles. Note lesquelles et pourquoi.

---

## Exercice 2 — Supervisé, non-supervisé ou renforcement ? (25 min)

Pour chaque situation, dis quel **type d'apprentissage** est le plus adapté, et **justifie en une phrase**.

1. Prédire le prix de vente d'un appartement à partir de ses caractéristiques
2. Regrouper 50 000 clients en profils-types sans savoir lesquels à l'avance
3. Apprendre à un robot à marcher en le laissant tomber et se relever
4. Détecter des transactions bancaires anormales sans liste de fraudes connues
5. Reconnaître si un e-mail est un spam à partir de milliers d'exemples déjà triés

---

## Exercice 3 — Les poupées russes (15 min)

Sans regarder le cours, complète de mémoire :

1. Classe ces 4 termes du plus large au plus précis :
   `Deep Learning` · `IA` · `IA générative` · `Machine Learning`
2. Donne **un exemple** pour chacun.
3. Vrai ou faux (justifie) :
   - a) « Tout le machine learning est du deep learning. »
   - b) « ChatGPT est de l'IA générative. »
   - c) « Un filtre anti-spam est forcément du deep learning. »

---

## Exercice 4 — Chasse à l'hallucination (30 min) 🔎

Ouvre un LLM grand public (ChatGPT, Claude, Le Chat de Mistral, Gemini…) et essaie de
le faire **se tromper**. Quelques pistes :

1. Demande-lui une biographie de **toi-même** (ton nom complet) ou d'une personne peu connue.
2. Demande une citation précise d'un livre, avec le numéro de page.
3. Demande des informations sur un événement **très récent** (après son cutoff).
4. Invente un concept qui n'existe pas et demande-lui de l'expliquer.

Pour chaque test, note :
- La réponse a-t-elle l'air **sûre d'elle** ?
- Est-elle **vraie** (vérifie !) ?
- Qu'est-ce que ça t'apprend sur la confiance à accorder à un LLM ?

---

## Exercice 5 — Manipulation : Teachable Machine (25 min) 🖐️

Va sur https://teachablemachine.withgoogle.com → *Get Started* → *Image Project*.

1. Crée **2 classes** (ex. « main ouverte » / « poing fermé ») et capture ~30 images de chacune avec ta webcam.
2. Clique sur **Train Model**, puis teste en direct.
3. Réponds :
   - Quelle était la phase d'**entraînement** ? Et l'**inférence** ?
   - Qu'étaient les **features** et les **labels** ?
   - Ajoute une 3ᵉ classe mal éclairée/floue : le modèle se trompe-t-il plus ? Pourquoi ?
     (relie ça au *garbage in, garbage out*)

---

## Exercice 6 — Quiz éclair (15 min)

Réponds en une ligne :

1. Différence entre **entraînement** et **inférence** ?
2. Que veut dire **feature** ? Et **label** ?
3. À quoi sert un **GPU** en IA ?
4. Cite **deux limites** d'une IA dont il faut se méfier.
5. En 2017, quelle invention a rendu les LLM modernes possibles ?

---

## ✅ Checklist d'auto-évaluation

Coche mentalement. Si un point coince, relis la section indiquée de `cours.md`.

- [ ] Je sais expliquer IA / ML / Deep Learning / Génératif et leur emboîtement (§2)
- [ ] Je peux citer 4 familles de l'IA avec un exemple (§3)
- [ ] Je distingue supervisé / non-supervisé / renforcement (§4)
- [ ] Je sais ce que sont features, labels, entraînement, inférence (§5)
- [ ] J'ai vu de mes yeux une hallucination de LLM (exo 4)
- [ ] J'ai entraîné un mini-modèle avec Teachable Machine (exo 5)
- [ ] Je situe les cours 9 à 12 dans le panorama (§8)

> 🎯 Si tout est coché, tu es prêt·e pour le **Cours 9 — Machine Learning**.

---

## 🚀 Fini en avance ? Pour aller plus loin

Ouvre **`pour_aller_plus_loin.md`** : démos bonus, l'IA secteur par secteur, idées reçues à
déconstruire, **sujets de débat** pour une discussion de groupe, ressources à regarder, et un
quiz bonus. De quoi explorer en autonomie jusqu'au prochain cours.
