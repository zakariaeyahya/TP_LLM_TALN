import pandas as pd
import os

def demonstrate_teacher_forcing_from_csv(file_path):
    """
    Charge un dataset depuis un fichier CSV, prend la première phrase générée
    et illustre comment les données sont préparées pour le "teacher forcing".
    """
    # --- 1. Vérification et lecture du fichier ---
    print(f"Tentative de lecture du fichier : {file_path}")

    if not os.path.exists(file_path):
        print("\n" + "="*60)
        print(f"ERREUR : Fichier non trouvé !")
        print(f"Le chemin d'accès '{file_path}' ne semble pas exister.")
        print("Veuillez vérifier que le fichier est bien à cet emplacement.")
        print("="*60)
        return

    try:
        df = pd.read_csv(file_path)
        print("Fichier CSV chargé avec succès.\n")
        # --- Ajout pour le débogage : Afficher les colonnes trouvées ---
        print(f"Colonnes trouvées dans le fichier : {df.columns.tolist()}\n")
    except Exception as e:
        print(f"\nERREUR lors de la lecture du fichier CSV : {e}")
        return

    # --- 2. Sélection et préparation d'une phrase d'exemple ---
    # MODIFICATION : Utilisons la colonne 'text'. Si ce n'est pas la bonne,
    # la ligne ci-dessus vous donnera le nom correct à utiliser.
    column_name_to_use = 'generated_response' # <-- MODIFIEZ CECI si le nom est différent

    if column_name_to_use not in df.columns:
        print(f"ERREUR: La colonne '{column_name_to_use}' n'a pas été trouvée.")
        print("Veuillez vérifier la liste des colonnes affichée ci-dessus et mettre à jour")
        print("la variable 'column_name_to_use' dans le script.")
        return

    # --- AMÉLIORATION : Chercher une phrase courte pour une démo plus claire ---
    # On calcule le nombre de mots pour chaque phrase
    df['word_count'] = df[column_name_to_use].str.split().str.len()
    
    # On cherche les phrases de moins de 15 mots
    short_sentences_df = df[df['word_count'] < 15]
    
    if not short_sentences_df.empty:
        # AMÉLIORATION 2 : Choisir une phrase courte AU HASARD pour une démo dynamique
        example_text = short_sentences_df.sample(n=1)[column_name_to_use].iloc[0]
    else:
        # Fallback si aucune phrase courte n'est trouvée: prendre une phrase au hasard dans le df complet
        example_text = df.sample(n=1)[column_name_to_use].iloc[0]

    # --- 3. Création des séquences pour le Teacher Forcing ---
    # On transforme la phrase en "tokens" (ici, des mots)
    # et on ajoute les marqueurs de début (<start>) et de fin (<end>)
    tokens = ["<start>"] + example_text.split() + ["<end>"]

    # L'INPUT pour le modèle : la séquence complète, sauf le tout dernier token.
    input_sequence = tokens[:-1]

    # Le TARGET (la cible) : la séquence complète décalée d'un cran.
    # C'est ce que le modèle doit apprendre à prédire à chaque étape.
    target_sequence = tokens[1:]

    # --- 4. Affichage pédagogique du résultat ---
    print("="*60)
    print("ILLUSTRATION DU TEACHER FORCING")
    print("="*60)
    print(f"Phrase d'exemple tirée du CSV :\n'{example_text}'")
    print("-"*60)
    print(f"Input pour le modèle :\n{input_sequence}")
    print("\n")
    print(f"Cible (vérité terrain) à prédire :\n{target_sequence}")
    print("-"*60)
    print("\nDéroulement de l'entraînement (étape par étape) :\n")
    for i in range(len(input_sequence)):
        current_input = " ".join(input_sequence[:i+1])
        expected_output = target_sequence[i]
        print(f"- Le modèle reçoit : '{current_input}'")
        print(f"  ... et doit prédire : '{expected_output}'\n")


# --- Point d'entrée du script ---
if __name__ == "__main__":
    # IMPORTANT : Assurez-vous que ce chemin est correct sur votre ordinateur.
    # L'utilisation de r"..." est une bonne pratique sur Windows pour éviter les problèmes avec les '\'.
    dataset_path = r"C:\Users\Hiba\Desktop\S9\belcaid\TP_LLM_TALN\teacher forcing\ManaGPT-1020_4080_prompts_and_generated_texts.csv"
    
    demonstrate_teacher_forcing_from_csv(dataset_path)
