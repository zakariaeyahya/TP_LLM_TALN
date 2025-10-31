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
