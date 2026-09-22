# The SGB word list

Knuth, *The Stanford GraphBase*, `words.dat`, and *The Art of Computer
Programming*, Volume 4A, Section 7, exercises 26-37. Code: `get_words.py`.

## What the file is

`sgb-words.txt` holds 5757 five-letter English words, one per line, all
lowercase, no duplicates, drawn from Knuth's Stanford GraphBase. Every
one of the 26 letters occurs somewhere in the list, so the alphabet for
these experiments is the full a-z.

    words        5757
    letter slots 28785   (5757 * 5)
    alphabet     26

## Order matters

The list is not alphabetical. It begins

    which there their about would these other words could write first water

and ends

    hypos assed spumy osier roble rumba biffy pupal

Knuth sorted the words roughly by frequency of use, most common first,
and writes WORDS(n) for the first n of them: the n most common five-letter
words. Several exercises are parametrized by n this way. `tries.py`
takes `words[:n]` to build WORDS(n), and `letter_coverage.py` works on
WORDS(1000) for speed. Any script that reports "first" or "last" in
alphabetical terms sorts the list itself first; `lexico.py` does this.

The frequency order also shows up in output that lists pairs. In
`palindromes.py` the pair loop runs j from i upward, so each pair is
printed with the more common word first (`parts, strap`; `lived,
devil`).

## What the function does

`get_words()` opens the file and returns `f.read().splitlines()`, a
list of 5757 strings with the newlines stripped. `readlines()` would
keep a trailing `\n` on every word, which would silently corrupt the
scripts downstream: `distinct.py` would count the newline as a sixth
letter, `lexico.py` would reject every word because `\n` sorts before
`a`, and the set lookups in `diff_by_n.py` would never match. Index
based checks like `word[0] == word[4]` would still pass, which is what
makes the bug silent. So the script uses `splitlines()`.

Every other script imports this one function and does its work on the
resulting list, or on `set(get_words())` when it needs O(1) membership
tests, as `diff_by_n.py` does.
