<<<<<<< HEAD
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
=======
# TP_LLM_TALN

## Overview

This repository contains resources for a sentiment analysis project targeting cryptocurrency markets. The code and artifacts focus on fine-tuning BERT-style models for text classification and preparing model predictions for submission.

Key highlights:
- Fine-tuning notebook for BERT-based classification
- Training and test CSV data provided for quick experiments
- A sample submission file for formatting predictions

## Repository structure

Top-level layout:

- `Fine-Tuning_BERT/`
	- `data/`
		- `train.csv` — training dataset (text + labels)
		- `test.csv` — test dataset (text only, for generating predictions)
	- `notebooks/`
		- `Bert_cassification (1).ipynb` — interactive notebook showing fine-tuning and evaluation steps
	- `submission/`
		- `sample_submission.csv` — example submission format expected by the evaluation pipeline

## Quick start (Windows / PowerShell)

These steps will help you create an environment and run the notebook locally.

1. Create and activate a virtual environment (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies. There is no `requirements.txt` in the repo yet; for experimentation install the common libraries used for BERT fine-tuning:

```powershell
pip install --upgrade pip
pip install transformers datasets torch pandas scikit-learn jupyter seaborn matplotlib
```

Notes:
- Installing `torch` may require selecting the right wheel for your CUDA version. See https://pytorch.org for the recommended install command.
- If you plan to use GPU acceleration, ensure appropriate drivers and CUDA/cuDNN are installed.

3. Start Jupyter and open the notebook:

```powershell
jupyter notebook
```

Then open `Fine-Tuning_BERT/notebooks/Bert_cassification (1).ipynb` in the browser.

## Data format

- `train.csv` — expected to contain at least two columns: `text` (the input) and `label` (the target class). Inspect the file in `Fine-Tuning_BERT/data/`.
- `test.csv` — expected to contain at least a `text` column and an `id` column for correspondence with `sample_submission.csv`.

## Notebook contents

The notebook `Bert_cassification (1).ipynb` demonstrates a typical workflow:

- Load and inspect `train.csv`
- Tokenize texts with a BERT tokenizer
- Create a PyTorch/Transformers dataset and dataloaders
- Fine-tune a pre-trained model (e.g., `bert-base-uncased`)
- Evaluate on a validation split
- Generate predictions for `test.csv` and save them in submission format

## Suggested next steps (low-effort improvements)

1. Add a `requirements.txt` or `environment.yml` for reproducible environments.
2. Split the notebook into modular scripts:
	 - `train.py` — training loop and checkpointing
	 - `eval.py` — evaluation and metrics
	 - `predict.py` — load model and create `submission.csv`
3. Add unit tests for data loading and simple model sanity checks.
4. Add a small README within `Fine-Tuning_BERT/` describing the exact expected columns and sample rows for `train.csv` and `test.csv`.

## Notes and assumptions

- This README assumes `train.csv` contains `text` and `label` columns and that `test.csv` contains `id` and `text` columns. If your files differ, update the notebook or scripts accordingly.
- The notebook file name includes a space and parentheses. When running scripts, consider renaming it to avoid tooling issues (e.g., `bert_classification.ipynb`).

## Contact

If you have questions or want help turning the notebook into scripts or CI, open an issue or contact the repo owner.

---

Happy fine-tuning! 🚀
>>>>>>> dcb4d4c09d7cb13cb15a7d32fdd0db8b81b6141c
