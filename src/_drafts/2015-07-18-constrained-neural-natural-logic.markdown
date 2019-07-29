---
title:  "Constrained Vector Space Semantics for Natural Logic"
layout: post
date:   2015-07-18 22:44:47
---
Samuel Bowman, a phd student advised by Christopher Manning and
Christopher Potts published the following series of papers in the past
couple of years. In this article I would summarize these papers and
also point out one simple extension that should help improve the current methods.

| Paper Id | Year | Title                                                                 | Venue              | Dataset/Experiments                    |
|----------+------+-----------------------------------------------------------------------+--------------------+---------------------|
|        1 | 2015 | Recursive Neural Networks Can Learn Logical Semantics                 | ACL Workshop       | SICK, Boolean Model |
|        2 | 2015 | Learning Distributed Word Representations for Natural Logic Reasoning | AAAI KRR Symposium |                     |
|        3 | 2014 | Can recursive neural tensor networks learn logical reasoning?         | ICLR               | Short Phrases                    |

One thing you might notice is that the titles all read the same and
personally I was only able to keep the differences between them
straight in my head after deconstructing the titles by their phrases.
The relevant phrases are

| Paper Id | Phrase                          | Meaning                                                                                                    |
|----------+---------------------------------+------------------------------------------------------------------------------------------------------------|
|        1 | Logical Semantics               | Same as natural logic reasoning                                                                            |
|      1,3 | Recursive                       | The representations are created from parses of the strings.                                                |
|        1 | Recursive Neural Network(RNN)   | Use a tree structured LSTM RNN instead of an RNTN                                                          |
|        2 | Distributed Word Representation |                                                                                                            |
|        3 | Recursive Neural Tensor Network |                                                                                                            |
|        2 | Natural Logic Reasoning         |                                                                                                            |
|        3 | Logical Reasoning               | Logical reasoning is actually just natural logic entailment over short synthetic phrases with quantifiers. |



The 3 papers that I am summarizing are different from each other in
terms of the specific model that was used and the exact task that was
performed using those networks. These papers are largely empirical and
actually the first paper contains a large number of details about how
the dataset was created and tested that it would be better to not
repeat here.

I would just say that the experiments in the paper
"Can recursive neural tensor networks learn logical reasoning?" showed
that atleast when the training set contains sufficient in-domain data
then an RNTN (that require the parse of a sentence) can be trained to
map phrases to representations which can then be passed
through a one/two layer neural network that has a classifier on top
and trained to perfection (100% test accuracy).

WordNet noun graph
