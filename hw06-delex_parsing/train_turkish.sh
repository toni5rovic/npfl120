udpipe=~/tools/udpipe-1.2.0-bin/bin-linux64/udpipe

echo "Training Turkish parser model with UDPipe"
$udpipe --train --tokenizer=none --tagger=none --parser='embedding_form=0;embedding_feats=0;iterations=5' "models/turkish_delex_parser.udpipe" < "data/tr_kenet-ud-train.conllu"
