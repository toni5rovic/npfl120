align_type=$1
src=$2
dst=$3
use_processed=${4:--use_processed}

improved=""
if [ "$use_processed" = "--use_processed" ] ; then
    improved="\.lcstem4"
fi

paste $src-$dst/SETIMES.$src-$dst$improved.$src \
$src-$dst/SETIMES.$src-$dst$improved.$dst \
 <(zcat $src-$dst$improved.ali.gz ) \
| cut -f 1,2,$align_type | ./alitextview.pl | less
