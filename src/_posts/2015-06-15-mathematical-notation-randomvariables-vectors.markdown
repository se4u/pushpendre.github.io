---
title:  "Mathematical Notation Glossary"
layout: post
date:   2015-06-15 08:14:10
---
It is extremely useful to settle on good notation at the beginning of a project.
Of course we seldom know exactly which concepts are going to be involved in the project and
what would be the similarities and differences between the concepts involved.
This problem is like the problem of class/type design in software.
Once we know what would be involved we can shape the syntactic notation to mirror those similarities and differences.
So this like most interesting problems is a chicken and egg problem.

In any case, if we think of our career/work as a project then at some point in our career we must
gain some idea of what mathematical notations we would usually need for the rest of it.
I feel like I have to come to such a point.

Lets define the following macros, where r is random, u is unknown, k is known, s is scalar, v is vector, m/ma is matrix
^
* `\newcommand{\rs}[1]{#1}`
* `\newcommand{\rv}[1]{\boldsymbol{#1}}`
* `\newcommand{\rm}[1]{\boldsymbol{#1}}`
* `\newcommand{\us}[1]{\mathsf{#1}}`
* `\newcommand{\uv}[1]{\mathbf{#1}}`
* `\newcommand{\um}[1]{\mathbf{#1}}`
* `\newcommand{\ks}[1]{\mathtt{#1}}`
* `\newcommand{\kv}[1]{\mathtt{#1}}`
* `\newcommand{\km}[1]{\mathtt{#1}}`

{% kramdown_include notationmatrix %}

\\
Other interesting fonts are mathfrak and mathscr
^
| mathfrak | $\mathfrak{ABCdef \; UVWxyz}$ |
| mathscr  | $\mathscr{ABCdef \; UVWxyz} $ |
