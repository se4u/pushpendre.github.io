---
title:  "Eigenvalue Problems"
layout: post
date:   2015-06-15 07:14:00
---
There are some structures/forms that tend to surface while solving
problems whose solutions are given in the form of eigen vectors
and eigen values. Knowing some of those forms can help while trying to
solve a larger problem because then you can pattern match the form to the
solution. Here's one pattern whose solution is given in the form of eigen vectors/values.


## Maximizing a Quadratic Form ##
Let $ \um{M} $ be a symmetric matrix with real elements.
The eigenvector of $ (M + M^\intercal)/2 $ that has the highest eigen value
maximizes the following objective:

$$ \arg \max_{ \uv{x} } \frac{\uv{x}^\intercal \um{M} \uv{x}}{||\uv{x}||^2}
$$

{% center_text Or %}

$$ \arg \max_{ \uv{x} } \uv{x}^\intercal \um{M} \uv{x} \text{ subject to } ||\uv{x}|| = 1
$$
