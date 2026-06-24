# 📚 Cours — Agents LLM

> Un LLM seul ne sait que produire du texte. Un **agent**, c'est un LLM à qui on donne des **outils** et la possibilité de les **utiliser en boucle** pour accomplir une tâche. C'est le saut de « répondre » à « agir ».

---

## 1. D'un LLM à un agent

Le LLM du cours 11 a trois faiblesses majeures :
- il ne sait pas **calculer** de façon fiable,
- il ne connaît pas l'**actualité** ni **tes données**,
- il ne peut **rien faire** d'autre que produire du texte.

Un **agent** corrige tout ça : on lui donne des **outils** (des fonctions Python) et on le laisse
décider **quand** les appeler. Le LLM devient le **cerveau** qui orchestre ; les outils sont ses **mains**.

```
        ┌─────────────────────────────────────────┐
        │              AGENT                        │
        │   ┌──────────┐        ┌───────────────┐  │
   but ─┼──▶│   LLM    │◀──────▶│    OUTILS      │  │──▶ résultat
        │   │(cerveau) │ décide │ calc, API, web │  │
        │   └──────────┘        └───────────────┘  │
        └─────────────────────────────────────────┘
```

---

## 2. La boucle agentique : perception → raisonnement → action

Un agent ne répond pas d'un coup : il **boucle**.

```
   ┌───────────────────────────────────────────────┐
   │  1. RAISONNER : que faut-il faire maintenant ? │
   │  2. AGIR      : appeler un outil                │
   │  3. OBSERVER  : lire le résultat de l'outil     │
   │  4. RECOMMENCER jusqu'à pouvoir répondre        │
   └───────────────────────────────────────────────┘
```

Exemple : *« Quel est le prix TTC de 3 articles à 19,99 € avec 20 % de TVA ? »*
1. Raisonner : « je dois calculer 3 × 19,99, puis ajouter 20 % »
2. Agir : appeler la **calculatrice** avec `3 * 19.99`
3. Observer : `59.97`
4. Agir : appeler la calculatrice avec `59.97 * 1.20`
5. Observer : `71.964`
6. Répondre : « Le prix TTC est 71,96 € »

Ce schéma (raisonner / agir / observer) s'appelle souvent **ReAct** (*Reasoning + Acting*).
👉 La démo `3_agent_boucle_react.py` le code **à la main** pour bien le voir.

---

## 3. Le function / tool calling

Comment le LLM « appelle » une fonction alors qu'il ne produit que du texte ? On lui **décrit**
les outils disponibles, et il répond — au lieu d'un texte — par une **demande d'appel structurée**.

```
1. On déclare l'outil :  { nom: "calculer", description: "...", paramètres: {expression} }
2. Le LLM répond :       « appelle calculer(expression="3 * 19.99") »   ← pas du texte libre !
3. NOTRE code exécute la vraie fonction Python  →  59.97
4. On renvoie le résultat au LLM  →  il formule la réponse finale
```

Points clés :
- **C'est toujours TON code qui exécute** la fonction, pas le LLM. Lui ne fait que **demander**.
- La **description** de l'outil est cruciale : c'est elle qui aide le LLM à choisir le bon outil
  au bon moment. Soigne-la comme un prompt.
- Le LLM peut demander **plusieurs** appels, d'affilée, jusqu'à avoir ce qu'il lui faut.

> 👉 Démos `1`, `2` et `4` : le tool calling « natif » (paramètre `tools`). Démo `3` : la même idée
> codée à la main par du prompt, pour comprendre la mécanique.

---

## 4. Donner les bons outils

Un outil est **n'importe quelle fonction Python**. Les plus courants :

| Outil | Pourquoi | Corrige quelle faiblesse |
|---|---|---|
| **Calculatrice** | Le LLM rate les calculs | Fiabilité des maths |
| **Recherche / base de connaissances** | Accéder à des infos à jour ou privées | Cutoff, ignorance de tes données |
| **Appel d'API** | Agir sur un autre système | « ne peut rien faire » |
| **Date / heure** | Le LLM n'a pas d'horloge | Ne connaît pas « maintenant » |
| **Exécuter du code** | Tâches complexes/déterministes | Fiabilité |

> 💡 Souviens-toi du cours 3 : **ton micro-service Python EST un outil d'agent parfait.**
> L'agent l'appelle comme n'importe quelle API. La démo `5` fait exactement ça.

---

## 5. MCP — sortir les outils du script

Dans les sections précédentes, chaque agent **recode ses outils dans son propre script**
(`REGISTRE` + `OUTILS`). Deux limites : si tu as trois applis, tu réécris **trois fois** l'outil
météo ; et ces outils ne servent **qu'à ton agent**. Le **MCP** règle exactement ça.

> **MCP** (*Model Context Protocol*) : un **protocole standard** pour brancher des outils et des
> données sur un LLM. Créé par **Anthropic fin 2024**, il est aujourd'hui adopté très largement
> (Anthropic, OpenAI, Google…). L'image consacrée : **« le port USB-C de l'IA »** — une prise
> universelle. Avant : chaque intégration était du sur-mesure. Avec MCP : tu écris l'outil **une
> fois**, et **n'importe quel client compatible** (Claude Desktop, Claude Code, Cursor…) le branche.

### L'architecture : hôte → client → serveur

```
   HÔTE  (l'appli : Claude Desktop, Claude Code, ou TON client)
     │  contient un ou plusieurs…
     ▼
   CLIENT ───[ protocole MCP ]───▶  SERVEUR  ──▶ outils / données
   (1 par serveur)                  (ton code, ou un serveur tout fait)

   Transport :
     • stdio  → serveur LOCAL lancé en sous-processus (le plus courant)
     • HTTP   → serveur DISTANT (une simple URL)
```

- L'**hôte** est l'application qui parle à l'utilisateur et au LLM.
- Le **serveur** expose des capacités. Il peut être **le tien** (démo `6`) ou un serveur **déjà
  existant** : il en existe des centaines (GitHub, Slack, Postgres, système de fichiers, navigateur…).

### Ce qu'un serveur MCP expose

| Capacité | C'est quoi | On l'a déjà croisé ? |
|---|---|---|
| **Tools** (outils) | Des fonctions que le LLM peut appeler | Oui : le tool calling de la §3, mais l'outil vit **dehors** |
| **Resources** | Des données que le modèle peut lire (fichier, ligne de BDD…) | C'est l'idée du RAG (cours 11), exposée proprement |
| **Prompts** | Des modèles de prompts réutilisables | Des prompts « prêts à l'emploi » fournis par le serveur |

> 💡 **Le lien avec le cours.** Un outil MCP, c'est *exactement* le tool calling de la §3 — mais
> l'outil est **sorti du script** pour vivre derrière une prise standard. C'est à l'outil ce que
> **le micro-service du cours 3** est à une simple fonction : on l'externalise pour le rendre
> **réutilisable et partageable**.

### Brancher un serveur — deux façons

**1) Sans code, dans un vrai client** (Claude Desktop, Claude Code…). On déclare le serveur dans un
fichier de config JSON ; le client **découvre ses outils tout seul** :

```json
{
  "mcpServers": {
    "mes-outils": {
      "command": "python",
      "args": ["6_serveur_mcp.py"]
    }
  }
}
```

> (En vrai, mets le **chemin absolu** vers le `python` de ton venv et vers le script.)

**2) En Python**, avec le SDK `mcp` : un client qui lance le serveur, **liste** ses outils et les
**appelle**. C'est ce que fait la démo `7`, qui rebranche ces outils dans la **boucle d'agent de la
démo 4** :

```
démo 6 (serveur)              démo 7 (client + agent)
  @mcp.tool() calculer  ──▶   list_tools()  ──▶  tools= envoyés au LLM
  @mcp.tool() meteo           call_tool()   ◀──  le LLM demande un outil
```

L'**aha** : à la démo 4, l'agent exécutait l'outil lui-même (`REGISTRE[nom](**args)`). À la démo 7,
il **délègue** l'exécution au serveur MCP (`session.call_tool(...)`). Le LLM, lui, ne voit **aucune
différence** : pour lui, c'est toujours du tool calling.

> ⚠️ **Garde-fou (voir §7).** Un serveur MCP, c'est du **code qui s'exécute chez toi** et qui peut
> agir ou lire tes données. N'installe que des serveurs **de confiance**, et garde la **validation
> humaine** pour les actions sensibles.

---

## 6. Mémoire & orchestration

- **Mémoire courte** : l'historique de la conversation (comme au cours 11).
- **Mémoire longue** : stocker des faits dans une base / un fichier, et les ressortir via un outil
  de recherche (c'est le RAG du cours 11, branché comme outil).
- **Orchestration multi-étapes** : pour une tâche complexe, l'agent enchaîne plusieurs appels
  d'outils. Certains systèmes vont jusqu'à des **équipes d'agents** spécialisés qui se répartissent
  le travail.

---

## 7. Les garde-fous (indispensables)

Un agent qui boucle et agit dans le monde réel, ça se **sécurise** :

- **Limite d'itérations** : sans plafond, un agent peut boucler à l'infini (et brûler du budget).
  → on impose un nombre max d'étapes.
- **Validation humaine** : pour les actions sensibles (envoyer un mail, payer…), demander une
  confirmation avant d'agir.
- **Outils en lecture seule par défaut** : méfiance avec les outils qui modifient/suppriment.
- **Filtrer les entrées** : un outil qui exécute du code ou des requêtes doit être **bridé**
  (ne jamais faire un `eval()` brut sur une chaîne venue du LLM — voir la démo calculatrice).
- **Coût** : chaque étape = un appel LLM. Un agent à 10 étapes coûte 10× un simple appel.

> ⚠️ Règle d'or (rappel du cours 8) : **une IA propose, un humain dispose** — surtout quand l'IA
> peut *agir*.

---

## 8. Le paysage des frameworks

Tu peux tout coder à la main (c'est ce qu'on fait ici, pour comprendre). En pratique, on
s'appuie souvent sur un framework :

| Outil | Pour quoi |
|---|---|
| **LangChain** | Le plus connu : chaînes, agents, intégrations à gogo |
| **LlamaIndex** | Spécialisé RAG / données |
| **SDK natifs** (OpenAI, Anthropic…) | Tool calling intégré, léger |
| **n8n (nœud AI Agent)** | Agents **en no-code**, branchés à 400+ services |

> 💡 Commencer **sans framework** (comme dans ce cours) est le meilleur moyen de comprendre ce
> qu'ils font pour toi. Ensuite, un framework te fait gagner du temps.

---

## 9. Aller plus loin

- **Streaming + UI** : afficher le raisonnement de l'agent en direct.
- **Agents multiples** : un « chef » qui délègue à des agents spécialisés.
- **Observabilité** : journaliser chaque étape (quel outil, quels arguments, quel résultat) — vital
  pour déboguer un agent.
- **n8n** : le nœud *AI Agent* te permet d'assembler tout ça visuellement et de le déclencher
  (cron, webhook, formulaire…). C'est le pont parfait avec tes cours 3 et 7.

🎓 **Bravo** : tu as parcouru tout le chemin, de la variable Python (cours 1) à l'agent autonome
qui orchestre des outils. C'est exactement la pile qu'utilisent les produits d'IA modernes.
