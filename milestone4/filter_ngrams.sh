#!/bin/bash

# reads each line of train_data_tokens.txt as element in array "tokens"
IFS=$'\r\n' GLOBIGNORE='*' command eval  'tokens=($(cat ~/train_data_tokens.txt))'

declare -a folders=(
"/nlp/data/corpora/LDC/LDC2006T13/data/3gms/*"
"/nlp/data/corpora/LDC/LDC2006T13/data/4gms/*"
"/nlp/data/corpora/LDC/LDC2006T13/data/5gms/*"
)

# gets 3grams, 4grams, 5grams of all words in the train_data_tokens.txt file
for tok in ${tokens[@]}
do
	for folder in ${folders[@]}
	do
		for f in /nlp/data/corpora/LDC/LDC2006T13/data/3gms/*
		do
			zcat * | grep "^\" ${tok} >> ~/filtered_ngrams.txt
		done
	done
done
