---
title:  "Induction and Recursion"
layout: post
date:   2015-08-02 16:52:26
---
<div markdown="1" class="note">
The following article summarizes the arguments presented in the book "A mathematical introduction to logic"(2001 edition) by Herbert Enderton on the topic of Induction and Recursion in Section 1.4. I have omitted the proofs and mainly placed the theorems in context.
</div>
$$\newcommand{\Epsilon}{\mathcal{E}}$$

## Introduction ##

The section on Induction analyzes the situation where one wants to construct a closure $C$ from a set of generating elements $B \subseteq U$($U$ is the universe). This section shows two seemingly different ways to doing so; 1) Top Down, 2) Bottom Up, that actually turn out to be the same under closer scrutiny. The entire section is devoted to proving that Top Down and Bottom Up inductions result in the same sets.

The section on recursion builds upon the previous section and presents sufficient conditions for the validity of constraints or rules that state how to compute the following:

1. $\bar{h}(x)$ for $x \in B$.
2. $\bar{h}(f(x, y))$ making use of $\bar{h}(x), \bar{h}(y)$.
3. $\bar{h}(g(x))$ making use of $\bar{h}(x)$.

By validity we mean that the computation rules should not be self contradictory and that the resultant object should be a valid function. If we consolidate the rules for computing $\bar{h}(x)$ for $x \in B$ and call the consolidated rules the function $h$ and similarly consolidate the rules in 2. and 3. and call them $F$ and $G$ respectively then it is easy to see that if $\bar{h}$ exists then it is uniquely determined by $h, F, G$. The hard part really is proving that $h, F, G$ must be "valid" (not run into contradictions) and one sufficient condition for that is that $C$ is "freely-generated" from $B$ by $f$ and $g$.

The fact that "free-generation" of $C$ is sufficient for the validity of the existence of the extension $\bar{h}$ is presented as the "Recursion Theorem" and then this theorem is used to prove that the $\bar{v}$ is a valid extension of the (valuation of sentential symbols)($v$) to the valuation of wffs, where the wffs are syntactically generated using composition operations $\Epsilon_{X}$:

$$
\begin{align*}
\Epsilon_{\neg}(\alpha) &= (\neg{\alpha}) \\
\Epsilon_{\land}(\alpha, \beta) &= (\alpha \land \beta)\\
\Epsilon_{\lor}(\alpha, \beta) &= (\alpha \lor \beta)\\
\Epsilon_{\rightarrow}(\alpha, \beta) &= (\alpha \rightarrow \beta)\\
\Epsilon_{\leftrightarrow}(\alpha, \beta) &= (\alpha \leftrightarrow \beta)
\end{align*}
$$

{% center_text AND, $\bar{v}$ is generated as follows %}

$$
\begin{equation*}
\bar{v}((\neg(\alpha))) = \text{ T if } \bar{v}(\alpha) = \text{ F else F} \text{and so on... }
\end{equation*}
$$

<div markdown="1" class="note">
The parenthesis are extremely important. They make strings behave like ordered pairs. In fact every wff starts with "(". and $\neg A \land B$ is actually $((\neg A) \land B)$.
</div>

That is because in the "Unique Readability Theorem" we prove that not only do the 5 functions $\Epsilon_{X}$ generate $C$ but their restrictions to the set of wffs:

1. Have disjoint ranges.
2. Are one-to-one.

## Induction ##

Imagine that you are given a set $U$ and that you then want to "generate" a closure of $B$ (which is a subset of $U$) from operations like $f, g$. For concreteness' sake $f$ is binary and $g$ is unary. I.e. the type signatures of $f$ and $g$ are:

$$
\begin{equation*}
 f :: U \times U \rightarrow U \\
 g :: U \times U
\end{equation*}
$$

Now there are two ways of "inducing" the "closure" of $B$ that we call $ C^{*} $ and $ C_{*} $.

### Top Down Induction ###

1. Say that a subset $S$ of $U$ is "closed" under $f, g$ if $x, y \in S \implies f(x, y), g(x) \in S$.
2. Say that a subset $S$ of $U$ is "inductive" if $B \subseteq S$ and $S$ is closed.
3. Let $C^{*}$ = intersection of all inductive subsets of $U$.

### Bottom Up Induction (Constructive approach) ###

1. Define a construction sequence to be a finite sequence $x_1, \ldots, x_n$ of elements of $U$ such that $\forall i \le n$ at least one of the following is true
    * $x_i \in B$
    * $x_i = f(x_j, x_k) \text{ for some } j < i, k < i$
    * $x_i = g(x_j) \text{ for some } j < i$
2. $C_{*}$ is the set of all points $x$ such that some construction sequence ends with $x$.

## Recursion ##


### Freely Generated ###

$C$ is "freely generated" from $B$ by $f, g$ iff in additional to the fact that $C$ is generated from $B$; $f_C, g_C$, the restrictions of $f, g$ to $C$ meet the following condition:

1. $f_C, g_C$ are one-to-one.
2. Range of $f_C, g_C, B$ are disjoint from each other (pairwise disjoint).

### Recursion Theorem ###

<div markdown="1" class="theorem">
Assume that the subset $C$ of $U$ is freely generated from $B$ by $f, g$ where:

$$
\begin{equation*}
f :: U \times U \rightarrow U \\
g :: U \rightarrow U
\end{equation*}
$$

Further assume that $V$ is a set and $F, G, h$ are functions such that:

$$
\begin{equation*}
h :: B \rightarrow V \\
F :: V \times V \rightarrow V \\
G :: V \rightarrow V
\end{equation*}
$$

Then there is a unique function $\bar{h} :: C \rightarrow V $ such that

1. For $x \in B, \bar{h}(x) = h(x)$
2. For $x, y \in C$ :
    1. $\bar{h}(f(x, y)) = F(\bar{h}(x), \bar{h}(y)$
    2. $\bar{h}(g(x)) = F(\bar{h}(x))$

<div markdown="1" class="note">
It is incredible that just the free generation of $C$ from $f, g, B$ is sufficient for the validity of $\bar{h}$. The fact that it is not dependent on $h, F, G$ at all is incredible. Don't be fooled that $F, G$ are named similar to $f, g$ they are completely different and unrelated functions.

To quote: Algebraically, the conclusion of this theorem says that any map $h$ of $B$ into $V$ can be extended to a homomorphism $\bar{h}$ from $C$ (with operations $f, g$) into $V$ (with operations $F, G$).
</div>
</div>



<div markdown="1" class="fun">
An advertisement for a tennis magazine states, "If I'm not playing tennis, then I'm watching tennis. And if I'm not watching tennis, I'm reading about tennis." We can assume that the speaker cannot do more than one of these activities at a time. What is the speaker doing?
</div>
