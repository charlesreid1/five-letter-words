# Complete binary tries in WORDS(n)

Knuth, *The Art of Computer Programming*, Volume 4A, Section 7, exercise
35: which letters of the alphabet can be the starting letter of sixteen
words that form a complete binary trie within WORDS(n)? Code: `tries.py`.

## Tries and the question

A trie stores a set of words by their shared prefixes. The root is a
first letter; its children are the second letters that follow it; a node
at depth k stands for a k-letter prefix, and the words themselves sit at
depth 5. A *complete binary trie* of sixteen five-letter words has one
root letter, two second letters under it, four three-letter prefixes,
eight four-letter prefixes and sixteen words: every internal node has
exactly two children.

WORDS(n) is the first n words of the list, the n most common (see
`get_words.md`). The exercise asks which root letters admit such a trie,
as a function of n. The docstring's example, and the trie found for `s`
in WORDS(1000):

                         s
              h                    t
        e           o          a         e
      e   l       o   r      l   r     a   e
    sheep shelf shook shore stalk stare steal steel
    sheer shell shoot short stall stars steam steep

## Algorithm

`TryTrieTree` does two passes for each (letter, n).

**assemble** builds the tree top down and prunes by a counting
condition. A node at depth k heads a subtree that must eventually hold
2^(5-k) words: 16 under the root, 8 under a second letter, 4 under a
three-letter prefix, 2 under a four-letter prefix. `_assemble` counts
the words of WORDS(n) beginning with the candidate prefix and creates
the node only if the count is at least that many, then recurses on all
26 possible next letters. Depth-4 nodes record their word count and
stop. The condition is necessary, not sufficient: `sh` may head 24
words in WORDS(1000) without those words splitting two by two the whole
way down.

**bubble_up** applies the exact condition from the bottom. It visits
children before parents (a post-order traversal, though the comments
call it pre-order) and sets each interior node's count to the number of
its children whose count is at least 2. By induction a node supports a
complete binary subtree if and only if its count is at least 2: a
four-letter prefix does iff it has 2 words, and a shorter prefix does
iff it has 2 children that do. So the root's count being at least 2 is
the answer for that letter. "At least 2" rather than "exactly 2" is
right because extra branches are harmless; we only need to be able to
choose two.

Each node visit filters the current word list, O(n), and tries 26
letters, but the pruning keeps the tree small and the whole table below
runs in well under a second.

## Results

For the full list, n = 5757, twelve letters admit a complete binary
trie and fourteen do not.

| perfect | b c d f h l m p r s t w |
|---|---|
| not perfect | a e g i j k n o q u v x y z |

Since WORDS(n) grows with n, a letter that is perfect at n stays perfect
for all larger n. The smallest n at which each letter first becomes
perfect:

| letter | s | c | b | d | p | m | w | l | h | f | r | t |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| first n | 978 | 2503 | 2730 | 3999 | 4230 | 4459 | 4709 | 4782 | 4824 | 4840 | 4924 | 5343 |

which produces the table the script prints:

| n | 1000 | 1500 | 2000 | 2500 | 3000 | 3500 | 4000 | 4500 | 5000 | 5500 | 5757 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| perfect tries | 1 | 1 | 1 | 1 | 3 | 3 | 4 | 6 | 11 | 12 | 12 |

`s` is alone until past n = 2500. It begins 724 of the 5757 words, far
more than any other letter (`c` is next with 440), and the `sh`/`st`
split above is already present among the thousand commonest words.

Raw count is not the whole story. `a` begins 296 words and `g` 279, more
than `r` (268) or `h` (239), yet neither `a` nor `g` ever reaches a
complete trie while `r` and `h` do. What matters is depth: a perfect
trie needs eight four-letter stems that each carry two words, and in
English those come from inflection pairs sharing a stem. The `b` trie at
n = 5757 is made entirely of them:

    balds baldy  baled baler  bared barer  barfs barfy
    beads beady  beaks beaky  beefs beefy  beers beery

Vowel-initial words spread across many second letters without stacking
two deep on common stems, so `a`, `e`, `i`, `o`, `u` all fail.
