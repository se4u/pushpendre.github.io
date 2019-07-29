---
title:  "Some Exercises for Block Relaxation Optimization"
layout: post
date:   2015-07-19 04:15:42
---
The following optimization problems are examples taken from the chapter on Block Relaxation in the book on Optimization written by Kenneth Lange.

##Sinkhorm Algorithm##
Given a martix $\km{M}$ with positive entries the problem is to find two
positive diagonal matrices $\um{A}, \um{B}$ such that $AMB$ has specific row
sums $r_i$ and column sums $c_j$.

Sinkhorn's theorem guarantees the existence of a solution and the
problem itself can be solved iteratively through block relaxation.

The problem can be stated as:

find $a_i, b_j$ such that $$\sum_i
