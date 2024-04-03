# Start with Division

## Divisibility and the Division Algorithm

**Def 1** If $a$ and $b$ are integers *s.t.* $a \neq 0$, then we say **"$a$ divides $b$"** if there exists an integer $k$ *s.t.* $b=ka$, denoted $a \mid b$.

**Example 3**

*a. $2 \mid n$ if $n$ is even, $2 \nmid n$ if $n$ is odd.*

*b. $\forall a \in \mathbb{Z}$ one has that $a \nmid 0$.*

*c. If $b \in \mathbb{Z}$ and $|b|<a$, and $b \neq 0$, then $a \nmid b$.*

**Thm 3** If $a$, $b and $c$ are integers *s.t.* $a \mid b$ and $b \mid c$, then $a \mid c$.

**Thm 4** If $c \mid a$ and $c \mid b$, then $c \mid (ma+nb)$ for all $m, n \in \mathbb{Z}$.

**Corollary** If $a \mid b_1, a \mid b_2, ..., a \mid b_n$, then

$$
a \mid \sum_{j=1}^{n}k_jb_j.
$$

### Division Algorithm

**Thm 5. The Division Algorithm** If $a$ and $b$ are integers *s.t.* $b>0$, then there exist **unique** integers $q$ and $r$ *s.t.* $a=bq+r$ where $0 \leq r < b$.

> *Proof* (**Existence**) Consider the set $A=\{a-bk | a-bk \geq 0 \wedge k \in \mathbb{Z}\}$. Note that $A$ is not empty since for $k<a/b, a-bk \in A$. Thus there exists a least element $r=a-bq \in A$ for some $q$ by the **Well Order Principle**. Notice that $r \geq 0$ by construction and if $r \geq b$, then
>
> $$
> s=r-b=a-b(q+1) \geq 0
> $$
>
> is smaller than $r$, implying that $r$ is not the least element in $A$. As a result we have $0 \leq r < b$.
>
> (**Uniqueness**) Suppose $a=bq_1+r_1$ and $a=bq_2+r_2$ and $q_1>q_2, r_1<r_2$, then
>
> $$
> r_2-r_1=(a-bq_2)-(a-bq_1)=(q_1-q_2)b \geq b
> $$
>
> Since $0 \leq r_1 < b$, we get $r_2 \geq b$ which is incorrect. Thus $q$ and $r$ are unique.
>
> ### Exercises

**Exercises**

4. For nonzero integers $a, c$ and integers $b, d$, *s.t.* $a \mid b$ and $c \mid d$, then $ac \mid bd$.

5. If $a$ and $b$ are positive integers and $a \mid b$, then $a \leq b$.

11. If $ac \mid bc$, then $a \mid b$.

12. If $a \mid b$ and $b \mid a$, then $a=\pm b$.

## Representations of Integers in Different Bases

**Notation** An integer $a$ written in base $b$ expansion is denoted by $(a)_b$.

**Thm 6** Let $b$ be a positive integer with $b>1$. Then any positive integer $m$ can be written uniquely as

$$
m=a_lb^l+a_{l-1}b^{l-1}+...+a_1b+a_0
$$

where $l$ is a positive integer, $0 \leq a<b$ for $j =0,1,...,l$ and $a_l \neq 0$.

> *Proof* (**Existence**) First of all, we have
>
> $$
> 1=0 \times b+1
> $$
>
> Suppose we have
>
> $$
> m=\sum_{j=0}^{l}a_jb^j
> $$
>
> then we have
>
> $$
> m+1=(\sum_{j=0}^{l}a_jb^j)+1
> $$
>
> If
>
> $$
> a_0+1<b
> $$
>
> Thus the proof finishes; otherwise let
> $a'_0=0$ and $a'_1=a_1+1$.
>
> So we can repeat this process iteratively. Since the process is finite so it ends at some time.
>
> (**Uniqueness**) Suppose
>
> $$
> m=\sum_{j=0}^{k}c_jb^j
> $$
>
> where $k>=l$. Assume $a_j=0$ for all $l<j \leq k$.
>
> Using **The Division Algorithm**, $m$ can be uniquely divided to $m=qb+r$ *s.t.* $a_0=c_0$. More again, let $n=(m-a_0)/b$, we get $a_1=c_1$. At last, we get $a_j=c_j$ for any $j \leq k$.