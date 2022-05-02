#!/usr/bin/env python3
#coding: utf-8

import sys
from collections import defaultdict, Counter
from numpy import true_divide
from tqdm.auto import tqdm

# parameters
source_filename = "/home/toni/repos/npfl120/hw08-tree-translation/parallel/sl.s.conllu"
target_filename = "/home/toni/repos/npfl120/hw08-tree-translation/parallel/hr.s.conllu"
alignment_filename = "/home/toni/repos/npfl120/hw08-tree-translation/alignments/sl-hr.i"

# number of sentences -- in PUD it is always 1000
SENTENCES = 1000

# field indexes
ID = 0
FORM = 1
LEMMA = 2
UPOS = 3
XPOS = 4
FEATS = 5
HEAD = 6
DEPREL = 7

# returns dict[source_id] = [target_id_1, target_id_2, target_id_3...]
# and a reverse one as well
# TODO depending on what type of alignment you use, 
# you may not need to have a list of aligned tokens 
# -- maybe there is at most one, or even exactly one?
def read_alignment(fh):
    line = fh.readline()
    src2tgt = defaultdict(list)
    tgt2src = defaultdict(list)
    for st in line.split():
        (src, tgt) = st.split('-')
        src = int(src)
        tgt = int(tgt)
        src2tgt[src].append(tgt)
        tgt2src[tgt].append(src)
    return (src2tgt, tgt2src)

# returns a list of tokens, where each token is a list of fields;
# ID and HEAD are converted to integers and switched from 1-based to 0-based
# if delete_tree=True, then syntactic annotation (HEAD and DEPREL) is stripped
def read_sentence(fh, delete_tree=False):
    sentence = list()
    for line in fh:
        if line == '\n':
            # end of sentence
            break
        elif line.startswith('#'):
            # ignore comments
            continue
        else:
            fields = line.strip().split('\t')
            if fields[ID].isdigit():
                # make IDs 0-based to match alignment IDs
                fields[ID] = int(fields[ID])-1
                #fields[HEAD] = int(fields[HEAD])-1
                if delete_tree:
                    # reasonable defaults:
                    fields[HEAD] = -1       # head = root
                    fields[DEPREL] = 'dep'  # generic deprel
                sentence.append(fields)
            # else special token -- continue
    return sentence

# takes list of lists as input, ie as returned by read_sentence()
# switches ID and HEAD back to 1-based and converts them to strings
# joins fields by tabs and tokens by endlines and returns the CONLL string
def write_sentence(sentence):
    result = list()
    for fields in sentence:
        # switch back to 1-based IDs
        fields[ID] = str(fields[ID]+1)
        fields[HEAD] = str(fields[HEAD]+1)
        result.append('\t'.join(fields))
    result.append('')
    return '\n'.join(result)

with open(source_filename) as source, open(target_filename) as target, open(alignment_filename) as alignment:
    #for sentence_id in tqdm(range(SENTENCES)):
    for sentence_id in range(SENTENCES):
        (src2tgt, tgt2src) = read_alignment(alignment)
        source_sentence = read_sentence(source)
        target_sentence = read_sentence(target, delete_tree=True)
        
        # iterate over source tokens
        output = []
        for source_token in source_sentence:
            source_token_id = source_token[ID]
            
            target_form = None
            # for each target token aligned to source_token (if any)
            for target_token_id in src2tgt[source_token_id]:
                target_form = target_sentence[target_token_id][FORM]
                break
            
            if target_form == None:
                output.append(f"{source_token[FORM]}\t")
            else:
                output.append(f"{source_token[FORM]}\t{target_form}")

        print('\n'.join(output))
        print()
