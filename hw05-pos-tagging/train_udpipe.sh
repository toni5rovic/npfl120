udpipe=~/tools/udpipe-1.2.0-bin/bin-linux64/udpipe
timestamp=$(date +%s)

echo "Part-of-Speech tags alignment..."
python ./pos_project.py $1 > output/kk.tagged.$timestamp.conllu
echo "Part-of-Speech tags alignment done."

echo "Training Kazakh PoS tagging model with UDPipe"
$udpipe --train --tokenizer=none --parser=none --tagger='use_xpostag=0;use_feats=0;iterations=5' "models/kazakh.$timestamp.udpipe" < output/kk.tagged.$timestamp.conllu
echo "Training done."


echo "Evaluating..."
$udpipe --tag --accuracy "models/kazakh.$timestamp.udpipe" < data/kk_ktb-ud-test.conllu

echo "----------------------"
echo "DONE"
echo $timestamp