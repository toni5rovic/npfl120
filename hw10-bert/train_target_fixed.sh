language_codes=("ar" "cs" "de" "en" "fi" "fr" "hi" "it" "pt" "ru" "sv" "tr" "zh")
language_names=("Arabic" "Czech" "German" "English" "Finnish" "French" "Hindi" "Italian" "Portuguese" "Russian" "Swedish" "Turkish" "Chinese")

for i in "${!language_codes[@]}"; do
    langCode="${language_codes[i]}"
    langName="${language_names[i]}"

    python train_mlp.py models/${langCode}_pud.mbert.model < embeddings/${langCode}_pud.mbert
    
    echo "Evaluating model trained on ${langName}"

    python eval_mlp.py models/${langCode}_pud.mbert.model < embeddings/es_pud.mbert
done

