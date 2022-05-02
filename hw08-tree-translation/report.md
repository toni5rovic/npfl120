# Homework assignment 8 - Tree Translation

NPFL120 - Multilingual NLP

Antonije Petrović

# Assignment description

- Take a pair of languages with alignments
- Translate each word from the source treebank to its most frequent target counterpart using parallel data (`translate_treebank.py`)
- Train UDPipe parser on that:
- `udpipe --train --tokenizer=none --tagger=none out.model < train.conllu`
- Evaluate the parser on the target evaluation trebank:
- `udpipe --parse --accuracy out.model < dev.conllu`

Possible improvements:
- better word alignment (i.e. FastAlign)
- use the source POS tags and/or morpological features
- use multiple source languages (i.e. concatenate source treebanks)
- use proper MT system
- use your knowledge of the target language
- guess some translations for unknown words
- pre-train target language word embeddings with word2vec (on some target language plaintext, can be target side of the parallel data or anything else). Or download FastText word embeddings (use text format) and use it in UDPipe while training

# Report 

I worked on Slovenian-Croatian language pair.

- Accuracy of the submitted VarDial model: UAS=61.33%, LAS=46.58%
- Baseline (default `translate_treebank.py`): 
  - trained for 1 epoch only
  - Results: UAS=59.83%, LAS=46.13%
- Baseline (default `translate_treebank.py`):
  - trained for 5 epochs
  - Results: UAS=63.91%, LAS=49.28%
- Using fasttext word embeddings: 
  - trained for 1 epoch only
  - command: `udpipe --train --parser="iterations=1;embedding_form_file=cc.hr.300.vec" --tokenizer=none --tagger=none models/fake-hr.model < output/fake-hr.conllu`
  - Results: UAS: 63.39%, LAS: 48.12%
- Using fasttext word embeddings: 
  - trained for 5 epochs
  - Results: UAS: 63.08%, LAS: 48.29%
- Using FastAlign alignments: 
  - script `prepare_parallel.sh`
    - Parse and tokenize the Watchtower data in Slovenian and Croatian
    - Align using fastalign
  - `convert.py` script to make alignments in the form: source_word[tab]target_word
  - translate Slovenian parsed treebank using `translate_treebank.py`
  - train UDPipe model on the translated Croatian data
  - Results: UAS: 64.81%, LAS: 58.52%
- Using fasttext+FastAlign: 
  - 1 iteration, using fasttext word embeddings
  - Results: UAS: 66.82%, LAS: 60.19%
