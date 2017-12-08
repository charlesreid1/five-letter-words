"""
near_palindromes.py

Donald Knuth, Art of Computer Programming, Volume 4 Facsimile 0
Variation on Exercise #29

Find SGB words that are near-palindromes
(edit distance of one or two letters away from a palindrome).
"""
from get_words import get_words
from euclidean_distance import euclidean_distance
from pprint import pprint

def is_near_palindrome(word,lo,hi):
    d1 = euclidean_distance(word[0],word[4])
    d2 = euclidean_distance(word[1],word[3])

    if( (d1+d2) > lo and (d1+d2) <= hi ):
        return True

    return False

if __name__=="__main__":
    words = get_words()

    knp = 0
    near_palindromes = []

    # Euclidean distance tolerance
    lo = 0.0
    hi = 1.0

    for i in range(len(words)):
        if(is_near_palindrome(words[i],lo,hi)):
            knp += 1
            near_palindromes.append(words[i])

    print("-"*40)
    print("Near Palindromes: \n")
    print(", ".join(near_palindromes))
    print("The number of near-palindromes is {0:d}".format(len(near_palindromes)))

