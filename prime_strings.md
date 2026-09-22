# Prime strings and unique factorization

Knuth, *The Art of Computer Programming*, Volume 4A, Section 7.2.1.1,
exercises 101 and 104. Code: `prime_strings.py`.

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

## Exercise 104: five-letter words

Formula (60) says about 1/n of all n-letter strings are prime, so about
1/5 of the 5757 SGB words, roughly 1151. Running `is_prime` over the
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
