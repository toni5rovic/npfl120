# Homework assignment 6 - Delexicalized Parsing

NPFL120 - Multilingual NLP

Antonije Petrović

# Assignment description

- use new treebanks
- use new UDPipe models
- train a delexicalized parser on a source language treebank
- apply it to cross-lingually-POS-tagged target-language data
- report parsing accuracies (LAS, UAS)

# Report 

First, Turkish delexicalized parser model is trained on the UD training data for Turkish language.
- Script: [train_turkish.sh](./train_turkish.sh)
- Parameters: `embedding_form=0;embedding_feats=0;iterations=5`


Then, 3 different approaches are taken and their results are compared.

## Approach 1

- Script: [approach1.sh](./approach1.sh) 
- Use trained Turkish delexicalized model
- Using Kazakh model from the previous homework ([kazakh_tagger.udpipe](./models/kazakh_tagger.udpipe)), tag the Kazakh UD training data
- Parse Kazakh cross-lingually tagged data with Turkish parser model and get the accuracy
- UAS: 31.57%, LAS: 12.67%

## Approach 2

- Script: [approach2.sh](./approach2.sh)
- Use available Turkish UDPipe model
- Using Kazakh model from the previous homework ([kazakh_tagger.udpipe](./models/kazakh_tagger.udpipe)), tag the Kazakh UD training data
- Parse Kazakh cross-lingually tagged data with UDPipe's Turkish model and get the accuracy
- UAS: 26.09%, LAS: 10.78%

## Approach 3

- Script: [approach3.sh](./approach3.sh)
- Use trained Turkish delexicalized parser model to parse cross-lingually tagged Kazakh data from the previous homework [kk.tagged.1649103740.conllu](./data/kk.tagged.1649103740.conllu)
- Then, use this parsed data to train Kazakh delexicalized parser model
- In the end, evaluate the Kazakh delexicalized model on UD test data
- After 5 epochs: UAS: 70.09%, LAS: 52.71%
- After 10 epochs: UAS: 71.06%, LAS: 53.33%


# Conclusion

Using UDPipe Turkish model instead of training our own doesn't help. This is expected since the UDPipe model probably uses lexical data along with other features. While in our case, we create the delexicalized model which is trained without looking at the word forms. In some other language pair, we could expect usual model to be better, but in the case of Turkish-Kazakh pair it is impossible to have the same word forms or even morphemes because the scripts used in these two languages are different (cyrillic vs. latin).

The 3rd approach is the best. Using Turkish trained parser to parse Kazakh data first and then use it for training Kazakh's own model helps a lot. The accuracy that we get in this case is much higher than in the previous two approaches.