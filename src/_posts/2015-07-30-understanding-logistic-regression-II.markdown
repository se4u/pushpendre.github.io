---
title:  "Understanding Logistic Regression II"
layout: post
date:   2015-07-30 17:11:49
---
<div markdown="1" class="note">
Version 0.8
</div>


Consider a hyperplane $h$ that is used separate the domain $X$ into two categories (say {Good, Bad} or {1, 0} or {1, -1}) that we can collectively call to be the set $Y$. In other words, there is a true function $y = \text{sign}(h(x))$ that perfectly divides the data into the two categories of interest.

<div markdown="1" class="note">
Another way of saying this is that learning the best hypothesis from the set of linear hyperplanes is a realizable learning problem. Actually, consider the above the definition of realizable learning.
</div>

Starting again, Consider a hyperplane $h$ that can map $x$ to $y$ as $y = \text{sign}(h(x))$ where $h(x) = \langle \theta, x \rangle$, where $\theta$ is the normal vector to the hyperplane.

<div markdown="1" class="note">
We are only considering hyperplanes that pass through the origin here
and not really addressing the general version with non-zero
intercepts.
</div>

Note, that there is no probability distribution; Data is not generated
stochastically. It isn't the case that based on the value of $x$, or
location of $x$ if we think of $x$ as designating a location in a
vector space, $y$ is emitted stochastically. However, even this
situation can be modeled stochastically, simply assume that $y$ is
emitted stochastically, but the probability distribution over the
possible values of $y$ is non-zero only at a single value given $x$.

Now logistic regression is a particular relaxation of the original
problem. Instead of assuming that the probability distribution of $y$
given $x$ is non-zero for only value of $y$ we instead assume a
parametric form of the distribution, the logistic function, which can
approach the true low-entropy if we increase the magnitude of the
value of $\theta$ used in the parameterization. This distribution is
dependent basically on the signed distance of a point from the
hyperplane defined by $\theta$.
The logistic assumption says that
$ p(y = 1 | x) = \frac{1}{1 + \exp(-h(x))} $.

<div markdown="1" class="note">
Since $h(x) = \langle \theta, x \rangle$ therefore $p(y = 1 | -x) = \frac{1}{1 + \exp(+h(x))} = 1 - p(y = 1 | x) = p(y = -1 | x)$
</div>


{% pysvg %}
import pygal
import numpy
chart = pygal.Line(x_label_rotation=60, tooltip_border_radius=10,
                   y_title='P(y = 1 | h(x))', x_title='h(x)')
chart.title = 'Quantified belief that the event y=1 becomes more likely as we proceed farther to the right of the hyperplane'
h = list(numpy.linspace(-10, 10, 50))
sigmoid = lambda h, a: 1.0 / (1.0 + numpy.exp(- a * h))
chart.x_labels = ['%.2f' % e for e in h]
chart.add('1/(1 + e^(-h(x)))', [sigmoid(e, 1) for e in h])
chart.add('1/(1 + e^(-10*h(x)))', [sigmoid(e, 10) for e in h])
print(chart.render_data_uri())
{% endpysvg %}

Here's a different take on this, imagine we have a large number of different features $x_1, x_2, x_k$ on which $y$ is dependent. and we make the above assumption for each of these features. i.e. we say that

$$p(y = 1 | x_1 ) = \frac{1}{1 + \exp(-x_1)}$$

$$p(y = 1 | x_2 ) = \frac{1}{1 + \exp(-x_2)}$$

$$p(y = 1 | x_k ) = \frac{1}{1 + \exp(-x_k)}$$

An improvement can be made to this assumption by incorporating the fact that certain features can have more influence than others in changing our beliefs. For example a single occurrence of the bi-gram "fantastic_movie" might be as potent as two occurrence of the bigram "good_acting" in a movie review for making us believe that a movie was truly "GOOD". In general we can add many scalar multipliers, 1 for each feature

$$p(y = 1 | x_1 ) = \frac{1}{1 + t_1 \exp(-x_1)}$$

$$p(y = 1 | x_2 ) = \frac{1}{1 + t_2 \exp(-x_2)}$$

$$p(y = 1 | x_k ) = \frac{1}{1 + t_k \exp(-x_k)}$$

Now think of each distribution as an expert, and you want to
incorporate the beliefs of all the experts into your final
distribution $ p(y = 1 | x_1, x_2, \ldots, x_k) $. The two standard ways to
make a single distribution from a collecion of distributions is to
either take their product "The Product of Experts" model or to make a
mixture.

Consider what it would mean to take a product of the individual probability distributions:

$$ p(y = 1 | x_1, x_2, \ldots x_k) = \frac{1}{1 + t_k \exp(-x_1)} \frac{1}{1 + t_k \exp(-x_2)} \ldots \frac{1}{1 + t_k \exp(-x_k)}$$

Now essentially what we are saying is that each expert has a veto power, imagine how many terms there would be if a full expansion of the above product was carried out. The exact formula is $2^k$. Now logistic regression could be phrased as an approximation of this where we have kept only two terms so that

$$p(y = 1| x_1, x_2, \ldots, x_k) = \frac{1}{1 + \exp( - \sum_{i=1}^k t_i x_i )}$$

Actually the above way is not really a satisfying way to understand
logistic regression and there there is a third and a better way to
understand this that was proposed by Jaynes. Essentially the maxent
principle finds the probability distribution that has the highest
entropy after assuming that certain statistics derived from the data
are good anough to be enforced as constraints for the predictive
probability distribution.

<div markdown="1" class="note">
Search for the entry "Why no maxent?" at
[David Mackay's FAQ site](http://beta.metafaq.com/faq/mackay/book) to
also get an understanding of why Maxent may not be a great idea.
</div>


Okay finally consider 4 scenarios

1. Data was completely linearly separable and generated by a
   distribution. Actually the probability of this event happening as
   the number of data points increase is lower. But even so with
   finite data such a situation can happen. The problem that can
   happen if we try to maximize the conditional log likelihod is that
   by increasing the magnitude of $\theta$ it is possible to keep
   making the log-likelihod higher and higher. After all when we
   increase the magnitude of $\theta$ the system keeps becoming more
   and more sure of itself and it never has to pay a penalty because
   well the data is linearly separable. Of course regularization is
   one way to solving this problem which can be interpreted as
   imposing a prior if one sticks to generative/statistical learning
   and do not use "learning theory" and its "regularized learning
   framework". Of course if the data truly is linearly separable then
   even a simple perceptron such as the one below would do the job.

2. Data was linearly seperable and generated by a deterministic
   function. In this case instead of using loglikelihood based methods
   one can even use percetrons. They are easy to code and simple to execute.
   However, even percetrons can overfit and for such cases we have
   the margins in hinge loss minimization and slack and $C$ parameter in
   the dual problem solved in SVMs.
   {% highlight python linenos %}
import numpy as np
class BatchPerceptron(object):

    def __init__(self, dim=2):
        self.hyperplane = np.zeros((dim,), dtype='float32'))

    def _distance(self, x):
        return np.dot(self.hyperplane, x)

    def predict(self, x):
        y_hat = np.sign(self._distance(x))
        return 1 if y_hat == 0 else y_hat

    def prediction_is_incorrect(self, y, x):
        return self.predict(x) != y

    def update(self, data):
        for (y, x) in data:
            if self.prediction_is_incorrect(y, x):
                self.hyperplane += (y * x)
                return True
        return False

bp = BatchPerceptron()
while bp.update(data):
    pass
print(bp.hyperplane)
   {% endhighlight %}
   ![]({{site.baseurl}}/res/perceptron_odyssey_25.gif)
   {% center_text Perceptron Odyssey %}

3. Data not linearly seperable, generated by linear
   threshold. Impossible! Of course the ideas of slack and margin
   allow us to solve even this problem.

4. Data not linearly separable, generated stochastically. Even in such
   cases regularization may be needed. But this problem at least is
   guaranteed to have a solution because it is a convex minimization
   problem in which the minima actually exists.

<div markdown="1" class="note">
Always remember that even the function $f(x) = x$ is a convex function
but it's doesn't actually have a minima over the real line.
</div>
