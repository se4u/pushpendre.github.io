---
title:  "Glossary/Cheat-Sheet of Some Statistical Terms"
layout: post
date:   2015-06-19 13:31:24
comments: true
---

#Preface#
Hierarchical bayesian models have made statistical
modeling easy. In fact the way statistical modeling is taught
in a good machine learning course is so general that it subsumes a
lot of the old terminology / old methods. In other words once a person
understands a bayesnet they also understand the concept behind general
linear models. And exponential families and log linear models in
particular cover all of logit/probit etc.
In this article I will try to translate some of the old statistics
acronyms to more modern terminology.

<div markdown="1" class="note">
Personally I tend to think of
technical terms as instances of variants,
for example the Baum-Welch algorithm is
(Model: Order-1 Chain HMM, Objective: Joint LogLikelihood,
Optimization: Expectation Maximization, Data: Unlabeled)
Of course, this description is not "complete". It is a lossy summary
based on my belief about what are the references that I would need to
reconstruct (or "triangulate" in
[Feynman's terminology](http://fed.wiki.org/journal.hapgood.net/concept-triangulation/alex.au.fedwikihappening.net/concept-triangulation))
the concept of Baum-Welch. I want to write down a description like
this for annoying acronyms like Probit/Logit/ANOVA/MANOVA/GLM/OLS
that sometimes people/papers assume that I would know.
</div>

* TOC
{:toc}

{% kramdown_include notationmatrix %}
^
##Simple Linear Regression(SLR/LR)##

In simple linear regression, $y, x$ are both scalars.

###Ordinary Least Squares(OLS)###

OLS is akin to doing MLE on the following model to find $a, b$
after assuming that $\sigma$ is known to us.

$$ y \sim \mathcal{N}(ax + b, \sigma^2) \\
   \equiv y = ax + b + \mathcal{N}(0, \sigma^2)
$$

The important characteristics of the model are that we don't assume there is any other error in the observations of $x$.
{% fn %}
There are no other additive/multiplicative noises.
Assumptions like linearity, constant variance (aka  homoscedasticity) are also evident.

<div markdown="1" class="proof">
Under the model specified above the log-likelihood of $\ks{N}$ data points $(x_i, y_i)$ is:

$$\sum_{i=1}^{\ks{N} } \log(p(y_i | x_i)) = \sum_{i=1}^{\ks{N} } \frac{(y_i - (a x_i + b))^2}{2\sigma^2} - \log(\frac{1}{\sqrt{2\pi \sigma^2}})$$

Remove all the constants and known values from the optimization problem and the OLS emerges.
</div>

####Gauss-Markov Theorem####

The Gauss-Markov theorem states that out of all possible "Linear" and "Unbiased" estimators of the value of $a, b$
,with all accompanying model assumptions as well like known constant variance and uncorrelated mean zero errors,
the OLS estimator has the least variance. Note that the Gauss-Markov theorem does not assume that the error is gaussian
distributed which means that the model I wrote above with the normal distribution is actually making more assumptions than
the linear regression model. And the generalized regression models can be considered to be a collection of guiding principles
that state what to do when you observe a certain type of input/output.

###Total Least Squares(TLS)(Deming Regression)###

It is the MLE of an errors-in-variables model in which the errors for
the two variables are assumed to be independent and normally distributed,
and the ratio of their variances, denoted $\delta$ is known.

Note that these ideas can always be ramped upto multivariate inputs and outputs.

###Generalized Least Squares###
This is done when the samples are correlated a little. Again, I would consider, this type of estimation method
outdated since we already have graphical models for sequences and trees which are highly correlated.

##Multiple linear regression(MLR)##

A MLR is just linear regression with vector valued input and single scalar output.

##General Linear Model(GLM)##

A GLM is just linear regression with vector valued input and vector values output.


#RAW MATERIAL#
https://en.wikipedia.org/wiki/Generalized_linear_model
https://en.wikipedia.org/wiki/Variance-stabilizing_transformation
Bayesian versions of the
F-test https://en.wikipedia.org/wiki/F-test
t-test https://en.wikipedia.org/wiki/Student%27s_t-test
Paper 0: A comparison using 855 published t-tests, Empirical Comparison , Wtzels et. al.

http://doingbayesiandataanalysis.blogspot.com/2012/03/bayesian-estimation-supersedes-t-test.html
In 252 articles, spanning 2394 pages, "we" found 855 t-tests.
This translates to an average of one t-test for every 2.8 pages, or about 3.4 t-tests per article.
http://www.ruudwetzels.com/proefschrift/proefschrift_ruud_wetzels.pdf
It was wetzels thesis : Statistical Evidence in Experimental Psychology: An Empirical Comparison Using 855 t Tests

Paper 1: Bayesian estimation supersedes the t test, John K. Kruschke, Journal of Experimental Psychology: General, 2013, v.142(2), pp.573-603. (doi: 10.1037/a0029146)
Bayesian estimation for two groups provides complete distributions of credible values for the effect size, group means and their difference, standard deviations and their difference, and the normality of the data. The method handles outliers. The decision rule can accept the null value (unlike traditional t tests) when certainty in the estimate is high (unlike Bayesian model comparison using Bayes factors). The method also yields precise estimates of statistical power for various research goals.

##Generalized Linear Model(GLM)##
Generalized linear models (GLMs) are a framework for modeling a response variable y that is bounded or discrete. This is used, for example:
when modeling positive quantities (e.g. prices or populations) that vary over a large scale—which are better described using a skewed distribution such as the log-normal distribution or Poisson distribution (although GLMs are not used for log-normal data, instead the response variable is simply transformed using the logarithm function);
when modeling categorical data, such as the choice of a given candidate in an election (which is better described using a Bernoulli distribution/binomial distribution for binary choices, or a categorical distribution/multinomial distribution for multi-way choices), where there are a fixed number of choices that cannot be meaningfully ordered;
when modeling ordinal data, e.g. ratings on a scale from 0 to 5, where the different outcomes can be ordered but where the quantity itself may not have any absolute meaning (e.g. a rating of 4 may not be "twice as good" in any objective sense as a rating of 2, but simply indicates that it is better than 2 or 3 but not as good as 5).
Generalized linear models allow for an arbitrary link function g that relates the mean of the response variable to the predictors, i.e. E(y) = g(β′x). The link function is often related to the distribution of the response, and in particular it typically has the effect of transforming between the (-\infty,\infty) range of the linear predictor and the range of the response variable.
Some common examples of GLMs are:
Poisson regression for count data.
Logistic regression and probit regression for binary data.
Multinomial logistic regression and multinomial probit regression for categorical data.
Ordered probit regression for ordinal data.
Single index models[clarification needed] allow some degree of nonlinearity in the relationship between x and y, while preserving the central role of the linear predictor β′x as in the classical linear regression model. Under certain conditions, simply applying OLS to data from a single-index model will consistently estimate β up to a proportionality constant

(Some known physical reasons for modeling it as such)

Multivariate analysis of variance or multiple analysis of variance (MANOVA) is a statistical test procedure for comparing multivariate (population) means of several groups. As a multivariate procedure, it is used when there are two or more dependent variables,[1] and is typically followed by significance tests involving individual dependent variables separately. It helps to answer [2]
Do changes in the independent variable(s) have significant effects on the dependent variables?
What are the relationships between the dependent variables?
What are the relationships between the independent variables?

Ordinal Regression
https://en.wikipedia.org/wiki/Ordered_logit
http://stats.stackexchange.com/questions/2619/continuous-and-categorical-variable-data-analysis
http://stats.stackexchange.com/questions/539/does-it-ever-make-sense-to-treat-categorical-data-as-continuous
https://en.wikipedia.org/wiki/Item_response_theory

http://web.engr.oregonstate.edu/~tgd/classes/534/slides/part11.pdf
Reconstituted Early Stopping
1-fold crossval , holdout validation

Holdout methods are the best way to Holdout methods are the best way to
choose a choose a classifier classifier
– Reduce error pruning for trees Reduce error pruning for trees
– Early stopping for neural networks Early stopping for neural networks
Cross-validation methods are the best way validation methods are the best way
to set a to set a regularization parameter regularization parameter
– Cost-complexity pruning parameter complexity pruning parameter α
– Neural network weight decay setting Neural network weight decay setting
– Number k of nearest neighbors in of nearest neighbors in k-NN
– C and σ for SVMs for SVMs


A number of statistical models are used in fields like bio-statistics,
agriculture, chemometrics etc. This page lists some of the most common
ones. This page mostly serves as an aid to translate what a paper
might be referring to when it uses one of these terms.

For example:
There are a number of terms like
Ordinary Least Squares : OLS

Generalized Linear Model : GLM (confusing)
OVERALS :
Multiple Linear Regression :
Factor Analysis :

A typical machine learning course might just start with
bayes nets and bayes theorem. It is not the student's fault at all
that s/he does not know what ANOVA/MANOVA/OLS/GLM etc. stand for.
After all a modern CS curriculum is not a study of history.
However a number of old papers, papers from other fields, are still
written using old terminology. More importantly, there are important
intuitions and theorems that a CS/EE curriculum misses out on that
probably should be  incorporated in the design of statistical models.


In the beginning there was linear regression single variable



Imagine we have data as follows

## Footnotes ##
{:.no_toc}
{% footnotes %}
{% fnbody %}
 Wikipedia calls it "Weak Exogeneity".
{% endfnbody %}
{% endfootnotes %}
