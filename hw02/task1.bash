test_file=$1

models_dir=~/tools/udpipe-ud-2.5-191206
ud_treebanks_dir=~/tools/ud-treebanks-v2.5
udpipe=~/tools/udpipe-1.2.0-bin/bin-linux64/udpipe

polish_model=polish-pdb-ud-2.5-191206.udpipe
czech_model=czech-pdt-ud-2.5-191206.udpipe
ukrainian_model=ukrainian-iu-ud-2.5-191206.udpipe
serbian_model=serbian-set-ud-2.5-191206.udpipe
english_model=english-partut-ud-2.5-191206.udpipe

echo "Evaluation of the Upper Sorbian tokenization using Polish tokenizer model..."
$udpipe --accuracy --tokenize $models_dir/$polish_model $ud_treebanks_dir/UD_Upper_Sorbian-UFAL/$test_file
echo ""

echo "Evaluation of the Upper Sorbian tokenization using Czech PDT tokenizer model..."
$udpipe --accuracy --tokenize $models_dir/$czech_model $ud_treebanks_dir/UD_Upper_Sorbian-UFAL/$test_file
echo ""

echo "Evaluation of the Upper Sorbian tokenization using Ukrainian tokenizer model..."
$udpipe --accuracy --tokenize $models_dir/$ukrainian_model $ud_treebanks_dir/UD_Upper_Sorbian-UFAL/$test_file
echo ""

echo "Evaluation of the Upper Sorbian tokenization using Serbian tokenizer model..."
$udpipe --accuracy --tokenize $models_dir/$serbian_model $ud_treebanks_dir/UD_Upper_Sorbian-UFAL/$test_file 
echo ""

echo "Evaluation of the Upper Sorbian tokenization using English ParTUT tokenizer model..."
$udpipe --accuracy --tokenize $models_dir/$english_model $ud_treebanks_dir/UD_Upper_Sorbian-UFAL/$test_file
echo ""
