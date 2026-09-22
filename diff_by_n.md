# Word pairs that differ by ±n in every position

Variation on Knuth, *The Art of Computer Programming*, Volume 4A,
Section 7, exercise 28. Find pairs of SGB words whose letters differ at
every position by a small alphabet shift. Code: `diff_by_n.py`.

## The problem

Treat a word as a vector in {0, ..., 25}⁵ as in
`euclidean_distance.md`. Two words v, w are *off by n* if

    1 ≤ |vᵢ - wᵢ| ≤ n   for every i = 0, ..., 4.

Every position must change (Hamming distance 5) and no position may
move more than n alphabet steps (Chebyshev distance at most n). The
sets are nested: off by 1 implies off by 2 implies off by 3. The n = 1
case is the diff-by-one problem: `rover` and `spuds` are such a pair,

    r o v e r
    s p u d s
    + + - - +

with every letter shifted by exactly one.

## Generate and look up

Comparing all N(N - 1)/2 ≈ 16.6 million pairs would work, but the
constraint is so tight that it is cheaper to generate the candidates.
At each of the five positions the other word's letter is one of the 2n
values wᵢ ± 1, ..., wᵢ ± n, so a word has at most

    (2n)⁵   candidates:   32 for n = 1,   1024 for n = 2,   7776 for n = 3.

`gen_variations` builds them by recursive backtracking, one position
per level of recursion, appending each of the 2n shifted characters to
the fragment built so far and recursing to the next position. At depth
5 the fragment is complete and goes into a set. Some candidates fall
off the ends of the alphabet (`chr(ord('a') - 1)` is a backquote); they
are harmless because they can never be in the word list.

The word list is held as a `set`, so each candidate is checked in O(1)
time. Total work is O(N (2n)⁵) set lookups, about 184 thousand for
n = 1 against 16.6 million pairwise comparisons.

Each pair is found twice, once from each end. The script normalizes to
(min, max) before adding to a set, so unordered pairs are counted once.

## Results

| n | pairs | candidates per word | time |
|---|---|---|---|
| 1 | 38 | 32 | 0.06 s |
| 2 | 525 | 1024 | 1.2 s |
| 3 | 4982 | 7776 | 8.2 s |

The 38 diff-by-one pairs begin `abaft babes`, `absit baths`, `adder
beefs`, `ambit blahs`, `anger boffs`, `anode boned`, ..., `ghost hints`,
and `rover spuds` is among them. The time column grows in step with the
candidate count, as the analysis predicts.

## Remarks

The count 38 for n = 1 is the figure quoted in the README for the
earlier `diff_by_one` scripts, which this program supersedes. As n grows
toward 25 the shift constraint disappears and the count approaches the
number of SGB pairs with Hamming distance 5, that is, pairs sharing no
letter in any position.

Distance sqrt(5) in the Euclidean sense is necessary but not sufficient
for n = 1; see `euclidean_distance.md` for the 1532 pairs of the other
shape.
