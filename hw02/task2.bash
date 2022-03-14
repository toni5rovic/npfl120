test_file=$1

models_dir=~/tools/udpipe-ud-2.5-191206
ud_treebanks_dir=~/tools/ud-treebanks-v2.5
udpipe=~/tools/udpipe-1.2.0-bin/bin-linux64/udpipe
upper_sorbian_model=upper_sorbian.udpipe
polish_model=polish-pdb-ud-2.5-191206.udpipe
czech_model=czech-pdt-ud-2.5-191206.udpipe

echo "Evaluation of the Upper Sorbian tokenization using trained tokenizer model..."
$udpipe --accuracy --tokenize $upper_sorbian_model $ud_treebanks_dir/UD_Upper_Sorbian-UFAL/$test_file
echo ""

######################################################

echo "--------------------------------------------"
echo "Evaluation of the Czech CAC tokenization using trained Upper Sorbian tokenizer model..."
$udpipe --accuracy --tokenize $upper_sorbian_model $ud_treebanks_dir/UD_Czech-CAC/cs_cac-ud-test.conllu
echo ""

echo "Evaluation of the Czech CAC tokenization using Czech tokenizer model..."
$udpipe --accuracy --tokenize $models_dir/$czech_model $ud_treebanks_dir/UD_Czech-CAC/cs_cac-ud-test.conllu
echo ""

echo "--------------------------------------------"
echo "Evaluation of the Czech PDT tokenization using trained Upper Sorbian tokenizer model..."
$udpipe --accuracy --tokenize $upper_sorbian_model $ud_treebanks_dir/UD_Czech-PDT/cs_pdt-ud-test.conllu
echo ""

echo "Evaluation of the Czech PDT tokenization using Czech tokenizer model..."
$udpipe --accuracy --tokenize $models_dir/$czech_model $ud_treebanks_dir/UD_Czech-PDT/cs_pdt-ud-test.conllu
echo ""


echo "--------------------------------------------"
echo "Evaluation of the Czech PUD tokenization using trained Upper Sorbian tokenizer model..."
$udpipe --accuracy --tokenize $upper_sorbian_model $ud_treebanks_dir/UD_Czech-PUD/cs_pud-ud-test.conllu
echo ""

echo "Evaluation of the Czech PUD tokenization using Czech tokenizer model..."
$udpipe --accuracy --tokenize $models_dir/$czech_model $ud_treebanks_dir/UD_Czech-PUD/cs_pud-ud-test.conllu
echo ""

######################################################

echo "--------------------------------------------"
echo "Evaluation of the Polish LFG tokenization using trained Upper Sorbian tokenizer model..."
$udpipe --accuracy --tokenize $upper_sorbian_model $ud_treebanks_dir/UD_Polish-LFG/pl_lfg-ud-test.conllu
echo ""

echo "Evaluation of the Polish LFG tokenization using Polish tokenizer model..."
$udpipe --accuracy --tokenize $models_dir/$polish_model $ud_treebanks_dir/UD_Polish-LFG/pl_lfg-ud-test.conllu
echo ""

echo "--------------------------------------------"
echo "Evaluation of the Polish PDB tokenization using trained Upper Sorbian tokenizer model..."
$udpipe --accuracy --tokenize $upper_sorbian_model $ud_treebanks_dir/UD_Polish-PDB/pl_pdb-ud-test.conllu
echo ""

echo "Evaluation of the Polish PDB tokenization using Polish tokenizer model..."
$udpipe --accuracy --tokenize $models_dir/$polish_model $ud_treebanks_dir/UD_Polish-PDB/pl_pdb-ud-test.conllu
echo ""


echo "--------------------------------------------"
echo "Evaluation of the Polish PUD tokenization using trained Upper Sorbian tokenizer model..."
$udpipe --accuracy --tokenize $upper_sorbian_model $ud_treebanks_dir/UD_Polish-PUD/pl_pud-ud-test.conllu
echo ""

echo "Evaluation of the Polish PUD tokenization using Polish tokenizer model..."
$udpipe --accuracy --tokenize $models_dir/$polish_model $ud_treebanks_dir/UD_Polish-PUD/pl_pud-ud-test.conllu
echo ""
