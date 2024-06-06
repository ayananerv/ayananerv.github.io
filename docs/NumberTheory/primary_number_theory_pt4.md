# Fantastic Prime Numbers

## The Sieve of Eratosthenes

**Def 8** A prime is an integer greater than $1$ that is only divisible by $1$ and itself.

**Lemma 3** Every integer greater than $1$ has a prime divisor.

> *Proof* For an integer $n$ greater than $1$, if $n$ is prime, it then has a prime divisor as itself by definition. If n is not prime, assume $d_1 \mid n, 2 \leq d_1<n$. If $d_1$ is prime, the Lemma is proved, otherwise assume $d_2 \mid d_1$ and repeat the procedure. Since the sequence $d_j$ has least bound $2$ is a prime, thus $n$ must have a prime divisor.

**Thm 12** If $n$ is a composite integer, then $n$ has a prime factor not exceeding $\sqrt{n}$.

> *Proof* Since $n$ is composite, then $n=ab$ for some integers $1<a \leq b<n$. Obviously, $a \leq \sqrt{n} \leq b$. By Lemma 3, $a$ must have a prime divisor $d \leq \sqrt{n}$ and $d$ is also a divisor of $n$.

### Exercises

+ Show that no integer of the form $a^3+1$ is a prime except $2=1^3+1$.

+ Show that if 2^n-1 is prime, then n is prime.

> *Hint: $(a^{kl}-1)=(a^k-1)(1+a^k+...+(a^k)^{l-1})$*

## The infinitude of Primes

**Thm 13** There are infinitely many primes.

> *Proof* Suppose there are finitely many primes $p_1,p_2,p_3,...,p_n$ where $p_1 \leq p_2 \leq p_3 \leq ... \leq p_n$. Set an positive integer $Q=p_1p_2...p_n+1$. Obviously, $Q>p_n$. Now we prove that $Q$ is a prime.
>
> By Lemma 3, every integer greater than one has a prime divisor, now we assume it is $p_i$. $Q$ can be written as
>
> $$
> Q=(q_1q_2...q_{i-1}q_{i+1}...q_n)q_i+1
> $$
>
> hence $q_i \nmid Q$, which means $Q$ does not have a prime divisor less than $Q$, thus $Q$ is a prime.

> **Question** Denote $\mathbb{P}$ is the set of all primes. Is the proposal true that $|\mathbb{P}|=\alef_0$?
>
> **Answer** In fact, every infinite subset $A$ of $\mathbb{N}$ has cardinality $\aleph_0$.
>
> We can define a bijection:
>
> $$
> f : A \subset \mathbb{N} \rightarrow \mathbb{N}
> $$
>
> $$
> f(a)=|\{n \in A : n<a\}|
> $$
>
> Firstly, we prove that $f$ is an injection. By well-ordering principle, set $A$ has a least element $m$, hence $f(a)=|\{n \in A : n<a\}|=a-m$. It is obvious that $f$ is an injection. Then now we prove that $f$ is also a surjection. For any element k in \mathbb{N}, we can find an element k+m in