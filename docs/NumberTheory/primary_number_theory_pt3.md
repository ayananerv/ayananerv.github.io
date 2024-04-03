# About Divisors And The Euclidean Algorithm

## The Greatest Common Divisor

**Def 2** The *greatest common divisor* of two integers $a$ and $b$ is the greatest integer that divides both $a$ and $b$.

We denote the greatest common divisor of two integers $a$ and $b$ by $(a,b)$. We also define $(0,0)=0$.

**Def 3** Two integers $a$ and $b$ are *relatively prime* if $(a,b)=1$.

**Thm 7** If $(a,b)=d$ then $(a/d,b/d)=1$.

> *Proof* Suppose $(a/d,b/d)=c$ then
>
> $$
> a/d=k_1c
> $$
>
> $$
> b/d=k_2c
> $$
>
> $$
> a=k_1cd
> $$
>
> $$
> b=k_2cd
> $$
>
> for some integers $k_1$ and $k_2$ where $(k_1,k_2)=1$. So we have $(a,b)=cd$ thus $c=1$.

**Thm 8** Let $a, b$ and $c$ be integers. Then $(a,b)=(a+cb,b)$.

> *Proof* Suppose $(a,b)=d$ then $d \mid a$ and $d \mid b$. Thus $d \mid a+cb$. If $(a+cb,b)=d' \neq d$ *i.e.*, $d$ is not the greatest common divisor of $a+cb$ and $b$, which implies
>
> $$
> d' \mid (a+cb)
> $$
>
> $$
> d' \mid b
> $$
>
> So $b=kd'$ for some integer $k$ and $a=(k-ck)d'$ thus $d' \mid a$. However, since $d$ is the greatest common divisor of $a$ and $b$ thus $d>d'$, which leads to contradiction. So $(a+cb,b)=d$ and $(a,b)=(a+cb,b)$.

**Eg 10** *Notice that $(4,14)=(4,14-3 \cdot 4)=(4,2)=2$.*

**Thm 9** The greatest common divisor fo two integers $a$ and $b$, not both $0$ is the least positive integer *s.t.* $ma+nb=d$ for some integers $m$ and $n$.

> *Proof* Assume $a, b$ are positive integers. Consider the set of all **positive** linear combination of $a$ and $b$, denoted by $A=\{ma+nb | m,n \in \mathbb{N}\}$. Now $A$ is not empty since $a=1 \cdot a+0 \cdot b$ and $b=0 \cdot a+ 1 \cdot b$ are in $A$. By the well-ordering principle, there exists a least element $d=ma+nb$ in $A$. Now we need to prove that $d$ is the greatest common divisor of $a$ and $b$.
> By the division algorithm, we have
>
> $$
> a=qd+r, 0 \leq r<d
> $$
>
> Thus
>
> $$
> r=a-qd=(1-qm)a-qnb
> $$
>
> So $r$ is a positive linear combination of $a$ and $b$ or $r=0$. The former case is incorrect. Hence $d \mid a$. Similarly, $d \mid b$. For any integer $c$ satisfying $c \mid a$ and $c \mid b$ we get $c \mid (ma+nb)$ and $c \mid d$. Hence $d$ is the greatest common divisor of $a$ and $b$.

**Corollary** If $a$ and $b$ are relatively prime then there exist integers $m$ and $n$ *s.t.* $ma+nb=1$.

**Def 4** Let $a_1,a_2,...,a_n$ be integers, not all $0$. The greatest common divisor of these integers is the largest integer that divides all of the integers in the set. The greatest common divisor of $a_1,a_2,...,a_n$ is denoted by $(a_1,a_2,...,a_n)$.

**Def 5** The integers $a_1,...,a_n$ re said to be *mutually relatively prime* if $(a_1,...,a_n)=1$.

**Def 6** The integers $a_1,...,a_n$ re said to be *pairwise relatively prime* if for each $i \neq j$, we have $(a_i,a_j)=1$.

### Exercises

**Exercises**

+ Let $m$ be a positive integer. Find the greatest common divisor of $m$ and $m+1$.

+ Let $m$ be a positive integer, find the greatest common divisor of $m$ and
$m + 2$.

> *Hint: Odd and Even.*

+ Show that if $m$ and $n$ are integers such that $(m, n) = 1$, then $(m+n,m-n)=1$
or $2$.

> *Proof* First of all, we prove that if $(m,n)=1$ then $(2m,2n)=2$.
>
> It is easy to see that $2$ is a common divisor of $2m$ and $2n$. Since $(m,n)=1$, there exist two integers $x$ and $y$ *s.t.* $xm+yn=1$ and so $x(2m)+y(2n)=2$ thus $2$ is the greatest common divisor of $2m$ and $2n$ according to Thm 9.
>
> Suppose $(m+n,m-n)=d$. By Thm 8,
>
> $$
> (m+n,m-n)=(m+n,m-n+1 \cdot (m+n))=(m+n,2m)
> $$
>
> and
>
> $$
> (m+n,m-n)=(m+n,m-n-1 \cdot (m+n))=(m+n,-2n)=(m+n,2n)
> $$
>
> Thus $d \mid 2m$ and $d \mid 2n$. $d \leq 2$.
>
> If $m+n$ is an even number, $2 \mid (m+n)$ and $2 \mid 2m$ so $2 \leq d$ and $d=2$.
>
> If $m+n$ is an odd number, $2 \nmid (m+n)$ thus $d=1$.

+ Show that if $a_1, a_2, ..., a_n$ are integers that are not all $0$ and $c$ is a positive integer, then $(ca_1, ca_2, ..., ca_n) = c(a_1, a_2, ..., a_n)$.

> *Proof* Suppose $(a_1,...,a_n)=d$ and $(ca_1,...,ca_n)=d'$. It is easy to verify that $cd \leq d'$. Now we prove that $d' \leq cd$.
>
> **Lemma** $d \mid ca$ iff $d \mid c$ or $d \mid a$.
> The proposition is equivalent to $d \nmid ca$ iff $d \nmid c$ and $d \nmid a$. The sufficiency is obvious and if $d \nmid ca$ then $ca=dq+r$ where $0<r<d$. The case $d \nmid c$ leads to $ca=dq$, which is contradict to our previous condition.
>
> Since $(ca_1,...,ca_n)=d'$, $d' \mid ca_j$ for $1 \leq j \leq n$. If $d' \mid c$, $d' \mid cd$ instantly. Otherwise $d' \mid a_j$ thus $d' \leq d \leq cd$. Hence $d=d'$.

## The Euclidean Algorithm

**Lemma 1** If $a$ and $b$ are two integers and $a=bq+r$ where also $q$ and $r$ are integers, then $(a,b)=(r,b)$.

> *Proof* $(a,b)=(bq+r,b)=(b,r)$ by Thm 8 instantly.

**Thm 10** Let $a=r_0$ and $b=r_1$ be two positive integers where $a \geq b$. If we apply the division algorithm successively to obtain that

$$
r_j=r_{j+1}q_{j+1}+r_{j+2}, 0 \leq r_{j+2}<r_{j+1}
$$

for all $j=0,1,...,n-2$ and

$$
r_{n+1}=0
$$

Then $(a,b)=r_n$.

> *Proof* By Lemma 1, $(a,b)=(r_0,r_1)=(r_1q_1+r_2,r_1)=(r_1,r_2)=...=(r_n,r_{n+1})=(r_n,0)=r_n$.

### Exercises

**Exercises**

+ Let $a$ and $b$ be two positive integers where $a$ is even and $b$ is odd. Prove that $(a,b)=(a/2,b)$.

> *Proof* Suppose $(a,b)=d$ and $(a/2,b)=d'$. $d$ is odd since $b$ has no even divisors. Assume that $a=kd$ then $k$ is even. Thus $\frac{a}{2}=\frac{k}{2}d$ and $d \mid \frac{a}{2}$. Since $d'$ is the greatest common divisor of $(a/2,b)$ so $d \leq d'$.
>
> Similarly, $d' \mid \frac{a}{2}$ thus $d' \leq d$. Hence $d=d'$.

## Lame's Theorem

### Fibonacci Sequence

**Def 7** The Fibonacci sequence is defined recursively by $f_1=1, f_2=1$, and

$$
f_n=f_{n-1}+f_{n-2}, n \geq 3
$$

The terms in the sequence are called Fibonacci numbers.

In the following lemma, we give a lower bound on the growth of Fibonacci numbers.

**Lemma 2** For $n \geq 3$, we have $f_n>\alpha^{n-2}$ where $\alpha=(1+\sqrt{5})/2$.

> *Proof* We use the second principle of mathematical induction to prove our result. It is easy to see that this is true for $n=3$ and $n=4$. Assume that $\alpha^{k-2}<f_k$ for all integers $k$ where $k \leq n$. Now since $\alpha$ is a solution of the polynomial $x^{2}-x-1=0$, we have $\alpha^2=\alpha+1$. Hence
>
> $$
> \alpha^{n-1}=\alpha^{2}\alpha^{n-3}=(\alpha+1)\alpha^{n-3}=\alpha^{n-2}+\alpha^{n-3}
> $$
>
> By the inductive hypothesis, we have
>
> $$
> \alpha^{n-2}<f_n, \alpha^{n-3}<{f_n-1}
> $$
>
> After adding the two inequalities, we get
>
> $$
> \alpha^{n-1}<f_n+f_{n-1}=f_{n+1}.
> $$

### Lame's Theorem

**Thm 11** Using the Euclidean algorithm to find the greatest common divisor of two positive integers has number of divisions less than or equal to five times the number of decimal digits in the minimum of the two integers.

> *Proof* Let $a$ and $b$ be two positive integers where $a>b$. Applying the Euclidean algorithm to find the greatest common divisor of two integers with $a=r_0$ and $b=r_1$, we get
>
> $$
> r_0=r_1q_1+r_2
> $$
>
> $$
> r_1=r_2q_2+r_3
> $$
>
> $$
> \cdot
> $$
>
> $$
> \cdot
> $$
>
> $$
> \cdot
> $$
>
> $$
> r_{n-2}=r_{n-1}q_{n-1}+r_{n}
> $$
>
> $$
> r_{n-1}=r_nq_n.
> $$
>
> Notice that $q_1,...,q_{n-1} \geq 1$ and $q_{n} \geq 2$. Thus we have
>
> $$
> r_n \geq 1=f_2
> $$
>
> $$
> r_{n-1} \geq 2r_n \geq 2f_2=f_3
> $$
>
> $$
> \cdot
> $$
>
> $$
> \cdot
> $$
>
> $$
> \cdot
> $$
>
> $$
> r_2 \geq r_3+r_4 \geq f_{n-1}+f_{n-2}=f_n
> $$
>
> $$
> b=r_1 \geq r_2+r_3 \geq f_n+f_{n-1}=f_{n+1}.
> $$
>
> By Lemma 2, we have $f_{n+1}>\alpha^{n-1}$ for $n>2$. As a result, we have $b>\alpha^{n-1}$. Now notice since
>
> $$
> \log_{10}{\alpha}>\frac{1}{5}
> $$
>
> we get
>
> $$
> \log_{10}b>(n-1)/5.
> $$
>
> Thus we have
>
> $$
> n-1<5\log_{10}b.
> $$
>
> Now let $b$ has $k$ decimal digits thus $\log_{10}b<k$. Hence $n \leq 5k$.

### Exercises

**Exercises**

1. Find an upper bound for the number of steps in the Euclidean algorithm that is used to find the greatest common divisor of $38472$ and $957748838$.

> *Sol* By Lame's Theorem, the number of steps of Euclidean algorithm has a upper bound $\lfloor5\log_{10}38472\rfloor=22$.