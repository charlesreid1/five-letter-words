# five-letter-words

This repository contains Donald Knuth's GraphBase list of five-letter words,
as well as scripts to run various combinatoric experiments, 
graph algorithms, and other algorithms to explore the 
relationships among these words.



The list of words comes from [[1]](http://www-cs-faculty.stanford.edu/~knuth/sgb.html) and is in the public domain.

## Get Words

A Python program that contains a method for getting all of the five letter words from a file,
and that's about it. Notes on the word list itself (size, frequency order, WORDS(n)) are in ```get_words.md```.

```stats.py``` - letter and bigram frequency counts for the whole list. Theory and tables in ```stats.md```.

## Warm Up Exercises

Exercises 26-37 of Knuth's Volume 4 Fascicle 0 are intended as a warm up to get to know
the SGB five letter word list. Solutions to these exercises are listed below.

```distinct.py```- computes the number of SGB words containing exactly k distinct letters.
The Stirling-number baseline and the counts are in ```distinct.md```.

```diff_by_n.py``` - computes the pairs of SGB words that are off by a small shift
in every letter position. An example is `rover` and `spuds`:
each corresponding letter differs by exactly one, `r -> s`, `o -> p`, and so on.
The script uses recursive backtracking to generate the candidate matches for each word
and a hash set to check for their existence in the word list, then repeats for shifts
of up to 2 and up to 3.

There are 38 such pairs in the SGB for a shift of 1, 525 for shifts up to 2,
and 4982 for shifts up to 3. The generate-and-look-up argument is in ```diff_by_n.md```.

Also see [Five Letter Words](https://charlesreid1.com/wiki/Five_Letter_Words)
on the charlesreid1.com wiki, and
[Five Letter Words: Part 4: Revisiting Diff by One](https://charlesreid1.github.io/five-letter-words-part-4-revisiting-diff-by-one.html)
(blog post) on [charlesreid1.github.io](https://charlesreid1.github.io).

```euclidean_distance.py``` - computes the Euclidean distance between two words, treating
each word as a vector of five letter indices (a = 0, ..., z = 25). This is a geometric
distance in letter space, not the string edit distance. See ```euclidean_distance.md```.

```lexico.py``` - find words that are sorted by lexicographic order (front to back, a-z). 
See ```lexico.md```.

```palindromes.py``` - look for five letter words that are either a palindrome, or a palindrome pair.
See ```palindromes.md```.

### Variations

```near_palindromes.py``` - variation on ```palindromes.py``` that finds words one alphabet step
away from a palindrome. See ```near_palindromes.md```.

```reverse_lexico.py``` - variation on ```lexico.py``` that finds words whose letters are in 
reverse lexicographic order. See ```reverse_lexico.md```.

## Letter Coverage

```letter_coverage.py``` - computes coverage of the alphabet (minimum number of words required 
to provide X letters of the alphabet)

Knuth mentions, in the text, a couple of facts about how many words cover how much
of the alphabet. We authored a dynamic program to compute precisely this - given a 
number of letters N from the alphabet, this program computes the minimum number of 
words it takes to cover all N letters.

Also see [Letter Coverage](https://charlesreid1.com/wiki/Letter_Coverage)
page on the charlesreid1.com wiki.

## Prime Strings

```prime_strings.py``` - solves exercises 101, 102, 103 and 104 of Volume 4A Section 7.2.1.1.
A string is *prime* (a Lyndon word) if it is less than all of its proper suffixes.
The script factors any string into nonincreasing primes with Duval's linear-time
algorithm, checks it against a brute-force method, factors the first 40 digits of pi,
and counts the SGB words that are prime: 1274 of 5757. The smallest nonprime is
`abaca` and the largest prime is `rutty`.

It also computes the number of m-ary primes of length n from the Euler product
that the factorization theorem implies, and checks it against brute force, and reads Fermat's theorem off the divisor sum.

Proofs for exercise 101 (a)-(d) and the derivations for 102 and 103 are in ```prime_strings.md```.

# Sources

1. Knuth, Donald. <u>The Stanford GraphBase: A Platform for Combinatorial Computing</u>. New York: ACM Press, 1994. 
<[http://www-cs-faculty.stanford.edu/~knuth/sgb.html](http://www-cs-faculty.stanford.edu/~knuth/sgb.html)>


