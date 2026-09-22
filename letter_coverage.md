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
five-letter words, whose union covers all N letters. The script runs
with N = 15, so the target is `a` through `o`.

`word2bitvector` turns a word into a length-N boolean array with a 1 at
each letter the word contains; letters past the Nth are dropped, which
is what the `IndexError` guard does. The union of two words' coverage is
the logical OR of their vectors and the number of letters covered is
the number of 1s.

This is the set cover problem. The universe is the N letters, each word
is a subset of size at most 5, and we want the smallest subfamily whose
union is the universe. Set cover is NP-hard in general, but with a
universe of at most 26 elements the instances here are small enough to
solve exactly.

## What the script computes

The script processes the words in list order and, for each word i,
stores a single state describing the best chain of words that ends at i:

- `bestcoverage_bv[i]`, the coverage vector of that chain;
- `ones_bv[i]`, its number of covered letters;
- `ws[i]`, its number of words;
- `bt[i]`, the previous word in the chain, for backtracking.

Word 0 starts a chain by itself. For each later word i the script first
assumes i stands alone, then tries every earlier word j as a
predecessor: the candidate is `wi_bv OR bestcoverage_bv[j]` with
`ws[j] + 1` words, and it replaces the current state for i if it covers
more letters, or the same number with fewer words. At the end the word
with the most covered letters (fewest words among ties) is chosen and
the chain is read back through `bt`.

For N = 15 the script reports

    Takes 8 words to cover 15 letters (a, ..., o)
    which their about could after right think major

Cost: every pair j < i is examined once, N-length OR each time, so
O(n² N) with n = 1000 words.

## Why this is not the minimum

The recurrence assumes optimal substructure: that the best chain ending
at i extends the best chain ending at some j. That fails here. The chain
kept for j is the one covering the *most* letters, but the right
predecessor for i may be a chain that covers fewer letters and
complements word i better. Since only one vector is kept per j, those
alternatives are thrown away. The result is a heuristic that always
covers all N letters (any chain can be extended until it does) but uses
more words than necessary. Every answer it produces starts with `which`,
the first word in the list, because that is the seed every chain is
built on.

An exact solver settles the question. Branch on the uncovered letter
that appears in the fewest remaining words, try each of those words,
and prune when the words chosen so far plus ⌈uncovered / 5⌉ cannot beat
the best cover found. Because the universe is tiny this finishes in a
fraction of a second for every N. Comparing the two on WORDS(1000):

| N | script | minimum | a minimum cover |
|---|---|---|---|
| 5 | 2 | 2 | about cried |
| 6 | 4 | 2 | about faced |
| 7 | 5 | 2 | being faced |
| 8 | 5 | 3 | right about faced |
| 10 | 6 | 3 | judge about chief |
| 12 | 7 | 3 | judge black fight |
| 13 | 8 | 4 | major right black field |
| 15 | 8 | 4 | major think globe faced |
| 16 | 8 | 4 | major being flock hoped |
| 17 | 11 | 5 | quite major being flock hoped |
| 20 | 11 | 5 | quite major black fight spend |
| 22 | 12 | 5 | quick major verbs flung depth |
| 24 | 13 | 6 | quite jokes fixed woven climb graph |
| 25 | 14 | 6 | quite jumps fixed heavy black wrong |
| 26 | 15 | 7 | dozen quite jumps waxes every black fight |

The 15-letter case the script prints, 8 words, is twice the true
minimum of 4: `major think globe faced` covers `a` through `o` exactly
(and `t` and `k` besides). The gap widens with N; the whole alphabet
needs 7 words from WORDS(1000), where the script uses 15.

## Lower bounds and the full list

Five letters per word gives the trivial bound of ⌈N / 5⌉ words. For
N = 26 that is 6, and the full SGB list achieves it:

    quite jumps whizz bronx gyved flack

No five SGB words cover 25 letters. Five words have exactly 25 letter
slots, so that would require five words with no letter repeated
anywhere among them, and the list contains no such quintuple. The
restriction to WORDS(1000) costs one more word (7) because the rare
letters `j`, `q`, `x`, `z` sit in only a handful of common words
(`judge`, `jumps`, `quite`, `waxes`, `dozen`), and those few words
overlap heavily in their other letters.
