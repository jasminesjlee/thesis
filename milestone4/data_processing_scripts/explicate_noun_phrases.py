from nltk.stem import WordNetLemmatizer
import argparse
import numpy as np
import random
import spacy

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Linear model baseline')
    parser.add_argument('--train', type=str, help='Path to training file', required=True)
    parser.add_argument('--valid', type=str, help='Path to valid file', required=True)
    parser.add_argument('--test', type=str, help='Path to test file', required=True)
    parser.add_argument('--out', type=str, help='Path to output file', default="pred.txt")
    parser.add_argument('--ngrams_file', type=str, help='Path to ngrams file', required=True)
    parser.add_argument('--templates_file', type=str, help='Embeddings file', required=True)
    args = parser.parse_args()

    # load spacy POS tagger
    nlp = spacy.load('en_core_web_sm')
    
    # read data
    train = open(args.train).readlines()
    test = open(args.test).readlines()

    print("Processing templates file...")
    templates = [[], [], []]
    template_to_id = {}

    # organize templates by number of words
    for line in open(args.templates_file):
        templates[len(line.split()) - 3].append(line.strip())
        template_to_id[line.strip()] = len(template_to_id)

    print("Extracting features...")
    
    
    y = np.zeros(len(train))
    X = np.zeros((len(train), len(template_to_id)*2))
    y_test = np.zeros(len(test))
    X_test = np.zeros((len(test), len(template_to_id)*2))
    
    # extract features for training data
    for i, l in enumerate(train):
        y[i] = l.split('\t')[-1]
        w1, w2, w3 = l.split('\t')[:-1]
        sent_feat = []
        for word in w2, w3:
            # want to see how many 3/4/5-grams of w1 w2 fit the template vs.
            # how many 3/4/5-grams of w2 w3 fit the template
            with open(args.ngrams_file) as f:
                for line in f:
                    line.strip('"').strip()
                    line_pos = []
                    wordpair_feat = np.zeros(len(template_to_id) * 2)
                    if line.startswith(word):
                        # extract POS tags of line
                        sent = nlp(line)
                        for token in sent:
                            line_pos.append(token.pos_)
                        for temp in templates[len(sent)-3]:
                            # check if this template matches the current ngram
                            if " ".join(line_pos[1:-1]) == temp:
                                wordpair_feat[template_to_id[temp]] += 1
            sent_feat += wordpair_feat
        X[i] = sent_feat
        
     # extract features for test data
    for i, l in enumerate(test):
        y_test[i] = l.split('\t')[-1]
        w1, w2, w3 = l.split('\t')[:-1]
        X_curr = []
        for word in w2, w3:
            # want to see how many 3/4/5-grams of w1 w2 fit the template vs.
            # how many 3/4/5-grams of w2 w3 fit the template
            with open(args.ngrams_file) as f:
                for line in f:
                    line.strip('"').strip()
                    line_pos = []
                    X_curr = []
                    curr_word = np.zeros(len(template_to_id) * 2)
                    if line.startswith(word):
                        # extract POS tags of line
                        sent = nlp(line)
                        for token in sent:
                            line_pos.append(token.pos_)
                        for temp in templates[len(sent)-3]:
                            # check if this template matches the current ngram
                            if " ".join(line_pos[1:-1]) == temp:
                                curr_word[template_to_id[temp]] += 1
            X_curr += curr_word
        X_test[i] = X_curr











