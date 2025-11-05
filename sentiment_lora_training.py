# ==============================================================
# SENTIMENT ANALYSIS avec DistilBERT + LoRA (PEFT)
# ==============================================================
# Auteur : Hiba 💙
# Objectif : entraîner un modèle DistilBERT avec LoRA
# pour prédire si une phrase est positive ou négative.
# ==============================================================

# ==============================================================
# 🧩 1. INSTALLATION DES BIBLIOTHÈQUES
# --------------------------------------------------------------
# Ces commandes installent les packages nécessaires.
# ⚠️ À exécuter UNE SEULE FOIS dans ton terminal (pas dans le code)
# --------------------------------------------------------------
# pip install datasets==2.15.0
# pip install transformers==4.40.1
# pip install peft==0.9.0
# pip install torch
# pip install pandas
# ==============================================================


# ==============================================================
# 📦 2. IMPORTATION DES BIBLIOTHÈQUES
# ==============================================================

from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    Trainer,
    TrainingArguments,
    DataCollatorWithPadding
)
from peft import LoraConfig, get_peft_model, TaskType
import pandas as pd
import numpy as np
import torch


# ==============================================================
# 🧠 3. CHARGEMENT DU DATASET (Stanford Sentiment Treebank)
# --------------------------------------------------------------
# Ce dataset contient des phrases en anglais avec un label :
# 0 = négatif, 1 = positif
# ==============================================================

dataset = load_dataset("stanfordnlp/sst2", split="train").train_test_split(
    test_size=0.2, shuffle=True, seed=23
)

# Afficher un exemple
print(dataset["train"][0])


# ==============================================================
# ✂️ 4. TOKENISATION DES PHRASES
# --------------------------------------------------------------
# On convertit le texte en "tokens" (nombres) compris par DistilBERT.
# ==============================================================

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
splits = ["train", "test"]

tokenized_dataset = {}
for split in splits:
    tokenized_dataset[split] = dataset[split].map(
        lambda x: tokenizer(x["sentence"], truncation=True, padding="max_length"),
        batched=True
    )

print("✅ Tokenisation terminée !")


# ==============================================================
# 🤖 5. CHARGEMENT DU MODÈLE DISTILBERT
# --------------------------------------------------------------
# On initialise DistilBERT pour la classification binaire :
# "negative" (0) ou "positive" (1)
# ==============================================================

model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=2,
    id2label={0: "negative", 1: "positive"},
    label2id={"negative": 0, "positive": 1},
)

# Débloquer tous les paramètres (on veut tout réentraîner)
for param in model.parameters():
    param.requires_grad = True

print("✅ Modèle DistilBERT chargé avec succès !")


# ==============================================================
# 📏 6. DÉFINITION D'UNE FONCTION DE MÉTRIQUES
# --------------------------------------------------------------
# Cette fonction calcule Precision, Recall et F1-score.
# ==============================================================

def calculate_precision_recall_f1(actuals, predictions):
    true_positives = sum((actuals == 1) & (predictions == 1))
    false_positives = sum((actuals == 0) & (predictions == 1))
    false_negatives = sum((actuals == 1) & (predictions == 0))

    precision = true_positives / (true_positives + false_positives + 1e-8)
    recall = true_positives / (true_positives + false_negatives + 1e-8)
    f1_score = 2 * (precision * recall) / (precision + recall + 1e-8)
    return {"precision": precision, "recall": recall, "f1": f1_score}


# ==============================================================
# ⚙️ 7. CONFIGURATION DE LoRA (Low-Rank Adaptation)
# --------------------------------------------------------------
# LoRA permet de fine-tuner le modèle avec peu de paramètres.
# ==============================================================

lora_config = LoraConfig(
    r=2,  # rang faible (taille réduite)
    lora_alpha=16,  # facteur de mise à l’échelle
    lora_dropout=0.05,  # pour éviter le surapprentissage
    target_modules=["q_lin", "k_lin", "v_lin"],  # couches où LoRA s'applique
    bias='none',
    task_type=TaskType.SEQ_CLS  # tâche = classification de séquence
)

# Appliquer LoRA sur le modèle
peft_model = get_peft_model(model, lora_config)
print("✅ LoRA configuré et appliqué au modèle !")


# ==============================================================
# 🏋️‍♀️ 8. CONFIGURATION DU TRAINER
# --------------------------------------------------------------
# Trainer simplifie l’entraînement et l’évaluation.
# ==============================================================

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=1)
    return calculate_precision_recall_f1(labels, preds)


trainer = Trainer(
    model=peft_model,
    args=TrainingArguments(
        output_dir="./results_lora_sst2",
        learning_rate=2e-3,
        per_device_train_batch_size=4,
        per_device_eval_batch_size=4,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        num_train_epochs=1,
        weight_decay=0.01,
        load_best_model_at_end=True,
        logging_dir="./logs",
        logging_steps=20,
        report_to="none"
    ),
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["test"],
    tokenizer=tokenizer,
    data_collator=DataCollatorWithPadding(tokenizer=tokenizer),
    compute_metrics=compute_metrics,
)


# ==============================================================
# 🚀 9. ENTRAÎNEMENT DU MODÈLE
# ==============================================================

print("🚀 Début de l'entraînement...")
trainer.train()
print("✅ Entraînement terminé !")

# Sauvegarde du modèle LoRA
peft_model.save_pretrained('./peft_model')


# ==============================================================
# 🧪 10. ÉVALUATION DU MODÈLE
# ==============================================================

eval_results = trainer.evaluate()
print("📊 Résultats d’évaluation :", eval_results)


# ==============================================================
# 🔍 11. TEST SUR QUELQUES EXEMPLES
# ==============================================================

items_for_manual_review = tokenized_dataset["test"].select(
    [0, 1, 22, 31, 43, 292, 448, 487]
)

results = trainer.predict(items_for_manual_review)

# Création d’un DataFrame pour comparer les prédictions
df = pd.DataFrame({
    "Sentence": [item["sentence"] for item in items_for_manual_review],
    "Prediction": results.predictions.argmax(axis=1),
    "Label": results.label_ids
})

pd.set_option("display.max_colwidth", None)
print("\n📋 Exemples de prédictions :")
print(df)
