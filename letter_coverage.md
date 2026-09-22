# Covering the alphabet with the fewest words

Knuth, *The Art of Computer Programming*, Volume 4A, Section 7, remarks
in the text on how many five-letter words it takes to cover the alphabet.
Code: `letter_coverage.py`. Also see the
[Letter Coverage](https://charlesreid1.com/wiki/Letter_Coverage) page on
the charlesreid1.com wiki.

## The problem

Fix N and take the first N letters of the alphabet, `a` through the
Nth letter. A word *covers* the letters it contains. The question is the
minimum number of words from WORDS(1000), the thousand most common
five-letter words, whose union covers all N letters. The script's
headline case is N = 15, the letters `a` through `o`.

`word2bitvector` turns a word into an N-bit integer with bit i set when
the word contains the ith letter; letters past the Nth are ignored. The
union of two words' coverage is the bitwise OR of their vectors and the
number of letters covered is the popcount.

This is the set cover problem. The universe is the N letters, each word
is a subset of size at most 5, and we want the smallest subfamily whose
union is the universe. Set cover is NP-hard in general, but with a
universe of at most 26 elements the instances here are small enough to
solve exactly.

## Why the obvious dynamic program fails

A tempting approach is to process the words in order and keep, for each
word i, the best chain of words ending at i: its coverage vector, its
letter count and its length, extending the best chain ending at some
earlier j. That recurrence assumes optimal substructure, and set cover
does not have it. The chain kept for j is the one covering the most
letters, but the right predecessor for i may be a chain that covers
fewer letters and complements word i better. Keeping one state per j
throws those alternatives away. On WORDS(1000) such a program reports 8
words for N = 15 and 15 words for the full alphabet, twice the true
minimum in both cases.

Exact dynamic programming over the 2^N subsets of covered letters does
work (2^15 = 32768 states, one pass per word), but a branch and bound
search is simpler and fast enough for N = 26, where 2^26 states would
not be.

## Branch and bound

`min_cover` first collapses the words to one representative per distinct
coverage pattern, then searches:

1. If every coverable letter is covered, record the solution if it is
   the shortest so far.
2. Otherwise bound: each word adds at most 5 letters, so if the words
   chosen so far plus ⌈uncovered / 5⌉ cannot beat the best solution,
   stop.
3. Otherwise pick the uncovered letter contained in the fewest words
   (the most constrained choice), and branch on each of those words.

Branching on the rarest letter is what makes this fast. Only 4 of the
5757 words contain `x` as a first letter, 138 contain it anywhere, and
`j`, `q`, `z` are similarly scarce, so the top of the search tree has a
few dozen branches rather than a thousand. The whole table below,
twenty-two values of N plus two full-alphabet runs, takes under two
seconds.

## Results

Minimum covers of `a` through the Nth letter from WORDS(1000):

| N | words | a minimum cover |
|---|---|---|
| 5 | 2 | about cried |
| 6 | 2 | about faced |
| 7 | 2 | being faced |
| 8 | 3 | right about faced |
| 10 | 3 | judge about chief |
| 12 | 3 | judge black fight |
| 13 | 4 | major right black field |
| 15 | 4 | major think globe faced |
| 16 | 4 | major being flock hoped |
| 17 | 5 | quite major being flock hoped |
| 20 | 5 | quite major black fight spend |
| 22 | 5 | quick major verbs flung depth |
| 24 | 6 | quite jokes fixed woven climb graph |
| 25 | 6 | quite jumps fixed heavy black wrong |
| 26 | 7 | dozen quite jumps waxes every black fight |

Minimum covers are rarely unique. `major think globe faced` covers `a`
through `o` (and `t` and `k` besides); so does `major right blank
faced`.

## Lower bounds and the full list

Five letters per word gives the bound ⌈N / 5⌉. For N = 26 that is 6,
and the full SGB list achieves it:

    quite jumps whizz bronx gyved flack

No five SGB words cover 25 letters. Five words have exactly 25 letter
slots, so that would require five words with no letter repeated
anywhere among them, and the list contains no such quintuple. The
restriction to WORDS(1000) costs one more word (7): the rare letters
`j`, `q`, `x`, `z` occur in only a handful of common words (`judge`,
`jumps`, `quite`, `waxes`, `dozen`), and those overlap heavily in their
other letters.
