language_codes=("ar" "cs" "de" "en" "es" "fi" "fr" "hi" "it" "ja" "pt" "ru" "sv" "tr" "zh")
language_names=("Arabic" "Czech" "German" "English" "Spanish" "Finnish" "French" "Hindi" "Italian" "Japanese" "Portuguese" "Russian" "Swedish" "Turkish" "Chinese")

for i in "${!language_codes[@]}"; do
    langCode="${language_codes[i]}"
    langName="${language_names[i]}"

    python conllu2vectors.py bert-base-multilingual-uncased < data/${langCode}_pud-ud-test.conllu > embeddings/${langCode}_pud.mbert

    echo "Done Conllu2Vectors for ${langName}"
done