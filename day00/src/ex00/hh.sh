#!/bin/sh

# result=$(echo $1 | sed 's/ /+/g')

# curl "https://api.hh.ru/vacancies?text=$result" | jq > hh.json

curl "https://api.hh.ru/vacancies?text=data+scientist" | jq > hh.json