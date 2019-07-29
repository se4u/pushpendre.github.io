---
title:  "Convex Neural Networks?"
layout: post
date:   2015-07-28 17:13:30
---
The trigger for this post was basically just this wish that wouldn't it have been nice if the neural network parameter optimization problem was itself convex? Although large scale convex optimization is not a "solved" problem and a lot of research is going on in this area {% cite yuan2010comparison %} but at least it is reasonable to hope that a "convex neural network optimization problem" could lead to improvements. Now I have come across the following two papers that deal with "Convex neural networks".

1. Breaking the Curse of Dimensionality with Convex Neural Networks. {% cite bach2014breaking %}

2. Convex Neural Networks. {% cite bengio2005convex %}

Both of these papers are on my reading list, but the techniques that they use are at least a few months beyond me if not more. Instead of discussing these papers, I want to present a way for possible "convexifying" the optimization objectives with respect to a neural network's parameters.

Consider a neural network with $\text{relu}$ activation units, where $\text{relu}(x) \triangleq max(0, x)$. Let $y_i$ be the activation(intermediate output) after the $i$th layer in a feed-forward neural network.

$$
 \begin{align*}
 y_1 &= \text{relu}(W_1 x) \\
 y_i &= \text{relu}(W_i y_{i-1})
 \end{align*}
$$

Now notice that:

1. $\text{relu}$ is a convex function.
   <details><summary>Proof</summary>
    TO ADD
   </details>

2. If $f$ is a convex function over scalars then $f(\kv{a}\uv{x})$ is also convex wrt to $\uv{x}$ as long as $\kv{a} \ge 0$. The notation $\kv{v} \ge 0$ means that every element of the vector $\kv{v}$ is greater than or equal to 0.
   <details><summary>Proof</summary>
    TO ADD
   </details>

3. If two differentiable functions $f$ and $g$ are convex then their composition $f g$ (I am using Haskell/Ocaml syntax for function composition) is convex if $f' (g x) > 0$ for all $x \in \text{domain}(g)$.
   <details><summary>Proof</summary>
    TO ADD
   </details>

<div markdown="1" class="note">
Convexity is not closed under composition of functions in general. Let $f(x) = x^2$ and $g(x) = x^2-1$. Then $f (g x) = (x+1)^2(x-1)^2$ which is not convex. The real reason why $h = f g$ is non-convex is that $f' (g x) = 2(x^2 -1)$ is negative at the neighborhood of 0. The proof of point 3 comes from the characterization of a convex function in terms of its gradients. Let $h = f g$ then we need to prove that a) $h y - h x \ge h' (y -x)$ where $h' = (f'(g x)) \times (g' x)$. We also know that b) $g y - g x \ge g'(x) (y -x)$ c) $f (g y) - f (g x) \ge (f' (g x)) \times (g y - g x)$. Once we impose the constraint that $f' (g x) > 0$ then b) and c) are sufficient to prove a).
</div>

Naively these 3 pieces of information suggest that if I constrain $x$, $y_i$, $W_i$ to be non-negative then the output $y_{\text{N}}$ would be a convex function of the parameters $W_i$, where $N$ is the number of transformations/layers in the network. $y_i$ is anyway guaranteed to be non-negative because of $\text{relu}$. Now assume that we are just solving binary classification, so that the last layer $y_N$ contains only two nodes and we are using the cross-entropy loss and we only have one sample in our corpus and the outcome was 1 for that example. then we would basically have to minimize

$ \log(1 + \exp(y_{N,0} - y_{N,1}))  = \log(1 + \exp([1, -1]^T [y_{N,0}; y_{N,1}]))$

I need to do more analysis, but I think this is where our nice trail of convexity disappears. Even though the function $\log(1 + \exp(.)$ by itself is convex, the composition is not because of $[1, -1]$ but honestly I am not sure about this at this point. There are two things in my mind as I approach this problem

1. Someone would have seen this way of convexifying neural networks, so I have a strong prior belief that I would be obstructed from actually creating a convex loss function.

2. I also believe that $\log(1 + \exp(\langle \kv{\theta}, \kv{x} \rangle))$ is convex in general, so I feel like pont 2 above may not be general enough.

In any case, I have written down a fairly coherent chain of steps of a construction that I can systematically check, so I should know the answer soon enough.

###Bibliography###
{% bibliography --cited %}
