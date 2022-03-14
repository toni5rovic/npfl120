models_dir=~/tools/udpipe-ud-2.5-191206
ud_treebanks_dir=~/tools/ud-treebanks-v2.5
udpipe=~/tools/udpipe-1.2.0-bin/bin-linux64/udpipe

polish_model=polish-pdb-ud-2.5-191206.udpipe
czech_model=czech-pdt-ud-2.5-191206.udpipe
ukrainian_model=ukrainian-iu-ud-2.5-191206.udpipe
serbian_model=serbian-set-ud-2.5-191206.udpipe
english_model=english-partut-ud-2.5-191206.udpipe

echo "Evaluation of the Upper Sorbian tokenization using Polish tokenizer model..."
$udpipe --accuracy --tokenize $models_dir/$polish_model $ud_treebanks_dir/UD_Upper_Sorbian-UFAL/$1
echo ""

echo "Evaluation of the Upper Sorbian tokenization using Czech PDT tokenizer model..."
$udpipe --accuracy --tokenize $models_dir/$czech_model $ud_treebanks_dir/UD_Upper_Sorbian-UFAL/$1
echo ""

echo "Evaluation of the Upper Sorbian tokenization using Ukrainian tokenizer model..."
$udpipe --accuracy --tokenize $models_dir/$ukrainian_model $ud_treebanks_dir/UD_Upper_Sorbian-UFAL/$1
echo ""

echo "Evaluation of the Upper Sorbian tokenization using Serbian tokenizer model..."
$udpipe --accuracy --tokenize $models_dir/$serbian_model $ud_treebanks_dir/UD_Upper_Sorbian-UFAL/$1 
echo ""

echo "Evaluation of the Upper Sorbian tokenization using English ParTUT tokenizer model..."
$udpipe --accuracy --tokenize $models_dir/$english_model $ud_treebanks_dir/UD_Upper_Sorbian-UFAL/$1
echo ""

echo "-----------------------------------------------------------------------------------"


french_gsd_model=french-gsd-ud-2.5-191206.udpipe
hindi_model=hindi-hdtb-ud-2.5-191206.udpipe
finnish_model=finnish-ftb-ud-2.5-191206.udpipe

echo "Evaluation of the Breton tokenization using French GSD tokenizer model..."
$udpipe --accuracy --tokenize $models_dir/$french_gsd_model $ud_treebanks_dir/UD_Breton-KEB/$2
echo ""

echo "Evaluation of the Bhojpuri tokenization using Hindi tokenizer model..."
$udpipe --accuracy --tokenize $models_dir/$hindi_model $ud_treebanks_dir/UD_Bhojpuri-BHTB/$3
echo ""

echo "Evaluation of the Estonian tokenization using Finnish FTB tokenizer model..."
$udpipe --accuracy --tokenize $models_dir/$finnish_model $ud_treebanks_dir/UD_Estonian-EDT/$4
echo ""
