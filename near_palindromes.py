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

def is_near_palindrome(word,tol):
    test1 = euclidean_distance(word[0],word[4])<=tol
    test2 = euclidean_distance(word[1],word[3])<=tol
    if(test1 and test2):
        return True
    return False

if __name__=="__main__":
    words = get_words()

    knp = 0
    near_palindromes = []

    # Euclidean distance tolerance
    tol = 2.0

    for i in range(len(words)):
        if(is_near_palindrome(words[i],tol)):
            knp += 1
            near_palindromes.append(words[i])

    print("-"*40)
    print("Near Palindromes: \n")
    pprint(near_palindromes)

