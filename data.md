My data can be found in the "splits" folder. 80% of my data has been assigned to the training set, and 10% each for validation and test. It is in total 16032 examples, where each line consists of a three-word noun phrase and a label "0" or "1". The label 0 means that the noun phrase is right branching, and the label 1 means that the noun phrase is left branching.

The following line is an example of a line in my training set:
`supermarket checkout machines   1`

The three-word noun phrase is "supermarket checkout machines", and since it is left branching, it is denoted with the label "1".

The data was collected from Penn TreeBank and OneNotes. Though the original Penn TreeBank used flat NPs, the work of Vadas and Curran (2007) annotated the full structure of NPs in the Penn TreeBank’s WSJ corpus. With this, I was able to extract 10613 three-word noun phrases with gold labels. I also was able to extract 5419 three-word noun phrases with gold labels from OpenNotes. 
