# Homework assignment 4 - Part of Speech Harmonization

NPFL120 - Multilingual NLP

Antonije Petrović

# Assignment description

Tagset harmonization exercise:
- You get a syntactic parser trained on **the UD tagset** (UPOS and Universal Features), 
- and data tagged with a different tagset. 
- **Try to convert the tagset into the UD tagset** to get better results when applying the parser to the data.

Evaluation:
- UAS: unlabeled attachment score 
  - studies the structure of a dependency tree (testing if correct children are attached to correct parents)
- LAS: abeled attachment score 
  - requires a correct label for each attachment
  - i.e. I is nsubj, am is aux, now is advmod, etc.
  - shouldn't be higher than UAS

# Intro

I will be working on the harmonization of Penn Treebank tagset to UD tagset.

# Harmonization iterations

## 1. Initial

Without any changes. Baseline metrics.

Metrics:
- UAS: 15.21%
- LAS: 4.37%

## 2. Verbs

VB, VBD, VBG, VBN, VBP, VBZ -> `VERB`

Metrics:
- UAS: 25.20%
- LAS: 10.77%

## 3. Nouns

NN, NNS -> `NOUN`

Metrics:
- UAS: 35.90%
- LAS: 16.96%

## 4. Proper nouns

NNP, NNPS -> `PROPN`

Metrics:
- UAS: 39.06%
- LAS: 20.35%

## 5. Adjectives

JJ, JJR, JJS -> `ADJ`

Metrics:
- UAS: 43.65%
- LAS: 26.13%

## 6. Adverbs

RB, RBR, RBS -> `ADV`

Metrics: 
- UAS: 44.02%
- LAS: 28.01%

## 7. Determiner

Quite a common few words!

DT -> `DET`

Metrics:
- UAS: 49.44%
- LAS: 37.84%

## 8. Particles

RP -> `PART`

Metrics:
- UAS: 49.45%
- LAS: 37.71%

## 9. Numbers

CD -> `NUM`

Metrics:
- UAS: 50.21%
- LAS: 38.85%

## 10. Punctuation

. , ( ) ! ? ; : ' '' \`\` " -> `PUNCT`

Metrics:
- UAS: 54.18%
- LAS: 42.55%

## 11. Interjection

UH -> `INTJ`

Metrics:
- UAS: 54.33%
- LAS: 42.91%

## 12. Pronouns

PRP, PRP$, WDT, WP, WP$ -> `PRON`

Metrics:
- UAS: 56.51%
- LAS: 48.95%

## 13. Coordinating conjunctions

CC -> `CCONJ`

Metrics:
- UAS: 57.01%
- LAS: 49.60%

## 14. Foreign words

UD manual says that foreign words can be assigned real PoS tags if such tag is possible to assign. In other cases, `X` is used. There's now way of knowing an actual PoS tag in this simple harmonization approach, so I assign `X` always.

FW -> `X`

Metrics:
- UAS: 57.01%
- LAS: 49.58%

## 15. Existential there

EX -> `PRON`

Metrics:
- UAS: 56.97%
- LAS: 49.65%

## 16. List item markers

LS -> `NUM`

Metrics:
- UAS: 56.95%
- LAS: 49.66%

## 17. Modal verbs

MD -> `AUX`

Metrics:
- UAS: 57.45%
- LAS: 51.22%

## 18. Predeterminers 

PDT -> `DET`

Metrics:
- UAS: 57.51%
- LAS: 51.29%

## 19. Possessive ending

POS -> `PART`

Metrics:
- UAS: 57.49%
- LAS: 51.32%

## 20. "to"

TO -> `PART`

Metrics:
- UAS: 57.49%
- LAS: 21.32%

## 21. Other symbols

\$, \# -> `SYM`

Metrics:
- UAS: 57.57%
- LAS: 51.59%

## 22. WRB

We have two options. We can map WRB (wh-adverb) to either adverbs or subordinating conjunctions

Let's try the first option: WRB -> `ADV`

Metrics:
- UAS: 57.48%
- LAS: 51.53%

The second option: WRB -> `SCONJ`

Metrics:
- UAS: 57.71%
- LAS: 51.66%

So the second option works better!

## 23. IN

IN tag in Penn Treebank tagset means "preposition or subordinating conjunction".

IN -> `ADP`:

Metrics:
- UAS: 62.29%
- LAS: 58.11%

IN -> `SCONJ`:

Metrics:
- UAS: 58.54%
- LAS: 50.29%

So the first option is better!



# Conclusion

I've now mapped all Penn Treebank tags to UD tags. The only tag that is the same is `SYM` tag which I haven't modified.

We started from the metrics:

- UAS: 15.21%
- LAS: 4.37%

After harmonization, final metrics are:

- UAS: 62.29%
- LAS: 58.11%

This was done by considering only PoS tags, and not including other data that is available in the conllu format. Some of the mappings are not entirely accurate and depend on the context. As we have seen, WRB can be regarded either as ADV or SCONJ and IN can be mapped to ADP or SCONJ. This gives some ambiguity and the results depend on the choice of the mapping. 