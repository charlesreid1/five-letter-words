"""
near_palindromes.py

Donald Knuth, Art of Computer Programming, Volume 4 Facsimile 0
Variation on Exercise #29

Find SGB words that are near-palindromes
(edit distance of one or two letters away from a palindrome).
"""
from get_words import get_words
def is_near_palindrome(word,lo,hi):
    d1 = abs(ord(word[0]) - ord(word[4]))
    d2 = abs(ord(word[1]) - ord(word[3]))
    return lo < (d1 + d2) <= hi

if __name__=="__main__":
    words = get_words()

    # Euclidean distance tolerance
    lo = 0.0
    hi = 1.0

    near_palindromes = [w for w in words if is_near_palindrome(w, lo, hi)]

    print("-"*40)
    print("Near Palindromes: \n")
    print(", ".join(near_palindromes))
    print("The number of near-palindromes is {0:d}".format(len(near_palindromes)))

