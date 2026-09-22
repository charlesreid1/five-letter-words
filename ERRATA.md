# Errata

Bugs fixed on the `fixup-md` branch, most recent first. Commit hashes
refer to that branch; `git show <hash>` gives the diff.

## Correctness

### `letter_coverage.py` did not compute the minimum

**Fixed in `757a9ed`.** The original script kept, for each word i, one
"best chain of words ending at i", extended from the best chain ending
at some earlier word j. Set cover has no optimal substructure of that
shape: the chain kept at j maximizes covered letters, but the right
predecessor for i may be a chain that covers fewer letters and
complements i better. Keeping one state per j threw those alternatives
away, so every answer was a heuristic upper bound rather than the
minimum.

On WORDS(1000) the old script reported 8 words for `a` through `o` when
4 suffice (`major think globe faced`), and 15 words to cover the whole
alphabet when 7 suffice. Rewritten as an exact branch and bound set
cover that branches on the uncovered letter contained in the fewest
words and prunes with the ⌈uncovered / 5⌉ bound. Finishes in under two
seconds on the full N = 5 to 26 table. `numpy` is no longer used;
`requirements.txt` was removed in the same commit.

## Documentation

### `get_words.md` misdescribed the `readlines()` failure

**Fixed in `c1807c7`.** The writeup said keeping a trailing `\n` would
"silently break every comparison of `word[4]` downstream". Index checks
like `word[0] == word[4]` still pass on `'level\n'`, which is what
makes the bug silent in the first place. The real casualties are the
distinct-letter count (which sees `\n` as a sixth letter), the lexico
test (`\n` sorts before `a`, so every word fails), and the set lookups
in `diff_by_n.py` (a candidate `'spuds'` never matches the entry
`'spuds\n'`). Rewritten to name those cases.

### `stats.md` used a non-SGB example

**Fixed in `c1807c7`.** The bigram example contrasted `bakes` and
`eskar` to illustrate that `stats.py` ignores position. `eskar` is not
in the SGB word list. Replaced with `beset`, which is.

### `palindromes.md` said Knuth's example was not in the SGB

**Fixed in `83e1f75`, in the same commit that added the writeup.**
Initial draft asserted "Knuth's example `regal lager` is not among them:
neither word is in the SGB." Both words are in the SGB, and the pair is
printed by `palindromes.py`. Caught by a spot check before that first
commit landed, so the incorrect sentence was never in a released state,
but noted here for the record.

### `near_palindromes.py` docstring overstated the code's scope

**Fixed in `c0c313a`.** The docstring said the script finds words
"edit distance of one or two letters away from a palindrome". The code
selects words with `0 < d1 + d2 <= 1`, that is, exactly one alphabet
step from a palindrome. Docstring rewritten to match the code; the
writeup already described the actual behavior. `near_palindromes.md`
no longer contrasts itself with the old docstring.

### `tries.py` mislabeled its traversal

**Fixed in `c0c313a`.** Three comments in `bubble_up` called the
bottom-up pass a pre-order traversal. It visits children before
parents, which is post-order. Corrected in place. The algorithm itself
was fine; only the labels were wrong.

### `euclidean_distance.py` module docstring was misplaced

**Fixed in `c0c313a`.** The docstring sat below the imports, so
Python did not treat it as the module docstring, and it named the
old filename `euclidean_dist.py`. Moved to the top of the file and
retitled.

### Stale README references to removed scripts

**Fixed in `71894fa`.** The README described `diff_by_one_fixed.py`
(removed 2024) and `diff_by_n_fixed.py` (removed 2024), and it called
Euclidean distance "reinterpreted to mean edit distance", which
`euclidean_distance.py` does not do. The two removed scripts are folded
into one entry for `diff_by_n.py`, and the Euclidean line now says
"geometric distance in letter space, not the string edit distance".
"Fascile" -> "Fascicle".

## Cleanups

### `diff_by_n.py` read the word file twice

**Fixed in `c0c313a`.** `main()` had

    words = get_words()
    #words = words[:1000]
    words = set(get_words())

The first assignment is immediately overwritten by the second, which
also re-reads the file. Collapsed to a single call.

### `letter_coverage.py` had an unused helper

**Fixed in `c0c313a`.** `printbv` was left over from the numpy-based
rewrite of the coverage script and had no remaining callers. Removed.

### Stale extensionless snapshots in `output/`

**Fixed in `1d090aa`.** `output/` held seven files without extensions
(`distinct`, `lexico`, `palindromes`, `near_palindromes`,
`reverse_lexico`, `stats`, and `diff_by_one`) from a much older run.
Six were superseded by the `.txt` twins that `run_all.sh` writes; the
seventh, `diff_by_one`, was output from a script that had itself been
removed. All seven deleted from git.
