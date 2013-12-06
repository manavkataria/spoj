#!/bin/bash
# Usage: 
# cd ./INVCNT/ (directory containg source-code)
# ../myUnit.sh invcnt.py

rst=$(tput sgr0)
txtbld=$(tput bold)             # Bold
bldred=${txtbld}$(tput setaf 1) #  red
bldgre=${txtbld}$(tput setaf 2) #  green
bldblu=${txtbld}$(tput setaf 4) #  blue
warn=${bldred}-${txtrst}
pass=${bldblu}-${txtrst}

echo "== Running Tests =="

for infile in $(ls in.*)
do
        echo -en "$infile \t"
        ./$1 < $infile &> result.tmp
        outfile=`echo $infile | sed 's/in\./out\./g'`
        diff $outfile result.tmp > diff.tmp
        if [ -s 'diff.tmp' ]; 
            then echo "$warn Fail! $rst"; 
            else echo "$pass Success! $rst"; 
        fi
        rm diff.tmp result.tmp
done

echo "== Done =="
