#!/usr/bin/env python

from nltk.stem import WordNetLemmatizer

if __name__ == "__main__":
    lemmatizer = WordNetLemmatizer()
    files = ["../milestone2/data_splits/train.txt", "../milestone2/data_splits/val.txt",
             "../milestone2/data_splits/test.txt"]
    out_files = ["train_lemma.txt", "val_lemma.txt", "test_lemma.txt"]
    for idx, file in enumerate(files):
        out = open(out_files[idx], 'w')
        with open(file) as f:
            for line in f:
                words = [word for word in line.split('\t')]
                for i, word in enumerate(words):
                    words[i] = lemmatizer.lemmatize(words[i])
                out.write('\t'.join(words) + '\n')

