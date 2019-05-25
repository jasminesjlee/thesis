The evaluation script is the file
  eval.py
  
To run the script on a given predictions file and gold labels file, you can type the following into your terminal:
  > python eval.py predictions_file goldlabels_file
  
I base my decision to use precision, recall, and F-score on the use of these metrics in the papers "Adding Noun Phrase Structure to the Penn Treebank" and "Parsing Noun Phrase Structure with CCG" by David Vadas and James R. Curran.
