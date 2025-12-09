# TP_LLM_TALN - Fine-Tuning BERT pour la Classification de Tweets

## 📌 Vue d'ensemble

Ce dépôt contient un **Travaux Pratiques (TP)** complet sur le fine-tuning du modèle BERT pour la classification binaire de tweets. Le notebook principal (`Bert_cassification (1).ipynb`) a été préparé comme un exercice pédagogique avec **5 sections TODO** que les étudiants doivent compléter.

**Objectif du TP :** Apprendre à fine-tuner BERT pour prédire le label (`target`) associé à chaque tweet (`text`) à partir d'un ensemble de données d'entraînement.

**Problème à résoudre :** Classification binaire de tweets pour déterminer si un tweet décrit une vraie catastrophe (target=1) ou non (target=0).

---

## 📁 Structure du dépôt

```
TP_LLM_TALN/
├── Fine-Tuning_BERT/
│   ├── notebooks/
│   │   └── Bert_cassification (1).ipynb    # Notebook principal avec 5 sections TODO
│   ├── data/
│   │   ├── train.csv                        # 7613 tweets d'entraînement avec labels
│   │   └── test.csv                         # 3263 tweets de test à prédire
│   ├── submission/
│   │   └── sample_submission.csv            # Format de soumission attendu
│   ├── models/                              # Dossier pour sauvegarder les modèles
│   └── README.md                            # Documentation spécifique au module
├── requirements.txt                          # Dépendances Python du projet
└── README.md                                # Ce fichier (guide d'utilisation)
```

---

## 🚀 Installation et Configuration

### Prérequis

- **Python** ≥ 3.8
- **GPU** recommandé (CUDA) pour accélérer l'entraînement (optionnel mais fortement recommandé)
- **RAM** : au moins 8 GB
- **Espace disque** : ~2 GB pour les modèles et données

### Option 1 : Google Colab (Recommandé pour débuter)

**Avantages :** GPU gratuit (T4), pas d'installation locale, environnement pré-configuré

#### Étapes :

1. **Télécharger le notebook**
   - Téléchargez `Fine-Tuning_BERT/notebooks/Bert_cassification (1).ipynb`

2. **Ouvrir sur Google Colab**
   - Allez sur [Google Colab](https://colab.research.google.com/)
   - Cliquez sur "Upload" et sélectionnez le notebook

3. **Configurer le runtime**
   - Menu : `Runtime` → `Change runtime type`
   - Sélectionnez `GPU` dans "Hardware accelerator"
   - Cliquez sur "Save"

4. **Uploadez les données**
   - Créez un dossier `/content/` (automatique sur Colab)
   - Uploadez `train.csv` et `test.csv` dans `/content/`
   - Ou utilisez le code suivant dans une cellule :
   ```python
   from google.colab import files
   uploaded = files.upload()  # Sélectionnez train.csv et test.csv
   ```

5. **Exécuter les cellules**
   - La première cellule installe automatiquement les dépendances
   - Exécutez les cellules une par une avec `Shift + Enter`

### Option 2 : Installation locale (Windows / PowerShell)

#### Étape 1 : Créer un environnement virtuel

```powershell
# Naviguer vers le dossier du projet
cd D:\bureau\BD_AI1\ci3\taln\TP\TP_LLM_TALN

# Créer l'environnement virtuel
python -m venv .venv

# Activer l'environnement
.\.venv\Scripts\Activate.ps1
```

**Note :** Si vous obtenez une erreur d'exécution de scripts, exécutez :
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Étape 2 : Installer les dépendances

```powershell
# Mettre à jour pip
pip install --upgrade pip

# Installer les dépendances depuis requirements.txt
pip install -r requirements.txt
```

**Note importante pour PyTorch avec GPU :**
- Si vous avez une carte graphique NVIDIA avec CUDA, installez PyTorch avec support GPU :
```powershell
# Pour CUDA 11.8 (vérifiez votre version CUDA)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Pour CUDA 12.1
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# Pour CPU uniquement (plus lent mais fonctionne)
pip install torch torchvision torchaudio
```

#### Étape 3 : Télécharger les données NLTK

Lancez Python et exécutez :

```python
import nltk
nltk.download('stopwords')
```

#### Étape 4 : Lancer Jupyter Notebook

```powershell
jupyter notebook
```

Le navigateur s'ouvrira automatiquement. Naviguez vers :
`Fine-Tuning_BERT/notebooks/Bert_cassification (1).ipynb`

#### Étape 5 : Modifier les chemins des fichiers CSV

Dans le notebook, modifiez la cellule 3 :

**Pour Colab :**
```python
df = pd.read_csv("/content/train.csv")
```

**Pour exécution locale :**
```python
df = pd.read_csv("../data/train.csv")  # Chemin relatif depuis le notebook
# OU
df = pd.read_csv("D:/bureau/BD_AI1/ci3/taln/TP/TP_LLM_TALN/Fine-Tuning_BERT/data/train.csv")  # Chemin absolu
```

Faites de même pour `test.csv` dans la cellule 25.

---

## 📊 Format des données

### `train.csv`

Structure attendue :
- **id** : Identifiant unique du tweet
- **keyword** : Mot-clé optionnel (peut être vide)
- **location** : Localisation optionnelle (peut être vide)
- **text** : Le texte du tweet (colonne d'entrée principale)
- **target** : Le label binaire (0 ou 1) - colonne cible

**Exemple :**
```csv
id,keyword,location,text,target
1,,,Our Deeds are the Reason of this #earthquake May ALLAH Forgive us all,1
4,,,Forest fire near La Ronge Sask. Canada,1
```

### `test.csv`

Structure attendue :
- **id** : Identifiant unique du tweet
- **keyword** : Mot-clé optionnel
- **location** : Localisation optionnelle
- **text** : Le texte du tweet à prédire

**Exemple :**
```csv
id,keyword,location,text
0,,,Just happened a terrible car crash
2,,,Heard about #earthquake is different cities, stay safe everyone.
```

### Prétraitement automatique

Le notebook applique automatiquement la fonction `clean_text()` qui :
- ✅ Convertit le texte en minuscules
- ✅ Supprime les URLs (http://, https://)
- ✅ Supprime les balises HTML
- ✅ Supprime les ponctuations spéciales
- ✅ Supprime les stopwords anglais (the, a, an, etc.)
- ✅ Supprime les emojis

---

## 📚 Guide d'utilisation du notebook

### Workflow complet

Le notebook suit cette séquence logique :

1. **Installation des dépendances** (Cellule 0)
2. **Import des bibliothèques** (Cellule 1)
3. **Configuration du device** (Cellule 2) - CPU ou GPU
4. **Chargement des données** (Cellule 3)
5. **Prétraitement des textes** (Cellules 4-7)
6. **Tokenization BERT** (Cellules 9-13) - **TODO #1**
7. **Création du dataset et split** (Cellule 15)
8. **Création des DataLoaders** (Cellule 16) - **TODO #2**
9. **Chargement du modèle BERT** (Cellule 17)
10. **Configuration de l'optimiseur** (Cellule 18) - **TODO #3**
11. **Configuration du scheduler** (Cellule 20) - **TODO #4**
12. **Boucle d'entraînement** (Cellule 23) - **TODO #5**
13. **Sauvegarde du meilleur modèle** (automatique)
14. **Chargement et prédictions** (Cellules 24-27)
15. **Génération de submission.csv** (Cellule 27)

---

## 🔍 Détails des sections TODO

### TODO #1 : Tokenization et padding (Cellule 13)

**Objectif :** Tokeniser tous les tweets en batch avec padding et truncation.

**Questions à répondre :**
- Comment calculer `max_len` pour que toutes les séquences aient la même longueur ?
- Quelle est la limite maximale de BERT (512 tokens) et pourquoi faut-il la respecter ?
- Quels paramètres utiliser dans `tokenizer()` pour :
  - Ajouter les tokens spéciaux `[CLS]` et `[SEP]` ?
  - Remplir les séquences courtes (padding) ?
  - Tronquer les séquences trop longues ?
  - Obtenir les attention masks et les tenseurs PyTorch ?

**Indices :**
```python
# Calcul de max_len
max_len = max([len(tokenizer.encode(str(s), add_special_tokens=True)) for s in tweets])
max_len = min(max_len, 512)  # Limite de BERT

# Tokenization en batch
encoded = tokenizer(
    list(tweets),
    add_special_tokens=True,    # Ajoute [CLS] et [SEP]
    padding='max_length',       # Remplit jusqu'à max_len
    truncation=True,            # Tronque si > max_len
    max_length=max_len,
    return_attention_mask=True,  # Retourne les masks
    return_tensors='pt'         # Tenseurs PyTorch
)

# Extraction
input_ids = encoded['input_ids']
attention_masks = encoded['attention_mask']
labels = torch.tensor(labels)
```

---

### TODO #2 : DataLoaders (Cellule 16)

**Objectif :** Créer les DataLoaders pour l'entraînement et la validation.

**Questions à répondre :**
- Quelle taille de batch est recommandée pour le fine-tuning de BERT (16 ou 32) ?
- Quel sampler utiliser pour l'entraînement : `RandomSampler` ou `SequentialSampler` ? Pourquoi ?
- Quel sampler utiliser pour la validation ? Pourquoi l'ordre n'a pas d'importance ici ?

**Indices :**
```python
batch_size = 32  # Recommandé pour BERT

# Pour l'entraînement : RandomSampler (mélange les données)
train_dataloader = DataLoader(
    train_dataset,
    sampler=RandomSampler(train_dataset),  # Mélange aléatoire
    batch_size=batch_size
)

# Pour la validation : SequentialSampler (ordre séquentiel)
validation_dataloader = DataLoader(
    val_dataset,
    sampler=SequentialSampler(val_dataset),  # Ordre fixe
    batch_size=batch_size
)
```

**Explication :**
- **RandomSampler** : Mélange les données à chaque epoch pour améliorer l'apprentissage
- **SequentialSampler** : Garde l'ordre fixe, suffisant pour la validation où on ne fait pas de gradient descent

---

### TODO #3 : Optimiseur AdamW (Cellule 18)

**Objectif :** Configurer l'optimiseur AdamW avec les bons paramètres.

**Questions à répondre :**
- Quels paramètres faut-il définir pour l'optimiseur AdamW ?
- Quel learning rate est approprié pour le fine-tuning de BERT ?
  - Valeur recommandée : entre 2e-5 et 5e-5
- Quel est le rôle du paramètre `eps` (epsilon) dans AdamW ?

**Indices :**
```python
from torch.optim import AdamW

optimizer = AdamW(
    model.parameters(),  # Paramètres à optimiser
    lr=2e-5,             # Learning rate (2e-5 à 5e-5 pour BERT)
    eps=1e-8             # Epsilon pour la stabilité numérique
)
```

**Explication :**
- **Learning rate (lr)** : Taux d'apprentissage. Trop élevé = instabilité, trop bas = apprentissage lent
- **Epsilon (eps)** : Petite valeur pour éviter la division par zéro dans les calculs d'AdamW

---

### TODO #4 : Scheduler de learning rate (Cellule 20)

**Objectif :** Calculer le nombre total de steps et créer le scheduler avec warmup.

**Questions à répondre :**
- Comment calculer le nombre total de steps d'entraînement ?
- Pourquoi ce n'est pas simplement `nombre d'échantillons × nombre d'epochs` ?
- Quelle fonction utiliser pour créer un scheduler de learning rate avec warmup ?
- Quels sont les deux paramètres principaux à fournir ?

**Indices :**
```python
from transformers import get_linear_schedule_with_warmup

# Calcul du nombre total de steps
# C'est le nombre de BATCHES, pas d'échantillons !
total_steps = len(train_dataloader) * epochs

# Création du scheduler
scheduler = get_linear_schedule_with_warmup(
    optimizer,                    # L'optimiseur à scheduler
    num_warmup_steps=0,           # Nombre de steps de "warmup" (0 = pas de warmup)
    num_training_steps=total_steps  # Nombre total de steps d'entraînement
)
```

**Explication :**
- **Total steps** : Nombre de batches × epochs (pas d'échantillons × epochs)
- **Warmup** : Période où le learning rate augmente progressivement au début
- **Linear schedule** : Le learning rate diminue linéairement après le warmup

---

### TODO #5 : Boucle d'entraînement (Cellule 23)

**Objectif :** Implémenter une étape d'entraînement complète dans le bon ordre.

**Questions à répondre :**
- Dans quel ordre faut-il exécuter les opérations suivantes ?
  1. Réinitialiser les gradients
  2. Calculer la perte (loss) avec le modèle
  3. Effectuer la rétropropagation (backward)
  4. Clipper les gradients (pourquoi est-ce important ?)
  5. Mettre à jour les paramètres avec l'optimiseur
  6. Mettre à jour le scheduler du learning rate

**Indices :**
```python
for step, batch in enumerate(train_dataloader):
    b_input_ids = batch[0].to(device)
    b_input_mask = batch[1].to(device)
    b_labels = batch[2].to(device)
    
    # 1. Réinitialiser les gradients (important !)
    optimizer.zero_grad()
    
    # 2. Forward pass : calculer la loss
    outputs = model(
        b_input_ids,
        token_type_ids=None,
        attention_mask=b_input_mask,
        labels=b_labels
    )
    loss = outputs.loss
    total_train_loss += loss.item()
    
    # 3. Backward pass : calculer les gradients
    loss.backward()
    
    # 4. Clipper les gradients (évite l'explosion des gradients)
    torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
    
    # 5. Mettre à jour les paramètres
    optimizer.step()
    
    # 6. Mettre à jour le learning rate
    scheduler.step()
```

**Explication de l'ordre :**
1. **zero_grad()** : Efface les gradients de l'itération précédente
2. **Forward** : Calcule la loss avec les données actuelles
3. **Backward** : Calcule les gradients via backpropagation
4. **Clip grad** : Limite la norme des gradients (évite l'explosion)
5. **Optimizer step** : Met à jour les poids du modèle
6. **Scheduler step** : Met à jour le learning rate

**Pourquoi clipper les gradients ?**
Les gradients trop grands peuvent causer l'instabilité de l'entraînement. Le clipping limite leur amplitude.

---

## 🎯 Exécution étape par étape

### Étape 1 : Préparation

1. Ouvrez le notebook dans Jupyter ou Colab
2. Vérifiez que les chemins vers `train.csv` et `test.csv` sont corrects
3. Exécutez les cellules 0-2 pour installer et importer

### Étape 2 : Chargement et prétraitement

1. Exécutez la cellule 3 pour charger les données
2. Vérifiez avec `df.head()` que les données sont bien chargées
3. Exécutez les cellules 4-8 pour le prétraitement

### Étape 3 : Tokenization (TODO #1)

1. Exécutez les cellules 9-12 pour comprendre la tokenization
2. **Complétez la cellule 13** avec votre code
3. Vérifiez que `input_ids`, `attention_masks` et `labels` sont bien créés

### Étape 4 : Dataset et DataLoaders (TODO #2)

1. Exécutez la cellule 15 pour créer le dataset et le split
2. **Complétez la cellule 16** avec les DataLoaders
3. Vérifiez que `train_dataloader` et `validation_dataloader` sont créés

### Étape 5 : Modèle et optimiseur

1. Exécutez la cellule 17 pour charger le modèle BERT
2. **Complétez la cellule 18** avec l'optimiseur AdamW
3. **Complétez la cellule 20** avec le scheduler

### Étape 6 : Entraînement (TODO #5)

1. Les cellules 21-22 définissent des fonctions utilitaires (accuracy, format_time)
2. **Complétez la cellule 23** avec la boucle d'entraînement
3. Exécutez la cellule et observez l'entraînement

**Ce que vous devriez voir :**
```
======== Epoch 1 / 4 ========
Training...

  Average training loss: 0.16
  Training epoch took: 0:00:51

Running Validation...
  Accuracy: 0.81
```

### Étape 7 : Prédictions

1. Exécutez la cellule 24 pour charger le meilleur modèle sauvegardé
2. Exécutez les cellules 25-27 pour faire les prédictions sur le test
3. Vérifiez que `submission.csv` est créé

---

## 📈 Interprétation des résultats

### Métriques d'entraînement

- **Training Loss** : Doit diminuer au fil des epochs
  - Si elle augmente : learning rate trop élevé ou problème dans le code
  - Si elle stagne : learning rate trop bas

- **Validation Accuracy** : Mesure la performance sur des données non vues
  - Objectif : > 0.80 (80%)
  - Si training loss diminue mais accuracy stagne : overfitting

### Fichiers générés

- **`bert_model_state.bin`** : Poids du meilleur modèle (selon validation accuracy)
- **`submission.csv`** : Prédictions sur le jeu de test au format :
  ```csv
  id,target
  0,1
  2,0
  3,1
  ...
  ```

---

## 🐛 Dépannage (Troubleshooting)

### Problème 1 : "FileNotFoundError: train.csv"

**Solution :**
- Vérifiez le chemin du fichier dans la cellule 3
- Pour Colab : `/content/train.csv`
- Pour local : `../data/train.csv` ou chemin absolu

### Problème 2 : "CUDA out of memory"

**Solutions :**
- Réduisez `batch_size` de 32 à 16 ou 8
- Réduisez `max_len` si possible
- Utilisez CPU (plus lent mais fonctionne)

### Problème 3 : "ModuleNotFoundError: No module named 'transformers'"

**Solution :**
```powershell
pip install transformers
# Ou réinstallez toutes les dépendances
pip install -r requirements.txt
```

### Problème 4 : "NameError: name 'encoded' is not defined"

**Solution :**
- Vous avez oublié de compléter TODO #1
- Assurez-vous que la variable `encoded` est créée avant d'extraire `input_ids`

### Problème 5 : "RuntimeError: Expected all tensors to be on the same device"

**Solution :**
- Assurez-vous que les données sont sur le même device que le modèle :
```python
b_input_ids = batch[0].to(device)
b_input_mask = batch[1].to(device)
b_labels = batch[2].to(device)
```

### Problème 6 : L'entraînement est très lent

**Solutions :**
- Utilisez un GPU (Colab ou local avec CUDA)
- Réduisez le nombre d'epochs pour tester
- Réduisez `batch_size` si vous manquez de mémoire

---

## 💡 Conseils et bonnes pratiques

### Pour compléter les TODO

1. **Lisez attentivement les questions** dans chaque section
2. **Consultez la documentation** :
   - [Hugging Face Transformers](https://huggingface.co/docs/transformers)
   - [PyTorch DataLoader](https://pytorch.org/docs/stable/data.html)
   - [AdamW Optimizer](https://pytorch.org/docs/stable/optim.html#torch.optim.AdamW)
3. **Testez votre code étape par étape** : ne complétez pas tout d'un coup
4. **Vérifiez les erreurs** : les messages d'erreur Python sont souvent très utiles
5. **Utilisez les cellules de test** : créez des cellules pour tester votre code avant de l'intégrer

### Optimisation

- **Batch size** : 32 est optimal, mais 16 fonctionne aussi
- **Learning rate** : 2e-5 est un bon point de départ
- **Epochs** : 4 est suffisant, plus peut causer de l'overfitting
- **Max length** : Utilisez la longueur détectée (souvent ~45) plutôt que 512 pour accélérer

---

## 📖 Ressources supplémentaires

### Documentation officielle

- [BERT Paper](https://arxiv.org/abs/1810.04805) - Article original de BERT
- [Hugging Face Transformers](https://huggingface.co/docs/transformers) - Documentation complète
- [Hugging Face Course](https://huggingface.co/course) - Cours gratuit sur les transformers
- [PyTorch Tutorials](https://pytorch.org/tutorials/) - Tutoriels PyTorch

### Vidéos et tutoriels

- [Fine-tuning BERT for Text Classification](https://www.youtube.com/results?search_query=bert+fine-tuning)
- [PyTorch DataLoader Tutorial](https://pytorch.org/tutorials/beginner/data_loading_tutorial.html)

### Articles utiles

- [The Illustrated BERT](https://jalammar.github.io/illustrated-bert/)
- [How to Fine-Tune BERT for Text Classification](https://arxiv.org/abs/1905.05583)

---

## 🎯 Objectifs pédagogiques

En complétant ce TP, vous apprendrez à :

- ✅ Utiliser le tokenizer BERT pour préparer les données textuelles
- ✅ Créer des DataLoaders PyTorch avec les bons samplers
- ✅ Configurer un optimiseur AdamW adapté au fine-tuning de BERT
- ✅ Utiliser un scheduler de learning rate avec warmup
- ✅ Implémenter une boucle d'entraînement complète avec gradient clipping
- ✅ Évaluer un modèle et sauvegarder les meilleurs poids
- ✅ Générer des prédictions sur un jeu de test
- ✅ Comprendre les concepts de padding, truncation, attention masks

---

## 📝 Notes importantes

### Configuration recommandée

- **Modèle** : `bert-base-uncased` (12 couches, 110M paramètres)
- **Classification** : Binaire (2 classes : 0 et 1)
- **Batch size** : 32 (ou 16 si mémoire limitée)
- **Learning rate** : 2e-5 (entre 2e-5 et 5e-5)
- **Epochs** : 4
- **Max sequence length** : Détecté automatiquement (souvent ~45), limité à 512

### Fichiers à ne pas modifier

- `clean_text()` : Fonction de prétraitement (cellule 6)
- `flat_accuracy()` : Fonction de calcul d'accuracy (cellule 21)
- `format_time()` : Fonction de formatage du temps (cellule 22)
- La structure de la boucle d'entraînement (cellule 23) - seulement compléter la partie TODO

---

## 🔧 Configuration avancée

### Modifier les hyperparamètres

Si vous voulez expérimenter, vous pouvez modifier :

```python
# Dans la cellule 20
epochs = 4  # Essayez 2, 3, ou 5

# Dans la cellule 16
batch_size = 32  # Essayez 16, 8, ou 64

# Dans la cellule 18 (après TODO #3)
optimizer = AdamW(
    model.parameters(),
    lr=2e-5,  # Essayez 1e-5, 3e-5, ou 5e-5
    eps=1e-8
)

# Dans la cellule 20 (après TODO #4)
scheduler = get_linear_schedule_with_warmup(
    optimizer,
    num_warmup_steps=100,  # Essayez 0, 100, ou 200
    num_training_steps=total_steps
)
```

### Utiliser un autre modèle

Vous pouvez essayer d'autres modèles BERT :

```python
# DistilBERT (plus rapide, plus petit)
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer
model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=2)
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased', do_lower_case=True)

# RoBERTa (souvent meilleur que BERT)
from transformers import RobertaForSequenceClassification, RobertaTokenizer
model = RobertaForSequenceClassification.from_pretrained('roberta-base', num_labels=2)
tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
```

---

## 📞 Support et questions

### En cas de problème

1. **Vérifiez les erreurs** : Les messages d'erreur Python contiennent souvent la solution
2. **Consultez la documentation** : Les liens dans "Ressources supplémentaires"
3. **Comparez avec le code de référence** : Vérifiez que vous avez bien suivi les indices
4. **Testez étape par étape** : Ne complétez pas tous les TODO d'un coup

### Questions fréquentes

**Q : Combien de temps prend l'entraînement ?**
R : Sur GPU (Colab T4) : ~3-4 minutes pour 4 epochs. Sur CPU : 30-60 minutes.

**Q : Pourquoi mon accuracy ne dépasse pas 0.75 ?**
R : Vérifiez que vous avez bien complété tous les TODO. Le code doit être correct.

**Q : Puis-je utiliser mes propres données ?**
R : Oui ! Assurez-vous que vos CSV ont les colonnes `text` et `target` (pour train.csv).

**Q : Le modèle sauvegarde-t-il automatiquement ?**
R : Oui, le meilleur modèle (selon validation accuracy) est sauvegardé dans `bert_model_state.bin`.

---

## 🎓 Conclusion

Ce TP vous permet de maîtriser les concepts fondamentaux du fine-tuning de BERT pour la classification de texte. Une fois complété, vous serez capable de :

- Adapter BERT à vos propres tâches de classification
- Comprendre le pipeline complet de fine-tuning
- Optimiser les hyperparamètres pour de meilleures performances

**Bon courage pour le TP ! 🚀**

---

*Dernière mise à jour : 2024*

