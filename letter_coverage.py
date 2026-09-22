"""
letter_coverage.py

Compute the minimum number of words from five-letter-words
needed to cover the first N letters of the alphabet.

This is a set cover problem: the universe is the N letters, each word
is a subset of at most five of them. Set cover is NP-hard in general,
but the universe here has at most 26 elements, so an exact branch and
bound search finishes in a fraction of a second. Branch on the
uncovered letter that appears in the fewest words, and prune when the
words chosen so far plus ceil(uncovered / 5) cannot beat the best
cover found.

https://charlesreid1.com/wiki/Five_Letter_Words
https://charlesreid1.com/wiki/Letter_Coverage
"""
from get_words import get_words


def word2bitvector(word, N):
    """
    Turn a word into an integer bit vector representing letter coverage
    of the first N letters of the alphabet. Letters past the Nth are
    ignored.
    """
    bv = 0
    for c in word:
        i = ord(c) - ord('a')
        if i < N:
            bv |= 1 << i
    return bv


def printbv(bv, N):
    """
    Pretty printing for bit vector: a 1 for each letter covered, a to z.
    """
    return "".join("1" if bv >> i & 1 else "0" for i in range(N))


def popcount(bv):
    return bin(bv).count("1")


def min_cover(words, N):
    """
    Return (covered, solution): the set of letters among the first N
    that any word covers, and a shortest list of words covering all of
    them.
    """
    # One representative word per distinct coverage pattern.
    by_pattern = {}
    for w in words:
        bv = word2bitvector(w, N)
        if bv and bv not in by_pattern:
            by_pattern[bv] = w
    patterns = list(by_pattern.items())

    # Words containing each letter, and the letters that can be covered at all.
    by_letter = [[(bv, w) for bv, w in patterns if bv >> i & 1] for i in range(N)]
    target = 0
    for i in range(N):
        if by_letter[i]:
            target |= 1 << i

    best = [len(patterns) + 1, None]

    def search(covered, chosen):
        if covered & target == target:
            if len(chosen) < best[0]:
                best[0] = len(chosen)
                best[1] = list(chosen)
            return

        remaining = popcount(target & ~covered)
        if len(chosen) + (remaining + 4) // 5 >= best[0]:
            return

        # Most constrained uncovered letter: fewest words contain it.
        uncovered = [i for i in range(N) if target >> i & 1 and not covered >> i & 1]
        i = min(uncovered, key=lambda i: len(by_letter[i]))

        for bv, w in by_letter[i]:
            chosen.append(w)
            search(covered | bv, chosen)
            chosen.pop()

    search(0, [])
    return target, best[1]


def report(words, N, label):
    covered, solution = min_cover(words, N)
    letters = ", ".join(chr(ord('a') + i) for i in range(N) if covered >> i & 1)
    print("Takes {0:d} words to cover {1:d} letters ({2:s}) from {3:s}".format(
        len(solution), popcount(covered), letters, label))
    print(solution)
    print("")


if __name__ == "__main__":

    words = get_words()

    # Searching for words covering first N letters
    N = 15

    report(words[:1000], N, "WORDS(1000)")

    # The whole alphabet
    report(words[:1000], 26, "WORDS(1000)")
    report(words, 26, "WORDS(5757)")

    # Minimum cover for each N, from WORDS(1000)
    print("{0:>3s}  {1:>5s}  {2:s}".format("N", "words", "cover"))
    for N in range(5, 27):
        covered, solution = min_cover(words[:1000], N)
        print("{0:3d}  {1:5d}  {2:s}".format(N, len(solution), " ".join(solution)))
