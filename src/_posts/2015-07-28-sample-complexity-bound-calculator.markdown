---
title:  "Online Sample Complexity Bound Calculator"
layout: post
date:   2015-07-28 13:05:37
---
Learning theory provides probabilitic guarantees on the deviation between training error of a certain size and true errors. I don't think people actually use these bounds literally, rather these bounds are used to get some sense of trends. For example, the wisdom that the number of samples needed for learning grows linearly with the number of parameters in the model which can be justfied because the sample complexity of ERM increases linearly with the VC dimension {% cite ng2002discriminative %} {% cite shalev2014understanding %}

$$
m(\delta , \epsilon) = \Theta(\frac{d + \log(\frac{1}{\delta})}{\epsilon^2})
$$

This formula comes with a large number of conditions. This is for 0-1 loss on a binary classification problem for the ERM algorithm in the agnostic setting. In this post I have put up an online script that calculates the sample complexities for some hypothesis spaces. Most useful case perhaps is the setting when "is_validation" is set to 1. This case can basically help us design the number of samples to keep in our dataset for good generalization to the test data. Of course if the test data has a different distribution then these bounds won't be useful.

####Bibliography####
{% bibliography --cited %}

<iframe src="https://trinket.io/embed/python/1719908ef5" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen> </iframe>
