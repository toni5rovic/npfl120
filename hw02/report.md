# Homework assignment 2 - Tokenization

NPFL120 - Multilingual NLP

Antonije Petrović

# Task 1 

**Using existing tokenization models for the languages that don't have their own trained models in UDPipe.**

I am going to work with Upper Sorbian language (WALS code=sou; ISO code=hsb).

Firstly, I'll use the solution for the Assignment 1 to find the most similar languages to Upper Sorbian. My script returned the following 3 top most-similar languages:

| WALS code |	Name | Genus  | Family | Macroarea | Matching features | Similarity score |
|---|---|---|---|---|---|---|
|ukr|Ukrainian|Slavic|Indo-European|Eurasia|8|0.041026
|cze|Czech|Slavic|Indo-European|Eurasia|8|0.041026
|pol|Polish|Slavic|Indo-European|Eurasia|8|0.041026

The results are fairly expected - the top 3 most similar languages are Slavic languages, of which 2 are from the same group as Upper-Sorbian (Western-Slavic group). Their scores are the same since the number of features that are the equal is the same for all of these, it is 8.

It's important to consider the orthography of these languages. Upper-Sorbian,Czech and Polish use Latin script, while Ukrainian uses Cyrillic. 

Therefore, the experiments with using UDPipe models will be using the following languages:
- Polish
- Czech
- Ukrainian
- Serbian: an example of another Slavic language, but from another group - South-Slavic
- English: just to prove that it doesn't work as well

Running script `task1.bash hsb_ufal-ud-test.conllu` gives the following output:

```console
Evaluation of the Upper Sorbian tokenization using Polish tokenizer model...
Loading UDPipe model: done.
Number of SpaceAfter=No features in gold data: 2063
Tokenizer words - system: 10591, gold: 10736, precision: 99.26%, recall: 97.92%, f1: 98.59%
Tokenizer sentences - system: 643, gold: 623, precision: 89.27%, recall: 92.13%, f1: 90.68%

Evaluation of the Upper Sorbian tokenization using Czech PDT tokenizer model...
Loading UDPipe model: done.
Number of SpaceAfter=No features in gold data: 2063
Tokenizer words - system: 10701, gold: 10736, precision: 99.55%, recall: 99.23%, f1: 99.39%
Tokenizer sentences - system: 627, gold: 623, precision: 92.66%, recall: 93.26%, f1: 92.96%

Evaluation of the Upper Sorbian tokenization using Ukrainian tokenizer model...
Loading UDPipe model: done.
Number of SpaceAfter=No features in gold data: 2063
Tokenizer words - system: 10521, gold: 10736, precision: 98.40%, recall: 96.43%, f1: 97.41%
Tokenizer sentences - system: 719, gold: 623, precision: 61.34%, recall: 70.79%, f1: 65.72%

Evaluation of the Upper Sorbian tokenization using Serbian tokenizer model...
Loading UDPipe model: done.
Number of SpaceAfter=No features in gold data: 2063
Tokenizer words - system: 10179, gold: 10736, precision: 95.89%, recall: 90.92%, f1: 93.34%
Tokenizer sentences - system: 547, gold: 623, precision: 82.82%, recall: 72.71%, f1: 77.44%

Evaluation of the Upper Sorbian tokenization using English ParTUT tokenizer model...
Loading UDPipe model: done.
Number of SpaceAfter=No features in gold data: 2063
Tokenizer words - system: 10611, gold: 10736, precision: 99.28%, recall: 98.13%, f1: 98.70%
Tokenizer sentences - system: 808, gold: 623, precision: 59.16%, recall: 76.73%, f1: 66.81%
```

To see the values more clearly:

|Tokenizer model|Words precision|Words Recall|Words F1|Sentences precision|Sentences recall|Sentences F1|
|---|---|---|---|---|---|---|
|Polish|99.26%|97.92%|98.59%|89.27%|92.13%|90.68%
|Czech|99.55%|99.23%|99.39%|92.66%|93.26%|92.96%
|Ukrainian|98.40%|96.43%|97.41%|61.34%|70.79%|65.72%
|Serbian|95.89%|90.92%|93.34%|82.82%|72.71%|77.74%
|English|99.28%|98.13%|98.70%|59.16%|76.73%|66.81%

The best scores for both sentence splitting and word tokenization are achieved when using Czech model trained on the Prague Dependency Treebank.


