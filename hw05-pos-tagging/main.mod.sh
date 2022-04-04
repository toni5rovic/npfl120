
en_udpipe_model=~/tools/udpipe-ud-2.5-191206/english-lines-ud-2.5-191206.udpipe
tur_udpipe_model=~/tools/udpipe-ud-2.5-191206/turkish-imst-ud-2.5-191206.udpipe
rus_udpipe_model=~/tools/udpipe-ud-2.5-191206/russian-gsd-ud-2.5-191206.udpipe

udpipe=~/tools/udpipe-1.2.0-bin/bin-linux64/udpipe

echo "1. Tokenizing and tagging English data"
$udpipe --tokenize --tokenizer=presegmented --tag $en_udpipe_model < data/en.s.mod > output/en.s.mod.conllu
echo "   Tokenization and tagging done."

echo "2. Tokenizing and tagging Turkish data"
$udpipe --tokenize --tokenizer=presegmented --tag $tur_udpipe_model < data/tr.s.mod > output/tr.s.mod.conllu
echo "   Tokenization and tagging done."

echo "3. Tokenizing and tagging Russian data"
$udpipe --tokenize --tokenizer=presegmented --tag $rus_udpipe_model < data/ru.s.mod > output/ru.s.mod.conllu
echo "   Tokenization and tagging done."

echo "4. Tokenizing Kazakh data (using Turkish model)"
$udpipe --tokenize --tokenizer=presegmented $tur_udpipe_model < data/kk.s.mod > output/kk.s.mod.conllu
echo "   Tokenization done."

