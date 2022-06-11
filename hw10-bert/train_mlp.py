#!/usr/bin/env python3

import sys

# Filename of model to save
filename = sys.argv[1] if len(sys.argv) == 2 else 'mlp.model'

# Training data
embeddings = list()
tags = list()
for line in sys.stdin:
    if line != '\n':
        fields = line.split()
        tags.append(fields[0])
        #print(fields[1:])
        embeddings.append([float(x) for x in fields[1:]])

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

# Split into train and test
embeddings_train, embeddings_test, tags_train, tags_test = train_test_split(embeddings, tags)

# Train a classifier
classifier = MLPClassifier(verbose=True)
classifier.fit(embeddings_train, tags_train)

# Evaluate the classifier
score_train = classifier.score(embeddings_train, tags_train)
score_test  = classifier.score(embeddings_test, tags_test)
print('Training score:', score_train)
print('Test score:', score_test)

# Save the model
import pickle
pickle.dump(classifier, open(filename, 'wb'))

