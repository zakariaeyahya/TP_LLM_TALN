# TP_LLM_TALN - Fine-Tuning BERT pour la Classification de Tweets

## 📌 Vue d'ensemble

Ce dépôt contient un **Travaux Pratiques (TP)** sur le fine-tuning du modèle BERT pour la classification binaire de tweets. Le notebook principal a été préparé comme un exercice pédagogique avec **5 sections TODO** que les étudiants doivent compléter.

**Objectif du TP :** Apprendre à fine-tuner BERT pour prédire le label (`target`) associé à chaque tweet (`text`) à partir d'un ensemble de données d'entraînement.

**Points clés :**
- Notebook interactif avec sections à compléter (5 TODO)
- Fine-tuning de BERT pour la classification binaire
- Données d'entraînement et de test fournies
- Pipeline complet : prétraitement → tokenization → entraînement → prédiction

## 📁 Structure du dépôt

```
TP_LLM_TALN/
├── Fine-Tuning_BERT/
│   ├── notebooks/
│   │   └── Bert_cassification (1).ipynb  # Notebook principal avec 5 sections TODO
│   ├── data/                              # (si présent)
│   │   ├── train.csv                      # Données d'entraînement (text, target)
│   │   └── test.csv                       # Données de test (text, id)
│   └── submission/                        # (si présent)
│       └── sample_submission.csv          # Format de soumission attendu
└── README.md                              # Ce fichier
```

**Note :** Les fichiers CSV peuvent être placés dans `/content/` si vous utilisez Google Colab, ou dans le dossier `data/` pour une exécution locale.

## 🚀 Démarrage rapide

### Option 1 : Google Colab (Recommandé)

1. Téléchargez le notebook `Bert_cassification (1).ipynb`
2. Uploadez-le sur Google Colab
3. Uploadez les fichiers `train.csv` et `test.csv` dans `/content/`
4. Exécutez les cellules une par une

**Avantages :** GPU gratuit, pas d'installation locale nécessaire

### Option 2 : Installation locale (Windows / PowerShell)

1. **Créer et activer un environnement virtuel :**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. **Installer les dépendances :**

```powershell
pip install --upgrade pip
pip install numpy pandas nltk torch scikit-learn transformers jupyter
```

**Note :** Pour PyTorch avec GPU, consultez https://pytorch.org pour la commande d'installation appropriée à votre version CUDA.

3. **Télécharger les données NLTK :**

```python
import nltk
nltk.download('stopwords')
```

4. **Lancer Jupyter :**

```powershell
jupyter notebook
```

5. **Ouvrir le notebook :** `Fine-Tuning_BERT/notebooks/Bert_cassification (1).ipynb`

## 📊 Format des données

### `train.csv`
Doit contenir au minimum :
- `text` : le texte du tweet (colonne d'entrée)
- `target` : le label binaire (0 ou 1) - colonne cible

### `test.csv`
Doit contenir au minimum :
- `id` : identifiant unique du tweet
- `text` : le texte du tweet à prédire

### Prétraitement automatique
Le notebook applique automatiquement :
- Suppression des URLs, balises HTML, ponctuations, emojis
- Suppression des stopwords (anglais)
- Conversion en minuscules

## 📚 Contenu du notebook - Sections TODO

Le notebook `Bert_cassification (1).ipynb` est structuré comme un **TP avec 5 sections à compléter** :

### 🔍 Sections TODO à compléter :

1. **Cellule 13 - Tokenization et padding**
   - Calcul de `max_len` pour les séquences
   - Tokenization en batch avec padding et truncation
   - Extraction des `input_ids` et `attention_masks`

2. **Cellule 16 - DataLoaders**
   - Définition de la taille de batch
   - Création des DataLoaders avec les samplers appropriés (RandomSampler vs SequentialSampler)

3. **Cellule 18 - Optimiseur AdamW**
   - Configuration de l'optimiseur avec les bons paramètres
   - Learning rate et epsilon

4. **Cellule 20 - Scheduler de learning rate**
   - Calcul du nombre total de steps d'entraînement
   - Création du scheduler avec warmup

5. **Cellule 23 - Boucle d'entraînement**
   - Ordre des opérations pour une étape d'entraînement complète
   - Zero grad, forward, backward, gradient clipping, optimizer step, scheduler step

### 📋 Workflow complet du notebook :

1. Installation des dépendances
2. Import des bibliothèques
3. Configuration du device (CPU/GPU)
4. Chargement et inspection des données
5. **Prétraitement des textes** (fonction `clean_text`)
6. **Tokenization BERT** (TODO #1)
7. Création du dataset et split train/validation
8. **Création des DataLoaders** (TODO #2)
9. Chargement du modèle BERT pré-entraîné
10. **Configuration de l'optimiseur** (TODO #3)
11. **Configuration du scheduler** (TODO #4)
12. **Boucle d'entraînement** (TODO #5)
13. Sauvegarde du meilleur modèle
14. Chargement du modèle et prédictions sur le test
15. Génération du fichier `submission.csv`

## 🎯 Objectifs pédagogiques du TP

En complétant ce TP, vous apprendrez à :

- ✅ Utiliser le tokenizer BERT pour préparer les données textuelles
- ✅ Créer des DataLoaders PyTorch avec les bons samplers
- ✅ Configurer un optimiseur AdamW adapté au fine-tuning de BERT
- ✅ Utiliser un scheduler de learning rate avec warmup
- ✅ Implémenter une boucle d'entraînement complète avec gradient clipping
- ✅ Évaluer un modèle et sauvegarder les meilleurs poids
- ✅ Générer des prédictions sur un jeu de test

## 💡 Conseils pour compléter les TODO

1. **Lisez attentivement les questions** dans chaque section TODO
2. **Consultez la documentation** :
   - [Hugging Face Transformers](https://huggingface.co/docs/transformers)
   - [PyTorch DataLoader](https://pytorch.org/docs/stable/data.html)
   - [AdamW Optimizer](https://pytorch.org/docs/stable/optim.html#torch.optim.AdamW)
3. **Testez votre code** étape par étape
4. **Vérifiez les erreurs** : les messages d'erreur Python sont souvent très utiles

## 📝 Notes importantes

- Le notebook utilise `bert-base-uncased` comme modèle de base
- La classification est binaire (2 classes : 0 et 1)
- Le batch size recommandé est 32
- Le learning rate recommandé est entre 2e-5 et 5e-5
- Le nombre d'epochs est fixé à 4
- Les fichiers CSV doivent être accessibles (dans `/content/` pour Colab ou dans le chemin spécifié)

## 🔧 Configuration recommandée

- **Python** ≥ 3.8
- **GPU** recommandé (CUDA) pour accélérer l'entraînement
- **RAM** : au moins 8 GB
- Compatible avec **Google Colab** (GPU T4 gratuit)

## 📖 Ressources supplémentaires

- [BERT Paper](https://arxiv.org/abs/1810.04805)
- [Hugging Face Course](https://huggingface.co/course)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)

---

**Bon courage pour le TP ! 🚀**
