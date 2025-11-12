#!/bin/sh

dest="hh_sorted.csv"
src="../ex01/hh.csv"

head -n 1 $src > $dest
tail -n +2 $src | sort -t, -k2,2 -k1,1n >> $dest