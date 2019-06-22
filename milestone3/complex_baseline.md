# Complex Baseline Description

The more complex baseline that I used was a nearest neighbors baseline (by suggestion of CCB). For each noun phrase in the training set, the model computes a "phrase embedding" for each phrase by summing the pretrained word embeddings for all the words in the phrase. The path of any file containing pretrained embeddings can be passed in to the script -- in my case, I used 300D Glove embeddings, which can be downloaded at https://nlp.stanford.edu/projects/glove/.

To run the script on a given training file and test file, you can type the following into your terminal:
  > python kmeans_baseline.py --train /PATH/TO/TRAINING/FILE --test /PATH/TO/TEST/FILE --out /NAME/OF/PREDICTIONS/FILE --n_neighbors <number_of_neighbors> --embeddings_file /PATH/TO/EMBEDDINGS/FILE
  
If you do not enter anything for --n_neighbors, it will be set to 1 by default. If you do not enter anything for --out, it will be set to "pred.txt" by default.

The below table contains the performance of the model on the validation set.

| n_neighbors | Precision | Recall   | F1       |
|-------------|-----------|----------|----------|
| 1           | 0.824432  | 0.827823 | 0.825790 |
| 2           | 0.810698  | 0.814722 | 0.793986 |
| 3           | 0.804225  | 0.812851 | 0.805537 |

The below table contains the performance of the model on the test set.

| n_neighbors | Precision | Recall   | F1       |
|-------------|-----------|----------|----------|
| 1           | 0.832748  | 0.833541 | 0.833127 |
| 2           | 0.824497  | 0.823566 | 0.804627 |
| 3           | 0.823624  | 0.829800 | 0.824247 |

This model does significantly better than the majority baseline from milestone 2, whose results I have included below for reference.

| Precision | Recall   | F1       |
|-----------|----------|----------|
| 0.524812  | 0.724439 | 0.608675 |
