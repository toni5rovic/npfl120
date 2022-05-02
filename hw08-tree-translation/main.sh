udpipe=~/tools/udpipe-1.2.0-bin/bin-linux64/udpipe

$udpipe --parse --accuracy hr-translex.norm.udpipe < data/hr_set-ud-test.conllu

echo "Translating the treebank..."
# Translating each word in the source treebank to the target treebank
#python translate_treebank.py data/sl-ud-train.conllu data/monogr_sl-hr.aligned > output/fake-hr.conllu
python translate_treebank.py parallel/sl.s.conllu data/WT_sl-hr.aligned > output/fake-hr-WT.conllu
echo "Translation done."

echo "Training UDPipe..."
$udpipe --train --parser="iterations=1" --tokenizer=none --tagger=none models/fake-hr-WT.model < output/fake-hr-WT.conllu
echo "Training done."

$udpipe --parse --accuracy models/fake-hr-WT.model < data/hr_set-ud-test.conllu
