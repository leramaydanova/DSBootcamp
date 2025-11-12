#!/bin/sh

src='../ex03/hh_positions.csv'

dates=$(awk -F',' '{print $2}' $src \
    | tail -n +2 \
    | cut -d'T' -f1 \
    | tr -d '"' \
    | sort \
    | uniq)

head=$(head -n 1 $src)

for d in ${dates[@]}; 
do 
    dest="$d.csv"
    echo $head > $dest
    grep $d $src >> $dest
done