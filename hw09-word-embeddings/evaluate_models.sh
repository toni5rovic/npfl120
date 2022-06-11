udpipe=~/tools/udpipe-1.2.0-bin/bin-linux64/udpipe
model=./models/es_sr_with_embs.udpipe

echo "Spanish"
$udpipe --accuracy $model --parse treebanks/es_ancora-ud-test.conllu

echo "Portugese"
$udpipe --accuracy $model --parse treebanks/pt_gsd-ud-test.conllu

echo "Italian"
$udpipe --accuracy $model --parse treebanks/it_pud-ud-test.conllu

echo "Serbian"
$udpipe --accuracy $model --parse treebanks/sr_set-ud-test.conllu

echo "Croatian"
$udpipe --accuracy $model --parse treebanks/hr_set-ud-test.conllu

echo "Bulgarian"
$udpipe --accuracy $model --parse treebanks/bg_btb-ud-test.conllu
