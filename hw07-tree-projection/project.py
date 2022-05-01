#!/usr/bin/env python3
#coding: utf-8

import sys
from collections import defaultdict, Counter
from numpy import true_divide
from tqdm.auto import tqdm

# parameters
source_filename, target_filename, alignment_filename = sys.argv[1:4]
# source_filename = "/home/toni/repos/npfl120/hw07-tree-projection/data/en_pud-ud-test.conllu"
# target_filename = "/home/toni/repos/npfl120/hw07-tree-projection/data/es_pud-ud-test.conllu"
# alignment_filename = "/home/toni/repos/npfl120/hw07-tree-projection/alignments/en-es.intersect"

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
                fields[HEAD] = int(fields[HEAD])-1
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


def get_deprel_stats(filename):
    pos_pair_stats = {}
    pos_stats = {}
    with open(filename) as treebank_file:
        for sentence_id in range(SENTENCES):
            sentence = read_sentence(treebank_file)
            
            for token in sentence:
                deprel = token[DEPREL]
                child_pos = token[UPOS]
                head_id = token[HEAD]

                head_pos = "ROOT"
                if head_id > 0:
                   head_pos = sentence[head_id][UPOS]
                
                # updating DepRel-PoS,PoS dict
                pos_pair = (child_pos, head_pos)
                if deprel not in pos_pair_stats:
                    pos_pair_stats[deprel] = []

                pos_pair_stats[deprel].append(pos_pair)

                # updating DepRel-PoS dict
                if deprel not in pos_stats:
                    pos_stats[deprel] = []

                pos_stats[deprel].append(head_pos)

    for deprel, pos_pairs_list in pos_pair_stats.items():
        counter = Counter(pos_pairs_list)
        pos_pair_stats[deprel] = counter
    
    for deprel, pos_list in pos_stats.items():
        counter = Counter(pos_list)
        pos_stats[deprel] = counter

    return pos_pair_stats, pos_stats

def find_root(sentence):
    for token in sentence:
        tokens_deprel = token[DEPREL]
        if tokens_deprel == "root":
            return token[ID]
    
    return None

def is_cyclical(sentence, child_token, parent_token):
    parent = sentence[parent_token]
    while parent[HEAD] != -1 and parent[HEAD] != child_token:
        parent = sentence[parent[HEAD]]

    if parent[HEAD] == child_token:
        return True
    
    return False

def find_head_for_deprel(deprel, sentence, skip_token_id):
    for token in sentence:
        if token[HEAD] == skip_token_id:
            continue

        if is_cyclical(sentence, skip_token_id, token[ID]):
            continue

        tokens_deprel = token[DEPREL]
        if tokens_deprel == deprel:
            assert token[HEAD] != skip_token_id
            return token[HEAD]
        
    return None

def choose_deprel(pos_pair_stats, pos_stats, potential_heads, target_sentence, target_token_id):
    if potential_heads != None and len(potential_heads) > 0:
        potential_head_id = potential_heads[0]
        

    target_pos = target_sentence[target_token_id][UPOS]

    best_head = None
    best_deprel = None
    best_deprel_count = 0

    # 1. Ako (target_token_id, potential_head_id) postoji u source_sentence, onda kopiramo deprel otuda
    #    i target_token-u setujemo HEAD na potential_head_id
    # 2. Ako nema, onda pogledamo POS tagove target_tokena i potential_head-a

    for potential_head_id in potential_heads:
        head_pos = target_sentence[potential_head_id][UPOS]

        pos_pair = (target_pos, head_pos)
        if pos_pair in pos_pair_stats:
            if pos_pair_stats[pos_pair][1] > best_deprel_count:
                best_head = potential_head_id
                best_deprel = pos_pair_stats[pos_pair][0]
                best_deprel_count = pos_pair_stats[pos_pair][1]

    # if best_deprel is None:
    #     for potential_head_id in potential_heads:
    #         head_pos = target_sentence[potential_head_id][UPOS]

    #         if head_pos in pos_stats:
    #             if pos_stats[head_pos][1] > best_deprel_count:
    #                 best_head = potential_head_id
    #                 best_deprel = pos_stats[head_pos][0]
    #                 best_deprel_count = pos_stats[head_pos][1]

    # if no best head is chosen, choose the head by finding 
    # the same deprel in the sentence and using the same head
    if best_head == None:
        target_pos = target_sentence[target_token_id][UPOS]
        best_deprel = pos_stats[target_pos][0]
        best_head = find_head_for_deprel(best_deprel, target_sentence, target_token_id)

    # if no best head is chosen, choose root
    #if best_head == None:
    #    best_head = find_root(target_sentence)

    if best_head == None:
        best_head = -1
        best_deprel = "dep"

    return best_head, best_deprel

def is_cycle(token_id, head_id, sentence):
    if token_id == head_id:
        return True

    curr_node = sentence[head_id]
    while curr_node[HEAD] != -1 and curr_node[HEAD] != token_id:
        curr_node = sentence[curr_node[HEAD]]
    
    return curr_node[HEAD] == token_id

def remove_cyclical(potential_heads, sentence, token_id):
    good_potential_heads = []
    for potential_head in potential_heads:
        curr_node = sentence[potential_head]
        while curr_node[HEAD] != -1 and curr_node[HEAD] != token_id:
            curr_node = sentence[curr_node[HEAD]]
        
        if curr_node[HEAD] != token_id:
            good_potential_heads.append(potential_head)

    assert token_id not in good_potential_heads
    return good_potential_heads

def find_tokens(sentence, pos_tag):
    tokens_list = []
    for token in sentence:
        if token[UPOS] == pos_tag:
            tokens_list.append(token)

    return tokens_list

def get_head(potential_heads, deprel, target_sentence, target_token_id):
    # if we have some potential heads that do not form a cycle,
    # we can take the first one and assign it as a head for 
    # the current target token
    if potential_heads != None and len(potential_heads) > 0:
        return potential_heads[0]
    
    # if we don't have potential heads by using alignments directly,
    # we can find the head by considering the PoS pair in the source sentence
    # and we can try to find the same PoS pair in the target sentence.
    src_head_pos = source_sentence[source_head_id][UPOS]

    tgt_tokens_with_head_pos = find_tokens(target_sentence, src_head_pos)
    if len(tgt_tokens_with_head_pos) > 0:
        # for example take first
        # TODO make sure no cycle is formed
        for possible_head in tgt_tokens_with_head_pos:
            head_id = possible_head[ID]
            if is_cycle(target_token_id, head_id, target_sentence):
                continue
        
            return head_id
    
    # now we can try to consider PoS statistics for a given deprel
    # by trying to find the same PoS pair in the target sentence.
    pos_pairs_counter = pos_pair_stats[deprel]
    
    for pos_pair in pos_pairs_counter:
        # ignore PoS pairs where the child token's PoS is not 
        # the same as our target token's PoS
        child_pos, head_pos = pos_pair
        if child_pos != target_sentence[target_token_id][UPOS]:
            continue

        found_tgt_tokens = find_tokens(target_sentence, head_pos)
        if len(found_tgt_tokens) > 0:
            # for example take first
            # TODO make sure no cycle is formed
            for possible_head in found_tgt_tokens:
                head_id = possible_head[ID]
                if is_cycle(target_token_id, head_id, target_sentence):
                    continue
                
                return head_id

    # if we still haven't found the head for the target token
    # try to use DepRel-PoS statistics
    pos_counter = pos_stats[source_token[DEPREL]]
    for pos in pos_counter:
        found_tgt_tokens = find_tokens(target_sentence, pos)
        if len(found_tgt_tokens) > 0:
            # TODO make sure no cycle is formed
            for possible_head in found_tgt_tokens:
                head_id = possible_head[ID]
                if is_cycle(target_token_id, head_id, target_sentence):
                    continue
                return head_id

    return -1

pos_pair_stats, pos_stats = get_deprel_stats(source_filename)

with open(source_filename) as source, open(target_filename) as target, open(alignment_filename) as alignment:
    #for sentence_id in tqdm(range(SENTENCES)):
    for sentence_id in range(SENTENCES):

        (src2tgt, tgt2src) = read_alignment(alignment)
        source_sentence = read_sentence(source)
        target_sentence = read_sentence(target, delete_tree=True)
        
        # iterate over source tokens
        processed_target_tokens = []
        for source_token in source_sentence:
            source_token_id = source_token[ID]
            source_head_id = source_token[HEAD]

            
            # for each target token aligned to source_token (if any)
            for target_token_id in src2tgt[source_token_id]:
                # copy source deprel to target deprel
                target_sentence[target_token_id][DEPREL] = source_token[DEPREL]
                
                # considering only heads that do not form a cycle for a given target_token_id
                potential_heads = src2tgt[source_head_id]
                noncyclical_heads = remove_cyclical(potential_heads, target_sentence, target_token_id)

                head_id = get_head(noncyclical_heads, source_token[DEPREL], target_sentence, target_token_id)
                assert head_id != target_token_id
                target_sentence[target_token_id][HEAD] = head_id
                
                #processed_target_tokens.append(target_token_id)

        print(write_sentence(target_sentence))

