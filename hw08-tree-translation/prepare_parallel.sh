
sl_udpipe_model=~/tools/udpipe-ud-2.5-191206/slovenian-ssj-ud-2.5-191206.udpipe
hr_udpipe_model=~/tools/udpipe-ud-2.5-191206/croatian-set-ud-2.5-191206.udpipe

udpipe=~/tools/udpipe-1.2.0-bin/bin-linux64/udpipe

echo "1. Tokenizing and tagging Slovenian data"
$udpipe --tokenize --parse --tokenizer=presegmented --tag $sl_udpipe_model < parallel/sl.s.mod > parallel/sl.s.conllu
echo "   Tokenization and tagging done."

echo "2. Tokenizing and tagging Croatian data"
$udpipe --tokenize --parse --tokenizer=presegmented --tag $hr_udpipe_model < parallel/hr.s.mod > parallel/hr.s.conllu
echo "   Tokenization and tagging done."

fast_align=/home/toni/tools/fast_align/build/fast_align
atools=/home/toni/tools/fast_align/build/atools

echo "Aligning Slovenian-Croatian pair"
paste parallel/sl.s.mod parallel/hr.s.mod | sed 's/\t/ ||| /' | grep '. ||| .' > alignments/sl-hr
$fast_align -d -o -v -i alignments/sl-hr > alignments/sl-hr.f
$fast_align -d -o -v -r -i alignments/sl-hr > alignments/sl-hr.r
$atools -i alignments/sl-hr.f -j alignments/sl-hr.r -c intersect > alignments/sl-hr.i
echo "Aligning Slovenian and Croatian done."