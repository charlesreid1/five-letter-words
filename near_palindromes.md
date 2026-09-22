# Near palindromes

Variation on Knuth, *The Art of Computer Programming*, Volume 4A,
Section 7, exercise 29: find SGB words that are a small step away from
being a palindrome. Code: `near_palindromes.py`. The exact problem is in
`palindromes.md`.

## Measuring distance from a palindrome

Write the alphabet as the number line a = 0, ..., z = 25, as
`euclidean_distance.md` does. For a five-letter word the two mirror
pairs are (w₀, w₄) and (w₁, w₃); the middle letter mirrors itself. Set

    d₁ = |w₀ - w₄|,   d₂ = |w₁ - w₃|,   D(w) = d₁ + d₂.

D(w) = 0 exactly when w is a palindrome. In general D(w) is the least
number of single alphabet steps (changing one letter to an adjacent
letter) needed to turn w into a palindrome: shift w₀ toward w₄ by d₁
steps and w₁ toward w₃ by d₂ steps, and nothing cheaper works because
each step changes one of d₁, d₂ by at most one. Equivalently D(w) is
half the L¹ distance between w and its reverse.

The script declares w a near palindrome when

    lo < D(w) ≤ hi,   with lo = 0 and hi = 1.

So as configured it selects the words with D(w) = 1: one mirror pair
matches exactly and the other is off by a single alphabet step. The
docstring speaks of "one or two letters"; raising `hi` to 2 admits the
D = 2 words as well.

## Results

| hi | words with 0 < D ≤ hi |
|---|---|
| 1 | 37 |
| 2 | 110 |
| 3 | 188 |

The 37 words at D = 1:

    going seeds tight trust suits sends plump slums sighs erase serfs
    soaps sewer soups sever slams scabs moron ceded scads suets fugue
    seder tryst educe twixt tutus shags slims abaca anima celeb selfs
    scuds tikis topos rajas

`going` has g...g and o..n, one step apart; `tight` has t...t and i..h;
`erase` has e...e and r..s.

## The uniform baseline

Count the strings with D = 1. One mirror pair is equal (26 choices) and
the other is adjacent in the alphabet (25 unordered adjacent pairs, 2
orders, 50 choices); either pair can be the adjacent one (factor 2) and
the middle letter is free (26):

    2 * 26 * 50 * 26 = 67600,

about 0.57% of all strings, an expected 33 among 5757 random strings.
The SGB has 37, close to the baseline. Unlike exact palindromes, which
English overproduces by a factor of two, near misses are no more common
in real words than in random ones.

## Complexity

One pass with two subtractions per word, O(N).
