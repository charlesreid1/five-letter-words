# Prime strings and unique factorization

Knuth, *The Art of Computer Programming*, Volume 4A, Section 7.2.1.1,
exercises 101, 102 and 104. Code: `prime_strings.py`.

## Definitions

Strings are over a linearly ordered alphabet and compared in
lexicographic (dictionary) order. In particular α ≤ αβ always, and
α < αβ iff β is nonempty.

**Definition P.** A string is *prime* if it is nonempty and less than all
of its proper suffixes.

So `01101` is not prime (it is greater than its suffix `01`), while
`01102` is prime (less than `1102`, `102`, `02`, `2`). Prime strings are
also called Lyndon words.

## Exercise 101

### (a) If λ and λ' are prime and λ < λ', then λλ' is prime.

Let β be a proper suffix of λλ'. We show λλ' < β. There are two shapes.

*β = αλ' with α a proper suffix of λ.* Since λ is prime, λ < α. Because
|α| < |λ|, α is not a prefix of λ, so λ and α differ at some position
inside α. Appending λ' to both cannot change that comparison, hence
λλ' < αλ'.

*β is a suffix of λ'.* Then β ≤ λ' (with equality iff β = λ'). Two
subcases:

- λ is not a prefix of β. From λ < λ' ≤ β, the strings λ and β differ at
  a position within λ, so λλ' < β.
- λ is a prefix of β, say β = λγ. Then γ is a suffix of λ' of length
  |β| - |λ| ≤ |λ'| - 1, so γ is a proper suffix of λ' and λ' < γ because
  λ' is prime. Therefore λλ' < λγ = β.

### (b) Every string α can be written α = λ₁λ₂…λₜ with λ₁ ≥ λ₂ ≥ … ≥ λₜ, each λⱼ prime.

Every one-character string is prime (it has no proper suffixes). Begin
with α split into its |α| single characters. While some adjacent pair
satisfies λⱼ < λⱼ₊₁, replace the pair by λⱼλⱼ₊₁, which is prime by (a).
Each step reduces the number of factors by one, so the process stops,
and it can only stop when no adjacent pair increases, i.e. when the
factors are nonincreasing.

`factor_greedy()` in the script runs this argument literally.

### (c) The factorization in (b) is unique.

*Hint: λₜ is the lexicographically smallest nonempty suffix of α.*

Let λ be the smallest nonempty suffix of α = λ₁…λₜ. Every proper suffix
of λ is also a suffix of α, so λ is less than all of them: λ is prime.

Since λ is a suffix of α it has the form βγ where β is a nonempty suffix
of some λⱼ and γ = λⱼ₊₁…λₜ. Then

    λₜ ≤ λⱼ ≤ β ≤ βγ = λ ≤ λₜ.

The first inequality is the nonincreasing condition. The second holds
because λⱼ is prime (β is a suffix of λⱼ, either proper, giving λⱼ < β,
or equal). The third is α ≤ αβ. The last is minimality of λ. So λ = λₜ:
the last factor is forced to be the smallest suffix of α, independent of
the factorization.

Remove λₜ and apply the same argument to λ₁…λₜ₋₁, which is also a
nonincreasing prime factorization. By induction on |α| every factor is
forced.

### (d) True or false: λ₁ is the longest prime prefix of α.

**True.** λ₁ is certainly a prime prefix. Suppose some prime prefix λ is
longer. Either λ ends exactly at a factor boundary or in the middle of a
factor.

- λ = λ₁…λₖ with k ≥ 2. Then λₖ is a proper suffix of λ, so λ < λₖ. But
  λₖ ≤ λ₁ (nonincreasing) and λ₁ ≤ λ (λ₁ is a prefix of λ). So λ < λ,
  contradiction.
- λ = λ₁…λₖβ' with β' a nonempty proper prefix of λₖ₊₁ (k ≥ 1). Then β'
  is a proper suffix of λ, so λ < β'. But β' ≤ λₖ₊₁ ≤ λ₁ ≤ λ, the same
  contradiction.

Knuth's one-line version: if α = λβ with λ prime and |λ| > |λ₁|, then
λ followed by the factors of β would be a second factorization of α,
contradicting (c).

### (e) Prime factors of 3141592653589793238462643383279502884197

    3
    1415926535897932384626433832795
    02884197

Knowing more digits of π would never change the first two factors, since
every further digit lands in the third factor or later. The infinite
decimal expansion of any number that is "normal" in Borel's sense
factors into primes of finite length.

## The algorithm in `factor()`

The script uses Duval's algorithm (J. P. Duval, *J. Algorithms* **4**
(1983), 363-381), which Knuth presents as steps E4-E5 of the answer to
exercise 106. It runs in O(n) time and O(1) extra space.

Maintain indices i ≤ k < j. The string s[i:j] is always a *preprime*,
a nonempty prefix of some prime, and by Theorem Q it is the
(j-i)-extension of the prime s[i:i+p] where p = j - k. Compare s[k]
against s[j]:

- s[k] < s[j]: s[i:j+1] is itself prime (exercise 105(a)). Reset k to i.
- s[k] = s[j]: the periodic extension continues. Advance k.
- s[k] > s[j] or j = n: the preprime cannot be extended. By exercise
  105(b), s[i:i+p] is the first factor λ₁, and it repeats
  ⌊(j-i)/p⌋ times. Emit those copies, move i past them, and restart.

The random cross-check in the script confirms, for 8000 strings, that
the output is a factorization into primes (by Definition P), is
nonincreasing, and agrees with the greedy merge of (b), which by (c) is
the only possible answer.

## Exercise 102: counting primes from the factorization theorem

Let L_m(n) be the number of m-ary primes of length n. Knuth derives eq.
(60) in the text from cyclic shifts. Exercise 102 asks for it from
exercise 101 instead.

A nonincreasing sequence of primes is the same thing as a multiset of
primes, so exercise 101 says: strings of length n over m letters are in
bijection with multisets of primes whose lengths sum to n. Count both
sides with a generating function in z, where z marks one character.

The left side is Σ mⁿ zⁿ = 1/(1 - mz).

On the right, each individual prime λ contributes a factor
1 + z^|λ| + z^2|λ| + … = 1/(1 - z^|λ|), the choice of how many copies of
λ the multiset holds. Grouping primes by length gives the Euler product

    1/(1 - mz) = ∏_{n≥1} (1 - zⁿ)^(-L_m(n)).

Take logarithms and expand both sides with -ln(1 - x) = Σ x^k / k:

    Σ_{k≥1} m^k z^k / k = Σ_{n≥1} L_m(n) Σ_{j≥1} z^{nj} / j.

Compare coefficients of z^N. On the right, z^N arises from every pair
(n, j) with nj = N, and 1/j = n/N:

    m^N / N = (1/N) Σ_{n | N} n L_m(n),  that is  Σ_{d | N} d L_m(d) = m^N.

This is eq. (59), obtained without the cyclic-shift argument. Möbius
inversion (exercise 4.5.3-28(a), or 4.6.2-4 which Knuth cites for the
same product) then gives eq. (60):

    L_m(n) = (1/n) Σ_{d | n} μ(d) m^{n/d}.

The script computes L_m(n) this way in `num_primes`, and confirms it
three independent ways: brute-force counting from Definition P for small
m and n, the divisor sum (59), and expanding the Euler product through
z¹² to recover the coefficients mⁿ.

| n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| L₂(n) | 2 | 1 | 2 | 3 | 6 | 9 | 18 | 30 | 56 | 99 |
| L₃(n) | 3 | 3 | 8 | 18 | 48 | 116 | 312 | 810 | 2184 | 5880 |
| L₄(n) | 4 | 6 | 20 | 60 | 204 | 670 | 2340 | 8160 | 29120 | 104754 |

Since the d = 1 term dominates, L_m(n) ≈ mⁿ/n: about 1/n of all strings
are prime, which is the estimate exercise 104 uses. For the SGB alphabet
L₂₆(5) = (26⁵ - 26)/5 = 2376270, exactly one fifth of 26⁵ after
discarding the 26 constant strings.

## Exercise 104: five-letter words

Formula (60) says about 1/n of all n-letter strings are prime, so about
1/5 of the 5757 SGB words, roughly 1151. Real words run a little higher,
at 1274, a fraction of 0.2213. Running `is_prime` over the
list:

| | count |
|---|---|
| prime | 1274 |
| nonprime | 4483 |

The first nonprimes alphabetically are `abaca`, `agora`, `ahead`. The
last primes are `rusts`, `rusty`, `rutty`. So the smallest nonprime is
`abaca` and the largest prime is `rutty`.

Knuth notes that `prime` is not prime (it factors as `pr` `im` `e`),
while `lowly` is, so perhaps prime strings should be called lowly.
