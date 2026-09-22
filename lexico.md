# Words whose letters are in alphabetical order

Knuth, *The Art of Computer Programming*, Volume 4A, Section 7,
exercise 30: each letter of the word `first` appears in correct
lexicographic order. Find the first and last such words in the SGB.
Code: `lexico.py`. The mirror-image problem is in `reverse_lexico.md`.

## The test

A word is *sorted* if w₀ ≤ w₁ ≤ w₂ ≤ w₃ ≤ w₄. Because ≤ is transitive,
checking the four adjacent pairs is enough:

    all(a <= b for a, b in zip(word, word[1:]))

Ties are allowed, so `abbey` and `bells` count. Requiring strict
inequality would give a different, smaller set (below).

## Results

The script sorts the list alphabetically first, since "first" and
"last" in the exercise mean alphabetical, not the frequency order of
the file (see `get_words.md`).

| | |
|---|---|
| sorted words | 105 |
| first | `abbey` |
| last | `pssst` |

`first` itself is one of the 105. The list runs from `abbey`, `abbot`,
`abhor` through `floor`, `flops`, `forty`, `ghost` to `moors`, `mossy`,
`pssst`. Nothing begins later than `p`: a sorted word starting with `q`
or later needs four more letters from the tail of the alphabet, and
English has none.

## The uniform baseline

A nondecreasing string of length 5 over 26 letters is the same thing as
a multiset of 5 letters: sort the multiset and you get the string,
read the string and you get the multiset. Multisets of size 5 from 26
kinds are counted by stars and bars:

    C(26 + 5 - 1, 5) = C(30, 5) = 142506,

about 1.2% of the 26⁵ = 11881376 strings. Among 5757 uniformly random
strings one would expect 69 sorted ones. The SGB has 105, half again as
many: English favors the pattern, largely because so many words end in
`s`, `t` or `y`, letters late in the alphabet.

The strictly increasing strings, with no repeated letter, correspond to
plain 5-subsets, C(26, 5) = 65780. The SGB has 37 of these:

    abhor abort adept adios adopt aegis aglow befit begin begot below
    blowy ceils chimp chino chins chips chops clops deist deity demos
    dirty empty films filmy first fisty flops forty ghost gimps gimpy
    gipsy glory horsy knops

The remaining 105 - 37 = 68 sorted words each contain at least one
doubled letter (`abbey`, `bells`, `ahhhh`).

## Complexity

One pass, four comparisons per word, plus the O(N log N) sort that
produces alphabetical first and last.
