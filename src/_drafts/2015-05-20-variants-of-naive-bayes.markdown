---
title:  "Variants Of Naive Bayes and Choosing a model"
layout: post
date:   2015-07-20 12:44:19
---
A single empirical paper, for example a paper that describes
experiments/models built to solve a shared task is only good as a
lower limit for the possible performance of a machine learning
method. That is why building machine learning systems is part science
and part art. It is a science because results are reproducible and if
one person claims to get 80% accuracy on a task using a particular
method then those results could be used in the future as a baseline(a
lower limit) on performance. And it is an art because one needs
intuition and considerable dilligence to reach the upper limit.

Some people/researchers are better at reaching that upper limit than
others and this was demonstrated beautifully in the short paper
"Baselines and Bigrams: Simple, Good Sentiment and Topic
Classification" published by Sida Wang and Christopher Manning in
ACL 2012.

The thesis of that paper was to show that careful use of naive bayes
classifiers and SVMs with the right features could
out-perform many other state of the art methods.
Through this article I would explain how their methods were derived and possible
variants.

###Setup###

The setup of the paper is that we are given strings of text and have
to assign one of two {Positive, Negative} sentiments to them.
The strings of text are converted to feature vectors denoted as
$\kv{x}$ and the labels to predict are $y$.
Let $\kv{x}_i$ be the $\ks{i}$-th component of $\kv{x}$ and let $\kv{x}^k$ be
the $\ks{k}$-th member of a sequence of $\kv{x}$. These notations can
be mixed to get $\kv{x}_i^k$, the $\ks{i}$-th component of the
$\ks{k}$-th "example" in a given dataset.

###Multinomial Naive Bayes###

The Naive Bayes model is a statistical model that assumes that the
observed data was generated from distributions that are conditionally
independent given the output label that we have to predict.

Note that the Naive Bayes model does not proscribe non-linear
classifiers nor does it advocate for a specific type of
distribution. It even does not advocate for a decision rule or an
objective. The knowledge
that these decisions can all be made differently, and how
computationally efficient different combinations of decisions are that
some decisions are going to mimic the true data more closely than
others is basically what data science is all about.

In some sense a statistical data model can be described as a 7-8 tuple of
(Feature function, loss function, ...)
but the trouble is that there are special combinations that are more
useful than others.

In fact even within the assumption that the observed data was
generated from condtionally independent distributions there is room
for interpretation. The standard assumption is that each word in the
string was generated independent of the other and that each word is
generated from a categorical distribution. In fact this assumption is what
gives rise to the multinomial distribution, but what if we say that
each word type was generate independent of the other, and that the
number of occurrences of each word type follows a poisson
distribution? That would lead to a different model.

Having said that let us derive the multinomial bayes model used in the
"Baseline and Bigrams" paper.

We would have to make the following decisions:

1. Objective Function :

2. Decision Rule :

3. Parametrization :

Thankfully, standard bayesian decision theory took care of most of
these decisions for us. And we can be safe in the knowledge that there
are theorems that show that if we take these decisions then we would
not go wrong. For example the theorem that shows that the bayes
decision rule is optimal, one could even argue that it is this theorem
which makes it lucrative to model the distribution of the data in the
first place. Also there are decisions like which distribution should
we parameterize for example we could parameterize the probability of
the hidden variable given the current input and the previous hidden
variable or we could parameterize the hidden variable given the
previous hidden variable and the whole input.
we could say that the log probability of each class is a linear
function of the input plus a normalization constant. And generative
just means that something is based on the joint distribution and
discriminative means it is modeling the conditional distribution.

The difference between MEMM and CRF is just local normalization versus
global normalization. In MEMM you have to locally normalize at every
step but in CRF you normalize globally.

In any case let us begin deriving the multinomial naive bayes
classifier.

$$
\begin{align}
& \text{The posterior probability equals likelihood times prior}\\
p(y^k | x^k) &\propto p(x^k | y^k) p(y^k)\\
p(x^k | y^k) &= \int_\theta p(x^k | y^k, \theta) p(\theta | y^k) \\
p(y^k)       &= \int_p p(y^k | p) p(p | y^k) \\
& \text{The likelihood given its parameters is multinomial distributed}\\
p(x^k | y^k, \theta) &\propto (\prod_i (\theta_{i,0}^k)^f_i^k)^{\mathbb{1}(y_k = 0)}  (\prod_i (\theta_{i,1}^k)^f_i^k)^{\mathbb{1}(y_k = 1)}\\
& \text{The conjugate distribution of hyperparameters of multinomial are dirichlet distributed}\\
p(\theta | y=1) &\propto \prod_i (\theta_{i,1})^\alpha\\
p(\theta | y=0) &\propto \prod_i (\theta_{i,0})^\alpha\\
& \text{Through some algebra, the likelihood } p(x^k | y^k) {can be calculated to be a DirichletMultinomial} \\

& \text{The prior given hyperparameter is bernoulli distributed}\\
p(y^k | p) &= p^{\mathbb{1}(y_k = 1)} (1-p)^{\mathbb{1}(y_k = 0)} \\
& \text{The conjugate distribution for the hyperparameter is beta distributed}\\
p(p, \beta) &\propto p^\beta (1-p)^\beta\\
& \text{Through some algebra, the likelihood } p(y^k) {can be calculated to be a BetaBernoulli} \\

& \text{We know that the bayes optimal classifier written below is
always better than other classifiers. The Bayes decision rule is:} \\
\text{Predict }\hat{y}  &= 1 \text{if} p(1 | x) > p(0 | x) \text{else} 0\\
& \text{So the decision rule becomes}\\
& 1 \text{if} \log(p(1 | x)) - \log(p(0 | x)) > 0 \text{else} 0\\
& \text{We already calculated } p(y^k | x^k) \\
\log(p(y | x)) &= \log(p(x | y)) + \log(p(y)) \\
\log(p(x | y)) &= \\
\log(p(y)) &=
\end{align}
$$

There are two alternate ways to think about bayesian prediction.

One ways is to think that we are using the data to estimate $p(y | x)$
as best as we can
so that we can then use it to create the bayes optimal classifier. We
know through some theorems that the bayes optimal classifier is always
better than other classifiers. And we know that the bayes optimal
classifier for binary prediction is to predict
$1 \text{if} p(1 | x) > p(0 | x) \text{else} 0$. Let's call our
estimate of the posterior probability distribution
$\hat{p}_D(y | x)$. Basically we want $\hat{p}_D(y | x)$ to be as
close to $p(y | x)$ as possible for those $x$ whose probability is
high. And actually we only need the decisions to be as close to the
decisions that the true probability distributions would
make. I.e. even if the probability distributions are not exactly
correct as long as the decisions made are correct we don't care about
other things.

In any case, one approach to learning is to compute $\hat{p}_D(y | x)$
so that it is as close to $p(y | x)$ as possible. And one way to do
this is to assume a parametric form for $p(y | x)$ or $p(y, x)$ and then to choose amongst
distributions with that parameteric form by finding parameters that make the probability of
the supervised training corpus as high as possible.

Note however that we are directly deriving our motivation
from the bayes optimal prediction rule. And according to the bayes optimal prediction
rule directly maximizing $p(y | x)$ for a corpus of $(x, y)$ tuples
makes more sense than maximizing $p(x | y)$ or even $p(y, x)$. Of course if there was
no class imbalance then maximizing $p(x | y)$ would result in the same
prediction rule or if we really knew that the data was really
generated from class based multinomial distributions then the MLE rule
of maximizing $p(x, y)$ would make sense. In fact that is basically
the generative/discriminative divide.

Now the discriminative method or the maximum entropy method has a
combinatoric motivaiton that was first promulgated by E.T. Jaynes and
according to Jaynes's principle if we have certain constraints that we
want to enforce on a probability distribution in a certain domain then
the form of the probability distribution should be one that maximizes
the entropy subject to the constraints. For example a discrete
distribution over two outcomes whose mean is known is best modelled as
a bernoulli and a discrete distribution whose


A Maximum Entropy Approach to Natural Language Processing by Berger,
Pietra, Pietra explains it perfectly.
you want to come up with a distribution p(y | x) such that
$$p(f) = p'(f)$$
where $p(f) = \sum_{x, y} p'(x) p(y | x) f(x, y)$
and $p'(f) = \sum_{x, y} p'(x, y) f(x, y)$
Now you can either derive the exact updates either as the gradients of
the loglikelihood of a joint distribution of p(x, y) or as a dual
function that is optimizing the entropy.

It is a happy coincidence that conditional maximum likelihood also
gives the same answer as maximum entropy methods but they are
different derivations altogether. but note that conditional maximum
likelihood does not tell us the form of the conditional distribution
at all so in a sense it is an impoverished rule compared to the
maximum entropy rule. There are a few papers that talk about
conditional maximum likelihood rule like
"A Decision Theoretic Formulation of a Training
Problem in Speech Recognition and a
Comparison of Training by Unconditional
Versus Conditional Maximum Likelihood "

Asymptotic Properties of Conditional Maximum-likelihood Estimators
The abstract says that
" In this paper a maximum-likelihood method
based on the conditional distribution given minimal sufficient statistics for
the incidental parameters isuggested. It is proved that conditional maximumlikelihood
estimates in the regular case are consistent and asymptotically
normally distributed with a simple asymptotic variance"

Discriminative Max-Ent modelling would basically say that we should
assume that




But note that we could have chosen completely different likelihood
functions in this place
###Risk based loss###
