language_codes=("ar" "cs" "es" "pt" "ru" "tr")
language_names=("Arabic" "Czech" "Spanish" "Portuguese" "Russian" "Turkish")

for i in "${!language_codes[@]}"; do
    langCode="${language_codes[i]}"
    langName="${language_names[i]}"

    python project.py data/en_pud-ud-test.conllu data/${langCode}_pud-ud-test.conllu alignments/en-${langCode}.intersect > output_new/${langCode}_deprel_tagged.conllu
    echo "------------------"
    echo "Evaluating ${langName}"
    python evaluator.py -m las -c data/${langCode}_pud-ud-test.conllu output_new/${langCode}_deprel_tagged.conllu
    #python evaluator.py -m deprel -j data/${langCode}_pud-ud-test.conllu output_new/${langCode}_deprel_tagged.conllu
done