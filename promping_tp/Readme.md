# README — tp_promping (version complète et simple)

Ce projet a pour objectif de présenter et comparer différents types de *prompts* et leurs résultats.

---

## 🎯 Objectif de ce TP

Le but de cet exercice (EPA) est de :

* Comprendre comment **se connecter à OpenRouter** pour exécuter des requêtes via une clé API ;
* Présenter les **différents types de prompts** utilisés dans les modèles de langage ;
* Comparer les **différentes manières de formuler un prompt** et observer les différences dans les résultats générés ;
* Manipuler concrètement les appels API dans un environnement Python / Jupyter Notebook.

---

## 🔑 1) Obtenir une clé API OpenRouter

1. Consulte ce lien : [https://openrouter.ai/settings/keys](https://openrouter.ai/settings/keys)
2. Crée un compte (ou connecte‑toi si tu en as déjà un).
3. Va dans **Settings → API Keys** et clique sur **Create Key**.
4. Copie la clé fournie (format `sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx`).

> ⚠️ **Ne partage jamais ta clé publique**. Traite‑la comme un mot de passe.

---

## 🧩 2) Ajouter ta clé dans le notebook

Dans le fichier **`tp_promping.ipynb`**, ajoute une cellule au début du notebook :

```python
# Colle ici ta clé OpenRouter (ne la partage pas publiquement)
api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx"


```

Une fois la clé ajoutée, tu peux **exécuter** le notebook normalement pour tester les requêtes et observer les réponses.

---

## 📚 3) Contenu du TP et notions abordées

Le notebook présente :

* Les **différents types de prompts** : instructions simples, questions guidées, contextuelles, formatées, etc.
* Les **techniques de prompting** : *zero-shot*, *few-shot*, *chain-of-thought*, *role prompting*, etc.
* Les **différences de formulation** et leur impact sur les résultats générés par le modèle.
* Des **exemples comparatifs** pour illustrer comment une légère variation dans le prompt peut influencer la réponse.

---

## 🧠 4) Objectif pédagogique

À la fin du TP, tu devras être capable de :

* Identifier les différents types de prompts et savoir quand les utiliser ;
* Adapter un prompt selon la tâche souhaitée ;
* Comprendre l’importance du contexte et de la formulation ;
* Faire des comparaisons entre les réponses selon la méthode de prompting utilisée.

---

## 🛡️ 5) Sécurité et bonnes pratiques

* Ne partage **jamais** ton notebook s’il contient ta clé.
* Si tu veux le partager, **supprime la clé** ou remplace‑la par une valeur factice (`"sk-demo-key"`).
* Si tu penses que ta clé a fuité, révoque‑la immédiatement sur [OpenRouter](https://openrouter.ai/settings/keys) et crée‑en une nouvelle.

---

## ✅ 6) Résumé rapide des étapes

1. Aller sur [openrouter.ai/settings/keys](https://openrouter.ai/settings/keys)
2. Créer une clé et la copier.
3. Ouvrir le notebook `tp_promping.ipynb`.
4. Coller la clé dans la variable `api_key`.
5. Exécuter les cellules pour observer et comparer les résultats des différents types de prompts.

---

**Fin du README.**
