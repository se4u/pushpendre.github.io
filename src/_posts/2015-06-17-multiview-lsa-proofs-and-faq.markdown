---
title:  "Multiview LSA Motivation and Proofs"
layout: post
date:   2015-06-17 00:41:10
comments: true
---
<!-- <div class="definition"> </div> -->
When I was presenting my [Multiview LSA (MVLSA)](mvlsa/mvlsa.pdf) paper at NAACL
I seriously felt that I had
left out a lot of the background/motivation/proofs
behind GCCA from the paper due to lack of space and only gave the most essential pieces of the
algorithm.
I still think that it was a good call
since the main point of the paper was to evaluate GCCA's
performance and my own contribution was to A) Make sure that its
computation was fast B) Leverage some methods to handle sparsity C) Do rigorous testing
D) Get the best results possible by tuning hyperparameters.
It's not like I derived GCCA itself.

Anyway, a few people expressed interested in the
derivation/motivation behind the method so I will write it down here.
So this article would serve as a supplemental to the main paper.

In this article I am going to start from scratch and first present (in
words) the motivation that led to GCCA  and then show how equation 1
and equation 3 from the paper result from it.

Once again, I'll note that I am merely rephrasing things that were already derived by
{% cite carroll1968generalization %} and
{% cite kettenring1971canonical %}. However, I do think that
Kettenring's notation is too old and readers might prefer the
simpler notation that I'll use.

* TOC
{:toc}

##What is the motivation for equation 1 in the paper ?##

Alternatively, the question could be that why do I say that the
objective of MAXVAR-GCCA is:

$$ \begin{align}
\arg \min_{G, U_j} \sum_{j=1}^J  || G - X_j U_j ||^2_F \text{ such that } G^TG = I \label{eq:mvlsa}
\end{align}
$$

Just like PCA has at least 3 different interpretations/derivations
GCCA too has multiple interpretations. Let me first state the
motivations in words:

1. MAXVAR GCCA finds a representation that maximizes
   total squared correlation between an auxilliary variable
   and possible rank-$$r$$ linear transformations/distortions of
   the data. (This is *Carroll's starting point*)

2. MAXVAR GCCA of rank $$r$$ finds an orthogonal representation $$G$$
   that minimizes the total squared distance from rank-$$r$$
   subspace spanned by the data points available in different
   views. ({% cite sengupta1983generalized %} reports that
    it was {% cite coelho1992generalized %}
    who first gave this "geometric" interpretation.){% fn  %}

3. There are two other closely related motivations that lead to the same solution:

   a. MAXVAR GCCA finds projections of the data that make the
      inter projection correlation matrix as close to a rank 1 matrix
      as possible (This was how {% cite horst1961generalized %}
      derived MAXVAR GCCA )

   b. MAXVAR GCCA finds projections of the data that maximize the
      highest eigen value of the inter projection correlation matrix.
      (This was the Interpretation that
      {% cite kettenring1971canonical %} gave. In his paper he basically
      unified 4-5 different types of GCCA as optimizations of different measures
      of the inter-correlation matrix. This was why he worded
      rephrased Horst's criteria like this)

Now the trouble is that even though the above statements
are simple to read they are woefully imprecise. What is "inter projection
correlation matrix"? What is "total squared distance"? What does it
mean that a matrix is "as close to a rank 1 matrix" as possible?
{% fn %} To really understand how all these criteria can have the same
solution we need precise notation.

{% kramdown_include notationmatrix %}
^
**Let us look at Carroll's original criteria (Motivation 1)**

Imagine that we have $ \ks{J} $ random variables
$ \rv{x}_j \; j \in [1, \ldots, \ks{J}]$ all of which have zero mean.
We want to find a single scalar linear projection
$ \rs{z}_j $ of each data source, i.e.

$$ \exists \uv{u}_j \in \mathbb{R}^{\ks{d}_j}: \rs{z}_j = \rv{x}_j \cdot \uv{u}_j $$

and some "auxilliary" mean-zero random variable $ \rs{g} $ such that $ \rs{g} $ and $ \rs{z_j} $ have as high
total squared correlation as possible. I.e. we maximize \eqref{eq:carroll}:

$$
\begin{align}
  \sum_{j=1}^{\ks{J} } \text{correlation}(\rs{g}, \rs{z}_j)^2 \label{eq:carroll}
\end{align}
$$

<div markdown="1" class="note">
At first sight it is not obvious why \eqref{eq:carroll} is a good objective.
It has some redeeming qualities such as the fact that it is constraining the auxiliary variable
to correlate well with any linear projection of the data.
So there is some flexibility in the model but not too much.
But what if we want to correlate more with one of the data sources ?
One could easily add some multiplicative weights to this criteria to get some more flexibility.
Would that be enough ? Probably not.
We will further analyze criteria \eqref{eq:carroll} later on, for now lets do the optimization.
</div>

Let's say that we have $\ks{n}$ data points. Let's denote the sample space manifestation of
$\rs{g} $ as $\uv{g} $ and of $ \rs{z}_j $ as $ \uv{z}_j $. Note that these are both unknown vectors in the sample space.
Now $ \text{correlation}(\rs{g}, \rs{z}_j)^2 $ can be estimated as follows:

Since we have control over both $\rs{g}$ and $\rs{z}_j$ we could constrain both of them to have unit $l_2$ norm and then
try to solve the optimization problem. The optimization problem would look like

$$ \sum_{j=1}^{\ks{J} } (\frac{\uv{g}^\intercal \uv{z}_j}{\sqrt{ \uv{g}^\intercal \uv{g} } \sqrt{ \uv{z}^\intercal \uv{z} } })^2
$$

{% center_text Or %}

$$ \begin{equation}
 \sum_{j=1}^{\ks{J} } ({\uv{g}^\intercal \uv{z}_j} )^2 \\
 \text{subject to } ||\uv{g}||_2 = 1 \text{ and } ||\uv{z}_j||_2 = 1 \;\; \forall j
 \end{equation}
$$

But this optimization problem is hard and there is a trick to solve this.
Note that we don't really need to constrain both $ \uv{g} $ and $ \uv{z}_j $.
We can instead constrain only $ ||\uv{g}||_2^2 = 1 $ and then maximize
the **squared length of the projection** of $ \uv{g} $
onto $ \uv{z}_j $ which is numerically the same as the cosine similarity
(correlation) between $ \uv{g} $ and $ \uv{z}_j $.
So the optimization criteria becomes

$$ \arg \max_{\uv{g}, \uv{z}_j} \sum_{j=1}^{\ks{J} }\text{projection}(\uv{g}, \uv{z}_j)^2 \text{subject to} ||\uv{g}||_2^2 = 1$$

We further note that for any value of $\uv{g}$ the following relation holds (by the pythagoras theorem)

$$ \max_{\uv{z}_j} \text{projection}(\uv{g}, \uv{z}_j)^2  = || \uv{g} ||^2_2 - \min_{ \uv{z}_j } || \uv{g} - \uv{z}_j ||^2_2 $$

Therefore the optimization criteria translates to:

$$ \arg \min_{\uv{g}, \uv{z}_j} \sum_{j=1}^{\ks{J} } ||\uv{g} - \uv{z}_j||^2_2 \text{subject to} ||\uv{g}||_2^2 = 1$$

Now we only have to generalize to the case where instead of searching for a scalar projection of the data
$\rs{z}_j$ we are instead looking for multiple projections. Clearly we must add constrain the projections in some
way otherwise all of them could end up the same. It turns out that the constraint
$\text{correlation}(\rs{g}_i, \rs{g}_j) = 0 \;\; \forall i, j : j \ne i $
over auxiliary representations $\rs{g}_1, \rs{g}_2, \ldots$  is enough
to ensure that we learn interesting projections. And this leads to the optimization problem \eqref{eq:mvlsa}
from the paper. Q.E.D.

##So how do we optimize criteria \eqref{eq:mvlsa}##


Since \eqref{eq:mvlsa} is a real valued function that is bounded below by $0$ therefore it must have at least one global minima.
Assume that $\um{G}^\* $ is the value of $\um{G} $ at one such minima.
Now each member of $ || \um{G} - \um{X}_j \um{U}_j ||_F^2 $ of the objective
is a linear regression with $ \um{U}_j $ as the unknown. So the solution
for $\um{U}_j$ is $(\um{X}_j^{\intercal} \um{X}_j)^{-1}\um{X}_j^{\intercal}\um{G}$.
Let $\um{P}_j = \um{X}_j(\um{X}_j^{\intercal} \um{X}_j)^{-1}\um{X}_j^{\intercal}$ and
note that $||\um{M}||^2_F = \text{trace}(\um{M}^\intercal \um{M})$.
So our objective translates to:

$$ \begin{equation}
\arg \min_{\um{G} } \sum_{j=1}^{\ks{J} } \text{trace}( (\um{G} - \um{P}_j\um{G})^\intercal (\um{G} - \um{P}_j\um{G}) ) \text{ subject to } \um{G}^\intercal \um{G} = I \\
= \um{G}^\intercal \left( \sum_{j=1}^{\ks{J} } ({I} - \um{P}_j)^\intercal ({I} - \um{P}_j) \right) \um{G} \text{ subject to } \um{G}^\intercal \um{G} = {I}
\end{equation}
$$

Now [we know that this is an eigenvector problem]({{ site.baseurl }}{% post_url 2015-06-15-eigenvalue-problems %}) and its solutions are
the eigen vectors of $ \sum_{j=1}^{\ks{J} } ({I} - \um{P}_j)^\intercal ({I} - \um{P}_j) $.
Consider

$$
\begin{align*}
\um{M} &= \sum_{j=1}^{\ks{J} } ({I} - P_j)^\intercal ({I} - P_j) \\
&= \sum_{j=1}^{\ks{J} } ({I} - P_j^\intercal - P_j + P_j^\intercal P_j) \\
&= \sum_{j=1}^{\ks{J} } ({I} - P_j) \text{If }P_j \text{ is symmetric and idempotent } \\
&= \ks{J}{I}  - \sum_{j=1}^{\ks{J} } (P_j)
\end{align*}
$$

Also note that the eigen vectors of ${I} - \km{M}$ are the same as the eigen vectors of $ M $.
Therefore the optimal $G$ can be found by computing the eigen vectors of $\sum_{j=1}{\ks{J} } P_j$.


<div markdown="1" class="note">
Corner Cases: The attentive reader would notice that there are corner cases that we did not address, like what happens if
$(\um{X}_j^{\intercal} \um{X}_j)^{-1}$ is not defined. While it is possible to cover these corner cases, we took the simpler root
and defined $P_j$ through $(\um{X}_j^{\intercal} \um{X}_j) + r I$. That ensures that all the assumptions about existence, symmetry
and idempotency of the projection matrix hold true.
</div>

##What about criteria 3a and 3b##

When I started writing this post, I did not realize that writing proofs is so hard.
Now I can appreciate why people take short cuts and leave exercises.
But any way let's press on.

Let's first establish that 3a is the same as 3b. Actually I think I can leave that as an exercise since this is just the
[Eckart-Young]https://en.wikipedia.org/wiki/Singular_value_decomposition#Applications_of_the_SVD) theorem restated.
And 3b has been derived quite clearly in {% cite kettenring1971canonical %} so I won't repeat him.

##So what's left to do ?##

Here's what I think my next steps should be:
1. {% cite kakade2007multi %} and {% cite sridharan2008information %} did information-theoretic/CoLT-type analysis of Multi-view learning and CCA. What is not clear to me and what would be nice to have are measurable condition about what constitutes a separate view ? After all we could just concatenate the matrices into a single view and then do LSA or Glove or Whatever ? When would hunting for correlation be better than hunting for variance ?

2. In our paper we never compared GCCA to basic LSA !! I think that was an oversight and that experiment must be run. Also I can probably feed all my co-occurrence matrices to Glove and run it. What would it learn ?

3. I talked about how Venvelden and Takane had collaborated and come up with better regularization methods. But I never applied them to our task ? Also I showed how we could approximate Glove by a special regularization scheme. Both of these experiments should be run and applied to the task.

4. Probabilistic GCCA. This has been on my plate for a while, and I think I'd try to blog the solution but the gist is that Tipping, Bishop and Sam Roweis did a factor analysis of PCA, Francis Bach and Michael Jordan gave probabilistic CCA. It should be pretty straight forward to do probabilistic GCCA. The key point is not whether its possible, it almost certainly is, but that once I do how would I use it ? What good is probabilistic GCCA once you know the formulas ?

5. Task specific GCCA. Till date all my experiments have been unsupervised but like I remarked earlier it is possible to add parameters to the model that can be tuned discrimatively.

## Footnotes ##
{:.no_toc}
{% footnotes %}
   {% fnbody %}
    This is like the
   statistical-geometric interpretations of PCA.
   {% endfnbody %}
   {% fnbody %}
   But the problem is also that if we give the rigorous definitions
   without a summary of what those definitions and derivations should
   be interpreted as, then it becomes hard to maintain interest. So
   it's a chicken and egg problem.
   {% endfnbody %}
{% endfootnotes %}

## Bibliography ##
{:.no_toc}
{% bibliography --cited %}
