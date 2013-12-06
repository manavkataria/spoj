#!/bin/bash

echo "== Running Tests =="

for infile in $(ls in.*)
do
        echo -en "$infile \t- "
        ./$1 < $infile &> result.tmp
        outfile=`echo $infile | sed 's/in\./out\./g'`
        diff $outfile result.tmp > diff.tmp
        if [ -s 'diff.tmp' ]; 
            then echo "Fail!"; 
            else echo "Success!"; 
        fi
        rm diff.tmp result.tmp
done

echo "== Done =="
