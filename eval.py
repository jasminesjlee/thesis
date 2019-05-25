#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
from sklearn.metrics import precision_recall_fscore_support
import argparse

def eval(true_labels, pred_labels):
    y_true = []
    with open(true_labels) as f:
        lines = f.readlines()
        for l in lines:
            y_true.append(l.split('\t')[1])
    y_true = np.array(y_true)
    with open(pred_labels) as f:
        lines = f.readlines()
    y_pred = np.array(lines)
    res = precision_recall_fscore_support(y_true, y_pred, average='weighted')
    s = "Precision:%f | Recall:%f | F-Score: %f" % (res[0], res[1], res[2])
    print(s)
def main():
    parser = argparse.ArgumentParser(description='Evaluation script')
    parser.add_argument('-i', type=str,help='Path to pred')
    parser.add_argument('-a', type=str, help='Path to gold')
    args = parser.parse_args()
    if not args.i:
        print('ERROR: The pred labels path is required')
        parser.exit(1)
    if not args.a:
        print('ERROR: The gold labels folder is required')
        parser.exit(1)
    eval(args.i,args.a)

if __name__ == '__main__':
    main()
