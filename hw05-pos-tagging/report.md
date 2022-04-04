# Homework assignment 5 - Part of Speech Tagging

NPFL120 - Multilingual NLP

Antonije Petrović

# Assignment description

1. Take parallel data
   - I used Watchtower parallel data for English (en.s) and Kazakh (kk.s)

2. Using script [main.sh](./main.sh):
   - English data is tokenized and tagged using UDPipe trained model for English 
   - Kazakh data is tokenized using Turkish UDPipe model
   - The choice of tokenization model is imporant and may influence the alignments, and therefore the training of the tagger
   - Sentence segmentation is preserved by using option `--tokenizer=presegmented`

3. Alignment of the parallel corpus is done by using FastAlign (script [align.sh](./align.sh))

4. Project POS tags through the alignment from the tagged source to the non-tagged target
  - Using the template: [pos_project.py](./pos_project.py) and iteratively adding more mappings
  - After changing [pos_project.py](./pos_project.py), script [train_udpipe.sh](./train_udpipe.sh) is being run in order to train UDPipe tagging model and then evaluate it on [Universal Dependencies Kazakh test data](https://github.com/UniversalDependencies/UD_Kazakh-KTB/blob/master/kk_ktb-ud-test.conllu)

# Iterations

Number of sentences: 10k

Training iterations: 5

## Base solution

Using English as a source language. Using alignments from FastAlign, we just copy the PoS tags from the source tokens to the target tokens. In case no alignment exists for a given target token, nothing is done and value "_" stays.

- Accuracy: 9.86%
- Timestamp: 1649079157
- Output file: [output/kk.tagged.1649079157.conllu](./output/kk.tagged.1649079157.conllu)

## Default `NOUN` tag

Here we assign "NOUN" PoS tag to all target tokens that are not aligned (and therefore source PoS tags are not copied for them).

- Accuracy: 22.60%
- Timestamp: 1649099142
- Output file: [output/kk.tagged.1649099142.conllu](./output/kk.tagged.1649099142.conllu)

## Voting: Turkish, Russian, English

- A few notes:
  - He we can work only with sentences that exist in all four corpora (Kazakh, Turkish, Russian, English)
  - Because of this, a script [remove_empty_lines.py](./remove_empty_lines.py) creates separate modified files for each of the 4 original corpus files, where the sentences will be only the ones that exist in all four languages
  - Again, we tokenize and tag all of the training data (Turkish, Russian, English) and with Kazak, we only tokenize it using Turkish UDPipe model. This is done by using script [main.mod.sh](./main.mod.sh)
  - Alignments are created again (using script [align.mod.sh](./align.mod.sh) ) and then we can train UDPipe model for Kazakh

- Accuracy: 49.15%
- Timestamp: 1649104793
- Output file: [output/kk.tagged.1649104793.conllu](./output/kk.tagged.1649104793.conllu)

## Voting + default NOUN

- Accuracy: 49.97%
- Timestamp: 1649103740
- Output file: [output/kk.tagged.1649103740.conllu](./output/kk.tagged.1649103740.conllu)

Note: It seems that not much accuracy is gained after setting default NOUN tag. This might be because voting system already assigns tags so backoff to default tag is done in a low number of cases 


# Conclusion

Voting system improves the accuracy by a large margin (from 9.86% to 49.15%, and 49.97% when using default `NOUN` tag). It is possible to assume that using more closely related languages might help even more. Here, Turkish has been chosen as an example of a language from the same language family as Kazakh - Turkic language family. Russian is chosen as a geographically close language, and English as the highest resourced language.