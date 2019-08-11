#!/bin/bash

declare -a ngram_folders=(
"/nlp/data/corpora/LDC/LDC2006T13/data/3gms"
"/nlp/data/corpora/LDC/LDC2006T13/data/4gms"
"/nlp/data/corpora/LDC/LDC2006T13/data/5gms"
)

declare -a template_files=(
"template_grep/template_grep_3.txt"
"template_grep/template_grep_4.txt"
"template_grep/template_grep_5.txt"
)

declare -a word_files=(
"lemma_data/train_lemma.txt"
"lemma_data/val_lemma.txt"
"lemma_data/test_lemma.txt"
)

declare -a write_files=(
"filtered_ngrams/ngrams_3.txt"
"filtered_ngrams/ngrams_4.txt"
"filtered_ngrams/ngrams_5.txt"
)

# we iterate through 3grams, 4grams, 5grams
for idx in "${!ngram_folders[@]}"
do
    echo "LOADING FROM NGRAMS $idx"
    # for each ngram set, we use different ngram file, different file of templates, and write to different filtered ngram file
    ngram_folder=${ngram_folders[$idx]}
    template_file=${template_files[$idx]}
    write_file=${write_files[$idx]}
    # for each ngram set, we extract ngrams for training file, valid file, test file
    for word_file in ${word_files[@]}
    do
	echo "file : $word_file"
	# iterate through all templates: of form '${w1} [a-zA-Z]+ {w2}'
        while IFS='	' read -r t1
        do
            # get each noun phrase
            while IFS='	' read -r w1 w2 w3 w4
            do
		# extract all occurrences of the noun phrase with the template
                zcat $ngram_folder/* | grep -E "$t1" >> $write_file
            done <$word_file
        done <$template_file
    done
done
