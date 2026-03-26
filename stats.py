"""
stats.py 

Compute statistics of the 5-letter word collection from the Stanford GraphBase.
"""
from collections import Counter
from pprint import pprint
from get_words import get_words

if __name__=="__main__":

    words = get_words()

    letters = Counter(c for word in words for c in word)
    bigrams = Counter(a + b for word in words for a, b in zip(word, word[1:]))
    
    sorted_letters = sorted(letters.items(), key=lambda x: x[1])
    sorted_bigrams = sorted(bigrams.items(), key=lambda x: x[1])
    
    print("\n\n")
    pprint(sorted_letters)
    
    print("\n\n")
    pprint(sorted_bigrams)
    
