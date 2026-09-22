# Words with exactly k distinct letters

Knuth, *The Art of Computer Programming*, Volume 4A, Section 7,
exercise 27: how many SGB words contain exactly k distinct letters, for
1 ≤ k ≤ 5? Code: `distinct.py`.

## The count

`len(set(word))` is the number of distinct letters in a word. The script
buckets every word by that number.

| k | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| SGB words | 0 | 4 | 163 | 1756 | 3834 |

The four two-letter words are `mamma`, `ahhhh`, `esses` and `ohhhh`. No
English five-letter word repeats a single letter five times.

## The uniform baseline

How many five-letter *strings* over a 26-letter alphabet use exactly k
distinct letters? Build one in three steps: choose which k letters
appear, partition the 5 positions into k nonempty blocks, and assign the
k letters to the k blocks bijectively. The number of ways to partition
an n-set into k nonempty blocks is the Stirling number of the second
kind S(n, k), so

    strings with exactly k distinct letters = C(26, k) * k! * S(5, k) = 26^(k falling) * S(5, k),

where 26^(k falling) = 26 * 25 * ... * (26 - k + 1) is the falling
factorial. The Stirling numbers S(5, k) for k = 1..5 are 1, 15, 25, 10,
1, and the identity

    x^n = Σ_k S(n, k) x^(k falling)

with x = 26 and n = 5 confirms that the five counts add up to
26⁵ = 11881376.

| k | S(5,k) | strings | fraction | expected of 5757 | actual |
|---|---|---|---|---|---|
| 1 | 1 | 26 | 0.0000022 | 0.01 | 0 |
| 2 | 15 | 9750 | 0.00082 | 4.7 | 4 |
| 3 | 25 | 390000 | 0.0328 | 189 | 163 |
| 4 | 10 | 3588000 | 0.3020 | 1739 | 1756 |
| 5 | 1 | 7893600 | 0.6644 | 3825 | 3834 |

The "expected" column is what 5757 uniformly random strings would give.
English words track the random model closely on this statistic: the
letter distribution is skewed (see `stats.md`), which should make
repeats more likely, but English also avoids most doubled and tripled
letters, and the two effects nearly cancel.

## Complexity

One pass over the list, five characters per word: O(5N) time and O(N)
space for the buckets. The script prints the first five words of each
bucket, which by the frequency order of the list are the most common
words with that many distinct letters (`which`, `there`, `these` for
k = 4; `their`, `about`, `would` for k = 5).
