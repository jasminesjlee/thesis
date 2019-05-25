The evaluation script is the file
  eval.py
  
To run the script on a given predictions file and gold labels file, you can type the following into your terminal:
  > python eval.py predictions_file goldlabels_file
  
Sample output when the command is run with legal paths for the predictions file and the gold labels file would look like the following:
  > Precision:0.187744 | Recall:0.433294 | F-Score: 0.261975
  
The definitions of the metrics are as follows:
- The precision is the ratio tp / (tp + fp) where tp is the number of true positives and fp the number of false positives. The precision is intuitively the ability of the classifier not to label as positive a sample that is negative.
- The recall is the ratio tp / (tp + fn) where tp is the number of true positives and fn the number of false negatives. The recall is intuitively the ability of the classifier to find all the positive samples.
- The F1 score can be interpreted as a weighted harmonic mean of the precision and recall, where an F score reaches its best value at 1 and worst score at 0.

For all three of these metrics, the higher the score, the better the performance. For the purposes of this task, maximizing F1 score is our goal, though the precision and recall metrics also offer valuable information because they allow us to analyze where our modelis failing (whether it yields too many false positives or too many false negatives).
  
I base my decision to use precision, recall, and F-score on the use of these metrics in the papers "Adding Noun Phrase Structure to the Penn Treebank" and "Parsing Noun Phrase Structure with CCG" by David Vadas and James R. Curran.
