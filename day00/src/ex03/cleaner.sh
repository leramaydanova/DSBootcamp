#!/bin/sh


jq -r '["id", "created_at", "name", "has_test", "alternate_url"], (.items[] 
    | [.id, .created_at, (.name 
    | [match("(Junior|Middle|Senior)"; "gi")
    | .string]
    | unique
    | if length > 0 then join("/") else "-" end), 
    .has_test, .alternate_url]) | @csv' ../ex00/hh.json > hh_positions.csv

head -n 1 hh_positions.csv > temp.csv
tail -n +2 hh_positions.csv | sort -t, -k2,2 -k1,1n >> temp.csv

cat temp.csv > hh_positions.csv 
rm temp.csv