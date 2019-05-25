The simple baseline I use is a majority baseline. I chose this baseline because the majority of my data (72% of my training split) is right-branching, whereas only 28% is left-branching. So, when I label all the examples to be right-branching, I expect to get about 70-75% accuracy.

The following table displays the values that my evaluation metric gives to the simple baseline for my test set:
| Precision | Recall   | F1       |
|-----------|----------|----------|
| 0.524812  | 0.724439 | 0.608675 |
