# Homework assignment 9 - Word Embeddings

NPFL120 - Multilingual NLP

Antonije Petrović

# Report

I chose to work with Spanish and Serbian. I downloaded FastText embeddings in the textual format and performed a cross-lingual mapping of the embeddings with VecMap tool. Because the original embeddings files contain 2 million entries, I used only the first 100k entries. Then, I used OpenSubtitles dictionary between these two languages, downloaded from the OPUS website. The dictionary is then cleaned with:

`cut -f 3,4 es-sr-dict | awk 'NF' | tr -s '\t' ' ' | awk -F " " "NF<=2" > dict_processed.txt`

- This chain of commands first extracts 3rd and 4th column of the original tab separated dictionary, then removes all the empty lines with awk. After that, all tabs are replaced by spaces because that's the format that VecMap expects. But now, entries with multiple words on the source or the target side can occur so we remove all of the entries in the dictionary which have multiple words. So we are left with the processed dictionary which contains only word-word translations.

Now we can run VecMap on the original FastText embeddings of Spanish and Serbian, and using the processed dictionary (`supervised` option of VecMap).

VecMap produces two embeddings files and then we concatenate them to create a single bilingual embeddings file.

# Experiments

Now let's take a look at the experiments.

| Experiments                                | Spanish                  | Portuguese               | Italian                  | Serbian                  | Croatian                 | Bulgarian                |
| ------------------------------------------ | ------------------------ | ------------------------ | ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| Spanish UDPipe baseline                    | UAS: 89.15%, LAS: 85.08% | UAS: 54.83%, LAS: 43.12% | UAS: 72.53%, LAS: 64.33% | UAS: 54.08%, LAS: 42.38% | UAS: 51.73%, LAS: 40.61% | UAS: 66.72%, LAS: 55.44% |
| Spanish data, no embeddings                | UAS: 78.86%, LAS: 72.90% | UAS: 27.41%, LAS: 21.06% | UAS: 71.70%, LAS: 63.80% | UAS: 45.29%, LAS: 28.47% | UAS: 45.25%, LAS: 28.52% | UAS: 61.65%, LAS: 50.50% |
| Spanish data, bilingual embeddings         | UAS: 81.53%, LAS: 76.35% | UAS: 39.73%, LAS: 30.75% | UAS: 73.16%, LAS: 65.78% | UAS: 44.52%, LAS: 31.84% | UAS: 43.94%, LAS: 31.64% | UAS: 63.76%, LAS: 52.00% |
| Spanish+Serbian data, no embeddings        | UAS: 73.90%, LAS: 68.20% | UAS: 40.40%, LAS: 31.97% | UAS: 70.41%, LAS: 63.38% | UAS: 66.31%, LAS: 59.58% | UAS: 64.08%, LAS: 56.92% | UAS: 68.60%, LAS: 59.11% |
| Spanish+Serbian data, bilingual embeddings | UAS: 78.74%, LAS: 72.30% | UAS: 34.41%, LAS: 24.79% | UAS: 71.01%, LAS: 63.90% | UAS: 73.81%, LAS: 67.05% | UAS: 70.04%, LAS: 62.35% | UAS: 69.39%, LAS: 59.45% |

I decided to evaluate on 6 languages. 2 of them are Spanish and Serbian, which are used for creating bilingual embeddings and are used as training data. On the other hand, I also evaluate on two other Romance languages and two other Slavic languages. It's worth noting that Bulgarian data is the only one using cyrillic script.

I trained 4 models (all models are trained for 1 iteration only):
1. Training on Spanish data, without embeddings
    - This model is my baseline, since comparing to the released UDPipe model is not good since that model is quite optimized and trained for longer.
2. Training on Spanish data, bilingual embeddings
    - This model gives better results for almost all languages
    - For Serbian and Croatian we see a slight drop in UAS
3. Training on Spanish+Serbian data, without embeddings
    - We get a lower performance on Spanish and Italian, while Portuguese actually performs slightly better than the model 2. 
    - With Slavic languages, Serbian of course performs much better because it is included in the training data, and therefore Croatian as very related language performs better as well. Bulgarian, as a close and related language, also profits from this.
4. Training on Spanish+Serbian data, bilingual embeddings
    - This model performs the best for Slavic languages. 
    - At the same time, it is worse than the baseline Spanish-trained model for all Romance languages.