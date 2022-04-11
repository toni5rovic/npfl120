udpipe=~/tools/udpipe-1.2.0-bin/bin-linux64/udpipe

echo "Obtaining cross-lingually tagged Kazakh training data"
$udpipe --tag models/kazakh_tagger.udpipe < data/kk_ktb-ud-train.conllu > data/kazakh_tagged_train.conllu
echo "Tagging training data done."

echo "###################################"
echo "Parsing Kazakh cross-lingually tagged data with trained Turkish model"
$udpipe --parse --accuracy "/home/toni/tools/udpipe-ud-2.5-191206/turkish-imst-ud-2.5-191206.udpipe" < "data/kazakh_tagged_train.conllu"
