# Palindromes and palindrome pairs

Knuth, *The Art of Computer Programming*, Volume 4A, Section 7,
exercise 29: find all SGB words that are palindromes (`kayak`) or that
form palindrome pairs (`regal lager`). Code: `palindromes.py`. The
loosened version is in `near_palindromes.md`.

## Reversal as an involution

Let ρ(w) be the reverse of w. Applying ρ twice gives w back, so ρ is an
involution on the set of all five-letter strings. An involution splits
its domain into fixed points and two-element orbits:

- **fixed points**, ρ(w) = w: palindromes;
- **orbits {w, ρ(w)}** with both members in the word list: palindrome
  pairs.

For a five-letter word ρ(w) = w means w₀ = w₄ and w₁ = w₃. The middle
letter w₂ pairs with itself and is unconstrained, which is why
`is_palindrome` makes only two comparisons. A palindrome pair needs all
five positions to match crosswise, w₀ = v₄, w₁ = v₃, w₂ = v₂, w₃ = v₁,
w₄ = v₀, which is what `is_palindrome_pair` checks.

## Results

| | |
|---|---|
| palindromes | 18 |
| palindrome pairs | 34 |
| words in some pair | 68 |

The palindromes, in the frequency order of the list:

    level refer radar madam rotor civic sexes solos sagas kayak minim
    tenet shahs stats stets kaiak finif dewed

The pairs begin `parts strap`, `lived devil`, `speed deeps`, `sleep
peels`, `straw warts`, `faced decaf`, `spots stops`, and end `hales
selah`, `tarps sprat`. Each is printed with the more common word first,
a side effect of the loop order (see `get_words.md`).

Knuth's example `regal lager` is among them, printed as `regal, lager`
since `regal` is the more common word.

## The uniform baseline

A palindromic five-letter string is determined by its first three
letters, so there are 26³ = 17576 of them, one in every 26² = 676
strings. Among 5757 random strings one expects 8.5 palindromes. The SGB
has 18, about twice that. English is fond of the consonant-vowel-
consonant-vowel-consonant shape with matching consonants (`level`,
`radar`, `rotor`, `civic`, `minim`, `tenet`).

For pairs the baseline is much smaller. Given a non-palindromic word, its
reverse is one specific string out of 26⁵, and the chance that a
uniformly random list of 5757 strings contains it is about
5757 / 11881376 ≈ 0.0005, so one would expect roughly 1.4 pairs. The
SGB has 34. Reversal preserves the vowel-consonant skeleton, and
English endings like `-s` and `-ed` reverse into common beginnings
like `s-` and `de-` (`spots stops`, `faced decaf`, `lived devil`).

## Complexity

Palindromes take one pass, O(N). The script finds pairs by comparing
every word to every later word, N(N - 1)/2 ≈ 16.6 million calls, which
is O(N²). The involution view gives an O(N) alternative: put the words
in a set and test `word[::-1] in words` for each word, keeping the pair
when the reverse is present and differs from the word. The `i != j`
guard in the script does the same job of excluding the 18 palindromes,
whose reverse is themselves.
