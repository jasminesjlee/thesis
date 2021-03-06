# Literature Review

Determining noun phrase bracketing is crucial to capturing the semantics of a noun phrase. For example, given the noun phrase “home delivery system”, if the noun phrase is left branching, it would mean “a system that specializes in delivering packages to homes.” On the other hand, if the phrase is right branching, it would mean “a system that specializes in delivering homes to people.” 

A classifier that labels a phrase as left-branching or right-branching could allow for better representations of the meaning of noun phrases, which could in turn have a cascading effect down the NLP pipeline and in the end, improve performance on other tasks. For example, Green (2011)found that access to the dependency parsing of internal noun phrase structure resulted in a 2.43% improvement for English to Czech machine translation.

Representing the meaning of sequences of words, such as noun phrases, is a challenge that many NLP reserrchers have tackled. Though more headway has been made in the arena of using vectors to represent words, how can these word representations be combined to create representations for longer sequences of words?

Before exploring how to computationally capture meaning, it is important to understand from a linguistics standpoint what it is that gives a sentence meaning. Barbara H. Partee (1995) wrote that truth conditions are a fundamental part of what the meaning of a sentence is. In a particular situation, if one of two sentences is true and the other is false, then they have different meanings. If two sentences have the same truth conditions in all situations, then we can use this as evidence to argue that they have the same meaning. 

In particular, Partee breaks down how to capture different semantic roles of words in noun phrases through a compositional syntactic/semantic analysis. Each sentence must be mapped to a binary branching tree, and the syntactic structure represented by the trees outlines which set of entities that the noun phrase represents. If the set of entities represented by the binary branching trees corresponding to two noun phrases are the same, then the two noun phrases have the same meaning. Otherwise, they do not.

By Partee’s argument, though the noun phrases “(home delivery) system” and “home (delivery system)” use the same words, depending on whether they are left- or right-branching, they are fundamentally different in meaning. Thus, it is crucial to be able to develop a system that can classify them differently, so that these judgements can later be used to contribute to how an embedding representing a noun phrase is generated.

In previous work, many composition models--models that generate a fixed-size representation for a sequence of words by somehow combining the representation of the individual words--have been experimented with. Wieting et. al (2015) found that on the task of learning general purpose, paraphrastic sentence embeddings based on supervision from PPDB, simply averaging the word vectors of a sequence of words better captured the sentence’s semantics than did using highly complex architectures, such as LSTMs or RNNs. However, the downfall of averaging is that since it uses bag-of-words, it does not take word order into account, so it does not take full advantage of context when extracting the meaning of phrases. Additionally, since it only takes into account what words are in the sequence, it does not take the dependency parsing into account. 

Some researchers have explored different ways of representing noun compounds. Of the tasks of representing word sequences, the task of representing noun compounds is particularly difficult because the implicit semantic relation between the two nouns is not always clear. For example, though the noun compounds "baby oil" and "olive oil" look similar, the implicit semantic relation between the two nouns is different in each case: in the former, the oil is made *for* babies, and in the latter, the oil is made *by* olives. Shwartz and Waterson (2018) focused on the fact that for different noun compounds, the words in the noun compound have different implicit semantic relations. Thus, Shwartz and Waterson implemented automatic interpretation of the relation between constituents of a noun compound by using a neural paraphrasing approach. In their model, they collect all the paraphrases of a noun compound (the patterns connecting the joint occurrences of the constituents in a corpus). For example, both “paper cup” and “steel knife” are connected by the dependency path “MADE OF”. Then, for each of these dependency paths, they learn a path embedding by encoding the edge vectors (for each edge of the path) with an LSTM and using the last output vector as the path embedding. Finally, they use a weighted average of all the path embeddings for a given noun compound as the feature vector for that noun compound. Though previous approaches based on either noun-compound representations or paraphrases have shown promising results, it is likely that these models have performed well because they have memorized prototypical words for each relation. Shwartz and Waterson’s neural paraphrasing approach, on the other hand, shows much better performance in settings where lexical memorization is impossible.

Shwartz and Dagan (2018) also investigated using a neural model to label noun compounds with the implicit semantic relation between their constituents. Many previous paraphrasing methods lack the ability to generalize, and have a hard time interpreting new noun-compounds. In this paper, they trained a model to (1) given a noun compound, predict a paraphrase () that expresses the semantic relation of the noun compound (ex. cake ___ apple) or a missing constituent given a combination of a noun compound and a paraphrase (ex. cake MADE OF w1). Constituents and paraphrase templates are represented as continuous vectors, so that semantically similar paraphrase templates are embedded more closely together. 

In their model, they encoded each word using its 100-dimensional pre-trained GloVE embedding, as well as learned embeddings for [w1], [w2], and [p] for each training instance (w2, p, w1). They learned the embeddings for [w1], [w2] and [p] of each instance by encoding the sequence of words surrounding each of [w1], [w2], and [p] using a bi-LSTM, then using the output vector corresponding to the given element as its embedding. Since we use a bi-LSTM, the output vector is a concatenation of the outputs of the forward and backward LSTMs, so the output vector contains information on valid substitutions with respect to both the previous words and the subsequent words. Then, they use these embeddings to predict the missing component for each noun compound. They found that their neural model generalizes better than other models because it represents paraphrases in a continuous space, and thus can generalize well on unseen and infrequent noun compounds. 

Other papers have focused on methods that can be generalized to noun-phrases. Because internal NP bracketing is not available on many widely used parsers, many researchers in early papers have attempted to solve the NP bracketing problem with unsupervised methods based on statistics from unannotated corpora (Lauer, 1995) or web hit counts (Lapata and Keller, 2004; Nakov and Hearst, 2005a).

An initial method for solving the NP bracketing task that was first described in Marcus (1980) is called the adjacency model. Given a noun phrase [w1] [w2] [w3], if [w1] [w2] is semantically unacceptable or [w2] [w3] is semantically unacceptable, it first groups together the alternative two words. Otherwise, if [w1] [w2] are more semantically associated than [w2] [w3], then the noun phrase is labeled as left-branching, and vice versa.

Lauer (1995) proposes the dependency model, which instead compares how semantically acceptable [w1] [w2] and [w1] [w3] are. If [w1] [w3] is more acceptable, then the phrase is labeled as left-branching. He argues that this is because there are many cases where [w1] [w2] is a plausible compound, and [w2] [w3] is a plausible compound and that often, [w2] is similar to [w3] whether or not the phrase is right-branching. The correct parse instead depends on whether w1 characterizes [w2] or [w3]. For example, given the phrase "calcium ion exchange:, both "calcium ion" and "ion exchange" are used frequently. The correct parse depends on whether "calcium" characterizes the "ions" or mediates the "exchange." Nakov and Hearst (2005a) also use web counts, but they incorporate additional counts from several variations on simple bigram queries, including queries for the pairs of words concatenated or joined by a hyphen.

Vadas and Curran (2008) were one of the first to use a supervised approach to annotating the inner structure of NPs. They trained a Maximum Entropy classifier using annotated noun phrases from the Penn Treebank. For each query, they got a bigram count of [w1] [w2], a bigram count of [w2] [w3], and lexical features for all unigrams, bigrams, and the trigram within the NP.

A task related to noun phrase parsing is that of query segmentation. The task of noun phrase bracketing is one that determines the syntactic structure of an noun phrase by predicting the bracketing--deciding whether the three-word noun phrase has a left or right-bracketing structure. On the other hand, the task of query segmentation handles the case where the query consists of multiple, separate noun phrases that need to be distinguished as separate entities. Though the two tasks of noun phrase bracketing and query segmentation are distinct, it is plausible that methodologies that are effective for query segmentation are also effective for noun phrase bracketing. 

Bergsma and Wang (2007) propose a data-driven, machine-learned approach to query segmentation. In the task of segmentation classification, the task is to determine the segmentation of a query, where there can be a segmentation break at any of the N-1 spaces between the N tokens. The full query segmentation is created as the combination of independent classification decisions made between each pair of tokens in the query. Thus, at test time, N-1 segmentation decisions are made for the N length query, and an output segmentation is produced. For a decision between two words, features are extracted from the surrounding 6 words (3 to left and 3 to right). 

Decision boundary features and context-based features were used. Decision boundary features included  rule-based features targeting words that often have a decision boundary next to it (like “the”), POS-tags for the two tokens between which the decision boundary being classified lies, the position of the decision boundary, and the mutual information between the two tokens. Using the log of the pointwise mutual information allows the model to detect when two words have a high co-occurrence count because they are related concepts, but do not often occur contiguously and thus are not phrasal constituents. 

Context-based features such as trigram and fourgram web and query-database counts of the tokens around the decision boundary as well as additional neighboring words. For example, for the query “bank loan amortization schedule”, though “loan amortization” has a strong connection, we may nevertheless insert a break between them because “bank loan” and “amortization schedule” each have even stronger association.

## References
Bergsma, S., & Wang, Q. I. (2007). Learning noun phrase query segmentation. In Proceedings of the 
  2007 Joint Conference on Empirical Methods in Natural Language Processing and Computational 
  Natural Language Learning (EMNLP-CoNLL).
  
Lapata, M., & Keller, F. (2004). The web as a baseline: Evaluating the performance of unsupervised web-
  based models for a range of NLP tasks. In Proceedings of the Human Language Technology Conference of 
  the North American Chapter of the Association for Computational Linguistics: HLT-NAACL 2004.
  
Lauer, M. (1995). Corpus statistics meet the noun compound: some empirical results. 
  
Nakov, P., & Hearst, M. (2005, June). Search engine statistics beyond the n-gram: Application to noun 
  compound bracketing. In Proceedings of the Ninth Conference on Computational Natural Language 
  Learning (pp. 17-24). Association for Computational Linguistics.

Partee, B. (1995). Lexical semantics and compositionality. An invitation to cognitive science: Language, 1, 
  311-360.
  
Shwartz, V., & Dagan, I. (2018). Paraphrase to Explicate: Revealing Implicit Noun-Compound Relations. 
  arXiv preprint arXiv:1805.02442.
  
Shwartz, V., & Waterson, C. (2018). Olive Oil is Made of Olives, Baby Oil is Made for Babies: Interpreting 
  Noun Compounds using Paraphrases in a Neural Model. arXiv preprint arXiv:1803.08073.
  
Wieting, J., Bansal, M., Gimpel, K., & Livescu, K. (2015). Towards universal paraphrastic sentence 
  embeddings. arXiv preprint arXiv:1511.08198.
  
Vadas, D., & Curran, J. R. (2008, June). Parsing noun phrase structure with CCG. In Proceedings of ACL-
  08: HLT (pp. 335-343).
  
Yu, M., & Dredze, M. (2015). Learning Composition Models for Phrase Embeddings. Transactions Of The 
  Association For Computational Linguistics, 3, 227-242. Retrieved from 
  https://transacl.org/ojs/index.php/tacl/article/view/586

