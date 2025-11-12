#!/bin/sh

jq -f filter.jq ../ex00/hh.json | jq -r '. | @csv' > hh.csv