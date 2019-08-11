#!/bin/bash

declare -a ngram_folders=(
"/nlp/data/corpora/LDC/LDC2006T13/data/3gms"
"/nlp/data/corpora/LDC/LDC2006T13/data/4gms/*"
"/nlp/data/corpora/LDC/LDC2006T13/data/5gms/*"
)

declare -a template_files=(
"template_grep_3.txt"
"template_grep_4.txt"
"template_grep_5.txt"
)

declare -a word_files=(
"train_lemma.txt"
"val_lemma.txt"
"test_lemma.txt"
)

declare -a write_files=(
"ngrams_3.txt"
"ngrams_4.txt"
"ngrams_5.txt"
)

for idx in "${!ngram_folders[@]}"
do
    ngram_folder=${ngram_folders[$idx]}
    template_file=${template_files[$idx]}
    word_file=${word_files[$idx]}
    write_file=${write_files[$idx]}
    while IFS='	' read -r t1
    do
        while IFS='	' read -r w1 w2 w3
        do
            #for f in $ngram_folder
            #do
            zcat $ngram_folder/* | grep -E "$t1" >> $write_file
            #done
        done <$word_file
    done <$template_file
done
