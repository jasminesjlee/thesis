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
    echo "LOADING FROM NGRAMS $idx"
    ngram_folder=${ngram_folders[$idx]}
    template_file=${template_files[$idx]}
    write_file=${write_files[$idx]}
    for word_file in ${word_files[@]}
    do
	echo "file : $word_file"
        while IFS='	' read -r t1
        do
            while IFS='	' read -r w1 w2 w3
            do
                zcat $ngram_folder/* | grep -E "$t1" >> $write_file
            done <$word_file
        done <$template_file
    done
done
