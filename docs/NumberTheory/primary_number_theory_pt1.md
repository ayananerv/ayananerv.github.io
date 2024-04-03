# Mathematical Methods

## The Well Ordering Principle and Mathematical Induction

### The Well Ordering Principle

**The Well Ordering Principle** A least element exist in any non empty set of **positive integers**.

**The Pigeonhole Principle** If $s$ objects are placed in $k$ boxes for $s>k$, then at least one box contains more than one object.

> *Proof* Suppose that none of the boxes contains more than one object. Then there are at most $k$ objects. This leads to a **contradiction** with the fact that there are $s$ objects for $s>k$.

### Mathematical Induction

**Theorem 1. The First Principle of Mathematical Induction** If a set of positive integers has the property that, if it contains the integer $k$, then it also contains $k+1$, and if this set contains $1$ then it must be the set of all positive integers $\mathbb{N}^+$.

> *Proof* Let $S$ be the set of positive integers containing the integer $1$, and the integer $k+1$ whenever it contains $k$. Assume also that $S$ is not the set of all positive integers. As a result, there are some integers that are not contained in $S$ and thus those integers must have a least element $\alpha$. Notice that $\alpha \neq 1$ since $1 \in S$. But $\alpha-1 \in S$ thus leading to $\alpha \in S$. Thus $S$ must contains all positive integers.

**Example** *Use mathematical induction to prove that $n! \leq n^n$ for all positive integers n.*

> *Proof* Note that $1! \leq 1^1$. We now suppose that
>
> $$
> n! \leq n^n
> $$
>
> for some $n$, we prove that $(n+1)! \leq (n+1)^{n+1}$. Note that
>
> $$
> (n+1)! = (n+1)n! \leq (n+1)n^n \leq (n+1)(n+1)^n = (n+1)^{n+1}
> $$

**Theorem 2. The Second Principle of Mathematical Induction** A set of positive integers that has the property that for every integer $k$, if it contains all the integers $1$ through $k$ then it contains $k+1$ and if it contains $1$ then it must be $\mathbb{N}^+$.