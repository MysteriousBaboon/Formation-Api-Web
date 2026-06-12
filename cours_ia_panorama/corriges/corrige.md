# ✅ Corrigés — Panorama de l'IA

> Ce sont des **éléments de réponse**, pas une vérité unique. Sur un cours de panorama,
> la justification compte plus que le mot exact. Si tu as argumenté autrement mais
> correctement, c'est bon.

---

## Exercice 1 — Familles de l'IA

| # | Cas | Famille(s) |
|---|---|---|
| 1 | Fil TikTok | **Recommandation** (+ Vision pour analyser les vidéos) |
| 2 | Photo → espèce de plante | **Vision** |
| 3 | Mémo vocal → texte | **Audio/voix** (reconnaissance vocale) |
| 4 | Midjourney (phrase → image) | **Génératif** (+ Langage pour comprendre la phrase) |
| 5 | Filtre anti-spam | **Langage (NLP)** |
| 6 | Voiture qui se gare | **Vision** + **Décision/robotique** |
| 7 | Traduction d'un menu | **Vision** (lire) + **Langage** (traduire) |
| 8 | AlphaGo | **Décision/robotique** (renforcement) |

👉 Le point clé : beaucoup de produits **combinent** plusieurs familles.

---

## Exercice 2 — Type d'apprentissage

1. Prix d'un appartement → **Supervisé** (régression) : on a des exemples avec le prix réel.
2. Regrouper des clients → **Non-supervisé** : pas d'étiquettes, on cherche des groupes.
3. Robot qui apprend à marcher → **Renforcement** : essai/erreur + récompense.
4. Transactions anormales sans liste de fraudes → **Non-supervisé** (détection d'anomalies).
5. Spam à partir d'exemples triés → **Supervisé** (classification).

---

## Exercice 3 — Poupées russes

1. Du plus large au plus précis : **IA → Machine Learning → Deep Learning → IA générative**.
2. Exemples possibles : IA = filtre anti-spam ; ML = prédire un prix ; Deep Learning =
   reconnaître un chat sur une photo ; IA générative = ChatGPT.
3. Vrai/Faux :
   - a) **Faux.** C'est l'inverse : tout le deep learning est du ML, pas le contraire.
   - b) **Vrai.** ChatGPT génère du texte → IA générative.
   - c) **Faux.** Un anti-spam peut marcher avec des méthodes ML simples (pas forcément deep).

---

## Exercice 4 — Chasse à l'hallucination

Pas de corrigé figé : **tu dois** avoir constaté qu'un LLM peut répondre faux **avec assurance**.
Points à retenir :
- Un LLM optimise « ce qui **sonne** juste », pas « ce qui **est** vrai ».
- Il est faible sur : les personnes peu connues, les citations exactes, les chiffres précis,
  et tout ce qui est **après son cutoff** (date limite de ses connaissances).
- D'où la règle d'or : **vérifier**, surtout quand l'enjeu est réel.

---

## Exercice 5 — Teachable Machine

- **Entraînement** = quand tu cliques « Train Model » (il apprend depuis tes images).
- **Inférence** = quand il devine en direct ce que montre la webcam.
- **Features** = les images (les pixels) ; **labels** = les noms de classes que tu as donnés.
- Avec une classe floue/mal éclairée, le modèle se trompe **plus** : il a appris sur de
  mauvaises données → **garbage in, garbage out**. La qualité des données fait tout.

---

## Exercice 6 — Quiz éclair

1. **Entraînement** = phase d'apprentissage (lente, une fois). **Inférence** = utilisation pour prédire (rapide, souvent).
2. **Feature** = caractéristique d'entrée ; **label** = la bonne réponse à prédire.
3. Un **GPU** accélère massivement les calculs parallèles de l'entraînement.
4. Deux limites parmi : biais, hallucinations, dépendance aux données, coût/énergie, vie privée.
5. Les **Transformers** (« Attention is all you need », 2017).
