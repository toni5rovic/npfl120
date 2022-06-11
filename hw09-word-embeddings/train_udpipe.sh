udpipe=~/tools/udpipe-1.2.0-bin/bin-linux64/udpipe
$udpipe --train es_baseline.udpipe --tokenizer=none --tagger=none --parser='iterations=3' treebanks/es_ancora-ud-train.conllu
$udpipe --train es_with_embs.udpipe --tokenizer=none --tagger=none --parser='iterations=3;embedding_form_file=mapped_embs.emb' treebanks/es_ancora-ud-train.conllu
