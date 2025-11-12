#!/bin/sh

src=$(ls | grep -E '^[0-9]{4}-[0-9]{2}-[0-9]{2}\.csv$')
dest='hh_positions.csv'

first_file=true

for file in $src;
do 
    if [ $first_file = true ]; then
        cat $file > $dest
        first_file=false
    else 
        tail -n +2 $file >> $dest
    fi
done