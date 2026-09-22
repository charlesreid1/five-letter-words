# Euclidean distance between words

Warm-up for Knuth, *The Art of Computer Programming*, Volume 4A,
Section 7, exercise 28, which treats five-letter words as vectors.
Code: `euclidean_distance.py`.

## Words as vectors

Map each letter to its index in the alphabet, a = 0, b = 1, ..., z = 25.
A five-letter word becomes a point in {0, ..., 25}⁵ ⊂ ℤ⁵, and the
ordinary Euclidean distance applies:

    d(v, w) = sqrt( Σ_{i=0}^{4} (vᵢ - wᵢ)² ).

`word2vec` does the mapping with `ord(c) - ord('a')` and `l2norm` sums
the squared differences. This is a geometric distance in letter space.
It is not the edit (Levenshtein) distance of string algorithms: `abbey`
and `abbez` are at distance 1 here, while `abbey` and `zbbey` are at
distance 25, though each is one edit from `abbey`.

## Range and baseline

The distance is 0 only between identical words. The maximum is between
`aaaaa` and `zzzzz`,

    sqrt(5 * 25²) = 25 sqrt(5) ≈ 55.9.

For two independent letters uniform on {0, ..., 25}, the variance of
one letter is (26² - 1)/12 = 56.25 and the variance of the difference is
twice that, 112.5. Summing five coordinates,

    E[d²] = 5 * 112.5 = 562.5,   sqrt(562.5) ≈ 23.7.

Actual SGB words sit closer together than random strings. Over 200000
random pairs of SGB words the mean squared distance is about 486 and the
mean distance about 21.2, because real letters cluster in the common
region of the alphabet (`e`, `s`, `a`, `o`, `r`, `i`; see `stats.md`).

## What the script prints

It draws 100 random pairs with `random.seed(1337)` and prints them
sorted by distance, largest first. The extremes of that sample:

    dizzy cocci  36.76
    ikats lazed  34.41
    ...
    vials shank   8.83
    winey unmet   7.42

## Relation to the diff-by-one problem

The pairs in `diff_by_n.md` differ by exactly ±1 in every position, so
they all lie at distance sqrt(5). The converse fails: squared distance 5
also arises from the pattern (±2, ±1, 0, 0, 0), since 4 + 1 = 5. The
SGB has 38 pairs of the first kind and 1532 of the second (`abuse
cause`, `acked baked`, ...). A filter on Euclidean distance alone
therefore cannot isolate the exercise-28 pairs, which is why
`diff_by_n.py` generates candidates position by position instead.
