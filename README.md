# TP Comparaison d'Architectures : Encodeur, Décodeur et Encodeur-Décodeur

## ⚠️ Important

Ce TP n'a PAS pour objectif de réaliser un entraînement complet (trop
long en pratique),\
mais uniquement de **comparer les trois grandes familles d'architectures
Transformer** : - Modèle *encodeur* (BERT) - Modèle *décodeur* (GPT-2) -
Modèle *encodeur-décodeur* (T5)

Le but est pédagogique : **observer les différences en précision,
F1-score et temps d'exécution**.

------------------------------------------------------------------------

## 🎯 Objectifs du TP

1.  Charger un dataset de classification de textes.
2.  Entraîner trois architectures différentes sur la même tâche.
3.  Mesurer :
    -   Accuracy
    -   F1-score
    -   Temps d'entraînement
    -   Temps d'inférence
4.  Comparer les performances.

------------------------------------------------------------------------

## 🧠 Base de données utilisée

Nous travaillons sur le dataset **AG News**, composé de **120 000
articles** répartis en **4 catégories** : - World - Sports - Business -
Sci/Tech

C'est un dataset standard pour tester les modèles de classification de
texte.

------------------------------------------------------------------------

## 🏗️ Les trois modèles utilisés

### 🔹 1. Encodeur (BERT)

-   Spécialité : comprendre le texte.
-   Entrée : une phrase.
-   Sortie : un vecteur de représentation.
-   Avantage : très bon pour la classification.

### 🔹 2. Décodeur (GPT-2)

-   Spécialité : générer du texte.
-   Peu adapté à la classification, mais possible via adaptation.
-   Avantage : flexibilité.

### 🔹 3. Encodeur-Décodeur (T5)

-   Spécialité : transformer un texte en un autre (traduction, résumé,
    classification...).
-   Pour la classification, la sortie est un token représentant la
    classe.

------------------------------------------------------------------------

## 🧩 Structure du code

### 1. Importation des librairies

Chargement de PyTorch, Transformers, Dataset, métriques, etc.

### 2. Préparation des données

-   Chargement du dataset
-   Split train / test
-   Tokenisation selon le modèle choisi

### 3. Entraînement de chaque modèle

Le notebook contient trois fonctions : - `train_bert(seed)` -
`train_gpt(seed)` - `train_t5(seed)`

Chaque fonction : - instancie le tokenizer - charge le modèle
pré-entraîné - prépare la dataset - entraîne le modèle à partir de la
seed donnée

### 4. Compilation des résultats

Fonction `compile_results()` : - calcule moyennes et écarts-types -
retourne un tableau résumé

------------------------------------------------------------------------

## 📊 Ce que vous devez rendre

-   Le notebook contenant les expérimentations.
-   Le présent README expliquant le TP.

------------------------------------------------------------------------

## ✔️ Conclusion

Ce TP sert à : - comprendre les différences d'architectures - mesurer
leur performance réelle - voir leur efficacité sur la même tâche -
apprendre à manipuler HuggingFace Transformers

Il ne vise pas la performance maximale, mais **la comparaison
pédagogique**.
