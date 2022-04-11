udpipe=~/tools/udpipe-1.2.0-bin/bin-linux64/udpipe

echo "Parse cross-lingually tagged Kazakh data with trained Turkish model"
$udpipe --parse models/turkish_delex_parser.udpipe < data/kk.tagged.1649103740.conllu > data/kazakh_parsed.conllu
echo "Parsing Kazakh data done."

echo "###################################"
echo "Training Kazakh parser model with UDPipe"
$udpipe --train --tokenizer=none --tagger=none --parser='embedding_form=0;embedding_feats=0;iterations=10' "models/kazakh_delex_parser_10epochs.udpipe" < "data/kazakh_parsed.conllu"
echo "Training Kazakkh parser model done."

echo "###################################"
echo "Parsing Kazakh UD test data with trained Kazakh parser model"
$udpipe --parse --accuracy "models/kazakh_delex_parser_10epochs.udpipe" < "data/kk_ktb-ud-test.conllu"
