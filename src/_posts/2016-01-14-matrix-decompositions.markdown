---
title:  "Matrix Decompositions"
layout: post
date:   2016-01-14 14:02:57
---

<div markdown="1" class="note">
Currently this post is skeletal.
The bibliography and background is incomplete.
</div>

Matrix decompositions can be thought of generally as representations of matrices.
Representations or datastructures that enable efficient operations.

Historically, one of the most common operation that one needs to perform with a matrix $M$
is to find a vector $x$ such that $Mx = y$ where $y$ is given. But there are other operations
that need to be done with a matrix as well. For example, we might need to find their
singular/eigen vectors. Also matrices may have structure like:

* Symmetry
* Positive Definiteness
* Semi Positive Definiteness
* Tri-Diagonalization
* Circulant Nature
* Toeplitz-ness
* Normality
* Idempotency
* Diagonality
* Random Sparsity

Matrices, also have representations associated with them. And those representations
sometimes encode the above properties. Let's list some of the decompositions that
are popular.

* SVD - $M = USV^T$
* QR - $M = QR$
* CS Decomposition
* LU - $M = LU$
* Permuted LU - $PM = LU$
* Cholesky - $M = LL^T$
* Permuted Cholesky - $PMP^T = LL^T$
* $LDL^T$ decomposition - Diagonal-Cholesky
* Permuted $LDL^T$ decomposition -
* UTV factorizations - T is triangular
* BiDiagonal Factorization - UBV
* Aasen - $PAP^T = LTL^T$ - T is tridiagonal
* Bunch-Parlett - $PAP^T = LDL^T$, where $D$ contains 1x1 and 2x2 diagonal blocks.
* $UTU^T$ decomposition, where U is orthogonal and T is tridiagonal,
* Antitriangular factorization $A = QMQ^T$, where Q is orthogonal and M is symmetric block lower antitriangular.

Now each of these decompositions brings something unique to the table.
Almost all of them enable efficient solution of a linear system of equations.
Some of them are known to support efficient rank-one updates/downdates.
And some of the others allow us to get a handle on the positive-definiteness of
the original matrix, and to "pre-condition" that original matrix while doing the
least modification.

Now let us list the
decompositions for which rank one updates/downdates algorithms are available.

* SVD - Only efficient in the thin rank case.
* QR - qrupdate is a builtin function in matlab.
* Diagonal-Cholesky - Exists always but only guaranteed to be stable if the resultant is PD
* Antitriangular Factorization - $A = QMQ^T$
* Bunch-Parlett - $PAP^T = LDL^T$ (Sorensen, 1977)

For a recent paper, I needed a decomposition for symmetric indefinite matrices that
allowed efficient symmetric rank-one updates and downdates and allowed low damage
positive definiteness inducing modifications to be made to representation. And after
the modification I needed to use the representation to solve a system of equations.
I also wanted the update scheme to numerically stable.

Note that all of these decompositions can be efficiently used while
solving a linear system of equations. The sensitivity of the solutions created
through them may vary however. With all these filters only the following
representations remain.

* QR - qrupdate is a builtin function in matlab.
* Antitriangular Factorization - $A = QMQ^T$
* Bunch-Parlett - $PAP^T = LDL^T$ (Sorensen, 1977)

Now for my application I needed a representation that would allow for easy access to
eigen values of the matrix and easy modification of them at each step, preferably in
$O(n^2)$ time. This leaves us with the one true matrix representation:

* Bunch-Parlett - $PAP^T = LDL^T$ (Sorensen, 1977)

This representation has all the desirable properties.
