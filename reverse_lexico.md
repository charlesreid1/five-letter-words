# Words whose letters are in reverse alphabetical order

Variation on Knuth, *The Art of Computer Programming*, Volume 4A,
Section 7, exercise 30. Each letter of `spied` appears in reverse
lexicographic order; find all such SGB words. Code: `reverse_lexico.py`.
The original problem is in `lexico.md`.

## The test

A word is *reverse sorted* if w₀ ≥ w₁ ≥ w₂ ≥ w₃ ≥ w₄, checked on the
four adjacent pairs:

    all(a >= b for a, b in zip(word, word[1:]))

## Results

| | |
|---|---|
| reverse sorted words | 37 |
| first (alphabetically) | `mecca` |
| last (alphabetically) | `zoned` |

The full list:

    mecca offed ohhhh plied poked poled polka skied skiff sniff soled
    solid sonic speed spied spiff spoke spoof spook spool spoon toked
    toned tonic treed tried troll unfed upped urged vroom wheee wooed
    wrong yoked yucca zoned

Of these, 19 are strictly decreasing with no repeated letter:

    plied poked poled polka skied soled solid sonic spied spoke toked
    toned tonic tried unfed urged wrong yoked zoned

## Symmetry, and where it breaks

The map c → 'z' - c that sends `a` to `z`, `b` to `y`, and so on,
reverses the order of the alphabet, so it carries nondecreasing strings
onto nonincreasing ones bijectively. Over uniformly random strings the
two problems have identical counts: C(30, 5) = 142506 strings, an
expected 69 of 5757.

English is not symmetric under this map. The SGB has 105 sorted words
but only 37 reverse sorted ones. The common endings `-s`, `-t`, `-y`
put late letters last and help the sorted case; the reverse sorted
words lean on the ending `-ed` (d < e) after a middle letter later than
`e`, as in `poked`, `toned`, `tried`, `speed`, plus initial `s`, `t`,
`w` followed by a vowel and a descent.

## Disjointness

A word that is both sorted and reverse sorted has all its letters equal.
There is no such word in the SGB (`distinct.md` counts zero words with
one distinct letter), so the two lists are disjoint, 105 + 37 = 142
words in all.
