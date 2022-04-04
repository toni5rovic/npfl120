#!/usr/bin/env python3
#coding: utf-8

from multiprocessing.sharedctypes import Value
import sys
from collections import defaultdict

# parameters
src_en_filename = "/home/toni/repos/npfl120/hw05-pos-tagging/output/en.s.mod.conllu"
src_ru_filename = "/home/toni/repos/npfl120/hw05-pos-tagging/output/ru.s.mod.conllu"
src_tr_filename = "/home/toni/repos/npfl120/hw05-pos-tagging/output/tr.s.mod.conllu"

target_filename = "/home/toni/repos/npfl120/hw05-pos-tagging/output/kk.s.mod.conllu"

en_alignment_filename = "/home/toni/repos/npfl120/hw05-pos-tagging/alignments/en-kk.f"
ru_alignment_filename = "/home/toni/repos/npfl120/hw05-pos-tagging/alignments/ru-kk.f"
tr_alignment_filename = "/home/toni/repos/npfl120/hw05-pos-tagging/alignments/tr-kk.f"

default_NOUN = len(sys.argv) > 1 and sys.argv[1] == "--default_noun"

# number of sentences -- in PUD it is always 1000
SENTENCES = 10000

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
# TODO depending on what type of alignment you use, you may not need to have 
# a list of aligned tokens -- maybe there is at most one, or even exactly one?
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
# if delete_pos=True, then morphological anotation (UPOS, XPOS, FEATS) is stripped
def read_sentence(fh, delete_pos=False):
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
                # fields[HEAD] = int(fields[HEAD])-1
                if delete_pos:
                    fields[UPOS] = '_'
                    fields[XPOS] = '_'
                    fields[FEATS] = '_'
                sentence.append(fields)
            # else special token -- continue
    return sentence

# takes list of lists as input, ie as returned by read_sentence()
# switches ID and HEAD back to 1-based and converts them to strings
# joins fields by tabs and tokens by endlines and returns the CONLL string
def write_sentence(sentence, sent_id):
    result = list()
    result.append(f"# sent_id = {sent_id}")
    result.append(f"# text = {' '.join([s[FORM] for s in sentence])}")
    for fields in sentence:
        # switch back to 1-based IDs
        fields[ID] = str(fields[ID]+1)
        # fields[HEAD] = str(fields[HEAD]+1)
        result.append('\t'.join(fields))
    result.append('')
    return '\n'.join(result)

def vote(alignments, source_sentences, target_token_id):
    
    voting_scores = {}
    
    for i in range(len(alignments)):
        alignment = alignments[i]
        source_sentence = source_sentences[i]
        
        for source_token_id in alignment[target_token_id]:
            pos_tag = source_sentence[source_token_id][UPOS]

            if pos_tag in voting_scores:
                voting_scores[pos_tag] += 1
            else:
                voting_scores[pos_tag] = 1
    
    winner_pos_tag = None
    winner_pos_count = 0
    for pos_tag, pos_tag_vote_count in voting_scores.items():
        if pos_tag_vote_count > winner_pos_count:
            winner_pos_count = pos_tag_vote_count
            winner_pos_tag = pos_tag
    
    if winner_pos_tag != None:
        return winner_pos_tag

    return None

def pos_projection(source_sentences, target_sentence, alignments):
    tgt2src_alignments = (alignments[0][1], alignments[1][1], alignments[2][1])
    source_sentences = (source_sentence_en, source_sentence_ru, source_sentence_tr)

    for target_token in target_sentence:
        target_token_id = target_token[ID]

        target_token_pos = vote(tgt2src_alignments, source_sentences, target_token_id)
        if target_token_pos == None:
            if default_NOUN:
                target_token_pos = "NOUN"
            else:
                target_token_pos = "_"
        
        target_sentence[target_token_id][UPOS] = target_token_pos

    print(write_sentence(target_sentence, sentence_id))

with open(src_en_filename) as source_en, open(src_ru_filename) as source_ru, open(src_tr_filename) as source_tr, open(target_filename) as target, open(en_alignment_filename) as alignment_en, open(ru_alignment_filename) as alignment_ru, open(tr_alignment_filename) as alignment_tr:
    for sentence_id in range(SENTENCES):
        (en_src2tgt, en_tgt2src) = read_alignment(alignment_en)
        (ru_src2tgt, ru_tgt2src) = read_alignment(alignment_ru)
        (tr_src2tgt, tr_tgt2src) = read_alignment(alignment_tr)
        alignments = [(en_src2tgt, en_tgt2src), (ru_src2tgt, ru_tgt2src), (tr_src2tgt, tr_tgt2src)]
        
        source_sentence_en = read_sentence(source_en)
        source_sentence_ru = read_sentence(source_ru)
        source_sentence_tr = read_sentence(source_tr)
        source_sentences = (source_sentence_en, source_sentence_ru, source_sentence_tr)

        target_sentence = read_sentence(target, delete_pos=True)
        
        pos_projection(source_sentences, target_sentence, alignments)