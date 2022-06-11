language_codes=("ar" "cs" "de" "en" "es" "fi" "fr" "hi" "it" "pt" "ru" "sv" "tr" "zh")
language_names=("Arabic" "Czech" "German" "English" "Spanish" "Finnish" "French" "Hindi" "Italian" "Portuguese" "Russian" "Swedish" "Turkish" "Chinese")

for i in "${!language_codes[@]}"; do

    langCode="${language_codes[i]}"
    langName="${language_names[i]}"

    echo "Model: ${langName}"
    for j in "${!language_codes[@]}"; do
        tgtCode="${language_codes[j]}"

        #echo "    Accuracy on ${language_names[j]}"
        score=`python eval_mlp.py models/${langCode}_pud.mbert.model < embeddings/${tgtCode}_pud.mbert`
        echo "    ${score}"
    done
done