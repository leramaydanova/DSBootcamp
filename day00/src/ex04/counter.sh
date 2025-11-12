#!/bin/sh

src='../ex03/hh_positions.csv'

cut -d',' -f3 $src \
    | tail +2 \
    | tr -d '"' \
    | tr '/' '\n' \
    | tr '[:upper:]' '[:lower:]' \
    | grep -v '-' \
    | sort \
    | uniq -ci \
    |sort \
    | awk 'BEGIN {print "\"name\",\"count\""} {printf "\"%s\",\"%d\"\n", $2, $1}' \
 > hh_uniq_positions.csv