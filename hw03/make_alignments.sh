moses_dir=/home/toni/tools/playground/playground/s.mosesgiza.f4b8a236.20220320-1443

./gizawrapper.pl \
 --bindir=$moses_dir/bin/ \
 el-sr/SETIMES.el-sr.el \
 el-sr/SETIMES.el-sr.sr \
 --dirsym=left,right,int,union | gzip > el-sr.ali.gz

echo "Done normal alignments EL-SR"

for f in el-sr/SETIMES.el-sr.??; do
  cat $f | /home/toni/tools/playground/scripts/lowercase.pl | /home/toni/tools/playground/scripts/stem_factor.pl > $f.lcstem4
done

echo "Done lowercase and stem processing"

mv el-sr/SETIMES.el-sr.el.lcstem4 el-sr/SETIMES.el-sr.lcstem4.el
mv el-sr/SETIMES.el-sr.sr.lcstem4 el-sr/SETIMES.el-sr.lcstem4.sr

./gizawrapper.pl \
  --bindir=$moses_dir/bin/ \
  el-sr/SETIMES.el-sr.lcstem4.el \
  el-sr/SETIMES.el-sr.lcstem4.sr \
  --dirsym=left,right,int,union | gzip > el-sr.lcstem4.ali.gz

echo "Done processed alignments EL-SR"
