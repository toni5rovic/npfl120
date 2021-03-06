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

It's important to consider the orthography of these languages. Upper-Sorbian, Czech and Polish use Latin script, while Ukrainian uses Cyrillic. 

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
|Czech|**99.55%**|**99.23%**|**99.39%**|**92.66%**|**93.26%**|**92.96%**
|Ukrainian|98.40%|96.43%|97.41%|61.34%|70.79%|65.72%
|Serbian|95.89%|90.92%|93.34%|82.82%|72.71%|77.74%
|English|99.28%|98.13%|98.70%|59.16%|76.73%|66.81%

The best scores for both sentence splitting and word tokenization are achieved when using Czech model trained on the Prague Dependency Treebank.

A couple of more languages with their respective similar languages that have a tokenizer model in UDPipe:

|Language|Tokenizer model|Words precision|Words Recall|Words F1|Sentences precision|Sentences recall|Sentences F1|
|---|---|---|---|---|---|---|---|
|Breton|French GSD|90.86%|93.43%|92.13%|94.60%|88.85%|91.64%
|Bhojpuri|Hindi|99.92%|99.96%|99.94%|86.87%|88.58%|87.72%
|Estonian|Finnish|99.28%|99.52%|99.40%|68.09%|73.96%|70.90%

# Task 2

**Training UDPipe tokenization model for Upper Sorbian**

The model is trained using the following command:

`udpipe --train --tagger=none --parser=none --tokenizer=epochs=10 upper_sorbian.udpipe < ~/tools/ud-treebanks-v2.5/UD_Upper_Sorbian-UFAL/hsb_ufal-ud-train.conllu`

After 10 epochs of training, training accuracy of 99.98% is reached. 

```console
Evaluation of the Upper Sorbian tokenization using trained tokenizer model...
Loading UDPipe model: done.
Number of SpaceAfter=No features in gold data: 2063
Tokenizer words - system: 10628, gold: 10736, precision: 99.07%, recall: 98.07%, f1: 98.57%
Tokenizer sentences - system: 702, gold: 623, precision: 65.53%, recall: 73.84%, f1: 69.43%
```

Comparing the previous results with our trained model using `task2.bash hsb_ufal-ud-test.conllu`:

|Tokenizer model|Words precision|Words Recall|Words F1|Sentences precision|Sentences recall|Sentences F1|
|---|---|---|---|---|---|---|
|Polish|99.26%|97.92%|98.59%|89.27%|92.13%|90.68%
|Czech|99.55%|99.23%|99.39%|92.66%|93.26%|92.96%
|Ukrainian|98.40%|96.43%|97.41%|61.34%|70.79%|65.72%
|Serbian|95.89%|90.92%|93.34%|82.82%|72.71%|77.74%
|English|99.28%|98.13%|98.70%|59.16%|76.73%|66.81%
|**Upper Sorbian**|**99.07%**|**98.07%**|**98.57%**|**65.53%**|**73.84%**|**69.43%**

The trained model performs better than Serbian and English model, but it is still worse than Czech and Polish. Important thing to note is that the training data has only 28 sentences and 460 tokens which is not enough to properly train the model. It is very easy to overfit on such a small data so in order to improve the model we definitely need more annotated data.

Now let's use our trained model on Czech and Polish data:

| UD Treebank | Word F1 using our model | Sentence F1 using our model | Word F1 using UDPipe model | Sentence F1 using UDPipe model |
|-------------|-------------------------|-----------------------------|----------------------------|:------------------------------:|
| Czech CAC   | 99.58%                  | 85.37%                      | **99.96%**                     |             **93.01%**             |
| Czech PDT   | 97.35%                  | 65.93%                      | **99.93%**                     |             **93.36%**             |
| Czech PUD   | 98.96%                  | 86.55%                      | **99.27%**                     |             **95.35%**             |
| Polish LFG  | 97.31%                  | 86.40%                      | **99.87%**                     |             **98.25%**             |
| Polish PDB  | 97.52%                  | 71.81%                      | **99.85%**                     |             **97.33%**             |
| Polish PUD  | 98.46%                  | 80.34%                      | **99.77%**                     |             **96.13%**             |

As expected, Polish and Czech own tokenizers work better.