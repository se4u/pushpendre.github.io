---
title:  "Beginners analysis for optimization in Data Science."
layout: post
date:   2016-01-12 01:37:48
---

Calculus, Pre-calculus and Beginners Analysis deal with concepts (definitions)
and facts (stated as theorems) about sequences and functions defined on real
or complex variables. Depending on the domain and range of the functions, the
calculus may be termed univariate or multivariate or vector calculus.
The following is a list of constructions and theorems that an engineer needs to
know for applied optimization, statistics, machine learning. Note that
this list is necessarily short and biased, does not cover topological concepts,
does not talk about functional analysis and more advanced concepts needed for
non-parametric models. This is the type of beginners analysis that one would need
to keep in
mind while doing non-linear constrained or unconstrained optimization of
typical machine learning objectives defined over reals: {% fn %}

1. The constructions of $\mathbb{R}$.
   1. Dedekind Cuts.
   2. The decimal representation - As a collection of $p$-adic sequences.
2. Equivalent axioms for constructing Reals.
   1. The least upper bound axiom.
      That every bounded set has a least upper bound.
   2. Monotone bounded sequences converge.
   3. Nested Interval Theorem
      A sequence of closed, bounded, non-empty sets, each of which is
      completely contained in its predecessors leads to a non-empty set.
      The non-empty set has a single element if the length of the
      intervals converges to 0.
3. Limit theorems - Interplay of upper bounds, least upper bounds (their lower analogues) and limits and lim sups and lim infs.
   1. The fact above that monotone bounded sequences converge.
   2. The fact that lim sup is less than or equal to the least upper bound.
   3. The fact that lim-inf is greater than the largest lower bound.
   4. The fact that convergent sequences are necessarily bounded with the same lim sup and lim inf.
   5. The definition of lim-sup and lim-inf creates a monotone sequence.
   6. This means every sequence has a monotone sequence.
   7. (Bolzano-Weierstrass) Every bounded sequence has a convergent subsequence (therefore cauchy sequence)
   8. (Corr. of BW) Every cauchy sequence of real numbers converges.
   9. (Weierstrass M-test) Let $(M_k)$ be a sequence of nonnegative real numbers where
      $\sum M_k < \infty$. If $|g_k(x) \le M_k$ for all $x$ in a set S, then $\sum g_k$
      converges unifrmly on $S$.
4. The algebra of limits - Tests for existence of limits.
   1. The map from convergent sequences to their limits is closed under:
      Addition, Multiplication and Division.
   2. Tests for existence/non-existence of limits of series, specially partial sums.
      Note that tests are just theorems about convergence of series.
      1. Term Test
      2. Root Test
      3. Ratio Test
      4. Absolute Convergence
      5. Alternating Series Test
      6. Cauchy Condensation Test
      7. Abel Test
      8. Dirichlet Test
5. Special types of sequences.
   1. Power series.
      Given a sequence $(a_n)$, the series $\sum_{n=0}^{\infty} a_n x^n$
      is called a power series. The power series is a sequence that is also
      a function wrt $x$. It turns out that the power series enjoys the special
      property that it either converges for all $x \in \mathbb{R}$ or only $x=0$
      or it converges $\forall x: x \in B_r(0)$ where $B_r(0)$ is a ball of radius
      $r$ centered at $0$. The radius of convergence $r$ is equal to
      $\frac{1}{\lim \sup |a_n|^{1/n}}$. The power series diverges for $|x| > r$
      and converges when $|x| < r$. When $|x| = R$ then you need to check
      case-by-case.
   2. Term-by-term power series differentiation and integration.
6. The concept of continuity.
7. Sequences of functions.
   Let $(f_n)$ be a sequence of real-valued functions defined on a set
   $S \subseteq \mathbb{R}$.
   1. Pointwise Convergence.
      The sequence $(f_n)$ converges pointwise to a function
      $f$ defined on $S$ if $\lim_{n \to \infty} f_n(x) = f(x) \forall x \in S$
   2. Uniform Convergence - this preserves continuity.
      $(f_n)$ converges uniformly on $S$ to a function $f$ defined on $S$ if
      for each $\epsilon > 0$ there exists a number $N$ such that
      $|f_n(x) - f(x)| < \epsilon$ for all $x \in S$ and all $n > N$.
      Uniform convergence, is regularization enough, for a lot of mix-match.
      1. Let $(f_n)$ be a sequence of continous functions on $[a,b]$ that
         converges uniformly to $f$. Then
         $lim_{n \to \infty} \int_a^b f_n(x) dx = \int f(x) dx$.
   3. A sequence of functions is uniformly Cauchy on $S$ if
      for each $\epsilon > 0$ there exists a number N such that
      $|f_n(x) - f_m(x)| < \epsilon$ for all $x \in S$ and all $m,n > N$.
8. Differentiation.
9. Integration.
10. Theorems about Approximations.
    1. Mean Value Theorem - Rolle's theorem.
    2. Cauchy's Mean Value Theorem.
    3. Taylor's theorem.
       1. Peano Remainder Form.
          Let $k \ge 1 \in \mathbb{Z}$. Let $f : \mathbb{R} \to \mathbb{R}$ be $k$ times
          differentiable at $a \in \mathbb{R}$. Then
          $\exists h_k : \mathbb{R} \to \mathbb{R}$ such that
          $$ f(x) = f(a) + f'(a)(x-a) + f''(a)/2!(x-a)^2 + \ldots + f^{(k)}(a)/k!(x-a)^k + h_k(x)(x-a)^k$$
          and $lim_{x \to a} h_k(x) = 0$.
       2. Lagrange Remainder Form.
          Let $f : \mathbb{R} \to \mathbb{R}$ be $k+1$ times differentiable on the
          open interval with $f^{(k)}$ continuous on the closed interval between a and x.
          Then $$R_k(x) = f^{k+1}(\xi_L)/(k+1)! (x - a)^{k+1}$$ for some real number
          $\xi_L$ between a and x.
       3. Cauchy Remainder Form.
          Let $f : \mathbb{R} \to \mathbb{R}$ be $k+1$ times differentiable on the
          open interval with $f^{(k)}$ continuous on the closed interval between a and x.
          Then $$R_k(x) = f^{k+1}(\xi_C)/k! (x - \xi_C)^k(x - \xi_C)^k (x-a)$$
       4. Proofs.
          1. Through integration by parts.
          2. As generalization of Mean Value Theorem.
    4. L'Hospital's rule.
    5. Intermediate Value Theorem.
    6. Extreme Value Theorem.
11. Fundamental Theorem of Calculus.
12. Techniques in Analysis.
    1. Inequalities.
       1. Bernoulli Inequality - Let $a > -1$, then $\forall n\ (1 + a)^n > 1 + na$
    2. The constructions of $e$.
       * Sandwich of $(1 + 1/n)^n$ and $(1 + 1/n)^{n+1}$

## Books ##

1. More calculus of a single variable. Peter Mercer
2. Elementary Analysis: The theory of calculus. Kenneth Ross
3. Real Analysis. Carothers

Next Step.

* Calculus on Normed Vector Spaces, Rodney Coleman.

## Footnotes ##
{:.no_toc}
{% footnotes %}
{% fnbody %}
It is background knowledge that a series is a sequence made up of partial sums.
{% endfnbody %}
{% endfootnotes %}
