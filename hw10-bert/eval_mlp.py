#!/usr/bin/env python3

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

import sys

# Filename of model to load
filename = sys.argv[1] if len(sys.argv) == 2 else 'mlp.model'

# Evaluation data
embeddings = list()
tags = list()
for line in sys.stdin:
    if line != '\n':
        fields = line.split()
        tags.append(fields[0])
        embeddings.append([float(x) for x in fields[1:]])

from sklearn.neural_network import MLPClassifier

# Load the model
import pickle
classifier = pickle.load(open(filename, 'rb'))

# Evaluate the classifier
score = classifier.score(embeddings, tags)
print(score)

