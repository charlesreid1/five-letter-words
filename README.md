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

```distinct.py'```- computes the number of SGB words containing exactly k distinct letters.

```diff_by_one.py``` - computes the number of words in the SGB that are off by a single letter,
shifted a single place. For example, "might" and "night" or "large" and "marge". There is a 
surprisingly large number of such pairs.

```euclidean_distance.py``` - computes the euclidean distance between two words. This uses
the traditional Euclidean distance definition but reinterprets distance to mean edit distance.

```lexico.py``` - find words that are sorted by lexicographic order (front to back, a-z). 

```palindromes.py``` - look for five letter words that are either a palindrome, or a palindrome pair.


## Letter Coverage

Knuth mentions, in the text, a couple of facts about how many words cover how much
of the alphabet. We authored a dynamic program to compute precisely this - given a 
number of letters N from the alphabet, this program computes the minimum number of 
words it takes to cover all N letters.

Also see [https://charlesreid1.com/wiki/Letter_Coverage](https://charlesreid1.com/wiki/Letter_Coverage)..

# Sources

1. Knuth, Donald. <u>The Stanford GraphBase: A Platform for Combinatorial Computing</u>. New York: ACM Press, 1994. 
<[http://www-cs-faculty.stanford.edu/~knuth/sgb.html](http://www-cs-faculty.stanford.edu/~knuth/sgb.html)>



