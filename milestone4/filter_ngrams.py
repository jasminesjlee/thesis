# !/usr/bin/env python

import gzip
import string
import os
import re

if __name__ == '__main__':
    ngram_folders = [
        "/nlp/data/corpora/LDC/LDC2006T13/data/3gms",
        "/nlp/data/corpora/LDC/LDC2006T13/data/4gms",
        "/nlp/data/corpora/LDC/LDC2006T13/data/5gms"
        ]

    template_files = [
        "sorted_new_templates_3",
        "sorted_new_templates_4",
        "sorted_new_templates_5"
        ]

    write_files = [
        "filtered_ngrams/ngrams_3.txt",
        "filtered_ngrams/ngrams_4.txt",
        "filtered_ngrams/ngrams_5.txt"
        ]

    punc_set = {c for c in string.punctuation}
    import pdb; pdb.set_trace()
    # we iterate through 3grams, 4grams, 5grams
    for ngram_folder, template_file, write_file in zip(ngram_folders, template_files, write_files):
        print("LOADING FROM " + ngram_folder.split('/')[-1])
        templates = open(template_file)
        curr_template = templates.readline()
        write_file = open(write_file, 'w')

        for path in os.listdir(ngram_folder):
            with gzip.open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    while line < curr_template:
                        curr_template = templates.readline()
                    line = line.split()
                    if len(line) == 0 or any([line[i] in punc_set for i in range(len(line))]):
                        continue
                    else:
                        pattern = r"" + re.escape(curr_template)
                        if re.search(pattern, line):
                            write_file.write(line)
