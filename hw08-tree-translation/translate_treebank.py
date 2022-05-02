#!/usr/bin/env python3
#coding: utf-8

import sys
from collections import defaultdict, Counter

conllu, para = sys.argv[1:]

lexicon = defaultdict(Counter)
with open(para) as translations:
    for line in translations:
        linesplit = line.split()
        if len(linesplit) == 2:
            lexicon[linesplit[0]][linesplit[1]] += 1

with open(conllu) as treebank:
    for line in treebank:
        line = line.strip()
        fields = line.split('\t')
        if fields[0].isdigit():
            word = fields[1]
            translation = word
            if word in lexicon:
                translation = lexicon[word].most_common(1)[0][0]
            fields[1] = translation
            print(*fields, sep='\t')
        else:
            print(line)

