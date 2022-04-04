fast_align=/home/toni/tools/fast_align/build/fast_align
atools=/home/toni/tools/fast_align/build/atools

echo "Aligning English-Kazakh pair"
paste data/en.s.mod data/kk.s.mod | sed 's/\t/ ||| /' | grep '. ||| .' > alignments/en-kk
$fast_align -d -o -v -i alignments/en-kk > alignments/en-kk.f
$fast_align -d -o -v -r -i alignments/en-kk > alignments/en-kk.r
$atools -i alignments/en-kk.f -j alignments/en-kk.r -c intersect > alignments/en-kk.i
echo "Aligning English-Kazakh done."

echo "Aligning Turkish-Kazakh pair"
paste data/tr.s.mod data/kk.s.mod | sed 's/\t/ ||| /' | grep '. ||| .' > alignments/tr-kk
$fast_align -d -o -v -i alignments/tr-kk > alignments/tr-kk.f
$fast_align -d -o -v -r -i alignments/tr-kk > alignments/tr-kk.r
$atools -i alignments/tr-kk.f -j alignments/tr-kk.r -c intersect > alignments/tr-kk.i
echo "Aligning Turkish-Kazakh done."

echo "Aligning Russian-Kazakh pair"
paste data/ru.s.mod data/kk.s.mod | sed 's/\t/ ||| /' | grep '. ||| .' > alignments/ru-kk
$fast_align -d -o -v -i alignments/ru-kk > alignments/ru-kk.f
$fast_align -d -o -v -r -i alignments/ru-kk > alignments/ru-kk.r
$atools -i alignments/ru-kk.f -j alignments/ru-kk.r -c intersect > alignments/ru-kk.i
echo "Aligning Russian-Kazakh done."