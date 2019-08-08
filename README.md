# File Outline

### Milestone 1
- **thesis-milestone1.pdf**
: Research proposal

### Milestone 2
- **datasplits**
: Contains files with training split, validation split, test split

- **data.md**
: Gives an example of the data, describes the file format of the data, gives a link to the full data set, and gives a description of where data was collected from.

- **score.py**
: Evaluation script

- **scoring.md**
: Gives a formal definition of your metric, and relevant citations to where it was introduced. Shows how to run your evaluation script on the command line (with example arguments, and example output).

- **simple_baseline.py**
: Code for simple baseline

- **simple_baseline.md**
: Description of simple baseline. Says what score your evaluation metric gives to the simple baseline for your test set.

### Milestone 3
- **complex_baseline.md**
: Contains description of implemented complex baseline

- **kmeans_baseline.py**
: Code for the implemented complex baseline

- **literature_review.md**
: Literature review for project

### Milestone 4
- **templates.txt**
: A list of templates that Vered Shwartz included in [the code for her paper "Paraphrase to Explicate"](https://github.com/vered1986/panic/tree/master/paraphrasing). These paraphrases "explicate" the relation between noun compounds -- for instance, with a given noun compound [w1] [w2], the relation between the two nouns can be reworded as a template such as [w2] VERB [w1]. 
- **explicate_noun_phrases.py**
: I wanted to use explicating the relation among words of a noun phrase as a feature in order to improve noun bracketing (left or right) of 3 word noun compounds. The feature would be, for a given [w1] [w2] [w3], to use how often [w1] [w2] fits the given templates versus how often [w2] [w3] fits the given templates. This script extracts this feature.
- **filter_ngrams.sh**
: A bash script that extracts the 3grams, 4grams, and 5grams that start with words in "train_data_tokens.txt". For a given 3-word noun phrase [w1] [w2] [w3], I wanted to retrieve all n-grams that start with either [w2] or [w3], so I include all words that occur at least once as [w2] or [w3] in the train_data_tokens.txt file.
