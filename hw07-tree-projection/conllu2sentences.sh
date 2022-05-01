#!/bin/bash

if [ -z $1 ]
then
    col=2
else
    col=$1
fi

# skip comments and special tokens, remove spaces inside forms, separate sentences by tabs, join tokens by spaces, separate sentences by newlines
grep -vE '^(#|[0-9]+[-.])' | cut -f$col | sed -e 's/ //g' -e 's/^$/\t/' | tr "\n" " " | tr "\t" "\n" | sed -e 's/^ //' -e 's/ $//'

