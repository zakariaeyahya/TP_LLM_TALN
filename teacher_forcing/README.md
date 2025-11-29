# Démonstration du Teacher Forcing pour l'entraînement de LLMs

Ce projet contient un script Python simple dont l'objectif est d'illustrer de manière pédagogique le concept de **Teacher Forcing** (ou apprentissage forcé). C'est une technique fondamentale utilisée lors de l'entraînement de modèles de langage génératifs (comme les LLMs).

Le script ne réalise pas un entraînement de modèle, mais simule la manière dont les données sont préparées et présentées au modèle à chaque étape d'une boucle d'entraînement.

## 📖 Concept : Qu'est-ce que le Teacher Forcing ?

Le "Teacher Forcing" est une stratégie d'entraînement pour les modèles qui génèrent des séquences (du texte, de la musique, etc.).

L'idée est simple : pour prédire le prochain mot d'une phrase, on ne donne pas au modèle sa propre prédiction de l'étape précédente (qui pourrait être fausse). À la place, on le **"force"** à utiliser le mot correct de la phrase d'exemple.

**Analogie :** C'est comme un professeur qui apprend une poésie à un élève. Au lieu de laisser l'élève continuer à réciter en se basant sur une rime erronée qu'il vient de faire, le professeur l'arrête, lui donne le bon mot, et lui demande de continuer à partir de cette base correcte.

Cette méthode permet de stabiliser et d'accélérer l'apprentissage.

## 🚀 Comment utiliser ce script

### Prérequis

*   Python 3.x
*   La bibliothèque `pandas`

Si `pandas` n'est pas installé, vous pouvez le faire via pip :
```bash
pip install pandas
