# five-letter-words

This repository contains Donald Knuth's GraphBase list of five-letter words,
as well as scripts to run various combinatoric experiments, 
graph algorithms, and other algorithms to explore the 
relationships among these words.



The list of words comes from [[1]](http://www-cs-faculty.stanford.edu/~knuth/sgb.html) and is in the public domain.

## Get Words

A Python program that contains a method for getting all of the five letter words from a file,
and that's about it.

## Warm Up Exercises

Exercises 26-37 of Knuth's Volume 4 Fascile 0 are intended as a warm up to get to know
the SGB five letter word list. Solutions to these exercises are listed below.

```distinct.py```- computes the number of SGB words containing exactly k distinct letters.

```diff_by_one_fixed.py``` - (**fixed 2019-03-09**) computes the number of words in the SGB
that are off by a single letter in each position. An example is `rover` and `spuds`.
Each corresponding letter is only different by one: `r -> s`, `o->p`, and so on.
This uses recursive backtracking to generate possible matches for each word, and 
uses a hash table to check for their existence in the original word set.

There are 38 such pairs in the SGB.

Also see [Five Letter Words](https://charlesreid1.com/wiki/Five_Letter_Words)
on the charlesreid1.com wiki.

```diff_by_n_fixed.py``` - (added 2019-03-10.) using the corrected approach (above) to
computing differences by 1, this generalizes the calculation to words that are different
by a distance `d` for each letter position.

Also see [Five Letter Words: Part 4: Revisiting Diff by One](https://charlesreid1.github.io/five-letter-words-part-4-revisiting-diff-by-one.html)
(blog post) on [charlesreid1.github.io](https://charlesreid1.github.io).

```euclidean_distance.py``` - computes the euclidean distance between two words. This uses
the traditional Euclidean distance definition but reinterprets distance to mean edit distance.

```lexico.py``` - find words that are sorted by lexicographic order (front to back, a-z). 

```palindromes.py``` - look for five letter words that are either a palindrome, or a palindrome pair.

### Variations

```diff_by_n.py``` - computes words in SGB that have an edit distance of n.

```reverse_lexico.py``` - variation on ```lexico.py``` that finds words whose letters are in 
reverse lexicographic order.

## Letter Coverage

```letter_coverage.py``` - computes coverage of the alphabet (minimum number of words required 
to provide X letters of the alphabet)

Knuth mentions, in the text, a couple of facts about how many words cover how much
of the alphabet. We authored a dynamic program to compute precisely this - given a 
number of letters N from the alphabet, this program computes the minimum number of 
words it takes to cover all N letters.

Also see [Letter Coverage](https://charlesreid1.com/wiki/Letter_Coverage)
page on the charlesreid1.com wiki.

# Sources

1. Knuth, Donald. <u>The Stanford GraphBase: A Platform for Combinatorial Computing</u>. New York: ACM Press, 1994. 
<[http://www-cs-faculty.stanford.edu/~knuth/sgb.html](http://www-cs-faculty.stanford.edu/~knuth/sgb.html)>


