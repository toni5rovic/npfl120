#!/usr/bin/env python3
import argparse
from tqdm.auto import tqdm

# align_type=$1
# src=$2
# dst=$3
# paste $src-$dst/SETIMES.$src-$dst.$src \
#       $src-$dst/SETIMES.$src-$dst.$dst \
#       <(zcat $src-$dst.ali.gz ) \
#       | cut -f 1,2,$align_type | less

parser = argparse.ArgumentParser()
parser.add_argument("--src", default=None, type=str, help="Src language")
parser.add_argument("--dst", default=None, type=str, help="Dst language")
parser.add_argument("--align_type", default=5, type=int, help="Align type")
parser.add_argument("--improved", default=False, type=bool, help="Use improved alignments")

def main(args):
    improved = ".lcstem4" if args.improved else ""
    src_file = f"{args.src}-{args.dst}/SETIMES.{args.src}-{args.dst}{improved}.{args.src}"
    dst_file = f"{args.src}-{args.dst}/SETIMES.{args.src}-{args.dst}{improved}.{args.dst}"
    alignments_file = f"{args.src}-{args.dst}-alignments/data"
    with open(src_file, "r", encoding="utf-8") as f:
        src_lines = [l.strip() for l in f.readlines()]
    
    with open(dst_file, "r", encoding="utf-8") as f:
        dst_lines = [l.strip() for l in f.readlines()]

    with open(alignments_file, "r") as f:
        align_file_lines = [l.strip()  for l in f.readlines()]

    alignment_lines = []
    for i in range(len(align_file_lines)):
        if align_file_lines[i] == None or len(align_file_lines[i]) == 0:
            alignment_lines.append(None)
            continue
        alignment_lines.append(align_file_lines[i].split('\t')[args.align_type - 3])

    word_pairs = []
    for i in range(len(src_lines)):
        alignments_entry = alignment_lines[i]
        if alignments_entry == None:
            continue

        src_sent = src_lines[i]
        dst_sent = dst_lines[i]

        src_tokens = src_sent.split()
        dst_tokens = dst_sent.split()

        alignments = alignments_entry.split()
        for alignment in alignments:
            src_idx = int(alignment.split('-')[0])
            dst_idx = int(alignment.split('-')[1])
            word_pair = (src_tokens[src_idx], dst_tokens[dst_idx])
            word_pairs.append(word_pair)
            #if word_pair not in word_pairs:
            #    word_pairs[word_pair] = 1
            #else:
            #    word_pairs[word_pair] += 1

    for word_pair in word_pairs:
        print(word_pair[0], word_pair[1])

if __name__ == "__main__":
    args = parser.parse_args([] if "__file__" not in globals() else None)
    main(args)
