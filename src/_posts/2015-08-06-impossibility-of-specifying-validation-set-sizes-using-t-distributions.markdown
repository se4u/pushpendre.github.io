---
title:  "The impossibility of specifying the number of samples needed in a validation set using t-distributions for regression with unbounded loss"
layout: post
date:   2015-08-06 19:58:53
---
Imagine that we have collected some data for a regression task.
Let's say that the regression task is predicting the weight of an item
and the most natural loss  function is the absolute difference between
the predicted value and the truth.

{% highlight python %}
loss = lambda y_hat, y: abs(y_hat - y)
{% endhighlight %}

Now the question is, how many samples should we ideally set
aside for our test data so that the probability that the (sample test error of the
hypothesis we tested is within $\epsilon$ factor with respect to the
true expected error of our hypothesis (When the expectation is taken
with respect to the same distribution that was used while creating the
test data) ) is greater than $\delta$.

Let $m$ be the sample size; Sample Error, Expected Error and Sample Standard Deviation (STD) have the intuitive meaning then our question can be stated as:

$$
\begin{equation}
m = \arg_m \min P(|\text{Sample Error } - \text{ Expected Error}| < \epsilon * \text{ Expected Error}) > \delta
\end{equation}
$$

Now let $R_1 = \text{Sample Error } - \text{ Expected Error}$
and let $R_2 = \frac{R_1}{\frac{\text{Sample STD}}{\sqrt{m}}}$.

We claim that the "theory of t-tests" says that
$R_2$ has the standard t-distribution with $m  - 1$ degrees of freedom.

<div markdown="1" class="warning">
TODO: Pause, make sure that the claim is correct.
</div>

Now the event $|R_1| < x$ is corresponds to the event $|R_2| < \frac{x}{\frac{\text{Sample STD}}{\sqrt{m}}}$.
Let $E$ be the event that a standard t-distributed random variable
with $m - 1$ degrees of freedom is bounded between
$\frac{\epsilon * \text{ Expected Error}}{\frac{\text{Sample STD}}{\sqrt{m}}}$.
By substituting $x = \epsilon * \text{ Expected Error}$ we can restate the optimization problem as:

$$
\begin{equation}
m = \arg_m \min P(E) > \delta
\end{equation}
$$

<div markdown="1" class="warning">
Beyond this point I am writing about my failed attempt to come up with
a good way to set a value of $m$ apriori.
</div>

Using binary search one can easily search for the smallest sample size
that would satisfy this constraint but the problem is to find
a reasonable way to set the expectations for
$\frac{\text{Expected Error}}{\text{Sample STD}}$ or
even $\frac{\text{Expected Error}\sqrt{m}}{\text{Sample STD}}$.
It is almost impossible to know apriori what these quantities would be
or should be. If let's say we were to set
$\frac{\text{Expected Error}\sqrt{m}}{\text{Sample STD}} = 1$
and let $\epsilon = 0.05$ and set $\delta = 0.95$, then no value of $m$
could do the job. If however we let
$\frac{\text{Expected Error}\sqrt{m}}{\text{Sample STD}} = 40$ with
$\delta=0.95$ then $m=70$ would be enough which in turn would mean
that $\frac{\text{Expected Error}}{\text{Sample STD}} = 4.78$. But
this is impossible to verify or guarantee beforehand.
