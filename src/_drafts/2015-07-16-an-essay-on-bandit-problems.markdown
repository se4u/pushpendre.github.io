---
title:  "An Essay on Bandit Problems"
layout: post
date:   2015-07-16 17:36:42
---
A Bandit Problem is a

A Reward Sequence

A k-tuple of stochastic processes

A strategy for selecting one stochastic process out of many.

An objective that depends on the processes sampled.

Variants

Maybe we get to select two at a time without replacement?
Maybe we have to maximize


Applications
Choosing Medicine
Choosing Ad

Choosing a job? (What if one of the processes is also dependent on your choices so far? Then its something like an MDP since I can just encode the impossible decisions as having a deterministic negative infinite payout, but its not an MDP since an MDP also has an extra uncertainity about what actually happened when we decided to do something. It would be like saying that we decided to choose job A but accidentally sent our resume to job B.)
Usually your selections affect the stochastic processes themselves. The key is to understand that in a bandit problem your selections are not affecting your future prospects. If your selection does not affect the future then this model is applicable. So for example bandits would not be a good model for selections that a single agent makes(ala. a markov decision process) but rather it would be a good model for deciding whether you want to sample this dish in a restaurant. Let's say you want to model which girl amongst k you should date? So in a sense we are assuming that after our choice we get instant feedback, there is no delayed reward)
Choosing gifts for your wedding anniversary to maximize harmony
What if there is divorce? Let's say there is a constant chance that in any year you would get divorced that does not depend on how long you are already married
Clearly this model would only work best if the

Optimal Strategy

Methods for solving this

Dynamic Programming (optimizing)


Myopic Strategies
Now why would we use myopic strategies

Analysis

Regret, The MiniMax Approaches
