---

# 🧠 Fine-Tuning BERT pour la Classification de Tweets

## 📌 Description

Ce projet présente le **fine-tuning du modèle BERT (bert-base-uncased)** pour une **tâche de classification binaire** sur un jeu de tweets.
L’objectif est de prédire le label (`target`) associé à chaque texte (`text`) à partir d’un ensemble de données d’entraînement (`train.csv`).

Le pipeline complet inclut :

* Prétraitement et nettoyage des textes
* Tokenization avec le tokenizer BERT officiel
* Création de DataLoaders PyTorch
* Entraînement et validation du modèle
* Sauvegarde du meilleur modèle
* Prédictions sur le jeu de test (`test.csv`) et génération du fichier `submission.csv`

---

## 🗂️ Structure du projet

```
.
├── train.csv
├── test.csv
├── bert_model_state.bin
├── submission.csv
├── train_bert.ipynb   # Notebook principal (ou script d’entraînement)
└── README.md
```

---

---

## 💾 Données

* **train.csv** : contient les tweets d’entraînement avec leurs labels (`text`, `target`)
* **test.csv** : contient les tweets à prédire (`text`)

Le script nettoie automatiquement les textes en :

* Supprimant les URLs, balises HTML, ponctuations, emojis
* Retirant les stopwords (anglais)
* Convertissant le texte en minuscules

---

## 🧩 Tokenization & Préparation

Les tweets sont tokenizés avec :

```python
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)
```

Chaque texte est encodé, tronqué ou paddé à la longueur maximale détectée (`max_len ≤ 512`).
Les tenseurs finaux (`input_ids`, `attention_mask`, `labels`) sont ensuite placés dans un `TensorDataset`.

---

## 🚀 Entraînement

Le modèle utilisé :

```python
from transformers import BertForSequenceClassification
model = BertForSequenceClassification.from_pretrained(
    "bert-base-uncased",
    num_labels=2
)
```

**Optimiseur :** `AdamW`
**Scheduler :** `get_linear_schedule_with_warmup`
**Batch size :** 32
**Epochs :** 4
**Learning rate :** 2e-5

Le meilleur modèle (selon l’accuracy sur le jeu de validation) est sauvegardé sous :

```
bert_model_state.bin
```

---

## 📈 Validation

Pendant l’entraînement, le script affiche :

* La **loss moyenne** sur le training set
* L’**accuracy moyenne** sur le validation set

Tu peux aussi calculer un rapport détaillé avec :

```python
from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred, digits=4))
```

---

## 🧮 Prédiction sur le jeu de test

Après entraînement :

```python
df_test = pd.read_csv('test.csv')
df_test['text'] = df_test['text'].apply(clean_text)
```

Les prédictions sont sauvegardées dans :

```
submission.csv
```

Structure attendue :

| id | target |
| -- | -----: |
| 1  |      0 |
| 2  |      1 |
| …  |      … |

---

## 🖥️ Environnement d’exécution

* **Python** ≥ 3.8
* **GPU** recommandé (CUDA)
* Compatible avec **Google Colab**

---

## 📊 Améliorations possibles

* Ajouter un **early stopping** pour éviter l’overfitting
* Tester des modèles plus légers : *DistilBERT, RoBERTa*
* Gérer le **déséquilibre des classes** avec un WeightedSampler
* Intégrer `transformers.Trainer` pour simplifier le code

---

## 👨‍💻 Auteur

**Zakariae YAHYA**
Étudiant en Ingénierie Data & IA — ENSA Tétouan
📧 [zakariae.yh@gmail.com](mailto:zakariae.yh@gmail.com)
🔗 [GitHub](https://github.com/zakariaeyahya)

---
