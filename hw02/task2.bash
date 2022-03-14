test_file=$1

models_dir=~/tools/udpipe-ud-2.5-191206
ud_treebanks_dir=~/tools/ud-treebanks-v2.5
udpipe=~/tools/udpipe-1.2.0-bin/bin-linux64/udpipe
upper_sorbian_model=upper_sorbian.udpipe

echo "Evaluation of the Upper Sorbian tokenization using trained tokenizer model..."
$udpipe --accuracy --tokenize $upper_sorbian_model $ud_treebanks_dir/UD_Upper_Sorbian-UFAL/$test_file
echo ""
