# Letter and bigram frequencies

Warm-up statistics for the SGB word list. Code: `stats.py`.

## What is counted

Two `Counter`s over the whole list:

- **letters**: every character of every word, 5757 * 5 = 28785 slots.
- **bigrams**: every adjacent pair `word[i:i+2]`, 4 per word, 23028
  slots, out of 26² = 676 possible bigrams.

Both are printed sorted by count, smallest first, so the rare items
come at the top of the output and the common ones at the bottom.

## Letters

Under a uniform model each letter would fill 28785 / 26 ≈ 1107 slots.
The actual distribution is far from uniform:

| letter | s | e | a | o | r | i | l | t | ... | x | z | j | q |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| count | 3033 | 3009 | 2348 | 1915 | 1910 | 1592 | 1586 | 1585 | ... | 139 | 135 | 89 | 53 |

The entropy of the letter distribution is 4.31 bits against a maximum
of log₂ 26 ≈ 4.70 bits, so about 0.39 bits per letter are "spent" on
the skew.

This is a *type* frequency, not the *token* frequency of running English
text. Each word counts once no matter how often it is used, so the
familiar running-text order `e t a o i n s h r d l u` shifts. The
biggest shift is `s`, which edges out `e` for first place: 1764 of the
5757 words end in `s`, mostly plurals and third-person verb forms, and
the list treats `part` and `parts` as unrelated entries.

## Bigrams

Only 433 of the 676 possible bigrams occur at all, and 40 of those occur
exactly once (`ml`, for instance). A uniform model would give
23028 / 676 ≈ 34 per bigram. The top of the distribution:

| bigram | es | er | ed | re | in | ar | ts | le |
|---|---|---|---|---|---|---|---|---|
| count | 433 | 425 | 352 | 282 | 273 | 267 | 229 | 225 |

`es`, `er` and `ed` are the English inflectional endings again; 302
words end in `ed`. The counter does not record position, so `es` in
`bakes` and in `eskar` land in the same bucket.

## Why it is here

The skew in these tables is what the later exercises push against. The
combinatorial baselines in `distinct.md`, `lexico.md` and
`palindromes.md` assume uniformly random letters, and the gap between
those baselines and the real counts is a measure of how much English
structure the word list carries.
