import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from nltk.stem import WordNetLemmatizer
import argparse
import codecs

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Complex baseline')
    parser.add_argument('--train', type=str, help='Path to training file', required=True)
    parser.add_argument('--test', type=str, help='Path to test file', required=True)
    parser.add_argument('--out', type=str, help='Path to output file', default="pred.txt")
    parser.add_argument('--n_neighbors', type=int, help='Number neighbors to consider in KNN', default=1)
    args = parser.parse_args()

    lemmatizer = WordNetLemmatizer()

    print("Loading Glove Model")
    model = {}

    f = open("glove.6B.300d.txt", 'r+', encoding="utf-8")

    train = open(args.train).readlines()
    test = open(args.test).readlines()

    for line in f:
        splitLine = line.split()
        word = splitLine[0]
        embedding = np.array([float(val) for val in splitLine[1:]])
        model[word] = embedding
    print("Done.", len(model), " words loaded!")

    print("Converting data...")

    y = np.zeros(len(train))
    X = np.zeros((len(train),300))
    y_test = np.zeros(len(test))
    X_test = np.zeros((len(test), 300))

    for i, l in enumerate(train):
        y[i] = l.split('\t')[-1]
        words = l.split('\t')[:-1]
        for w in words:
            new_w = lemmatizer.lemmatize(w.lower())
            if new_w in model:
                X[i] += model[new_w]

    for i, l in enumerate(test):
        y_test[i] = l.split('\t')[-1]
        words = l.split('\t')[:-1]
        for w in words:
            new_w = lemmatizer.lemmatize(w.lower())
            if new_w in model:
                X_test[i] += model[new_w]

    print("Training model...")

    neigh = KNeighborsClassifier(n_neighbors=args.n_neighbors)
    neigh.fit(X, y)

    print("Making predictions...")
    pred = neigh.predict(X_test)


    print("Writing to file...")
    out = open(args.out, 'w')
    for elt in pred:
        out.write(str(int(elt)))
        out.write('\n')

    print("Done.")
