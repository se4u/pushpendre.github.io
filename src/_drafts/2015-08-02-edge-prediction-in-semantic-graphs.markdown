---
title:  "Edge Prediction in Semantic Graphs"
layout: post
date:   2015-08-05 13:48:43
---

## Preliminaries and Notation ##

We are given a domain of entities $\mathcal{E} = {a, b, c, \ldots}$ and we are
provided binary relations between these entities $\mathcal{R} = {P, Q, R, \ldots}$.
{% fn %}
Also we have access to closure rules $\mathcal{C}$.
Let $e_i, r_j, c_k$ be metavariables useful for indexing over the
entities, relations and closure rules.
The sizes of $ \mathcal{E}, \mathcal{R}, \mathcal{C}$ are
$ \ks{E}, \ks{R}, \ks{C}$ respectively.
a closure rule $c_k$ is a constraint an example of which is the following:

$$ \text{If } e_1\ r_1\ e_2 \text{ And } e_2\ r_2\ e_3 \text{ Then } e_1\ r_3\ e_3$$

Now very generally we can view training examples as strings in a
language of tuples where if two strings are present in a language then
a third string must also be present as well. And the examples that we
are presented are
There are two other isomorphic ways to visualize these entities, relations
and closure rules:

1. As nodes and typed edges in a graph, with constraints over the
   cliques in a graph. We observe edges that stay within a graph cut
   but not those that cross a cut. Or more generally we observe edges
   that stay within a connected cluster but not those that would cross
   across a cluster. And we may learn about the edges within a cluster
   independently of edges within another cluster.
2. As colored locations in a 2d automata, with constraints over the
   fill of the colored locations.


### An Example ###

Let $ \mathcal{E} = {a, b, c}$, $ \mathcal{R} = {P, Q, R}$ and

$$
\begin{equation*}
 \mathcal{C} =
 \begin{cases}
e_1\ P \ e_3 & \text{If } e_1\ P \ e_2 \text{ And } e_2\ Q \ e_3 \\
e_1\ R \ e_3 & \text{If } e_1\ Q \ e_2 \text{ And } e_2\ R\ e_3 \\
e_1\ R \ e_3 & \text{If } e_1\ Q \ e_2 \text{ And } e_2\ P\ e_3
 \end{cases}
\end{equation*}
$$

<div markdown="1" class="note">
Our rules look rigid. If we want other rules then we would have to
either express them in the specific form we have chosen or forego
them.

For example, consider the following rules. Rule 1) can be expressed by
unrolling it into explicit rules about the relations but that would
not be possible if the number of rules is large. Rule 2) and 3) can
not really be expressed easily in our framework.

$$
\begin{align*}
e_1\ R \ e_3  & \text{ If } e_1\ r_1 \ e_2 \text{ And } e_2\ R\ e_3 \\
e_1\ R \ e_3  & \text{ If } e_1\ r_1 \ c \text{ And } c \ R\ e_3 \\
a \ R \ e_3   &\text{ If } a \ Q \ e_2 \text{ And } e_2\ R\ e_3
\end{align*}
$$

Also consider the case where we have other type of rules for example

$$
\begin{equation}
e_1\ R \ e_2 \text{ If } e_2\ R\ e_1
\end{equation}
$$
</div>


### 2d Automata Visualizations ###

Let us assign a color to each predicate, then our closure rules can be
represented as the following:

{% colortable %}
P:red Q:blue R:green
  | P | Q | R |
P |   | P |   |
Q |   | R | R |
R |   |   |   |
{% endcolortable %}

<div markdown="1" class="note">
Our colored automata analogy breaks down if there can be more than one
relation between the entities. But if the closure rules are written to ensure
that there should be only type of relation between any two entities
then the colored automata analogy holds true.
</div>


### Previous Work ###

<div markdown="1" class="warning">
This list is incomplete!
</div>


### Interesting Questions ###
<div markdown="1" class="warning">
This list is incomplete!
</div>

Now the interesting questions are as follows:

1. If we are given a random sample of the strings from the language
   then how can we best use the rules?
2. If we are given biased samples of the edges in the graph such that
   we don't see edges that cross a cut boundary then how can we
   recover the edges?

## Footnotes ##
{:.no_toc}
{% footnotes %}
{% fnbody %}
  Throughout this article, we represent the entities in lower case and the binary relations in upper case.
{% endfnbody %}
{% endfootnotes %}
