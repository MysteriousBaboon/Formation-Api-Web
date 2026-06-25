# Troc'Quartier — architecture (à remplir)

## 1. Architecture multicouche

```mermaid
flowchart TB
  subgraph Presentation
    UI[…]
  end
  subgraph Orchestration
    ORCH[…]
  end
  subgraph Metier
    API[…]
  end
  subgraph Donnees
    DB[(…)]
  end
  %% TODO : relie les couches dans le bon sens
```

## 2. Séquence — « un voisin réserve un objet »

```mermaid
sequenceDiagram
  actor V as Voisin
  participant UI as Interface
  participant API as Service métier
  participant DB as Base
  %% TODO : la suite des échanges jusqu'à la confirmation
```

## 3. Tableau des choix justifiés

| Couche | Outil choisi | Pourquoi ce choix | Point de sécurité (ANSSI) |
|---|---|---|---|
| Présentation | … | … | … |
| Orchestration | … | … | … |
| Métier | … | … | … |
| Données | … | … | … |

## Question de défense

> Pourquoi la règle « l'objet est-il libre ? » vit dans le micro-service et pas dans le formulaire ?

…
