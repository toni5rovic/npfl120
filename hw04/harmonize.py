#!/usr/bin/env python3
#coding: utf-8

import sys

# field indexes
ID = 0
FORM = 1
LEMMA = 2
UPOS = 3
XPOS = 4
FEATS = 5
HEAD = 6
DEPREL = 7

for line in sys.stdin:
    fields = line.strip().split('\t')
    if len(fields) >= 1 and fields[ID].isdigit():
        # TODO harmonize the tag, store the harmonized tag into UPOS
        fields[UPOS] = fields[XPOS]
        
        if fields[XPOS][0] == "V":
            fields[UPOS] = "VERB"

        if fields[XPOS] in ["NN", "NNS"]:
            fields[UPOS] = "NOUN"
        
        if fields[XPOS] in ["NNP", "NNPS"]:
           fields[UPOS] = "PROPN"

        if fields[XPOS][0] == "J":
           fields[UPOS] = "ADJ"

        if fields[XPOS] in ["RB", "RBR", "RBS"]:
            fields[UPOS] = "ADV"

        if fields[XPOS] == "DT":
            fields[UPOS] = "DET"

        if fields[XPOS] == "RP":
            fields[UPOS] = "PART"

        if fields[XPOS] == "CD":
            fields[UPOS] = "NUM"

        if fields[XPOS] in ['.', ',', '(', ')', '!', '?', ';', ':', '\'', '\'\'', '``', '"', '`', '‘', '’']:
            fields[UPOS] = "PUNCT"

        if fields[XPOS] == "UH":
            fields[UPOS] = "INTJ"

        if fields[XPOS] in ["PRP", "PRP$", "WDT", "WP", "WP$"]:
            fields[UPOS] = "PRON"

        if fields[XPOS] == "CC":
            fields[UPOS] = "CCONJ"

        if fields[XPOS] == "FW":
            fields[UPOS] = "X"

        if fields[XPOS] == "EX":
            fields[UPOS] = "PRON"

        if fields[XPOS] == "LS":
            fields[UPOS] = "NUM"

        if fields[XPOS] == "MD":
            fields[UPOS] = "AUX"

        if fields[XPOS] == "PDT":
            fields[UPOS] = "DET"

        if fields[XPOS] == "POS":
            fields[UPOS] = "PART"

        if fields[XPOS] == "TO":
            fields[UPOS] = "PART"

        if fields[XPOS] in ["$", "#"]:
            fields[UPOS] = "SYM"

        # if fields[XPOS] == "WRB":
        #     fields[UPOS] = "ADV"

        if fields[XPOS] == "WRB":
            fields[UPOS] = "SCONJ"

        # if fields[XPOS] == "IN":
        #     fields[UPOS] = "ADP"

        if fields[XPOS] == "IN":
            fields[UPOS] = "SCONJ"


        # output
        print('\t'.join(fields))
    else:
        # pass thru
        print(line.strip())
